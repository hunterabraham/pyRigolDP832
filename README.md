# RigolDP832
Class to remotely control Rigol DP832 Programmable DC Power Supply

# Methods

## Getting settings

### get\_voltage()
Returns the current voltage setting

### get\_channel()
Returns the current channel being controlled

### get\_power()
Returns the current power setting

### get\_ocp()
Returns the current ocp setting

## Setting settings
Methods to manipulate the power supply using SCPI commands

### set\_voltage()
Sets the voltage setting

### set\_channel()
Sets the channel being manipulated

### set\_current()
Sets the current

### set\_power()
Sets the power

### set\_ocp()
Sets the OCP setting

## Applying settings

### apply\_all()
Apply all settings

### apply\_ocp()
Apply ocp setting

# Usage
`git clone https://github.com/hunterabraham/pyRigolDP832`
`cd pyRigolDP832`
`python -m pip install -e .`
