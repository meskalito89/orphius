from PitchLession import PitchLession
from midi2audio import FluidSynth
import tempfile
import wave
from pdb import set_trace

REPEAT = 2
SOUND_FONT = 'sound_fonts/Yamaha_C3_Grand_Piano.sf2'


# def connect_wav_files(wav_files:list[bytearray]) -> bytearray :
#     HEAD_BYTES_IN_WAV = 0
#     tmp_file = tempfile.TemporaryFile('+ba')
#     for i, file in enumerate(wav_files):
#         file.seek(HEAD_BYTES_IN_WAV)
#         if i == 0:
#            file.seek(0) 
#         tmp_file.write(file.read())
#     tmp_file.seek(0)
#     return tmp_file




# def create_lession():
#     PitchLession(note=60, distance=7, output_file='output.mid')
#     fs = FluidSynth(SOUND_FONT)
#     fs.midi_to_audio("output.mid", 'output.wav')
#     data = []
#     for i in range(REPEAT):
#         with wave.open('output.wav') as w:
#             data.append( [w.getparams(), w.readframes(w.getnframes())] )
#     with wave.open('answers/2.wav') as w:
#         data.append([w.getparams(), w.readframes(w.getnframes())])
#     with wave.open('result.wav', 'wb') as result:
#         result.setparams(data[0][0])
#         for i in range(len(data)):
#             result.writeframes(data[i][1])

# def create_lession():
#     l = PitchLession(note=60, distance=-7)
#     with tempfile.NamedTemporaryFile('b+w') as midi_file, tempfile.NamedTemporaryFile('b+w') as wav_file:
#         l.writeFile(midi_file)
#         midi_file.seek(0)
#         fs = FluidSynth(SOUND_FONT)
#         fs.midi_to_audio(midi_file.name, wav_file.name)
#         with open('output.wav', 'bw') as f:
#             result = connect_wav_files([wav_file, wav_file, wav_file])
#             f.write(result.read())

# create_lession()

def main():
    l = PitchLession(note=60, distance=7, repeat=3)
    l.to_wav('sound_fonts/Yamaha_C3_Grand_Piano.sf2', "output.wav")
    # with tempfile.NamedTemporaryFile('b+w') as wav_file:
    #     l.to_wav('sound_fonts/Yamaha_C3_Grand_Piano.sf2', wav_file.name)
    

if __name__ == "__main__":
    main()