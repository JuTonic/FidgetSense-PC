from dataclasses import dataclass
import serial

PORT = '/dev/serial/by-id/usb-1a86_USB_Serial-if00-port0'
BAUDRATE = 115200
TIMEOUT = 1

ser = serial.Serial(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT)

@dataclass
class Entry:
    time: int
    x: int
    y: int
    z: int

    @staticmethod
    def parse(line: str) -> "Entry":
        time, x, y, z = line.strip().split(";")
        return Entry(int(time), int(x), int(y), int(z))


while True:
    line = ser.readline().decode('utf-8', errors='ignore')
    if line:
        entry = Entry.parse(line)
        print(entry)
