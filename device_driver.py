from hardware_interface import FlashMemoryDevice


class DeviceDriver:
    """
    This class is used by the operating system to interact with the hardware 'FlashMemoryDevice'.
    """

    def __init__(self, device: FlashMemoryDevice):
        """
        :type device: hardware_interface.FlashMemoryDevice
        """
        self._device = device

    def write(self, address: int, data: int) -> None:
        # TODO: implement this method
        ret = self._device.read(address)
        if ret != 0xFF:
            raise Exception()
        self._device.write(address,data)


    def read(self, address: int) -> int:
        ret = self._device.read(address)
        for i in range(4):
            if self._device.read(address) != ret:
                raise Exception()
        return ret