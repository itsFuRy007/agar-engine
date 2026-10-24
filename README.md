# Agar Engine

A Python project exploring Agar.io-related bot infrastructure, WebSocket communication, and game protocol analysis.

I started this project to understand how these systems work under the hood. I've worked on the local API, bot management logic, packet handling, and protocol utilities. I also used Ghidra to inspect compiled code and investigate parts of the communication flow.

## What I've Been Working On

- **API Development:** Built a local API using FastAPI.
- **Bot Management:** Implemented bot state and lifecycle management, with unit tests.
- **WebSocket Client:** Developed the foundation for secure WebSocket communication.
- **Protocol Research:** Experimented with packet construction, XOR operations, and LZ4 decompression.
- **Reverse Engineering:** Used Ghidra to inspect compiled binaries and trace selected functions.
- **Testing:** Added unit tests for bot management and protocol utilities.

## Tech Stack

Python, FastAPI, Pydantic, Uvicorn, WebSockets, LZ4, Ghidra, Git, and GitHub.

## Current Status

This project is a work in progress. The local API, bot management logic, and experimental protocol utilities are implemented, with tests covering selected functionality.

A connection to live Agar.io game servers and functional in-game bot behavior have not been implemented or verified. Compatibility with the current game protocol is also unconfirmed.

## Getting Started

### Requirements

- Python 3.14 (used during development)
- pip

### Installation

Clone the repository:

    git clone https://github.com/itsFuRy007/agar-engine.git
    cd agar-engine

Create a virtual environment and install dependencies:

    python -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements.txt

### Run the API

    uvicorn server:app --host 127.0.0.1 --port 8000

### Run Tests

    python -m unittest discover -s tests -v

## Reverse Engineering Notes

Ghidra was used to inspect compiled code, trace function calls, and investigate selected HTTP request and response routines.

## Disclaimer

This is an independent research and learning project. It is not affiliated with or endorsed by Agar.io or its operators.

Use these techniques responsibly and only on systems you are authorized to investigate.
