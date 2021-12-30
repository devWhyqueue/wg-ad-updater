# WG Request Updater

Keeps your WG Request always at the top of the search hit list!

# Prerequisites

- Venv: `python3 -m pip install --user virtualenv`
- Poetry: `python3 -m pip install poetry`

# Installation

Create and activate venv:

```
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```
poetry install
```

# Usage

Execute main.py as a background process and log to file:

```
nohup python3 wgrequestupdater/main.py {USERNAME} {PASSWORD} >> wgrequestupdater-info.log 2>> wgrequestupdater-error.
log &
```

To stop:

```
pkill -f wgrequestupdater
```
