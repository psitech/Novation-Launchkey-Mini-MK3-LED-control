# https://www.partsnotincluded.com/how-to-control-the-leds-on-a-novation-launchkey-mini-ii/
# https://github.com/giezu/LaunchkeyMiniMK3
# https://mido.readthedocs.io/en/latest/index.html
# https://www.kraftmusic.com/media/ownersmanual/Novation_Launchkey_Programmers_Reference_Manual.pdf

import mido
import random
from time import sleep

row1 = (96, 97, 98, 99, 100, 101, 102, 103)         # LED indices, top row
row2 = (112, 113, 114, 115, 116, 117, 118, 119)     # LED incides, bottom row
leds = row1 + row2                                  # LED indices, combined


def write_led(led_id, led_color):
    midi_out.send(mido.Message('note_on', channel=0, note=led_id, velocity=led_color))


if __name__ == "__main__":
    try:
        midi_out = mido.open_output('MIDIOUT2 (Launchkey Mini MK3 MI 2')  # Launchkey DAW port
        midi_out.send(mido.Message.from_bytes([0x9F, 0x0C, 0x7F]))        # switch to "DAW" mode
    
        while True:
#           color = random.randint(0, 127)
           for color in range(127):
 
                for index, led in enumerate(row1):
                    # Set current LED color
                    write_led(row1[index], color)
                    write_led(row2[index], color)
                    
                    # Turn off last set LEDs
                    write_led(row1[index - 1], 0)
                    write_led(row2[index - 1], 0)
                    sleep(0.05)

    except KeyboardInterrupt:                              # Ctrl-C to exit
        pass


for led in leds:
    write_led(led, 0)  # Turn off all LEDs
    
midi_out.send(mido.Message.from_bytes([0x9F, 0x0C, 0x00]))  # exit "DAW" mode
midi_out.close()
