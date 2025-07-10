
print("Enter your text (press Enter twice to finish):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

text = "\n".join(lines)

num_lines = len(lines)
num_words = len(text.split())
num_chars = len(text)

print("\n--- Analysis ---")
print(f"Number of lines: {num_lines}")
print(f"Number of words: {num_words}")
print(f"Number of characters: {num_chars}")
