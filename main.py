from PitchLession import PitchLession
from midi2audio import FluidSynth
import wave

REPEAT = 2
SOUND_FONT = 'sound_fonts/Yamaha_C3_Grand_Piano.sf2'

def create_lession():

    PitchLession(note=60, distance=7, output_file='output.mid')
    fs = FluidSynth(SOUND_FONT)
    fs.midi_to_audio("output.mid", 'output.wav')
    data = []

    for i in range(REPEAT):
        with wave.open('output.wav') as w:
            data.append( [w.getparams(), w.readframes(w.getnframes())] )

    with wave.open('result.wav', 'wb') as result:
        result.setparams(data[0][0])
        for i in range(len(data)):
            result.writeframes(data[i][1])

# print(create_lession())


