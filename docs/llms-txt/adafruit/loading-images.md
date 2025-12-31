# Source: https://learn.adafruit.com/adafruit-gfx-graphics-library/loading-images.md

# Adafruit GFX Graphics Library

## Loading Images

![](https://cdn-learn.adafruit.com/assets/assets/000/067/997/medium800/graphic_lcds_loaded-bmp.jpg?1545441110)

Loading .BMP images from an **SD card** &nbsp;(or the **flash memory chip** on Adafruit “Express” boards) is an option for most of our color displays…though it’s not built into Adafruit\_GFX and must be **separately installed**.

The **Adafruit\_ImageReader** library handles this task. It can be installed through the Arduino Library Manager&nbsp;(Sketch→Include Library→Manage Libraries…). Enter “imageread” in the search field and the library is easy to spot:

![](https://cdn-learn.adafruit.com/assets/assets/000/067/995/medium800/graphic_lcds_install-imagereader-lib.png?1545427440 That’s “imageread,” not “ermahgerd.”)

While you’re there, also look for the **Adafruit\_SPIFlash** library and install it similarly.

There’s one more library required, but it can’t be installed through the Library Manager. The **Adafruit fork** of the **SdFat** library needs to be downloaded as a .ZIP file, uncompressed and [installed the old-school Arduino library way](https://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use/how-to-install-a-library).

[Download SdFat (Adafruit fork) Arduino library](https://github.com/adafruit/SdFat/archive/master.zip)
# Using the Adafruit\_ImageReader Library
The syntax for using this library (and the separate installation above) are admittedly a bit **peculiar** …it’s a side-effect of the way Arduino handles libraries. We _purposefully_ did not roll this into Adafruit\_GFX because any mere _mention_ of an SD card library will incur _all_ of that library’s considerable memory requirements…_even if one’s sketch doesn’t use an SD card at all!&nbsp;_A majority of graphics projects are self-contained and don’t reference files from a card…not everybody needs this functionality.

There are several **example sketches** in the Adafruit\_ImageReader/examples folder. It’s recommended that you dissect these for ideas how to use the library in your own projects.

They all start with several #includes…

```
#include &lt;Adafruit_GFX.h&gt;         // Core graphics library
#include &lt;Adafruit_ILI9341.h&gt;     // Hardware-specific library
#include &lt;SdFat.h&gt;                // SD card &amp; FAT filesystem library
#include &lt;Adafruit_SPIFlash.h&gt;    // SPI / QSPI flash library
#include &lt;Adafruit_ImageReader.h&gt; // Image-reading functions
```

One of these lines may vary from one example to the next, depending which display hardware it’s written to support. Above we see it being used with the Adafruit\_ILI9341 display library required of certain shields, FeatherWings or breakout boards. Others examples reference Adafruit\_HX8357, Adafruit\_ST7735, or other color TFT or OLED display libraries…use the right one for the hardware you have.

Most of the examples can work from either an **SD card** , or the small **flash storage drive** that’s on certain Adafruit “Express” boards. The code to initialize one or the other is a little different, and the examples check whether&nbsp; **USE\_SD\_CARD** is #defined to select one method vs. the other. If you _know for a fact_ that your own project only needs to run on one type or the other, you really only need the corresponding initialization.

For SD card use, these two globals are declared:

```
  SdFat                SD;         // SD card filesystem
  Adafruit_ImageReader reader(SD); // Image-reader object, pass in SD filesys
```

For a flash filesystem, there are some special declarations made that help us locate the flash device on different Express boards, then declare three globals:

```
  // SPI or QSPI flash filesystem (i.e. CIRCUITPY drive)
  #if defined(__SAMD51__) || defined(NRF52840_XXAA)
    Adafruit_FlashTransport_QSPI flashTransport(PIN_QSPI_SCK, PIN_QSPI_CS,
      PIN_QSPI_IO0, PIN_QSPI_IO1, PIN_QSPI_IO2, PIN_QSPI_IO3);
  #else
    #if (SPI_INTERFACES_COUNT == 1)
      Adafruit_FlashTransport_SPI flashTransport(SS, &amp;SPI);
    #else
      Adafruit_FlashTransport_SPI flashTransport(SS1, &amp;SPI1);
    #endif
  #endif
  Adafruit_SPIFlash    flash(&amp;flashTransport);
  FatFileSystem        filesys;
  Adafruit_ImageReader reader(filesys); // Image-reader, pass in flash filesys
```

The “reader” object&nbsp;will be used to access the image-loading functions later.

Then…we declare a display object (called “tft” in most of the examples) the usual way…for example, with the 2.8 inch TFT touch shield for Arduino, it’s:

```
#define SD_CS   4 // SD card select pin
#define TFT_CS 10 // TFT select pin
#define TFT_DC  9 // TFT display/command pin

Adafruit_ILI9341 tft = Adafruit_ILI9341(TFT_CS, TFT_DC);
```

That all takes place in the global variable section, even before the setup() function.

Now we need to do some work in setup(), and again it’s different for SD cards vs. flash filesystems…

For SD card use, it might look like this:

```
  if(!SD.begin(SD_CS, SD_SCK_MHZ(25))) { // ESP32 requires 25 MHz limit
    Serial.println(F("SD begin() failed"));
    for(;;); // Fatal error, do not continue
  }
```

Warning: Some boards such as the Feather M0 prefer a slower clock speed. Reduce the 25 MHz to 12 MHz if you are see seeing a "SD begin() failed." message on a FeatherWing.

This example is providing some very basic error handling…checking the return status of SD.begin() and printing a message to the Serial Monitor if there’s a problem.

Using a flash filesystem instead requires two steps:

```
  if(!flash.begin()) {
    Serial.println(F("flash begin() failed"));
    for(;;);
  }
  if(!filesys.begin(&amp;flash)) {
    Serial.println(F("filesys begin() failed"));
    for(;;);
  }
```

 **All other code is now the same regardless whether using an SD card or flash.** That either/or setup required some extra steps but it’s all smooth sailing now…

After the SD (or flash) and TFT’s `begin()` functions have been called, you can then call `reader.drawBMP()` to load a BMP image from the card to the screen:

```
ImageReturnCode stat;
stat = reader.drawBMP("/purple.bmp", tft, 0, 0);
```

This accepts **four** arguments:

- A filename in “8.3” format (you shouldn’t _need_ to provide an absolute path (the leading “/”), but there are some issues with the SD library on some cutting-edge boards like the ESP32, so go ahead and include this for good measure).
- The display object where the image will be drawn (e.g. “tft”). _This is the weird syntax previously mentioned…rather than tft.drawBMP(), it’s reader.drawBMP(tft), because reasons._
- An X and Y coordinate where the top-left corner of the image is positioned (this doesn’t need to be within screen bounds…the library will clip the image as it’s loaded). 0, 0 will draw the image at the top-left corner…so if the image dimensions match the screen dimensions, it will fill the entire screen.

This function returns a value of type `ImageReturnCode`, which you can either ignore or use it to provide some diagnostic functionality. Possible values are:

- `IMAGE_SUCCESS`&nbsp;— Image loaded successfully (or was clipped fully off screen, still considered “successful” in that there was no error).
- `IMAGE_ERR_FILE_NOT_FOUND`&nbsp;— Could not open the requested file (check spelling, confirm file actually exists on the card, make sure it conforms to “8.3” file naming convention (e.g. “filename.bmp”).
- `IMAGE_ERR_FORMAT`&nbsp;— Not a supported image format. Currently only **uncompressed 24-bit color BMPs** are supported (more will likely be added over time).
- `IMAGE_ERR_MALLOC`&nbsp;— Could not allocate memory for operation (drawBMP() won’t generate this error, but other ImageReader functions might).

Rather than dealing with these values yourself, you can optionally call a function to display a basic diagnostic message to the Serial console:

```
reader.printStatus(stat);
```

If you need to know the **size** of a BMP image _without actually loading it,_ there’s the `bmpDimensions()` function:

```
int32_t width, height;
stat = reader.bmpDimensions("/parrot.bmp", &amp;width, &amp;height);
```

This accepts **three** arguments:

- A filename, same rules as the `drawBMP()` function.
- **Pointers** to two **32-bit integers**. On successful completion, their contents will be set to the image width and height in pixels. On any error these values should be ignored (they’re left uninitialized).

This function returns an&nbsp;`ImageReturnCode` as explained with the `drawBMP()` function above.

# Loading and Using Images in RAM

Depending on image size and other factors, loading an image from SD card to screen may take several seconds. Small images…those that can fit entirely in RAM…can be loaded once and used repeatedly. This can be handy for frequently-used icons or sprites, as it’s usually much easier than converting and embedding an image as an array directly in one’s code…a horrible process.

This introduces another ImageReader function plus a new object type, `Adafruit_Image`:

```
Adafruit_Image img;
stat = reader.loadBMP("/wales.bmp", img);
```

`loadBMP()` accepts **two** arguments:

- A filename, same rules as the previous functions.
- An `Adafruit_Image` object. This is a slightly more flexible type than the bitmaps used by a few drawing functions in the GFX library.

This returns an&nbsp;`ImageReturnCode` as previously described. If an image is too large to fit in available RAM, a value of&nbsp;`IMAGE_ERR_MALLOC` will be returned. Color images require two bytes per pixel…for example, a 100x25 pixel image would need 100\*25\*2 = 5,000 bytes RAM.

On success, the `img` object will contain the image in RAM.

The `loadBMP()` function is useful only on microcontrollers with considerable RAM, like the Adafruit “M0” and “M4” boards, or ESP32. Small devices like the Arduino Uno just can’t cut it. It might be _marginally_ useful on the Arduino Mega with very small images.

After loading, use the `img.draw()` function to display an image on the screen:

```
img.draw(tft, x, y);
```

This accepts **three** arguments:

- A display object (e.g. “tft” in most of the examples), similar to how `drawBMP()` worked.
- An X and Y coordinate for the upper-left corner of the image on the screen, again similar to `drawBMP()`.

We use `img.draw(tft,…)` rather than `tft.drawRGBBitmap(…)` (or other bitmap-drawing functions in the Adafruit\_GFX library) because in the future we plan to add more flexibility with regard to image file formats and types. The `Adafruit_Image` object “understands” a bit about the image that’s been loaded and will call the appropriate bitmap-rendering function automatically, you won’t have to handle each separate case on your own.

If the image failed to load for any reason, `img.draw()` can still be called, it just won’t _do_ anything. But at least the sketch won’t crash.

 **There is no BMP-to-flash function.** &nbsp;This is on purpose and by design.&nbsp;We do something similar to that in the&nbsp;[M4\_Eyes](https://learn.adafruit.com/adafruit-monster-m4sk-eyes/compiling-from-source-code) project&nbsp;and you’re welcome to look through that code for insights,&nbsp;but generally speaking this is fraught with peril and not something we recommend.&nbsp;SD to screen or to RAM should cover most cases.

- [Previous Page](https://learn.adafruit.com/adafruit-gfx-graphics-library/using-fonts.md)
- [Next Page](https://learn.adafruit.com/adafruit-gfx-graphics-library/minimizing-redraw-flicker.md)

## Related Guides

- [Arduino Lesson 11. LCD Displays - Part 1](https://learn.adafruit.com/adafruit-arduino-lesson-11-lcd-displays-1.md)
- [2.8" TFT Touchscreen](https://learn.adafruit.com/2-8-tft-touchscreen.md)
- [Adafruit 1.28" 240x240 Round TFT LCD](https://learn.adafruit.com/adafruit-1-28-240x240-round-tft-lcd.md)
- [Adafruit MacroPad RP2040](https://learn.adafruit.com/adafruit-macropad-rp2040.md)
- [USB + Serial RGB Backlight Character LCD Backpack](https://learn.adafruit.com/usb-plus-serial-backpack.md)
- [I2C/SPI LCD Backpack](https://learn.adafruit.com/i2c-spi-lcd-backpack.md)
- [Adafruit Grayscale 1.5" 128x128 OLED Display](https://learn.adafruit.com/adafruit-grayscale-1-5-128x128-oled-display.md)
- [Generating Text with ChatGPT, Pico W & CircuitPython](https://learn.adafruit.com/generating-text-with-chatgpt-pico-w-circuitpython.md)
- [HalloWing Flapping Bat](https://learn.adafruit.com/hallowing-flapping-bat.md)
- [CircuitPython OLED and Dual Knob Sketcher](https://learn.adafruit.com/circuitpython-oled-knob-sketcher.md)
- [Adafruit IO IOT Hub with the Adafruit FunHouse](https://learn.adafruit.com/adafruit-io-hub-with-the-adafruit-funhouse.md)
- [Adafruit 16x2 Character LCD + Keypad for Raspberry Pi](https://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi.md)
- [CircuitPython Hardware: SSD1306 OLED Display](https://learn.adafruit.com/micropython-hardware-ssd1306-oled-display.md)
- [Adafruit 128x64 OLED FeatherWing ](https://learn.adafruit.com/adafruit-128x64-oled-featherwing.md)
- [Sous-vide controller powered by Arduino - The SousViduino!](https://learn.adafruit.com/sous-vide-powered-by-arduino-the-sous-viduino.md)
