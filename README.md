#create a virtua environment not required
python -m venv lesson_env

#activate the virtual environment
lesson_env\Scripts\activate


#install required libraries for the project to run
pip install -r requirements.txt

#see results inthe terminal
python leson_plan_generator.py


#run the app
python lesson_plan_gradio.py


Project Documentation Template
Project Title: Lesson-Plan Generator
________________________________________
Table of Contents

________________________________________
Introduction
The project is mainly about helping the user to plan for their lesson to boost productivity. This helps the planner to save time and schedule their time well and avoid deadlines and being in trouble in case of exam. As my favorite quote goes him who fails to plan is planning to fail so this helps the user not to fail. If it’s a teacher the cause their textbook to plan for their classes and get to know what they will be teaching in classes.
Problem Statement
My project is used to solve the problem of failing and being behind schedule in Kenya schools some teachers fail to finish the syllabus early this me will help them to plan very well for their lesson. For students in the higher education as this will help them generate a good study plan and get enough time to do various stuff.________________________________________
Solution Overview 
The main features of the project is that you can upload a pdf and from that your lessons are planned based on the, main topics and units in the story helping you to save and get to understand what you are learning or teaching.
Target Audience
My target audience are the teachers and my fellow students. Anyone can us the project of main. The students require to have a good study plan that will help achieve whatever they require to achieve thus this will give them a good way to plan out the subject that they require to study.
________________________________________
Project Setup
Prerequisites
The required libraries are:
1.	The project runs on python version of 3.8 and above
2.	Install the requirements which have been stated in the requirements.txt and they include
I.	Gradio
II.	Asyncio
III.	PyPDF2
IV.	Nltk
Installation
To install the app please follow the following steps step by step to get access
First you should visit my repos and clone the farm project repo
# Clone the repository
Git clone https://github.com/smartgreendeer/lesson_planner

Change the location to where you have stored the repo using the function below
# Navigate to the project directory
cd lesson_planner

Create a virtual environment to prevent interfering with your python software
Python -m venv lesson_env

Next activate the virtual environment
lesson_env\Scripts\activate

 
Next you have to install all the dependencies and libraries required for the project to run smoothly (in case of any error install the libraries step by step)
# Install dependencies
Pip install -r requirements.txt

Running the Project
In order to run the project 
Go to you environment in the terminal and key in the following 
Python lesson_plan_gradio.py 
this will run the app and it will appear as a web server as it has used Gradio UI interface
In case you want to see the functionality you can run 
Python lesson_plan_generator.py 
This will run in the terminal

