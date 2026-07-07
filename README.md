# 🏓 Ping Pong Game

A classic two-player Ping Pong game built with Python's `turtle` graphics module.

## 🎮 Demo

A simple black-background arcade-style Pong game where two paddles bounce a ball back and forth, with a live scoreboard tracking points.

## 🕹️ Controls

| Player | Move Up | Move Down |
|--------|---------|-----------|
| Left Paddle  | `W` | `S` |
| Right Paddle | `Up Arrow` | `Down Arrow` |

## ⚙️ Features

- Smooth ball movement with increasing speed after each paddle hit
- Collision detection with paddles and top/bottom walls
- Automatic scoring when the ball exits the left or right side
- Live scoreboard display

## 📁 Project Structure

```
ping-pong-game/
├── main.py         # Game loop, screen setup, and collision logic
├── paddle.py       # Paddle class (movement and appearance)
├── ball.py         # Ball class (shape, color, movement speed)
├── scoreboard.py   # Scoreboard class (score tracking and display)
└── README.md
```

## 🛠️ Requirements

- Python 3.x
- `turtle` module (included in the Python standard library)

## ▶️ How to Run

```bash
python main.py
```

## 📌 Future Improvements

- Add sound effects on collision and scoring
- Add a "Game Over" screen with a win condition
- Add a pause/restart feature
- Add difficulty levels (ball speed presets)
