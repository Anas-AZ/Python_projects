from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    q_text = data["question"]
    q_ans = data["correct_answer"]
    question_bank.append(Question(q_text, q_ans))  # appends question objects to a list

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.get_question()

print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
