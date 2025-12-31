# Source: https://learn.sparkfun.com/tutorials/nest-thermostat-teardown-

## Introduction

Awhile ago I read about [Nest](https://nest.com/), a newfangled thermostat with a color display and some interesting \'learning\' techniques for keeping your home warmed or cooled, as sensible as possible. Did I mention the beast has IR proximity, PIR movement, humidity, magneto scroll, and a mini USB connector? Oh. It does.

[![alt text](https://cdn.sparkfun.com/assets/7/c/6/7/4/52e1584fce395f253c8b456c.jpg)](https://cdn.sparkfun.com/assets/7/c/6/7/4/52e1584fce395f253c8b456c.jpg)

It\'s kind of awesome, but it comes at a price. Pre-orders were \$249 + shipping but I\'m a sucker for new technology so I got in line. A few weeks after I placed my pre-order I got a piece of spam email from Nest offering a free professional installation. That\'s great, but I was not planning on my Nest ever seeing the light of day - I wanted to take it apart and see how it worked. So on a whim, I replied to the email:

*Hi Matt,*

*This offer is a great idea! I feel very much appreciated as a customer but I won\'t need an install, thanks! I can\'t wait to get my nest and poke around inside. Depending on what\'s inside it might be worth doing a homepage post. Would you mind?*

*From your friends at SparkFun,* *-Nathan*

Much to my surprise and honor, I got a response from Matt:

*Thanks for the note Nathan! I\'m a frequent shopper of SparkFun myself. Feel free to dig, poke, and post! -Matt Founder and VP Engineering*

No way! The founder/VP of engineering responded?! Thanks Matt! And you know of SparkFun? Very cool. We even got a semi-green light to post a tear down. This is a refreshing difference from some other companies [we have emailed](https://www.sparkfun.com/tutorials/323) in the past. When I received the Nest shortly after Thanksgiving, I set out to tear the beast apart.

\*\*Disclosure time: \*\*We didn\'t get Nest for free. This teardown was purely the result of Nate ordering stuff late night when he probably shouldn\'t be.

After tearing apart the Nest then re-assembling, it actually continued to function (a first for me!). I was so impressed with the thing that I stayed up way late to document the tear down. I have nothing but very positive things to say about the hardware design, website design, and user interface design of the Nest. It\'s slick. Really slick. I consider myself an amateur when it comes to consumer electronics so take this review with a grain of salt. But whoa - I just turned off my heat while writing this tutorial! Welcome to the future.

## Cracking It Open

The packaging of the device is on par or above what one would expect for \$250 - I even got a Nest branded screw driver. Neat. But we are not here for a packaging review now are we?

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/0/9/0/4/c/52e157acce395f3b558b4567.jpg)](https://cdn.sparkfun.com/assets/0/9/0/4/c/52e157acce395f3b558b4567.jpg)

Here\'s the nest shortly before meeting the business end of a Phillips head screw driver. Did I mention they included their own disassembly tools? They get a +1.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/e/6/8/f/d/52e1579fce395f67328b456c.jpg)](https://cdn.sparkfun.com/assets/e/6/8/f/d/52e1579fce395f67328b456c.jpg)

The camera was playing funny reflections with the glass and the apertures. Here we can see where the IR LEDs and sensor are exposed.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/9/9/8/e/8/52e157afce395f142b8b4568.jpg)](https://cdn.sparkfun.com/assets/9/9/8/e/8/52e157afce395f142b8b4568.jpg)

Back side. If you\'ve read some of [my other tutorials](https://www.sparkfun.com/tutorials/323), this miniUSB connector is completely surprising! Thank you Nest for including an external connector. I don\'t want to completely hack/reprogram/re-purpose the thing today, my goal is just to show off the internal hardware. But by making it easy to plug in you are opening the door way to good things.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/8/8/a/9/b/52e157afce395f07588b4567.jpg)](https://cdn.sparkfun.com/assets/8/8/a/9/b/52e157afce395f07588b4567.jpg)

This thing has an internal LiPo battery? Really? 2.1Wh over 3.7V = around 567mAh battery. That\'s fairly sizable for a thermostat. My guess is that the unit may need more power than the HVAC wiring can provide when WiFi is broadcasting and the display is on. The LiPo acts as a very large capacitor.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/f/b/8/6/3/52e157aece395f101a8b456d.jpg)](https://cdn.sparkfun.com/assets/f/b/8/6/3/52e157aece395f101a8b456d.jpg)

Here we have the head unit on the right. In the lower left we have the first layer of the housing - the bit that actually attaches to the wall. This includes the user press-able button as well as the 8+ connector to the house wiring. When you snap this thermostat to the plate on the wall, there is a multipin connector that connects through the first layer to the head unit. That said, there\'s an awful lot of exposed gold pads on the first layer. I\'m not entirely sure what they are there for but my first impression: This thing is extremely well designed and produced. The ribbons, connectors, battery, and hardware are all of very high quality.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/b/7/f/6/6/52e157afce395f06528b4569.jpg)](https://cdn.sparkfun.com/assets/b/7/f/6/6/52e157afce395f06528b4569.jpg)

Hi Fish. Must be the manufacturer?

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/f/2/c/1/1/52e157afce395fbd558b4567.jpg)](https://cdn.sparkfun.com/assets/f/2/c/1/1/52e157afce395fbd558b4567.jpg)

Up close on the head unit. Note the three wires coming from the battery: 3.7V, GND, and what else? A temperature sensor on the battery? A third wire on a LiPo is sort of odd for such a low current application.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/c/5/8/0/9/52e157a5ce395fde3a8b456a.jpg)](https://cdn.sparkfun.com/assets/c/5/8/0/9/52e157a5ce395fde3a8b456a.jpg)

A few things are cool here. Note the IC in lower left. I don\'t know what that is! It is facing towards the wall when the Nest is installed onto the wall. It doesn\'t read the dial, proximity, motion or anything I can fathom but it\'s a clear epoxy encased IC which usually indicates visible spectrum or light (IR) sensing - but why is it pointing at the wall? A dust sensor? Humidity? Nah.

Also you\'ll notice three Phillips head screws holding a small board south of the LiPo in place. That is the PIR. The small daughter board is powered and sensed through the screws (three screws = VCC/GND/Signal). I\'ve seen this technique before but I\'m not sure what they used it here. Perhaps it\'s because three screws are cheaper than three screws and a 3-pin connector.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/1/4/6/3/3/52e157a0ce395f3c158b456b.jpg)](https://cdn.sparkfun.com/assets/1/4/6/3/3/52e157a0ce395f3c158b456b.jpg)

Here is the PIR removed. The IC reads XLitos. Used to detect motion in a room.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/f/d/7/9/d/52e157acce395fc40c8b456b.jpg)](https://cdn.sparkfun.com/assets/f/d/7/9/d/52e157acce395fc40c8b456b.jpg)

Check that out! I\'ve seen magneto sensors like this before on the trackball for the Blackberry Pearl. We used the same type of sensors for the [Trackballer Breakout](https://www.sparkfun.com/products/9320). I am assuming these two sensors are reading the notches on the dial via magnetic field but I could be wrong. I love how they used a very tiny vertical board. This is one heck of a design, all for a thermostat!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/1/9/0/9/3/52e157b3ce395f933a8b4569.jpg)](https://cdn.sparkfun.com/assets/1/9/0/9/3/52e157b3ce395f933a8b4569.jpg)

The included Phillips screw driver got me this far, at this point I had to break out the Torx bits.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/5/6/a/0/8/52e157adce395f9f7f8b4567.jpg)](https://cdn.sparkfun.com/assets/5/6/a/0/8/52e157adce395f9f7f8b4567.jpg)

Note the high density connector on the left. It was something like 40 pins in a tiny ribbon cable. Look closely if you need to know how to flip up the connector to release the ribbon.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/a/6/b/c/6/52e157acce395f730b8b456c.jpg)](https://cdn.sparkfun.com/assets/a/6/b/c/6/52e157acce395f730b8b456c.jpg)

Here we can see the main board covered in a massive RF shield (and my thumb print). Is it cheaper just to throw a metal shield on everything than to risk FCC testing failure? Also note not one but two antenna connectors. It\'s odd to see external U.FL connectors on the board. They must be there for ease of testing? Next to the connectors you should see some gold clips. These actually make a compression contact to the dual flexible antennas embedded into the face of the unit.

Although I failed to capture them on the camera, there was two flexible PCB antennas in a vertical configuration. One antenna was marked \'Zigbee\'. Now this has my interest piqued. I assumed there was two antennas for better reception but perhaps one antenna is Wifi and one antenna is for something else? Zigbee? No way. Really? Could Nest be planning on adding other equipment control such as lighting or refridgeration? After using the Nest and its accompanying website, I certainly hope so.

## The Electronic Bits

With the RF shield removed, we can finally see what lies within.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/b/e/0/3/e/52e157abce395f42318b456c.jpg)](https://cdn.sparkfun.com/assets/b/e/0/3/e/52e157abce395f42318b456c.jpg)

Here\'s what we were waiting for. This is an astronomical amount of silicon for a thermostat!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/8/5/c/7/4/52e157adce395f47598b4567.jpg)](https://cdn.sparkfun.com/assets/8/5/c/7/4/52e157adce395f47598b4567.jpg)

Here are a few shots in case folks want IC identifiers.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/f/c/8/1/8/52e157adce395f07528b4567.jpg)](https://cdn.sparkfun.com/assets/f/c/8/1/8/52e157adce395f07528b4567.jpg)

I haven\'t looked any ICs up yet.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/f/c/1/a/0/52e157adce395fed4a8b4567.jpg)](https://cdn.sparkfun.com/assets/f/c/1/a/0/52e157adce395fed4a8b4567.jpg)

But they should be out there.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/9/a/7/c/a/52e157abce395fab158b456d.jpg)](https://cdn.sparkfun.com/assets/9/a/7/c/a/52e157abce395fab158b456d.jpg)

This is the back side of the main board. Note that this was completely covered up with another RF shield. That seems odd to me as there isn\'t much here but decoupling and another anonymous IC that has been bonded to the PCB. Did Nest really believe there would be that much mechanical shock and vibration that they bonded every IC to the PCB?!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/9/a/3/8/6/52e157acce395f774c8b4568.jpg)](https://cdn.sparkfun.com/assets/9/a/3/8/6/52e157acce395f774c8b4568.jpg)

Here is a view of the inside front face. You can see that they covered the lower small aperture of the face with the characteristic PIR prism material. Checkout our [motion sensor](https://www.sparkfun.com/products/8630) for a comparison. Ok, now take a step back and try to remember where all the screws, ribbons, and clips go. Astonishingly, the unit went back together within a few minutes - another mark of incredible DFM (design for manufacture).

## Putting It Back Together 

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/1/2/2/6/9/52e157adce395fcc3a8b456b.jpg)](https://cdn.sparkfun.com/assets/1/2/2/6/9/52e157adce395fcc3a8b456b.jpg)

After re-assembling I plugged in a miniUSB cable. After running a series of interesting characters on the display, I got this message - \'Please attach the display to its base\'. Booo.

[![alt text](https://cdn.sparkfun.com/assets/8/6/2/1/b/52e157b0ce395f99118b456b.jpg)](https://cdn.sparkfun.com/assets/8/6/2/1/b/52e157b0ce395f99118b456b.jpg)

But the unit did come up as a Mass Storage Device!

[![alt text](https://cdn.sparkfun.com/assets/c/7/b/6/1/52e157b8ce395fc2568b4567.jpg)](https://cdn.sparkfun.com/assets/c/7/b/6/1/52e157b8ce395fc2568b4567.jpg)

Who wants to use their thermostat as a 38MB jumpdrive? I do! I do!

Now it was time to actually wire the thing to my existing HVAC wiring and mount it to the wall. This was really easy and straight forward. Well, except for the fact I was too lazy to spackle and paint over the spots where the old, much larger thermostat lived. So I\'ll just take some really dark pictures so you can\'t see the holes in my wall:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/6/f/2/0/3/52e157adce395fed568b4567.jpg)](https://cdn.sparkfun.com/assets/6/f/2/0/3/52e157adce395fed568b4567.jpg)

*Shhh!*

Configuring the device was surprisingly easy. Interfacing with the device via the dial is a dream.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/8/7/8/b/1/52e157b0ce395ffe158b4569.jpg)](https://cdn.sparkfun.com/assets/8/7/8/b/1/52e157b0ce395ffe158b4569.jpg)

*Oh geesh. Not you too!*

Once connected to Wifi, Nest needed an update. Look closely for the pinkish dot in the upper left area. I took this photo with my cell phone so that you can see the IR LEDs triggering. It didn\'t come out well but it\'s fun to see through the camera of a cell phone.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/4/a/a/e/6/52e157afce395f2b308b4567.jpg)](https://cdn.sparkfun.com/assets/4/a/a/e/6/52e157afce395f2b308b4567.jpg)

Nifty.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/3/1/2/0/3/52e1579dce395f90248b4568.jpg)](https://cdn.sparkfun.com/assets/3/1/2/0/3/52e1579dce395f90248b4568.jpg)

The thing that really sealed the deal for me was when I went online to connect to the thermostat over the internet. To activate the new thermostat onto remote control you have to create a login to Nest.com. Creating my new account was the most basic and best account creation I have ever done! It was as simple as providing an email address and a password.

Next, the web page told me it detected a new thermostat near by. Cool! To verify it had the right one, I needed to go over to my newly installed thermostat and hit the button to confirm that my thermostat was indeed the one attempting a connection. This makes sense - it\'s a simple handshake confirmation of unique IDs. However, when I walked downstairs the thermostat was off. As I approached it I cannot describe to you how amazing the feeling was when the display slowly came alive saying \'Would you like to connect this thermostat to nathan@sparkfun.com?\' - why yes, yes I would. I know it\'s just the IR prox detecting that I\'m near so the display kicked on, but it\'s the polish of these ease-of-use steps that make this a really nicely designed product.

To sum up, Nest is a \$250 thermostat. It may be not for everyone, but for me, it\'s exceptionally easy to use and alleviates the nightmare of programming a thermostat. I can even same some money by turning down the heat when I\'m on the road. Nice job Nest.