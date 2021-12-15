from spherov2 import scanner
from spherov2.toy import mini
from spherov2.sphero_edu import SpheroEduAPI
import tty, sys, termios

FileDescriptor = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
pressed = 0

print('Searching for toy...')
toy = scanner.find_toy()
print(f"Toy found: {toy.toy_type.display_name} - {toy.name}")

print("Attempting to connect...")
with SpheroEduAPI(toy) as api:
    print(f'Connected to {toy.name}')
    api.spin(360,0.1)

    a = True
    esc = 0
    print(f"Press {esc} to exit")
    while a:
        pressed = 0
        pressed =sys.stdin.read(1)[0]
        match pressed:
            case "w":
                api.roll(180, 255, 0.0001)
                continue
            case "a":
                api.roll(90, 255, 0.00001)
                continue
            case "s":
                api.roll(0, 255, 0.0001)
                continue
            case "d":
                api.roll(270, 255, 0.0001)
                continue
            case esc:
                api.stop_roll()
                a = False
                continue
        
    print(f'Disconnected from toy {toy.name}')




termios.tcsetattr(sys.stdin, termios.TCSADRAIN, FileDescriptor)