print("PROGRAM STARTED")

def spam_detector(message, spam_words):
    message_lower = message.lower()
    found_spam_words = []

    for word in spam_words:
        if word in message_lower:
            found_spam_words.append(word)

    is_spam = len(found_spam_words) > 0
    return is_spam, found_spam_words


print("Task 3: Spam Detector")

message = "you are winning a free prize now!"
spam_list = ["win", "cash", "free"]

result, words = spam_detector(message, spam_list)

print("Message:", message)
print("Is Spam:", result)
print("Spam Words Found:", words)
