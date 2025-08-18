with open("input.txt" ,"r") as file:
    content = file.read()
    print(content)

word_count = len(content.split())
content_upper = content.upper()
with open("output.txt", "w") as file:
    file.write(content_upper + "\n")
    file.write(f"\nWord count: {word_count}\n")

print("Success. Output.txt has beeen created.")