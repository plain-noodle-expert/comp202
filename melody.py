# Cleo Tang
# 261070795
import doctest
import note
import musicalbeeps


class Melody:
    '''A class stores information about a melody of
    many notes and the operations to perform on them.
    
    Instance Attributes
    * title: str
    * author: str
    * notes: list<Note>
    '''        
        
        
        
    def __init__(self, filename):
        '''(str, list<Note>) -> NoneType
        Takes as explicit input a string of a filename.
        Creates an instance attribute for the title and
        author and an instance attribute notes.
        >>> happy_birthday = Melody('birthday.txt')
        >>> len(happy_birthday.notes)
        25
        >>> happy_birthday.title
        'Happy Birthday'
        >>> hot_cross_buns = Melody('hotcrossbuns.txt')
        >>> str(hot_cross_buns.notes[0]) == str(hot_cross_buns.notes[3])
        True
        >>> twinkle = Melody('twinkle.txt')
        >>> len(twinkle.notes)
        42
        >>> print(twinkle.notes[10])
        0.5 E 4 natural
        '''
        
        song = open(filename,'r')
        content = song.read()
        song.close()
        lines = content.strip().split('\n')
        while lines.count('') != 0:
            lines.remove('')
        #if len(lines) == 0 or len(lines) <= 2:
            #raise AssertionError('invalid song file.')
        # lines is a list of strings of each line in the file: ['Hot Cross Buns', 'Traditional', ...]
        self.title = lines[0]
        self.author = lines[1]        
        
        notes_list = []
        start_repeat = None
        repeated_lines = 0
        for nth_line, line in enumerate(lines[2:]):
            line = line.strip()
            try:
                if line.split()[1] == 'R': # 'R' won't have octave and accidental to unpack
                    duration, pitch, repeat = line.split()
                    single_note_obj = note.Note(float(duration), pitch)
                else:
                    duration, pitch, octave, accidental, repeat = line.split()
                    single_note_obj = note.Note(float(duration), pitch, int(octave), accidental.lower())
            except: #duration is not float or octave is not integer or not correct amount of element to unpack
                raise AssertionError(f'there are invalid line in the song file:line {nth_line} \'{line}\'')
            
            notes_list.append(single_note_obj)
            
            # find the repeated sequence of notes in the notes_list and append them again in order
            if start_repeat == None and repeat == 'true':
                start_repeat = nth_line + repeated_lines
            elif start_repeat != None and repeat == 'true':
                end_repeat = nth_line + repeated_lines + 1
                repeated_lines += end_repeat - start_repeat
                # recreate notes that need to be repeated, so each note object has different id
                for a_note in notes_list[start_repeat:end_repeat]:
                    duration,pitch,octave,accidental=a_note.duration,a_note.pitch,a_note.octave,a_note.accidental
                    notes_list.append(note.Note(duration, pitch, octave, accidental))
                start_repeat = None

        self.notes = notes_list
        

    def play(self, player):
        '''(Play) -> NoneType
        Takes as explicit input a music player object, and calls
        the play method on each Note object of the notes instance
        attribute in order, passing the music player object each
        time as argument.
        '''
        
        for single_note in self.notes:
            single_note.play(player)
        


    def get_total_duration(self):
        '''() -> float
        Takes no inputs and reurns the total duration of
        the song as a float.
        >>> happy_birthday = Melody('birthday.txt')
        >>> happy_birthday.get_total_duration()
        13.0
        >>> twinkle = Melody('twinkle.txt')
        >>> twinkle.get_total_duration()
        24.5
        >>> tetris = Melody('tetris.txt')
        >>> tetris.get_total_duration()
        15.5
        '''
        
        total_duration = 0
        for single_note in self.notes:
            total_duration += single_note.duration
        
        return total_duration
    
    
    def change_octave(self, change):
        ''' () -> bool
        Takes as input a note and a str indicating lowering or
        uppering the octave, reduces or increases the
        octave of a note by 1 and return True. False
        if the octave is OCTAVE_MIN and change is lower,
        or the octave is OCTAVE_MAX and the change is upper.
        >>> happy_birthday = Melody('birthday.txt')
        >>> print(happy_birthday.notes[0])
        0.25 D 4 natural
        >>> happy_birthday.change_octave('lower')
        True
        >>> print(happy_birthday.notes[0])
        0.25 D 3 natural
        >>> happy_birthday.notes[5].octave
        3
        >>> happy_birthday.change_octave('upper')
        True
        >>> print(happy_birthday.notes[5].octave)
        4
        >>> happy_birthday.change_octave('upper')
        True
        >>> happy_birthday.change_octave('upper')
        True
        >>> happy_birthday.change_octave('upper')
        False
        >>> print(happy_birthday.notes[5])
        1.0 F 6 sharp
        '''
        
        for single_note in self.notes:
            if single_note.pitch != 'R':
                if change == 'lower' and single_note.octave == single_note.OCTAVE_MIN:
                    return False
                elif change == 'upper' and single_note.octave == single_note.OCTAVE_MAX:
                    return False
        for single_note in self.notes:
            if single_note.pitch != 'R':
                if change == 'upper':
                    single_note.octave += 1
                elif change == 'lower':
                    single_note.octave -= 1
        return True
        
        
        
        
    def lower_octave(self):
        '''() -> bool
        Takes no explicit input, reduces the octave of all
        notes in a song by 1 and return True. False if the
        octave is 1.
        >>> happy_birthday = Melody('birthday.txt')
        >>> octave_before_lower = happy_birthday.notes[0].octave
        >>> happy_birthday.lower_octave()
        True
        >>> happy_birthday.notes[5].octave
        3
        >>> hot_cross_buns = Melody('hotcrossbuns.txt')
        >>> hot_cross_buns.lower_octave()
        True
        >>> print(hot_cross_buns.notes[0])
        0.5 B 3 natural
        >>> tetris = Melody('tetris.txt')
        >>> tetris.lower_octave()
        True
        >>> print(tetris.notes[1])
        0.25 B 3 natural
        >>> tetris.lower_octave()
        True
        >>> tetris.lower_octave()
        True
        >>> tetris.lower_octave()
        False
        >>> tetris.notes[1].octave
        1
        '''
        
        return self.change_octave('lower')
        

    
    def upper_octave(self):
        '''() -> bool
        Takes no explicit inputs, increases the octave of
        each note in notes by 1 and return True, if octave
        is 7, then does not increase any and returns False.
        >>> happy_birthday = Melody('birthday.txt')
        >>> happy_birthday.upper_octave()
        True
        >>> print(happy_birthday.notes[7])
        0.25 D 5 natural
        >>> hot_cross_buns = Melody('hotcrossbuns.txt')
        >>> hot_cross_buns.upper_octave()
        True
        >>> hot_cross_buns.notes[3].octave
        5
        >>> tetris = Melody('tetris.txt')
        >>> tetris.upper_octave()
        True
        >>> tetris.upper_octave()
        True
        >>> tetris.notes[2].octave
        7
        >>> tetris.upper_octave()
        False
        '''
        
        return self.change_octave('upper')
        
        
    
    def change_tempo(self, tempo):
        '''(float) -> NoneType
        Takes as an explicit input of a float, multiplies
        the duration of each note by the tempo. 
        >>> happy_birthday = Melody('birthday.txt')
        >>> happy_birthday.change_tempo(1.5)
        >>> happy_birthday.notes[3].duration
        0.75
        >>> hot_cross_buns = Melody('hotcrossbuns.txt')
        >>> prev_tempo = hot_cross_buns.notes[0].duration
        >>> hot_cross_buns.change_tempo(0.5)
        >>> hot_cross_buns.notes[0].duration == prev_tempo * 0.5
        True
        >>> tetris = Melody('tetris.txt')
        >>> tetris.change_tempo(-1)
        Traceback (most recent call last):
        AssertionError: cannot multiply the duration by a non-positive number.
        '''
        
        if tempo <= 0 or type(tempo) != float:
            raise AssertionError('cannot multiply the duration by a non-positive number.')
        for i in range(len(self.notes)):
            self.notes[i].duration = self.notes[i].duration * tempo
        


if __name__ == '__main__':
    doctest.testmod()