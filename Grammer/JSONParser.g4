/** Taken from "The Definitive ANTLR 4 Reference" by Terence Parr */

// Derived from http://json.org
parser grammar JSONParser;

options {
    tokenVocab = JSONLexer;
}

entry
   : LCURLY identifier COLON filename (COMMA properties)? RCURLY
   | LCURLY RCURLY
   ;

identifier
   : STRING
   ;

filename
   : STRING
   ;

propertiesIdentifier
    : STRING
    ;

properties
   : propertiesIdentifier COLON LCURLY oneControl (COMMA oneControl)* RCURLY
   | propertiesIdentifier COLON LCURLY RCURLY
   ;

// UIKIT control

oneControl
   : identifier COLON LCURLY STRING COLON controlType (COMMA uiKitProperties)? RCURLY
   | nullProperty
   ;

controlType
   : STRING
   ;

uiKitProperties
   : propertiesIdentifier COLON LCURLY oneProperty (COMMA oneProperty)* RCURLY
   | propertiesIdentifier COLON LCURLY RCURLY
   ;

// basic property

oneProperty
   : propertyName COLON value
   ;

propertyName
   : STRING
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
