from midiutil import MIDIFile
from midi2audio import FluidSynth
from random import randint
import tempfile
from pdb import set_trace

class PitchLession(MIDIFile):
    def __init__(self,
        note: int,
        distance: int,
        # output_file: str,
        track = 0,
        channel = 0,
        time = 0, 
        duration = 1,
        tempo = 100,
        volume = 100,
        repeat = 1,
    ):
        super().__init__(1)
        self.track = track
        self.channel = channel
        self.time = time
        self.duration = duration
        self.tempo = tempo
        self.volume = volume
        self.note = note
        self.distance = distance
        self.repeat = repeat
        self.addTempo(self.track, self.time, self.tempo)

        for i in range(self.repeat):
            self.addNote(self.track, self.channel, self.note, i*2, self.duration, self.volume)
            self.addNote(self.track, self.channel, self.note + self.distance, i*2+1, self.duration, self.volume)

        # with open(output_file, 'wb') as file:
        #     self.writeFile(file)
    
    # def open(self):
    #     self.file = tempfile.NamedTemporaryFile('+wb')
    #     self.writeFile(self.file)
    #     self.file.seek(0)
    #     return self.file
        
    def to_wav(self, sound_font: str, output_file: str):
        fs = FluidSynth(sound_font)
        with tempfile.NamedTemporaryFile('b+w') as midi_file:
            self.writeFile(midi_file)
            midi_file.seek(0)
            fs.midi_to_audio(midi_file.file.name, output_file)



