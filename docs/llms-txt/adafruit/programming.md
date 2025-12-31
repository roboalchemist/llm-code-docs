# Source: https://learn.adafruit.com/babel-fish/programming.md

# Babel Fish

## Programming

Program your Arduino with the following sketch and open the serial monitor.  
  
Dont forget you'll need to have the Waveshield WaveHC library, and NFCshield library installed first. Visit the Wave and NFC shield product pages and test both of them before continuing onto this code!

```
#include &lt;WaveHC.h&gt;
#include &lt;WaveUtil.h&gt;
#include &lt;Wire.h&gt;
#include &lt;Adafruit_NFCShield_I2C.h&gt;


#define IRQ 6 // this trace must be cut and rewired!
#define RESET 8

Adafruit_NFCShield_I2C nfc(IRQ, RESET);

SdReader card; // This object holds the information for the card
FatVolume vol; // This holds the information for the partition on the card
FatReader root; // This holds the information for the volumes root directory
FatReader file; // This object represent the WAV file for a pi digit or period
WaveHC wave; // This is the only wave (audio) object, since we will only play one at a time
/*
* Define macro to put error messages in flash memory
*/
#define error(msg) error_P(PSTR(msg))

//////////////////////////////////// SETUP

void setup() {
  // set up Serial library at 9600 bps
  Serial.begin(9600);
  
  PgmPrintln("Pi speaker");
  
  if (!card.init()) {
    error("Card init. failed!");
  }
  if (!vol.init(card)) {
    error("No partition!");
  }
  if (!root.openRoot(vol)) {
    error("Couldn't open dir");
  }

  PgmPrintln("Files found:");
  root.ls();
  
  // find Adafruit RFID/NFC shield
  nfc.begin();

  uint32_t versiondata = nfc.getFirmwareVersion();
  if (! versiondata) {
    Serial.print("Didn't find PN53x board");
    while (1); // halt
  }
  // Got ok data, print it out!
  Serial.print("Found chip PN5"); Serial.println((versiondata&gt;&gt;24) &amp; 0xFF, HEX);
  Serial.print("Firmware ver. "); Serial.print((versiondata&gt;&gt;16) &amp; 0xFF, DEC);
  Serial.print('.'); Serial.println((versiondata&gt;&gt;8) &amp; 0xFF, DEC);
  
  // configure board to read RFID tags
  nfc.SAMConfig();

}

/////////////////////////////////// LOOP

unsigned digit = 0;

void loop() {
  uint8_t success;
  uint8_t uid[] = { 0, 0, 0, 0, 0, 0, 0 }; // Buffer to store the returned UID
  uint8_t uidLength; // Length of the UID (4 or 7 bytes depending on ISO14443A card type)

  // wait for RFID card to show up!
  Serial.println("Waiting for an ISO14443A Card ...");

    
  // Wait for an ISO14443A type cards (Mifare, etc.). When one is found
  // 'uid' will be populated with the UID, and uidLength will indicate
  // if the uid is 4 bytes (Mifare Classic) or 7 bytes (Mifare Ultralight)
  success = nfc.readPassiveTargetID(PN532_MIFARE_ISO14443A, uid, &amp;uidLength);

  uint32_t cardidentifier = 0;
  
  if (success) {
    // Found a card!

    Serial.print("Card detected #");
    // turn the four byte UID of a mifare classic into a single variable #
    cardidentifier = uid[3];
    cardidentifier &lt;&lt;= 8; cardidentifier |= uid[2];
    cardidentifier &lt;&lt;= 8; cardidentifier |= uid[1];
    cardidentifier &lt;&lt;= 8; cardidentifier |= uid[0];
    Serial.println(cardidentifier);

  // repeat this for loop as many times as you have RFID cards
    if (cardidentifier == 2588581390) { // this is the card's unique identifier
      playcomplete("1.WAV"); // these are file names for the sample audio files - change them to your own file names
    }
  
    if (cardidentifier == 2146122274) {
      playcomplete("2.WAV");
    }
  }
}

/////////////////////////////////// HELPERS

/*
* print error message and halt
*/
void error_P(const char *str) {
  PgmPrint("Error: ");
  SerialPrint_P(str);
  sdErrorCheck();
  while(1);
}
/*
* print error message and halt if SD I/O error
*/
void sdErrorCheck(void) {
  if (!card.errorCode()) return;
  PgmPrint("\r\nSD I/O error: ");
  Serial.print(card.errorCode(), HEX);
  PgmPrint(", ");
  Serial.println(card.errorData(), HEX);
  while(1);
}
/*
* Play a file and wait for it to complete
*/
void playcomplete(char *name) {
  playfile(name);
  while (wave.isplaying);
  
  // see if an error occurred while playing
  sdErrorCheck();
}
/*
* Open and start playing a WAV file
*/
void playfile(char *name) {
  if (wave.isplaying) {// already playing something, so stop it!
    wave.stop(); // stop it
  }
  if (!file.open(root, name)) {
    PgmPrint("Couldn't open file ");
    Serial.print(name);
    return;
  }
  if (!wave.create(file)) {
    PgmPrintln("Not a valid WAV");
    return;
  }
  // ok time to play!
  wave.play();
}
```

