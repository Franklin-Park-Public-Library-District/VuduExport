# VuduExport
Tool for exporting CSV list of owned and wanted Movies and TV Shows from Vudu

## Requirements
- [python2](https://www.python.org/downloads/release/python-2718/)
- python2-requests

## Usage
### On Windows
1. Download Python2 for Windows, or use the Windows Subsystem for Linux or similar software.
2. Then follow the general steps below.

### On macOS
1. Download Python2 for macOS via Python.org, Homebrew, or MacPorts.
2. Then follow the general steps below.

### On Linux (Ubuntu 20.04 in this case)
1. Download Python2 via Ubuntu's universe repository.
3. Then follow the general steps below.

### General
1. Open a Terminal or Command Prompt (that has $PATH access to Python2).
2. Download the script, `$ git clone https://github.com/Franklin-Park-Public-Library-District/VuduExport`.
3. Edit `credentials.txt`.
4. Download `requests` with `$ pip2 install requests`.
5. For movies, run `$ python2 vudu.py`.
6. For TV shows, run `$ python2 vudu-tv.py`.

# Credits
All credit goes to [this script](https://gist.github.com/eviljim/9bb40c273d15d755a66c) from eviljim for creating the original `vudu.py`.
`vudu-tv.py` is just modified to query Vudu's API for TV Shows, rather than Movies.
