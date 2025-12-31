# Source: https://learn.sparkfun.com/tutorials/bare-conductive-musical-painting-

## Introduction

Hello everybody! I am Detour, and I am here to take you on a detour and off the traditional path of art. Since the days of Michelangelo and Leonardo da Vinci, traditional art has been treated as something that can be looked at but not touched. Step into any gallery in your local neighborhood, and you can see the "DON'T TOUCH" signs plastered throughout the space. This way of thinking creates an environment that disconnects the viewer from the art. This means that, in most cases, only ONE of the five senses that we can use to experience art is stimulated.

Luckily, technology came along with ways to break the archaic paradigm. In this tutorial, I will show you how I am working to take this approach in my art. More specifically, I will take you through the process I use to create interactive art that not only looks good on a wall but can be touched and played like an instrument.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/4/Detour.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/Detour.png)

*DJ A-L playing a musical self-portrait painted by Detour*

### Suggested Reading/Viewing

Before you get started, you should have a good understanding of the following:

- A basic understanding of [Capacitors](https://learn.sparkfun.com/tutorials/capacitors) is nice but not required.
- [Wikipedia article](http://en.wikipedia.org/wiki/Capacitive_sensing) on capacitive sensing.
- [How to Solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) - Light soldering is required to interface the wires to the Touch Board.
- This episode of ElectriCute shows off the functaioanlity of the Bare Conductive Touch Board very well:

## Required Materials 

Here are all the tools, supplies, hardware and software used in this tutorial:

### Tools and Supplies

- 1 x wood panel Canvas (size is up to you)
- Acrylic Paints
- Paint brush
- Guerilla tape
- Power drill
- 1/16\" drill bit
- Gesso
- [Soldering kit](https://www.sparkfun.com/products/13086)
- Foam brush
- wood block (1" x 3.5" x 2.5")
- 3 screws
- [Spool of wire](https://www.sparkfun.com/products/11375)

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/essentials_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/essentials_2.jpg)

### Software

- You\'ll need a computer running [Garage Band](https://www.apple.com/mac/garageband/) or a similar program.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/essentials_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/essentials_1.jpg)

### Electronic Supplies

## Assembly

1.  First, we need to prep the canvas for the paint. To do this, we need to unpack the wood panel canvas, and cover it in a layer of gesso. This will help create a consistent surface on which the acrylic paint can adhere. Let\'s use our foam brush to spread a thin layer of gesso across the canvas. You can do this multiple times, after a layer dries. Wood panel canvases that are pre-gessoed are available at art shops as well. In this case, you can skip this step.

    ::: 
    [![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/step_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/step_1.jpg)
    :::

2.  Use this step to paint anything that you would like. The goal is to create a painting where you are able to add the solid black Bare Conductive paint without compromising the image that you painted. I just took a few minutes to whip up a painting of one of my favorite artists, Marvin Gaye. OK, I'll be honest, it took about a 2 hours to paint this.

    ::: 
    [![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/Step-2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/Step-2.jpg)
    :::

3.  Now that your painting has had time to dry, it's time for the real fun to begin. Look at your painting, and decide where there are opportunities to place the interactive paint. Once you decide on the areas, drill small 1/16\" holes into the canvas with the power drill.

    I decided to drill mine in the area of the keypad, because it seamlessly blends in with the image.

    ::: 
    [![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/Step-3)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/Step-3)
    :::

4.  Using the interactive pen, fill the holes you just drilled such that paint comes out of the other side of the canvas. Once complete, paint the front side of the your painting using a brush and the jar of Bare Conductive paint. Allow time to dry. This will conceal the holes you drilled.

    ::: 
    [![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/step_4)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/step_4)
    :::

5.  Attach the Touch Board the the back of the canvas. I accomplished this by using a small 3.5" x 2.5" block of wood that I affixed to the bottom of the canvas using wood glue. I then attached the Touch Board with 3 small screws. Be careful not to use too long of a screw, or it will poke through the front of the canvas.

    ::: 
    [![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/step-5.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/step-5.jpg)
    :::

6.  Run 12 strips of wire from the 12 electrodes on the Touch Board to each of the drilled holes. Use the Guerrilla Tape to hold down the wires so that they don\'t move. Connect the wire to the drilled holes using a glob of the interactive paint

    ::: 
    [![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/step_6.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/step_6.jpg)
    :::

7.  Solder the wires to each of the electrodes.

    ::: 
    [![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/step_7.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/step_7.jpg)
    :::

8.  Time to get creative. Setup your Touch Board to be a midi Controller interface by following the [Bare Conductive's midi interface tutorial](http://www.bareconductive.com/make/midi-interface/).

    [![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/step_8)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/step_8)

9.  Now that you have all the right programs loaded onto your touch board, we are ready to rock-n-roll. Connect your iPad or Mac to the touch board using the micro USB. Open up the Garage Band program. Garage band should prompt a dialogue informing you that it sees a new MIDI input. Create a new project, and select an instrument to use. I love using the Hip-Hop drum machine. From there, it\'s just a matter of selecting sounds for each of your conductive paint pads and loading them on the Touch Board SD Card.

    ::: 
    [![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/step_9.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/step_9.jpg)
    :::

10. Once you have completed this step, enjoy your hard work! Here is a painting from my current collections.

    :::: 
    ::: 
    :::
    ::::