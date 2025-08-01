import pytest
from hardware_interface import FlashMemoryDevice
from device_driver import DeviceDriver

def test_successful_read(mocker):
    hardware: FlashMemoryDevice = mocker.Mock()
    driver = DeviceDriver(hardware)
    assert driver.read(0xFF) == 0x0
