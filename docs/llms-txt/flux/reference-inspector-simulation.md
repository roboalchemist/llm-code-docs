# Source: https://docs.flux.ai/reference/reference-inspector-simulation.md

# Simulation menu

**There are two different simulation menus depending what element is selected:**

- If **no element is selected**, the global simulator menu will be shown.
- If **any element is selected**, the object-specific simulator menu will be shown

### Global simulation menu

Controls simulation parameters for the whole circuit.

![](https://uploads.developerhub.io/prod/86Yw/ct2me21qeoc6zykybjkil5i7j6zwq1hulrjy6wd1wam43h4cog9k2yglte147y6c.png)

**Simulation Speed:** how fast the the circuit is simulated relative to real time. Moving the slider to the right will increase how fast the circuit simulates.

**Time Step Size:** The time in the simulation between the a measurement of the circuit and the upcoming measurement.

- Most circuit simulation tools (including Flux's) work by measuring a circuit's state many times-per-second to create a seemingly continuous measurement. A good analogy is how a camera takes several pictures per second to create a video. This means that there's a certain amount of time (the step size) between every measurement. If this time is too large, the circuit's simulation behavior may not reflect the real world behavior accurately.

**Simulation Restart:** By clicking the rewind-clock icon, the simulation will restart its model using the initial conditions of each component in the schematic design.

### Object-specific simulation menu

Controls the simulation parameters for each object. To show or hide each simulation variable, click on the eye-type icon on the right side. 

![](https://uploads.developerhub.io/prod/86Yw/zrltjdla6qcg754keevup8m5fx96jvtmpi6044iyi5gebzegdcd1qmxqyw8qmujd.png)