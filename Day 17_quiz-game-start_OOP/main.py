from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for i in range(len(question_data)):
    ques_var = question_data[i]['text']
    answer_var = question_data[i]['answer']

    question_bank.append(Question(ques_var,answer_var))


#print(question_bank[0].answer)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz \nYour final score was: {quiz.score}/{quiz.question_number}")


