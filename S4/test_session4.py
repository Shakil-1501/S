import pytest
import os
import session4
import inspect
import re
import random

README_CONTENT_CHECK_FOR = ['__and__' ,
                            '__or__',
                            '__repr__',
                            '__str__',
                            '__add__',
                            '__eq__',
                            '__float__',
                            '__ge__',
                            '__gt__',
                            '__invertsign__',
                            '__le__',
                            '__lt__',
                            '__mul__',
                            '__sqrt__',
                            '__bool__'
                            ]


#1
def test_readme_exists():
    assert os.file.isfile('README.md') , "README File Missing "


#2
def test_readme_words_counts():
    readme = open('README.md','r')
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100 , "Kindly define README properly"


#3
def test_readme_proper_desscription():
    READMELOOKSGOOD = True
    readme = open('README.md','r')
    readme_words = readme.read().split()
    readme.close()
    for words in README_CONTENT_CHECK_FOR:
        if words not in readme_words:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True , "You have not defined all functions/classes in README.md"


#4
def test_readme_for_formatting():
    readme = open('README.md','r')
    content = readme.read().split()
    readme.close()
    assert content.count('#') > 10 , "Kindly format the README.md"


#5
def test_identation():
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +',lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 


#6
def test_funcation_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction() )
    for function in function:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


#7
def test_repr():
    assert 'Object at' not in session4.__repr__() , "Kindly return meaningful message from __repr__"


#8
def test_str():
    assert 'Object at' not in session4.__str__() , "Kindly return meaningful message from __str__"


#9 Less than
def test_lt_check():
    a = random.uniform(-1, 1)
    assert session4.__lt__(a) , "__lt__ is not properly implementated "


#10
def test_le_check():
    a = randm.uniform(-1,1)
    assert session4.__le__(a) , "__le__ is not properly implemented"
