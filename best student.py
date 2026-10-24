scores = [12, 17, 9, 15, 14]

best = scores[0]
position = 1

for number, score in enumerate(scores, start=1):
    if score > best:
        best = score
        position = number

print(f"Best score: {best}")
print(f"Student number: {position}")
