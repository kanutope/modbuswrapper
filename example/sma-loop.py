from getopt import gnu_getopt
from logging import DEBUG, ERROR, INFO, basicConfig
from sys import argv
from time import sleep

from modbus.configuration import NODES
from modbuswrapper.example import implement
from modbuswrapper.wrapper import ModbusWrapper

basicConfig(level=INFO)


# Initialize physical devices
mdbwrapper = ModbusWrapper(NODES)


def read_sma(cnt=None):
    xfc = mdbwrapper.get_interface('sma')
    if xfc is None:
        print("some problem to initiate 'sma' interface")
    else:
        implement.read_all(xfc, cnt)

optList, args = gnu_getopt(argv, 'c:', ['count='])

count = 999
for opt, arg in optList:
    if opt in ('-c', '--count'):
        count = int(arg)

read_sma(count)
