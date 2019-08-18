/** Taken from "The Definitive ANTLR 4 Reference" by Terence Parr */

// Derived from http://json.org
lexer grammar JSONLexer;

SLASH
    : '/'
    ;

LCURLY
    : '{'
    ;

RCURLY
    : '}'
    ;

LPAREN
    : '('
    ;

RPAREN
    : ')'
    ;

LSQUARE
    : '['
    ;

RSQUARE
    : ']'
    ;

DOLLAR
    : '$'
    ;

LABRACKET
    : '<'
    ;

RABRACKET
    : '>'
    ;

COMMA
    : ','
    ;

ASSIGN
    : '='
    ;

SEMICOLON
    : ';'
    ;

COLON
    : ':'
    ;

ESCAPE
    : '\\'
    ;

TRUE
    : 'true'
    ;

FALSE
    : 'false'
    ;

NULL
    : 'null'
    ;

STRING
   : '"' (ESC | SAFECODEPOINT)* '"'
   ;


// business define

TYPE
    : '"''type''"'
    ;

ID
    : '"''id''"'
    ;

PROPERTIES
    : '"''properties''"'
    ;

COLOR
    : '"''color''"'
    ;

BACKGROUNDCOLOR
    : '"''backgroundColor''"'
    ;

FONT
    : '"''font''"'
    ;

TEXT
    : '"''text''"'
    ;

LABEL
    : '"''label''"'
    ;

BUTTON
    : '"''button''"'
    ;

IMAGE
    : '"''image''"'
    ;

VIEW
    : '"''view''"'
    ;

fragment ESC
   : '\\' (["\\/bfnrt] | UNICODE)
   ;
fragment UNICODE
   : 'u' HEX HEX HEX HEX
   ;
fragment HEX
   : [0-9a-fA-F]
   ;
fragment SAFECODEPOINT
   : ~ ["\\\u0000-\u001F]
   ;

NUMBER
   : '-'? INT ('.' [0-9] +)? EXP?
   ;

fragment INT
   : '0' | [1-9] [0-9]*
   ;

// no leading zeros

fragment EXP
   : [Ee] [+\-]? INT
   ;

// \- since - means "range" inside [...]

WS
   : [ \t\n\r] + -> skip
   ;