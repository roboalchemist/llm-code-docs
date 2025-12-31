# Source: https://learn.sparkfun.com/tutorials/proto-pedal-chassis-hookup-guide

## Introduction

The Proto Pedal chassis comes with the holes required to interface the PCB, but since different pedal designs use different types of controls, we\'ve left drilling holes for the controls to the builder. This guide will take you through laying out and drilling holes, then painting the chassis.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-77.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-77.jpg)

We\'ll be drilling a chassis to match the [digital Proto Pedal example](https://learn.sparkfun.com/tutorials/proto-pedal-example-programmable-digital-pedal), which shows an application using a [Teensy 3.2](https://www.sparkfun.com/products/13736) and an [Audio Adapter](https://www.sparkfun.com/products/12767) with the [Proto Pedal](https://www.sparkfun.com/products/13124) and [Proto Pedal Chassis](https://www.sparkfun.com/products/13967).

### Materials

#### Required:

- The [Proto Pedal](https://www.sparkfun.com/products/13124) and [Chassis](https://www.sparkfun.com/products/13967)
- A twist drill bit (not spade) that matches the desired hole diameter
- A pilot drill of about 1/8 inch. Make sure it\'s sharp and fresh!
- A few drill bits between to step up to the desired size.
- Ruler
- Center punch (a large metal screw and hammer will work)
- Variable speed hand drill, wired or cordless
- Clamps, vice, holders
- Some scrap wood blocks
- A pencil

#### Also Recommended:

- Thin circular file (needle or chain sharpening file)
- Speed square
- Combination square / scribe
- Spring loaded center punch
- Isopropyl Alcohol / Acetone
- Paint

### Recommended Reading

- If got here from the ether, check out the [Proto Pedal Assembly and Theory guide](https://learn.sparkfun.com/tutorials/proto-pedal-assembly-and-theory-guide) which shows how to assemble the circuit board that goes in the case. Make sure to assemble this first.

## Laying Out The Holes

Before drilling, we need to figure out where to locate the holes.

This is an exercise in three-dimensional thinking. We need to account for the location of the controls on the panel, as well as the clearance above and below. Above the surface of the pedal, you\'ll probably want to leave some room around the controls, so you can grab them. Inside the chassis, you need to consider where the internal portion of the control will be located, especially in relation to the taller components on the PCB.

### Rough Layout

In this example, we wanted to put five potentiometers on the chassis. We simply moved the knobs around on top of the chassis until we reached a reasonable arrangement. Notice that we\'re leaving clearance for the TRS jacks.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-12.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-12.jpg)

*Laying out the knobs*

We had the circuit board nearby to use as a reference, to help see where internal objects are are located. We also had the assembled stack of Teensy 3.2 and Audio Adapter nearby, which we test fit several times as we worked. This allowed us to recognize that the stack doesn\'t stand much above the board, leaving vertical space to place a pot over it.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-13.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-13.jpg)

*Tracing the knob outlines*

With the knobs in rough proximity of their ultimate destinations, we traced them in pencil, making circles on the box.

### More Precise Layout

With the knobs removed, we measured the location of their centers from the top edge of the box. We averaged the measurements, so the holes would be in reasonable alignment.

Here we\'ve marking a line 2 1/2 inches from the top edge, using a combination square to insure a consistent distance. If you don\'t have a square, you can carefully measure two points and draw a line between them.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-14.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-14.jpg)

*Setting the vertical alignment*

The top row is an inch closer to the edge, at 1 1/2 inches.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-15.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-15.jpg)

*Do this for each row.*

With the lines for the rows drawn, we\'ll move on to the horizontal position of each pot within the rows.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-16.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-16.jpg)

*Center your rule to a common overlap to identify center*

We decided to center these knobs, so we set the ruler on the box such that the edges aligned the same number of subdivisions past the last whole inch, or a little more than 1/4 inch, at 9 1/4 and 5 3/4. Now, the 8 1/2 inch mark is centered horizontally and we can count subdivisions out from there to make sure the holes are equally spaced.

The top row holes were marked 1/2 way between the marks in the bottom row, resulting in a regular \"M\" shape.

Notice that the rough knob outlines are no longer accurate to the center marks. The outlines were just eye-balled on for aesthetics, while the measured marks insure accuracy.

#### Punching

Punch the center of each hole. This will help guide the drill bit.

If you\'ve never seen a spring loaded center punch before, they\'re really cool. Just press down until the internal spring is sprung, and it leaves a mark behind. You can get these at most hardware stores.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/3click.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/3click.png)

*Using a spring loaded punch*

Or if you don\'t have a center punch, use a large screw and a hammer. Big pan heads work well, but wood deck screws or drywall screws are too pointy.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-20.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-20.jpg)

*Using a screw for a punch*

Now let\'s get to the real action!

## Drilling

When you\'re happy with your center punch marks, it\'s time to start drilling.

### Drilling Metal

When drilling metal, it\'s important to start with a small pilot hole, and work progressively up to the desired size. For these holes, they\'ll be 5/16 inch for the [10k linear potentiometers](https://www.sparkfun.com/products/9939). Each successive hole should be 25% to 50% larger than it\'s predecessor.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/drillhit.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/drillhit.png)

*This diagram shows the maximum overlap desired.*

When drilling metal, use a moderately slow speed, and reasonable pressure. A drill that\'s too fast can cause the bit to overheat, and is more dangerous if you lose control.

### Preparation

Before drilling, solidly secure the workpiece with a vice or a clamp.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-21b.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-21b.jpg)

*Preparing to drill*

