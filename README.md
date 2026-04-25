# Holey rectangle domino tiling
A $m \times n$ holey rectangle is a $m \times n$ rectangle with the center $(m-4) \times (n-4)$ rectangle removed, Given a $m \times n$ holey rectangle, this script generates a random domino tiling and calculates the total number of tilings for this figure.

![A domino tiling of a 5x5 holey rectangle](5x5.PNG)

## Technology used

The script is written in python, It uses the random and the Pillow libraries to create the tiling and the SymPy library to calculate the number of tilings.\
You can change the colors of the dominoes and the size of the holey rectangle, $n$ and $m$ must be greater or equal than 5, technically the script can generate tilings of a $4 \times 4$ square (since it is a degenerate case of the holey rectangle), but errors may happen.

![A domino tiling of a 4x4 square](4x4.PNG)

## Number of tilings

Given a $m \times n$ holey rectangle the number of tilings is: 
