# JoJo Pinball Adventure ⭐️👊

A high-energy, **JoJo's Bizarre Adventure** themed pinball game built with Python and Pygame. Use your "Golden Spirit" to rack up high scores and master the physics of the Stand-infused arena!

---

## 📸 Visuals

| **Level 2 // Gen 1** | **Level 2 // Gen 9** | **Level 5 // Gen 1** |
| :--- | :--- | :--- |
| ![Gen 1](a.png) | ![Gen 9](b.png) | ![Lvl 5](c.png) |
| *Initial setup and early testing.* | *Advanced physics and bumper placement.* | *Complex obstacle layouts for higher difficulty.* |

---

## 🚀 Game Features

* **Stand Dynamics:** Custom bumpers that reflect the ball with a **1.4x velocity boost**, turning every collision into a strategic play.
* **Dual Flipper Controls:** Independent flipper mechanics allow for precise aiming and ball saves.
* **Physics-Driven Gameplay:** Features realistic gravity ($0.2$), air friction ($0.995$), and vector-based reflections.
* **Custom Aesthetics:** * **Golden Ball:** The ball glows with the "Golden Spirit."
    * **Dynamic Background:** Supports a custom `jojo.background.png` for an immersive experience.
* **Automatic Reset:** If the ball falls, the score resets and a new ball is launched instantly, keeping the action going.

---

## ⌨️ How to Play

### Controls
* **[A] Key:** Activate Left Flipper (Purple)
* **[D] Key:** Activate Right Flipper (Orange)
* **[X] Close:** Quit the game

### Goal
Hit the red and green **Bumpers** to increase your score. Every hit adds **100 points**! Don't let the ball fall past your flippers, or your score will reset to zero.

---

## 🛠️ Technical Setup

1.  **Install Pygame:**
    ```bash
    pip install pygame
    ```

2.  **Asset Placement:**
    Place your background image in the project folder and name it:
    `jojo.background.png`

3.  **Run the Script:**
    ```bash
    python main.py
    ```

---

## 📜 Code Overview

The game logic is handled in a standard Pygame loop:
* **Physics:** Calculated using `pygame.Vector2` for precision.
* **Collisions:** Uses `.distance_to()` for circular bumpers and `.collidepoint()` for flippers.
* **Rendering:** The background is blit first, followed by physics objects and the UI overlay.

---

*Note: This project is a fan-made tribute. JoJo's Bizarre Adventure is the property of Hirohiko Araki and Shueisha.*
