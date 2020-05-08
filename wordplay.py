class WordplayStr (str):
    """ A String that can report whether it has interesting properties."""

    def same_start_and_end(self):
        """ (WordplayStr) -> bool

        Return whether self starts and ends with the same letter.
        >>> s = WordplayStr('abracadabra')
        >>> s.same_start_and_end()
        True
        >>> s = WordplayStr('canoe')
        >>> s.same_start_and_end()
        False
        """
        return self[0] == self[-1]
if __name__ == '__main__':
    import doctest
    doctest.testmod()
