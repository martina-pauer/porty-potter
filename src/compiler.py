#!/usr/bin/python3
import lang as lang, os, sys

def kinda_file(name : str) -> str:
    '''
        Said what kind of source code
        is a file
    '''
    extensions = {'c' : 'C', 'py' : 'Python', 'java' : 'Java', 'go' : 'Go', 'rs' : 'Rust', 'pl' : 'Perl', 'js' : 'Javascript', 'php' : 'PHP'}

    return extensions[name.split('.')[name.count('.')]] + ' file'

def read_file(name : str) -> str:
    '''
        Show the content of file for
        compile and for reviewing the
        code because compile between
        programming languages is better
        for humans, this only for speed up
        some parts
    '''
    text = ''

    file = open(name, 'r')

    for line in file.readlines():
        text += line

    file.close()

    return text

def write_file(name : str, text : str):
    file = open(name, 'w')
    file.write(text)
    file.close()

source, destination = sys.argv[1].__str__(), sys.argv[2].__str__()

print(f'Compile {kinda_file(source)} ("{source}") to {kinda_file(destination)} ("{destination}")')
print(f'\n{read_file(source)}\t{kinda_file(source)}\n')

objects = {'C file' : lang.C, 'Go file' : lang.Go, 'Python file' : lang.python, 'Java file' : lang.Java}

output = objects[kinda_file(source)].transform(read_file(source), objects[kinda_file(destination)])
print(f'\n{output}\t{kinda_file(destination)}\n')
write_file(destination, output)

os.system('rm -R __pycache__')