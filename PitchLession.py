from midiutil import MIDIFile
from midi2audio import FluidSynth
from random import randint
import tempfile

class PitchLession(MIDIFile):
    def __init__(self,
        sound_font,
        note: int,
        distance: int,
        # output_file: str,
        track = 0,
        channel = 0,
        time = 0, 
        duration = 1,
        tempo = 100,
        volume = 120,
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
        self.sound_font = sound_font

        for i in range(self.repeat):
            self.addNote(self.track, self.channel, self.note, i*2+1, self.duration, self.volume)
            self.addNote(self.track, self.channel, self.note + self.distance, i*2+2, self.duration, self.volume)

        
    def to_wav(self, output_file: str):
        '''Сохранить в wav формате'''
        fs = FluidSynth(self.sound_font)
        with tempfile.NamedTemporaryFile('b+w') as midi_file:
            self.writeFile(midi_file)
            midi_file.seek(0)
            fs.midi_to_audio(midi_file.file.name, output_file)

    def to_temporary_file(self):
        '''saves to temporary file'''
        file = tempfile.NamedTemporaryFile('b+w')
        self.to_wav(file.name)
        return file

