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
