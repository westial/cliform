from distutils.core import setup

version_file = open('VERSION', 'r')
version = version_file.readline()

setup(
    name='cliform',
    version=version,
    packages=['cliform'],
    url='https://github.com/westial/cliform',
    license='GPL v3',
    author='Jaume Mila',
    author_email='jaume@westial.com',
    description='User input menu with callback for command line applications.'
)