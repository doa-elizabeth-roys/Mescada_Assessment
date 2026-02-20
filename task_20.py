#PSEUDOCODE

# function english_to_pigLatin(sentence):
    # Split the sentence into words → word_list
    # Create an empty list → pig_latin_list

    # For each word in word_list:
    #     Remove the first letter 
    #     Take the rest of the word 
    #     New word = rest_of_word + first_letter + "ay"
    #     Append new word to pig_latin_list

    # Join all words in pig_latin_list with spaces → pig_latin_sentence
    # Return pig_latin_sentence



# # function pigLatin_to_english(pig_latin_sentence):
#     Split pig_latin_sentence into words → pigLatin_list
#     Create empty list → english_list

#     For each word in word_list:
#         Remove last two characters ("ay") 
#         Slice the last character of word stored as first_letter
#         The remaining characters = rest_of_word
#         Original word = first_letter + rest_of_word
#         Append original word to english_list

#     Join english_list with spaces  
#     Return english_sentence
# End Function