from porty import Syntax

# Define some commons syntax but help but always require reviwing code
python, C, Go, Java = Syntax(), Syntax(), Syntax(), Syntax()
# Python syntax
python.show_text = 'print(.{1})'
python.variables = '(w+)s*=s*(.+)'
python.functions = r'^def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\((.*?)\)\s*:'
# C Syntax
C.show_text = 'printf(.{1})'
C.variables = '((long|short|int|char|float|double|void)s+)(w+)(s*=s*)(.+)'
C.manipulate = ''
C.conditionals = ''
C.loops = ''
C.functions = r'^(?:static\s+|extern\s+)?(?:const\s+)?\w+\s+\w+\s*\((?:(?:\w+\s*\**\s*\w+\s*(?:,\s*)?)*)?\)\s*\{$'
# Go Syntax
Go.show_text = 'fmt.Println(.{1})'
Go.variables = '((var)s+)(w+)(s*=s*)(.+)'
Go.manipulate = ''
Go.conditionals = ''
Go.loops = ''
Go.functions = '^func(s+)(w+)(s*)[(](?:(?:(w+)(s+)(w+)(s*)(?:,(s*))?)*)?[)](s*)(?:[(].*[)])?(s*)({)$'
# Java Syntax
Java.show_text = 'System.out.println(.{1})'
Java.variables = '((int|String|boolean|float|double|char|long|short|byte)s+)(w+)(s*=s*)(.+)(;?)'
Java.manipulate = ''
Java.conditionals = ''
Java.loops = ''
Java.functions = '^(?:public|private|protected|(s+))?(?:static(s+))?(?:final(s+))?(?:abstract(s+))?(?:synchronized(s+))?(?:native(s+))?(?:strictfp(s+))?w+(?:s*<[^>]+>s*)?s+w+s*[(](.*?)[)]s*(?:throws(s+)w+(?:,s*w+)*)?s*[{]$'