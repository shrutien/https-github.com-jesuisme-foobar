from foobar import FoobarClass
import csv
from math import sqrt
import unittest


class FoobarChild(FoobarClass):
    def __init__(self):
        """
        Initialize the class
        :param name: The class name
        :param code_map: A dictionary that specifies how the card labels should be converted to letters
        :param answer: The correct ordering of cards (by their label) translated into a string according to the code map
        :param max_score: The highest possible score
        :param card_labels: List of cards from list
        :param student_list: Contains Whole list
        :param email_list: Contains list of emails
        :param scores : Contains the scores of each student

        """
        self.name = "FoobarChild"
        self.code_map = {'A1': 'a', 'A2': 'b', 'A3': 'c', 'A4': 'd', 'A5': 'e', 'A6': 'f', 'A7': 'g'}
        self.answer = 'abcdefg'
        self.max_score = 28
        self.card_labels = []
        self.student_list = []
        self.email_list = []
        self.scores = []

    def read_data(self):
        """               To Read score in CSV file and split the list into two

               """
        try:
            with open('student_responses.csv') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                for row in readCSV:
                    self.student_list.append(row)
                    length = len(self.student_list)

                    # To Remove Duplicates from list
                '''unique = []
                for item in new_list:
                    if sorted(item) not in unique:
                        unique.append(sorted(item))

                print("Uniqueee",unique)'''

                ''' duplicate = set()
                                print("Duplicate", duplicate)
                                # result = []
                                for item in self.student_list:
                                    # print("Item Given In Email: ", item)
                                    if item not in duplicate:
                                        duplicate.add(item)
                                        # print("Duplicate Values", duplicate, "Item in Duplicate", item)
                                        self.result.append(item)
                                print("Duplicate removed", self.result)'''

                for i in range(len(self.student_list)):
                    student = self.student_list[i]
                    # print("Student", student)
                    student_length = len(student) - 1
                    list2 = []

                    for index, item in enumerate(student):

                        if index < student_length:

                            list2.append(student[index])

                        else:
                            self.email_list.append(student[index])
                    self.card_labels.append(list2)

        except Exception as e:
            print("Exception", e)

        else:
            print("Card Labels are      ", self.card_labels)
            print("Email    ", self.email_list)

    def compute_score(self):
        """               To Calculate Student score

                       """
        try:
            student_scores = []
            for card_label in self.card_labels:
                transformstring = self.transform_card_order_to_string(card_label)
                incorrectdata = self.levenshtein_score(transformstring)
                correctdata = len(self.code_map) - incorrectdata
                total = (correctdata * 4) - (incorrectdata * 2)
                student_scores.append(total)

        except ArithmeticError as err:
            print("Arithmetic Error", err)

        else:
            self.scores = student_scores
            print("Scores", self.scores)

    def write_student_scores(self):
        """               To write result in CSV file

                       """

        try:
            with open('studentresults.csv', 'w', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)

                row = 0

                # To sort the score from highest to lowest
                '''self.scores.sort(reverse=True)
                print("Sorted In reverse",self.scores)'''

                for data in self.scores:
                    percent = (data / self.max_score) * 100
                    spamwriter.writerow([self.email_list[row]] + [str(data)] + [str(percent)])
                    row += 1
        except Exception as e:
            print("Exception in write Students", e)

    def standard_deviation(self):
        """               To Calculate the Average and Standard Deviation

                            """
        try:
            length_items = len(self.scores)
            average = sum(self.scores) / length_items
            print("Average Value", average)
            differences = [x - average for x in self.scores]
            sq_differences = [d ** 2 for d in differences]
            ssd = sum(sq_differences)
            variance = ssd / (length_items - 1)
            sd = sqrt(variance)
            print("Standard Deviation", sd)

        except ArithmeticError as error:
            print("Exception in Standard Deviation", error)


childobject = FoobarChild()
childobject.read_data()
childobject.compute_score()
childobject.write_student_scores()
childobject.standard_deviation()
