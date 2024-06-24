import gradio as gr
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
import asyncio
import PyPDF2

# download nltkeverytime the app runs
nltk.download('punkt')
nltk.download('stopwords')

# initialize nltk 
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

# this is a functionto preprocess the data that has been inputted
def preprocess_text(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    # Remove stop words and punctuation
    cleaned_words = [ps.stem(w.lower()) for w in words if w.isalnum() and w.lower() not in stop_words]

    return cleaned_words

# this is a function to extract text to pdf
async def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    num_pages = len(pdf_reader.pages)
    text = ""
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

# function to generate lesson plan
async def generate_lesson_plan(text):
    import re
    headings = re.findall(r'\n([A-Za-z0-9 ]+)\n', text)

    # Initialize lesson plan structure
    lesson_plan = {
        "Introduction": "Introduction to the topic",
        "Units": []
    }
    
    current_unit = None
    current_subtopics = []

    # Analyze sections based on extracted headings
    for heading in headings:
        # Check if the heading is below the sentences stated below
        if any(keyword in heading.lower() for keyword in ["unit", "chapter", "section", "lesson", "topic"]):
            if current_unit is not None:
                lesson_plan["Units"].append({
                    "Unit": current_unit,
                    "Subtopics": current_subtopics,
                    "Key Concepts": []
                })
                
            # Update current unit
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

    # analyze content basedonthe data that yoyu have been given
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

# Async function to handle file upload and processing
async def text_to_lesson_plan(input_file):
    pdf_text = await extract_text_from_pdf(input_file)
    return await generate_lesson_plan(pdf_text)

inputs = [
    gr.File(label="Upload PDF file"),
]

iface = gr.Interface(
    fn=text_to_lesson_plan,
    inputs=inputs,
    outputs=gr.JSON(),
    title="John Lesson Plan Generator",
    description="Generate a structured lesson plan from PDF file.",
)

# Launch Gradio interface asynchronously
async def main():
    await iface.launch()

# Run the asyncio event loop
if __name__ == "__main__":
    asyncio.run(main())