________________________________________
Flow Design
Flow Diagram
%3CmxGraphModel%3E%3Croot%3E%3CmxCell%20id%3D%220%22%2F%3E%3CmxCell%20id%3D%221%22%20parent%3D%220%22%2F%3E%3CmxCell%20id%3D%222%22%20value%3D%22START%22%20style%3D%22ellipse%3BwhiteSpace%3Dwrap%3Bhtml%3D1%3B%22%20vertex%3D%221%22%20parent%3D%221%22%3E%3CmxGeometry%20x%3D%22156%22%20y%3D%22-206%22%20width%3D%2280%22%20height%3D%2232%22%20as%3D%22geometry%22%2F%3E%3C%2FmxCell%3E%3CmxCell%20id%3D%223%22%20value%3D%22%22%20style%3D%22shape%3Dstencil(lVbLUsMwDPyaXDWWbPlxhvIfzNDSDKVl2vL6e2QySSq3EcPNcbKxV7sru%2FN3p%2B3j27ojdzofDy%2Frz%2F7pvO38fUfU77frY3%2BWUedXnb%2FbHI7r5%2BPhff80PL891i%2Fr6PXwUf%2FwNeByASwVRe57mPERAv3OPAyAXb%2B%2FAJQIFBQgyIw3AAVSVgBOkJIJCKwAsUAOBoCBNIeMgMYKWTZAClAccF4GpASsSZcEriwDIkPWK6Bz4Nwygn1bJqmDM4QIBLEBBCBeBngPsSlTBDRYk5RJs04M0agrMYSklfOQ0VwBnfYGQrY4ULtCQHCGN%2Bpr1P4mYEsHHL02AuomjRVmihOAgQ3ScxEvVkiGmapMTUbFLFbkJiNMVaLR8UuRc9qubAt34eZJajaVq4HRdq2higZAIqnLVGNrsK6hjzoQDN6QurYVrVxtPcaW%2BCoQc3O77b4r5YrdLKX5el2luUEvAsp%2FABTBaW9kEc4gjbGtUnaAltJA2hlJQmvI4Ns%2BJolyxv%2FFF5oASyc0CFw5VXqC2ZTAaRt5NPlGiDo7hKbt0I%2FlmM4GGk%2BL2xuiNp1iIoOA7Lfo5NhN9fok%2BfOoYmy%2BT0oAGcwXjk2%2F2w33lcv37QVFpobLjV%2F9AA%3D%3D)%3BlineShape%3D1%3BstrokeColor%3Ddefault%3B%22%20vertex%3D%221%22%20parent%3D%221%22%3E%3CmxGeometry%20x%3D%22230.551263526428%22%20y%3D%22-20.450479815204062%22%20width%3D%223.2230755116522687%22%20height%3D%223.2248481794399595%22%20as%3D%22geometry%22%2F%3E%3C%2FmxCell%3E%3CmxCell%20id%3D%224%22%20value%3D%22%22%20style%3D%22edgeStyle%3Dnone%3BorthogonalLoop%3D1%3BjettySize%3Dauto%3Bhtml%3D1%3Bshape%3DflexArrow%3Brounded%3D1%3BstartSize%3D8%3BendSize%3D8%3BfontSize%3D12%3Bcurved%3D1%3B%22%20edge%3D%221%22%20parent%3D%221%22%3E%3CmxGeometry%20width%3D%22140%22%20relative%3D%221%22%20as%3D%22geometry%22%3E%3CmxPoint%20x%3D%22192%22%20y%3D%22-174%22%20as%3D%22sourcePoint%22%2F%3E%3CmxPoint%20x%3D%22190%22%20y%3D%22-123%22%20as%3D%22targetPoint%22%2F%3E%3CArray%20as%3D%22points%22%2F%3E%3C%2FmxGeometry%3E%3C%2FmxCell%3E%3CmxCell%20id%3D%225%22%20value%3D%22FILE_UPLOAD%22%20style%3D%22rounded%3D0%3BwhiteSpace%3Dwrap%3Bhtml%3D1%3B%22%20vertex%3D%221%22%20parent%3D%221%22%3E%3CmxGeometry%20x%3D%22114%22%20y%3D%22-127%22%20width%3D%22160%22%20height%3D%2235%22%20as%3D%22geometry%22%2F%3E%3C%2FmxCell%3E%3CmxCell%20id%3D%226%22%20value%3D%22%22%20style%3D%22edgeStyle%3Dnone%3BorthogonalLoop%3D1%3BjettySize%3Dauto%3Bhtml%3D1%3Bshape%3DflexArrow%3Brounded%3D1%3BstartSize%3D8%3BendSize%3D8%3BfontSize%3D12%3Bcurved%3D1%3BexitX%3D0.5%3BexitY%3D1%3BexitDx%3D0%3BexitDy%3D0%3BentryX%3D0.431%3BentryY%3D0.029%3BentryDx%3D0%3BentryDy%3D0%3BentryPerimeter%3D0%3B%22%20edge%3D%221%22%20source%3D%2215%22%20target%3D%227%22%20parent%3D%221%22%3E%3CmxGeometry%20width%3D%22140%22%20relative%3D%221%22%20as%3D%22geometry%22%3E%3CmxPoint%20x%3D%22273%22%20y%3D%22-105%22%20as%3D%22sourcePoint%22%2F%3E%3CmxPoint%20x%3D%22352%22%20y%3D%22-109%22%20as%3D%22targetPoint%22%2F%3E%3CArray%20as%3D%22points%22%2F%3E%3C%2FmxGeometry%3E%3C%2FmxCell%3E%3CmxCell%20id%3D%227%22%20value%3D%22%26lt%3Bdiv%20style%3D%26quot%3Bcolor%3A%20rgb(212%2C%20212%2C%20212)%3B%20background-color%3A%20rgb(30%2C%2030%2C%2030)%3B%20font-family%3A%20Consolas%2C%20%26amp%3Bquot%3BCourier%20New%26amp%3Bquot%3B%2C%20monospace%3B%20font-size%3A%2014px%3B%20line-height%3A%2019px%3B%20white-space%3A%20pre%3B%26quot%3B%26gt%3B%26lt%3Bspan%20style%3D%26quot%3Bcolor%3A%20%23ce9178%3B%26quot%3B%26gt%3BText_Preprocessing%26lt%3B%2Fspan%26gt%3B%26lt%3B%2Fdiv%26gt%3B%22%20style%3D%22rounded%3D0%3BwhiteSpace%3Dwrap%3Bhtml%3D1%3B%22%20vertex%3D%221%22%20parent%3D%221%22%3E%3CmxGeometry%20x%3D%22120%22%20y%3D%22303%22%20width%3D%22160%22%20height%3D%2234%22%20as%3D%22geometry%22%2F%3E%3C%2FmxCell%3E%3CmxCell%20id%3D%228%22%20value%3D%22%26lt%3Bdiv%20style%3D%26quot%3Bcolor%3A%20rgb(212%2C%20212%2C%20212)%3B%20background-color%3A%20rgb(30%2C%2030%2C%2030)%3B%20font-family%3A%20Consolas%2C%20%26amp%3Bquot%3BCourier%20New%26amp%3Bquot%3B%2C%20monospace%3B%20font-size%3A%2014px%3B%20line-height%3A%2019px%3B%20white-space%3A%20pre%3B%26quot%3B%26gt%3B%26lt%3Bspan%20style%3D%26quot%3Bcolor%3A%20%23ce9178%3B%26quot%3B%26gt%3BGenerate_Lesson_Plan%26lt%3B%2Fspan%26gt%3B%26lt%3B%2Fdiv%26gt%3B%22%20style%3D%22whiteSpace%3Dwrap%3Bhtml%3D1%3B%22%20vertex%3D%221%22%20parent%3D%221%22%3E%3CmxGeometry%20x%3D%22116%22%20y%3D%22514%22%20width%3D%22152%22%20height%3D%2241%22%20as%3D%22geometry%22%2F%3E%3C%2FmxCell%3E%3CmxCell%20id%3D%229%22%20value%3D%22%22%20style%3D%22edgeStyle%3Dnone%3BorthogonalLoop%3D1%3BjettySize%3Dauto%3Bhtml%3D1%3Bshape%3DflexArrow%3Brounded%3D1%3BstartSize%3D8%3BendSize%3D8%3BfontSize%3D12%3Bcurved%3D1%3BexitX%3D0.5%3BexitY%3D1%3BexitDx%3D0%3BexitDy%3D0%3B%22%20edge%3D%221%22%20source%3D%227%22%20parent%3D%221%22%3E%3CmxGeometry%20width%3D%22140%22%20relative%3D%221%22%20as%3D%22geometry%22%3E%3CmxPoint%20x%3D%22133%22%20y%3D%22205%22%20as%3D%22sourcePoint%22%2F%3E%3CmxPoint%20x%3D%22198%22%20y%3D%22405%22%20as%3D%22targetPoint%22%2F%3E%3CArray%20as%3D%22points%22%2F%3E%3C%2FmxGeometry%3E%3C%2FmxCell%3E%3CmxCell%20id%3D%2210%22%20value%3D%22PREPROCESSED%20DATA%22%20style%3D%22shape%3Dparallelogram%3Bperimeter%3DparallelogramPerimeter%3BwhiteSpace%3Dwrap%3Bhtml%3D1%3BfixedSize%3D1%3B%22%20vertex%3D%221%22%20parent%3D%221%22%3E%3CmxGeometry%20x%3D%22128.5%22%20y%3D%22407%22%20width%3D%22120%22%20height%3D%2260%22%20as%3D%22geometry%22%2F%3E%3C%2FmxCell%3E%3CmxCell%20id%3D%2211%22%20value%3D%22OUTPUT%3D%7BJSON.FILE%7D%22%20style%3D%22shape%3Dparallelogram%3Bperimeter%3DparallelogramPerimeter%3BwhiteSpace%3Dwrap%3Bhtml%3D1%3BfixedSize%3D1%3B%22%20vertex%3D%221%22%20parent%3D%221%22%3E%3CmxGeometry%20x%3D%22129%22%20y%3D%22699%22%20width%3D%22145%22%20height%3D%2257%22%20as%3D%22geometry%22%2F%3E%3C%2FmxCell%3E%3CmxCell%20id%3D%2212%22%20value%3D%22%22%20style%3D%22edgeStyle%3Dnone%3BorthogonalLoop%3D1%3BjettySize%3Dauto%3Bhtml%3D1%3Bshape%3DflexArrow%3Brounded%3D1%3BstartSize%3D8%3BendSize%3D8%3BfontSize%3D12%3Bcurved%3D1%3BentryX%3D0.5%3BentryY%3D0%3BentryDx%3D0%3BentryDy%3D0%3BexitX%3D0.5%3BexitY%3D1%3BexitDx%3D0%3BexitDy%3D0%3B%22%20edge%3D%221%22%20source%3D%2218%22%20target%3D%2211%22%20parent%3D%221%22%3E%3CmxGeometry%20width%3D%22140%22%20relative%3D%221%22%20as%3D%22geometry%22%3E%3CmxPoint%20x%3D%22170%22%20y%3D%22635%22%20as%3D%22sourcePoint%22%2F%3E%3CmxPoint%20x%3D%22256%22%20y%3D%22205%22%20as%3D%22targetPoint%22%2F%3E%3CArray%20as%3D%22points%22%2F%3E%3C%2Fmx Geometry%3E%3C%2FmxCell%3E%3CmxCell%20id%3D%2213%22%20style%3D%22edgeStyle%3Dnone%3Bcurved%3D1%3Brounded%3D0%3BorthogonalLoop%3D1%3BjettySize%3Dauto%3Bhtml%3D1%3BexitX%3D0%3BexitY%3D0.25%3BexitDx%3D0%3BexitDy%3D0%3BfontSize%3D12%3BstartSize%3D8%3BendSize%3D8%3B%22%20edge%3D%221%22%20source%3D%2211%22%20target%3D%2211%22%20parent%3D%221%22%3E%3CmxGeometry%20relative%3D%221%22%20as%3D%22geometry%22%2F%3E%3C%2FmxCell%3E%3CmxCell%20id%3D%2214%22%20value%3D%22%22%20style%3D%22edgeStyle%3Dnone%3Bcurved%3D1%3Brounded%3D0%3BorthogonalLoop%3D1%3BjettySize%3Dauto%3Bhtml%3D1%3BfontSize%3D12%3BstartSize%3D8%3BendSize%3D8%3B%22%20edge%3D%221%22%20source%3D%2215%22%20target%3D%225%22%20parent%3D%221%22%3E%3CmxGeometry%20relative%3D%221%22%20as%3D%22geometry%22%2F%3E%3C%2FmxCell%3E%3CmxCell%20id%3D%2215%22%20value%3D%22INPUT%20PDF%20FILE%22%20style%3D%22rhombus%3BwhiteSpace%3Dwrap%3Bhtml%3D1%3B%22%20vertex%3D%221%22%20parent%3D%221%22%3E%3CmxGeometry%20x%3D%22103%22%20y%3D%22-8%22%20width%3D%22171%22%20height%3D%22162%22%20as%3D%22geometry%22%2F%3E%3C%2FmxCell%3E%3CmxCell%20id%3D%2216%22%20value%3D%22%22%20style%3D%22edgeStyle%3Dnone%3BorthogonalLoop%3D1%3BjettySize%3Dauto%3Bhtml%3D1%3Bshape%3DflexArrow%3Brounded%3D1%3BstartSize%3D8%3BendSize%3D8%3BfontSize%3D12%3Bcurved%3D1%3BexitX%3D0.5%3BexitY%3D1%3BexitDx%3D0%3BexitDy%3D0%3B%22%20edge%3D%221%22%20source%3D%225%22%20parent%3D%221%22%3E%3CmxGeometry%20width%3D%22140%22%20relative%3D%221%22%20as%3D%22geometry%22%3E%3CmxPoint%20x%3D%22160%22%20y%3D%22205%22%20as%3D%22sourcePoint%22%2F%3E%3CmxPoint%20x%3D%22191%22%20y%3D%22-6%22%20as%3D%22targetPoint%22%2F%3E%3CArray%20as%3D%22points%22%2F%3E%3C%2FmxGeometry%3E%3C%2FmxCell%3E%3CmxCell%20id%3D%2217%22%20value%3D%22%22%20style%3D%22edgeStyle%3Dnone%3BorthogonalLoop%3D1%3BjettySize%3Dauto%3Bhtml%3D1%3Bshape%3DflexArrow%3Brounded%3D1%3BstartSize%3D8%3BendSize%3D8%3BfontSize%3D12%3Bcurved%3D1%3BexitX%3D0.5%3BexitY%3D1%3BexitDx%3D0%3BexitDy%3D0%3BentryX%3D0.461%3BentryY%3D0.024%3BentryDx%3D0%3BentryDy%3D0%3BentryPerimeter%3D0%3B%22%20edge%3D%221%22%20source%3D%2210%22%20target%3D%228%22%20parent%3D%221%22%3E%3CmxGeometry%20width%3D%22140%22%20relative%3D%221%22%20as%3D%22geometry%22%3E%3CmxPoint%20x%3D%22-2%22%20y%3D%22239%22%20as%3D%22sourcePoint%22%2F%3E%3CmxPoint%20x%3D%22138%22%20y%3D%22239%22%20as%3D%22targetPoint%22%2F%3E%3CArray%20as%3D%22points%22%2F%3E%3C%2FmxGeometry%3E%3C%2FmxCell%3E%3CmxCell%20id%3D%2218%22%20value%3D%22LESSON%20PLAN%22%20style%3D%22rounded%3D0%3BwhiteSpace%3Dwrap%3Bhtml%3D1%3B%22%20vertex%3D%221%22%20parent%3D%221%22%3E%3CmxGeometry%20x%3D%22120%22%20y%3D%22593%22%20width%3D%22160%22%20height%3D%2239%22%20as%3D%22geometry%22%2F%3E%3C%2FmxCell%3E%3CmxCell%20id%3D%2219%22%20value%3D%22%22%20style%3D%22edgeStyle%3Dnone%3BorthogonalLoop%3D1%3BjettySize%3Dauto%3Bhtml%3D1%3Bshape%3DflexArrow%3Brounded%3D1%3BstartSize%3D8%3BendSize%3D8%3BfontSize%3D12%3Bcurved%3D1%3BexitX%3D0.461%3BexitY%3D1.195%3BexitDx%3D0%3BexitDy%3D0%3BexitPerimeter%3D0%3BentryX%3D0.425%3BentryY%3D0.154%3BentryDx%3D0%3BentryDy%3D0%3BentryPerimeter%3D0%3B%22%20edge%3D%221%22%20source%3D%228%22%20target%3D%2218%22%20parent%3D%221%22%3E%3CmxGeometry%20width%3D%22140%22%20relative%3D%221%22%20as%3D%22geometry%22%3E%3CmxPoint%20x%3D%2213%22%20y%3D%22463%22%20as%3D%22sourcePoint%22%2F%3E%3CmxPoint%20x%3D%22153%22%20y%3D%22463%22%20as%3D%22targetPoint%22%2F%3E%3CArray%20as%3D%22points%22%2F%3E%3C%2FmxGeometry%3E%3C%2FmxCell%3E%3CmxCell%20id%3D%2220%22%20value%3D%22%22%20style%3D%22edgeStyle%3Dnone%3BorthogonalLoop%3D1%3BjettySize%3Dauto%3Bhtml%3D1%3Bshape%3DflexArrow%3Brounded%3D1%3BstartSize%3D8%3BendSize%3D8%3BfontSize%3D12%3Bcurved%3D1%3B%22%20edge%3D%221%22%20source%3D%2211%22%20parent%3D%221%22%3E%3CmxGeometry%20width%3D%22140%22%20relative%3D%221%22%20as%3D%22geometry%22%3E%3CmxPoint%20x%3D%2213%22%20y%3D%22572%22%20as%3D%22sourcePoint%22%2F%3E%3CmxPoint%20x%3D%22202%22%20y%3D%22816%22%20as%3D%22targetPoint%22%2F%3E%3CArray%20as%3D%22points%22%2F%3E%3C%2FmxGeometry%3E%3C%2FmxCell%3E%3CmxCell%20id%3D%2221%22%20value%3D%22STOP%22%20style%3D%22ellipse%3BwhiteSpace%3Dwrap%3Bhtml%3D1%3B%22%20vertex%3D%221%22%20parent%3D%221%22%3E%3CmxGeometry%20x%3D%22152%22%20y%3D%22813%22%20width%3D%22124%22%20height%3D%2238%22%20as%3D%22geometry%22%2F%3E%3C%2FmxCell%3E%3C%2Froot%3E%3C%2FmxGraphModel%3E
Flow Description
The first step is whereby the user input their location or a location they require, here you will be prompted to input the city name cause that is the get functionality of the api were are using this will prevent the user from getting errors
Next step is where by it gets a response which we got the action from the weather.py file this will give us the response from the API about the weather of that location (city) that the user had input
________________________________________
Custom Action
Description
My action is to get the weather information of a certain area thus helping which is an action from the main file this will give a response based on that
Code
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    num_pages = len(pdf_reader.pages)
    text = ""
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

