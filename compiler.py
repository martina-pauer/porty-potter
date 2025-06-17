import lang

print('\n\tfrom Java to C: ', lang.Java.transform('System.out.println("Test IT");', C))
print('\n\tfrom C to Java: ', lang.C.transform('printf("Hello World");', Java))
print('\n\tfrom C to Go: ', lang.C.transform('printf("modern");', Go))