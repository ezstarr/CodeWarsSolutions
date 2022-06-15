"""altERnaTIng cAsE <=> ALTerNAtiNG CaSe
Define String.prototype.toAlternatingCase
(or a similar function/method such as
to_alternating_case/toAlternatingCase/ToAlternatingCase
in your selected language; see the initial solution for details)
such that each lowercase letter becomes uppercase and each
uppercase letter becomes lowercase. For example:

"hello world".toAlternatingCase() === "HELLO WORLD"
"HELLO WORLD".toAlternatingCase() === "hello world"
"hello WORLD".toAlternatingCase() === "HELLO world"
"""


def to_alternating_case(string):
    output = ""
    for s in string:
        if s.islower() == True:
            output += s.upper()
        else:
            output += s.lower()
    print(output)



def to_alternating_case1(string):
    return string.swapcase()


def to_alternating_case2(string):
    print(''.join([s.swapcase() for s in string]))


to_alternating_case2("HeLLo WoRLD")


