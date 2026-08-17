<div align="center">

# 🐒 Rogue Monkey

**A classic text-based roguelike RPG with procedural dungeons, turn-based combat, and tactical ASCII exploration.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Terminal RPG](https://img.shields.io/badge/Platform-Terminal%20CLI-10B981?style=for-the-badge&logo=gnubash&logoColor=white)](#-controls--gameplay)
[![Procedural](https://img.shields.io/badge/Dungeons-Procedural%20Generation-8B5CF6?style=for-the-badge&logo=curseforge&logoColor=white)](#-features)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-0%20(Pure%20Python)-06B6D4?style=for-the-badge&logo=pypi&logoColor=white)](#%EF%B8%8F-tech-stack)
[![GitHub Stars](https://img.shields.io/github/stars/Jacekarino/rogue-monkey?style=for-the-badge&logo=github&color=EAB308)](https://github.com/Jacekarino/rogue-monkey/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Jacekarino/rogue-monkey?style=for-the-badge&logo=github&color=6366F1)](https://github.com/Jacekarino/rogue-monkey/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/Jacekarino/rogue-monkey?style=for-the-badge&logo=github&color=EC4899)](https://github.com/Jacekarino/rogue-monkey/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-22C55E?style=for-the-badge&logo=github)](https://github.com/Jacekarino/rogue-monkey/pulls)
[![License: MIT](https://img.shields.io/badge/License-MIT-3B82F6?style=for-the-badge&logo=open-source-initiative&logoColor=white)](license.txt)

<br />

<p align="center">
  <img src="https://raw.githubusercontent.com/Jacekarino/rogue-monkey/main/thumbnail.png" alt="Rogue Monkey Gameplay Preview" width="720" />
</p>
<br />

</div>

---

## 🌟 Overview

**Rogue Monkey** is a text-based roguelike dungeon crawler crafted for the terminal. Step into the role of a courageous Monkey (`@`) venturing into deep underground mazes teeming with vicious monsters, hidden traps, and legendary treasures. 

Explore procedurally generated levels through a dynamic field-of-view system, gather equipment and consumable potions, master turn-based tactical combat, and conquer all 5 floors to slay the final Dragon Boss.

> Inspired by the legendary 1980 classic *Rogue* by Michael Toy, Glenn Wichman, and Ken Arnold.

---

## ✨ Features

- 🗺️ **Procedural Dungeon Generation** — Navigate through 5 unique, randomly generated labyrinth floors with randomized enemy placements, loot, and hazards.
- 🐵 **Hero Progression & Attributes** — Level up your monkey hero to enhance core attributes: Strength, Perception (Vision Range), Agility, Endurance, Intelligence, and Luck.
- ⚔️ **Tactical Turn-Based Combat** — Engage diverse dungeon beasts with weapon strikes, defensive shields, mana-powered special abilities, and real-time combat logs.
- 🎒 **Loot, Gear & Inventory Management** — Discover weapons, armor, shields, and consumable potions inside treasure chests (`C`) scattered across each level.
- 🌫️ **Dynamic Field of View (Fog of War)** — The exploration area dynamically calculates line-of-sight based on your character's Perception attribute.
- ⚠️ **Traps & Hazards** — Beware of pressure-plate traps (`^`) and hazardous tiles concealed throughout the labyrinth.
- 🐉 **Epic Dragon Boss Encounter** — Slay the mighty Dragon waiting on Floor 5 to claim ultimate victory.
- 🎚️ **Multiple Difficulty Modes** — Choose between **Easy**, **Normal**, and **Hard** modes with custom starting equipment (Rusty Dagger, Torn Rags, or Pot Lid).
- ⚡ **Zero External Dependencies** — Runs purely on standard Python libraries without needing any third-party packages or complex setup.

---

## 🎮 Controls & Gameplay

| Key | Action | Description |
| :---: | :--- | :--- |
| <kbd>W</kbd> | **Move Up** | Navigate north through the dungeon |
| <kbd>A</kbd> | **Move Left** | Navigate west through the dungeon |
| <kbd>S</kbd> | **Move Down** | Navigate south through the dungeon |
| <kbd>D</kbd> | **Move Right** | Navigate east through the dungeon |
| <kbd>I</kbd> | **Inventory** | View, consume, or equip items from your backpack |
| <kbd>C</kbd> | **Character** | Inspect character stats, attributes, and level progress |
| <kbd>E</kbd> | **Equipment** | View currently equipped weapon, armor, and shield |
| <kbd>Q</kbd> | **Quit** | Abandon the current dungeon run |

### 🗺️ Map Legend

| Symbol | Element | Description |
| :---: | :--- | :--- |
| `@` | **Player (Monkey)** | Your hero character |
| `#` | **Wall** | Impassable dungeon boundary |
| `.` | **Floor** | Walkable dungeon path |
| `E` | **Exit / Stairs** | Portal to descend to the next dungeon floor |
| `C` | **Chest** | Contains weapons, armor, or consumables |
| `^` | **Trap** | Hidden pressure plate hazard |
| `?` | **Enemy** | Hostile dungeon monster |

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Rendering:** Terminal ANSI Color Sequences & ASCII Art
- **Architecture:** Object-Oriented Design (Modular Entities, Database Dictionaries, State Loops)
- **External Dependencies:** `0` (Zero — Standard Library: `os`, `random`, `math`)

---

## 💻 Getting Started

### 1. Clone Repository
```bash
git clone https://github.com/Jacekarino/rogue-monkey.git
cd rogue-monkey
```

### 2. Run the Game
No installation of external packages required! Simply run:

```bash
# On Windows (PowerShell / Command Prompt)
python main.py

# On macOS / Linux
python3 main.py
```

---

## 📂 Project Structure

```text
rogue-monkey/
├── src/
│   ├── database/         # Data tables for weapons, armors, consumables & enemies
│   │   ├── enemies_db.py
│   │   └── items_db.py
│   ├── entities/         # Character classes & combatant entities
│   │   ├── enemy.py
│   │   ├── entity.py
│   │   └── player.py
│   ├── essential/        # Core game loop, procedural generator, combat & maps
│   │   ├── combat.py
│   │   ├── game.py
│   │   ├── generate.py
│   │   ├── logs.py
│   │   └── map.py
│   ├── items/            # Item subclasses (equipment, consumables)
│   │   ├── consumable.py
│   │   ├── equipment.py
│   │   └── item.py
│   ├── misc/             # Utilities, ANSI color codes, instructions & cheats
│   │   ├── cheats.py
│   │   ├── colors.py
│   │   └── how_to_play.py
│   └── ui/               # Terminal interfaces for stats, inventory & gear
│       ├── character_ui.py
│       ├── equipment_ui.py
│       └── inventory_ui.py
├── main.py               # Main game entry point
├── thumbnail.png         # Game preview screenshot
├── license.txt           # MIT License documentation
└── readme.md             # Project documentation
```

---

## 🤝 Contributing

Contributions, issues, and feature ideas are welcome!

1. Fork the Project (**Fork**)
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a **Pull Request**

---

## 👥 Authors & Credits

- **Jacek Kowalczyk** — [@Jacekarino](https://github.com/Jacekarino)
- **Igor Drzewosz**
- **Jakub Broszko**

*Inspired by **Rogue (1980)** created by Michael Toy, Glenn Wichman, and Ken Arnold.*

---

## 📄 License

Distributed under the **MIT License**. See [`license.txt`](license.txt) for more information.

---

<div align="center">

Made with ♡ by [**Jacekarino**](https://github.com/Jacekarino)

</div>