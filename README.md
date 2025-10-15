# PongGame

A classic Pong game recreated in Python using the built-in `turtle` graphics module.  
Two players control paddles to bounce the ball back and forth across the screen while trying not to miss.  
Each miss awards a point to the opposing player.

## Installation guide

This project requires no external dependencies.  
It runs entirely with Python’s standard library.

1. Make sure you have **Python 3.6 or higher** installed.  
2. Download the **PongGame** project.  
3. Open a terminal (or command prompt) and navigate to the project folder.  
4. Run the script: `python main.py`

## Usage guide

After running the game, a black window will open with two paddles and a blue ball in the center.  
Each player controls a paddle using the following keys:

| Player | Move Up | Move Down |
|---------|----------|------------|
| Left Paddle | **W** | **S** |
| Right Paddle | **Arrow Up** | **Arrow Down** |

### Gameplay
- The ball bounces off the top and bottom walls.  
- When it hits a paddle, it bounces back and speeds up slightly.  
- If a player misses the ball, the opponent scores a point.  
- The current score is displayed at the top of the screen.  

![img_1.png](img_1.png)

## License

This project is licensed under the **MIT License** — see the LICENSE file for details.
