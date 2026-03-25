# Source: https://docs.edgeimpulse.com/projects/expert-network/voice-commands-particle-photon-2.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Recognize Voice Commands with the Particle Photon 2

Created By: Roni Bandini

Public Project Link: [https://studio.edgeimpulse.com/public/288386/latest](https://studio.edgeimpulse.com/public/288386/latest)

GitHub Repository: [https://github.com/ronibandini/Photon2VoiceCommand](https://github.com/ronibandini/Photon2VoiceCommand)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5rOHXnajjgzPqvkd/.assets/images/voice-commands-particle-photon-2/cover.jpg?fit=max&auto=format&n=5rOHXnajjgzPqvkd&q=85&s=d3c8dad8647f1c0d2b4874c3d043590f" width="750" height="1000" data-path=".assets/images/voice-commands-particle-photon-2/cover.jpg" />
</Frame>

## Introduction

In industrial settings, workers often find themselves unable to operate machinery manually due to concurrent tasks demanding the use of their hands. Machine Learning (ML) has emerged as a transformative solution, enabling compact devices to comprehend and respond to vocal instructions, thereby initiating or halting machines as needed.

In the context of this project, we will leverage the Edge Impulse platform to train a customized ML model. Subsequently, we will deploy this model onto a [Particle Photon 2 microcontroller board](https://store.particle.io/products/photon-2). The Photon 2 board will be connected to a PDA microphone and a Relay module, creating an integrated system for practical demonstration.

## Prerequisites

The Photon 2 is an interesting, high quality board made by Particle. It has 5 GHz WiFi and Bluetooth (BLE) 5, an ARM Cortex-M33 CPU running at 200 MHz, 2 MB of storage for user applications, 3 MB of RAM available to user applications, and a 2 MB flash file system.

The board size is 1.5 x 0.78 inches (5 x 2cm) and it comes with pre-soldered, labeled male headers. It also has 2 buttons (Reset and Mode), one RGB led, a LIPO charger with a JST-PH port, and a 10-pin micro JTAG connector for SWD (Serial Wire Debug).

Besides the Photon 2 board, the [Edge ML Kit](https://docs.particle.io/reference/datasheets/accessories/edge-ml-kit/) is required for this project, which includes a W18340-A PDA MEMs microphone by Adafruit. The Edge AI Kit also includes jumper wires, a protoboard, PIR sensor, distance sensor, LED, switches, resistors, vibration sensor, accelerometer, and loudness sensor for many other AI projects. The Relay module is not included, but it is a cheap common device that can be ordered online from many electronic stores.

## Circuit

The PDA MIC comes without header pins soldered, so we need to solder 5 headers and discard the sixth one (if using a 6-pin header as I've done here). After that we will connect the PDA mic to the board using jumper cables.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5rOHXnajjgzPqvkd/.assets/images/voice-commands-particle-photon-2/microphone.jpg?fit=max&auto=format&n=5rOHXnajjgzPqvkd&q=85&s=10bfc45db9984082efafab81408edadf" width="750" height="1000" data-path=".assets/images/voice-commands-particle-photon-2/microphone.jpg" />
</Frame>

The PDA microphone connections should be:

* PDA GND to Photon 2 GND
* PDA 3v to Photon 2 3v3
* PDA CLK to Photon 2 A0
* PDA DAT to Photon 2 A1
* The PDA Mic SEL pin is not used for this scenario.

The Relay module should be connected as follows:

* Relay GND to Photon 2 GND
* Relay VCC to Photon 2 VCC
* Relay Signal to Photon 2 D3

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5rOHXnajjgzPqvkd/.assets/images/voice-commands-particle-photon-2/circuit.jpg?fit=max&auto=format&n=5rOHXnajjgzPqvkd&q=85&s=8716b184e003977bd9423b84b211f614" width="850" height="602" data-path=".assets/images/voice-commands-particle-photon-2/circuit.jpg" />
</Frame>

Since the Photon 2 has one GND and one 3v3 pin on the board, the Microphone GND and Relay GND should
be connected together, and also Microphone 3v and Relay 3v. You can do that using the
protoboard and Male-Female jumper cables from the Edge AI kit, or you can also cut and solder the
cables.

## Data Acquisition and Model Training

We will create an account at [Edge Impulse](https://edgeimpulse.com/), then login and create a new project.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5rOHXnajjgzPqvkd/.assets/images/voice-commands-particle-photon-2/project.jpg?fit=max&auto=format&n=5rOHXnajjgzPqvkd&q=85&s=3bd70d3b8d46654a3c0b8abb12b6c0c0" width="1483" height="532" data-path=".assets/images/voice-commands-particle-photon-2/project.jpg" />
</Frame>

We will use the computer to record data samples for 2 labels: **machine** and **background**. Go to Collect data, Connect a Device, and Connect to your computer.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5rOHXnajjgzPqvkd/.assets/images/voice-commands-particle-photon-2/data-1.jpg?fit=max&auto=format&n=5rOHXnajjgzPqvkd&q=85&s=e27f1636c83a47c8ef4504790757af02" width="940" height="462" data-path=".assets/images/voice-commands-particle-photon-2/data-1.jpg" />
</Frame>

Enable your microphone permissions if necessary, and repeat the word **"machine"** several times, leaving a few seconds in between each. For **background** sound, just record any continuous background sound.

Wait a few seconds to allow the recording to be uploaded to Edge Impulse before going to the next step.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5rOHXnajjgzPqvkd/.assets/images/voice-commands-particle-photon-2/data-3.jpg?fit=max&auto=format&n=5rOHXnajjgzPqvkd&q=85&s=70b4afa60a019e310487f5533c91c911" width="1600" height="463" data-path=".assets/images/voice-commands-particle-photon-2/data-3.jpg" />
</Frame>

Now we are going to Split the samples. Click on the three vertical dots next to the recording and select "Split sample". Leave the length set to the default, 1000ms. Repeat this process for both labels.

Now we will design an Impulse. In the Edge Impulse Studio, go to **Create impulse**, set the Window size to 1000ms, the Window increase to 500ms, and add the 'Audio MFCC' Processing Block, which is perfect for voices. Then add 'Classification (Keras)' as the Learning Block. Now click **Save impulse**.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5rOHXnajjgzPqvkd/.assets/images/voice-commands-particle-photon-2/impulse.jpg?fit=max&auto=format&n=5rOHXnajjgzPqvkd&q=85&s=d29283ae21defb1a4cfe6238425fd9a4" width="1600" height="750" data-path=".assets/images/voice-commands-particle-photon-2/impulse.jpg" />
</Frame>

Next we will go to MFCC parameters. This page allows us to configure the MFCC block, and lets us preview how the data will be transformed. The MFCC block transforms a window of audio into a table of data where each row represents a range of frequencies, and each column represents a span of time. The value contained within each cell reflects the amplitude of its associated range of frequencies during that span of time.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5rOHXnajjgzPqvkd/.assets/images/voice-commands-particle-photon-2/features-1.jpg?fit=max&auto=format&n=5rOHXnajjgzPqvkd&q=85&s=09ce82873eaf66edb4276392e57458e7" width="1600" height="750" data-path=".assets/images/voice-commands-particle-photon-2/features-1.jpg" />
</Frame>

We will leave the default values, which are pre-configured according to the data. Then we click on Generate Features.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5rOHXnajjgzPqvkd/.assets/images/voice-commands-particle-photon-2/features-2.jpg?fit=max&auto=format&n=5rOHXnajjgzPqvkd&q=85&s=40791efadc1c42dac40e2bb4fa132c31" width="1600" height="768" data-path=".assets/images/voice-commands-particle-photon-2/features-2.jpg" />
</Frame>

Now we go to Neural Network configuration. Click on **Classifier**, and the settings can be left on their default values, then scroll down to click **Start Training**. In this case, we have got a 100% accuracy, which is uncommon, but the data and recordings are quite different so the neural network is able to segment them quite well.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5rOHXnajjgzPqvkd/.assets/images/voice-commands-particle-photon-2/model.jpg?fit=max&auto=format&n=5rOHXnajjgzPqvkd&q=85&s=dc8548747669093b1f53949b8b337100" width="1600" height="741" data-path=".assets/images/voice-commands-particle-photon-2/model.jpg" />
</Frame>

You can upload new samples and test them with Model Testing feature.

The final step is to deploy a library to the Particle Photon 2. We will click **Deployment**, begin to type the word Particle in the search box, then select the Particle Library and click **Build**.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5rOHXnajjgzPqvkd/.assets/images/voice-commands-particle-photon-2/deployment.jpg?fit=max&auto=format&n=5rOHXnajjgzPqvkd&q=85&s=018e817d5313d9c5ecf7acca1ef31d38" width="1600" height="740" data-path=".assets/images/voice-commands-particle-photon-2/deployment.jpg" />
</Frame>

## Visual Studio Code

The main difference about working with the Photon 2 is that the Arduino IDE is not used to upload the code and libraries. Instead, Microsoft Visual Studio Code is used, and there are several setup steps to carefully follow.

### Windows Installation

Install [Microsoft Visual Studio Code](https://code.visualstudio.com), then add the [Particle Workbench](https://marketplace.visualstudio.com/items?itemName=particle.particle-vscode-pack) extension.

Unzip the Particle library exported from Edge Impulse Studio.

In VS Code, press Ctrl+Shift+P to bring up the Particle menu and select the "Particle: Import Project" feature to choose the library. The first time, VSCode will download dependencies.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5rOHXnajjgzPqvkd/.assets/images/voice-commands-particle-photon-2/vscode-1.jpg?fit=max&auto=format&n=5rOHXnajjgzPqvkd&q=85&s=861ef4d1765033ccd63f6c58acc09e5f" width="1600" height="858" data-path=".assets/images/voice-commands-particle-photon-2/vscode-1.jpg" />
</Frame>

In Visual Studio, at the lower right there will be a button to open the Properties file. Navigate to the unzipped folder, select `project.properties` and select "Yes, I trust confirmation".

The `src/main.cpp` code included in the zip file detects the trained keyword, and prints predictions over serial console. So we need to add some code to control the Relay.

We will open `src/main.cpp` and add the following:

```
// Before Setup function

float myLimit=0.8; // the limit to detect the word
int machineOn=0; // machine current state
```

and

```
// Inside Setup function

pinMode(3, OUTPUT); // set pin 3 to control the Relay Module
```

Then, inside the loop we will add this code to control the Relay. In this case, the label contains the keyword "muted" instead of "machine", as I was exploring audio output. If you are going to use another label, just change the word "muted" to the keyword contained in your own label.

```
 for (size_t ix = 0; ix < EI_CLASSIFIER_LABEL_COUNT; ix++) {
 	if (strstr(result.classification[ix].label, "muted") && result.classification[ix].value > detectionLimit) {
 		if (machineOn==1){
 			ei_printf(" - Turning the machine off");
 			digitalWrite(3, HIGH);
 			machineOn=0;
 		}
 		else{
 			ei_printf(" - Turning the machine on");
 			digitalWrite(3, LOW);
 			machineOn=1;
 		}
 	}
```

> Note: you can also download the `main.cpp` file from [https://github.com/ronibandini/Photon2VoiceCommand](https://github.com/ronibandini/Photon2VoiceCommand) to make sure you have everything entered correctly.

Now press Ctrl+Shift+P to bring up the Particle menu again, and this time select "Particle: Configure Project for Device".  Select deviceOS\@5.5.0, board P2, and ESC for device name.

> Note: if you get a Microphone library not found, press Ctrl+Shift+P, install the 'Microphone\_PDM\@0.0.2' library.

Finally, bring up the Particle menu again with Ctrl+Shift+P and select "Particle: Flash application and device, local" (For Windows, it will take around 5 minutes to flash).

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5rOHXnajjgzPqvkd/.assets/images/voice-commands-particle-photon-2/vscode-2.jpg?fit=max&auto=format&n=5rOHXnajjgzPqvkd&q=85&s=5f137d420407afc131fb2629955674c4" width="1600" height="859" data-path=".assets/images/voice-commands-particle-photon-2/vscode-2.jpg" />
</Frame>

If you obtain an "Argument list too long" error during flashing, Particle Support recommends using Docker instead to build:

* [https://docs.particle.io/firmware/best-practices/firmware-build-options/#using-buildpack](https://docs.particle.io/firmware/best-practices/firmware-build-options/#using-buildpack)
* [https://docs.docker.com/desktop/install/windows-install/](https://docs.docker.com/desktop/install/windows-install/)

Another option is to use Mac or Linux. For the demo below, the `main.cpp` modifications were made following the work done by Particle for this example [https://docs.particle.io/getting-started/machine-learning/youre-muted](https://docs.particle.io/getting-started/machine-learning/youre-muted)

### Linux (Ubuntu) Installation

1. Install a lightweight Ubuntu, such as [Lubuntu](https://lubuntu.me/downloads)
2. Install [VSCode](https://code.visualstudio.com/docs/?dv=linux64_deb)
3. Open a Terminal window and execute: `sudo apt-get install libarchive-zip-perl` (this step is to avoid an error where crc32 tool is not found)
4. Click Ctrl+P: Extension Install and locate and install `particle.particle-vscode-pack` and press Enter.
5. Login with Particle credentials
6. Create a Project
7. Import the unzipped folder. Accept "Trust all"
8. Now click Ctrl+Shift+P, choose "Particle: Configure Project for Device", and choose deviceOS\@5.3.2, board P2
9. Bring up the Particle menu again with Ctrl+Shift+P and choose "Particle: Flash Application and Device, local"

## Demo Video

<iframe src="https://www.youtube.com/embed/8BHUCaMyceg" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Conclusion

Machine Learning not only facilitates the recognition of voice commands but also empowers the identification of distinct machine-generated sounds, enabling automatic shutdown in response to specific malfunction indicators. This functionality proves invaluable in enhancing operational safety and efficiency within industrial environments.

Moreover, the compact form factor and cost-effectiveness of boards like the Particle Photon 2, coupled with their ability to manage external devices, render them an enticing augmentation for various industries. They offer a gateway to harnessing the potential of ML-powered automation within diverse manufacturing settings.

## Contact

[https://www.instagram.com/ronibandini](https://www.instagram.com/ronibandini)

[https://twitter.com/RoniBandini](https://twitter.com/RoniBandini)

[https://bandini.medium.com](https://bandini.medium.com)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5rOHXnajjgzPqvkd/.assets/images/voice-commands-particle-photon-2/device.jpg?fit=max&auto=format&n=5rOHXnajjgzPqvkd&q=85&s=29af9466e7767d906fd8901d2d30df05" width="1333" height="1000" data-path=".assets/images/voice-commands-particle-photon-2/device.jpg" />
</Frame>


Built with [Mintlify](https://mintlify.com).