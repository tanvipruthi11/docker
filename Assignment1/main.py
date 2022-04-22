import json
wordExist = False

with open('C:/Users/Tanvi.Pruthi/Downloads/sampleinput.json', 'r') as inputFile:
    inputFileData = json.load(inputFile)
inputFile.close()

jsonOutput = inputFileData['word']
print(jsonOutput)


with open('C:/Users/Tanvi.Pruthi/Downloads/dictionary.txt') as f:
    lines = f.readlines()

for line in lines:
    print(line.split("=")[0])
    if jsonOutput == line.split("=")[0]:
        wordExist = True
wordExist = False
if wordExist:
    with open('C:/Users/Tanvi.Pruthi/Downloads/sampleresponse.json', 'r') as inputFile:
        inputFileData = json.load(inputFile)
        print(json.dumps({"word":jsonOutput, "defination":inputFileData['definition']}))

elif jsonOutput == "":
    print(json.dumps({"word": "nil", "error": "Invalid JSON input."}))

else:
    print(json.dumps({"word": "nil", "error": "Invalid JSON input."}))




