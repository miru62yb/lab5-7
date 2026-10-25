text = input('Введите текст: ')
raw_words = text.split()
matched_words = []
for raw_word in raw_words:
    cleaned_word = raw_word.strip(".,!?;:").lower()
    if cleaned_word and cleaned_word.startswith('а'):
        matched_words.append(cleaned_word)
if matched_words:
    for word in matched_words:
        print(word)
    print(len(matched_words))
else:
    print("Нет совпадений")
    print(0)