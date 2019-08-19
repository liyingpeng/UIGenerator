# Generated from ./JSONParser.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\17:\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write(u"\3\2\3\2\7\2\21\n\2\f\2\16\2\24\13\2\3\2\3\2\3\2\3\2")
        buf.write(u"\5\2\32\n\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4$\n\4")
        buf.write(u"\f\4\16\4\'\13\4\3\4\3\4\3\4\3\4\5\4-\n\4\3\5\3\5\3\5")
        buf.write(u"\3\5\3\5\3\5\3\5\5\5\66\n\5\3\6\3\6\3\6\2\2\7\2\4\6\b")
        buf.write(u"\n\2\2\2>\2\31\3\2\2\2\4\33\3\2\2\2\6,\3\2\2\2\b\65\3")
        buf.write(u"\2\2\2\n\67\3\2\2\2\f\r\7\3\2\2\r\22\5\4\3\2\16\17\7")
        buf.write(u"\b\2\2\17\21\5\4\3\2\20\16\3\2\2\2\21\24\3\2\2\2\22\20")
        buf.write(u"\3\2\2\2\22\23\3\2\2\2\23\25\3\2\2\2\24\22\3\2\2\2\25")
        buf.write(u"\26\7\4\2\2\26\32\3\2\2\2\27\30\7\3\2\2\30\32\7\4\2\2")
        buf.write(u"\31\f\3\2\2\2\31\27\3\2\2\2\32\3\3\2\2\2\33\34\5\n\6")
        buf.write(u"\2\34\35\7\t\2\2\35\36\5\b\5\2\36\5\3\2\2\2\37 \7\5\2")
        buf.write(u"\2 %\5\b\5\2!\"\7\b\2\2\"$\5\b\5\2#!\3\2\2\2$\'\3\2\2")
        buf.write(u"\2%#\3\2\2\2%&\3\2\2\2&(\3\2\2\2\'%\3\2\2\2()\7\6\2\2")
        buf.write(u")-\3\2\2\2*+\7\5\2\2+-\7\6\2\2,\37\3\2\2\2,*\3\2\2\2")
        buf.write(u"-\7\3\2\2\2.\66\7\r\2\2/\66\7\16\2\2\60\66\5\2\2\2\61")
        buf.write(u"\66\5\6\4\2\62\66\7\n\2\2\63\66\7\13\2\2\64\66\7\f\2")
        buf.write(u"\2\65.\3\2\2\2\65/\3\2\2\2\65\60\3\2\2\2\65\61\3\2\2")
        buf.write(u"\2\65\62\3\2\2\2\65\63\3\2\2\2\65\64\3\2\2\2\66\t\3\2")
        buf.write(u"\2\2\678\7\r\2\28\13\3\2\2\2\7\22\31%,\65")
        return buf.getvalue()


