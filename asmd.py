#!/usr/bin/ python3
from os import system as shell
from sys import argv
raw_filename = argv[1]
filename = argv[1].replace(".asm", "")
shell(f"nasm -f elf64 -o {filename}.o {raw_filename} ")
shell(f"ld -m elf_x86_64 -o {filename} {filename}.o")
shell(f"./{filename}")
shell(f"rm -r {filename}.o")
