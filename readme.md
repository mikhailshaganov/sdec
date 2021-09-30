
# 🎛 SDEC

Basic CLI for interfacing with the custom PCBs developed by Sun Devil Rocketry

## Sun Devil Embedded Controller

The Sun Devil Embedded Controller CLI is a simple program for interfacing with embedded systems in the custom PCB's and other software written for the ASU student club Sun Devil Rocketry (SDR). This project is written in python using the libraries click and pyserial among others.

# Building / Running

- Ensure you have [poetry](https://python-poetry.org/) installed.
- Clone the project.
- Run `poetry install` then `poetry shell` to set up then enter the virtual environment.
- Plug SDR PCB into your computer.
- Run `sdec dump` to dump information about the processor / PCB.
