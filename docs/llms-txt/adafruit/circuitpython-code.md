# Source: https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/circuitpython-code.md

# Source: https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/circuitpython-code.md

# PIR Motion Sensor

## CircuitPython Code

It's easy to use a PIR sensor with CircuitPython using simple digital inputs.&nbsp; The PIR sensor looks and acts kind of like a button or switch, i.e. it's only ever a high or low logic level, so you don't need any special libraries or other code to read one from Python.&nbsp; It will help to familiarize yourself with [CircuitPython digital inputs and outputs](../../../../circuitpython-digital-inputs-and-outputs) before continuing though!

First make sure your PIR sensor is wired to your board as shown in the previous page.&nbsp; There's no difference wiring a PIR sensor to an Arduino vs. CircuitPython board.&nbsp; You must connect the power, ground, and sensor output to your board.&nbsp; The sensor output should be connected to any digital I/O line on your board.&nbsp; In this example we'll use pin D2 on a Trinket&nbsp;M0.

![](https://cdn-learn.adafruit.com/assets/assets/000/047/592/medium800/proximity_trinket_m0_pir_bb.png?1508891944)

[Fritzing Source](https://cdn-learn.adafruit.com/assets/assets/000/047/593/original/trinket_m0_pir.fzz?1508891968)
Next&nbsp;[connect to the board's serial REPL&nbsp;](../../../../micropython-basics-how-to-load-micropython-on-a-board/serial-terminal)so you are at the CircuitPython&nbsp; **\>\>\>** &nbsp;prompt.

Run the following code to import the **board** and&nbsp; **digitalio** modules which lets you read digital inputs:

```
import board
import digitalio
```

Then create a simple digital input for the PIR.&nbsp; Remember to use the right board pin for how you've wired your sensor to your board.&nbsp; This example is using pin D2 on a Trinket M0:

```
pir = digitalio.DigitalInOut(board.D2)
pir.direction = digitalio.Direction.INPUT
```

At this point you can read the state of the sensor by reading the value property.&nbsp; If the value is at a&nbsp;low logic level, or False, the sensor sees no movement.&nbsp; If it's at a&nbsp;high&nbsp;logic level, or True, the sensor is detecting movement!&nbsp;

Note you'll likely want the sensor's jumper in the H position for retriggering mode as mentioned on the previous page.

For example with no movement in front of the sensor you might see:

```
pir.value
```

![](https://cdn-learn.adafruit.com/assets/assets/000/047/433/medium800/proximity_Screen_Shot_2017-10-20_at_3.10.07_PM.png?1508537424)

Then wave your hand in front of the sensor, and as you wave it run the same command again.&nbsp; Notice you get a True result!

```
pir.value
```

![](https://cdn-learn.adafruit.com/assets/assets/000/047/434/medium800/proximity_Screen_Shot_2017-10-20_at_3.11.31_PM.png?1508537506)

That's all there is to using a PIR sensor with CircuitPython!

Here's a complete example just like from the previous page where movement from the PIR sensor will turn on the board's LED and print a message.&nbsp; This is a direct port of the previous page's Arduino example to CircuitPython.&nbsp; Try saving it as a **main.py** on your board and connecting to the serial terminal to see the output as it runs! (be sure to change the board pin numbers to your sensor and LED wiring!)

```
import board
import digitalio

LED_PIN = board.D13  # Pin number for the board's built in LED.
PIR_PIN = board.D2   # Pin number connected to PIR sensor output wire.

# Setup digital input for PIR sensor:
pir = digitalio.DigitalInOut(PIR_PIN)
pir.direction = digitalio.Direction.INPUT

# Setup digital output for LED:
led = digitalio.DigitalInOut(LED_PIN)
led.direction = digitalio.Direction.OUTPUT

# Main loop that will run forever:
old_value = pir.value
while True:
    pir_value = pir.value
    if pir_value:
        # PIR is detecting movement! Turn on LED.
        led.value = True
        # Check if this is the first time movement was
        # detected and print a message!
        if not old_value:
            print('Motion detected!')
    else:
        # PIR is not detecting movement. Turn off LED.
        led.value = False
        # Again check if this is the first time movement
        # stopped and print a message.
        if old_value:
            print('Motion ended!')
    old_value = pir_value
```

- [Previous Page](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/using-a-pir-w-arduino.md)
- [Next Page](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/example-projects.md)

## Primary Products

### PIR (motion) sensor

[PIR (motion) sensor](https://www.adafruit.com/product/189)
PIR sensors are used to detect motion from pets/humanoids from about 20 feet away (possibly works on zombies, not guaranteed). This one has an adjustable delay before firing (approx 2-4 seconds), adjustable sensitivity **and** we include a 1 foot (30 cm) cable with a socket so you...

In Stock
[Buy Now](https://www.adafruit.com/product/189)
[Related Guides to the Product](https://learn.adafruit.com/products/189/guides)

## Related Guides

- [HalloWing All-Seeing Skull](https://learn.adafruit.com/hallowing-all-seeing-skull.md)
- [Magical Mistletoe](https://learn.adafruit.com/magical-mistletoe.md)
- [Screaming Cauldron](https://learn.adafruit.com/screaming-cauldron.md)
- [IoT Bird Feeder with Camera](https://learn.adafruit.com/iot-window-bird-feeder-with-camera.md)
- [No-Code WipperSnapper Summoning Horn](https://learn.adafruit.com/adafruit-io-wippersnapper-summoning-horn.md)
- [Motion Controlled Matrix Bed Clock](https://learn.adafruit.com/motion-controlled-matrix-bed-clock.md)
- [Adafruit VCNL4020 Proximity and Light Sensor](https://learn.adafruit.com/adafruit-vcnl4020-proximity-and-light-sensor.md)
- [Fog Machine with Motion Sensor and Adafruit IO](https://learn.adafruit.com/fog-machine-remote-trigger.md)
- [Feather Freezer Door Alarm](https://learn.adafruit.com/feather-door-alarm.md)
- [MIDI Laser Harp with Time of Flight Distance Sensors](https://learn.adafruit.com/midi-laser-harp-time-of-flight-sensors.md)
- [Using Adafruit IO Actions to Make an IoT Door Detector](https://learn.adafruit.com/using-adafruit-io-actions-to-make-an-iot-door-detector.md)
- [Quadcopter Spray Can Mod](https://learn.adafruit.com/quadcopter-spray-can-mod.md)
- [Adafruit VCNL4040 Proximity Sensor](https://learn.adafruit.com/adafruit-vcnl4040-proximity-sensor.md)
- [Using ItsaSNAP for HomeKit PIR Motion Detection](https://learn.adafruit.com/itsasnap-homekit-pir-motion-detection.md)
- [No-Code Room Occupancy Status ](https://learn.adafruit.com/no-code-room-occupancy-status.md)
