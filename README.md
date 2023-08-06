# Vince Garden

This repository holds the software that automates the garden of Vincent. It should be able to configure **when** plants will be watered and **how long**.

Also the system should not work anymore when a certain threshold of water is consumed in the water tank.

The user should be able to change these different parameters through a user interface, accesible through a touch screen. It is not necessary to do a "connected" thing, vincent does not have a wifi router, even if he has a smartphone that could be used as a AP.

## Material

- Raspberry PI 3B
- Touch screen
- 4 solenoid valves
- 4 relay
- 4 flow meter
- 1 hygrometric probe

## Software

The software will use **python** with **Qt** framework (to avoid cross compilation). It will have access to the GPIO to activated the different relays, according to the programed timing set.

```
pip3 install pyside6
```

