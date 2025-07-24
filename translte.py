from deep_translator import GoogleTranslator

try:
    with open('to_translat.txt', mode = 'r') as my_file:
        translated = GoogleTranslator(source='auto', target='de').translate(my_file.read())
    with open('translated.txt', mode = 'w') as my_file2:
        my_file2.write(translated)
except  FileNotFoundError as err:
    print('file not found or you dont have the permitions')

