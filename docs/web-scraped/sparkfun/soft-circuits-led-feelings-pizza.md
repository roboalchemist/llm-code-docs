# Source: https://learn.sparkfun.com/tutorials/soft-circuits-led-feelings-pizza

## Introduction

[![alt text](//cdn.sparkfun.com/r/600-600/assets/4/b/c/2/a/511aaf20ce395f6b07000006.JPG)](//cdn.sparkfun.com/assets/4/b/c/2/a/511aaf20ce395f6b07000006.JPG)

Love is sort of an unavoidable human condition, be it love for a person or a delicious snack. So here \-- whether you give it to someone you love more than pizza, or keep it for yourself as a symbol of your own undying love for pizza \-- are detailed instructions on how to make your own slice of LED-riddled, felt Feelings Pizza. Is it silly? Yes. Does it serve a purpose? Other than amusement, not especially. So why are we doing this? We are doing this because it\'s better than watching Rock of Love re-runs, and why not.

As a side bonus, this is also a good project to introduce kids to electronics, as the supplies are inexpensive, the electronic components are simple and the danger level is low.

### Suggested Reading

If you\'d like to start from square one, here are a couple tutorials that cover some of the basic concepts we\'ll be using to build our dream pizza:

- [Sewing with conductive thread](http://learn.sparkfun.com/tutorials/sewing-with-conductive-thread)
- [Sewing a basic circuit](https://learn.sparkfun.com/tutorials/ldk-experiment-1-lighting-up-a-basic-circuit)

## The Recipe

[![alt text](//cdn.sparkfun.com/r/600-600/assets/d/e/7/9/8/511aa2a4ce395f3d07000003.JPG)](//cdn.sparkfun.com/assets/d/e/7/9/8/511aa2a4ce395f3d07000003.JPG)

Here is a wishlist of the electronic components needed to follow along with this tutorial:

You will also need:

- Felt pizza bits (I used wool felt from a craft supply store - I cut the pieces with a laser cutter but you can cut the pizza and toppings out by hand; felt is very easy to work with):
  - two triangles for the front and back of the pizza (so we can hide the circuitry between them); one yellow for cheese, and one brown for the crust
  - one crust-colored piece to go across the top of the front
  - toppings of choice: I made mushrooms, green and black olives, and red, heart-shaped pepperonis (these are the only ones that really matter for this project, since the hearts will be the part that lights up)
- fabric glue or hot glue to attach toppings

## The Setup

You'll want to start by figuring out a layout for your toppings on the top triangle - you can put the toppings wherever you like, but be sure to space out the pepperonis enough that you'll be able to sew an LED underneath each one with enough room. You can attach the toppings to the top piece now if you like, as all our circuitry will be sewn onto the crust piece, or you can just mark a small dot where you know your pepperonis will be.

[![alt text](//cdn.sparkfun.com/r/600-600/assets/6/c/4/e/7/511aa66fce395f5406000003.JPG)](//cdn.sparkfun.com/assets/6/c/4/e/7/511aa66fce395f5406000003.JPG)

Once you've decided where you want your pepperonis, use small scissors to cut a tiny hole in the top triangle underneath where each pepperoni will be so the LED can shine through more easily.

[![alt text](//cdn.sparkfun.com/r/600-600/assets/f/b/1/2/b/511aa7c3ce395fd540000000.JPG)](//cdn.sparkfun.com/assets/f/b/1/2/b/511aa7c3ce395fd540000000.JPG)

Stack the top piece on the crust and mark through the holes with a pencil so you know where to sew down each LED on the crust piece. Then attach all your toppings to the top piece of the pizza and set it aside.

[![alt text](//cdn.sparkfun.com/r/600-600/assets/a/6/9/6/8/511aa7cdce395ffe05000001.JPG)](//cdn.sparkfun.com/assets/a/6/9/6/8/511aa7cdce395ffe05000001.JPG)

[![alt text](//cdn.sparkfun.com/r/600-600/assets/e/c/e/4/e/511aa7d6ce395f5706000000.JPG)](//cdn.sparkfun.com/assets/e/c/e/4/e/511aa7d6ce395f5706000000.JPG)

## Electronics. Part I. 

Now: ELECTRONICS. I want my LilyTwinkle board and the three LEDs to be hidden inside the pizza, but I want to be able to access the on/off switch and the battery, so I'm going to sew the battery holder onto the back of the pizza first.

Thread your needle with a 12-16" piece of thread (doubled as in the photo, with a double knot at the end to prevent it from pulling through the felt).

[![alt text](//cdn.sparkfun.com/r/600-600/assets/7/b/2/e/c/511aa9f2ce395f0505000003.JPG)](//cdn.sparkfun.com/assets/7/b/2/e/c/511aa9f2ce395f0505000003.JPG)

Place the battery holder in the upper left corner of what will be the very back of your pizza, with the switch right side up and the positive sides on the left. Sew the upper positive terminal down (I loop each stitch through the terminals three times to ensure strong contact with the conductive thread), run stitches down to the lower positive terminal, and sew that down also. Don\'t cut the thread yet! We\'ll continue this circuit on the inside.

[![alt text](//cdn.sparkfun.com/r/600-600/assets/f/a/2/5/8/511aaa33ce395f7206000001.JPG)](//cdn.sparkfun.com/assets/f/a/2/5/8/511aaa33ce395f7206000001.JPG)

[![alt text](//cdn.sparkfun.com/r/600-600/assets/7/4/e/4/f/511aaa33ce395f3907000000.JPG)](//cdn.sparkfun.com/assets/7/4/e/4/f/511aaa33ce395f3907000000.JPG)

## Electronics. Part II. 

Now, without cutting our first piece of thread, we will flip the felt over and begin sewing our circuit on the other side, which will be the inside of our pizza. On the blank side of the felt \-- somewhere below where the battery holder lies on the other side, but not obstructing any of the spots you'll need to sew down the LEDs to match up with your pepperonis \-- continue your stitch from the second positive terminal of the battery holder to the positive terminal on the LilyTwinkle, and sew it down.

[![alt text](//cdn.sparkfun.com/r/600-600/assets/0/a/f/1/7/511aacface395f1306000002.JPG)](//cdn.sparkfun.com/assets/0/a/f/1/7/511aacface395f1306000002.JPG)

Now you can cut and tie off your thread (make sure to tie it tight and cut the ends of all threads short to avoid crossing stray threads and shorting your circuit), and re-thread the needle with a new piece of conductive thread for the next part.

[![alt text](//cdn.sparkfun.com/r/600-600/assets/6/5/e/9/b/511aad3bce395fdf05000003.JPG)](//cdn.sparkfun.com/assets/6/5/e/9/b/511aad3bce395fdf05000003.JPG)

## Electronics. Part III. 

Using a new piece of thread for each LED, sew a numbered terminal (whichever ones are easiest to reach with a stitch) on the LilyTwinkle to the positive terminal on an LED, and cut and tie off the thread. Make sure the LEDs are placed on the spots you marked earlier to match up with the locations of the pepperonis.

[![alt text](//cdn.sparkfun.com/r/600-600/assets/c/0/2/8/f/511aae36ce395f0107000001.JPG)](//cdn.sparkfun.com/assets/c/0/2/8/f/511aae36ce395f0107000001.JPG)

Once all your LEDs are sewn to the LilyTwinkle board, use one long piece of conductive thread to connect the negative terminals of the LEDs to each other and then to the negative terminal on the LilyTwinkle. Tie off the thread, and cut it.

[![alt text](//cdn.sparkfun.com/r/600-600/assets/2/7/8/2/c/511aae36ce395f9206000001.JPG)](//cdn.sparkfun.com/assets/2/7/8/2/c/511aae36ce395f9206000001.JPG)

## Electronics. Part IV. 

[![alt text](//cdn.sparkfun.com/r/600-600/assets/f/8/8/9/7/511aaeb3ce395fe905000000.JPG)](//cdn.sparkfun.com/assets/f/8/8/9/7/511aaeb3ce395fe905000000.JPG)

Finally, sew both negative terminals on the battery holder down and to each other, and then to the negative terminal on the LilyTwinkle (it'll be tight with the thread from the negative LED terminals, but now it's all connected!). This is what my full circuit looks like (yours will look different depending on the placement of your LEDs.

[![alt text](//cdn.sparkfun.com/r/600-600/assets/4/e/3/1/a/511aaeb3ce395f3807000003.JPG)](//cdn.sparkfun.com/assets/4/e/3/1/a/511aaeb3ce395f3807000003.JPG)

## The Moment of Truth

Jam that coin cell battery into the battery holder (writing side up), and flip the switch to "on."

[![alt text](//cdn.sparkfun.com/r/600-600/assets/b/c/0/e/4/511aaf20ce395f2607000001.JPG)](//cdn.sparkfun.com/assets/b/c/0/e/4/511aaf20ce395f2607000001.JPG)

Your LEDs should light up randomly, at which point you can plop the top of your pizza over the bottom and, if you lined everything up correctly, your heart-shaped pepperonis should begin twinkling festively. Hurray! Now you can glue or sew your pizza halves together (stick to the edges and don't get glue all over your circuits) and be on your way, to wave your success from the rooftops and bask in the accolades of potential love interests everywhere.

[![alt text](//cdn.sparkfun.com/r/600-600/assets/4/b/c/2/a/511aaf20ce395f6b07000006.JPG)](//cdn.sparkfun.com/assets/4/b/c/2/a/511aaf20ce395f6b07000006.JPG)

Congratulations!