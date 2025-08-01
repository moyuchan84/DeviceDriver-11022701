import pytest
from pytest_mock import MockerFixture

from device_driver import DeviceDriver
from hardware_interface import FlashMemoryDevice


def test_read_five_times(mocker: MockerFixture):
    hw = mocker.Mock(spec=FlashMemoryDevice)
    dd = DeviceDriver(hw)

    dd.read(0x5E)

    assert hw.read.call_count == 5


def test_read_successful(mocker: MockerFixture):
    hw = mocker.Mock(spec=FlashMemoryDevice)
    dd = DeviceDriver(hw)
    hw.read.return_value = 10

    ret = dd.read(0x5E)

    assert ret == 10

@pytest.mark.parametrize("lst", [
    (10,10,10,10,5),
    (10,10,5,10,10),

])
def test_read_failure(mocker: MockerFixture,lst):
    hw = mocker.Mock(spec=FlashMemoryDevice)
    dd = DeviceDriver(hw)
    hw.read.side_effect = lst

    with pytest.raises(Exception):
        dd.read(0x5E)

def test_read_once_when_write(mocker: MockerFixture):
    ...