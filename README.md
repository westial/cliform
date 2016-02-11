# cliform #

Basic menu features for command line applications. A callback function can be
configured to execute after the user input using the input value.

## Requirements ##

* Python 3

## Usage ##

1. Define a callback function. A parameter signed as "user_input" will contain 
the user input. E.g.:
```def function(user_input, extra_param):
    print(user_input)
    return extra_param```
2. Define the parameters of the callback function into a dict. E.g.:
`params={'extra_param':'bye'}`
3. Configure the Menu object like so:
```menu = Menu(question='Question?', action=function, params=params)```
4. Display and execute the form:
```menu.display()```

See the examples directory.
