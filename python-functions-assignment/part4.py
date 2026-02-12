def name_fn(name):
    message = f"Hello, {name}"
    return message

def score(student_score):
    count = len(student_score)
    avgerage = sum(student_score)/count
    return count,avgerage

def student_result(average):
    if average >= 50:
        return "Pass"
    return "Fail"
def main():
    student_name = "Abhineet"
    student_score = [20,55,73]
    
    greeting = name_fn(student_name)
    student_subject, student_avg = score(student_score)
    student_res = student_result(student_avg)

    print(greeting)
    print(f"Subject:{student_subject}")
    print(f"Score:{student_avg:.1f}")
    print(f"Result:{student_res}")
main()