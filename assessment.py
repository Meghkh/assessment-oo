"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Abstraction -

   Encapsulation -

   Polymorphism -

2. What is a class?

3. What is an instance attribute?

4. What is a method?

5. What is an instance in object orientation?

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is an attribute given to an instance of a class


"""


# Parts 2 through 5:
# Create your classes and class methods

# Part 2

class Student(object):
    """A student."""

    def __init__(self, first, last, address):
        """Instantiation of a student."""

        self.first = first
        self.last = last
        self.address = address


class Question(object):
    """A question."""

    def __init__(self, question, answer):
        """Instantiation of a question."""

        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):
        """Print question to console, prompt user for answer, return True or False."""

        print self.question
        user_answer = raw_input("Answer: ")
        if user_answer == self.answer:
            return True
        else:
            return False


class Exam(object):
    """An exam."""

    def __init__(self, name):
        """Instantiation of an exam."""

        self.name = name
        self.questions = []

    def add_question(self, question):
        """Add an instance of Question to an Exam object."""

        self.questions.append(question)

    def administer(self):
        """Administer an instance of an Exam."""

        correct = 0
        num_questions = 0

        for question in self.questions:
            num_questions += 1
            correct_answer = question.ask_and_evaluate()
            if correct_answer:
                correct += 1

        score = (float(correct) / num_questions) * 100
        return score


class StudentExam(object):
    """A student exam."""

    def __init__(self, student, exam):
        """Instantiation of a StudentExam."""

        self.student = student
        self.exam = exam
        self.score = None

    def take_test(self):
        """Administer exam and display score."""

        self.score = self.exam.administer()
        print "Final score: {}".format(self.score)

    def __repr__(self):
        """Return a printable representation of StudentExam."""

        return "<class '__main__.StudentExam'>"


class Quiz(Exam):
    """A quiz."""

    def administer(self):
        """Administer an instance of an Exam."""

        correct = 0
        num_questions = 0

        for question in self.questions:
            num_questions += 1
            correct_answer = question.ask_and_evaluate()
            if correct_answer:
                correct += 1

        score = (float(correct) / num_questions) * 100

        if score < 50:
            return 0
        else:
            return 1

    def __repr__(self):
        """Return a printable representation of StudentExam."""

        return "<class '__main__.Quiz'>"


class StudentQuiz(StudentExam):
    """A student quiz."""

    def take_test(self):
        """Administer quiz and return score"""
        self.score = self.exam.administer()
        if self.score:
            print "You passed!"
        else:
            print "You failed :'("

    def __repr__(self):
        """Return a printable representation of StudentExam."""

        return "<class '__main__.StudentQuiz'>"


def example():
    """Creates exam/quiz, adds questions, creates student,
    Instantiate StudentExam/StudentQuiz, administer exam/quiz"""

    # create exam
    exam = Exam('midterm')

    # add questions to exam
    set_q = Question('What is the method for adding an element to a set?', '.add()')
    exam.add_question(set_q)
    pwd_q = Question('What does pwd stand for?', 'print working directory')
    exam.add_question(pwd_q)
    list_q = Question('Python lists are mutable, iterable, and what?', 'ordered')
    exam.add_question(list_q)

    # create quiz
    quiz = Quiz('quiz')

    # add questions to exam
    quiz.add_question(set_q)
    quiz.add_question(pwd_q)
    quiz.add_question(list_q)

    # create student
    student = Student("meghan", "khurana", "450 Sutter, San Francisco")

    # instantiate a StudentExam, pass student and exam created
    assessment = StudentExam(student, exam)
    quiz_assessment = StudentQuiz(student, quiz)

    # administer test
    assessment.take_test()
    quiz_assessment.take_test()


example()
