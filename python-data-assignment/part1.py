scores = [72, 85, 90, 45, 82, 66, 78, 94]
length = len(scores)
score1 = scores [0:3]
score2 = scores [(length-3):]
print(f"Full List: {scores}")
print(f"First 3 marks: {score1}")
print(f"Last 3 marks: {score2}")
Highest = max(scores)
print(f"Highest: {Highest}")
Lowest = min(scores)
print(f"Lowest: {Lowest}")
Average = sum(scores)/length
print(F"Average:{Average}")