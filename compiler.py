import lang, os

print('\n\tfrom Java to C: ', lang.Java.transform('System.out.println("Test IT");', lang.C))
print('\n\tfrom C to Java: ', lang.C.transform('printf("Hello World");', lang.Java))
print('\n\tfrom C to Go: ', lang.C.transform('\nprintf("modern");\nint x = 9', lang.Go))
print('\n\tfrom Python to C: ', lang.python.transform('variable = 2', lang.C))

os.system('rm -R __pycache__')