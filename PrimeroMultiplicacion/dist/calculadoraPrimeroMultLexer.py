# Generated from calculadoraPrimeroMult.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,16,92,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,2,14,7,14,2,15,7,15,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,
        1,4,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,10,1,
        10,1,11,4,11,61,8,11,11,11,12,11,62,1,12,4,12,66,8,12,11,12,12,12,
        67,1,13,4,13,71,8,13,11,13,12,13,72,1,13,1,13,4,13,77,8,13,11,13,
        12,13,78,1,14,3,14,82,8,14,1,14,1,14,1,15,4,15,87,8,15,11,15,12,
        15,88,1,15,1,15,0,0,16,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,
        10,21,11,23,12,25,13,27,14,29,15,31,16,1,0,3,2,0,65,90,97,122,1,
        0,48,57,2,0,9,9,32,32,97,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,
        1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,
        1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,
        1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,1,33,1,0,0,0,3,35,1,0,0,0,5,37,
        1,0,0,0,7,39,1,0,0,0,9,41,1,0,0,0,11,44,1,0,0,0,13,47,1,0,0,0,15,
        49,1,0,0,0,17,51,1,0,0,0,19,53,1,0,0,0,21,55,1,0,0,0,23,60,1,0,0,
        0,25,65,1,0,0,0,27,70,1,0,0,0,29,81,1,0,0,0,31,86,1,0,0,0,33,34,
        5,61,0,0,34,2,1,0,0,0,35,36,5,40,0,0,36,4,1,0,0,0,37,38,5,41,0,0,
        38,6,1,0,0,0,39,40,5,33,0,0,40,8,1,0,0,0,41,42,5,43,0,0,42,43,5,
        43,0,0,43,10,1,0,0,0,44,45,5,45,0,0,45,46,5,45,0,0,46,12,1,0,0,0,
        47,48,5,42,0,0,48,14,1,0,0,0,49,50,5,47,0,0,50,16,1,0,0,0,51,52,
        5,43,0,0,52,18,1,0,0,0,53,54,5,45,0,0,54,20,1,0,0,0,55,56,5,116,
        0,0,56,57,5,97,0,0,57,58,5,110,0,0,58,22,1,0,0,0,59,61,7,0,0,0,60,
        59,1,0,0,0,61,62,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,24,1,0,0,
        0,64,66,7,1,0,0,65,64,1,0,0,0,66,67,1,0,0,0,67,65,1,0,0,0,67,68,
        1,0,0,0,68,26,1,0,0,0,69,71,7,1,0,0,70,69,1,0,0,0,71,72,1,0,0,0,
        72,70,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,76,5,46,0,0,75,77,7,
        1,0,0,76,75,1,0,0,0,77,78,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,
        28,1,0,0,0,80,82,5,13,0,0,81,80,1,0,0,0,81,82,1,0,0,0,82,83,1,0,
        0,0,83,84,5,10,0,0,84,30,1,0,0,0,85,87,7,2,0,0,86,85,1,0,0,0,87,
        88,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,90,1,0,0,0,90,91,6,15,
        0,0,91,32,1,0,0,0,7,0,62,67,72,78,81,88,1,6,0,0
    ]

class calculadoraPrimeroMultLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    NOT = 4
    INCREMENT = 5
    DECREMENT = 6
    MUL = 7
    DIV = 8
    ADD = 9
    SUB = 10
    TAN = 11
    ID = 12
    INT = 13
    FLOAT = 14
    NEWLINE = 15
    WS = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'('", "')'", "'!'", "'++'", "'--'", "'*'", "'/'", "'+'", 
            "'-'", "'tan'" ]

    symbolicNames = [ "<INVALID>",
            "NOT", "INCREMENT", "DECREMENT", "MUL", "DIV", "ADD", "SUB", 
            "TAN", "ID", "INT", "FLOAT", "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "NOT", "INCREMENT", "DECREMENT", 
                  "MUL", "DIV", "ADD", "SUB", "TAN", "ID", "INT", "FLOAT", 
                  "NEWLINE", "WS" ]

    grammarFileName = "calculadoraPrimeroMult.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


