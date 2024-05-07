from midiutil import MIDIFile
from random import randint

class PitchLession(MIDIFile):
    def __init__(self,
        note: int,
        distance: int,
        output_file: str,
        track = 0,
        channel = 0,
        time = 0, 
        duration = 1,
        tempo = 100,
        volume = 100,
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
        self.addTempo(self.track, self.time, self.tempo)

        self.addNote(self.track, self.channel, self.note, time*4, self.duration, self.volume)
        self.addNote(self.track, self.channel, self.note + self.distance, time*4+1, self.duration, self.volume)

        with open(output_file, 'wb') as file:
            self.writeFile(file)
    