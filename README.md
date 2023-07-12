# README #

### What is this repository for? ###

This is something I made when I was super sick and lost my voice. 

Once setup, usage is as simple as updating a file (`speech.txt`) and running the program (`python main.py`) again.

### Quick Start ###

* Install Python
* Optional: set up virtual environment
  * Create virtual environment (`python -m venv venv`)
  * Activate virtual environment (`source ./venv/bin/activate`)
  * See [here](https://python.land/virtual-environments/virtualenv) for beginner-friendly explanation and [here](https://docs.python.org/3/library/venv.html) for reference.
* `pip install pyttsx3`
* Change speech.txt to whatever you want!
* `python main.py`

### Voice Selection ###
The `VOICE_INDEX` variable defined in `main.py` indicates which voice to use. You can hear other voices by passing in a different voice index. `main` also has `find_voices`, which lets you try different text with different language bases to hear different choices. 

Note that if you want to dive into more detail, the function `find_voices` in `helper.py` can go through all voices available. You can use that to identify the voice you want as your own and change the `VOICE_INDEX`.
