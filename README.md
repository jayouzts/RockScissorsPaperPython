# Rock, Paper, Scissors, Lizard, Spock – Rules Engine (Python)

Inspired by the *Big Bang Theory*'s extended version of Rock, Paper, Scissors, this Python project demonstrates the **Rules Design Pattern**, enabling you to extend gameplay by simply adding new rule classes — no changes to core logic required.

## 🕹 How to Play

### Option 1: One-click on Windows
Double-click `run_game.bat` from the root directory.

### Option 2: Use the command line
Open a terminal in the project root and run:

```bash
$env:PYTHONPATH="src"
python -m src
```

You’ll be prompted to choose between:
- Classic mode (Rock, Paper, Scissors)
- Lizard-Spock mode (adds Lizard and Spock)

---

## 🧪 Run Unit Tests

From the project root, run:

```bash
python run_tests.py
```

This will discover and run all tests in the `tests/` directory.

---

## 📁 Project Structure

```
RockScissorsPaperPython/
├── run_game.bat           # One-click launcher for Windows
├── run_tests.py           # Launches all unittests
├── requirements.txt       # (optional)
├── tests/
│   └── test_rules.py      # Unit tests for the rules engine
└── src/
    ├── __main__.py        # Main game entry point
    ├── rules/
    │   ├── __init__.py
    │   ├── RSPRulesBase.py
    │   └── RulesClassic.py
    └── utils/
        ├── __init__.py
        ├── RulesCollector.py
        ├── RulesEnforcer.py
        └── RulesEnums.py
```

---

## 🔧 Requirements

This project runs on **Python 3.10+** and uses only the standard library.

## 📚 Design Highlights

- Uses the **Rules Design Pattern**: each rule is encapsulated in its own class
- Automatically discovers rules via reflection (`__subclasses__`)
- Extensible: add a new rule class — no changes to core logic
- Demonstrates `enum`, `abc`, and dynamic introspection

---

