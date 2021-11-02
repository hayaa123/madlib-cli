import re
from typing import Pattern
def read_template(path):

    with open(path) as file :
        content =file.read()
        
    return content

def parse_template (string):

    words = []
    temp_word = ""
    is_reached = False
    for letter in string:
        if  letter == "{" : 
            is_reached  = True
        
        elif letter == "}" :
            words.append(temp_word)
            is_reached= False
            temp_word =""

        elif is_reached == True :
            temp_word += letter
    return words

def user_inputs (words):
    
    print("welcome to madlib game :D ")
    print("you are requierd to fill the following question and see the surprise ^^")

    for i,value in enumerate(words) :
        
        words[i] = input(f"{value} ")

    return words
        

def merge_function (string , words):
    template_words = parse_template(string)
    user_words = words

    for (temp,user) in zip(template_words,user_words):
        
        string= string.replace(f"{{{temp}}}",user,1)

    return string

if __name__ == "__main__":

    content = read_template("madlib_cli/assets/game.txt")
    words = parse_template(content)
    words = user_inputs(words)
    print(merge_function(content,words))

