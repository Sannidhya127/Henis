# Assign right hand value to left hand place holder

import ctypes as c
import re

# assigner = '='
# # libc = c.CDLL("libc.so.6")
# # libc.printf.argtypes = [c.c_char_p]
# def assign(line):
#     global assigner
#     params = line.split('=', 1)
#     if type(params[1]) == str:
#         # params[0] = c.create_string_buffer(100)
#         try:
#             params[1] = eval(params[1])
#         except:
#             pass
#         try:
#             final = params[1].strip().encode('utf-8')
#         except:
#             final = params[1]
#         params[0] = c.c_char_p(final.encode('utf-8'))
#     elif type(params[1]) == int:
#         try:
#             params[1] = eval(params[1])
#         except:
#             pass
#         params[0] = c.c_int(params[1])
#     elif type(params[1]) == float:
#         try:
#             params[1] = eval(params[1])
#         except:
#             pass
#         params[0] = c.c_float(params[1])
#     elif type(params[1]) == bool:
#         try:
#             params[1] = eval(params[1])
#         except:
#             pass
#         params[0] = c.c_bool(params[1])
#     else:   
#         print("Error: Invalid type")
#         return
    
#     prt = c.pointer(params[0])
#     print(prt.contents.value.decode('utf-8'))




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
        pattern = r"(?<=^|\s)(?!')\s+|\s+(?=\s|$)"
    
    # Replace the matched whitespace with an empty string
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
        elif self.value.isalnum():
            return "01"
        
        # Default case if none of the above match
        else:
            print(self.value, self.value.startswith("'"), self.value.endswith("'")) 
            return "10"
    def var_parser(self):
        check = self.check_string_type()
        if check == "00":
            val = self.value[1:-1]
            self.vid = Buffer(val)
            return self.vid.get_buffer_address(), self.vid.get_buffer_value()
        elif check == "11":
            return 11
        elif check == "01":
            return '01'
        elif check == '10':
            return '000'

variable_instance = Variable("j = 'yo bro' ")
print(f"String: {variable_instance.value}")
print(f"Type: {type(variable_instance)}")
print(f"Buffer Address: {variable_instance.var_parser()}")