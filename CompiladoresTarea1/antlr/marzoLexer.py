# Generated from c:\Users\IGNACIO\Desktop\CompiladoresTarea1\antlr\marzo.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("k\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\22\6\22\\\n\22\r\22\16\22]\3\23\6\23a\n\23\r\23")
        buf.write("\16\23b\3\24\6\24f\n\24\r\24\16\24g\3\24\3\24\2\2\25\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25\3\2\5\3\2\62;\3\2")
        buf.write("c|\5\2\13\f\17\17\"\"\2m\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\3)\3\2\2\2")
        buf.write("\5+\3\2\2\2\7-\3\2\2\2\t/\3\2\2\2\13\61\3\2\2\2\r\63\3")
        buf.write("\2\2\2\17\65\3\2\2\2\218\3\2\2\2\23;\3\2\2\2\25>\3\2\2")
        buf.write("\2\27A\3\2\2\2\31F\3\2\2\2\33K\3\2\2\2\35M\3\2\2\2\37")
        buf.write("Q\3\2\2\2!X\3\2\2\2#[\3\2\2\2%`\3\2\2\2\'e\3\2\2\2)*\7")
        buf.write("-\2\2*\4\3\2\2\2+,\7/\2\2,\6\3\2\2\2-.\7\61\2\2.\b\3\2")
        buf.write("\2\2/\60\7,\2\2\60\n\3\2\2\2\61\62\7@\2\2\62\f\3\2\2\2")
        buf.write("\63\64\7>\2\2\64\16\3\2\2\2\65\66\7@\2\2\66\67\7?\2\2")
        buf.write("\67\20\3\2\2\289\7>\2\29:\7?\2\2:\22\3\2\2\2;<\7?\2\2")
        buf.write("<=\7?\2\2=\24\3\2\2\2>?\7k\2\2?@\7h\2\2@\26\3\2\2\2AB")
        buf.write("\7v\2\2BC\7j\2\2CD\7g\2\2DE\7p\2\2E\30\3\2\2\2FG\7g\2")
        buf.write("\2GH\7n\2\2HI\7u\2\2IJ\7g\2\2J\32\3\2\2\2KL\7?\2\2L\34")
        buf.write("\3\2\2\2MN\7k\2\2NO\7p\2\2OP\7v\2\2P\36\3\2\2\2QR\7r\2")
        buf.write("\2RS\7t\2\2ST\7k\2\2TU\7p\2\2UV\7v\2\2VW\7*\2\2W \3\2")
        buf.write("\2\2XY\7+\2\2Y\"\3\2\2\2Z\\\t\2\2\2[Z\3\2\2\2\\]\3\2\2")
        buf.write("\2][\3\2\2\2]^\3\2\2\2^$\3\2\2\2_a\t\3\2\2`_\3\2\2\2a")
        buf.write("b\3\2\2\2b`\3\2\2\2bc\3\2\2\2c&\3\2\2\2df\t\4\2\2ed\3")
        buf.write("\2\2\2fg\3\2\2\2ge\3\2\2\2gh\3\2\2\2hi\3\2\2\2ij\b\24")
        buf.write("\2\2j(\3\2\2\2\6\2]bg\3\b\2\2")
        return buf.getvalue()


class marzoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    Numero = 17
    Variable = 18
    WS = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'/'", "'*'", "'>'", "'<'", "'>='", "'<='", "'=='", 
            "'if'", "'then'", "'else'", "'='", "'int'", "'print('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "Numero", "Variable", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "Numero", "Variable", "WS" ]

    grammarFileName = "marzo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


