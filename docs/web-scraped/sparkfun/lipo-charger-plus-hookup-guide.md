# Source: https://learn.sparkfun.com/tutorials/lipo-charger-plus-hookup-guide

## Introduction

The [SparkFun LiPo Charger Plus](https://www.sparkfun.com/products/15217) is the souped-up power option in the SparkFun line of single-cell lithium polymer (LiPo) battery chargers. With this iteration, we\'ve changed the input charge connector to USB-C and provided charge rate selection as well as optional thermal protection. Charge, power, and done LEDs clearly indicate the status of your charging process.

Got a battery? Let\'s charge!

[![SparkFun LiPo Charger Plus](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/6/5/8/15217-SparkFun_LiPo_Charger_Plus-02.jpg)](https://www.sparkfun.com/sparkfun-lipo-charger-plus.html)

### [SparkFun LiPo Charger Plus](https://www.sparkfun.com/sparkfun-lipo-charger-plus.html) 

[ PRT-15217 ]

The SparkFun LiPo Charger Plus is the suped-up power option in the SparkFun line of single-cell lithium polymer (LiPo) batter...

[ [\$11.75] ]

### Required Materials

All that is needed to charge a LiPo battery sufficiently is a [micro-C USB cable](https://www.sparkfun.com/products/14743) to connect to either a computer USB port or a [wall adapter](https://www.sparkfun.com/products/11456).

[![USB 3.1 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html)

### [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html) 

[ CAB-14743 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

[ [\$7.95] ]

[![USB Wall Charger - 5V, 1A (Black)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/3/1/0/11456-USB_Wall_Charger_-_5V__1A__Black_-01.jpg)](https://www.sparkfun.com/usb-wall-charger-5v-1a-black.html)

### [USB Wall Charger - 5V, 1A (Black)](https://www.sparkfun.com/usb-wall-charger-5v-1a-black.html) 

[ TOL-11456 ]

USB is being implemented as a power connection standard more and more these days, but you don\'t always have a computer on han...

[ [\$5.95] ]

[![USB 2.0 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/5/0/15092-USB_2.0_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/products/15092)

### [USB 2.0 Cable A to C - 3 Foot](https://www.sparkfun.com/products/15092) 

[ CAB-15092 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

**Retired**

A few LiPo batteries with nominal 3.7V from our catalog:

[![Lithium Ion Battery - 110mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/0/13853-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-110mah.html)

### [Lithium Ion Battery - 110mAh](https://www.sparkfun.com/lithium-ion-battery-110mah.html) 

[ PRT-13853 ]

This is a very small, extremely light weight battery based on Lithium Ion chemistry. This is the highest energy density curre...

[ [\$7.53] ]

[![Lithium Ion Battery - 850mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/1/13854-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-850mah.html)

### [Lithium Ion Battery - 850mAh](https://www.sparkfun.com/lithium-ion-battery-850mah.html) 

[ PRT-13854 ]

These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 850...

[ [\$13.61] ]

[![Lithium Ion Battery - 400mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/5/8/13857-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-400mah.html)

### [Lithium Ion Battery - 400mAh](https://www.sparkfun.com/lithium-ion-battery-400mah.html) 

[ PRT-13851 ]

This is a very small, extremely lightweight battery based on Lithium Ion chemistry, with the highest energy density currently...

[ [\$7.98] ]

[![Lithium Ion Battery - 1Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/0/1/13813-01.jpg)](https://www.sparkfun.com/products/13813)

### [Lithium Ion Battery - 1Ah](https://www.sparkfun.com/products/13813) 

[ PRT-13813 ]

Slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 1000 mAh!

**Retired**

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/battery-technologies)

### Battery Technologies 

The basics behind the batteries used in portable electronic devices: LiPo, NiMH, coin cells, and alkaline.

[](https://learn.sparkfun.com/tutorials/alternating-current-ac-vs-direct-current-dc)

### Alternating Current (AC) vs. Direct Current (DC) 

Learn the differences between AC and DC, the history, different ways to generate AC and DC, and examples of applications.

## Hardware Overview

For a quick reference, here is an annotated diagram of the parts used on the LiPo Charger Plus:

[![Highlighted top view of board](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/4/15217-LiPo_Charger_Highlights_withArrowsandNumbers_fixed.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/4/15217-LiPo_Charger_Highlights_withArrowsandNumbers_fixed.jpg)

  ------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Number**   **Description**
  1            **Charge Input** - The input voltage for the MCP73833 charger IC is between **3.75 to 6V**. To fully charge the battery, it is recommended to have a voltage around 5V. The charge IC will regulate the voltage down to safely charge the LiPo battery.
  2            **Power LED** - When power is supplied this red LED should turn on. The LED is connected to the active low PG (power good) pin, which is active whenever the input to charger is about the UVLO (3.7V) threshold and greater than the battery voltage.
  3            **Charge LED** - When a battery is connected and the charge controller is charging the battery, this LED will turn on, and should be off otherwise.
  4            **Done LED** - After the battery has reached a full charge, this LED will turn on, and should be off otherwise.
  5            **Charge Rate Select** - Programmable current regulation (**default: 1kΩ**). Selects the maximum amount of current to charge the battery. **For a detailed explanation, see the charge rate setting section of this guide**.
  6            **Thermistor Input** - An internal 50 µA current source provides the bias for most common 10kΩ negative-temperature coefficient thermistors (NTC). The MCP73833 compares the voltage at the THERM pin to factory set thresholds of 1.20V and 0.25V, typically. **If using a NTC thermistor, the 10kΩ SMD resistor should be removed**.
  7            **Battery Input** - A single-cell LiPo battery can be connected to either the JST connector, or PTH pins. If using the PTH pins, pay close attention to the polarity of the battery/battery holder, as connecting a LiPo battery backwards to the charger will destroy the IC.
  ------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\

### Status LEDs

The LiPo Charger Plus has three LEDs, a red LED for power, and two status LEDs. Most of the time the charge LED will turn on when the board is charging a battery, and turn off when the board is done charging. The done LED will turn off when the board is charging and turn on when done charging. For a full list of LED status indicators, refer to the table below.

  ------------------------ -------- ---------- ---------
  **Charge Cycle State**   Charge   **Done**   **PWR**
  Shutdown                 OFF      OFF        OFF
  Standby                  OFF      OFF        ON
  Charge In Progress       ON       OFF        ON
  Charge Complete          OFF      ON         ON
  Temperature Fault        OFF      OFF        ON
  Timer Fault              OFF      OFF        ON
  System Test Mode         ON       ON         ON
  ------------------------ -------- ---------- ---------

\

### Setting a Different Charge Rate

Lithium batteries should be charged at a rate no higher than 1C (eg. a 400mAh battery should be charged no faster than 400mA). The LiPo Charger Plus has a 1kΩ SMD resistor populated, which sets the charge rate at the maximum 1000mA. If your battery is smaller than 1000mAh, this resistor should be removed and replaced with an appropriate resistor. To determine the correct resistor value, use the formula or lookup table below:

\

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/4/LipoChargeRateEquation.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/4/LipoChargeRateEquation.png)

\
\

  ---------------- -----------------
  **I_REG (mA)**   **R_PROG (kΩ)**
  1000             1.00
  900              1.11
  800              1.25
  700              1.43
  600              1.67
  500              2.00
  400              2.50
  300              3.33
  200              5.00
  100              10.0
  ---------------- -----------------

\

### Over Temperature Protection

The MCP73833 has two forms of thermal protection, one for the charge controller itself and the other for the battery. The charge controller has an internal temperature sensor to maximize the current charge rate up to the programmed charge rate without over heating. When the die temperature of the MCP73833 reaches \~95°C, the charge controller will reduce the charge rate to prevent over heating. Over heating is most likely to occur at the beginning of a charge when the battery\'s voltage is the lowest. As the difference between the supply voltage and the battery voltage decreases, the die temperature will decrease and allow the charge current to increase up to the programmed charge rate.

[![Graph of charge current vs junction temperature](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/4/Charge_Current_vs_Junction_TemperatureCropped.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/4/Charge_Current_vs_Junction_TemperatureCropped.PNG)

**Charge Current(I~out~) vs Junction Temperature(T~J~)**

*Image pulled from [MCP73833 Datasheet](https://cdn.sparkfun.com/assets/b/a/7/6/8/MCP73833Datasheet.pdf)*

The other temperature sensor is optionally available for the battery. The MCP73833 has an input pin for a [thermistor](https://www.sparkfun.com/products/250) which can be attached to the battery using a [high temperature tape](https://www.sparkfun.com/products/10687). The thermistor that the charge controller is designed to use is a negative-temperature coefficient (NTC), which decreases it\'s resistance as the temperature increases. If sourcing your own NTC thermistor, look for a NTC thermistor with a resistance of 10kΩ at 25°C. To connect a NTC thermistor, remove the 10kΩ SMD resistor and solder the leads of the NTC to the PTH resistor pads highlighted below.

[![Highlight of Thermistor Pads](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/4/Thermistor_Pins_Highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/4/Thermistor_Pins_Highlight.jpg)

### Adding a Heatsink

If the charge rate isn\'t getting up to the programmed charge rate, the IC is most likely overheating and limiting the current to the battery. One of the easiest ways to solve this is to add a [heatsink](https://www.sparkfun.com/products/11510) with our [thermal tape](https://www.sparkfun.com/products/17054). On the bottom of the board is an exposed pad underneath the MCP73833.

[![Highlight of exposed pad on back of board](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/4/Exposed_Pad_Highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/4/Exposed_Pad_Highlight.jpg)

To add a heatsink first cut the thermal tape to rough size:

[![Thermal tape cut to rough size](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/4/LiPo_Charger_Plus_Heatsink_Rough_Size.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/4/LiPo_Charger_Plus_Heatsink_Rough_Size.jpg)

Peel off one of the protective coverings and attach heatsink to thermal tape:

[![Heatsink connected to thermal tape](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/4/LiPo_Charger_Plus__Heatsink_Connected_to_tape.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/4/LiPo_Charger_Plus__Heatsink_Connected_to_tape.jpg)

With a [hobby knife](https://www.sparkfun.com/products/9200), follow the perimeter of the heatsink to cut the tape to it\'s final size:

[![Cutting thermal tape](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/4/LiPo_Charger_Plus_cut_to_size.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/4/LiPo_Charger_Plus_cut_to_size.jpg)

Remove the remaining protective covering of the tape and attach the heatsink to the exposed pad. If using a standoff, you may want to attach the standoff first to make sure you have enough clearance between the standoff and the heatsink.

[![Heatsink attached to board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/4/LiPo_Charger_Plus_Heatsink1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/4/LiPo_Charger_Plus_Heatsink1.jpg)

## Troubleshooting

[] **Need help?**\
\
If your product is not working as you expected or you need technical assistance or information, head on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.