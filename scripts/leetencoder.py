# Encode your message in `basic leet`
# Usage Examples:
#   python leetencoder.py leetcode
#   python leetencoder.py "Hello noobs!"
#   python leetencoder.py --file lorem.txt
#   python leetencoder.py --help
#
# @file: leetencoder.py
# @created: 09.03.2025
# @author: blueberry077
# -----------------------------------------------------
# MIT License
# 
# Copyright (c) 2025 Marc-Daniel DALEBA (blueberry077)
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -----------------------------------------------------

import sys

basic_leet_alphabet = [
    "4", "b", "c", "d", "3", "f",
    "6", "h", "1", "j", "k", "1",
    "m", "n", "0", "p", "q", "r",
    "5", "7", "u", "v", "w", "x",
    "y", "z"
]

def print_help():
    print("usage: python leetencoder.py [Options] text");
    print("Options:")
    print("  --file       use `text` as the input file")
    print("  --help       print information about options")

def main():
    input_file_flag = False
    argv = sys.argv
    argc = len(sys.argv)
    
    if argc < 2:
        print("error: input message is missing");
        print_help();
        return -1
    
    # Process potential options
    argc -= 1
    ptr = 1
    msg = argv[1]
    filename = ""
    
    while argc > 0:
        if argv[ptr] == "--help":
            print_help()
            return
            
        if argv[ptr] == "--file":
            argc -= 1
            ptr += 1
            if argc <= 0:
                print("error: no input file provided after --file")
                print("help: type `python leetencoder.py --help` for informations")
                return -1
            else:
                try:
                    filename = argv[ptr]
                    with open(filename, "r") as f:
                        msg = f.read();
                except FileNotFoundError:
                    print("error: could not open input file:", filename)
                    return -1
            input_file_flag = True
        ptr += 1
        argc -= 1
    
    # Convert message
    res = ""
    for l in msg:
        if l.isalpha():
            lower = l.lower()
            leet_ver = basic_leet_alphabet[ord(lower) - ord('a')]
            if leet_ver != lower:
                res += leet_ver
                continue
        # Keep the old character as it was
        res += l
    
    if input_file_flag:
        with open(filename+".1337", "w") as f:
            f.write(res)
        print("Translated message is stored in", filename+".1337")
    else:
        print(res)

if __name__ == "__main__":
    main()