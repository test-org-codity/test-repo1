import subprocess

def echo_value(value):
    return subprocess.check_output(f"printf %s {value}", shell=True, text=True)
