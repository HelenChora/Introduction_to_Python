def read_scores(filename):
    scores = []

    try:
        with open(filename, "r") as file:
            for line in file:
                try:
                    name, score = line.strip().split(",")
                    score = int(score)
                    scores.append(score)

                except ValueError:
                    print("Skipped line:", line.strip())

        if len(scores) > 0:
            average = sum(scores) / len(scores)
            print("Average:", average)
        else:
            print("No valid scores")

    except FileNotFoundError:
        print("File not found")


read_scores("scores.txt")