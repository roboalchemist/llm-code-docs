# Source: https://learn.adafruit.com/adafruit-gfx-graphics-library/rotating-the-display.md

# Adafruit GFX Graphics Library

## Rotating the Display

You can also rotate your drawing. Note that this will _not_ rotate what you already drew, but it will change the coordinate system for any new drawing. This can be really handy if you had to turn your board or display sideways or upside down to fit in a particular enclosure. In most cases this only needs to be done once, inside setup().

We can only rotate 0, 90, 180 or 270 degrees - anything else is not possible in hardware and is too taxing for an Arduino to calculate in software  

![](https://cdn-learn.adafruit.com/assets/assets/000/001/266/medium800/lcds___displays_rotated.jpg?1396770456)

```
void setRotation(uint8_t rotation);
```

The **rotation** parameter can be **0** , **1** , **2** or **3**. For displays that are part of an Arduino shield, rotation value 0 sets the display to a _portrait_ (tall) mode, with the USB jack at the top right. Rotation value 2 is also a portrait mode, with the USB jack at the bottom left. Rotation 1 is _landscape_ (wide) mode, with the USB jack at the bottom right, while rotation 3 is also landscape, but with the USB jack at the top left.

For other displays, please try all 4 rotations to figure out how they end up rotating as the alignment will vary depending on each display, in general the rotations move counter-clockwise

When rotating, the origin point (0,0) changes — the idea is that it should be arranged at the top-left of the display for the other graphics functions to make consistent sense (and match all the function descriptions above).

If you need to reference the size of the screen (which will change between portrait and landscape modes), use width() and height().

```
uint16_t width(); 
uint16_t height();
```

Each returns the dimension (in pixels) of the corresponding axis, adjusted for the display’s current rotation setting.

- [Previous Page](https://learn.adafruit.com/adafruit-gfx-graphics-library/graphics-primitives.md)
- [Next Page](https://learn.adafruit.com/adafruit-gfx-graphics-library/using-fonts.md)

## Related Guides

- [AdaBox 019](https://learn.adafruit.com/adabox019.md)
- [Sous-vide controller powered by Arduino - The SousViduino!](https://learn.adafruit.com/sous-vide-powered-by-arduino-the-sous-viduino.md)
- [Adafruit 128x64 OLED Bonnet for Raspberry Pi](https://learn.adafruit.com/adafruit-128x64-oled-bonnet-for-raspberry-pi.md)
- [Adafruit IO IOT Hub with the Adafruit FunHouse](https://learn.adafruit.com/adafruit-io-hub-with-the-adafruit-funhouse.md)
- [HalloWing Flapping Bat](https://learn.adafruit.com/hallowing-flapping-bat.md)
- [CircuitPython OLED and Dual Knob Sketcher](https://learn.adafruit.com/circuitpython-oled-knob-sketcher.md)
- [Monochrome OLED Breakouts](https://learn.adafruit.com/monochrome-oled-breakouts.md)
- [4x4 Rotary Encoder MIDI Messenger](https://learn.adafruit.com/4x4-rotary-encoder-midi-messenger.md)
- [Pico W HTTP Server with CircuitPython](https://learn.adafruit.com/pico-w-http-server-with-circuitpython.md)
- [Capturing Camera Images with CircuitPython](https://learn.adafruit.com/capturing-camera-images-with-circuitpython.md)
- [WiFi OLED Display Badge](https://learn.adafruit.com/digital-display-badge.md)
- [Trinket Ultrasonic Rangefinder](https://learn.adafruit.com/trinket-ultrasonic-rangefinder.md)
- [PyPortal Adafruit Quote Book](https://learn.adafruit.com/pyportal-adafruit-quote-board.md)
- [2.8" TFT Touchscreen](https://learn.adafruit.com/2-8-tft-touchscreen.md)
- [Magic Storybook with ChatGPT](https://learn.adafruit.com/magic-storybook-with-chatgpt.md)
