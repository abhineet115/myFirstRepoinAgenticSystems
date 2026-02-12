def calculate_average(scores):
    return sum(scores) / len(scores)
def status(roles):
    return "admin" in roles

def main():
    data = [
        {
        "name": "Abhineet",
        "scores": [85, 90, 78],
        "roles": {"admin"}
    },
    {
        "name": "Prachi",
        "scores": [88, 76, 92],
        "roles": {"viewer"}
    },
    {
        "name": "Amit",
        "scores": [70, 80, 75],
        "roles": {"editor"}
    },
    {
        "name": "Neha",
        "scores": [95, 89, 93],
        "roles": {"admin"}
    }
    ]
    for user in data:
        avg = calculate_average(user["scores"])
        print("Name:", user["name"])
        print(f"Average Scores: {avg:.1f}")
        if "admin" in user["roles"]:
            print("Admin Access: Yes\n")
        else:
            print("Admin Access: No\n")
main()
