# Conway's Game of Life
## Introduction
![game](docs/game.gif)

This is an implementation of Conway's iconic game in Python using Numpy and MatPlotLib. The game board size and number of generations can be changed by updating variables in the interface file. For simulations using a game board size larger than a 100 x 100 2D array, a second implementation of the game built with scipy.signal.convolve2d can be used (with good performance up to 1000 x 1000 2D array board size.) Follow the steps below to play the game locally.

## Run Locally
1) Clone this repo locally
```bash
git clone https://github.com/clpatterson/game_of_life.git
```
2) Create a virtual environment in project root using venv
```bash
python3 -m venv venv
```
3) Install all requirements
```bash
pip install -r requirements.txt
```
4) Set game variables
    * Starting at line 22 in game_of_life_interface.py set board size, number of generations, and game speed
5) Run the game
```bash
python3 game_of_life_interface.py
```
6) For game boards with size over 1000, use convolve_gol.py
    * Set game variables starting at line 6
7) Run game
```bash
python3 convolve_gol.py
```
8) Use the magnify glass icon in the GUI to zoom in on large boards

![gui_zoom](docs/convolve_game_zoom.gif)


