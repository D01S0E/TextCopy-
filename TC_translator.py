import clipboard
from googletrans import Translator

translator = Translator()

while True :
    if input() : continue
    copytext = clipboard.paste()
    result = translator.translate(copytext, dest='ko')
    print("{0} : {1}".format(copytext, result.text))

# Enter로 번역 결과 확인, Ctrl+C로 프로그램 종료