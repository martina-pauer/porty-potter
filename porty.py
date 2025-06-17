import re

class Syntax():
    '''
        Define the main language syntax for could
        be used to relate the next things in various
        programming langueges:

            Show text in terminal (Syntax.show_text)

            Create Varibles (Syntax.variables)

            Manipulate Variables (Syntax.manipulate)

            Use Conditionals (Syntax.conditionals)

            Create Loops (Syntax.loops)

            Make and use functions (Syntax.functions)

            Read and Write files (Syntax.read, Syntax.write)           

        Use Standar Python Regular expresions for clasify and transform text   
    '''    
    def __init__(self):

        self.show_text : str = ''

        self.variables : str = ''

        self.manipulate : str = ''

        self.conditionals : str = ''

        self.loops : str = ''

        self.functions : str = ''

        self.read : str = ''

        self.write : str = ''


    def transform(self, text : str, language):
        '''
            Translate a text written in the language syntax to
            language with other Syntax object.
        '''
        output = re.sub(self.show_text, language.show_text, text)

        output = re.sub(self.variables, language.variables, output)

        output = re.sub(self.conditionals, language.conditionals, output)

        return output.replace('.{1})', '')