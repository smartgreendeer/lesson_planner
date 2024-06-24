import sys
import yaml
import asyncio
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
import aiofiles
import PyPDF2

# Download NLTK resources (uncomment if not downloaded)
# nltk.download('punkt')
# nltk.download('stopwords')

# Initialize NLTK components
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

# Function to preprocess text asynchronously
async def preprocess_text(text):
    # Tokenize text into sentences and words
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    # Remove stop words and punctuation, and perform stemming
    cleaned_words = [ps.stem(w.lower()) for w in words if w.isalnum() and w.lower() not in stop_words]

    return cleaned_words

# Function to extract text from PDF file asynchronously
async def extract_text_from_pdf(file_path):
    try:
        async with aiofiles.open(file_path, "rb") as file:
            pdf_reader = PyPDF2.PdfFileReader(await file.read())
            num_pages = pdf_reader.numPages
            text = ""
            for page_num in range(num_pages):
                page = pdf_reader.getPage(page_num)
                text += page.extractText()
        return text
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

async def generate_lesson_plan(text):
    # Extract headings using regular expressions
    import re
    headings = re.findall(r'\n([A-Za-z0-9 ]+)\n', text)

    # Initialize lesson plan structure
    lesson_plan = {
        "Introduction": "Introduction to the topic",
        "Units": []
    }
    
    current_unit = None
    current_subtopics = []

    # analyze data based on the extracted data
    for heading in headings:
        # Check if the heading is likely a main unit 
        if any(keyword in heading.lower() for keyword in ["unit", "chapter", "section", "lesson", "topic"]):
            if current_unit is not None:
                lesson_plan["Units"].append({
                    "Unit": current_unit,
                    "Subtopics": current_subtopics,
                    "Key Concepts": []
                })
                
            
            current_unit = heading.strip()
            current_subtopics = []
            
       
        else:
            current_subtopics.append(heading.strip())

    # Append the last detected unit and its subtopics
    if current_unit is not None:
        lesson_plan["Units"].append({
            "Unit": current_unit,
            "Subtopics": current_subtopics,
            "Key Concepts": []
        })

   
    for unit_data in lesson_plan["Units"]:
        unit_text = ""
        for page_num in range(len(text)):
            if unit_data["Unit"] in text[page_num]:
                unit_text += text[page_num]

        # preprocess text for the unit
        cleaned_words = preprocess_text(unit_text)

        # Analyze word frequency distribution
        freq_dist = FreqDist(cleaned_words)

        # Extract key concepts based on frequency or specific keywords

        key_concepts = []
        for word, freq in freq_dist.most_common(10): 
            if len(word) > 1:  
                key_concepts.append(word)
        
        unit_data["Key Concepts"] = key_concepts

    return lesson_plan



async def handle_step(step, inputs):
    if step == 'Upload_or_Paste_Text':
        if inputs['type'] == 'File_Upload':
            file_path = inputs['file_path']
            if file_path.endswith('.pdf'):
                text = await extract_text_from_pdf(file_path)
            else:
                print(f"Error: Unsupported file format for '{file_path}'. Please upload a PDF file.")
                return None
        elif inputs['type'] == 'Text_Input':
            text = inputs['text']
        else:
            print("Error: Invalid input type.")
            return None

        return await preprocess_text(text)

    elif step == 'Text_Preprocessing':
        
        return inputs['processed_text']

    elif step == 'Generate_Lesson_Plan':
        return await generate_lesson_plan(inputs['processed_text'])

    elif step == 'Display_Output':
        print("Generated Lesson Plan:")
        print("=====================")
        print(inputs['generated_lesson_plan'])
        return None

    else:
        print(f"Error: Unknown step '{step}'.")
        return None

async def execute_flow(flow):
    for step_info in flow['application_flow']:
        step = step_info['step']
        print(f"Executing step: {step}")

        if 'inputs' in step_info:
            inputs = {}
            for input_info in step_info['inputs']:
                input_type = input_info['type']
                if input_type == 'File_Upload':
                    file_path = input_info['description']
                    inputs['type'] = 'File_Upload'
                    inputs['file_path'] = file_path
                elif input_type == 'Text_Input':
                    text = input_info['description']
                    inputs['type'] = 'Text_Input'
                    inputs['text'] = text
                else:
                    print(f"Error: Unknown input type '{input_type}'")
                    return

            processed_data = await handle_step(step, inputs)

            if processed_data is None:
                print(f"Step '{step}' failed.")
                break

            step_info['outputs'][0]['description'] = processed_data

        else:
            print("Error: Step information incomplete.")
            break

        if 'outputs' in step_info:
            outputs = step_info['outputs']
            if len(outputs) > 0:
                output_description = outputs[0]['description']
                if output_description:
                    print(f"Output of step '{step}': {output_description}")

        print()

def main():
    if len(sys.argv) < 2:
        print("Usage: python lesson_plan_generator_async.py <flow_yaml_file>")
        return
    
    flow_yaml_file = sys.argv[1]

    try:
        with open(flow_yaml_file, 'r') as file:
            flow = yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: File '{flow_yaml_file}' not found.")
        return
    except yaml.YAMLError as exc:
        print(f"Error in YAML file: {exc}")
        return

    asyncio.run(execute_flow(flow))

if __name__ == "__main__":
    main()
