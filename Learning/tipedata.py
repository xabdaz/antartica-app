# tipe data integer
data_integer = 1
print(type(data_integer))
print(" - data: ", data_integer)

# tipe data float
data_float: float = 1.5
print("data : ", data_float)
print("bertipe : ", type(data_float))

# tipe data string

data_string: str = "data string"
print("data : ", data_string)
print("bertipe : ", type(data_string))

# tipe data bool
data_bool: bool = False
print("data : ", data_string)
print("bertipe : ", type(data_bool))

#tipe data complex
data_complex = (4, 1)
print("data : ", data_complex)
print("bertipe : ", type(data_complex))

from ctypes import c_double
data_c_double = c_double(15.2)
print("data : ", data_c_double)
print("bertipe : ", type(data_c_double))