from decimal import Decimal
from importlib.metadata import PackageNotFoundError, version
from logging import getLogger

_logger = getLogger(__name__)

def convert_version(vers) -> Decimal:
    nbrs = vers.split(".")
    # Safely handle potential minor/patch variations
    major = Decimal(nbrs[0])
    minor = Decimal(nbrs[1]) if len(nbrs) > 1 else Decimal(0)
    patch = Decimal(nbrs[2].split("-")[0]) if len(nbrs) > 2 else Decimal(0)
    return major + minor / 1000 + patch / 1000000


def get_pkg_version(pkg: str) -> str:
    try:
        return version(pkg)
    except PackageNotFoundError:
        txt = f"%%% [{__name__}] - package {pkg} not found in library."
        _logger.warning(txt)
        return "#N/A"
        

# pymodbus
v3_7 = convert_version("3.7")
v3_10 = convert_version("3.10")
PYMODBUS = convert_version(version("pymodbus"))
if PYMODBUS < v3_7:
    from pymodbus.framer.rtu_framer import ModbusRtuFramer
    from pymodbus.framer.socket_framer import ModbusSocketFramer

    proxyRtuFramer = ModbusRtuFramer
    proxySocketFramer = ModbusSocketFramer
else:
    from pymodbus.framer import FramerType

    proxyRtuFramer = FramerType.RTU
    proxySocketFramer = FramerType.SOCKET

def repack_kwargs(**kwargs):
    repacked = {}
    for key, val in kwargs.items():
        if PYMODBUS >= v3_10 and key == 'slave':
            repacked['device_id'] = val
        else:
            repacked[key] = val
    
    print(repacked)
    return repacked
