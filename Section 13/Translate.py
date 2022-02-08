from translate import Translator
translaor = Translator(to_lang="de")
with open('english.txt', mode='r') as file:
    text = file.read()
    translation = translaor.translate(text)
    with open('german.txt', mode='w') as my_file:
        my_file.write(translation)
print(translation)