Replace the long number in the following for loop with your RFID card's ID. Replace the sound file name with the filename for your chosen sound samples.

```
    if (cardidentifier == 2146122274) {
      playcomplete("2.WAV");
    }
```

- [Previous Page](https://learn.adafruit.com/babel-fish/flash-cards.md)
- [Next Page](https://learn.adafruit.com/babel-fish/fish-box.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Adafruit PN532 NFC/RFID Controller Shield for Arduino + Extras

[Adafruit PN532 NFC/RFID Controller Shield for Arduino + Extras](https://www.adafruit.com/product/789)
We've taken our popular Adafruit PN532 breakout board and turned it into a shield - the perfect tool for any 13.56MHz RFID or NFC application. The Adafruit NFC shield uses the PN532 chip-set (the most popular NFC chip on the market) and is what is embedded in pretty much every phone or...

In Stock
[Buy Now](https://www.adafruit.com/product/789)
[Related Guides to the Product](https://learn.adafruit.com/products/789/guides)
### Adafruit Wave Shield for Arduino Kit

[Adafruit Wave Shield for Arduino Kit](https://www.adafruit.com/product/94)
Adding quality audio to an electronic project is surprisingly difficult. Here is a shield for Arduino 328's that solves this problem. It can play up to 22KHz 12bit uncompressed audio files of any length. It's low cost, available as an easy-to-make kit. It has an onboard DAC, filter and...

Out of Stock
[Buy Now](https://www.adafruit.com/product/94)
[Related Guides to the Product](https://learn.adafruit.com/products/94/guides)
### Music & sound add-on pack for Arduino

[Music & sound add-on pack for Arduino](https://www.adafruit.com/product/175)
Its a Wave shield party pack! Just add an Arduino to create your own iPod-killer, audio art, sound-effects box...

Comes with:

- Latest [Wave shield kit](http://www.adafruit.com/products/94), works with more SD cards and with older NG Arduinos! Unassembled
- 8 GB...

Out of Stock
[Buy Now](https://www.adafruit.com/product/175)
[Related Guides to the Product](https://learn.adafruit.com/products/175/guides)
### 9 VDC 1000mA regulated switching power adapter - UL listed

[9 VDC 1000mA regulated switching power adapter - UL listed](https://www.adafruit.com/product/63)
This is a really nice power supply. It's a switching DC supply so it's small and light and efficient. It is thin so it fits in power strips without blocking other outlets. The output is regulated so you'll get a steady 9V up to 1000mA (1 Amp) of current draw. 5.5mm/2.1mm barrel...

Out of Stock
[Buy Now](https://www.adafruit.com/product/63)
[Related Guides to the Product](https://learn.adafruit.com/products/63/guides)
### 13.56MHz RFID/NFC Card - Classic 1K

[13.56MHz RFID/NFC Card - Classic 1K](https://www.adafruit.com/product/359)
This is a blank 13.56MHz RFID/NFC card - often used for train/bus passes but also found in other systems where a proximity card is desired. The tag contains a small RFID chip and an antenna, and is passively powered by the reader/writer when placed a couple inches away.  
  
These can be...

In Stock
[Buy Now](https://www.adafruit.com/product/359)
[Related Guides to the Product](https://learn.adafruit.com/products/359/guides)

## Related Guides

- [Circuit Playground: D is for Diode](https://learn.adafruit.com/circuit-playground-d-is-for-diode.md)
- [Wave Shield](https://learn.adafruit.com/adafruit-wave-shield-audio-shield-for-arduino.md)
- [Adafruit Ultimate GPS Logger Shield](https://learn.adafruit.com/adafruit-ultimate-gps-logger-shield.md)
- [36mm LED Pixels](https://learn.adafruit.com/36mm-led-pixels.md)
- [Arduino "Hunt The Wumpus"](https://learn.adafruit.com/arduino-hunt-the-wumpus.md)
- [1,500 NeoPixel LED Curtain with Raspberry Pi and Fadecandy](https://learn.adafruit.com/1500-neopixel-led-curtain-with-raspberry-pi-fadecandy.md)
- [Arduino Lesson 2. LEDs](https://learn.adafruit.com/adafruit-arduino-lesson-2-leds.md)
- [Electronic Demon Costume](https://learn.adafruit.com/electronic-demon-costume.md)
- [Arduino GPS Clock](https://learn.adafruit.com/arduino-clock.md)
- [LED Lightbox](https://learn.adafruit.com/led-lightbox.md)
- [Smart Measuring Cup](https://learn.adafruit.com/smart-measuring-cup.md)
- [WiFi Weather Station](https://learn.adafruit.com/wifi-weather-station-arduino-cc3000.md)
- [Arduino Lesson 14. Servo Motors](https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors.md)
- [NeoPixel Painter](https://learn.adafruit.com/neopixel-painter.md)
- [WiFi Candy Bowl Monitor](https://learn.adafruit.com/wifi-candy-bowl.md)
