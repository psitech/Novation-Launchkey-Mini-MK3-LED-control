# Novation Launchkey Mini MK3  LED control

This Python code is a fork from [Dave Madison's code](https://www.partsnotincluded.com/how-to-control-the-leds-on-a-novation-launchkey-mini-ii/) that he wrote for the MK2.

For the MK3, the MIDI message to get into "DAW mode" was changed from **0x90**, 0x0C, 0x7F to **0x9F**, 0x0C, 0x7F.

To find the exact portname for opening the MK3 on your OS, you can use the following REPL commands:
```
>>> import mido
>>> mido.get_output_names()
```

The available colour palette can be found in the Novation Launchkey MK3 Programmers Reference Manual.
