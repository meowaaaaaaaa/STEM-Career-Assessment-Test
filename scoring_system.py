# Scoring System for STEM Career Assessment Test

# Mapping of STEM fields with their subcategories and assigned point values.
scoring_system = {
    'Biological Sciences': {
        'Biotechnology': 10,
        'Ecology': 8,
        'Genetics': 9,
        'Zoology': 7
    },
    'Physical Sciences': {
        'Physics': 10,
        'Chemistry': 9,
        'Earth Science': 8,
        'Astronomy': 7
    },
    'Engineering': {
        'Mechanical Engineering': 10,
        'Civil Engineering': 10,
        'Electrical Engineering': 9,
        'Aerospace Engineering': 8,
    },
    'Mathematics': {
        'Pure Mathematics': 10,
        'Applied Mathematics': 9,
        'Statistics': 8,
        'Computational Mathematics': 7
    },
    'Computer Science': {
        'Software Development': 10,
        'Data Science': 9,
        'Artificial Intelligence': 10,
        'Cybersecurity': 9
    },
    'Chemistry': {
        'Analytical Chemistry': 9,
        'Inorganic Chemistry': 8,
        'Organic Chemistry': 10,
        'Physical Chemistry': 9
    },
    'Geosciences': {
        'Geology': 10,
        'Meteorology': 8,
        'Oceanography': 9,
        'Environmental Science': 9
    },
    'Health Sciences': {
        'Medicine': 10,
        'Nursing': 9,
        'Pharmacy': 9,
        'Dentistry': 8
    },
    'Interdisciplinary STEM': {
        'Biostatistics': 8,
        'Environmental Engineering': 9,
        'Robotics': 10,
        'Nanotechnology': 9
    }
}

# A function to calculate the total score based on answers provided

def calculate_score(answers):
    total_score = 0
    for field, subcategory in answers.items():
        if field in scoring_system and subcategory in scoring_system[field]:
            total_score += scoring_system[field][subcategory]
    return total_score

# Example Usage:
# answers = {
#     'Biological Sciences': 'Biotechnology',
#     'Engineering': 'Civil Engineering',
#     'Computer Science': 'Data Science'
# }
# print('Total Score:', calculate_score(answers))