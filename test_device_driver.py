import pytest
from pytest_mock import MockerFixture

from app import Application
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
    hw = mocker.Mock(spec=FlashMemoryDevice)
    hw.read.return_value = 0xFF
    dd = DeviceDriver(hw)
    dd.write(0x5E,13)
    assert hw.read.call_count == 1


def test_exist_data_when_write(mocker: MockerFixture):
    hw = mocker.Mock(spec=FlashMemoryDevice)
    hw.read.return_value = 0xAA
    dd = DeviceDriver(hw)
    with pytest.raises(Exception):
        dd.write(0x5E, 13)


def test_write_once_when_no_data(mocker: MockerFixture):
    hw = mocker.Mock(spec=FlashMemoryDevice)
    hw.read.return_value = 0xFF
    dd = DeviceDriver(hw)
    dd.write(0x5E, 13)
    assert hw.write.call_count == 1


def test_app_read_operation(mocker: MockerFixture):
    hw = mocker.Mock(spec=FlashMemoryDevice)
    hw.read.return_value = 0xFF
    dd = DeviceDriver(hw)
    app =Application(dd)
    app.read_and_print(0,5)
    assert hw.read.call_count > 0