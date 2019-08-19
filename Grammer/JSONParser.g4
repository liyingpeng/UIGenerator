/** Taken from "The Definitive ANTLR 4 Reference" by Terence Parr */

// Derived from http://json.org
parser grammar JSONParser;

options {
    tokenVocab = JSONLexer;
}

obj
   : LCURLY pair (COMMA pair)* RCURLY
   | LCURLY RCURLY
   ;

pair
   : key COLON value
   ;

array
   : LSQUARE value (COMMA value)* RSQUARE
   | LSQUARE RSQUARE
   ;

value
   : STRING
   | NUMBER
   | obj
   | array
   | TRUE
   | FALSE
   | NULL
   ;

key
   : STRING
   ;