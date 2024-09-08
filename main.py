def main():
    path = 'books/frankenstein.txt'
    text = getContents(path)
    loweredText = toLowerCase(text)

    wordCount = countWords(loweredText)

    characterDict = countCharacters(loweredText)
    characterList = convertToList(characterDict)
    characterList.sort(reverse=True, key=sort_on)
    printReport(path, wordCount, characterList)
    

def getContents(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def countWords(content):
    words = content.split()
    return len(words)

def toLowerCase(text):
    return text.lower()
    
def countCharacters(text):
    character_dictionary = {}
    for c in text:
        if c.isalpha():
            if c in character_dictionary:
                character_dictionary[c] += 1
            else: 
                character_dictionary[c] = 1
    return character_dictionary

def convertToList(dictionary):
    character_list = []
    for key,value in dictionary.items():
        new_dictionary = {'character': key, 'num': value}
        character_list.append(new_dictionary)
    return character_list

def sort_on(dict):
    return dict["num"]

def printReport(path, wordCount, characterList):
    print(f"--- Begin report of {path} ---")
    print(f"{wordCount} words found in the document")

    for item in characterList:
        print(f"The '{item['character']}' character was found {item['num']} times")
    
    print(f"--- End report ---")

main()