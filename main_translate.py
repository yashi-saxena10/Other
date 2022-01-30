from translate import Translator

to_langg=input('enter target language: ')

translator= Translator(from_lang="english", to_lang=to_langg)

text=input('enter text: ')

translation=translator.translate(text)

print('translated: ', translation)