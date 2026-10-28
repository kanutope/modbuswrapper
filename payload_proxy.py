""" payload_proxy
"""
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder


class payloadBuilder:
    """ extends the BinaryPayloadBuilder class with a dictionary allowing to call the various add_xxx methods by 'label'
    """
    def __init__(self, byteorder='>', wordorder='>'):
        """ creates the 'add' dictionary which renders the various add_methods callable by 'label'
            parameters:
                byteorder - string - default '>' (big endian)
                wordorder - string - default '>' (big endian)
        """
        self.bplb = BinaryPayloadBuilder(byteorder=byteorder, wordorder=wordorder)

        self._add = {
            'bits':self.bplb.add_bits,
            'flt16':self.bplb.add_16bit_float,
            'flt32':self.bplb.add_32bit_float,
            'flt64':self.bplb.add_64bit_float,
            'int16':self.bplb.add_16bit_int,
            'int32':self.bplb.add_32bit_int,
            'int64':self.bplb.add_64bit_int,
            'int8':self.bplb.add_8bit_int,
            'str':self.bplb.add_string,
            'uint16':self.bplb.add_16bit_uint,
            'uint32':self.bplb.add_32bit_uint,
            'uint64':self.bplb.add_64bit_uint,
            'uint8':self.bplb.add_8bit_uint,
        }

    def add_payload(self, value=0, datatype=''):
        add = self._add.get(datatype, False)
        if add:
            self._add[datatype](value)

    def to_registers(self):
        return self.bplb.to_registers()



class payloadDecoder:
    """ renders the various decode_xxx methods from a given BinaryPayloadDecoder object accessible by 'label'
    """
    def __init__(self, registers: list[int], byteorder=Endian.LITTLE, wordorder=Endian.BIG):
        """ creates the decoder dictionary which renders the various decoded_XXX methods callable by 'label'
            parameters:
                bpld - BinaryPayloadDecoder instance
        """
        bpld = BinaryPayloadDecoder.fromRegisters(registers=registers,
                                                 byteorder= byteorder,
                                                 wordorder= wordorder)
        
        self.decoder = {
            'bits': bpld.decode_bits,
            'flt16': bpld.decode_16bit_float,
            'flt32': bpld.decode_32bit_float,
            'flt64': bpld.decode_64bit_float,
            'int16': bpld.decode_16bit_int,
            'int32': bpld.decode_32bit_int,
            'int64': bpld.decode_64bit_int,
            'int8': bpld.decode_8bit_int,
            'str': bpld.decode_string,
            'uint16': bpld.decode_16bit_uint,
            'uint32': bpld.decode_32bit_uint,
            'uint64': bpld.decode_64bit_uint,
            'uint8': bpld.decode_8bit_uint,
        }


