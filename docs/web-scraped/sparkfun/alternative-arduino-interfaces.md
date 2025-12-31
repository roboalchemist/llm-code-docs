# Source: https://learn.sparkfun.com/tutorials/alternative-arduino-interfaces

## Overviewing the Options

[Arduino](https://learn.sparkfun.com/tutorials/what-is-an-arduino) is awesome! It\'s our go-to electronics education platform, and it\'s our top choice for rapid prototyping, but it isn\'t for everyone. Maybe it\'s the cryptic language, or the Java-based IDE, or maybe it\'s just the teal window border \-- regardless of your reasoning, if you\'re trying to escape the Arduino IDE, here are a few alternatives we\'d like to share.

The Arduino alternatives covered in this tutorial range from simple, introductory graphical programming to web-based Arduino interfaces for your web browser. Here\'s a quick overview of each interface covered, we\'ll go into further detail later on:

#### ArduBlock \-- A Visual Programming Arduino Extension

[ArduBlock](http://ardublock.com/) is a **graphical programming** add-on to the default Arduino IDE. Instead of memorizing cryptic functions, forgetting semicolons, and debugging code, ArduBlock allows you to build your Arduino program by dragging and dropping interlocking blocks.

[![ArduBlock example](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/1/ardublock_01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/ardublock_01.png)

ArduBlock is a perfect interface if you\'re just getting into programming, electronics, or Arduino. Check out the [ArduBlock section of this tutorial](https://learn.sparkfun.com/tutorials/alternative-arduino-interfaces/ardublock) for an introduction and quick getting started guide.

#### Minibloq \-- Visual Programming Standalone Software

In the same vein as ArduBlock, [Minibloq](http://minibloq.org) is a **graphical programming environment** where groups of blocks are stacked on top of each other to create your program. Unlike ArduBlock, however, Minibloq is a stand-alone program \-- no Arduino install required.

[![Minibloq example](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/1/minibloq_01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/minibloq_01.png)

One of Minibloq\'s most powerful features is its real-time code generation \-- as you drag blocks into your program, the equivalent code is generated concurrently. This makes Minibloq an excellent tool for beginners to intermediate programmers.

Check out the [Minibloq section of this tutorial](https://learn.sparkfun.com/tutorials/alternative-arduino-interfaces/minibloq) for an introduction to the interface.

### \...and Beyond

Those are the alternatives we\'ll be discussing in this tutorial, but there are many others worth checking out, including:

- [Scratch for Arduino](http://s4a.cat/) \-- More **visual programming**! Scratch for Arduino (S4A) is a riff on the popular [Scratch](http://scratch.mit.edu/) programming environment. If you\'re an experienced Scratch user, this is most definitely worth checking out!
- [Modkit](http://www.modk.it/) \-- After a successful Kickstarter campaign, Modkit is well on it\'s way to producing another great **visual** alternative to Arduino. Check out their website and get a feel for their **browser-based** visual environment.
- [Arduino IDE for Atmel Studio](http://www.visualmicro.com/page/User-Guide.aspx) \-- [Atmel Studio](http://www.atmel.com/tools/atmelstudio.aspx) is an incredibly powerful tool for programming and debugging AVR chips like those on the Arduino. If you\'re looking for a more **advanced** approach to Arduino, or Atmel chips in general, check out this extension to Atmel Studio.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/1/atmel_studio_example.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/atmel_studio_example.png)

This extension can be an extremely powerful tool \-- complete with breakpoint implementation and a host of features you may be used to from more advanced IDE\'s.

## ArduBlock

[ArduBlock](http://ardublock.com) is a programming environment designed to make "physical computing with Arduino as easy as drag-and-drop." Instead of writing code, worrying about syntax, and (mis)placing semicolons, ArduBlock allows you to **visually program** with an snapped-together list of code blocks.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/1/ardublock_01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/ardublock_01.png)

ArduBlock builds on the simplicity of Arduino, and creates a perfect beginner gateway to physical computing. Instead of tearing your hair out debugging, you can spend your time creating!

### Installing ArduBlock

ArduBlock is something of an \"add-on\" to Arduino, so it requires that you have the Arduino IDE installed. The benefit of that, though, is \-- because Arduino is multi-platform \-- ArduBlock **works on Windows, Mac, or Linux**. Plus, having Arduino already present makes the transition from visual programming to text programming easier, when the inevitability approaches.

Installing ArduBlock can be a little tricky \-- there\'s no installer, just a Java file that needs to be stored in a very specific location. Follow the steps below to install it:

1.  **Download and Install Arduino** (if you haven\'t already) \-- Ardublock is an extension of the default Arduino IDE, so you\'ll need to have Arduino installed on your computer to run it. Check out our [Installing Arduino IDE tutorial](https://learn.sparkfun.com/tutorials/installing-arduino-ide) for help with that.
2.  **[Download ArduBlock](http://sourceforge.net/projects/ardublock/files/latest/download)** \-- Click the link to the left, or head over to the [ArduBlock Sourceforge page](http://sourceforge.net/projects/ardublock/) to find the latest and greatest version.
3.  **Identify your Arduino Sketchbook location** \-- This is a folder on your computer where your sketches and libraries are saved by default. To find your sketchbook location, run Arduino, and **open Preferences** by going to File \> Preferences. The contents of the top text box defines your sketchbook location. Memorize that location and close Arduino.\
    [![](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/ardublock-sketchbook-location_01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/ardublock-sketchbook-location_01.png)
    \
4.  **Create \[sketchbook\]/tools/ArduBlockTool/tool/** \-- The Ardublock file you downloaded earlier needs to live in a very specific location within your Arduino sketchbook. Navigate to your sketchbook, then create a nest of three directories: *tools* \> *ArduBlockTool* \> *tool* (watch out, each folder is **case sensitive**).
5.  **Paste \"ardublock-xxxxxxxx.jar\" Into /tool/** \-- Paste the Ardublock file you downloaded \-- a JAR (Java ARchive) file \-- into the last folder in the nest you created.\
    \
    [![](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/ardublock_file-location.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/ardublock_file-location.png)
    \
6.  **Start Arduino** \-- Or restart it if it was open.
7.  **Select the Board and Serial Port** \-- Just as you would if you were using Arduino, make your board and serial port selections from the \"Tools\" menu.
8.  **Open ArduBlock** \-- Run ArduBlock by clicking **Tools** \> **ArduBlock**. If you don\'t see an entry for ArduBlock here, double-check to make sure your directories are all correctly typed and cased.\
    \
    [![](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/ardublock_open.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/ardublock_open.png)
    \

ArduBlock works hand-in-hand with the Arduino IDE \-- it relies on the IDE being open in the background, so **don\'t close the Arduino window**!

### Using ArduBlock

The ArduBlock window is split into two halves. On the left there are \"bins\", which store every possible block you can add to your sketch. The blank, gray slate to the right of that is where you \"draw\" your sketch. To add a block to your sketch, simply drag it from the bin into the blank, gray area.

To begin, every ArduBlock sketch requires a **Program block**, which you can find in the \"Control\" bin. The Program block defines the `setup` and `loop` functions that every Arduino program requires.

[![Ardublock program location](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/ardublock_program.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/ardublock_program.png)

From there, you can drag more Blocks over, snapping them into either the `loop` or `setup` sections. Here, try making a **blink program**. The **set digital pin** blocks, which effect a digital output (analogous to Arduino\'s `digitalWrite` function), are found under the \"Pins\" bin. The **delay milliseconds** block, found under \"Control\", is analogous to a `delay` Arduino function.

[![Ardublock blink program](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/ardublock_blink.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/ardublock_blink.png)

Then click **Upload to Arduino** to send your drawing off to your Arduino board. You can ALT+TAB back over to the Arduino window to check your code upload status.

[![Upload program](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/upload-location.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/upload-location.png)

After you\'ve successfully uploaded your first sketch, continue to play around and explore the contents of the other bins!

### ArduBlock Tips & Tricks

You can **clone** blocks, or groups of blocks, by right clicking and selecting \"Clone\". Everything from the block you right-clicked to the bottom of that \"group\" will be copied and pasted into the top-left corner of the window. This is a *huge* timesaver for bigger drawings.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/ardublock_clone.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/ardublock_clone.png)

You can **temporarily remove code** from your sketch by dragging it out of the entirety of the \"Program\" block. Anything not connected to the main Program block will be ignored when your code is compiled. This is a great debugging tool \-- you can remove a block of code from program execution, while not actually deleting it, much like commenting out code.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/ardublock_remove-block.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/ardublock_remove-block.png)

Finally, if you peek back over at the Arduino window, after you\'ve uploaded an ArduBlock drawing, you may notice something different. To create your code, the ArduBlock program simply parses your blocks and spits the equivalent Arduino code over into the Arduino window.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/1/ardublock_combo.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/1/ardublock_combo.png)

This becomes a great learning tool if you\'re interested in transitioning from graphical programming to text.

### ArduBlock Resources

- [ArduBlock Homepage](http://ardublock.com)
- [ArduBlock GitHub Repository](https://github.com/taweili/ardublock) (Open Source!)
- [SparkFun Digital SandBox Experiment Guide](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide) \-- A series of Arduino experiments all based around ArduBlock.

[![SparkFun Digital Sandbox](https://cdn.sparkfun.com/r/600-600/assets/parts/9/3/5/0/12651-03.jpg)](https://www.sparkfun.com/products/12651)

### [SparkFun Digital Sandbox](https://www.sparkfun.com/products/12651) 

[ DEV-12651 ]

The Digital Sandbox (DS) is a learning platform that engages both the software and hardware worlds. It's powered by a micro...

**Retired**