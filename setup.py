import sys
from cx_Freeze import setup, Executable

setup(
    name = "whatsNerf",
    version = "1.0",
    description = "Your friends will love it",
    executables = [Executable("whatsNerf.py", base = None)])