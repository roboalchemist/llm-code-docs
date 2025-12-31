# Source: https://learn.sparkfun.com/tutorials/creating-a-humidor-control-box

## Overview

In this tutorial, I am going to go through the process of how the SparkFun humidor was designed and built. A humidor is any kind of box or room with constant humidity, used to store cigars, cigarettes, pipe tobacco, or in this case sensors. I\'ll be covering designing a 3D software model and fabricating it using a CNC router.

[![alt text](//cdn.sparkfun.com/r/600-600/assets/d/f/6/4/2/513f7015ce395f2848000000.JPG)](//cdn.sparkfun.com/assets/d/f/6/4/2/513f7015ce395f2848000000.JPG)

*The finished project*

### Requirements

I realize the following list includes some items that are very expensive and probably not too common in everyone's home/shop. I still wanted to show their use for someone who may not be familiar with these tools. Here is what I will be using:

- Creo Parametric 2.0 (formerly Pro Engineer, FREE for educational purposes - Software)
- Visual Mill 5 (Software)
- Mach 2 CNC (Software)
- K2 CNC Machine (Hardware)

### Background

If you don't already know, a CNC router is a computer controlled router capable of cutting out very complex shapes. CNC stands for [Computer Numerical Control](http://en.wikipedia.org/wiki/Numerical_control). The CNC machine is connected to a computer and is given very precise three dimensional coordinates to which the machine should move. Using a combination of motors and encoders, the machine is able to cut out nearly anything you can draw. There is lots to cover, so lets get started.

## 3D Design 

Our Production department came to me needing a humidor built. They needed a better system to re-humidify a select few of our boards that need it after coming out of the reflow oven.

I am a very visual person. I like to see exactly what I have designed and how it fits together before I start making it. By doing this, it is easy to see where my mistakes are and correct them.

For this project, I designed both the humidor and the control box for it. The control box allows our Production team to select which board they are placing in the humidor, iit will keep track of the time it has been in there. It also makes sure the humidity stays at the required percentage. I'm not going to cover much of the humidor in this tutorial, however. I laser cut acrylic and epoxied it together in the shape of a box. When it was dry, I added some weather strip to the front door to seal it and put caulk in all the joints to ensure it was air tight. Not too much going on there!

The control box was really fun to make. I decided to cut 'teeth' in all of the edges so it would fit together like a 3D puzzle. Here at Sparkfun, we use Creo Parametric 2.0 for our 3D modeling. Our [Arduino and breadboard holder](https://www.sparkfun.com/products/11235) was designed with this along with all of our [retail clamshell packaging.](https://www.sparkfun.com/products/9890) I learned this program in High School, and of all the modeling software I have used along the way, it is my favorite. Before I begin, I want to tell you that this tutorial only scratches the surface of the feature in Creo. I'm only going to cover a few main points and features, there is certainly more than one way to do all of this. Let's start designing!

\(1\) In the picture below, we are going to start drawing the top panel for the control box. The area with the labels 'FRONT', 'TOP', and 'RIGHT' is our workspace. We want to choose one that accurately describes the surface that we want to draw. Since this panel will go on the top side of the box, I am going to select the 'TOP' plane. Probably the most used feature is the Extrude command. This allows us to create material (or remove it) in the shape we want. So to recap, we choose the 'TOP' plane and click Extrude.

[![Choose Plane](//cdn.sparkfun.com/r/600-600/assets/3/3/c/b/1/513f6a31ce395f1144000000.jpg)](//cdn.sparkfun.com/assets/3/3/c/b/1/513f6a31ce395f1144000000.jpg)

*(1) Choose Plane*

\(2\) This brings us to the Sketcher. The Sketcher is where we draw the features that we want. Using the Rectangle command, I will draw a rectangle. I decided that I wanted the panel to be 8 inches wide and 6 inches tall. The dimensions are added automatically when I draw the rectangle. All I have to do it change them to what I want. Once they are correct, I click OK.

[![Draw!](//cdn.sparkfun.com/r/600-600/assets/5/9/6/1/a/513f6a31ce395f1c44000000.jpg)](//cdn.sparkfun.com/assets/5/9/6/1/a/513f6a31ce395f1c44000000.jpg)

*(2) Draw Rectangle*

\(3\) If the computer accepts the shape, it will add depth to it. This is where we move from a 2D drawing to a 3D model. Since I am cutting this out of plywood that is 0.35" thick, I will enter that in the box shown and click OK.

[![Time for 3D](//cdn.sparkfun.com/r/600-600/assets/8/d/0/8/3/513f6a31ce395f0948000000.jpg)](//cdn.sparkfun.com/assets/8/d/0/8/3/513f6a31ce395f0948000000.jpg)

*(3) Time to go 3D!*

\(4\) Next, I want to cut a hole for the LCD and a few buttons. I'll select the surface that I want to create the 2D drawing on. In this case, I'll choose the top of the panel. Once again, I'll click the Extrude command for this. Remember: Extrude can add or remove material.

[![Cut LCD hole](//cdn.sparkfun.com/r/600-600/assets/c/7/0/1/b/513f6a31ce395f6244000000.jpg)](//cdn.sparkfun.com/assets/c/7/0/1/b/513f6a31ce395f6244000000.jpg)

*(4) Select the surface to cut through*

\(5\) After measuring the size of the LCD screen, I'll use the Rectangle command to draw the hole where I want it. Now I want to add holes for the buttons. I want the buttons on the right side of the screen, and I want them to be lined up perfectly. I'm going to use what's called a Centerline for this. You can think of a Centerline as a reference or helper line. In this picture, they are the purple dashed lines. When it comes time to create the 3D model, the computer will ignore these lines, so it doesn't matter how many you have or where they are placed. Creo will create the center line where I click and it will 'snap' to a vertical position, ensuring the buttons are lined up perfectly with the panel.

[![Sketch cutouts](//cdn.sparkfun.com/r/600-600/assets/0/a/5/f/8/513f6a31ce395fab44000000.jpg)](//cdn.sparkfun.com/assets/0/a/5/f/8/513f6a31ce395fab44000000.jpg)

*(5) Drawing the cut-outs*

\(6\) By default, the Extrude command adds material. Since we want to do a cut out, we use the 'Change Direction' button on the left to tell the computer to cut away from where we drew the hole and also the 'Remove Material' button on the right to tell it to remove material. The result is what we want, a hole for the LCD and holes for buttons. I'll repeat this process for the other buttons.

[![Extrude a cut](//cdn.sparkfun.com/r/600-600/assets/3/1/8/5/d/513f6a32ce395fcb45000000.jpg)](//cdn.sparkfun.com/assets/3/1/8/5/d/513f6a32ce395fcb45000000.jpg)

*(6) Not what we want*

[![Now it is cut](//cdn.sparkfun.com/r/600-600/assets/5/4/6/4/e/513f6a32ce395f3348000000.jpg)](//cdn.sparkfun.com/assets/5/4/6/4/e/513f6a32ce395f3348000000.jpg)

*(6) After a few changes to the settings, it is correct*

\(7\) Now it is time to create the 'teeth' for the edges. Like before, I select the top surface of the panel and click Extrude. In the Sketcher, I'll draw a small rectangle that represents one of the teeth I want to cut out. The red color of the dimension indicates that I have locked the dimension. This prevents me or the computer from altering that particular dimension. For now, I am only going to draw one. I'll show you why in the next step.

[![Create one tooth](//cdn.sparkfun.com/r/600-600/assets/4/6/d/6/b/513f6a31ce395f3e48000000.jpg)](//cdn.sparkfun.com/assets/4/6/d/6/b/513f6a31ce395f3e48000000.jpg)

*(7) We only need to draw one tooth*

\(8\) Now drawing 7 cutouts would not have taken too much time, but what if we needed to create 1000 teeth around a circular gear? That would take forever. To save time I will use the 'Pattern' command. This allows me to duplicate a feature that I had previously drawn. If you look at the red arrows in the picture below, from left to right:

- Direction -- tells the computer that you want to pattern in a straight line, as opposed to circular.
- 1 Plane -- if you look very carefully, the right side of the panel has an orange line, that is the direction I choose to move.
- 7 -- the number of copies I want to make.
- 1.0625 -- the spacing between each copy. The black dots represent where the computer will add the feature.

[![Pattern](//cdn.sparkfun.com/r/600-600/assets/d/e/6/4/7/513f6a32ce395f3848000000.jpg)](//cdn.sparkfun.com/assets/d/e/6/4/7/513f6a32ce395f3848000000.jpg)

*(8) Setting up the pattern*

Voilà! We have created the top 8 teeth for our box!

[![Confirming the pattern](//cdn.sparkfun.com/r/600-600/assets/5/b/4/c/1/513f6a32ce395f2b46000000.jpg)](//cdn.sparkfun.com/assets/5/b/4/c/1/513f6a32ce395f2b46000000.jpg)

*(8) The pattern looks correct*

\(9\) Since the top and bottom of the panel both use the same pattern, we can use the 'Mirror' command to do this easily. I'll turn on the planes again and select the 'FRONT' plane because it runs through the center of the panel. Now the computer will take that single tooth that we drew and patterned and copy it to the bottom of the panel.

[![Mirror the pattern](//cdn.sparkfun.com/r/600-600/assets/9/5/2/4/4/513f6a32ce395fe447000000.jpg)](//cdn.sparkfun.com/assets/9/5/2/4/4/513f6a32ce395fe447000000.jpg)

*(9) The Mirror command can save a great amount of time*

\(10\) I'll repeat these last few steps for the teeth on the left and right side of the panel. In the end, we have one part of the box done!

[![Repeat process](//cdn.sparkfun.com/r/600-600/assets/a/4/d/2/1/513f6a32ce395fff47000001.jpg)](//cdn.sparkfun.com/assets/a/4/d/2/1/513f6a32ce395fff47000001.jpg)

*(10) The finished face plate of the controller*

## 3D Assembly 

\(1\) Using the same techniques as above, I went ahead and made the side walls and bottom piece for the box. Now that we have 6 individual parts of the box, let's put them together! In a new file, I'll import the control panel using the 'Assemble' command.

[![Time to assemble](//cdn.sparkfun.com/r/600-600/assets/7/b/d/1/8/513f6a32ce395f1248000000.jpg)](//cdn.sparkfun.com/assets/7/b/d/1/8/513f6a32ce395f1248000000.jpg)

*(1)Assembling the box*

\(2\) Next, I will tell the computer that I do not want this piece to move. I will be building all of the other parts around it, so it is nice to have it stay still. By right clicking on the part in the Model Tree, I can choose Fix Location. Mine is already fixed so the option to UnFix is displayed.

[![Fix location](//cdn.sparkfun.com/r/600-600/assets/0/9/6/a/a/513f6a32ce395ff658000000.jpg)](//cdn.sparkfun.com/assets/0/9/6/a/a/513f6a32ce395ff658000000.jpg)

*(2) Fixing the location prevents it from moving*

\(3\) Next, I will add another piece of the box. Using the Assemble command from before, I'll bring in the part I want. If you look at the picture, the word 'Coincidence' appears several times. This is more or less the way to tell the computer to 'make these two surfaces touch or line up.' Simply put, I choose what surfaces should be lined up, and the computer will 'glue' them together.

[![Add more parts](//cdn.sparkfun.com/r/600-600/assets/9/1/f/9/e/513f6a32ce395ff347000000.jpg)](//cdn.sparkfun.com/assets/9/1/f/9/e/513f6a32ce395ff347000000.jpg)

*(3)Adding more parts to the assembly*

\(4\) Repeating the process four more times gives us a completed box! Now we can inspect all the sides to see if we made any mistakes in the length or position of any features.

[![Complete assembly](//cdn.sparkfun.com/r/600-600/assets/0/3/0/2/4/513f6a32ce395fe147000000.jpg)](//cdn.sparkfun.com/assets/0/3/0/2/4/513f6a32ce395fe147000000.jpg)

*(4) The assembled box*

\(5\) Let's go ahead and add the LCD screen and buttons just for fun.

[![Add electronics](//cdn.sparkfun.com/r/600-600/assets/5/0/4/0/3/513f6a32ce395fe544000000.jpg)](//cdn.sparkfun.com/assets/5/0/4/0/3/513f6a32ce395fe544000000.jpg)

*(5) Added the LCD and buttons*

\(6\) We can now use the 'Exploded View' command to see the box as if it were taken apart.

[![Exploded viewt](//cdn.sparkfun.com/r/600-600/assets/6/a/b/e/a/513f6a32ce395f4648000000.jpg)](//cdn.sparkfun.com/assets/6/a/b/e/a/513f6a32ce395f4648000000.jpg)

*(6)The exploded view with temporarily split apart the assembly*

\(7\) Now that I box is designed, assembled, and inspected, we can get the files ready to cut out on the CNC router. In Creo, we want to create a new Drawing.

[![Create drawing](//cdn.sparkfun.com/r/600-600/assets/7/7/9/d/d/513f6a32ce395fbe44000000.jpg)](//cdn.sparkfun.com/assets/7/7/9/d/d/513f6a32ce395fbe44000000.jpg)

*(7) Creating a new drawing*

\(8\) Since we only care about the 2D feature of each part at this point, the parts can lay flat on the screen.

[![2D now](//cdn.sparkfun.com/r/600-600/assets/8/8/6/7/4/513f6a33ce395fd347000000.jpg)](//cdn.sparkfun.com/assets/8/8/6/7/4/513f6a33ce395fd347000000.jpg)

*(8) The 3D model is no longer needed*

\(9\) After adding all views we have the entire box laid out in front of us.

[![All parts](//cdn.sparkfun.com/r/600-600/assets/b/a/4/7/e/513f6a32ce395fdb47000000.jpg)](//cdn.sparkfun.com/assets/b/a/4/7/e/513f6a32ce395fdb47000000.jpg)

*(9) Each part in a 2D view*

\(10\) Lastly, we want to export this drawing as a .dxf file. This type of file is supported in many, many different types of programs so it is a good choice to use.

[![Export](//cdn.sparkfun.com/r/600-600/assets/f/a/5/d/b/513f6a32ce395fe847000000.jpg)](//cdn.sparkfun.com/assets/f/a/5/d/b/513f6a32ce395fe847000000.jpg)

*(10) Exporting the drawing for later use*

## Creating Tool Paths

I'm using a program called Visual Mill to create the tool paths for the box. A Tool Path is the area that the CNC machine will follow to cut out our box.

\(1\) First I will open the .dxf file that we saved. Then we need to choose the size of the endmill we are going to use.

[![Open file, choose bit](//cdn.sparkfun.com/r/600-600/assets/f/d/a/1/e/513f6d99ce395fbd47000000.jpg)](//cdn.sparkfun.com/assets/f/d/a/1/e/513f6d99ce395fbd47000000.jpg)

*(1) Open the file, choose the bit*

\(2\) I am going to use a 1/8" endmill. We can enter in the specific feature of our tool if we need to. Everything looks good so I'll choose OK.

[![Choose bit](//cdn.sparkfun.com/r/600-600/assets/6/a/3/c/8/513f6d99ce395fc747000001.jpg)](//cdn.sparkfun.com/assets/6/a/3/c/8/513f6d99ce395fc747000001.jpg)

*(2) Select the ⅛" bit*

\(3\) Next, I'm going to select everything that we want to cut out. Selected lines turn yellow so the user can tell they are selected. We want to do a 'Profile' type cut. A profile cut will cut around the inside or outside of the part and leave the center intact.

[![Select lines](//cdn.sparkfun.com/r/600-600/assets/8/4/5/1/2/513f6d99ce395f1244000003.jpg)](//cdn.sparkfun.com/assets/8/4/5/1/2/513f6d99ce395f1244000003.jpg)

*(3) Select lines, choose cut type*

\(4\) Next we have to define a few options. We set the 'Tolerance' to .001 inches for good accuracy. 'Cut Direction' tells the computer to cut either clockwise or counter clockwise. For wood, a 'Conventional' cut works well. This will make the cutting edge on the tool spin into the material (think of a car tire spinning on pavement as the car slowly creeps forward) and keep the wood from peeling off instead of being cut. And lastly 'Cut Start Side' tells the computer to either cut on the inside or outside of the selected lines. We want to cut on the outside.

[![alt text](//cdn.sparkfun.com/r/600-600/assets/e/d/d/8/2/513f6d9ace395f4848000000.jpg)](//cdn.sparkfun.com/assets/e/d/d/8/2/513f6d9ace395f4848000000.jpg)

*(4) Setting cut parameters*

\(5\) On the next tab, we define how deep to cut. This is why earlier in the tutorial I said we only care about the 2D features of the parts. 'Total Cut Depth' tells the computer; yep you guessed it, how deep we want to cut. Since the wood is 0.35" thick, let's go 0.36" to be sure. The 'Rough Depth' and 'Finish Depth' are ways to allow the user to very precisely control how much the CNC cuts off at a given time. Since we are cutting wood and not metal, we don't need to worry too much about this. I have told the machine to cut in depths of 0.09". That means it will take 4 passes to cut through.

[![Parameters](//cdn.sparkfun.com/r/600-600/assets/1/f/c/7/5/513f6d99ce395f4548000000.jpg)](//cdn.sparkfun.com/assets/1/f/c/7/5/513f6d99ce395f4548000000.jpg)

*(5) Setting the cut depth and step distance*

\(6\) Lastly for this options box are the approaches and engage motions. Because the bit I have is a center cutting bit, I can do what is called plunge cutting. Some bits can drill straight down (plunge) through the material, while others cannot. This is because the teeth of some cutters do not extend all the way to the center of the bit. However, these cutters can cut downwards at an angle of 45 degrees or so (called ramp cutting). We can set all of these values to zero. This will make the mill move into position and come straight down (plunge). Think of it like a bulldozer cutting into the ground (ramp cutting) versus an excavator digging in one spot (plunge cutting). The 'Cut Transfer' tells the CNC how high to lift up when moving from one spot to another. Since the plywood I'm using is somewhat warped, I'll use 0.25" to be sure the machine does not accidently cut into a high spot in the wood when it is moving.

[![Motions](//cdn.sparkfun.com/r/600-600/assets/b/f/4/c/7/513f6d9ace395fc947000000.jpg)](//cdn.sparkfun.com/assets/b/f/4/c/7/513f6d9ace395fc947000000.jpg)

*(6) Telling the CNC how we want it to move*

\(7\) Here we can see the tool path that has been created. If you look at the light blue colored lines you can see exactly where the endmill will be cutting. Hmm...wait a minute something doesn't look right. The tool paths are on the inside of the part. If we run this, the panel will be too small!

[![Incorrect tool path](//cdn.sparkfun.com/r/600-600/assets/c/7/d/f/6/513f6d9ace395f2148000001.jpg)](//cdn.sparkfun.com/assets/c/7/d/f/6/513f6d9ace395f2148000001.jpg)

*(7) Incorrect tool path*

\(8\) Easy fix! I'll just edit the tool path and change the 'Cut Start Side' from Left to Right. This will generate the tool path on the correct side.

[![Change the starting side](//cdn.sparkfun.com/r/600-600/assets/9/8/6/2/a/513f6d9ace395f3145000000.jpg)](//cdn.sparkfun.com/assets/9/8/6/2/a/513f6d9ace395f3145000000.jpg)

*(8) Change the start side to correct the problem*

\(9\) Well that fixed the tool path for the panels. The cut marks are on the outside of the parts, which is what we want, but look at the LCD hole and button holes. Now they are on the outside. If we run the CNC now, they will be too big. So I guess we can\'t select everything at the same time. I'll do one tool path for the outlines and one for the LCD + buttons.

[![Must create 2 different tool paths](//cdn.sparkfun.com/r/600-600/assets/6/8/5/3/e/513f6d9ace395f1044000000.jpg)](//cdn.sparkfun.com/assets/6/8/5/3/e/513f6d9ace395f1044000000.jpg)

*(9) We'll need 2 separate paths for this*

\(10\) There! Now everything looks as it should. The tool paths are on the outside of the exterior and inside the interior of the parts we want to cut out. Those green lines show where the machine will raise the bit and move to a new area.

[![The correct tool path](//cdn.sparkfun.com/r/600-600/assets/c/1/c/f/7/513f6d9ace395f0446000000.jpg)](//cdn.sparkfun.com/assets/c/1/c/f/7/513f6d9ace395f0446000000.jpg)

*(10) Everything looks correct now*

\(11\) Now we can export the tool paths as G code. G code is a format in which the computer tells the CNC where to move, one point at a time. The CNC moves in a straight line from one point to the next. As you can imagine for a circle, there are lots and lots of coordinates. The CNC controller program we use is called Mach2 so I'll tell it to export for that.

[![Export tool paths](//cdn.sparkfun.com/r/600-600/assets/1/e/6/6/d/513f6d9ace395f0244000002.jpg)](//cdn.sparkfun.com/assets/1/e/6/6/d/513f6d9ace395f0244000002.jpg)

*(11) Exporting the tool paths*

\(12\) We're almost there now! This is Mach2 (see below), the program that reads the G code and sends the pulse commands to the CNC machine. I'll explain the areas that I highlighted.

G CODE -- This is the G code that is loaded into the program. N10 stands for Line Number 1. The G command tells the computer that we want to move the cutting bit to a certain location without cutting anything. A person could write an entire tool path in a text document if they wanted. It might take awhile though. Check out the wiki page for [G code](http://en.wikipedia.org/wiki/G-code) for a full list of all the codes!

POSITION -- This is the current position of the center of the cutting bit as reported by the encoders on the CNC motors. X, Y, and Z are used here (we have a 3 axis CNC) but the 4th is not used.

USER SETTINGS -- The Jog setting sets the speed limit for movement. If I want to manually move the CNC head to a certain spot, I can use the keyboard. If I tap an arrow key once, the CNC head will move a distance set in the Step box, in this case 0.001". If I hold shift and press an arrow key, the CNC will move rapidly for as long as I hold the key. The 'Slow Jog Rate' limits the speed that the CNC can travel during the rapid movement.

Units/Min -- This shows how fast the mill is traveling. When I cut wood, it will usually be around 15-30 inches per minute.

SPEED CONTROL -- I didn't show you this in Visual Mill, mostly because I hardly ever adjust it, but there are several speed setting for various things. We can set the speed at which material is cut, the speed at which the cutting bit goes up and down, the speed at which the CNC makes non-cutting movements, and other. The Speed Control lets us manually speed up or slow down all of these settings at the same time.

VISUALIZATION -- This area shows 3 things. The lines in blue are what the mill is going to cut out, the green lines show where the mill has already cut (we haven\'t cut anything yet), and the yellow crosshairs show where the center of the endmill is at.

Some other features here are not available on our CNC. For example the Mist and Flood buttons control whether or not coolant is being sprayed on our part. We don't have coolant on our CNC, so we don't use this feature.

[![Mach2](https://cdn.sparkfun.com/r/600-600/assets/2/7/b/1/5/513f6d9ace395f8648000000.jpg)](https://cdn.sparkfun.com/assets/2/7/b/1/5/513f6d9ace395f8648000000.jpg)

*(12) The CNC control layout*

## Time to Cut

\(1\) Once the machine is set up, it is time to get the wood into place. I\'ll be using some run-of-the-mill 3/8\" plywood. Because there will be large amounts of force pushing into the wood from the endmill, it is very important to secure the wood to the table. Our CNC has a grid pattern of threaded holes that allow pieces of any size and shape (okay, almost any size and shape) to be securely mounted to the bed.

[![Secure the wood](//cdn.sparkfun.com/r/600-600/assets/d/c/b/0/d/513f7015ce395f3848000001.JPG)](//cdn.sparkfun.com/assets/d/c/b/0/d/513f7015ce395f3848000001.JPG)

*(1) It is very important that the piece does not move*

\(2\) Next we need to tell the machine where the wood is located. Since we could have placed the wood at any random location on the bed, we need to make sure the machine knows where to start cutting. We do this by placing the center of the bit over the bottom left corner of the plywood and clicking the \'Zero X\' and \'Zero Y\' buttons shown in the POSITION box I labeled in the previous section. Because our plywood is larger than it needs to be, our positioning does not need to be exact. Anywhere near the bottom corner will be just fine.

[![Setting the home](//cdn.sparkfun.com/r/600-600/assets/2/6/a/6/c/513f7015ce395f2b48000000.JPG)](//cdn.sparkfun.com/assets/2/6/a/6/c/513f7015ce395f2b48000000.JPG)

*(2) Setting the (0,0) position*

\(3\) Once that is all set, we can click the \'Cycle Start\' button and watch in wonder as the parts are cut out. You will have to talk my word for it since you only get to see a picture. But trust me, it is really fun to watch!

[![Running the CNC](//cdn.sparkfun.com/r/600-600/assets/8/1/e/8/6/513f7015ce395f3348000001.JPG)](//cdn.sparkfun.com/assets/8/1/e/8/6/513f7015ce395f3348000001.JPG)

*(3) One piece of the box*

\(4\) Once the box was cut out, I stained it and fit the pieces together. I added all of the electronic components and glued them in.

[![Finished](//cdn.sparkfun.com/r/600-600/assets/c/1/6/9/6/513f8767ce395f1644000000.JPG)](//cdn.sparkfun.com/assets/c/1/6/9/6/513f8767ce395f1644000000.JPG)

*(4) The finished box*