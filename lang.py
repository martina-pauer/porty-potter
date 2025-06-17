from porty import Syntax

# Define some commons syntax but help but always require reviwing code
python, C, Go, Java = Syntax(), Syntax(), Syntax(), Syntax()
# Python syntax
python.show_text = 'print(.{1})'
python.variables = '.{1} = .{1}'
# C Syntax
C.show_text = 'printf(.{1})'
C.variables = '.{1} .{1} = .{1}'
# Go Syntax
Go.show_text = 'fmt.Println(.{1})'
Go.variables = 'var .{1} .{1} = .{1}'
# Java Syntax
Java.show_text = 'System.out.println(.{1})'
Java.variables = 'private .{1} .{1} = .{1}'