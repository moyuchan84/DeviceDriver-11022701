from device_driver import DeviceDriver


class Application:
    def __init__(self,device:DeviceDriver):
        self._device = device

    def read_and_print(self,start_addr,end_addr):
        self._device.read(start_addr)

    def write_all(self,value): ...