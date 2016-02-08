"""Callback action object

Example:

    def foo(first, second):
        print(first)
        print(second)

    callback = Callback()

    callback.action = foo

    callback.params = {
        'first': 'good',
        'second': 'better'
    }

    callback.execute()

"""


class Callback(object):

    def __init__(self):
        self._params = None
        self._action = None

    def execute(self):
        """Executes the action and returns its results
        """
        if self._params:
            return self._action(**self._params)
        else:
            return self._action()

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, action):
        self._action = action

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, params):
        """Sets the callback parameters by key and value of the given dict.

        Args:
                params: dict. {param name: param value}

        """
        self._params = params

    def add_param(self, key, value):
        """Appends a new parameter. Updates its value if parameter exists.

        Args:
            key: string
            value: mixed
        """
        if type(self._params) is dict:
            self._params[key] = value
        else:
            self._params = {key: value}
