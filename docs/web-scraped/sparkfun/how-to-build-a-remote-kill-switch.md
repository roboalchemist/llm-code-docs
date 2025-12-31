# Source: https://learn.sparkfun.com/tutorials/how-to-build-a-remote-kill-switch

## When Things Get Out of Control

[![The remote control kill switch](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/2/Kill_Switch_Images-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/2/Kill_Switch_Images-01.jpg)

*Kill Switches: It\'s not a question of if, but when.*

I highly recommend building something that scares you every once and awhile. In this case, I'm planning to enter an autonomous vehicle into the [AVC in 2016](https://avc.sparkfun.com/), and it\'s pushing my limits of comfort. A 1,000W motor with a large battery pack behind it mean that if things go wrong, it could be dangerous. For that reason, one of the new safety requirements of the AVC is a remote kill switch that allows the user to remotely power down the vehicle. This tutorial is my solution to safely disconnecting the motor from the motor controller in case things get out of control\...

ReplaceMeOpen

ReplaceMeClose

Here\'s a quick video showing the kill switch controlling the 1kW motor (that just happens to be attached to a blender).

## System Requirements

Here are the design requirements for my system. These should fulfill the kill switch safety requirements of the [A+PRS rules](https://avc.sparkfun.com/2016/rules#APRS_StopSwitch).

- If user presses the green button the system should energize the cut-off relay allowing power to flow to the motor.
- If user presses the red button the system should de-energize the cut-off relay shorting the + and - of the motor causing the motor to brake.
- If user presses the yellow button the system should assert a signal pin. This will be connected to the master controller to let it know that the race is in "yellow flag" mode.
- If the vehicle fails to hear from the remote after a certain length of time the vehicle should go into safety-shutdown (de-energize the cut-off relay causing engine to brake).
- If the remote fails to hear a response from the vehicle (out of range), then go into disconnect mode (blink all three LEDs).
- If the link is re-established, then start in safety-shutdown mode.

I broke the killswitch system into two parts: the **Vehicle Control Unit** that lives on the vehicle and the **Remote Control Unit** that the human holds in their hand.

[![Remote control electronics](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/2/Kill_Switch_Images-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/2/Kill_Switch_Images-02.jpg)

*The electronics in the hand held remote (RCU)*

[![Vehicle Control Electronics](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/2/Kill_Switch_Images-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/2/Kill_Switch_Images-03.jpg)

*The electronics on the vehicle (VCU)*

## VCU Parts List

[![Vehicle Control Unit Electronics](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/2/Kill_Switch_Images-03-VCU.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/2/Kill_Switch_Images-03.jpg)

*Click on the image to see the electronics without highlighting*

The Beefcake Relay can be seen next to the larger, blue, 24V/80A relay. The VCU itself (the Pro Mini connected to the RFM69 breakout board) can be seen in the lower right corner.

Parts used on the Vehicle Control Unit:

- [Arduino Pro Mini 328 - 3.3V/8MHz](https://www.sparkfun.com/products/11114)
- [RFM69 Breakout](https://www.sparkfun.com/products/12823)
- [Beefcake Relay Control Kit](https://www.sparkfun.com/products/11042)
- [24VDC 80A Relay](http://www.ebay.com/itm/270773291995)
- [48V to 24V DC to DC Buck Converter](http://www.amazon.com/gp/product/B00XKL6M8U)
- [48V to 5V DC to DC Buck Converter](http://www.amazon.com/GERI-Converter-Module-8-50V-Output/dp/B00W52N8XW)
- A handful of [3-Pin](https://www.sparkfun.com/products/9915) and [2-pin](https://www.sparkfun.com/products/9914) JST Jumper Wire Assemblies

I use our [SparkFun RFM69 Breakout](https://www.sparkfun.com/products/12823) for a variety of reasons:

- **Encryption:** This allows me to rest easy that no one else (ok I'm sure someone *could* hack it) will power up/down my car.
- **Software Defined Radio:** The AVC has nearly 100 teams, all with their own radios and telemetry systems. It's excellent to be able to sit in the 434MHz or 915MHz spectrum rather than the very crowded 2.4GHz arena.
- **Data Rate Scaling:** The data rates can be reduced and frequency changed so that range can be increased quite significantly. [UKHASnet](https://ukhas.net/) has even setup a network of RFM69 based repeaters across Europe with transmission ranges pushing 65km (40miles)! I plan to be within sight of my autonomous power wheels at all times, but it's good to know the 100mW transmission power of the RFM69 can do the job.
- **Library Support:** The community has been writing various libraries to support the RFM type modules for years now. The latest I use for this project is [RadioHead by AirSpayce](http://www.airspayce.com/mikem/arduino/RadioHead/). It does everything I need with some decent documentation to boot.

## Vehicle Control Unit

[![Vehicle Control Unit Electronics](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/2/Kill_Switch_Images-03-VCU.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/2/Kill_Switch_Images-03-VCU.jpg)

*RFM69, Arduino Pro Mini, and two relays make up the VCU*

The Vehicle Control Unit (VCU) sits between the [motor controller](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/2/Kill_Switch_Images-06.jpg) and the motor. The VCU only connects the motor to power if the Remote Control Unit (RCU) is powered up and transmitting the *'User pressed the green button, go for it'* signal.

I've decided to run my PRS vehicle at 48V, which is the higher end of allowed system voltages. Luckily, there are some really nice DC to DC buck converters to get 48V down to 24V (to control the cut-off relay) and 5V (to power the 3.3V Pro Mini). See the [parts list](https://learn.sparkfun.com/tutorials/how-to-build-a-remote-kill-switch#vcu-parts-list) for links to the particular ones I used.

[![Relay up close](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/2/Kill_Switch_Images-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/2/Kill_Switch_Images-04.jpg)

Under load and at top speed, the motor controller will be putting out 10\'s of amps at 48V. The VCU needs a substantial relay big enough to handle that load. Some of the lowest cost, highest current relays I could find were 24V relays. Because my 3.3V/8MHz Pro Mini can only turn on/off 3.3V, I decided to use a two relay setup.

[![Bootstrapped two relay setup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/2/KillSwitch-Relay-Setup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/2/KillSwitch-Relay-Setup.jpg)

*The relay setup*

This is an example of a 'bootstrapped' relay system. Bootstrapping allows a small signal to control big loads. The 3.3V signal from the Pro Mini can't control the large 24V relay directly, so I used the 3.3V signal to control a 5V relay to activate the 24V relay.

When we want to allow power to the motor, the Pro Mini activates the [Beefcake Relay](https://www.sparkfun.com/products/11042) with a 3.3V signal (KILL_LOW goes from 0 to 3.3V). This signal grounds the Q1 transistor allowing current to flow across the coil in R1. Next, the reed on R1 moves from the normally closed position (where it is connected to nothing) to the normally open position. Current begins to flow freely from 24V through the R2 coil to ground. This flow causes the reed on R2 to move from the normally closed position to the upper position connecting the + lead of the motor to the +M on the motor controller. In real life, this whole process produces a most satisfying **thunk**. Note this does not power the motor; rather, it allows the motor controller to control the motor. If the motor controller is outputting 0% power, the motor will just sit happily still.

### 48V / 24V / 5V Subsystems

You may be wondering why I am running a 24V subsystem? For my A+PRS entry, I am controlling the steering with a 12V linear actuator that I am over-driving with 24V. The actuator is very strong but slow, and the extra voltage drives the actuator much faster. The 24V cut-off relay (R2) fit nicely into this design as well.

### Motor Braking

When R2 is in the normally closed (unactivated) position, the + and - of the motor are shorted together. This is called motor braking. To see what this feels like, find a large DC motor, and try spinning the axle. It should be relatively easy. Now, short + and - of the motor together; the axle will be considerably harder to turn. By setting R2 up this way we have another layer of safety in that, if everything goes wrong and the Kill Switch goes haywire, the system should fail safe, turn off all the relays, short the motor and brake to a stop. It is not yet clear to me how aggressive this braking power is. If the braking is too abrupt (as in it ejects the human rider) it could be more dangerous than it is helpful, in which case I will disconnect the **MOTOR-** from the lower pin of R2 and let the motor freewheel in the event of a safety shutdown. That way the human passenger has the ability to control braking with the brake rather than something they cannot control.

## RCU Parts List

[![Inside the kill switch](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/2/Kill_Switch_Images-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/2/Kill_Switch_Images-02.jpg)

*Inside the remote control unit*

Parts Used on the Remote:

- [Three Button Switch Station Box](http://www.amazon.com/Momentary-Green-Button-Switch-Station/dp/B00D0YRX1M)
- [Arduino Pro Mini 328 - 3.3V/8MHz](https://www.sparkfun.com/products/11114)
- [RFM69 Breakout](https://www.sparkfun.com/products/12823)
- [Red/Yellow/Green 5MM LEDs](https://www.sparkfun.com/products/12062)
- [850mAh LiPo Battery](https://www.sparkfun.com/products/341)
- [Lipo Charger Basic - Mini-USB](https://www.sparkfun.com/products/10401)
- [Small Latching Power Switch](https://www.sparkfun.com/products/11975) or [On/Off Slide Switch](https://www.sparkfun.com/products/102)
- [4-Pin](https://www.sparkfun.com/products/9916) and [3-Pin](https://www.sparkfun.com/products/9915) JST Jumper Wire Assembly
- [FTDI Basic Breakout - 3.3V](https://www.sparkfun.com/products/9873) for programming
- [Right Angle Headers](https://www.sparkfun.com/products/553) if you need them for your Pro Mini

## Remote Control Unit

[![The remote control kill switch](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/2/Kill_Switch_Images-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/2/Kill_Switch_Images-01.jpg)

*The remote control kill switch*

The RCU is the thing that the user holds in their hand and jams the red button in case the autonomous vehicle becomes sentient, or is just doing something it shouldn't.

[![Schematic for kill switch](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/2/KillSwitch-Remote-Control-Unit.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/2/KillSwitch-Remote-Control-Unit.jpg)

*Schematic for kill switch*

Let's start with the simple bits: The LEDs are simply on/off and don't need PWM pins. I chose to connect the LEDs to pins 3, 4, and 5 because it allowed me to solder in a [3-pin JST connector](https://www.sparkfun.com/products/9915). The three buttons within the switch station are the Normally Open (NO) type. I wired them to pins 6, 7 and 9 with 8 serving as the ground pin. I did this because I ran out of GND pins on the Pro Mini. You can use a GPIO as ground, you just set it as an output and LOW. Also, by creating a bank of four pins it allowed me to solder a 4-pin JST directly to the Pro Mini.

The RFM69 is wired according to Mike's excellent [hookup guide](https://learn.sparkfun.com/tutorials/rfm69hcw-hookup-guide). **Note:** The connection from pin 2 on the Pro Mini to DIO0 on the RFM69 is required and serves as the interrupt from RFM to Pro Mini. You cannot use a different pin on the Pro Mini because pin 2 is a hardware interrupt pin, and the library depends on interrupts.

The remote needs to have a battery! I used the [3.7V 850mA LiPo](https://www.sparkfun.com/products/341). The average current draw is about 42mA, so this should last for around 20 hours on a charge. I didn't do any power minimization efforts because 20 hours was plenty for my purposes. To avoid having to open and close the enclosure to charge the battery, I installed a [LiPo charger with miniB connector](https://www.sparkfun.com/products/10401). Plugging a miniB cable in will charge the battery any time, and pressing S4 (a latching switch) will turn on/off the remote. Note that if the remote is turned off, the vehicle will go into automatic safety shutdown (a good thing).

I really enjoy the quality and feel of the three buttons in the Switch Station, but they are very big and packing all the electronics into the enclosure is a challenge. If I were to build another remote, I would look for a better trade off of more room vs quality (there are many low quality switch stations on Amazon with more room inside the enclosure).

## Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

You can find the latest code for the RCU and VCU in this [github repo](https://github.com/sparkfun/Wireless_Kill_Switch).

    language:c
    /*
     Remote Kill Switch - On the Car
     By: Nathan Seidle
     SparkFun Electronics
     Date: March 23rd, 2016
     License: This code is public domain but you buy me a beer if you use this and we meet someday (Beerware license).

     This is the part of the remote kill switch that lives on the car.

     If we receive 'R' (kill) system turns off the relay.
     If we receive 'Y' (pause) from the remote then set pin PAUSE high to signal master
     computer to pause.
     If we receive 'G' (go) system turns on relay, sets PAUSE pin to low.
     If we don't receive a system status from the remote every MAX_TIME_WITHOUT_OK ms, system goes into safety shutdown (relay off).

     Locomotion controller requires a 5V FTDI. The kill switch requires a 3.3V FTDI.
    */

    #include <SPI.h>
    #include <RH_RF69.h> //From http://www.airspayce.com/mikem/arduino/RadioHead/
    #include <SimpleTimer.h> //https://github.com/jfturcot/SimpleTimer
    #include <avr/wdt.h> //We need watch dog for this program

    //If we don't get ok after this number of milliseconds then go into safety-shutdown
    //This must be longer than MAX_DELIVERY_FAILURES * CHECKIN_PERIOD
    //250ms is good
    //L defines the value as a long. Needed for millisecond times larger than int (+32,767) but doesn't hurt to have.
    #define MAX_TIME_WITHOUT_OK 250L

    unsigned long lastCheckin = 0;

    RH_RF69 rf69;

    #define RELAY_CONTROL 9
    #define PAUSE_PIN 6

    #define LED_RED 5
    #define LED_YLW 4
    #define LED_GRN 3

    //Define the various system states
    #define RED 'R'
    #define YELLOW 'Y'
    #define GREEN 'G'
    #define DISCONNECTED 'D'

    char systemState;

    void setup()
    ;
      rf69.setEncryptionKey(key);

      systemState = RED; //On power up start in red state
      setLED(LED_RED);

      Serial.println("Power Wheels Kill Switch Online");

      wdt_reset(); //Pet the dog
    //  wdt_enable(WDTO_1S); //Unleash the beast
    }

    void loop()
    
      }

      if (rf69.available())
      
          }
          else if (buf[0] == YELLOW)
          
          }
          else if (buf[0] == GREEN)
          
          }
          else if (buf[0] == DISCONNECTED)
          

          Serial.print("RSSI: ");
          Serial.println(rf69.lastRssi(), DEC);
        }
      }
    }

    //If we receive a system state we send a response
    void sendResponse()
    

    //Turns on a given LED
    void setLED(byte LEDnumber)
    

    //Turn on the relay
    void turnOnRelay()
    

    //Turn off the relay
    void turnOffRelay()
    

*Above is the code for the VCU*

    language:c
    /*
     Remote Kill Switch - Hand Held Controller
     By: Nathan Seidle
     SparkFun Electronics
     Date: March 23rd, 2016
     License: This code is public domain but you buy me a beer if you use this and we meet someday (Beerware license).

     This is the part of the remote kill switch that the user holds in their hand.

     If red button pressed we send 'R' (kill). Turn on red LED.
     If yellow button pressed we send 'Y' (pause). Turn on yellow LED.
     If green button pressed we send 'G' (go). Turn on green LED.
     Send the system state every CHECKIN_PERIOD ms. Car turns off if nothing is received after MAX_TIME_WITHOUT_OK ms.

     Indicator LEDs: Green/Yellow/Red

     Measured current: 42mA roughly

    */

    #include <SPI.h>
    #include <RH_RF69.h> //From: http://www.airspayce.com/mikem/arduino/RadioHead/s
    #include <SimpleTimer.h> //https://github.com/jfturcot/SimpleTimer
    #include <avr/wdt.h> //We need watch dog for this program

    RH_RF69 rf69;

    SimpleTimer timer;
    long secondTimerID;

    #define BUTTON_RED 9
    #define BUTTON_GND 8
    #define BUTTON_GRN 7
    #define BUTTON_YLW 6

    #define LED_RED 5
    #define LED_YLW 4
    #define LED_GRN 3

    //Define the various system states
    #define RED 'R'
    #define YELLOW 'Y'
    #define GREEN 'G'
    #define DISCONNECTED 'D'

    //Number of milliseconds between broadcasting our system state to the vehicle
    //L defines the value as a long. Needed for millisecond times larger than int (+32,767) but doesn't hurt to have.
    //25ms is good.
    #define CHECKIN_PERIOD 25L

    //Number of milliseconds to block for sending packets and waiting for the radio to receive repsonse packets
    //This should be not be longer than the CHECKIN_PERIOD
    //10ms is good. 
    #define BLOCKING_WAIT_TIME 10L

    //How many failed responses should be allowed from car until we go into disconnect mode
    #define MAX_DELIVERY_FAILURES 3
    byte failCount = 0;

    char systemState;

    unsigned long lastBlink = 0;
    #define BLINK_RATE 500 //Amount of milliseconds for LEDs to toggle when disconnected

    void setup()
    ;
      rf69.setEncryptionKey(key);

      systemState = RED; //On power up start in red state
      setLED(LED_RED);

      Serial.println("Remote Controller Online");

      wdt_reset(); //Pet the dog
    //  wdt_enable(WDTO_1S); //Unleash the beast
    }

    void loop()
    
      else if (digitalRead(BUTTON_YLW) == LOW)
      
      else if (digitalRead(BUTTON_GRN) == LOW)
      
    }

    //Powers down all LEDs, radio, etc and sleeps until button interrupt
    void shutDown()
    

    //Send the system status notification every CHECKIN_PERIOD number of ms
    void checkIn()
    
      else if (systemState == YELLOW)
      
      else if (systemState == GREEN)
      
      else if (systemState == DISCONNECTED)
      
      }
    }

    //Sends a packet
    //If we fail to send packet or fail to get a response, time out and go to DISCONNECTED system state
    void sendPacket(char* thingToSend)
    

      if(responseFromCar == true) //We got a response
      
        else if(systemState == DISCONNECTED)
        
      }
      else if (responseFromCar == false)
      
        }

        rf69.setModeIdle(); //This clears the buffer so that rf69.send() does not lock up
      }
    }

    //Turns on a given LED
    void setLED(byte LEDnumber)
    

*Above is the code for the RCU*

The RCU waits for the user to press a button and monitors the link to the VCU. If the link is not detected, the RCU flashes all three LEDs letting the user know the VCU is offline (either unpowered or out of range). Once the user presses the green button, the RCU turns the LED to green and begins transmitting the 'Ok, go for it' signal. Once received, the VCU sets the **KILL_LOW** pin to high, thus activating both relays and connecting the motor to the motor controller.

Certain settings can be changed in the code for your specific application:

- **MAX_DELIVERY_FAILURES:** It turns out that the RF link will drop a packet every once and a awhile, so the MAX_DELIVERY_FAILURES is set to three. If we don't get a valid send/response after 3 tries, the system goes into disconnected mode. Setting this lower than 3 means the car may shutdown prematurely because we had some RF traffic/collisions.
- **CHECKIN_PERIOD:** The remote will broadcast the system state every 25ms.
- **MAX_TIME_WITHOUT_OK:** The vehicle will shut down if it doesn't hear from the remote after 250ms.

These settings worked well for me and created a responsive, dependable link that shut the vehicle down within 250ms if things went pear-shaped. You may need to adjust these settings for other, longer-range applications.