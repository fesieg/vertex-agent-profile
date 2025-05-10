from ..personal_info import NAME, CAREER, INTERESTS, SKILLS

def get_info_on_person():
    """
    This function provides information about the Person and their career, interests, and skills.
    It is designed to be used as a tool in an agent that can answer questions about the person.

    Pick out the most relevant information from the following list
    """
    # information about Person
    person_info = {
        "name": NAME,
        "career": CAREER,
        "interests": INTERESTS,
        "skills": SKILLS
    }
    
    return person_info


