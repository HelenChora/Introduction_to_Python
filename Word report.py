with open("text.txt", "r") as f:
    text = f.read()

text = text.lower()

for p in ".,!?":
    text= text.replace(p, "")

words= text.split()

word_count={}

for word in words:
    if word in word_count:
        word_count[word] +=1
    else:
        word_count[word] =1

with open("report.txt", "w") as f:
    f.write(f"Words: {len(words)}\n")
    f.write(f"Unique: {len(word_count)}\n")

 
    for word in sorted(word_count):
        f.write(f"{word:<10} {word_count[word]}\n")

print("Report created successfully!")            