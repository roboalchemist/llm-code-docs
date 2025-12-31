# Source: https://learn.sparkfun.com/tutorials/what-is-electricity

## Getting Started

Electricity is all around us\--powering technology like our cell phones, computers, lights, soldering irons, and air conditioners. It\'s tough to escape it in our modern world. Even when you try to escape electricity, it\'s still at work throughout nature, from the lightning in a thunderstorm to the synapses inside our body. But what exactly *is* electricity? This is a very complicated question, and as you dig deeper and ask more questions, there really is not a definitive answer, only abstract representations of how electricity interacts with our surroundings.

[![Public domain NOAA lightning picture](https://cdn.sparkfun.com/r/600-600/assets/9/8/d/5/4/519f9719ce395faa3c000000.jpg)](https://cdn.sparkfun.com/assets/9/8/d/5/4/519f9719ce395faa3c000000.jpg)

Electricity is a natural phenomenon that occurs throughout nature and takes many different forms. In this tutorial we\'ll focus on current electricity: the stuff that powers our electronic gadgets. Our goal is to understand how electricity flows from a power source through wires, lighting up LEDs, spinning motors, and powering our communication devices.

Electricity is briefly defined as the **flow of electric charge,** but there\'s so much behind that simple statement. Where do the charges come from? How do we move them? Where do they move to? How does an electric charge cause mechanical motion or make things light up? So many questions! To begin to explain what electricity is we need to zoom way in, beyond the matter and molecules, to the atoms that make up everything we interact with in life.

This tutorial builds on some basic understanding of physics, [force](http://en.wikipedia.org/wiki/Force), [energy](http://en.wikipedia.org/wiki/Energy), [atoms](http://en.wikipedia.org/wiki/Atoms), and \[fields\](http://en.wikipedia.org/wiki/Field\_(physics)) in particular. We\'ll gloss over the basics of each of those physics concepts, but it may help to consult other sources as well.

## Going Atomic

To understand the fundamentals of electricity, we need to begin by focusing in on atoms, one of the basic building blocks of life and matter. Atoms exist in over a hundred different forms as chemical elements like hydrogen, carbon, oxygen, and copper. Atoms of many types can combine to make molecules, which build the matter we can physically see and touch.

Atoms are *tiny*, stretching at a max to about 300 picometers long (that\'s 3x10^-10^ or 0.0000000003 meters). A copper penny (if it actually were made of 100% copper) would have 3.2x10^22^ atoms (32,000,000,000,000,000,000,000 atoms) of copper inside it.

Even the atom isn\'t small enough to explain the workings of electricity. We need to dive down one more level and look in on the building blocks of atoms: protons, neutrons, and electrons.

### Building Blocks of Atoms

An atom is built with a combination of three distinct particles: electrons, protons, and neutrons. Each atom has a center nucleus, where the protons and neutrons are densely packed together. Surrounding the nucleus are a group of orbiting electrons.

[![Rutherford atom model](https://cdn.sparkfun.com/r/400-400/assets/0/4/e/8/2/519fa09dce395f8b08000000.png)](https://cdn.sparkfun.com/assets/0/4/e/8/2/519fa09dce395f8b08000000.png)

*A very simple atom model. It\'s not to scale but helpful for understanding how an atom is built. A core nucleus of protons and neutrons is surrounded by orbiting electrons.*

Every atom must have at least one proton in it. The number of protons in an atom is important, because it defines what chemical element the atom represents. For example, an atom with just one proton is hydrogen, an atom with 29 protons is copper, and an atom with 94 protons is plutonium. This count of protons is called the atom\'s **atomic number**.

The proton\'s nucleus-partner, neutrons, serve an important purpose; they keep the protons in the nucleus and determine the isotope of an atom. They\'re not critical to our understanding of electricity, so let\'s not worry about them for this tutorial.

Electrons are critical to the workings of electricity (notice a common theme in their names?) In its most stable, balanced state, an atom will have the same number of electrons as protons. As in the [Bohr atom model](http://en.wikipedia.org/wiki/Bohr_model) below, a nucleus with 29 protons (making it a copper atom) is surrounded by an equal number of electrons.

[![Copper Bohr model](https://cdn.sparkfun.com/r/400-400/assets/9/5/4/c/f/519fbf5cce395f953c000000.png)](https://cdn.sparkfun.com/assets/9/5/4/c/f/519fbf5cce395f953c000000.png)

*As our understanding of atoms has evolved, so too has our method for modeling them. The Bohr model is a very useful atom model as we explore electricity.*

The atom\'s electrons aren\'t all forever bound to the atom. The electrons on the outer orbit of the atom are called valence electrons. With enough outside force, a valence electron can escape orbit of the atom and become free. **Free electrons** allow us to move charge, which is what electricity is all about. Speaking of charge\...

## Flowing Charges

As we mentioned at the beginning of this tutorial, electricity is defined as the flow of electric charge. **Charge** is a property of matter\--just like mass, volume, or density. It is measurable. Just as you can quantify how much mass something has, you can measure how much charge it has. The key concept with charge is that it can come in two types: **positive (+) or negative (-)**.

In order to move charge we need **charge carriers**, and that\'s where our knowledge of atomic particles\--specifically electrons and protons\--comes in handy. Electrons always carry a negative charge, while protons are always positively charged. Neutrons (true to their name) are neutral, they have no charge. Both electrons and protons carry the same **amount** of charge, just a different type.

[![Lithium atom with particle charges labeled](https://cdn.sparkfun.com/r/600-600/assets/3/4/1/a/3/51a65d7bce395f156c000000.png)](https://cdn.sparkfun.com/assets/3/4/1/a/3/51a65d7bce395f156c000000.png)

*A lithium atom (3 protons) model with the charges labeled.*

The charge of electrons and protons is important, because it provides us the means to exert a force on them. Electrostatic force!

### Electrostatic Force

Electrostatic force (also called [Coulomb\'s law](https://en.wikipedia.org/wiki/Coulomb%27s_law)) is a force that operates between charges. It states that charges of the same type repel each other, while charges of opposite types are attracted together. **Opposites attract, and likes repel**.

[![Charges attract/repel](https://cdn.sparkfun.com/r/400-400/assets/a/6/2/4/4/519fb817ce395fff0a000000.png)](https://cdn.sparkfun.com/assets/a/6/2/4/4/519fb817ce395fff0a000000.png)

The **amount** of force acting on two charges depends on how far they are from each other. The closer two charges get, the greater the force (either pushing together, or pulling away) becomes.

Thanks to electrostatic force, electrons will push away other electrons and be attracted to protons. This force is part of the \"glue\" that holds atoms together, but it\'s also the tool we need to make electrons (and charges) flow!

### Making Charges Flow

We now have all the tools to make charges flow. **Electrons** in atoms can act as our **charge carrier**, because every electron carries a negative charge. If we can free an electron from an atom and force it to move, we can create electricity.

Consider the atomic model of a copper atom, one of the preferred elemental sources for charge flow. In its balanced state, copper has 29 protons in its nucleus and an equal number of electrons orbiting around it. Electrons orbit at varying distances from the nucleus of the atom. Electrons closer to the nucleus feel a much stronger attraction to the center than those in distant orbits. The outermost electrons of an atom are called the **valence electrons**, these require the least amount of force to be freed from an atom.

[![Copper atom with valence electron labeled](https://cdn.sparkfun.com/r/400-400/assets/6/e/6/0/2/51a67853ce395fa26b000000.png)](https://cdn.sparkfun.com/assets/6/e/6/0/2/51a67853ce395fa26b000000.png)

*This is a copper atom diagram: 29 protons in the nucleus, surrounded by bands of circling electrons. Electrons closer to the nucleus are hard to remove while the valence (outer ring) electron requires relatively little energy to be ejected from the atom.*

Using enough electrostatic force on the valence electron\--either pushing it with another negative charge or attracting it with a positive charge\--we can eject the electron from orbit around the atom creating a free electron.

Now consider a copper wire: matter filled with countless copper atoms. As our **free electron** is floating in a space between atoms, it\'s pulled and prodded by surrounding charges in that space. In this chaos the free electron eventually finds a new atom to latch on to; in doing so, the negative charge of that electron ejects another valence electron from the atom. Now a new electron is drifting through free space looking to do the same thing. This chain effect can continue on and on to create a flow of electrons called **electric current**.

[![Simple electron flow](https://cdn.sparkfun.com/assets/9/5/6/1/4/519fcd42ce395f804c000000.gif)](https://cdn.sparkfun.com/assets/9/5/6/1/4/519fcd42ce395f804c000000.gif)

*A very simplified model of charges flowing through atoms to make current.*

### Conductivity

Some elemental types of atoms are better than others at releasing their electrons. To get the best possible electron flow we want to use atoms which don\'t hold very tightly to their valence electrons. An element\'s conductivity measures how tightly bound an electron is to an atom.

Elements with high conductivity, which have very mobile electrons, are called **conductors**. These are the types of materials we want to use to make wires and other components which aid in electron flow. Metals like copper, silver, and gold are usually our top choices for good conductors.

Elements with low conductivity are called **insulators**. Insulators serve a very important purpose: they prevent the flow of electrons. Popular insulators include glass, rubber, plastic, and air.

## Static or Current Electricity

Before we get much further, let\'s discuss the two forms electricity can take: static or current. In working with electronics, current electricity will be much more common, but static electricity is important to understand as well.

### Static Electricity

Static electricity exists when there is a build-up of opposite charges on objects separated by an insulator. Static (as in \"at rest\") electricity exists until the two groups of opposite charges can find a path between each other to balance the system out.

[![Static electricity example](https://cdn.sparkfun.com/assets/d/9/1/2/4/51a79b81ce395f8a10000000.png)](https://cdn.sparkfun.com/assets/d/9/1/2/4/51a79b81ce395f8a10000000.png)

When the charges do find a means of equalizing, a **static discharge** occurs. The attraction of the charges becomes so great that they can flow through even the best of insulators (air, glass, plastic, rubber, etc.). Static discharges can be harmful depending on what medium the charges travel through and to what surfaces the charges are transferring. Charges equalizing through an air gap can result in a visible shock as the traveling electrons collide with electrons in the air, which become excited and release energy in the form of light.

[![Spark gap igniter static shock](https://cdn.sparkfun.com/assets/9/6/8/6/6/51a4e10fce395f1525000000.jpg)](https://cdn.sparkfun.com/assets/9/6/8/6/6/51a4e10fce395f1525000000.jpg)

*[Spark gap igniters](https://www.sparkfun.com/products/11218) are used to create a controlled static discharge. Opposite charges build up on each of the conductors until their attraction is so great charges can flow through the air.*

One of the most dramatic examples of static discharge is **lightning**. When a cloud system gathers enough charge relative to either another group of clouds or the earth\'s ground, the charges will try to equalize. As the cloud discharges, massive quantities of positive (or sometimes negative) charges run through the air from ground to cloud causing the visible effect we\'re all familiar with.

Static electricity also familiarly exists when we rub balloons on our head to make our hair stand up, or when we [shuffle on the floor](http://www.youtube.com/watch?v=3PPDmDnxcEc) with fuzzy slippers and shock the family cat (accidentally, of course). In each case, friction from rubbing different types of materials transfers electrons. The object losing electrons becomes positively charged, while the object gaining electrons becomes negatively charged. The two objects become attracted to each other until they can find a way to equalize.

Working with electronics, we generally don\'t have to deal with static electricity. When we do, we\'re usually trying to protect our sensitive electronic components from being subjected to a static discharge. Preventative measures against static electricity include wearing ESD (electrostatic discharge) wrist straps, or adding special components in circuits to protect against very high spikes of charge.

### Current Electricity

Current electricity is the form of electricity which makes all of our electronic gizmos possible. This form of electricity exists when charges are able to **constantly flow**. As opposed to static electricity where charges gather and remain at rest, current electricity is dynamic, charges are always on the move. We\'ll be focusing on this form of electricity throughout the rest of the tutorial.

#### Circuits

In order to flow, current electricity requires a [circuit](https://learn.sparkfun.com/tutorials/what-is-a-circuit): a closed, never-ending loop of conductive material. A circuit could be as simple as a conductive wire connected end-to-end, but useful circuits usually contain a mix of wire and other components which control the flow of electricity. The only rule when it comes to making circuits is they **can\'t have any insulating gaps** in them.

If you have a wire full of copper atoms and want to induce a flow of electrons through it, *all* free electrons need somewhere to flow in the same general direction. Copper is a great conductor, perfect for making charges flow. If a circuit of copper wire is broken, the charges can\'t flow through the air, which will also prevent any of the charges toward the middle from going anywhere.

On the other hand, if the wire were connected end-to-end, the electrons all have a neighboring atom and can all flow in the same general direction.

------------------------------------------------------------------------

We now understand *how* electrons can flow, but how do we get them flowing in the first place? Then, once the electrons are flowing, how do they produce the energy required to illuminate light bulbs or spin motors? For that, we need to understand electric fields.

## Electric Fields

We have a handle on how electrons flow through matter to create electricity. That\'s all there is to electricity. Well, almost all. Now we need a source to induce the flow of electrons. Most often that source of electron flow will come from an electric field.

### What\'s a Field?

A *field* is a tool we use to model physical interactions which **don\'t involve any observable contact**. Fields can\'t be seen as they don\'t have a physical appearance, but the effect they have is very real.

We\'re all subconsciously familiar with one field in particular: [Earth\'s gravitational field](http://en.wikipedia.org/wiki/Earth%27s_gravity), the effect of a massive body attracting other bodies. Earth\'s gravitational field can be modeled with a set of vectors all pointing into the center of the planet; regardless of where you are on the surface, you\'ll feel the force pushing you towards it.

[![Earth gravity field](https://cdn.sparkfun.com/assets/5/1/a/e/9/51a4ee19ce395f2625000000.png)](https://cdn.sparkfun.com/assets/5/1/a/e/9/51a4ee19ce395f2625000000.png)

The strength or intensity of fields isn\'t uniform at all points in the field. The further you are from the source of the field the less effect the field has. The magnitude of Earth\'s gravitational field decreases as you get further away from the center of the planet.

As we go on to explore electric fields in particular remember how Earth\'s gravitational field works, both fields share many similarities. Gravitational fields exert a force on objects of mass, and electric fields exert a force on objects of charge.

### Electric Fields

Electric fields (e-fields) are an important tool in understanding how electricity begins and continues to flow. Electric fields **describe the pulling or pushing force in a space between charges**. Compared to Earth\'s gravitational field, electric fields have one major difference: while Earth\'s field generally only attracts other objects of mass (since everything is *so* significantly less massive), electric fields push charges away just as often as they attract them.

The direction of electric fields is always defined as the **direction a positive test charge would move** if it was dropped in the field. The test charge has to be infinitely small, to keep its charge from influencing the field.

We can begin by constructing electric fields for solitary positive and negative charges. If you dropped a positive test charge near a negative charge, the test charge would be attracted towards the **negative** charge. So, for a single, negative charge we draw our electric field arrows **pointing inward** at all directions. That same test charge dropped near another **positive** charge would result in an outward repulsion, which means we draw **arrows going out** of the positive charge.

[![Electric fields of single charges](https://cdn.sparkfun.com/assets/2/d/5/0/0/519fd3c7ce395f974c000000.png)](https://cdn.sparkfun.com/assets/2/d/5/0/0/519fd3c7ce395f974c000000.png)

*The electric fields of single charges. A negative charge has an inward electric field because it attracts positive charges. The positive charge has an outward electric field, pushing away like charges.*

Groups of electric charges can be combined to make more complete electric fields.

[![Bigger e-field](https://cdn.sparkfun.com/r/400-400/assets/3/b/d/a/0/519fd76ece395f4b4c000000.png)](https://cdn.sparkfun.com/assets/3/b/d/a/0/519fd76ece395f4b4c000000.png)

The uniform e-field above points away from the positive charges, towards the negatives. Imagine a tiny positive test charge dropped in the e-field; it should follow the direction of the arrows. As we\'ve seen, electricity usually involves the flow of electrons\--negative charges\--which flow **against** electric fields.

Electric fields provide us with the pushing force we need to induce current flow. An electric field in a circuit is like an electron pump: a large source of negative charges that can propel electrons, which will flow through the circuit towards the positive lump of charges.

## Electric Potential (Energy)

When we harness electricity to power our circuits, gizmos, and gadgets, we\'re really transforming energy. Electronic circuits must be able to store energy and transfer it to other forms like heat, light, or motion. The stored energy of a circuit is called electric potential energy.

### Energy? Potential Energy?

To understand potential energy we need to understand energy in general. Energy is defined as the ability of an object to do *work* on another object, which means moving that object some distance. Energy comes in **many forms**, some we can see (like mechanical) and others we can\'t (like chemical or electrical). Regardless of what form it\'s in, energy exists in one of two **states**: kinetic or potential.

An object has **kinetic energy** when it\'s in motion. The amount of kinetic energy an object has depends on its mass and speed. **Potential energy**, on the other hand, is a **stored energy** when an object is at rest. It describes how much work the object could do if set into motion. It\'s an energy we can generally control. When an object is set into motion, its potential energy transforms into kinetic energy.

[![Gravitational potential energy](https://cdn.sparkfun.com/r/400-400/assets/2/9/2/3/a/51a7c325ce395f341d000001.png)](https://cdn.sparkfun.com/assets/2/9/2/3/a/51a7c325ce395f341d000001.png)

Let\'s go back to using gravity as an example. A bowling ball sitting motionless at the top of [Khalifa tower](http://en.wikipedia.org/wiki/Burj_Khalifa) has a lot of potential (stored) energy. Once dropped, the ball\--pulled by the gravitational field\--accelerates towards the ground. As the ball accelerates, potential energy is converted into kinetic energy (the energy from motion). Eventually all of the ball\'s energy is converted from potential to kinetic, and then passed on to whatever it hits. When the ball is on the ground, it has a very low potential energy.

### Electric Potential Energy

Just like mass in a gravitational field has gravitational potential energy, charges in an electric field have an **electric potential energy**. A charge\'s electric potential energy describes how much stored energy it has, when set into motion by an electrostatic force, that energy can become kinetic, and the charge can do work.

Like a bowling ball sitting at the top of a tower, a positive charge in close proximity to another positive charge has a high potential energy; left free to move, the charge would be repelled away from the like charge. A positive test charge placed near a negative charge would have low potential energy, analogous to the bowling ball on the ground.

[![Potential Energy in a field](https://cdn.sparkfun.com/r/600-600/assets/2/3/5/1/e/51a4f1a7ce395f4125000000.png)](https://cdn.sparkfun.com/assets/2/3/5/1/e/51a4f1a7ce395f4125000000.png)

To instill anything with potential energy, we have to do **work** by moving it over a distance. In the case of the bowling ball, the work comes from carrying it up 163 floors, against the field of gravity. Similarly, work must be done to push a positive charge against the arrows of an electric field (either towards another positive charge, or away from a negative charge). The further up the field the charge goes, the more work you have to do. Likewise, if you try to pull a negative charge *away* from a positive charge\--against an electric field\--you have to do work.

For any charge located in an electric field its electric potential energy depends on the type (positive or negative), amount of charge, and its position in the field. Electric potential energy is measured in units of joules (*J*).

### Electric Potential

Electric potential builds upon electric potential *energy* to help define how much **energy is stored in electric fields**. It\'s another concept which helps us model the behavior of electric fields. Electric potential is *not* the same thing as electric potential energy!

At any point in an electric field the electric potential is the **amount of electric potential energy divided by the amount of charge** at that point. It takes the charge quantity out of the equation and leaves us with an idea of how much potential energy specific areas of the electric field may provide. Electric potential comes in units of joules per coulomb (*J/C*), which we define as a **volt** (V).

In any electric field there are two points of electric potential that are of significant interest to us. There\'s a point of high potential, where a positive charge would have the highest possible potential energy, and there\'s a point of low potential, where a charge would have the lowest possible potential energy.

One of the most common terms we discuss in evaluating electricity is **voltage**. A voltage is the difference in potential between two points in an electric field. Voltage gives us an idea of just how much pushing force an electric field has.

------------------------------------------------------------------------

With potential and potential energy under our belt we have all of the ingredients necessary to make current electricity. Let\'s do it!

## Electricity in Action!

After studying particle physics, field theory, and potential energy, we now know enough to make electricity flow. Let\'s make a circuit!

First we will review the ingredients we need to make electricity:

- The definition of electricity is the **flow of charge**. Usually our charges will be carried by free-flowing electrons.
- Negatively-charged **electrons** are loosely held to atoms of conductive materials. With a little push we can free electrons from atoms and get them to flow in a generally uniform direction.
- A closed **circuit** of conductive material provides a path for electrons to continuously flow.
- The charges are propelled by an **electric field**. We need a source of electric potential (voltage), which pushes electrons from a point of low potential energy to higher potential energy.

### A Short Circuit

Batteries are common energy sources which convert chemical energy to electrical energy. They have two terminals, which connect to the rest of the circuit. On one terminal there are an excess of negative charges, while all of the positive charges coalesce on the other. This is an electric potential difference just waiting to act!

[![Battery with charges](https://cdn.sparkfun.com/assets/4/2/5/5/c/51a78f3ece395fa011000003.png)](https://cdn.sparkfun.com/assets/4/2/5/5/c/51a78f3ece395fa011000003.png)

If we connected our wire full of conductive copper atoms to the battery, that electric field will influence the negatively-charged free electrons in the copper atoms. Simultaneously pushed by the negative terminal and pulled by the positive terminal, the electrons in the copper will move from atom to atom creating the flow of charge we know as electricity.

[![Battery short circuit](https://cdn.sparkfun.com/r/400-400/assets/8/4/1/0/e/51a79424ce395f9a11000000.png)](https://cdn.sparkfun.com/assets/8/4/1/0/e/51a79424ce395f9a11000000.png)

After a second of the current flow, the electrons have actually moved *very* little\--fractions of a centimeter. However, the energy produced by the current flow is *huge*, especially since there\'s nothing in this circuit to slow down the flow or consume the energy. Connecting a pure conductor directly across an energy source is a **bad idea**. Energy moves very quickly through the system and is transformed into heat in the wire, which may quickly turn into melting wire or fire.

### Illuminating a Light Bulb

Instead of wasting all that energy, not to mention destroying the battery and wire, let\'s build a circuit that does something useful! Generally an electric circuit will transfer electric energy into some other form\--light, heat, motion, etc. If we connect a light bulb to the battery with wires in between, we have a simple, functional circuit.

[![Lightbulb animation](https://cdn.sparkfun.com/assets/a/0/9/4/0/51a52b62ce395f2f25000001.gif)](https://cdn.sparkfun.com/assets/a/0/9/4/0/51a52b62ce395f2f25000001.gif)

*Schematic: A battery (left) connecting to a lightbulb (right), the circuit is completed when the switch (top) closes. With the circuit closed, electrons can flow, pushed from the negative terminal of the battery through the lightbulb, to the positive terminal.*

While the electrons move at a snails pace, the electric field affects the entire circuit almost instantly (we\'re talking speed of light fast). Electrons throughout the circuit, whether at the lowest potential, highest potential, or right next to the light bulb, are influenced by the electric field. When the switch closes and the electrons are subjected to the electric field, all electrons in the circuit start flowing at seemingly the same time. Those charges nearest the light bulb will take one step through the circuit and start transforming energy from electrical to light (or heat).