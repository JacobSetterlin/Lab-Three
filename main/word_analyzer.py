"""
    word_analyzer
    Jacob Setterlin
    This file is used to hold the WordAnalyzer class.

    Last Updated on 10/2/2026
"""

from pathlib import Path
import string

class WordAnalyzer:
    """
    Used to create WordAnalyzer objects.
    """

    def __init__(self, filepath):
        """Used to initialize WordAnalyzer objects."""
        self.filepath = filepath
        #word_frequency is an empty dictionary.
        self.word_frequnecy = {}

    def process_file(self):
        """
        Used to hold the main logic of processing files.
        """
        
        translation_table = str.maketrans("", "", string.punctuation)
        no_punctuation = self.filepath.read_text(encoding="utf-8").translate(translation_table)