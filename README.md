
# Text to speech

A brief description of how to start
## Prerequirements

Required Python3 and pip

## Installation

Install pyttsx3 dependency with pip

```
pip install pyttsx3 install
```
    
## Start 

start main.py
```
  python3 main.py
```

Now you can see output.mp3 file and open

## Usage :

```
python3
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
```

**Single line usage with speak function with default options**

```python3
import pyttsx3
pyttsx3.speak("I will speak this text")
```


## Different types of drivers for OS

#### Included TTS engines:

* sapi5 (For windows)
* nsss (For macos)
* espeak (For both)

### Maybe you need install py3-tts

```
pip install py3-tts                                                  
```