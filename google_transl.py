import googletrans

translator = Translator()

print(googletrans.LANGUAGES)

text = print(input('Enter your text '))

srct = translator.detect(text)

print('Language detected ',dec)

destt = print(input('Enter the language as per the printed languages '))

translated = translator.translate(text,src=srct,dest=dest)

print(traslated.text)


