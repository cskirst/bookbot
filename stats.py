def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def character_count(text: str) -> dict:
    char_count = {}
    for char in text:
        char = char.lower()
        if char_count.get(char):
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_characters(d: dict) -> list:
    sorted_items =[]
    for key, value in d.items():
        sorted_items.append({"char": key, "num": value})
    sorted_items.sort(key=lambda x: x["num"], reverse=True)
    return sorted_items
