# Cleo Tang
# 261070795

import musicalbeeps
import doctest

class Note:
    '''A class contains all information about a single
    music note and operations that can be performed on
    it.
    
    Class Attributes
    * OCTAVE_MIN: int
    * OCTAVE_MAX: int
    
    Instance Attributes
    * duration: float
    * pitch: str
    * octave: int
    * accidental: str
    '''
    
    OCTAVE_MIN = 1
    OCTAVE_MAX = 7
    
    def __init__(self, duration, pitch, octave=1, accidental='natural'):
        '''(float, str, int, str) -> NoneType
        Creates an object of Note Type
        >>> note = Note(1.0, 'C', 4, 'natural')
        >>> note.octave
        4
        >>> note = Note(2.5, 'Z', 3)
        Traceback (most recent call last):
        AssertionError: pitch should be single letter from A to G or R.
        >>> note = Note(2.2, 'A', 8, 'natural')
        Traceback (most recent call last):
        AssertionError: octave should be an integer from 1 to 7.
        '''
        
        if type(duration) != float or duration <=0:
            raise AssertionError('duration should be a positive float.')
        if type(pitch) != str or pitch not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'R']:
            raise AssertionError('pitch should be single letter from A to G or R.')
        if type(octave) != int or octave < self.OCTAVE_MIN or octave > self.OCTAVE_MAX:
            raise AssertionError('octave should be an integer from 1 to 7.')
        if type(accidental) != str or accidental not in ['natural', 'sharp', 'flat']:
            raise AssertionError('invalid accidental value(either natural, sharp or flat).')
        
        self.duration = duration
        self.pitch = pitch
        self.octave = octave
        self.accidental = accidental
    
    def __str__(self):
        '''() -> str
        Takes no explicit inputs, returns a string of the
        format 'DURATION PITCH OCTAVE ACCIDENTAL'
        >>> note = Note(1.5, 'D', 1, 'natural')
        >>> print(note)
        1.5 D 1 natural
        >>> note = Note(2.0, 'E', accidental='sharp')
        >>> print(note)
        2.0 E 1 sharp
        >>> note = Note(1.0, 'R')
        >>> print(note)
        1.0 R 1 natural
        '''
        #if self.pitch == 'R':
            #return str(self.duration) + ' ' + self.pitch
        return str(self.duration) + ' ' + self.pitch + ' ' + str(self.octave) + ' ' + self.accidental
    
    
    def play(self, player_obj):
        '''(Player) -> NoneType
        Takes as explicit input a music player object.
        Constructs and passes the note string with duration
        to the play_note method.
        '''
        
        note_str = self.pitch+str(self.octave)
        if self.accidental == 'sharp':
            note_str += '#'
        elif self.accidental == 'flat':
            note_str += 'b'
        if self.pitch == 'R':
            note_str = 'pause'
        player_obj.play_note(note_str, self.duration)
        
        



if __name__ == '__main__':
    doctest.testmod()


print(str(Note))
