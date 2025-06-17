from porty import Syntax

# Define some commons syntax but help but always require reviwing code
python, C, Go, Java = Syntax(), Syntax(), Syntax(), Syntax()
# Python syntax
python.show_text = 'print(.{1})'
python.variables = '(w+)s*=s*(.+)'
# C Syntax
C.show_text = 'printf(.{1})'
C.variables = '((long|short|int|char|float|double|void)s+)(w+)(s*=s*)(.+)'
# Go Syntax
Go.show_text = 'fmt.Println(.{1})'
Go.variables = '((var)s+)(w+)(s*=s*)(.+)'
# Java Syntax
Java.show_text = 'System.out.println(.{1})'
Java.variables = '((int|String|boolean|float|double|char|long|short|byte)s+)(w+)(s*=s*)(.+)(;?)'