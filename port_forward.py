import subprocess
from random import randint


def is_forward_success(proc) -> bool:
    while True:
        line = proc.stdout.readline()
        if line != '':
            if b"Forwarding TCP connections from serveo.net" in line:
                return True
            elif b"Warning: remote port forwarding failed for listen port" in line:
                return False
        else:
            return False


def port_forward(local_port: int) -> str:
    """
    SSHes to serveo.net and forwards a local port on localhost to a random port on servo.net.

    :return the host (hostname:port) to connect to over the network
    """

    ssh_host = "serveo.net"

    while True:
        test_port = randint(1000, 65535)
        proc = subprocess.Popen(['ssh', '-R', f'{test_port}:localhost:{local_port}', ssh_host],
                                stdout=subprocess.PIPE)
        if is_forward_success(proc):
            return f"{ssh_host}:{test_port}"
        else:
            continue
