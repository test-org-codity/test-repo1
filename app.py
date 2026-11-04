import subprocess

def echo_value(value):
    return subprocess.check_output(["printf", "%s", value], text=True)
