
from flask import Flask, request, render_template, redirect, url_for
from adaptive_learning_path import AdaptiveLearningPath
from interactive_quiz import InteractiveQuiz

app = Flask(__name__)

# Initialize the learning path and quiz
student_id = "student_123"
learning_path = AdaptiveLearningPath(student_id)
quiz = InteractiveQuiz()

@app.route('/')
def index():
    return render_template('index.html', learning_path=learning_path.get_learning_path())

@app.route('/quiz', methods=['GET', 'POST'])
def quiz_page():
    if request.method == 'POST':
        question = request.form['question']
        selected_option = request.form['selected_option']
        feedback = quiz.get_feedback(question, selected_option)
        if feedback == "Correct!":
            learning_path.update_learning_path("Introduction to Python", "completed")
        return render_template('result.html', feedback=feedback, learning_path=learning_path.get_learning_path())
    else:
        question = quiz.get_random_question()
        return render_template('quiz.html', question=question)

@app.route('/save')
def save_learning_path():
    learning_path.save_learning_path("learning_path.json")
    return redirect(url_for('index'))

@app.route('/load')
def load_learning_path():
    learning_path.load_learning_path("learning_path.json")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
