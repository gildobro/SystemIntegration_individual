#Gil Dobrovinsky gilx0029 08/26/22
import os
import sys

breakline = "\n\n\n"

#Parse .txt
print(breakline, "Parsing .txt File\n")
with open(os.path.join(sys.path[0], "message.txt"), "r") as f:
    newline_break = ""
    for readline in f:
        line_strip = readline.strip()
        newline_break += line_strip
    print(newline_break)


print(breakline, "Parsing .csv File\n")

#Parse .csv
with open(os.path.join(sys.path[0], "aboutme.csv"), "r") as f:
    newline_break = ""
    for readline in f:
        line_strip = readline.strip()
        newline_break += line_strip
    print(newline_break)

print(breakline, "Parsing .json File\n")


#Parse .json
with open(os.path.join(sys.path[0], "aboutme.json"), "r") as f:
    newline_break = ""
    for readline in f:
        line_strip = readline.strip()
        newline_break += line_strip
    print(newline_break)

print(breakline)