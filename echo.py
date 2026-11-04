import subprocess

def echo_value(value):
    """Echo the given string literally, including whitespace and metacharacters."""
    return subprocess.check_output(f"printf %s {value}", shell=True, text=True)
