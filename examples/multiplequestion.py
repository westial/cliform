"""Multiple question form using cliform
"""
from cliform.src.Menu import Menu


################################################################################
# pause

menu = Menu(question='Please, write the answers of the next questions.\n'
                     'Click "Enter" to continue')

menu.display()

################################################################################
# one question


def hello(user_input):
    print('Hello {!s}!'.format(user_input))


menu = Menu(question='What is your name?', action=hello)

menu.display()

print("\n")

################################################################################
# select one option


color_options = [
    'Green',
    'Red',
    'Blue'
]


def get_colors_question():
    global color_options
    question = "Select a color number (1-3):"
    counter = 1
    for option in color_options:
        question += "\n\t{:d}: {!s}".format(counter, option)
        counter += 1
    return question


def run_color_option(user_input, prefix):
    if user_input == "1":
        print('{!s}, like the Hulk'.format(prefix))
    elif user_input == "2":
        print('{!s}, like the blood'.format(prefix))
    elif user_input == "3":
        print('{!s}, like the sky'.format(prefix))
    else:
        print('There is no option for this number')

menu = Menu(question=get_colors_question(),
            action=run_color_option,
            params={'prefix': 'Nice color'})

menu.display()
