import json
import requests

handle_names = json.load(open('users.json'))
problem_names = json.load(open('problems.json'))
problems_solved = []
problems_solved_by_user = []

for handles in handle_names:
    name = handles["name"]
    req_json = requests.get(f'http://codeforces.com/api/user.status?handle={name}').json()
    if req_json["status"] == "OK":
        req_json = req_json["result"]
        for problem_tried in req_json:
            problem_act = problem_tried["problem"]
            identifier = str(problem_act["contestId"]) + str(problem_act["index"])
            for problem_contest in problem_names:
                if identifier == problem_contest:
                    problems_solved.append(identifier)
                    problems_solved_by_user.append((identifier, name))

unique_problems_solved_by_user = set(problems_solved_by_user)
unique_problems_solved = set(problems_solved)

print("Problems Solved:")
for problem in unique_problems_solved:
    print(f"{problem}")
print("-------------------------")

for problem, user in unique_problems_solved_by_user:
    print(f"Problem {problem} was tried by {user}")

