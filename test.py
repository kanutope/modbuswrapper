
""" test.py """
import os
import stat
import sys
from logging import getLogger
from socket import AF_INET, SOCK_STREAM, socket

from validator import ConstraintFactory

_logger = getLogger(__name__)

def node_exists(node):
    try:
        st = os.stat(node)
        
        # 1. Verify it exists and is a character device (e.g., /dev/ttyAMA0)
        is_char_dev = stat.S_ISCHR(st.st_mode)
        
        # 2. Check if group has read AND write permissions
        # S_IRGRP = Group Read (0o040)
        # S_IWGRP = Group Write (0o020)
        group_rw = bool(st.st_mode & stat.S_IRGRP) and bool(st.st_mode & stat.S_IWGRP)
        
        return is_char_dev and group_rw

    except OSError as ex:
        txt = f"%%% Device {node} unavailable -> {ex.strerror}"
        _logger.error(txt)
        return False

def socket_exists(host, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(3)

    try:
        s.connect((host, port))
        s.close()
        return True
    
    except TimeoutError as ex:
        print(f"%%% Connecting {host}:{port} timed out -> {ex.strerror}")
        return False
    except OSError as ex:
        # OSError: [Errno 113] No route to host
        # ConnectionRefusedError: [Errno 111] Connection refused
        print(f"%%% Unable to connect {host}:{port} -> {ex.strerror}")
        return False

factory = ConstraintFactory()


if sys.argv[1] == "-f":
    nod = sys.argv[2]
    print(f"node_exists({nod}): {node_exists(nod)}")
elif sys.argv[1] == "-h":
    hst = sys.argv[2]
    prt = int(sys.argv[3])
    print(f"socket_exists({hst}:{prt}): {socket_exists(hst, prt)}")
else:
    constraint = sys.argv[1]
    value = float(sys.argv[2])

    # 1. Compile configuration strings into lambdas (done ONCE at initialization)
    validate = factory.compile(constraint)

    # 2. Execute the compiled lambdas directly at runtime (extremely fast)
    print(f"value {value} is {constraint}: {validate(value)}")
        