Here, three bits have been selected and the piece is clamped. You may think you can just hold the piece down with your hand, but more often than not it will wedge on the drill bit and spin around, whacking your hand and causing injury (and perhaps damaging the workpiece). Also, use scrap wood to protect the piece from marring, and to provide something soft for the drill bits to crash into when they break through.

### Drilling

Start with a small pilot hole. This is the most important drill as it will guide the other holes.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-22.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-22.jpg)

*Carefully align the pilot holes*

A challenge with using a hand drill is maintaining perpendicularly to the work surface. As a reference, set a square on the piece and use it as a visual guide. Before you start drilling, hold the drill where you think it should go and move your head around like an owl to see that you\'ve got good alignment from all angles.

When you\'re ready, drill with a medium speed and decent pressure. The bit should produce a constant stream of waste material. If it seems like it\'s just spinning, doublecheck you\'re not in reverse, try adding more pressure, or slow the drill speed.

**Double check alignment!** After drilling the pilot holes, check that they are aligned as they should be. If not, you can use a thin file to make the hole oblong and bring the geometric center back in line, and the next bit should correct the offset. With sharp bits and good perpendicular alignment, this shouldn\'tbe required.

After the pilot holes are complete, move up to the next larger bit, and use it to enlarge each hole. As you move to larger and larger bits, less speed should be required.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-23.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-23.jpg)

*Progressing through the selected drill bits, enlarging the holes*

After an intermediate hole, we can drill the final hole, 5/16 inch.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-24.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-24.jpg)

*The final size is being drilled here.\
The drill has been stopped partway through to show the overlap detail (lower right).*

The drilled holes frequently have a sharp burr around the edge. If you like, you can bevel the edges with a chamfer tool, or clean them up with a file. It\'s not required, but will get rid of the sharp edges.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-26.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-26.jpg)

*Cleaning up the edges*

## Notes for Potentiometers

The potentiometers have an alignment / retention boss. You can either drill an extra hole to retain it, or trim it off with a pair of side cutters.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-27.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-27.jpg)

*Removing the bosses.*

## Extra holes for the Teensy

For the Teensy based digital pedal, we\'re going to add a couple extra holes. The first is one on the side of the chassis for the USB connector, plus a second smaller hole in the top of the pdeal, so we can reach the manual-load button.

As with our initial layout, we\'re going to do it empirically, using the final parts to gauge where the holes need to be. We started with the USB port, measuring on the left side of the enclosure.

### Programming Port

First, choose the location of the programming hole based on where you want the Teensy to be in the pedal. Use the circuit board as a guide, aligning the 1/4 inch jack shoulders to the inside plane.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-31.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-31.jpg)

*Using the board as a guide for hole placement*

Approximate the height of the hole by holding the circuit board where it will sit when assembled, and cross the previous mark.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-32.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-32.jpg)

*Aligning the height of the hole*

Then, punch a center point, and move on to drilling.

We going all the way up to our largest drill, to accommodate the USB plug molding, making 4 drills overall. This time, were using a vice to hold the workpiece, again using blocks of wood to protect it.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-33.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-33.jpg)

*Preparing to drill*

As before, we\'re working progressively up to the larger drills.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-34.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-34.jpg)

*Here the pilot hole is being enlarged. I like to allow more overlap on the smaller drills.*

Since this hole is larger, there will be two intermediate drills.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-35.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-35.jpg)

*The second oversize closer to the first size.*

Watch the quality of the waste material. It\'s a good sign that speeds and pressures are correct when the waste forms into curls rather than little chips. Also, it can be seen here that the overlap is quite small for this large bit. Otherwise, the bit would have a great tendency to catch when getting close to being through.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-36.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-36.jpg)

*Drilling the final USB hole.*

Once the drilling is complete, we want to chamfer the edges of the hole. The chamfer is more important for this hole, because the sharp edge won\'t be covered with a control. This time, the hole is as large as the bit were were chamfering with before, so we have to do it manually, with a file.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-37.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-37.jpg)

*Deburring with a file*

### Reset Switch

We used a similar triangulation process for the hole for the button. Here, there\'s a mark where it *should* be, but that is underneath a knob. The hole was moved outside of the knob outlines, and will have to be used at a slight angle.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-30.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-30.jpg)

*Center punching the button hole*

Since this hole is smaller, we didn\'t need to step through as many drills.

## Painting

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-79.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-79.jpg)

For a finishing touch, you can paint your pedal. We\'ve chosen to try out a couple Rust-Oleum oil-based enamels, which have wildly different properties based on the color, and a spray job using red Krylon Shimmer spray paint, with a clear overcoat.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-38.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-38.jpg)

*Cleaning the workpiece*

Start by cleaning the case with acetone or isopropyl alcohol. This removes oils and pencil marks.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-39.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-39.jpg)

*Make sure to not touch clean areas!*

The liquid paint was applied using a foam applicator wedge.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-40.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-40.jpg)

*Use scrap wood to catch extra paint*

Painting can be a messy process, and you\'re likely to get some on your work surface. You can protect against paint slop with a drop cloth, or other scrap materials, such as wood, or cardboard.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-42.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-42.jpg)

*Allowing to dry*

You can paint the faces of the screws too, if you wish, but try not to get any into the threaded holes, or they may be difficult to drive.

### Painting Results

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-77.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/5/Proto_Pedal_Tutorial_Images-77.jpg)

You can see that the red paint tended to pile up and stay streaky, and needs to be sanded and coated again. This paint should probably be used with a sprayer or thinned out. The black leveled well and could be sanded to a decent finish, but the red refused to level as can be seen above. The Shimmer paint was pretty much fabulous.