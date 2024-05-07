from midiutil import MIDIFile

#NOTES = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']

class PitchLession(MIDIFile):
    def __init__(self,
        track = 0,
        channel = 0,
        time = 0, 
        duration = 1,
        tempo = 120,
        volume = 100,
    ):
        super().__init__(1)
        self.track = track
        self.channel = channel
        self.time = time
        self.duration = duration
        self.tempo = tempo
        self.volume = volume

        self.addTempo(self.track, self.time, self.tempo)
        for time, pitch in enumerate(range(60, 100)):
            self.addNote(self.track, self.channel, pitch, time*4, self.duration, self.volume)
        with open('test2.mid', 'wb') as file:
            self.writeFile(file)