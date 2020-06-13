# Poker Game

A set of python programs for playing poker with friends while in isolation. 

Requires one trusted moderator to run it, as they have access to the codes and hand contents. 

Card color will vary in support by your terminal. 

## Linux

### Dependencies

- `python3`
- `git`

### Installing

Clone and enter this repo

```
$ git clone https://github.com/nkruss/Poker_game
$ cd Poker_game
```

### Participating in a Game

Run the `card_decryptor.py` program and enter the numbers the host indicates to you

```
$ python3 card_decryptor.py
```

### Hosting a Game

Run the `poker.py` program, respond to the prompts. 

> Note that as the host, you will also need to enter your name in the list of players, should you intend to play. 

```
$ python3 poker.py
```

and, in a separate terminal window

```
$ python3 card_decryptor.py
```

To distribute the codes, run `cat player_info.txt` in a separate terminal window to get the values (offset and multiplier for each player) and distribute them around.

## Windows

### Dependencies

- `python3`: this can be installed from [here](https://www.python.org/downloads/windows/)
- some form of `git`: [Git Bash](https://gitforwindows.org/), [GitHub Desktop](https://desktop.github.com/), ...

### Installing

Clone this repo according to your Git client's specifications.

### Participating in a Game

Run the `card_decryptor.py` program and enter the numbers the host indicates to you

The easiest and most debuggable way to do this is with the Python IDLE, where you should `file` > `open` the `card_decryptor.py` program, then F5 (run) it.

### Hosting a Game

Run the `poker.py` program, respond to the prompts. 

> Note that as the host, you will also need to enter your name in the list of players, should you intend to play. 

The easiest and most debuggable way to do this is with the Python IDLE, where you should `file` > `open` the `poker.py` program, then F5 (run) it.

Do the same for `card_decryptor.py`, possibly in a different IDLE session. 

To distribute the codes, open `player_info.txt` to get the values (offset and multiplier for each player) and distribute them around.

## MacOS

### Dependencies

- `python3`: Follow [a guide](https://docs.python-guide.org/starting/install3/osx/) or install from [the Python site](https://www.python.org/downloads/mac-osx/).
- `git`

### Installing

Clone and enter this repo

```
$ git clone https://github.com/nkruss/Poker_game
$ cd Poker_game
```

### Participating in a Game

Run the `card_decryptor.py` program and enter the numbers the host indicates to you

```
$ python3 card_decryptor.py
```

### Hosting a Game

Run the `poker.py` program, respond to the prompts. 

> Note that as the host, you will also need to enter your name in the list of players, should you intend to play. 

```
$ python3 poker.py
```

and, in a separate terminal window

```
$ python3 card_decryptor.py
```

To distribute the codes, run `cat player_info.txt` in a separate terminal window to get the values (offset and multiplier for each player) and distribute them around.