from translate import Translator

translator = Translator(to_lang='es')

try:
    with open('C:/Users/DIVERGENT/Desktop/text.txt') as my_file:
        text = (my_file.read())
        translation = translator.translate(text)
        print(translation)
    with open('C:/Users/DIVERGENT/Desktop/trans.txt', mode='w') as my_file2:
        my_file2.write(translation)
except FileNotFoundError as e:
    print('check file path')
