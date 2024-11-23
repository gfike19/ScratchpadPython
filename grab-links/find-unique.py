import re

# Set to store unique matches
unique_texts = set()

# Regex pattern to match text between "/" and ":"
pattern = r'\/([^:]+):'

# Open the file and loop through each line
with open('all-list-items.txt', 'r') as file:
    for line in file:
        matches = re.findall(pattern, line)
        unique_texts.update(matches)

# Display unique matches
for text in unique_texts:
    print(text)
