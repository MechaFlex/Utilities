from random import shuffle

# Repeatedly shuffles a list of items using the bag method (well known from modern Tetris), and prints the shuffled list.

bag = ["L-Piece", "I-Piece", "T-Piece", "S-Piece", "Z-Piece", "J-Piece", "O-Piece"]

stringToBePrinted = ""

for i in range(20):
  shuffle(bag)
  for thing in bag:
    stringToBePrinted += thing + "\r\n"

print(stringToBePrinted)