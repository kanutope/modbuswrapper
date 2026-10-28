""" payload_proxy
"""
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder


class payloadBuilder(BinaryPayloadBuilder):
    """ extends the BinaryPayloadBuilder class with a dictionary allowing to call the various add_xxx methods by 'label'
    """
    def __init__(self, byteorder='>', wordorder='>'):
        """ creates the 'add' dictionary which renders the various add_methods callable by 'label'
            parameters:
                byteorder - string - default '>' (big endian)
                wordorder - string - default '>' (big endian)
        """
        super().__init__(byteorder=byteorder, wordorder=wordorder)
        self.add = {
            'bits': super().add_bits,
            'flt16': super().add_16bit_float,
            'flt32': super().add_32bit_float,
            'flt64': super().add_64bit_float,
            'int16': super().add_16bit_int,
            'int32': super().add_32bit_int,
            'int64': super().add_64bit_int,
            'int8': super().add_8bit_int,
            'str': super().add_string,
            'uint16': super().add_16bit_uint,
            'uint32': super().add_32bit_uint,
            'uint64': super().add_64bit_uint,
            'uint8': super().add_8bit_uint,
        }


class payloadDecoder:
    """ renders the various decode_xxx methods from a given BinaryPayloadDecoder object accessible by 'label'
    """
    def __init__(self, registers: list[int]):
        """ creates the decoder dictionary which renders the various decoded_XXX methods callable by 'label'
            parameters:
                bpd - BinaryPayloadDecoder instance
        """
        bpd = BinaryPayloadDecoder.fromRegisters(registers=registers,
                                                 byteorder=self._byteorder,
                                                 wordorder=self._wordorder)
        
        self.decoder = {
            'bits': bpd.decode_bits,
            'flt16': bpd.decode_16bit_float,
            'flt32': bpd.decode_32bit_float,
            'flt64': bpd.decode_64bit_float,
            'int16': bpd.decode_16bit_int,
            'int32': bpd.decode_32bit_int,
            'int64': bpd.decode_64bit_int,
            'int8': bpd.decode_8bit_int,
            'str': bpd.decode_string,
            'uint16': bpd.decode_16bit_uint,
            'uint32': bpd.decode_32bit_uint,
            'uint64': bpd.decode_64bit_uint,
            'uint8': bpd.decode_8bit_uint,
        }


