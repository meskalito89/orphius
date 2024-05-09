from PitchLession import PitchLession
from midi2audio import FluidSynth
import pydub
import tempfile
import wave
from pdb import set_trace
import random

REPEAT = 2
SOUND_FONT = 'sound_fonts/Yamaha_C3_Grand_Piano.sf2'
MIN_NOTE = 60
MAX_NOTE = 80
MAX_DISTANCE = 12
COUNT_OF_LESSIONS = 10

ANSWERS = [
    'answers/0.wav',
    'answers/1.wav',
    'answers/2.wav',
    'answers/3.wav',
    'answers/4.wav',
    'answers/5.wav',
    'answers/6.wav',
    'answers/7.wav',
    'answers/8.wav',
    'answers/9.wav',
    'answers/10.wav',
    'answers/11.wav',
    'answers/12.wav',
]



def main():
    distance1 = random.randint(0, 13)
    distance_is_greather_then_0 = random.choice([-1, 1])
    distance2 = distance1 * distance_is_greather_then_0

    # with tempfile.NamedTemporaryFile('b+w') as notes_file, tempfile.NamedTemporaryFile('ba') as result:
    with open('result.wav', 'ba') as result:
        for i in range(COUNT_OF_LESSIONS):
            set_trace() #TODO перезаписывает файл на каждой итерации
            l = PitchLession(note=60, distance=distance2, repeat=2)
            l.to_wav(SOUND_FONT, result.name)
            seq = pydub.AudioSegment.from_wav(result.name)
            seq2 = pydub.AudioSegment.from_wav(ANSWERS[distance1])
            r = seq.append(seq2)
            r.export(result.name, format='wav')
        
            # with tempfile.NamedTemporaryFile('b+w') as wav_file:
            #     l.to_wav('sound_fonts/Yamaha_C3_Grand_Piano.sf2', wav_file.name)
        

if __name__ == "__main__":
    main()