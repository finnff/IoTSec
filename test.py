from spherov2 import scanner
from spherov2.toy import mini
from spherov2.sphero_edu import SpheroEduAPI
import tty
import sys
import termios

FileDescriptor = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
pressed = 0

print('Searching for toy...')
toy = scanner.find_toy()
print(f"Toy found: {toy.toy_type.display_name} - {toy.name}")

print("Attempting to connect...")
with SpheroEduAPI(toy) as api:
    print(f'Connected to {toy.name}')
    api.spin(360, 0.1)

    a = True
    esc = 0
    print(f"Press {esc} to exit")
    pressed = 0
    pressed = sys.stdin.read(1)[0]
    api.roll(180, 255, 0.0001)
    api.roll(90, 255, 0.00001)
    api.roll(0, 255, 0.0001)
    api.roll(270, 255, 0.0001)

    print(f'Disconnected from toy {toy.name}')


termios.tcsetattr(sys.stdin, termios.TCSADRAIN, FileDescriptor)
