from random import shuffle


import random

bag = ["L-Piece", "I-Piece", "T-Piece", "S-Piece", "Z-Piece", "J-Piece", "O-Piece"]

stringToBePrinted = ""

for i in range(20):
  random.shuffle(bag)
  for thing in bag:
    stringToBePrinted += thing + "\r\n"

print(stringToBePrinted)