import argparse

def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print(text)

parser = argparse.ArgumentParser(description="This program will decode text")
parser.add_argument("--file")
args = parser.parse_args()
filename = args.file
opened_file = open("data/dataset/input.txt")
encoded_text = opened_file.read()
opened_file.close()
decode_Caesar_cipher(encoded_text, -13)

