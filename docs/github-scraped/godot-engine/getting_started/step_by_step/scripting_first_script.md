..
    Intention:

    - Giving a *short* and sweet hands-on intro to GDScript. The page should
      focus on working in the code editor.
    - We assume the reader has programming foundations. If you don't, consider
      taking the course we recommend in the [introduction to Godot page <doc_introduction_learning_programming>].

    Techniques:

    - Creating a sprite.
    - Creating a script.
    - _init() and _process().
    - Moving an object on screen.


# Creating your first script

In this lesson, you will code your first script to make the Godot icon turn in
circles. As we mentioned :ref:`in the introduction
<doc_introduction_learning_programming>`, we assume you have programming
foundations. 

This tutorial is written for GDScript, and the equivalent C# code is included in
another tab of each codeblock for convenience.

> **IMAGE**
>
> **SEEALSO**
> the :ref:`doc_gdscript` section. To learn more about C#,
> head to the :ref:`doc_c_sharp` section.
>
## Project setup

Please [create a new project <doc_creating_and_importing_projects>] to
start with a clean slate. Your project should contain one picture: the Godot
icon, which we often use for prototyping in the community.

> **IMAGE**
>
We need to create a Sprite2D node to display it in the game. In the :ui:`Scene` dock,
click the :button:`Other Node` button.

> **IMAGE**
>
Type "Sprite2D" in the search bar to filter nodes and double-click on Sprite2D
to create the node.

> **IMAGE**
>
Your :ui:`Scene` tab should now only have a Sprite2D node.

> **IMAGE**
>
A Sprite2D node needs a texture to display. In the :ui:`Inspector` on the right, you
can see that the :inspector:`Texture` property says `<empty>`. To display the
Godot icon, click and drag the file `icon.svg` from the FileSystem dock onto the
Texture slot.

> **IMAGE**
>
> **NOTE**
>
> You can create Sprite2D nodes automatically by dragging and dropping images
> on the viewport.
>
Then, click and drag the icon in the viewport to center it in the game view.

> **IMAGE**
>
## Creating a new script

To create and attach a new script to our node, right-click on Sprite2D in the
Scene dock and select :button:`Attach Script`.

> **IMAGE**
>
The :ui:`Attach Node Script` window appears. It allows you to select the script's
language and file path, among other options.

Change the :ui:`Template` field from `Node: Default` to `Object: Empty` to
start with a clean file. Leave the other options set to their default values and
click the :button:`Create` button to create the script.

> **IMAGE**
>
> **NOTE**
>
> C# script names need to match their class name. In this case, you should name the
> file ``MySprite2D.cs``.
>
The :ui:`Script` workspace should appear with your new `sprite_2d.gd` file open and
the following line of code:

> **TABS**

    extends Sprite2D


    using Godot;
    using System;
    
    public partial class MySprite2D : Sprite2D
## {

Every GDScript file is implicitly a class. The `extends` keyword defines the
class this script inherits or extends. In this case, it's `Sprite2D`, meaning
our script will get access to all the properties and functions of the Sprite2D
node, including classes it extends, like `Node2D`, `CanvasItem`, and
`Node`.

> **NOTE**
> class will implicitly extend :ref:`RefCounted <class_RefCounted>`, which
> Godot uses to manage your application's memory.
>
Inherited properties include the ones you can see in the :ui:`Inspector` dock, like
our node's `texture`.

> **NOTE**
>
> By default, the :ui:`Inspector` displays a node's properties in "Title Case", with
> capitalized words separated by a space. In GDScript code, these properties
> are in "snake_case", which is lowercase with each word separated by an underscore.
>
> You can hover over any property's name in the :ui:`Inspector` to see a description and
> its identifier in code.
>
## Hello, world!

Our script currently doesn't do anything. Let's make it print the text "Hello,
world!" to the Output bottom panel to get started.

Add the following code to your script:

> **TABS**

    func _init():
        print("Hello, world!")


    public MySprite2D()
    {
        GD.Print("Hello, world!");
    }


Let's break it down. The `func` keyword defines a new function named
`_init`. This is a special name for our class's constructor. The engine calls
`_init()` on every object or node upon creating it in memory, if you define
this function.

> **NOTE**
> that says ``print()`` is necessary for the code to work. If you omit
> it or don't indent a line correctly, the editor will highlight it in
> red and display the following error message: "Indented block expected".
>
Save the scene as `sprite_2d.tscn` if you haven't already, then press :kbd:`F6` (:kbd:`Cmd + R` on macOS)
to run it. Look at the :ui:`Output` bottom panel that expands.
It should display "Hello, world!".

> **IMAGE**
>
Delete the `_init()` function, so you're only left with the line ``extends
Sprite2D``.

