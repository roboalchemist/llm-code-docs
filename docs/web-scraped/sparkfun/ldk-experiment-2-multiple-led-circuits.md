# Source: https://learn.sparkfun.com/tutorials/ldk-experiment-2-multiple-led-circuits

## Introduction

Welcome to the second experiment of the LilyPad Design Kit, where we\'ll learn how to add more than one [LED](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds) to a [circuit](http://learn.sparkfun.com/tutorials/what-is-a-circuit). Additionally, we\'ll learn about the two types of standard circuit configurations: [series and parallel](https://learn.sparkfun.com/tutorials/series-and-parallel-circuits).

[![finished circuits example](https://cdn.sparkfun.com/r/600-600/assets/6/2/3/f/e/5244b467757b7f71398b456a.jpg)](https://cdn.sparkfun.com/assets/6/2/3/f/e/5244b467757b7f71398b456a.jpg)

When working with LEDs, you'll use parallel circuits very often. In addition to being able to turn on more components with less voltage, they're more durable. In a series circuit, if one LED gets damaged, all of the LEDs will stop working. In a parallel circuit, one broken LED won't stop the others from lighting up! You may have heard of this effect, or experienced it firsthand, in Christmas lights.

In spite of the reasons to prefer parallel circuits for most projects, no education in basic circuits is complete without discussing series circuits, so we'll give one a try!

### Suggested Reading

Here are a few related tutorials that you might want to read over or refer to:

- [LDK Experiment 1](http://learn.sparkfun.com/tutorials/ldk-experiment-1-lighting-up-a-basic-circuit)
- [Parallel and Series circuits](https://learn.sparkfun.com/tutorials/series-and-parallel-circuits)
- [Light-emitting Diodes (LEDs)](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)
- [How do I power my project?](http://learn.sparkfun.com/tutorials/how-to-power-a-project)

## Gather Materials

Here are the components you\'ll need for this circuit. If you\'re using the LilyPad Design Kit, you\'ve already got these!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/0/c/8/a/b/5244b467757b7f81398b456a.jpg)](https://cdn.sparkfun.com/assets/0/c/8/a/b/5244b467757b7f81398b456a.jpg)

You'll also want scissors, fabric, an embroidery hoop, and possibly a needle threader.

Go ahead and get the fabric set up in the embroidery hoop, and start with a threaded, knotted needle.

[![fabric in hoop](//cdn.sparkfun.com/r/600-600/assets/9/1/f/4/5/5122ba6ace395f5d0f000001.jpg)](//cdn.sparkfun.com/assets/9/1/f/4/5/5122ba6ace395f5d0f000001.jpg)

## Adding LEDs to a Parallel Circuit

We're going to use the circuit you made in [LDK experiment 1](http://learn.sparkfun.com/tutorials/ldk-experiment-1-lighting-up-a-basic-circuit) as the foundation for our [parallel](https://learn.sparkfun.com/tutorials/series-and-parallel-circuits/parallel-circuits) circuit. In a parallel circuit, you sew all of the positive pins to each other and all of the negative pins to each other. As in experiment 1, you never want to allow the positive and negative traces to come into contact with each other. For this circuit, don't use any red or yellow LEDs you still have \-- you'll need those for the series circuit!

**Note:** Remember to take your battery out while you're sewing, to prevent battery drain and short circuits while you\'re sewing.

### Positive Trace

[![positive trace tie-in](//cdn.sparkfun.com/assets/f/2/c/c/d/5122b6c9ce395f5911000003.png)](//cdn.sparkfun.com/assets/f/2/c/c/d/5122b6c9ce395f5911000003.png)

Start with your needle threaded and knotted. Sew a new stitch into the positive pin of the LED you used on the initial circuit, and add another tight stitch on top of the stitches holding it down. Due to the uninsulated nature of [conductive thread](http://learn.sparkfun.com/tutorials/sewing-with-conductive-thread), the thread you are currently sewing with is now conductively connected to your original circuit. The trace you start sewing now is a continuation of the positive trace that already existed in the original circuit.

[![good and bad examples](//cdn.sparkfun.com/assets/b/c/5/7/c/5122b6c8ce395f390f000002.png)](//cdn.sparkfun.com/assets/b/c/5/7/c/5122b6c8ce395f390f000002.png)

*Green = correct traces, Red = incorrect traces.*

From here, sew in a line to where you'd like the positive pin of your next LED. You're going to need to keep the positive and negative traces parallel to each other (hence 'parallel' circuit), so don't place the new LED such that its position is reversed from the original LED.

[![additional LEDs positive trace](//cdn.sparkfun.com/assets/5/9/4/f/8/5122b6c8ce395f8921000000.png)](//cdn.sparkfun.com/assets/5/9/4/f/8/5122b6c8ce395f8921000000.png)

Sew the positive pin of the second LED down with three stitches, as you have done with all previous pins. From here on, I'm just going to tell you to sew the pins down, but please continue to use several stitches per pin! Continue sewing to the third LED, and sew that positive pin as well. Keep thinking in a parallel fashion as you locate the third LED.

That's the end of the positive trace for this circuit. Go ahead and tie your thread off, and cut it.

### Negative Trace

Begin with a newly threaded needle. As you did on the positive trace, sew one stitch around the negative pin of your LED on the original circuit, to connect your new trace to the old.

Stitch from here in a line to the new LEDs, sewing each one down as you go. Be careful not to cross or contact your positive trace while you do this.

[![Tie-in negative trace](//cdn.sparkfun.com/assets/9/0/c/f/3/5122b6c8ce395f2412000001.png)](//cdn.sparkfun.com/assets/9/0/c/f/3/5122b6c8ce395f2412000001.png)

Knot and cut your thread on the finished negative trace, and do a quick check for stray threads, long knot-ends, and anything else that might cause a [short circuit](http://learn.sparkfun.com/tutorials/what-is-a-circuit/short-and-open-circuits#short).

[![additional LEDs negative trace](//cdn.sparkfun.com/assets/6/b/3/0/a/5122b6c8ce395fe902000001.png)](//cdn.sparkfun.com/assets/6/b/3/0/a/5122b6c8ce395fe902000001.png)

Double-check that you don\'t have any loose threads, crossed traces, or other visible problem spots. If everything looks good, slide your battery into the holder, positive side up. All three of your LEDs should light up. You've successfully completed a multi-LED parallel circuit!

## Creating a Multi-LED Series Circuit

One of the things that's very different about a series circuit is the power requirement. To create this circuit, you're going to need more power than you needed for the parallel circuit, so we'll be using two batteries instead of one. In the parallel circuit, we connected all of the positive pins to each other, and all of the negative pins to each other. In the series circuit, things are very different. We'll be creating our circle by connecting each positive to a negative, each negative to a positive. You'll want to use red and yellow LEDs for this circuit, because they have the lowest [forward voltage drop](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds/delving-deeper#fwdV) requirement.

[![alt text](//cdn.sparkfun.com/r/300-300/assets/4/3/3/3/e/5122b6c9ce395f3f12000000.png)](//cdn.sparkfun.com/assets/4/3/3/3/e/5122b6c9ce395f3f12000000.png)

Once again, let's start with the battery packs. You'll need two of them, so we\'re going to combine them in a series circuit. Start by placing the battery pack you'd like to be on top, and make sure you leave room for another one on the fabric below it. Point the negative pins down towards the second battery pack location.

[![alt text](//cdn.sparkfun.com/r/200-200/assets/0/5/4/0/d/5122b6c8ce395ffb0e000001.png)](//cdn.sparkfun.com/assets/0/5/4/0/d/5122b6c8ce395ffb0e000001.png)

Sew down one negative pin with a few stitches.

[![alt text](//cdn.sparkfun.com/r/300-300/assets/4/a/2/3/5/5122b6c8ce395f6211000001.png)](//cdn.sparkfun.com/assets/4/a/2/3/5/5122b6c8ce395f6211000001.png)

Next, place your second battery pack directly underneath the first one, with the **positive** pins pointed towards the **negative** pins of the first battery pack. Sew just one or two stitches from the negative pin you've already sewn down to the closest positive pin on the other pack, and stitch that positive pin down.

[![alt text](//cdn.sparkfun.com/r/300-300/assets/8/e/a/c/c/5122b6c8ce395f0d12000001.png)](//cdn.sparkfun.com/assets/8/e/a/c/c/5122b6c8ce395f0d12000001.png)

Sew from this positive pin, in several stitches to the other positive pin on this board, and sew the second pin down.

[![alt text](//cdn.sparkfun.com/r/300-300/assets/3/b/f/a/c/5122b6c8ce395f6912000004.png)](//cdn.sparkfun.com/assets/3/b/f/a/c/5122b6c8ce395f6912000004.png)

From this positive pin, take another stitch or two up to the remaining negative pin on the first battery pack.

[![alt text](//cdn.sparkfun.com/r/300-300/assets/b/5/c/d/c/5122b6c8ce395f1012000000.png)](//cdn.sparkfun.com/assets/b/5/c/d/c/5122b6c8ce395f1012000000.png)

You should now have one set of negative pins attached to one set of positive pins, with another set of each unsewn positives and negatives pointed up and down, respectively. Knot and cut your thread, getting ready to sew a new trace. Start up at the unsewn positive traces, which should be at the top edge of your top battery pack. Sew down the pin furthest from the side you'd like your LEDs on, then sew a few stitches to the other positive pin and sew that down as well.

[![alt text](//cdn.sparkfun.com/r/300-300/assets/7/0/9/d/4/5122b6c9ce395f5612000000.png)](//cdn.sparkfun.com/assets/7/0/9/d/4/5122b6c9ce395f5612000000.png)

From here, sew to where you'd like your first LED, and sew down the positive pin. Knot and cut your thread here.

[![alt text](//cdn.sparkfun.com/r/300-300/assets/0/2/8/4/9/5122b6c8ce395fc412000002.png)](//cdn.sparkfun.com/assets/0/2/8/4/9/5122b6c8ce395fc412000002.png)

Re-knot your thread and sew down the negative pin of the same LED with the new length of thread. The positive and negative sides of this LED should not be connected to each other by any thread. Sew from this negative pin to where you would like the **positive** pin of the next LED to be, and sew that positive pin down. Once again, knot and cut your thread.

[![alt text](//cdn.sparkfun.com/r/300-300/assets/2/8/d/f/7/5122b6c8ce395fd911000002.png)](//cdn.sparkfun.com/assets/2/8/d/f/7/5122b6c8ce395fd911000002.png)

Start again with your new thread and sew the negative pin of the second LED to the positive pin of the third LED, then knot and cut your thread.

[![alt text](//cdn.sparkfun.com/r/300-300/assets/5/f/0/8/0/5122b6c8ce395fb512000000.png)](//cdn.sparkfun.com/assets/5/f/0/8/0/5122b6c8ce395fb512000000.png)

With this last independent length of thread, sew down the negative pin of the third LED, and sew from there to the nearest negative pin of the bottom battery pack; these negative pins should be the last ones left unsewn. continuing this trace, sew the first negative battery pin down.

[![alt text](//cdn.sparkfun.com/r/300-300/assets/9/c/1/7/8/5122b6c8ce395f4f12000001.png)](//cdn.sparkfun.com/assets/9/c/1/7/8/5122b6c8ce395f4f12000001.png)

Sew a few stitches to the other negative pin of the battery pack, and sew that down as well. Knot and cut your thread, and take a quick look for long thread end, dangling thread, loose stitches, or other problems that could cause [shorts](http://learn.sparkfun.com/tutorials/what-is-a-circuit/short-and-open-circuits#short).

[![alt text](//cdn.sparkfun.com/r/300-300/assets/a/8/a/1/9/5122b6c8ce395fe812000000.png)](//cdn.sparkfun.com/assets/a/8/a/1/9/5122b6c8ce395fe812000000.png)

Once you're sure you don't have any extraneous thread mucking up your circuit, put both batteries in. All three LEDs should light up! Depending on the colors you've used, you're likely to see that the lights in the parallel circuit are significantly brighter than the ones in the series circuit.