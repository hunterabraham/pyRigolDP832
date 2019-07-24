class VisaSupply:

    @property
    def IDN(self):
        if self._iface is not None:
            return self._iface.query("*IDN?")
        else:
            return 'No ID returned, there may be a connection problem.'

    def ready_for_command(self):
        if self._iface is not None:
            return self._iface.query("*OPC?")
        return 0

    def set_voltage(self, voltage):
        raise Exception("set_voltage not implemented")

    def set_current(self, current):
        raise Exception("set_current not implemented")

    def set_channel(self, channel):
        raise Exception("set_channel not implemented")

    def set_power(self, power):
        raise Exception("set_power not implemented")

    def get_voltage(self):
        raise Exception("get_voltage not implemented")

    def get_current(self):
        raise Exception("get_current not implemented")

    def get_channel(self):
        raise Exception("get_channel not implemented")

    def get_power(self):
        raise Exception("get_power not implemented")