## Turning around

It's time to make our node move and rotate. To do so, we're going to add two
member variables to our script: the movement speed in pixels per second and the
angular speed in radians per second. Add the following after the `extends Sprite2D` line.

> **TABS**

    var speed = 400
    var angular_speed = PI


    private int _speed = 400;
    private float _angularSpeed = Mathf.Pi;

Member variables sit near the top of the script, after any "extends" lines,
but before functions. Every node
instance with this script attached to it will have its own copy of the `speed`
and `angular_speed` properties.

> **NOTE**
> but you have built-in functions and properties available if you prefer
> to calculate angles in degrees instead.
>
To move our icon, we need to update its position and rotation every frame in the
game loop. We can use the `_process()` virtual function of the `Node` class.
If you define it in any class that extends the Node class, like Sprite2D, Godot
will call the function every frame and pass it an argument named `delta`, the
time elapsed since the last frame.

> **NOTE**
>
> Games work by rendering many images per second, each called a frame, and
> they do so in a loop. We measure the rate at which a game produces images in
> Frames Per Second (FPS). Most games aim for 60 FPS, although you might find
> figures like 30 FPS on slower mobile devices or 90 to 240 for virtual
> reality games.
>
> The engine and game developers do their best to update the game world and
> render images at a constant time interval, but there are always small
> variations in frame render times. That's why the engine provides us with
> this delta time value, making our motion independent of our framerate.
>
At the bottom of the script, define the function:

> **TABS**

    func _process(delta):
        rotation += angular_speed * delta


    public override void _Process(double delta)
    {
        Rotation += _angularSpeed * (float)delta;
    }

The `func` keyword defines a new function. After it, we have to write the
function's name and arguments it takes in parentheses. A colon ends the
definition, and the indented blocks that follow are the function's content or
instructions.

> **NOTE**
> underscore. By convention, Godot's virtual functions, that is to say,
> built-in functions you can override to communicate with the engine,
> start with an underscore.
>
The line inside the function, `rotation += angular_speed * delta`, increments
our sprite's rotation every frame. Here, `rotation` is a property inherited
from the class `Node2D`, which `Sprite2D` extends. It controls the rotation
of our node and works with radians.

> **TIP**
> macOS) on any built-in property or function like ``position``,
> ``rotation``, or ``_process`` to open the corresponding documentation
> in a new tab.
>
Run the scene to see the Godot icon turn in-place.

> **IMAGE**
>
> **NOTE**
> ``double``. We therefore need to convert it to ``float`` when we apply
> it to the rotation.
>
### Moving forward

Let's now make the node move. Add the following two lines inside of the `_process()`
function, ensuring the new lines are indented the same way as the `rotation += angular_speed * delta` line before
them.

> **TABS**

    var velocity = Vector2.UP.rotated(rotation) * speed

    position += velocity * delta


    var velocity = Vector2.Up.Rotated(Rotation) * _speed;

    Position += velocity * (float)delta;

As we already saw, the `var` keyword defines a new variable. If you put it at
the top of the script, it defines a property of the class. Inside a function, it
defines a local variable: it only exists within the function's scope.

We define a local variable named `velocity`, a 2D vector representing both a
direction and a speed. To make the node move forward, we start from the Vector2
class's constant `Vector2.UP`, a vector pointing up, and rotate it by calling the
Vector2 method `rotated()`. This expression, `Vector2.UP.rotated(rotation)`,
is a vector pointing forward relative to our icon. Multiplied by our `speed`
property, it gives us a velocity we can use to move the node forward.

We add `velocity * delta` to the node's `position` to move it. The position
itself is of type [Vector2 <class_Vector2>], a built-in type in Godot
representing a 2D vector.

Run the scene to see the Godot head run in circles.

> **IMAGE**
>
> **NOTE**
> walls or the floor. In :ref:`doc_your_first_2d_game`, you will learn
> another approach to moving objects while detecting collisions.
>
Our node currently moves by itself. In the next part,
[doc_scripting_player_input], we'll use player input to control it.

## Complete script

Here is the complete `sprite_2d.gd` file for reference.

> **TABS**

    extends Sprite2D

    var speed = 400
    var angular_speed = PI


    func _process(delta):
        rotation += angular_speed * delta

        var velocity = Vector2.UP.rotated(rotation) * speed

        position += velocity * delta


    using Godot;
    using System;
    
    public partial class MySprite2D : Sprite2D
    {
        private int _speed = 400;
        private float _angularSpeed = Mathf.Pi;

        public override void _Process(double delta)
        {
            Rotation += _angularSpeed * (float)delta;
            var velocity = Vector2.Up.Rotated(Rotation) * _speed;

            Position += velocity * (float)delta;
## }
