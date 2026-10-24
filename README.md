# Agar Engine

A network protocol research project exploring client-server communication, WebSockets, binary packet handling, and reverse engineering.

The goal of this project is to investigate how networked game systems communicate, understand the structure of protocol messages, and experiment with the components involved in client-server interactions.

## Areas of Research

### Network Communication
- Explored secure WebSocket client implementation.
- Examined the structure of client-server communication.
- Built a local API to manage bot-related operations.

### Protocol Analysis
- Experimented with binary packet construction.
- Implemented experimental XOR and LZ4 processing utilities.
- Wrote tests to validate selected protocol-helper behavior.

### Reverse Engineering
- Used Ghidra to inspect compiled binaries and trace selected functions.
- Investigated HTTP request construction and response handling.
- Examined communication flows to better understand how software components interact.

### Development and Testing
- Implemented bot lifecycle and state management.
- Built a local API using FastAPI.
- Added unit tests for bot-management logic and protocol utilities.

## Technologies and Tools

- **Networking:** WebSockets, HTTP, client-server architecture
- **Programming:** Python
- **Frameworks:** FastAPI, Pydantic, Uvicorn
- **Data Processing:** Binary packet handling, XOR, LZ4
- **Reverse Engineering:** Ghidra
- **Testing:** Python unittest
- **Version Control:** Git and GitHub

## Current Status

This project is an ongoing research prototype.

The local API, bot-management components, WebSocket client foundation, and experimental protocol utilities have been implemented to varying degrees.

Live connectivity to Agar.io game servers has not been implemented or verified. Compatibility between the experimental protocol utilities and the current production game protocol remains unconfirmed.

The existing tests cover selected local management and protocol-helper functionality; they do not establish compatibility with live servers.

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

The API listens on localhost.

### Run Tests

    python -m unittest discover -s tests -v

## Disclaimer

This is an independent research project and is not affiliated with or endorsed by Agar.io or its operators.

All research and testing should be conducted responsibly and within the scope of authorized systems.
