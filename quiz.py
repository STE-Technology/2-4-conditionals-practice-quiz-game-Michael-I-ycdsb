"""
File: quiz.py
Author: Michael Iacobelli
Date: 2024-03-05
Description: A brief explanation of what this program does.
"""

# defines a class for the quiz
class Quiz():
    # when initalizes defines attributes of score and the list of questions
    def __init__(self, questions_list: list[list[str, str, int]]) -> None:
        self.score = 0
        self.questions_list = questions_list

    # defines the method for asking each question in the question list
    def ask_question(
            self,
            question: str,
            options: list[str],
            correct_option_index: int
    ) -> None:
        print(f'{question}\n')
        
        # prints the multiple choice options
        for index, option in enumerate(options):
            print(f'\t({index + 1}) {option}')
            
            if index == len(options) - 1:
                print('')
        
        # askes for input for users answer
        user_answer = int(input(f'Pick a number between 1-{len(options)}: ')) - 1

        # changes score depending on if correct or not
        if user_answer is correct_option_index:
            print('Correct!')
            self.score += 1
        else:
            print('Incorrect')
    
    # defines the method to run the quiz
    def run(self):
        print('Multiple-Choice Quiz Game\n')

        # calls the ask question method for every question in the list
        for question, options, answer in self.questions_list:
            self.ask_question(question, options, answer)
        
        # prints final score
        print(f'\nQuiz complete!\nYou answered {self.score} out of {len(self.questions_list)} questions correctly.')


# creates the quiz object with all the answers and questions
quiz = Quiz([
    [
        '1. What is the capital of France?',
        ['Paris', 'London', 'Rome'],
        0
    ],
    [
        '2. Which planet is known as the Red Planet?',
        ['Mars', 'Venus', 'Jupiter'],
        0
    ],
    [
        '3. Who painted the Mona Lisa?',
        ['Leonardo da Vinci', 'Pablo Picasso', 'Vincent van Gogh'],
        0
    ],
    [
        '4. What is the capital of Russia?',
        ['Toronto', 'Los Angeles', 'Moscow'],
        2
    ],
    [
        '5. What is the tallest mammal on Earth?',
        ['Elephants', 'Giraffes', 'Whale', 'Tree'],
        1
    ]
    ]
)

# runs the quiz object
quiz.run()