# fname = input("Enter file name: ")
# fh = open(fname)
# count = 0
# for i in fh:
#     fh.rstrip()
#     if fh.startlinewith("From: "):
#         fh.split()
#         word = fh[1]
#         check = word.split("")
fname = input("Enter file name: ")
fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()  # Remove trailing whitespace/newline
    if line.startswith("From: "):  # Check if the line starts with 'From: '
        words = line.split()  # Split the line into words
        if len(words) > 1:
            email = words[1]  # The email is the second word
            print(email)  # You can print the email or process it
            count += 1

print("There were", count, "lines in the file with From as the first word")
