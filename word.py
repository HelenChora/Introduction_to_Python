with open("text.txt","r",encoding="utf-8") as f:
    text= f.read().lower()

for p in ".,!?":
    text= text.replace(p,"")

words=text.split()

counts={}

for word in words:
    counts[word]=counts.get(word,0)+1

with open("report.text","w",encoding="utf-8") as out:
    out.write(f"Words: {len(words)}\n")
    out.write(f"Unique:{len(counts)}\n") 

    for word in sorted(counts):
        out.write(f"{word:<15} {counts[word]}\n")   