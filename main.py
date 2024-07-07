# Read File
def readBook(path):
    with open(path) as f:
        return f.read()

def countWords(inputString):
    return len(inputString.split())

def countCharacters(inputString):
    characterCount = {}

    for i in range(ord('a'), ord('z') + 1):
        characterCount[chr(i)] = inputString.lower().count(chr(i))

    return characterCount

def dictToListOfDict(dict):
    dictList = []

    for key, value in dict.items():
        temp = {}
        temp["char"] = key
        temp["num"] = value
        dictList.append(temp)
    
    return dictList

def sort_on(dict):
    return dict["num"]

def main():
    path = "books/frankenstein.txt"
    file_contents = readBook("books/frankenstein.txt")
    wordCount = countWords(file_contents)
    characterCount = countCharacters(file_contents)
    characterCountList = dictToListOfDict(characterCount)
    characterCountList.sort(reverse=True, key=sort_on)

    print("--- Begin report of " + path + " ---")
    print(f"{wordCount} words found in the document")
    print("")
    for pair in characterCountList:
        char = pair["char"]
        number = pair["num"]
        print(f"The '{char}' character was found {number} times")
    print("--- End report ---")

main()