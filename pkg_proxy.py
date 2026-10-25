from decimal import Decimal
from importlib.metadata import version

from pymodbus.framer import FramerType


def convert_version(vers) -> Decimal:
    nbrs = vers.split(".")
    # Safely handle potential minor/patch variations
    major = Decimal(nbrs[0])
    minor = Decimal(nbrs[1]) if len(nbrs) > 1 else Decimal(0)
    patch = Decimal(nbrs[2].split("-")[0]) if len(nbrs) > 2 else Decimal(0)
    return major + minor / 1000 + patch / 1000000


pmb_version = version("pymodbus")
if convert_version(pmb_version) < convert_version("3.7"):
    from pymodbus.framer.rtu_framer import ModbusRtuFramer
    from pymodbus.framer.socket_framer import ModbusSocketFramer

    RtuFramer = ModbusRtuFramer
    SocketFramer = ModbusSocketFramer
else:
    from pymodbus.framer import FramerType

    RtuFramer = FramerType.RTU
    SocketFramer = FramerType.SOCKET
