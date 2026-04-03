# Creating the player scene

# Creating the player scene
With the project settings in place, we can start working on the
player-controlled character.
The first scene will define thePlayerobject. One of the benefits of
creating a separate Player scene is that we can test it separately, even before
we've created other parts of the game.

## Node structure
To begin, we need to choose a root node for the player object. As a general
rule, a scene's root node should reflect the object's desired functionality -
what the objectis. In the upper-left corner, in the "Scene" tab, click the
"Other Node" button and add anArea2Dnode to the scene.
Note
Godot also provides theCharacterBody2Dnode,
specifically designed for 2D characters, which includes built-in support for some
of the processes explained in this tutorial. In many real world projects, CharacterBody2D
would be a better choice for players and enemies. However, this tutorial focuses on
core concepts that apply to a wider range of nodes and use cases.
When you add theArea2Dnode, Godot will display the followingwarning iconnext to it in the scene tree:
This warning tells us that theArea2Dnode requires a shape to detect collisions or overlaps.
We canignore the warning temporarilybecause we will first set up the player's visuals
(using an animated sprite). Once the visuals are ready, we will add a collision shape as a child
node. This will allow us to accurately size and position the shape based on the sprite's appearance.
WithArea2Dwe can detect objects that overlap or run into the player.
Change the node's name toPlayerby double-clicking on it. Now that we've
set the scene's root node, we can add additional nodes to give it more
functionality.
Before we add any children to thePlayernode, we want to make sure we don't
accidentally move or resize them by clicking on them. Select the node and click
the icon to the right of the lock. Its tooltip says "Groups the selected node
with its children. This causes the parent to be selected when any child
node is clicked in 2D and 3D view."
Save the scene asplayer.tscn. ClickScene > Save, or pressCtrl+Son Windows/Linux orCmd+Son macOS.
Note
For this project, we will be following the Godot naming conventions.
- GDScript: Classes (nodes) use PascalCase, variables and
functions use snake_case, and constants use ALL_CAPS (SeeGDScript style guide).
GDScript: Classes (nodes) use PascalCase, variables and
functions use snake_case, and constants use ALL_CAPS (SeeGDScript style guide).
- C#: Classes, export variables and methods use PascalCase,
private fields use _camelCase, local variables and parameters use
camelCase (SeeC# style guide). Be careful to type
the method names precisely when connecting signals.
C#: Classes, export variables and methods use PascalCase,
private fields use _camelCase, local variables and parameters use
camelCase (SeeC# style guide). Be careful to type
the method names precisely when connecting signals.

## Sprite animation
Click on thePlayernode and add (Ctrl+Aon Windows/Linux orCmd+Aon macOS) a child nodeAnimatedSprite2D. TheAnimatedSprite2Dwill handle the
appearance and animations for our player. Notice that there is a warning symbol
next to the node. AnAnimatedSprite2Drequires aSpriteFramesresource, which is a list of the animations it can
display. Make sureAnimatedSprite2Dis selected and then find theSpriteFramesproperty under
theAnimationsection in the Inspector and click "[empty]" -> "New SpriteFrames":
Click on theSpriteFramesyou just created to open the "SpriteFrames" panel:
On the left is a list of animations. Click thedefaultone and rename it towalk. Then click theAdd Animationbutton to create a second animation
namedup.
Find the player images in the FileSystem dock - they're in theartfolder
you unzipped earlier. Drag the two images for each animation, into theAnimation Framesside of the panel for the corresponding animation:
- playerGrey_walk1andplayerGrey_walk2for thewalkanimation
playerGrey_walk1andplayerGrey_walk2for thewalkanimation
- playerGrey_up1andplayerGrey_up2for theupanimation
playerGrey_up1andplayerGrey_up2for theupanimation
The player images are a bit too large for the game window, so we need to scale
them down. Click on theAnimatedSprite2Dnode and set theScaleproperty
to(0.5,0.5). You can find it in the Inspector under theNode2Dheading.
Finally, add aCollisionShape2Das a child ofPlayer. This will determine the player's "hitbox", or the bounds of its
collision area. For this character, aCapsuleShape2Dnode gives the best
fit, so next to "Shape" in the Inspector, click "[empty]" -> "New
CapsuleShape2D". Using the two size handles, resize the shape to cover the
sprite:
When you're finished, yourPlayerscene should look like this:
Once this is done, the warning on theArea2Dnode will disappear, as it now has
a shape assigned and can interact with other objects.
Make sure to save the scene again after these changes.
In the next part, we'll add a script to the player node to move and animate it.
Then, we'll set up collision detection to know when the player got hit by
something.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.