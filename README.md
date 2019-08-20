# UIGenerator

cd grammer
antlr4 -Dlanguage=Python2 ./JSONLexer.g4
antlr4 -Dlanguage=Python2 ./JSONParser.g4
co file to Parser
cd ..
python UIGenerator.py -f json/PUGLiveUserProfileView.json -o output


export CLASSPATH=".:/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH"

alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig'



// TODO:
1. 支持BOOL 类型 value
2. 支持superview
	a.通过嵌套类型支持
	b.通过指定superView type支持
3. 支持autolayout
4. 支持高级布局技巧