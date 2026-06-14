# 🎮 Word Guessing Game

Welcome to the **Word Guessing Game**! This is a classic, interactive, command-line hangman-style game built using Python. Players have a limited number of attempts to guess a randomly chosen hidden word, letter by letter.

Developed with 💻 by **Sahil Chaudhary**.

---

## 🚀 Features

*   **Random Word Selection:** The game automatically selects a word from a predefined pool of words (e.g., *communication, suffocation, elimination, aeroplane, python, designing, creative, figmentation, development*, etc.).
*   **Dynamic Word Tracking:** Displays your progress after every guess, showing correctly guessed letters and hiding the rest behind underscores (`_`).
*   **History Tracking:** Keeps track of all the unique letters you've already guessed so you don't repeat mistakes.
*   **Input Validation:** Ensures you only enter single alphabetical characters, handling invalid or repetitive inputs gracefully.
*   **Visual Feedback:** Fun, encouraging console emojis and clear prompts for wins, losses, and generic updates.

---

## 🛠️ Requirements

To run this game, you only need to have **Python 3.x** installed on your system. No external libraries are required as it uses the built-in `random` module.

---

## 🎮 How to Play

As seen in the source code layout in `image.png`, the rules are simple:

1.  The game randomly chooses a secret word and grants you **6 lives/attempts**.
2.  On each turn, you will see the hidden word represented by underscores (e.g., `_ _ _ _ _ _`).
3.  Type a single letter and press `Enter`.
    *   **Correct Guess:** The letter is revealed in its correct position(s) within the word.
    *   **Incorrect Guess:** You lose 1 attempt.
4.  **Winning:** Guess all the letters of the word before running out of attempts!
5.  **Losing:** If your remaining attempts drop to `0`, the game ends and reveals the hidden word.

---

## 💻 How to Run

1. Clone or download this repository.
2. Save the game script into a file named `main.py`.
3. Open your terminal or command prompt and navigate to the folder containing `main.py`.
4. Run the following command:

```bash
python main.py
