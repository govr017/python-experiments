from tokenize import String
from pydub import AudioSegment
audList = []
print('Input the files you want to connect type "stickstop" when you want to stop' )
x = "deez"
while x != "stickstop":
    x = input()
    audList.append(x)
    print(audList)
audList.pop(-1)
output = AudioSegment.from_wav(audList[0])
print(audList)
for aud in audList[1:]:
    output = output + AudioSegment.from_wav(aud)
    print(aud)
print("Where do you want to save the file?")
direction = input()
output.export(direction + "sticked.wav", format="wav")