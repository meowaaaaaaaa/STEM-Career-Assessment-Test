# STEM Career Assessment Test System

class STEMCareerAssessment:
    def __init__(self):
        self.courses = {
            'Biology': ['Biologist', 'Biochemist', 'Pharmacologist'],
            'Physics': ['Physicist', 'Astronomer', 'Engineer'],
            'Mathematics': ['Statistician', 'Data Scientist', 'Actuary'],
            'Computer Science': ['Software Developer', 'Data Analyst', 'Systems Architect']
        }
        self.scores = {}
        self.questions = []

    def categorize_courses(self):
        return self.courses

    def add_question(self, question, options):
        self.questions.append({'question': question, 'options': options})

    def calculate_score(self, answers):
        self.scores = {key: 0 for key in self.courses.keys()}
        for answer in answers:
            if answer['course'] in self.scores:
                self.scores[answer['course']] += answer['score']
        return self.scores

    def display_results(self):
        print("Assessment Results:")
        for course, score in self.scores.items():
            print(f"{course}: {score}")

# Example usage
assessment = STEMCareerAssessment()

# Categorizing courses
print(assessment.categorize_courses())

# Adding questions
assessment.add_question('What do you enjoy most?', ['Solving problems', 'Conducting experiments', 'Analyzing data'])

# Simulated answers
answers = [
    {'course': 'Mathematics', 'score': 5},
    {'course': 'Biology', 'score': 3},
]

# Calculating score
final_scores = assessment.calculate_score(answers)
assessment.display_results()

