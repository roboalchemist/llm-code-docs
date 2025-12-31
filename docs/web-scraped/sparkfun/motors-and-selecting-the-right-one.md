# Source: https://learn.sparkfun.com/tutorials/motors-and-selecting-the-right-one

## Introduction

At any given moment, you are near at least one or two types of motors. From the [vibration motor in your cell phone](http://en.wikipedia.org/wiki/Vibrating_alert), to the fans and CD drive in your favorite [gaming system](http://en.wikipedia.org/wiki/Dreamcast), motors are all around us. Motors provide a way for our devices to interact with us and the environment. With a myriad of applications for motors, the design and operation of them can vary.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/4/c/6/4/7/52a22672757b7f511d8b456b.jpg)](https://cdn.sparkfun.com/assets/4/c/6/4/7/52a22672757b7f511d8b456b.jpg)

### What You Will Learn

In this tutorial we\'ll cover some of these basic motor types and uses:

- DC Brush Motors
- Brushless Motors
- Stepper Motors
- Linear Motors

### Recommended Reading

- [What is Electricity](https://learn.sparkfun.com/tutorials/what-is-electricity)
- [What is a Circuit?](https://learn.sparkfun.com/tutorials/what-is-a-circuit)
- [Voltage, Current, Resistance, and Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

## What Makes A Motor Move? 

The most vague and simple answer is magnetism! Ok, now let\'s take this simple force and turn it into a super car!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/3/2/0/0/6/52656c76757b7f347c8b4572.png)](https://cdn.sparkfun.com/assets/3/2/0/0/6/52656c76757b7f347c8b4572.png)

To keep things simple, we will need to look at some concepts through the lens of the [thought experiment](http://en.wikipedia.org/wiki/Thought_experiment). Some liberties will be taken, but if you want to get down and dirty with the details, you can consult [Dr. Griffiths](http://www.amazon.com/Introduction-Electrodynamics-Edition-David-Griffiths/dp/013805326X). For our thought experiment, we are going to state that a magnetic field is produced by a moving electron *i.e. current*. While this creates a classical model for us to use, things break down when we reach the atomic level. To understand the atomic level of magnetism more, Griffiths explains that in another [book](http://www.amazon.com/Introduction-Quantum-Mechanics-2nd-Edition/dp/0131118927)\...

### Electromagnetism

To create a magnet or magnetic field, we are going to have to look at how they are generated. The relationship between current and magnetics field behave according to the [right-hand rule](http://en.wikipedia.org/wiki/Right-hand_rule). As current passes through a wire, a magnetic field forms around the wire in the direction of your fingers as they wrap around it. This is a simplification of [Ampère\'s force law](http://en.wikipedia.org/wiki/Amp%C3%A8re%27s_force_law) as it acts on a current carrying wire. Now, if you place that same wire in a pre-existing magnetic field, you can generate a force. This force is referred to as the [Lorentz force](http://en.wikipedia.org/wiki/Lorentz_force#Force_on_a_current-carrying_wire).

[![Right Hand Rule](https://cdn.sparkfun.com/assets/6/0/a/1/e/5229074f757b7fbd568b456a.gif "The Fonz approves!")](https://cdn.sparkfun.com/assets/6/0/a/1/e/5229074f757b7fbd568b456a.gif)

*The right-hand rule shows the direction of the magnetic field in relation to the current path.*

*(Credit: [HyperPhysics](http://hyperphysics.phy-astr.gsu.edu/hbase/hframe.html))*

If the current is increased, the strength of the magnetic field is strengthened. Though, to do something useful with the field, it would take incredible amounts of current. Furthermore, the wire delivering the current would be carrying the same magnetic strength, thus creating uncontrolled fields. By bending the wire into a loop, a directed and concentrated field can be created.

[![Loop of Wire Creates a Magnet](https://cdn.sparkfun.com/assets/c/f/9/3/7/52290a54757b7f4f568b456b.gif)](https://cdn.sparkfun.com/assets/c/f/9/3/7/52290a54757b7f4f568b456b.gif)

*The field has not changed. By bending the wire into a loop, field directions are simply aligned.*

*(Credit: [HyperPhysics](http://hyperphysics.phy-astr.gsu.edu/hbase/hframe.html))*

### Electromagnets

By looping wire and passing a current, an electromagnet is created. If one loop of wire can concentrate the field, what can you do with more? How about a few **hundred** more! The more loops you add to the circuit, the stronger the field becomes for a given current. If that\'s the case, why don\'t we see **thousands \*\*, if not \*\*millions**, of windings in motors and electromagnets? Well, the longer the wire the higher resistance it has. [Ohm\'s law (V = I\*R)](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law) says to maintain the same current as resistance increases, voltage must increase. In some cases it makes sense to use higher voltages; in other cases some use larger wire with less resistance. Using larger wire is more costly and is generally more difficult to work with. These are factors that have to be weighed when designing a motor.

[![alt text](https://cdn.sparkfun.com/assets/c/b/f/b/3/5229074f757b7f66568b456e.gif)](https://cdn.sparkfun.com/assets/c/b/f/b/3/5229074f757b7f66568b456e.gif)

*An energized electromagnet producing a magnetic field.*

*(Credit: [HyperPhysics](http://hyperphysics.phy-astr.gsu.edu/hbase/hframe.html))*

#### Experiment Time

To create your own electromagnet, simply find a bolt (or other round steel object), some [magnet wire](https://www.sparkfun.com/products/11363) (30-22 gauge works fine), and a [battery](https://www.sparkfun.com/products/10218).

*Note: Lithium Batteries are **NOT** recomended for this experiment.*

[![alt text](https://cdn.sparkfun.com/r/500-500/assets/1/a/3/4/6/522a2758757b7f7e018b4567.JPG)](https://cdn.sparkfun.com/assets/1/a/3/4/6/522a2758757b7f7e018b4567.JPG)

Wrap between 75-100 turns of wire around the steel. Using a steel center further concentrates the magnetic field, increasing its effective strength. We will go over why this is happens in the next section.

[![alt text](https://cdn.sparkfun.com/r/500-500/assets/d/9/c/e/2/522a2758757b7f5a568b456c.JPG)](https://cdn.sparkfun.com/assets/d/9/c/e/2/522a2758757b7f5a568b456c.JPG)

[![alt text](https://cdn.sparkfun.com/r/500-500/assets/f/a/7/9/6/522a4e27757b7fac118b4567.JPG)](https://cdn.sparkfun.com/assets/f/a/7/9/6/522a4e27757b7fac118b4567.JPG)

*A bit of heat shrink or tape can help keep the coils on the steel center.*

Now, using sand paper, remove the insulation from the ends of the wires, and connect each wire to each terminal of the battery. Congratulations! You have built the first component of a motor! To test the strength of your electromagnet, try to pick up paper clips or other small steel objects.

[![alt text](https://cdn.sparkfun.com/r/500-500/assets/3/a/6/9/f/522a4ab9757b7f98118b4568.jpg)](https://cdn.sparkfun.com/assets/3/a/6/9/f/522a4ab9757b7f98118b4568.jpg)

*It\'s not magic, it\'s SCIENCE!!!*

## Ferromagnetism

Looking back to the beginning of our thought experiment, magnetic fields may only be produced by a current. Taking the definition of current as a flow of electrons, electrons orbiting an atom should create a current and thus a magnetic field! If every atom has electrons is everything magnetic? YES! All matter, [including frogs](https://www.youtube.com/watch?v=2VlWonYfN3A), can express magnetic properties when given enough energy. But not all magnetism is created equally. The reason I can pick up screws with a refriderator magnent and not a frog is the difference between [ferromagnetism](http://en.wikipedia.org/wiki/Ferromagnetism) and [paramagnetism](http://en.wikipedia.org/wiki/Paramagnetism). The way to differentiate the two (and a few more types) is through the study of [quantum mechanics](http://en.wikipedia.org/wiki/Quantum_mechanics).

Ferromagnetism will be our focus, since it is the strongest phenomenon and is what we have the most experience with. Further, to relieve us from having to understanding this at the quantum level, we are going to accept that atoms of ferromagnetic materials *tend* to align their magnetic fields with their neighbors. Though they tend to align, inconsistencies in material and other factors like crystaline structure create [magnetic domains](http://en.wikipedia.org/wiki/Magnetic_domain).

[![alt text](https://cdn.sparkfun.com/assets/5/f/f/8/4/523a3271757b7fe91e8b4568.png)](https://cdn.sparkfun.com/assets/5/f/f/8/4/523a3271757b7fe91e8b4568.png)

When magnetic domains are aligned in a random order, neighboring fields cancel each other out resulting in a non-magnetized material. Once in the presence of an strong external field it is possible to re-align these domains. By aligning these domains, the overall field strengthens, creating a magnet!

[![alt text](https://cdn.sparkfun.com/assets/f/6/0/5/b/523a1855757b7f696f8b4567.gif)](https://cdn.sparkfun.com/assets/f/6/0/5/b/523a1855757b7f696f8b4567.gif)

*(Credit: [HyperPhysics](http://hyperphysics.phy-astr.gsu.edu/hbase/hframe.html))*

This re-alignment can be permanent depending on the strength of the field. This is great because we\'ll need these in the next section.

## Permanent Magnets

Permanent magnets behave in the same way as electromagnets. The only difference is, well, they are permanent.

[![alt text](https://cdn.sparkfun.com/assets/e/2/e/4/b/5229074f757b7f4b568b456d.gif)](https://cdn.sparkfun.com/assets/e/2/e/4/b/5229074f757b7f4b568b456d.gif)

In all drawings, arrows will be pointing away from the north pole and towards the south pole. Another convention is to use the color red to represent north and blue to represent south. To identify a magnets polarity, you can use a compass. Since opposites attract, the needle will point north to the south pole of the magnet.

[![alt text](https://cdn.sparkfun.com/assets/2/7/a/b/d/52a2197a757b7fcd5c8b4567.png)](https://cdn.sparkfun.com/assets/2/7/a/b/d/52a2197a757b7fcd5c8b4567.png)

You can perform the same experiment with an electromagnet to determine polarity.

[![Compass and electromagnet](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/6/compassElectromagnet-Corrected.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/6/compassElectromagnet-Corrected.jpg)

If you reverse the flow of current, you can see how an electromagnet can reverse its poles.

[![Compass and electromagnet current reversed](https://cdn.sparkfun.com/assets/4/5/1/4/a/52a224c7757b7f85328b4568.png)](https://cdn.sparkfun.com/assets/4/5/1/4/a/52a224c7757b7f85328b4568.png)

This is a key principle for building motors! Now, let\'s look at some different motors and how they use magnets and electromagnets.

## DC Brush Motors - The Classic

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/1/c/4/1/7/52a0cce7757b7fdf2c8b4568.jpg)](https://cdn.sparkfun.com/assets/1/c/4/1/7/52a0cce7757b7fdf2c8b4568.jpg)

The DC brush motor is one of the simplest motors in use today. You can find these motors just about anywhere. They are in household appliances, toys, and automobiles. Being simple to construct and control, these motors are the go-to solution for professionals and hobbyists alike.

## The Anatomy of a Brush Motor

[![](https://cdn.sparkfun.com/assets/a/1/6/0/2/524dcee9757b7f00478b4567.jpg)](https://cdn.sparkfun.com/assets/a/1/6/0/2/524dcee9757b7f00478b4567.jpg)

To better understand how one works, let\'s start by tearing down a simple [hobby motor](https://www.sparkfun.com/products/10171). As you can see, they are simple in construction, comprising of a few key components.

[![Disected Motor!](https://cdn.sparkfun.com/r/500-500/assets/9/3/c/2/4/BrushMotorAnatomy_1.png)](https://cdn.sparkfun.com/assets/9/3/c/2/4/BrushMotorAnatomy_1.png)

- Brushes - Delivers power from the contacts to the armature through the commutator
- Contacts - Brings power from the controller to the brushes
- Commutator - Delivers power to the appropriate set of windings as the armature rotates
- Windings - Converts electricity to a magnetic field that drives the axle
- Axle - Transfers the mechanical power of the motor to the user application
- Magnets - Provide a magnetic field for the windings to attract and repel
- Bushing - Minimizes friction for the axle
- Can - Provides a mechanical casing for the motor

## Theory of Operation

[![Go Speed Racer!](https://cdn.sparkfun.com/assets/1/d/4/3/f/525d9258757b7f557c8b4567.gif)](https://cdn.sparkfun.com/assets/1/d/4/3/f/525d9258757b7f557c8b4567.gif)

As the windings are energized, they attract to the magnets located around the motor. This rotates the motor until the brushes make contact with a new set of commutator contacts. This new contact energizes a new set of windings and starts the process again. To reverse the direction of the motor, simply reverse the polarity on the motor contacts. Sparks inside a brush motor are produced by the brush jumping to the next contact. Each wire of a coil is connected to the two closest commutator contacts.

[![Coils Shown](https://cdn.sparkfun.com/assets/a/d/9/c/9/525eb3ce757b7f28278b4569.png)](https://cdn.sparkfun.com/assets/a/d/9/c/9/525eb3ce757b7f28278b4569.png)

An odd number of windings is always used to prevent the motor from getting locked into a steady state. Larger motors also use more sets of windings to help eliminate \"cogging,\" thus providing smooth control at low revolutions per minute (RPMs). Cogging can be demonstrated by rotating the motor axle by hand. You will feel \"bumps\" in the motion where the magnets are closest to the exposed stator. Cogging can be eliminated with a few tricks in design, but the most prevalent is removing the stator all together. These types of motors are referred to as [ironless or coreless motors](http://en.wikipedia.org/wiki/Electric_motor#Ironless_or_coreless_rotor_motor).

## Pros

- Simple to control
- Excellent torque at low RPM
- Inexpensive and mass produced

## Cons

- Brushes can wear out over time
- Brush arcing can generate electromagnetic noise
- Usually limited in speed due to brush heating

## Brushless Motors - MORE POWER!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/3/7/d/a/b/52a0cce6757b7f17488b456b.jpg)](https://cdn.sparkfun.com/assets/3/7/d/a/b/52a0cce6757b7f17488b456b.jpg)

Brushless motors are taking over! Ok, maybe that was an overstatement. However, brushless motors have begun to dominate the hobby markets between aircraft and ground vehicles. Controlling these motors had been a hurdle up until microcontrollers became cheap and powerful enough to handle the task. There is still work being done to develop faster and more efficient controllers to unlock their amazing potential. Without brushes to fail, these motors deliver more power and can do so silently. Most high-end appliances and vehicles are moving to brushless systems. One notable example is the [Tesla Model S](http://en.wikipedia.org/wiki/Tesla_Model_S).

## The Anatomy of a Brushless Motor

[![alt text](https://cdn.sparkfun.com/r/500-500/assets/6/3/5/8/9/525ee353757b7f8d2d8b4568.jpg)](https://cdn.sparkfun.com/assets/6/3/5/8/9/525ee353757b7f8d2d8b4568.jpg)

To better understand how one works, let\'s start by tearing down a simple brushless motor. These are commonly found on remote control airplanes and helicopters.

[![alt text](https://cdn.sparkfun.com/r/500-500/assets/0/b/0/0/9/BrushlessMotorAnatomy.png)](https://cdn.sparkfun.com/assets/0/b/0/0/9/BrushlessMotorAnatomy.png)

- Windings - Converts electricity to a magnetic field that drives the rotor
- Contacts - Brings power from the controller to the windings
- Bearings - Minimizes friction for the axle
- Magnets - Provide a magnetic field for the windings to attract and repel
- Axle - Transfers the mechanical power of the motor to the user application

## Theory of Operation

[![alt text](https://cdn.sparkfun.com/assets/f/5/b/e/b/525ee354757b7fc92d8b456c.gif)](https://cdn.sparkfun.com/assets/f/5/b/e/b/525ee354757b7fc92d8b456c.gif)

The mechanics of a brushless motor are incredibly simple. The only moving part is the the rotor, which contains the magnets. Where things become complicated is orchestrating the sequence of energizing windings. The polarity of each winding is controlled by the direction of current flow. The animation demonstrates a simple pattern that controllers would follow. Alternating current changes the polarity, giving each winding a \"push/pull\" effect. The trick is keeping this pattern in sync with the speed of the rotor. There are two (widely used) ways this can be accomplished. Most hobby controllers measure the voltage produced ([back EMI](http://en.wikipedia.org/wiki/Counter-electromotive_force)) on the un-energized winding. This method is very reliable in high velocity operation. As the motor rotates slower, the voltage produced becomes more difficult to measure and more errors are induced. Newer hobby controllers and many industrial controllers utilize [Hall effect sensors](http://en.wikipedia.org/wiki/Hall_effect_sensor) to measure the magnets position directly. This is the primary method for controlling computer fans.

[![alt text](https://cdn.sparkfun.com/r/500-500/assets/8/1/c/7/8/5260259e757b7f9d538b456d.png)](https://cdn.sparkfun.com/assets/8/1/c/7/8/5260259e757b7f9d538b456d.png)

## Pros

- Reliable
- High speed
- Efficient
- Mass produced and easy to find

## Cons

- Difficult to control without specialized controller
- Requires low starting loads
- Typically require specialized gearboxes in drive applications

## Stepper Motors - Simply Precise

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/b/f/a/9/d/52a0cce7757b7f1a458b4569.jpg)](https://cdn.sparkfun.com/assets/b/f/a/9/d/52a0cce7757b7f1a458b4569.jpg)

Stepper motors are great motors for position control. They can be found in desktop printers, plotters, 3d printers, CNC milling machines, and anything else requiring precise position control. Steppers are a special segment of brushless motors. They are purposely built for high-holding torque. This high-holding torque gives the user the ability to incrementally \"step\" to the next position. This results in a simple positioning system that doesn\'t require an encoder. This makes stepper motor controllers very simple to build and use.

## The Anatomy of a Stepper Motor

[![alt text](https://cdn.sparkfun.com/assets/f/a/6/9/8/525f0431757b7fa85b8b456a.jpg)](https://cdn.sparkfun.com/assets/f/a/6/9/8/525f0431757b7fa85b8b456a.jpg)

To better understand how one works, let\'s start by tearing down a simple [stepper motor](https://www.sparkfun.com/products/10846). As you can see, these motors are built for direct drive loads containing a few key components.

[![alt text](https://cdn.sparkfun.com/r/500-500/assets/9/3/f/5/2/StepperMotorAnatomy_1.png)](https://cdn.sparkfun.com/assets/9/3/f/5/2/StepperMotorAnatomy_1.png)

- Axle - Transfers the mechanical power of the motor to the user application
- Bearings - Minimizes friction for the axle
- Magnets - Provide a magnetic field for the windings to attract and repel
- Poles - Increases the resolution of the step distance by focusing the magnetic field
- Windings - Converts electricity to a magnetic field that drives the axle
- Contacts - Brings power from the controller to the windings

## Theory of Operation

[![alt text](https://cdn.sparkfun.com/assets/b/3/0/5/f/52a27243757b7f7f398b456a.gif)](https://cdn.sparkfun.com/assets/b/3/0/5/f/52a27243757b7f7f398b456a.gif)

*(Credit: [PCB heaven](http://www.pcbheaven.com/wikipages/How_Stepper_Motors_Work/?p=1))*

Stepper motors behave exactly the same as a brushless motor, only the step size is much smaller. The only moving part is the the rotor, which contains the magnets. Where things become complicated is orchestrating the sequence of energizing windings. The polarity of each winding is controlled by the direction of current flow. The animation demonstrates a simple pattern that controllers would follow. Alternating current changes the polarity, giving each winding a \"push/pull\" effect. A notable difference is how the magnet structure of a stepper is different. It is difficult to get an array of magnets to behave nicely on a small scale. It\'s also very expensive. To get around this, most stepper motors utilize a stacked plate method to direct the magnetic poles into \"teeth\".

[![alt text](https://cdn.sparkfun.com/assets/b/6/b/4/3/52a24ada757b7f2b268b4567.png)](https://cdn.sparkfun.com/assets/b/6/b/4/3/52a24ada757b7f2b268b4567.png)

In a brushless motor, back EMF is used to measure velocity. A stepper relies on the short throw of each winding to \"guarantee\" it reaches the desired point in time. In highspeed travel, this can lead to stalling where the rotor can\'t keep up with the sequence. There are ways around this, but they rely on a higher understanding of the relationship between motor windings and inductance.

## Pros

- Excellent position accuracy
- High holding torque
- High reliability
- Most steppers come in standard sizes

## Cons

- Small step distance limits top speed
- It\'s possible to \"skip\" steps with high loads
- Draws maximum current constantly

## Linear Motors - The Future!!!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/d/7/4/6/5/52a2268f757b7fc26b8b4568.jpg)](https://cdn.sparkfun.com/assets/d/7/4/6/5/52a2268f757b7fc26b8b4568.jpg "This machine can place over 1000 chips per minute!")

The future is linear! In high-speed pick and place machines speed is everything. With speed comes friction, with friction comes maintanence, with maintanance comes [downtime](http://en.wikipedia.org/wiki/Downtime), with downtime comes lost productivity. By removing the components needed to transfer rotary to linear motion, the system becomes much lighter and more efficient. Linear motors are simple to maintain, and, with only one moving part, are incredibly reliable. Did I mention they are incredibly fast?! This is the [pick and place machine](https://learn.sparkfun.com/tutorials/electronics-assembly/pick-and-place) we are using in production, and it is incredibly fast! This machine also packs such a punch, there is a warning for pacemakers on it. There is an entire row of high-power, [rare-earth magnets](http://en.wikipedia.org/wiki/Rare-earth_magnet).

[![alt text](https://cdn.sparkfun.com/assets/0/b/4/2/3/52a7c28f757b7fad038b456e.gif)](https://cdn.sparkfun.com/assets/0/b/4/2/3/52a7c28f757b7fad038b456e.gif)

## The Anatomy of a Linear Motor

To better understand how one works, let\'s look inside our pick and place machine downstairs.

- Motion Module - Contains electromagnets and controller.
- Magnets - Provide a magnetic field for the coils to attract and repel
- Linear Bearning - Keeps the motor in alignment with magnets and is the only moving part.

[![alt text](https://cdn.sparkfun.com/assets/5/4/e/b/d/52a68053757b7fa8348b456b.png)](https://cdn.sparkfun.com/assets/5/4/e/b/d/52a68053757b7fa8348b456b.png "Note the massive amount of magnets")

## Theory of Operation

[![alt text](https://cdn.sparkfun.com/assets/d/d/c/4/7/52a677c9757b7f2e6b8b4568.gif)](https://cdn.sparkfun.com/assets/d/d/c/4/7/52a677c9757b7f2e6b8b4568.gif)

The mechanics of a linear motor is nearly identical to a brushless motor. The only difference is if you were to take a brushless motor and unfold it into a straight line you\'d have a linear motor. The Motion Module is the only moving part. Where things become complicated is orchestrating the sequence of energizing coils. The polarity of each coil is controlled by the direction of current flow. The animation demonstrates a simple pattern that controllers would follow. Alternating current changes the polarity giving each coil a \"push/pull\" effect. In a linear motor, there is typically an encoder or some advanced positioning system to keep track of the location of the Motion Module. To reach a high position accuracy, the controllers are much more complicated than anything found on a conventional system. [Microstepping](http://en.wikipedia.org/wiki/Stepper_motor#Microstepping) is a method to \"throttle\" the magnets to provide smooth and precise motion. To achieve this though, linear motors require a highly specialized controller tuned for each motor. As controller technology improves, we are likely to see these motors decrease in price. Maybe someday our 3D printers will print in seconds and not hours!

## Pros

- Reliable
- High speed
- Efficient
- No rotary to linear conversion required

## Cons

- Expensive
- Require custom controllers
- Purpose built for each system
- Did I mention expensive?