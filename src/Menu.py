"""Menu object
"""
from cliform.src.Callback import Callback


class Menu(object):

    def __init__(self, question, action=None, params=None):
        """
        Args:
            question: str
            action: object|None optional function
            params: dict|None optional keywords map for callback
        """
        self._user_input = None
        self._callback = None
        self._options = dict()

        self._question = question

        if action:
            self._callback = Callback()
            self._callback.action = action
            self._callback.params = params

    def _print_options(self):
        """Prints options if set
        """
        if not self._options:
            return

        while self._options:
            option = self._options.popitem()
            print('{!s}: {!s}'.format(option[0], option[1]))

    def display(self):
        """Displays the item, gets the input and sets it in context
        """
        print(self._question)
        self._print_options()
        self._user_input = input()
        return self._execute_callback()

    def _execute_callback(self):
        """Executes the callback action expected by the user input.
        """
        if not self._callback:
            return
        self._callback.add_param('user_input', self._user_input)
        return self._callback.execute()
