#  importing file 
from Data import data
from random import Random
random = Random()
class Model:
    def __init__(self,data):
        self.data = data
        self.question = []
        self.answers = []
        self.corr_ans = []
        self.options = ['a', 'b', 'c', 'd']
        self.get_question()
        self.get_answer()
        self.question_ans = self.question_ans_shuffled()

    def get_question (self):
        for item in self.data['results']:
            self.question.append(item['question'])

    def get_answer(self):
        for item in self.data['results']:
            correct_ans = item['correct_answer']
            incorrect_ans = item['incorrect_answers']
            incorrect_ans.append(correct_ans)
            random.shuffle(incorrect_ans)
            self.answers.append(incorrect_ans)
            self.corr_ans.append(correct_ans)
    
    def question_ans_shuffled(self):
        question_answer = []
        for items in zip(self.question, self.answers, self.corr_ans):
            question_answer.append(items)
        random.shuffle(question_answer)
        return question_answer

    def check_answer(self, answer:str, corr_ans:str|int) -> bool:
        if answer == corr_ans:
            return True
        else: 
            return False
            

DataObj = Model(data)
option = DataObj.options
# question = DataObj.question_ans
# total  = len(question)
# score = 0
# for i in range(len(question)):
#     print(f'Q{i + 1}: {question[i][0]}')
#     for w in range(len(question[i][1])):
#         print(f'{option[w]}) {question[i][1][w]}.')
    
#     ans = option.index(input('Ans: ').lower()) 
#     userAns = question[i][1][ans]

#     if DataObj.check_answer(userAns, question[i][2]):
#         print('correct!')
#         score += 1
#     else:
#         print('incorrect')

#     print('')

# print(f'you Got {score}/{total}.')
