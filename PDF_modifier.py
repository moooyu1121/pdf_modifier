# -*- coding: utf-8 -*-

# copy&paste from PDF

# This function removes "new lines" and begins on a new line by "period"
# Then, copy&paste the output to DeepL or something to translate smoothly

def PDF_modify(input_str):
    output = input_str.replace('\n', ' ')
    output = output.replace(". ", ".\n")
    return output

# =============================================================================
print("""this function removes disturbing "new line" and ready your document to translate by translate application such as DeepL""" + "\n")
print("copy & @ paste from your document below" + "\n")
input_str = input()
output = PDF_modify(input_str)
print("=============================================================================")
print(output)
