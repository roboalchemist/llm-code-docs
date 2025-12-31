# Source: https://learn.sparkfun.com/tutorials/lilypad-buzzer-hookup-guide

## Introduction

The [LilyPad Buzzer](https://www.sparkfun.com/products/8463) lets you create different noises using code when attached to a LilyPad Arduino. Send the buzzer a series of tones, and you can make musical melodies, special effect sounds, alarms, and more. This buzzer isn\'t very loud, but will be audible in close range to your projects. In this tutorial, we\'ll demonstrate how to hook up to a LilyPad Arduino and how to use the `tone()` function in Arduino to make sounds.

The LilyPad Buzzer is different than a speaker that plays audio, if you are looking to make a project that loads and plays music, we recommend the [LilyPad MP3](https://www.sparkfun.com/products/11013).

[![LilyPad Buzzer](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/5/9/08463-01.jpg)](https://www.sparkfun.com/lilypad-buzzer.html)

### [LilyPad Buzzer](https://www.sparkfun.com/lilypad-buzzer.html) 

[ DEV-08463 ]

This is a small buzzer for the LilyPad system. Use 2 I/O pins on the LilyPad main board and create different noises based on ...

[ [\$5.25] ]

[] This particular LilyPad component cannot be washed. We recommend sewing to a piece of fabric using [metal snaps](https://www.sparkfun.com/products/11347) so that it can be removed for washing. See the [Sewing Into a Project](https://learn.sparkfun.com/tutorials/using-the-lilypad-buzzer#sewing-into-a-project) section for more details.

To follow along with the code examples, we recommend:

### Suggested Reading

To add this component to a project, you should be comfortable sewing with conductive thread and uploading code to your LilyPad Arduino. Here are some tutorials to review before working with the buzzer:

- [E-Textiles Basics](https://learn.sparkfun.com/tutorials/e-textile-basics)
- [Insulation Techniques for E-Textiles](https://learn.sparkfun.com/tutorials/insulation-techniques-for-e-textiles)
- [Short Circuits](https://learn.sparkfun.com/tutorials/what-is-a-circuit/short-and-open-circuits)
- [Analog vs Digital](https://learn.sparkfun.com/tutorials/analog-vs-digital)

## Attaching to a LilyPad Arduino

The LilyPad Buzzer has two sew tabs: **Power (+)** and **Ground (-)**. Connect **+** to any digital I/O pin on a LilyPad Arduino and **-** to the **-** pin on the Arduino. To follow along with the code examples in this tutorial, connect the buzzer to a LilyPad Arduino as shown below. [Alligator clips](https://www.sparkfun.com/products/12978) are useful for making temporary connections while prototyping until you are ready to sew the board into a project. When you are finished prototyping, replace the alligator clips with conductive thread traces.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/9/LilyPadBuzzer_SimpleHookup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/9/LilyPadBuzzer_SimpleHookup.jpg)

*If using the [LilyPad Arduino Simple](https://www.sparkfun.com/products/10274), [LilyPad Arduino SimpleSnap](https://www.sparkfun.com/products/10941), or [LilyPad Main Board](https://www.sparkfun.com/products/9266), connect to **Pin 5**.\
If using the [LilyPad Arduino USB](https://www.sparkfun.com/products/12049), connect to **Pin 2***.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/9/ProtoPlus_Buzzer.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/9/ProtoPlus_Buzzer.png)

*If following along with a [LilyPad ProtoSnap Plus](https://www.sparkfun.com/products/14346) the buzzer is pre-wired to **Pin A3**.*

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/9/LilyPadBuzzer_DevSimple.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/9/LilyPadBuzzer_DevSimple.jpg)

*If following along with a [LilyPad Development Simple](https://www.sparkfun.com/products/11201) the buzzer is pre-wired to **Pin 9**.*

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/9/LilyPadBuzzer_Dev.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/9/LilyPadBuzzer_Dev.jpg)

*If following along with a [LilyPad Development Board](https://www.sparkfun.com/products/11262) the buzzer is pre-wired to **Pin 7**.*

## Making Sounds 

Inside the buzzer is a coil of wire and a small magnet. When current flows through this coil, it becomes magnetized and pulls towards the magnet, which makes a tiny \"click\". When done thousands of times per second, the clicks create tones. We can use commands in Arduino to click the buzzer at specific frequencies, which we hear as different pitches. To create a musical note, we\'ll need two things: a pitch and a duration.

A tone's pitch is what we perceive when we think of a note as being very high (screams, forks scratching plates, etc.) versus very low (like earth-rumbling bass). The pitch of a tone is very closely related to the frequency played through a speaker. If we toggle a pin from HIGH-to-LOW then LOW-to-HIGH 440 times per second, for example, it produces a 440 Hz (hertz) frequency - a "middle A" pitch. Humans can hear frequencies ranging from 20 (low-pitch, bass) to 20,000 Hz (high-pitch, "ow, my ears").\
\
We can also program the duration of a tone - the length of time a pitch is played. In our program, we'll use the delay function to set the duration. Playing a tone with Arduino is very easy. Just give it a pitch, and it will start toggling the output pin for you. Much like analog output, you can set it and forget it; the tone won't stop playing until you tell it to.\
\
- excerpt from [The Digital Sandbox Arduino Companion](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/14-opto-theremin-addon)

### Playing Notes

Upload the following code to your LilyPad Arduino, making sure to select the correct LilyPad board from the drop down menu below. The LilyPad Arduino Simple, LilyPad Arduino, and LilyPad Development Board, and Development Board Simple all use a **LilyPad ATmega 328**. Choose **LilyPad Arduino USB** if using a LilyPad Arduino USB.\
\
Don\'t forget to select the Serial Port that your LilyPad is connected to.\
\
If prototyping with a LilyPad Development Board Simple, change **buzzerPin** to 9.\
If prototyping with a LilyPad Development Board, change **buzzerPin** to 7.

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

    language:c
    /******************************************************************************

    LilyPad Buzzer Example
    SparkFun Electronics

    This example code shows how to hook up a LilyPad Buzzer to play a simple song 
    using the tone() function and setting variables for each note.

    Buzzer connections:
       * + pin to 5
       * - to -

    ******************************************************************************/
    // Which pin the buzzer is attached to
    int buzzerPin = 5;

    // Delay in milliseconds
    int delayTime = 500; 

    // Notes and their frequencies
    const int C = 1046;
    const int D = 1175;
    const int E = 1319;
    const int F = 1397;
    const int G = 1568;
    const int A = 1760;
    const int B = 1976;
    const int C1 = 2093;
    const int D1 = 2349;

    void setup()
    

    void loop()
    

Upload this code to your LilyPad Arduino and listen - the code plays a scale. To make the notes, we give the [tone function](https://www.arduino.cc/en/Reference/Tone) two pieces of information - the pin the buzzer is attached to and the frequency we want to play -`tone(pin, frequency)`. To make a note last a certain amount of time, we use a `delay()` in between notes. At the top of the sketch we created variables for musical notes with the frequency in hertz. To make a pause or rest, we can use the `noTone()` function followed by a delay.

Try using the `tone()` and `noTone()` functions to compose a simple song. One drawback of this code is that the sounds never stop. Next we\'ll learn how to trigger sounds with an input so they are not constantly playing.

**TIP:**\
When prototyping with the buzzer, sounds can get quite annoying, especially in large groups. Rather than unplugging or powering down your LilyPad Arduino to stop the sounds, we recommend unclipping an alligator clip from one side of the buzzer to quickly quiet it. For projects sewn together with conductive thread, stitch a [LilyPad Slide Switch](https://www.sparkfun.com/products/9350) between the LilyPad Arduino pin and the positive side of the buzzer as a way to quickly toggle the sound ON/OFF while letting the rest of the code run.

## Triggering Sounds

For this example, we\'ll make the song play only after a trigger is pressed. We can use alligator clips to make a quick and easy switch, or hook up a [LilyPad Button](https://www.sparkfun.com/products/8776) or [home-made button](https://learn.sparkfun.com/tutorials/ldk-experiment-4-make-your-own-button) to the LilyPad Arduino. For LilyPad Development Board users, a button is pre-wired to **pin A5**.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/9/LilyBuzzer_Switch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/9/LilyBuzzer_Switch.jpg)

Here we\'ll use an `if()` statement to check if the button is pressed. If yes, we\'ll call a function we created to play a song, and if not `noTone()` will keep the buzzer from making noise. To keep the code easier to read/more organized, we\'ve created a function to hold the song we\'re composing called `playSong()`. We\'ve also added an additional variable called **buttonState** to store the readings from the button pin.

    language:c
    /******************************************************************************

    LilyPad Buzzer Example
    SparkFun Electronics

    This example code shows how use a button (or alligator clips) to trigger sounds
    with the LilyPad Buzzer.

    Buzzer connections:
       * + pin to 5
       * - to -

    Button connections:
       * + pin to A3
       * - to -

    ******************************************************************************/
    // Pin the buzzer is attached to
    int buzzerPin = 5;

    // Pin the button is attached to
    int buttonPin = A3;

    // Variable to store the button's state 
    int buttonState = 0;

    // Set a time in milliseconds for all delays
    int delayTime = 100; 

    // Notes
    const int C = 1046;
    const int D = 1175;
    const int E = 1319;
    const int F = 1397;
    const int G = 1568;
    const int A = 1760;
    const int B = 1976;
    const int C1 = 2093;
    const int D1 = 2349;

    void setup()
    

    void loop()
     else 
        
        delay(delayTime);
    }

    void playSong() 
    

After uploading the code, press the alligator clip connected to the input (buttonPin) to the alligator clip connected to the negative pin on the LilyPad. You should hear a sound play.

We can also take a look at the button press readings in the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics). You should begin seeing some values - the first is printing the number in the \*\*buttonState \*\* variable. If the button is not pressed, the value will show as 1. If pressed, it will read 0. We also print a message saying if the button is pressed or not.

If your button isn\'t behaving, take a look at a way of **debouncing** input readings with this [tutorial](https://www.arduino.cc/en/Tutorial/Debounce).

Learn more about buttons and switches in our [Switch Basics](https://learn.sparkfun.com/tutorials/switch-basics) tutorial.

## Sewing Into a Project

We mentioned at the beginning of this tutorial that the buzzer isn\'t washable. Here are some methods for adding the buzzer to a project so it is detachable.

### Sewable Snaps

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/9/Buzzer_SewSnap1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/9/Buzzer_SewSnap1.jpg)

Create a detachable buzzer patch by stitching the buzzer to a small piece of cloth or felt with size 1/0 [sewable snaps](https://www.sparkfun.com/products/11347) on either side. You will need two pairs of snaps for this method. We used a male snap attached to the positive side of the buzzer and a female snap on the negative side to avoid accidentally plugging the buzzer in backwards. Stitch the snaps with conductive thread as you would any other LilyPad component (3-4 stitches) for a good electrical connection.

Materials needed:

- Small piece of felt/fabric (at least 1\" x 2\")
- Small needle
- Conductive thread
- \(2\) pairs of size 1/0 sew-on snaps

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/9/Buzzer_SewSnap2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/9/Buzzer_SewSnap2.jpg)

### Soldered Snaps

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/9/Buzzer_SolderSnap1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/9/Buzzer_SolderSnap1.jpg)

Size 4/0 sew-on snaps are the perfect size for soldering directly to the buzzer\'s sew tabs. Carefully solder the snaps to the tabs and use conductive thread to sew the mating snaps to the project. You will need to use a small needle to get through the small snap holes.

Materials needed:

- Soldering iron and solder
- Small needle
- Conductive thread
- \(2\) pairs of size 4/0 sew-on snaps

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/9/Buzzer_SolderSnap2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/9/Buzzer_SolderSnap2.jpg)

### Adding a Switch

To quickly shut off the sound in your project during debugging (or as an optional feature), we recommend adding a switch in line with the buzzer. Stitch the switch in between the assigned pin on the LilyPad Arduino and the positive tab on the buzzer. This allows the other features of the project project to still function while muting the sound from the buzzer.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/9/Buzzer_Switch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/9/Buzzer_Switch.jpg)

## Project Examples

### Interactive Stuffed Monster from [Sew Electric](https://www.sparkfun.com/products/12019)

This project from [Sew Electric](https://www.sparkfun.com/products/12019) is a singing and glowing monster that responds to touch. It uses the LilyPad Buzzer to play a song when you complete a circuit by touching conductive material on the monster\'s hands. *For full project instructions, you\'ll need a copy of the book.*

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/9/SewElectric_Monster.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/9/SewElectric_Monster.jpg)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/9/SewElectric_Monster2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/9/SewElectric_Monster2.jpg)

### Fabric Piano from [Sew Electric](https://www.sparkfun.com/products/12019)

Another [project](http://sewelectric.org/diy-projects/5-fabric-piano/) from Sew Electric is soft piano that plays different tones when you press on the keys. It can also be connected to a computer to play music through application for your [Mac](http://sewelectric.org/troubleshooting/piano-application-mac/) or [PC](http://sewelectric.org/troubleshooting/piano-application-pc/). *For full project instructions, you\'ll need a copy of the book.*

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/9/SewElectric_Piano.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/9/SewElectric_Piano.jpg)

### Musical Bracelet

You are not limited to just using a button or a switch to trigger sounds from the buzzer, here\'s an example of a wearable light-controlled musical instrument or Opto-Theremin. Control tones on the buzzer by covering the LilyPad Light Sensor. This project uses a switch to mute the buzzer when no sound is wanted.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/9/CyberCuff.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/9/CyberCuff.jpg)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/9/CyberCuffDetail.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/9/CyberCuffDetail.jpg)