The logic for this action is to extract data from the pdf file that has been uploaded by the user and giving out the text to be used to plan and schedule your lesson
Integration
The flow of the project contains different flows that depend on each other. The action for the first code is to upload a file this helps the user when he or she wants to upload a file.
 
________________________________________
User Interface
UI Design
The design of my user interface is the y using the gradio default template.
The submit button submits whatever the user input in the text area 
The clear button erases every information from the text area and output area thus
The flag button acts as our save button which saves whatever the app has displayed on the output area for future references for the user
 
Gradio Implementation
I used Gradio to create the interface by creating buttons and areas to input text and out text required by the user 

import gradio as gr
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
import asyncio
import PyPDF2

# Download NLTK resources (uncomment if not downloaded)
nltk.download('punkt')
nltk.download('stopwords')

# Initialize NLTK components
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

# Function to preprocess text
def preprocess_text(text):
    # Tokenize text into sentences and words
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    # Remove stop words and punctuation, and perform stemming
    cleaned_words = [ps.stem(w.lower()) for w in words if w.isalnum() and w.lower() not in stop_words]

    return cleaned_words

# Async function to extract text from PDF file
async def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    num_pages = len(pdf_reader.pages)
    text = ""
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

# Async function to generate lesson plan
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

    # Analyze sections based on extracted headings
    for heading in headings:
        # Check if the heading is likely a main unit (e.g., Chapter, Unit, Section)
        if any(keyword in heading.lower() for keyword in ["unit", "chapter", "section", "lesson", "topic"]):
            # Save previous unit and subtopics
            if current_unit is not None:
                lesson_plan["Units"].append({
                    "Unit": current_unit,
                    "Subtopics": current_subtopics,
                    "Key Concepts": []
                })
                
            # Update current unit
            current_unit = heading.strip()
            current_subtopics = []
            
        # All other headings are treated as subtopics under the current unit
        else:
            current_subtopics.append(heading.strip())

    # Append the last detected unit and its subtopics
    if current_unit is not None:
        lesson_plan["Units"].append({
            "Unit": current_unit,
            "Subtopics": current_subtopics,
            "Key Concepts": []
        })

    # Analyze content under each unit to extract key concepts
    for unit_data in lesson_plan["Units"]:
        unit_text = ""
        for page_num in range(len(text)):
            if unit_data["Unit"] in text[page_num]:
                unit_text += text[page_num]

        # Tokenize and preprocess text for the unit
        cleaned_words = preprocess_text(unit_text)

        # Analyze word frequency distribution
        freq_dist = FreqDist(cleaned_words)

        # Extract key concepts based on frequency or specific keywords
        # Here, we will extract the most frequent meaningful words or phrases
        key_concepts = []
        for word, freq in freq_dist.most_common(10):  # Adjust number based on content size
            if len(word) > 1:  # Filter out very short words (adjustable threshold)
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




