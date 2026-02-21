# Pac-Man: Python & Pygame Engine
A custom implementation of the classic arcade game built entirely in Python, featuring dynamic algorithmic audio generation and heuristic-based enemy AI.

## 🛠 Technical Engineering Highlights
* **Algorithmic Audio Synthesis**: Instead of loading static audio files, the game utilizes `numpy` to generate continuous sine waves and math functions to create 16-bit stereo sound effects and frequency sweeps entirely from scratch.
* **Heuristic Pathfinding (AI)**: Implemented a Manhattan Distance algorithm in the enemy logic (`ghost.py`), allowing the ghosts to dynamically calculate the shortest path to chase the player through the grid matrix.
* **Matrix-Based State Management**: The game board is managed via a 2D array mapping system, enabling O(1) time complexity for collision detection and wall boundary checks.
* **Custom Sprite Rendering**: Bypasses external image assets by mathematically drawing and animating sprites (Pac-Man's mouth mechanics, Ghost wavy animations) directly onto transparent Pygame surfaces.

## 📂 Project Structure
* **main.py**: Initializes the game window and triggers the main application loop.
* **game.py**: The core engine handling the 15 FPS game loop, state transitions (Win/Game Over), and rendering logic.
* **ghost.py**: Contains the enemy AI logic, move calculations, and procedural drawing methods.
* **player.py**: Manages user input, valid move verification against the maze array, and frame-based animations.
* **sounds.py**: A custom synthesizer using `numpy` and `pygame.mixer` to generate beeps, win tones, and collision sounds dynamically.
* **game_board.py**: Stores the structural blueprint of the level as a 2D integer matrix.

## 🗺️ Roadmap & Future Enhancements
Currently, this project serves as a foundational engine (MVP) featuring a single, hardcoded matrix level to demonstrate the core pathfinding AI and algorithmic audio mechanics. 

Planned architectural improvements include:
* **Procedural Maze Generation**: Implementing maze-generation algorithms (like Prim's or Kruskal's) to dynamically create new, navigable matrices instead of relying on hardcoded arrays.
* **State Management**: Building a level-progression system to handle transitions, increased game speeds, and progressively harder ghost logic.
* **Advanced Ghost AI**: Upgrading the pathfinding from a simple Manhattan distance chase to distinct behavioral heuristics (e.g., implementing A* Search or calculating interception paths based on the player's current trajectory).

## 🚀 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/RZ-Logic/pacman-python.git

2. **Install dependencies**:
    ```bash
    pip install pygame numpy

3. **Execute the game**:
    ```bash
    python main.py
