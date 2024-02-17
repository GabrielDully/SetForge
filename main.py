class SetForge(object):

    def __init__(self):
        
        self.set = []

    def get_set(self):
        
        return self.set
    
    def __str__(self):
        
        self.set.sort()

        if len(self.set) == 0:
            
            return '{ }'

        elif len(self.set) == 1:
            
            return '{' + str(self.set[0]) + '}'
        
        else:

            set_string = '{' + str(self.set[0])

            for i in range(1, len(self.set)):
                set_string = f'{set_string}, {self.set[i]}'
            set_string = set_string + '}'
                

            return set_string
        
    def insert(self, element):
        
        if not element in self.set:

            self.set.append(element)

    def member(self, element):
        
        return element in self.set

    def remove(self, element):

        try:
        
            self.set.remove(element)
        
        except:
            
            raise ValueError(str(element) + ' not found')
        
        