________________________________________
How to Use
To run the project follow the step by step instructions to run it
Step 1: Start the Application
1.	Run the application using the command provide above ensure it’s in your terminal
2.	You can use the ctrl+click to open the url or follow the statement below 
3.	Open your web browser and navigate to the local host URL (usually http://localhost:7861/).
4.	 
Step 2: Interact with the UI
1.	Upload the pdf that you want it to be Click the submit button to run the flow or just click the enter button.
2.	View the output results in the output area 
3.	 
Step 3: Understanding the Output
1.	The output above is injsonformat that contains the lessonpplanwhich divides into sections the main part which contains the keyconcepts ,the unitsor subtopics and many nmore. 

Use Cases
My project can be used by a user who wants to get the planandschedule their study classes therefore helping them to study everything
________________________________________
Demo Video
This is the link for my demo video of my app in action
https://youtu.be/KpxtI8JlI4g________________________________________
Conclusion
My project is based on the user’s ability to upload a pdf and use it to schedule and plan their day.
I got to understand how to integrate the gradio user interface and how to use asyncflows in my project.
________________________________________
Future Work
I plan to add the llama language model to help in planning the work easier and help analyze and summarize the work easier 
I also plan to add a feature whereby you not  only upload a pdf but also a txt file that will help the user in future to plan their work more easily________________________________________
References
ChatGpt
Asyncflows.com
Gradio.app
________________________________________



