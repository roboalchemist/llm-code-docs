# Source: https://docs.edgeimpulse.com/hardware/deployments/run-particle.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run Particle library

The Particle Library deployment option packages all your signal processing blocks, configuration and learning blocks up into a single library (.zip file). You can include this library in your own application to run the impulse locally.

## Particle Libraries

To run your Impulse on your Particle board follow these steps:

1. Open a new VS Code window, ensure that [Particle Workbench](https://docs.particle.io/getting-started/developer-tools/workbench/) has been installed.
2. Use [VS Code Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) and type in **Particle: Import Project**
   1. Select the `project.properties` file in the directory that you just downloaded and extracted from the section above.
3. Use [VS Code Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) and type in **Particle: Configure Project for Device**
   1. Select **`deviceOS@5.3.2` (or a later version)**
   2. Choose a target. (e.g. **P2** , this option is also used for the Photon 2).
4. It is sometimes needed to manually put your Device into DFU Mode. You may proceed to the next step, but if you get an error indicating that "No DFU capable USB device available" then please follow these step.
   1. Hold down both the **RESET** and **MODE** buttons.
   2. Release only the **RESET** button, while holding the **MODE** button.
   3. Wait for the LED to start flashing yellow.
   4. Release the **MODE** button.
5. Compile and Flash in one command with: **Particle: Flash application & DeviceOS (local)**

<Warning>
  **Local Compile Only!**
  At this time you cannot use the **Particle: Cloud Compile** or **Particle: Cloud Flash** options; local compilation is required.
</Warning>

<iframe src="https://www.youtube.com/embed/A_twb-ategU" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />


Built with [Mintlify](https://mintlify.com).