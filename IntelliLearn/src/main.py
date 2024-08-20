
from adaptive_learning_path import AdaptiveLearningPath
from interactive_quiz import InteractiveQuiz

def main():
    student_id = "student_123"
    learning_path = AdaptiveLearningPath(student_id)
    
    # Initial assessment (placeholder results)
    assessment_results = {"math": 80, "science": 70, "literature": 90}
    learning_path.initial_assessment(assessment_results)
    
    print("Initial Learning Path:")
    print(learning_path.get_learning_path())
    
    # Interactive Quiz
    quiz = InteractiveQuiz()
    question = quiz.get_random_question()
    print("\nQuestion:")
    print(question["question"])
    print("Options:", question["options"])
    
    # User input for quiz answer
    selected_option = input("Select an option: ")
    feedback = quiz.get_feedback(question["question"], selected_option)
    print("Feedback:", feedback)
    
    # Update learning path based on quiz result
    if feedback == "Correct!":
        learning_path.update_learning_path("Introduction to Python", "completed")
    
    print("\nUpdated Learning Path:")
    print(learning_path.get_learning_path())
    
    # Save learning path to file
    learning_path.save_learning_path("learning_path.json")
    print("\nLearning path saved to learning_path.json")
    
    # Load learning path from file
    learning_path.load_learning_path("learning_path.json")
    print("\nLearning path loaded from learning_path.json")
    print(learning_path.get_learning_path())

if __name__ == "__main__":
    main()
