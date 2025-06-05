## Snake Game CMD
Snake game developed in Python to run in the command line.   
Gameplay, [here](https://youtu.be/zsprRhqMh5k).

### How to start
1. Create virtual environment `python -m venv .venv`
2. Activate the env `.venv\Scripts\Activate.ps1`
3. Run dev `python main.py`

### Dependencies
`windows-curses`

### Build as exe
1. `pip install pyinstaller`
2. `pyinstaller --onefile --console --name snake-game main.py`
3. run snake-game.exe

### How to play
Movements with the arrows.
Esc to end the game.
