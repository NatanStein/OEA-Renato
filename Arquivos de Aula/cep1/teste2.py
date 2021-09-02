import struct

linha = b"AAAAABBBBBCCCCC"
registro = struct.Struct("5s5s5s")
x = registro.unpack(linha)