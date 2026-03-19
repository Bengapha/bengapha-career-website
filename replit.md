# bengapha-career-website

## Project Overview
A Python OOP demonstration script that checks network connectivity to several hosts (google.com, github.com, cloudflare.com). Despite the repository name suggesting a career website, the current codebase is a simple Python console script.

## Tech Stack
- **Language:** Python 3.12
- **Libraries:** Standard library only (`socket`, `datetime`)
- **Runtime:** Nix (stable-25_05 channel)

## Project Structure
```
OOPclass.py   - Main script: defines Target class and runs connectivity checks
README.md     - Project description
LICENSE       - MIT License
.replit       - Replit environment configuration
```

## Running the Project
The workflow "Start application" runs:
```
python OOPclass.py
```
Output appears in the console showing hostname, IP, status, and timestamp for each target.
