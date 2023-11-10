import csv

def spelling_bee(allowed_letters,required_letters = [], minimum_lenth = 0, score_mode = False):
    file = open('C:\\Users\\andrz\\OneDrive\\Desktop\\code\\SpellingBee\\test.csv')
    csvreader = csv.reader(file)

    header = []
    header = next(csvreader)
    #print(header)
    rows = []

    for row in csvreader:
        rows.append(row)

    words = []
    for i in rows:
        words.append(i[0])

    for i in range(len(words)):
        words[i-1] = words[i-1].lower()
    special_charecters = [' ','-','/']

    words2 = []
    for i in range(len(words)):
        Test = True
        for j in special_charecters:
            for k in range(len(words[i-1])):
                if j == words[i-1][k-1]:
                    Test = False
        if Test == True:
            words2.append(words[i-1])
    words = words2
    candidate_words = []
    for i in range(len(words)):
        for j in required_letters:
            for k in range(len(words[i-1])):
                if j == words[i-1][k-1]:
                    candidate_words.append(words[i - 1])
    candidate_words2 = candidate_words
    candidate_words = []
    for i in range(len(required_letters)):
        allowed_letters.append(required_letters[i-1])

    for i in range(len(candidate_words2)):
        T = True
        for k in range(len(candidate_words2[i-1])):
            if candidate_words2[i-1][k-1] not in allowed_letters:
                T = False
        if T == True:
            candidate_words.append(candidate_words2[i-1])

    if minimum_lenth != 0:
        candidate_words2 = candidate_words
        candidate_words = []
        for i in candidate_words2:
            if len(i) >= minimum_lenth:
                candidate_words.append(i)

    candidate_words2 = candidate_words
    candidate_words = []
    for i in candidate_words2:
        if i not in candidate_words:
            candidate_words.append(i)


    candidate_words.sort()

    for word in candidate_words:
        print(word)

    print("This program has found", len(candidate_words),"words that fulfill your requirements.")

    if score_mode == True:
        score = 0
        for i in candidate_words:
            test = []
            if len(i) == minimum_lenth:
                score += 1
            else:
                score += len(i)
            if len(i) >= len(allowed_letters):
                for j in allowed_letters:
                    if j in i:
                        test.append("yes")
                if len(test) == len(allowed_letters):
                    score += 15

        print("This program has generated a score of", score,".")





spelling_bee(['e','l','o','i','m','k'], ['b'], 4, True)
