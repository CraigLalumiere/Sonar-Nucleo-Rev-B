# README #

### What is this repository for? ###

* a template STM32CubeMX project for the Nucleo-G474 development board to make rapid SW prototyping easier
* this allows one to use CubeMX to auto generate code to setup the peripherals
* the following are already setup:
    * ~~clocks configured for maximum core clock~~
    * clocks configured with internal oscillator at maximum core clock (since most of my Nucleo boards have the PF0 pin fried)
    * QP framework with QK kernel
    * LPUART to communicate with Pyton PC com tool via the serial to USB converter built into the ST-link V3 on the nucleo board
    * fault manager
    * reset handler
    * fancy plotting with PC com tool
        * dynamically create new plots
        * add single datapoint to a plot
        * wipe and re-draw entire plot at once
        * draw a bode plot (magnitude + phase on log scale)
        * clear all plots

### Setup ###

* clone this repo to your local WSL directory, e.g. `\\wsl.localhost\Ubuntu\home\clalumiere\Jobs\personal\nucleo-g474-template`
* CD into the newly created directory
* open the directory with VScode `code . `
* In the bottom-right, VS code will prompt you to reopen in devcontainer
* The devcontainer will take considerable time to generate the first time
* select the **[Debug]** build option in the bottom toolbar (wrench + screwdriver icon)
* compile using the 'Build' button in the bottom toolbar (gear icon)
* launch Ozone and connect a J-link debugger to your microcontroller
* open `Nucleo.jdebug` and flash the microcontroller

### Compiling the protobufs ###
* in a terminal (including the terminal inside VS code), type the following
```bash
cd ./messages
./build.sh
```

### Running the Python PC com tool ###
* install Python 3 - [Link](https://www.python.org/ftp/python/3.12.4/python-3.12.4-amd64.exe)
* clone this repo to a local directory in Windows
* open a **command prompt** window in Windows (not powershell)
* CD to your newly cloned repo
```commandline
python -m venv .venv
.venv\Scripts\activate.bat pip install -r requirements.txt
```
* run pc_com.bat

### Updating Python Virtual Environment ###
If additional packages are added to this project, update requirements.txt with 

```commandline
pip freeze > requirements.txt
```

### Updating the GUI ###

The GUI is developed using the QT framework. Open `designer.exe` located in `.venv\Lib\site-packages\PySide6`

The design outputs a `main_window.ui` file, which needs to be converted to python. From the command line, call:

```commandline
GUIRebuild.bat
```



# Contacts

| Person        | Role               | Email                  |
|---------------|--------------------|------------------------|
| Craig Lalumiere | Project Lead       | clalumiere@inertiapd.com |
