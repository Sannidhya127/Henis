# Assign right hand value to left hand place holder

import ctypes as c
import re
import numexpr as ne



# assign("a = 34/33.3")
def strip_outside_quotes(input_string):
      
        parts = re.split(r"('.*?')", input_string) 

      
        for i in range(len(parts)):
            if i % 2 == 0:  
                parts[i] = parts[i].strip()

        return ''.join(parts)

class Locker:
    def __init__(self, line):
        self.line = line
        self.assigner = '='
        match = re.match(r"(\w+)\s*=\s*(.*)", self.line)
        if match:
            self.params = [match.group(1), match.group(2)]
        else:
            raise ValueError("Line format is incorrect. Expected format: name = value")
        
class Buffer:
    def __init__(self, initial_value):
        # Create a buffer with extra space
        self.buffer = c.create_string_buffer(len(initial_value) + 1)
        self.buffer.value = initial_value.encode('utf-8')

        # Get pointer to the buffer
        self.buffer_pointer = c.pointer(self.buffer)

    def get_buffer_address(self):
        # Retrieve the buffer's address directly
        return c.addressof(self.buffer)
    def set_value(self, new_val):
        # Update the buffer in-place
        if len(new_val) <= len(self.buffer) - 1:
            self.buffer.value = new_val.encode('utf-8')  # Direct memory update
        else:
            raise ValueError("New value is too large for the buffer.")

    def get_buffer_value(self):
        # Access value using the buffer pointer (dereference it)
        return self.buffer_pointer.contents.value.decode('utf-8')
class Variable(Locker):
    def __init__(self, line):
        super().__init__(line)

    
        self.variables = {}
        self.value = strip_outside_quotes(self.params[1])
        self.vid = self.params[0]
    
   
    def check_string_type(self):
        # Check if enclosed in single or double quotes
        if (self.value.startswith("'") and self.value.endswith("'")) or (self.value.startswith('"') and self.value.endswith('"')):
            return "00"
        
        # Check if it's a numeric operation (numbers and valid operators)
        elif re.fullmatch(r"[0-9+\-*/%^(). ]+", self.value):
            return "11"
        
        # Check if it's alphanumeric without quotes
        elif bool(re.fullmatch(r"^[a-zA-Z0-9+\-*/]+$", self.value)):
            return "01"
        
        # Default case if none of the above match
        else:
            print("Unrecognized type. Error code: 000/10") 
            return "10"
    def var_parser(self):
        print(self.vid)
        check = self.check_string_type()
        if check == "00":
            print("Enetered str")
            val = self.value[1:-1]
            self.vid = Buffer(val)
            self.variables[self.vid] = self.vid.get_buffer_value()
            print(self.variables)
            print(f"buffer adress: {self.vid.get_buffer_address()}, Buffer value: {self.vid.get_buffer_value()}") 
        elif check == "11":
            print("Entered num")
            try:
                val = ne.evaluate(self.value)
                self.vid = Buffer(str(val))
                self.variables[self.vid] = self.vid.get_buffer_value()
                print(self.variables)
                print(f"buffer adress: {self.vid.get_buffer_address()}, Buffer value: {self.vid.get_buffer_value()}")
            except:
                print("Invalid operation.")
        elif check == "01":
            print("Entered alpha")
            print(self.variables)
            for i in self.value:
                if i.isalpha():
                    if i not in self.variables:
                        print(f"Variable {i} not defined.")
                        return
                    else:
                        self.value = self.value.replace(i, self.vid.get_buffer_value())
                        print(f"buffer adress: {self.vid.get_buffer_address()}, Buffer value: {self.vid.get_buffer_value()}")
        elif check == '10':
            return '000'
variable_instance_b = Variable("a=6")
print(f"String: {variable_instance_b.value}")
print(f"Type: {type(variable_instance_b)}")
variable_instance_a = Variable("j =a+5")

variable_instance_a.var_parser()
print(f"Type: {type(variable_instance_a)}")
print(variable_instance_a.variables)