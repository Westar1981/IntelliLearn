
import random

class InteractiveQuiz:
    def __init__(self):
        self.question_bank = self._load_question_bank()

    def _load_question_bank(self):
        # Placeholder for loading questions from a database or file
        question_bank = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
            {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
            {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"], "answer": "Harper Lee"},
        ]
        return question_bank

    def get_random_question(self):
        return random.choice(self.question_bank)

    def check_answer(self, question, selected_option):
        for q in self.question_bank:
            if q["question"] == question:
                return q["answer"] == selected_option
        return False

    def get_feedback(self, question, selected_option):
        if self.check_answer(question, selected_option):
            return "Correct!"
        else:
            return f"Incorrect. The correct answer is {self._get_correct_answer(question)}."

    def _get_correct_answer(self, question):
        for q in self.question_bank:
            if q["question"] == question:
                return q["answer"]
        return None