class JSONParser ( Parser ):

    grammarFileName = "JSONParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'{'", u"'}'", u"'['", u"']'", u"'$'", 
                     u"','", u"':'", u"'true'", u"'false'", u"'null'" ]

    symbolicNames = [ u"<INVALID>", u"LCURLY", u"RCURLY", u"LSQUARE", u"RSQUARE", 
                      u"DOLLAR", u"COMMA", u"COLON", u"TRUE", u"FALSE", 
                      u"NULL", u"STRING", u"NUMBER", u"WS" ]

    RULE_obj = 0
    RULE_pair = 1
    RULE_array = 2
    RULE_value = 3
    RULE_key = 4

    ruleNames =  [ u"obj", u"pair", u"array", u"value", u"key" ]

    EOF = Token.EOF
    LCURLY=1
    RCURLY=2
    LSQUARE=3
    RSQUARE=4
    DOLLAR=5
    COMMA=6
    COLON=7
    TRUE=8
    FALSE=9
    NULL=10
    STRING=11
    NUMBER=12
    WS=13

    def __init__(self, input, output=sys.stdout):
        super(JSONParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ObjContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(JSONParser.ObjContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LCURLY(self):
            return self.getToken(JSONParser.LCURLY, 0)

        def pair(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(JSONParser.PairContext)
            else:
                return self.getTypedRuleContext(JSONParser.PairContext,i)


        def RCURLY(self):
            return self.getToken(JSONParser.RCURLY, 0)

        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(JSONParser.COMMA)
            else:
                return self.getToken(JSONParser.COMMA, i)

        def getRuleIndex(self):
            return JSONParser.RULE_obj

        def enterRule(self, listener):
            if hasattr(listener, "enterObj"):
                listener.enterObj(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitObj"):
                listener.exitObj(self)




    def obj(self):

        localctx = JSONParser.ObjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_obj)
        self._la = 0 # Token type
        try:
            self.state = 23
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.match(JSONParser.LCURLY)
                self.state = 11
                self.pair()
                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONParser.COMMA:
                    self.state = 12
                    self.match(JSONParser.COMMA)
                    self.state = 13
                    self.pair()
                    self.state = 18
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 19
                self.match(JSONParser.RCURLY)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.match(JSONParser.LCURLY)
                self.state = 22
                self.match(JSONParser.RCURLY)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PairContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(JSONParser.PairContext, self).__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(JSONParser.KeyContext,0)


        def COLON(self):
            return self.getToken(JSONParser.COLON, 0)

        def value(self):
            return self.getTypedRuleContext(JSONParser.ValueContext,0)


        def getRuleIndex(self):
            return JSONParser.RULE_pair

        def enterRule(self, listener):
            if hasattr(listener, "enterPair"):
                listener.enterPair(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPair"):
                listener.exitPair(self)




    def pair(self):

        localctx = JSONParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.key()
            self.state = 26
            self.match(JSONParser.COLON)
            self.state = 27
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(JSONParser.ArrayContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LSQUARE(self):
            return self.getToken(JSONParser.LSQUARE, 0)

        def value(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(JSONParser.ValueContext)
            else:
                return self.getTypedRuleContext(JSONParser.ValueContext,i)


        def RSQUARE(self):
            return self.getToken(JSONParser.RSQUARE, 0)

        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(JSONParser.COMMA)
            else:
                return self.getToken(JSONParser.COMMA, i)

        def getRuleIndex(self):
            return JSONParser.RULE_array

        def enterRule(self, listener):
            if hasattr(listener, "enterArray"):
                listener.enterArray(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArray"):
                listener.exitArray(self)




    def array(self):

        localctx = JSONParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(JSONParser.LSQUARE)
                self.state = 30
                self.value()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONParser.COMMA:
                    self.state = 31
                    self.match(JSONParser.COMMA)
                    self.state = 32
                    self.value()
                    self.state = 37
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 38
                self.match(JSONParser.RSQUARE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(JSONParser.LSQUARE)
                self.state = 41
                self.match(JSONParser.RSQUARE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(JSONParser.ValueContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(JSONParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(JSONParser.NUMBER, 0)

        def obj(self):
            return self.getTypedRuleContext(JSONParser.ObjContext,0)


        def array(self):
            return self.getTypedRuleContext(JSONParser.ArrayContext,0)


        def TRUE(self):
            return self.getToken(JSONParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(JSONParser.FALSE, 0)

        def NULL(self):
            return self.getToken(JSONParser.NULL, 0)

        def getRuleIndex(self):
            return JSONParser.RULE_value

        def enterRule(self, listener):
            if hasattr(listener, "enterValue"):
                listener.enterValue(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitValue"):
                listener.exitValue(self)




    def value(self):

        localctx = JSONParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_value)
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.match(JSONParser.STRING)
                pass
            elif token in [JSONParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.match(JSONParser.NUMBER)
                pass
            elif token in [JSONParser.LCURLY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.obj()
                pass
            elif token in [JSONParser.LSQUARE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 47
                self.array()
                pass
            elif token in [JSONParser.TRUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 48
                self.match(JSONParser.TRUE)
                pass
            elif token in [JSONParser.FALSE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 49
                self.match(JSONParser.FALSE)
                pass
            elif token in [JSONParser.NULL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 50
                self.match(JSONParser.NULL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class KeyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(JSONParser.KeyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(JSONParser.STRING, 0)

        def getRuleIndex(self):
            return JSONParser.RULE_key

        def enterRule(self, listener):
            if hasattr(listener, "enterKey"):
                listener.enterKey(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitKey"):
                listener.exitKey(self)




    def key(self):

        localctx = JSONParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(JSONParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





