def word_counter(filename):
    with open(filename, "r") as file:
        text = file.read().lower()

    words = text.split()

    counter = {}
    for word in words:
        word = word.strip(".,!?")
        counter[word] = counter.get(word, 0) + 1

    sorted_words = sorted(counter.items(), key=lambda x: x[1], reverse=True)

    for word, count in sorted_words[:10]:
        print(word, count)


word_counter("text.txt")