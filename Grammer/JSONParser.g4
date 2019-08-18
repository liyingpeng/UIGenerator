/** Taken from "The Definitive ANTLR 4 Reference" by Terence Parr */

// Derived from http://json.org
parser grammar JSONParser;

options {
    tokenVocab = JSONLexer;
}

entry
   : LCURLY ID COLON STRING (COMMA properties)? RCURLY
   | LCURLY RCURLY
   ;

properties
   : PROPERTIES COLON LCURLY oneControl (COMMA oneControl)* RCURLY
   | PROPERTIES COLON LCURLY RCURLY
   ;

// UIKIT control

oneControl
   : label
   | button
   | image
   | view
   ;

label
   : STRING COLON LCURLY labelType (COMMA uiKitProperties)? RCURLY
   | nullProperty
   ;

button
   : STRING COLON LCURLY buttonType (COMMA uiKitProperties)? RCURLY
   | nullProperty
   ;

image
   : STRING COLON LCURLY imageType (COMMA uiKitProperties)? RCURLY
   | nullProperty
   ;

view
   : STRING COLON LCURLY viewType (COMMA uiKitProperties)? RCURLY
   | nullProperty
   ;

uiKitProperties
   : PROPERTIES COLON LCURLY oneProperty (COMMA oneProperty)* RCURLY
   | PROPERTIES COLON LCURLY RCURLY
   ;

// basic property

oneProperty
   : color
   | font
   | text
   ;

color
   : COLOR COLON STRING
   ;

font
   : FONT COLON NUMBER
   ;

text
   : TEXT COLON STRING
   ;

// basic type

labelType
   : STRING COLON LABEL
   ;

buttonType
   : STRING COLON BUTTON
   ;

imageType
   : STRING COLON IMAGE
   ;

viewType
   : STRING COLON VIEW
   ;

// json grammer

obj
   : LCURLY pair (COMMA pair)* RCURLY
   | LCURLY RCURLY
   ;

pair
   : STRING COLON value
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

nullProperty
   : STRING COLON LCURLY RCURLY
   ;