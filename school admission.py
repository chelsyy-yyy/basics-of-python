admitted_students = {}
def school_admission_profile(full_name, age, email, grade):
 if grade in ['A', 'B', 'C']:
    print(f"Congratulations {full_name}, you have been admitted to our school")
    profile ={
        'name': full_name,
        'age': age,
        'email':email,
        'grade':grade
    }
    admitted_students[full_name] = profile
    return profile
 else:
    print(f"Sorry {full_name}, you are not eligible for admission")
user_input = input("Enter your full name, age, email and grade separated by commas: ")
print(user_input)
full_name, age, email, grade = user_input.split(',')
grade = grade.strip()
school_admission_profile(full_name, age, email, grade)

