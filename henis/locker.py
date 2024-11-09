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


class Locker:
    def __init__(self, line):
        self.line = line
        self.assigner = '='
        match = re.match(r"(\w+)\s*=\s*(.*)", self.line)
        if match:
            self.params = [match.group(1), match.group(2)]
        else:
            raise ValueError("Line format is incorrect. Expected format: name = value")
class Variable(Locker):
    def __init__(self, line):
        super().__init__(line)
        self.vid = self.params[0]
        self.value = self.params[1]


# working
# variable_instance = Variable("a = 'hey man' ")
# print(f"Line: {variable_instance.line}")
# print(f"Params: {variable_instance.params}")
# print(f"Name: {variable_instance.vid}")
# print(f"Value: {variable_instance.value}")
