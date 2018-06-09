"""
A simple app to generate the names based upon the configurable values
"""

import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class NamesRoot(BoxLayout):
    """
    A general class to generate the names as per the configuration
    """

    def suggest_names(self, length=3, chars_in='', return_results=1):
        """
        Returns a names build randomly using the english alphabet
        Takes optional argument:
        length: restrict the length of the name. if not passed then by default 3
        chars_in: generate the names from the characters only in it.
            If empty then generates the name from A-Z.
        return_results: how many names should be generated and returned. By default 1.
        returns: a list of generated names
        """
        lookup_char = chars_in and chars_in.upper() or ''.join([chr(x) for x in range(65, 65 + 26)])
        result = []
        for i in range(return_results):
            # generate a string of length 'length' randomly taken from lookup_char
            name = ''
            for x in range(length):  # randomly selects and char for length times and build up name
                name += random.choice(lookup_char)
            result.append(name)
        return result


    def generate_names(self, name_len, allowed_chars, total_names):
        try:
            name_len = name_len and int(name_len) or 3
            allowed_chars = allowed_chars or ''
            total_names = total_names and int(total_names) or 1
            name_list = self.suggest_names(name_len, allowed_chars, total_names)
            multiline = '\n'.join(name_list)
            self.ids.display_names.text = multiline
        except Exception as err:
            self.ids.display_names.text = 'Error: \n' + str(err)



class NamesApp(App):

    name = 'Names Generator'

    def build(self):
        return NamesRoot()

    def on_pause(self):
        return True


if __name__ == '__main__':
    NamesApp().run()
