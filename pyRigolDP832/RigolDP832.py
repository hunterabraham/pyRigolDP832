import numpy as np
from .baseClasses import VisaSupply


class RigolDP832(VisaSupply):

    def __init__(self, iface):
        self._iface = iface
        self._voltage = 0
        self._current = 0
        self._power = 0
        self._channel = 'ch1'
        self._ocp = 0

    def get_voltage(self):
        return self._iface.query(":meas?")

    def get_channel(self):
        return self._channel

    def get_current(self):
        return self._iface.query(":meas:curr?")

    def get_power(self):
        return self._iface.query(":meas:power?")

    def set_voltage(self, voltage):
        self._voltage = voltage

    def set_channel(self, channel):
        self._channel = channel

    def set_current(self, current):
        self._current = current

    def set_power(self, power):
        self._power = power

    def set_ocp(self, ocp):
        self._ocp = ocp

    def get_ocp(self):
        return self._ocp

    def apply_all(self):
        return self._iface.write(":appl " + str(self._channel) + ", " + str(self._voltage) + ", " + str(self._current))

    def apply_ocp(self):
        return self._iface.write(":outp:ocp:val " + str(self._channel) + "," + str(self._ocp))
