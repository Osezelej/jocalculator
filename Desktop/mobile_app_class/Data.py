from random import Random
data = {"results": [{"question": "How many officially recognized dwarf planets in the solar system are named after Polynesian deities?",
                                         "correct_answer": "2", "incorrect_answers": ["0", "1", "5"]},
                                        {
                                         "question": "A comet gaseous envelope (which creates the tail) is called what?",
                                         "correct_answer": "The coma",
                                         "incorrect_answers": ["The wake", "The backwash", "The ablative"]},
                                        {"category": "Science & Nature", "type": "multiple", "difficulty": "medium",
                                         "question": "Which of these elements on the Periodic Table is a Noble Gas?",
                                         "correct_answer": "Neon",
                                         "incorrect_answers": ["Potassium", "Iodine", "Colbalt"]},
                                        {"category": "Science & Nature", "type": "multiple", "difficulty": "hard",
                                         "question": "What nucleotide pairs with guanine?",
                                         "correct_answer": "Cytosine",
                                         "incorrect_answers": ["Thymine", "Adenine", "Uracil"]},
                                        {"category": "Science & Nature", "type": "boolean", "difficulty": "hard",
                                         "question": "The value of one Calorie is different than the value of one calorie.",
                                         "correct_answer": "True", "incorrect_answers": ["False"]},
                                        {"category": "Science & Nature", "type": "multiple", "difficulty": "hard",
                                         "question": "The Western Lowland Gorilla is scientifically know as?",
                                         "correct_answer": "Gorilla Gorilla Gorilla",
                                         "incorrect_answers": ["Gorilla Gorilla Diehli", "Gorilla Beringei Graueri",
                                                               "Gorilla Beringei Beringei"]},
                                        {"category": "Science & Nature", "type": "multiple", "difficulty": "easy",
                                         "question": "Which noble gas has the lowest atomic number?",
                                         "correct_answer": "Helium", "incorrect_answers": ["Neon", "Argon", "Krypton"]},
                                        {"category": "Science & Nature", "type": "multiple", "difficulty": "hard",
                                         "question": "What was the first organic compound to be synthesized from inorganic compounds?",
                                         "correct_answer": "Urea",
                                         "incorrect_answers": ["Propane", "Ethanol", "Formaldehyde"]},
                                        {"category": "Science & Nature", "type": "multiple", "difficulty": "hard",
                                         "question": "What is the most potent toxin known?",
                                         "correct_answer": "Botulinum toxin",
                                         "incorrect_answers": ["Ricin", "Cyanide", "Asbestos"]},
                                        {"category": "Science & Nature", "type": "multiple", "difficulty": "hard",
                                         "question": "How many types of quarks are there in the standard model of physics?",
                                         "correct_answer": "6", "incorrect_answers": ["2", "3", "4"]}]}

rand = Random()
rand.shuffle(data['results'])
result = data["results"]
question_list = [item['question'] for item in data["results"]]
print('')
print('')