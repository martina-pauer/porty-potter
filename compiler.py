import lang, os

print('\n\tfrom Java to C: ', lang.Java.transform('System.out.println("Test IT");', lang.C))
print('\n\tfrom C to Java: ', lang.C.transform('printf("Hello World");', lang.Java))
print('\n\tfrom C to Go: ', lang.C.transform('printf("modern");', lang.Go))

os.system('rm -R __pycache__')