"""
    word_analyzer
    Jacob Setterlin
    This file is used to hold the WordAnalyzer class.

    Last Updated on 10/2/2026
"""

class WordAnalyzer:
    """
        Used to create WordAnalyzer objects.
    """

    def __init__(self, filepath):
        """Used to initialize WordAnalyzer objects."""
        self.filepath = filepath
        #word_frequency is an empty dictionary.
        self.word_frequnecy = {}

    