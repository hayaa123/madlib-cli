
def read_template(path):

    with open(path) as file :
        content =file.read()
        
    return content

def parse_template (string):

    words = []
    temp_word = ""
    parsed_text = ""
    is_reached = False
    for letter in string:
        if  letter == "{" :
            parsed_text +=letter      
            is_reached  = True
        
        elif letter == "}" :
            words.append(temp_word)
            parsed_text+=letter
            is_reached= False
            temp_word =""

        elif is_reached == True :
            temp_word += letter
        else :
            parsed_text+=letter
    return words, parsed_text

def user_inputs (words):
    
    print("welcome to madlib game :D ")
    print("you are requierd to fill the following question and see the surprise ^^")

    for i,value in enumerate(words) :
        
        words[i] = input(f"{value} ")

    return words
        

def merge_function (string , words):
    
    return string.format(*words)

def save_on_file (text):
    with open("new_file.txt", "x") as f:
        f.write(text)

if __name__ == "__main__":

    content = read_template("madlib_cli/assets/game.txt")
    words,parsed_text = parse_template(content)
    words = user_inputs(words)
    merged_text = merge_function(parsed_text,words)
    print(merged_text)
    save_on_file(merged_text)
