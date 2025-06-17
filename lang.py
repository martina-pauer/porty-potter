from porty import Syntax

# Define som commons syntax
python, C, Go, Java = Syntax(), Syntax(), Syntax(), Syntax()

python.show_text = 'print(.{1})'

C.show_text = 'printf(.{1})'

Go.show_text = 'fmt.Println(.{1})'

Java.show_text = 'System.out.println(.{1})'