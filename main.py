

def read_file_content(filename):
    # [assignment] Add your code here 
     with open(filename) as story:
           storyTold = story.read()    
           story.close()
     return storyTold

read_file_content("/home/user/Desktop/helloWorld/Reading-Text-Files/readingTextFiles/story.txt")


def count_words():
    text = read_file_content("/home/user/Desktop/helloWorld/Reading-Text-Files/readingTextFiles/story.txt")
    textList =  text.split(" ")

    textDict ={}
    for i in textList:
                  textDict[i] = textList.count(i)

    return textDict
   

print(count_words())