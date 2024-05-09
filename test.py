from pydub import AudioSegment
from gtts import gTTS

texts = [
    'прима',
    'малая секунда',
    'большая секунда',
    'малая терция',
    'большая терция',
    'чистая кварта',
    'тритон',
    'чистая квинта',
    'малая секста',
    'большая секста',
    'малая септима',
    'большая септима',
    'октава',
]

for i, text in enumerate(texts):
    audio = gTTS(text=text, lang='ru', slow=False)
    audio.save(f'answers/{i}.mp3')

# for i in range(13):
#     sound = AudioSegment.from_mp3(f'answers/{i}.mp3')
#     sound.export(f'answers/{i}.wav', format='wav')
