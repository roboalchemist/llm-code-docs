# Source: https://docs.edgeimpulse.com/projects/expert-network/voice-controlled-power-plug-nicla-voice.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Voice Controlled Power Plug with Syntiant NDP120 (Nicla Voice)

Created By: Jallson Suryo

Public Project Link: [https://studio.edgeimpulse.com/public/297564/latest](https://studio.edgeimpulse.com/public/297564/latest)

GitHub Repo: [https://github.com/Jallson/Voice\_Controlled\_PowerPlug](https://github.com/Jallson/Voice_Controlled_PowerPlug)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5rOHXnajjgzPqvkd/.assets/images/voice-controlled-power-plug-nicla-voice/Image00.png?fit=max&auto=format&n=5rOHXnajjgzPqvkd&q=85&s=0983f282a1e56e9b8ec8246d8be9c1bf" width="1219" height="1000" data-path=".assets/images/voice-controlled-power-plug-nicla-voice/Image00.png" />
</Frame>

## Introduction

Can you imagine Amazon Alexa without the cloud?

For most services, adding voice means adding an internet connection and it means extra expense, privacy and security concerns, and you need to install an app (or access to the web) for everything in your home. Another problem is the time delay between a voice command being given, the command being sent to a cloud server and then back to the device for execution, creating a poor user experience.

## Our Solution

A power-plug which can be controlled using voice commands, with no connection to the internet. By using a machine learning model embedded in a microcontroller that has been trained to recognize several commands, which are then passed to relays which will turn the power on or off at each socket according to the issued command, instantly. Practicality, privacy concerns, and cost-effectiveness are the goals of this Non-IoT Voice Controlled Power Plug project.

## Description

This project takes advantage of Edge Impulse's Syntiant audio processing block that extracts time and frequency features from a signal, specific to the Syntiant NDP120 accelerator included in the Nicla Voice. The NDP120 is ideal for always-on, low-power speech recognition applications with the “find posterior parameters” feature that will only react to the specified keywords.

Devices with an embedded ML model will accept voice commands, but won't need a WIFI or Bluetooth connection. All processing is done locally on the device, so you can directly tell a lamp, air conditioner, or TV to turn on or off without Alexa or Siri, or any digital assistant speaker/hub.

This project will use relays and a power strip connected to various appliances such as a lamp, fan, TV, etc. An Arduino Nicla Voice with embedded ML model has been trained to recognize various keywords like: `one`, `two`, `three`, `four`, `on`, and `off` is the center of the decision process. From the Nicla Voice we use the I2C protocol which is connected to an Arduino Pro Micro to carry out voice commands from the Nicla Voice, and forwarded to the relays which control power sockets.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5rOHXnajjgzPqvkd/.assets/images/voice-controlled-power-plug-nicla-voice/Image01.png?fit=max&auto=format&n=5rOHXnajjgzPqvkd&q=85&s=0c13b88f0ecdf535af3d373e8fd85589" width="663" height="595" data-path=".assets/images/voice-controlled-power-plug-nicla-voice/Image01.png" />
</Frame>

### Hardware Requirements:

* Arduino Nicla Voice (with Syntiant NDP120)
* Any microcontroller or Arduino (I use Pro Micro)
* 5V Relay (4pcs)
* Breadboard
* Cable jumper
* Cable for 110/220V
* Powerstrip (4 sockets)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5rOHXnajjgzPqvkd/.assets/images/voice-controlled-power-plug-nicla-voice/Image02.png?fit=max&auto=format&n=5rOHXnajjgzPqvkd&q=85&s=99d166a70b9609c6068c18064fe28382" width="1600" height="986" data-path=".assets/images/voice-controlled-power-plug-nicla-voice/Image02.png" />
</Frame>

### Software & Online Services:

* Edge Impulse Studio (Enterprise account or Free Trial for more than 4 hours of training data)
* Arduino IDE
* Terminal

## Steps

### 1. Upload or Collect Audio Data

Before we start, we need to install the Arduino CLI and Edge Impulse tooling on our computer.

You can follow [this guide](/hardware/boards/arduino-nicla-voice) to get everything installed.

Open [https://studio.edgeimpulse.com](https://studio.edgeimpulse.com) in a browser, and sign in, or create a new account if you do not have one. Click on *New project*, then in *Data acquisition*, click on the *Upload Data* icon for uploading .wav files (e.g. from Kaggle, Google Speech Commands Dataset, etc.). Other methods to collect data are from devices such as a connected smartphone with QR code link, or a connected Nicla Voice with Edge Impulse audio firmware flashed to it. For ease of labelling, when collecting or uploading data, fill in the name according to the desired label, for example `one`, `two`, `three`, `on`, `off`, or `zzz` for words or sound that can be ignored.

> Note: With over 4 hours of audio data, multiple classes and higher performance settings to build the model, this project uses an [Enterprise account](https://edgeimpulse.com/product) for more capable and faster results.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5rOHXnajjgzPqvkd/.assets/images/voice-controlled-power-plug-nicla-voice/Image03.png?fit=max&auto=format&n=5rOHXnajjgzPqvkd&q=85&s=ab3de24f379f5bb3d02441a221382925" width="1600" height="786" data-path=".assets/images/voice-controlled-power-plug-nicla-voice/Image03.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5rOHXnajjgzPqvkd/.assets/images/voice-controlled-power-plug-nicla-voice/Image04.png?fit=max&auto=format&n=5rOHXnajjgzPqvkd&q=85&s=4065aa5476abb891402f9fc79336b8cf" width="929" height="1000" data-path=".assets/images/voice-controlled-power-plug-nicla-voice/Image04.png" />
</Frame>

### 2. Split and Balancing

Click on a data sample that was collected, then click on the 3 dots to open the menu, and finally choose *Split sample*. Set the segment length to 1000 ms (1 second), or add segments manually, then click **Split**. Repeat this process until all samples are labeled in 1 second intervals. Make sure the comparison between one, two, three, four, on, off and unknown data is quite balanced, and the ratio between Training and Test data is around 80/20.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5rOHXnajjgzPqvkd/.assets/images/voice-controlled-power-plug-nicla-voice/Image05.png?fit=max&auto=format&n=5rOHXnajjgzPqvkd&q=85&s=2e058ba3a7ceb0f762237583e771bd59" width="1138" height="722" data-path=".assets/images/voice-controlled-power-plug-nicla-voice/Image05.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5rOHXnajjgzPqvkd/.assets/images/voice-controlled-power-plug-nicla-voice/Image06.png?fit=max&auto=format&n=5rOHXnajjgzPqvkd&q=85&s=2d815a92569cc0c49ca03424159525dc" width="674" height="630" data-path=".assets/images/voice-controlled-power-plug-nicla-voice/Image06.png" />
</Frame>

### 3. Train and Build the Model (Syntiant)

Choose *Create Impulse*, set *Window size* to 968ms, then add an *Audio (Syntiant)* Processing block, and choose *Classifier* for the Learning block, then **Save Impulse**. In the Syntiant parameters, choose **log-bin (NDP120/200)** then click **Save**. Set the training to around 50 cycles with 0.0005 Learning rate, and choose *Dense Network* with Dropout rate around 0.5, then click **Start training**. It will take a short while, but you can see the progress of the training on the right. If the results show a figure of around 80% accuracy upon completion, then we can most likely proceed to the next stage.

Now we can test the model in *Live classification*, or choose *Model testing* to test with the data that was set aside earlier (the 80/20 split), and click **Classify all**. If the result is quite good -- again around 80% accuracy, then we can move to the next step -- Deployment.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5rOHXnajjgzPqvkd/.assets/images/voice-controlled-power-plug-nicla-voice/Image07.png?fit=max&auto=format&n=5rOHXnajjgzPqvkd&q=85&s=5ea60db7d0e5572800dd5d8e516a7f46" width="1120" height="566" data-path=".assets/images/voice-controlled-power-plug-nicla-voice/Image07.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/5rOHXnajjgzPqvkd/.assets/images/voice-controlled-power-plug-nicla-voice/Image08.png?fit=max&auto=format&n=5rOHXnajjgzPqvkd&q=85&s=5258fa709b8c3de53ed1ecda8b281176" width="983" height="866" data-path=".assets/images/voice-controlled-power-plug-nicla-voice/Image08.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/voice-controlled-power-plug-nicla-voice/Image09.png?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=ef4bfd5e61aae29276787e1594c9cadf" width="1320" height="813" data-path=".assets/images/voice-controlled-power-plug-nicla-voice/Image09.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/voice-controlled-power-plug-nicla-voice/Image10.png?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=442ba755ec75b5dd2fcf4a41e857a207" width="1299" height="910" data-path=".assets/images/voice-controlled-power-plug-nicla-voice/Image10.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/voice-controlled-power-plug-nicla-voice/Image11.png?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=7e4ab587ae4cf577b71423c4edfdf521" width="1308" height="781" data-path=".assets/images/voice-controlled-power-plug-nicla-voice/Image11.png" />
</Frame>

### 4. Deploy to Nicla Voice

For a Syntiant NDP device like the Nicla Voice, we can configure the [Posterior parameters](/tutorials/hardware/syntiant-ndp-keyword-spotting#8-deploying-to-your-device) (in this case tick all labels except `zzz`). To run your Impulse locally on the Arduino Nicla Voice, you should select the Nicla Voice in the *Deployment* tab, then click **Build**. The binary firmware will start building and automatically download to your computer once it is complete, and a video with instructions on how to flash the firmware will pop-up. [Flash this firmware to the Nicla Voice](/tutorials/hardware/syntiant-ndp-keyword-spotting#9-flashing-the-device) as instructed. Once complete, Now you can run this model in a Terminal for live classification.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/voice-controlled-power-plug-nicla-voice/Image12.png?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=46789a5842d0fb3077252d18c3ac19c8" width="781" height="684" data-path=".assets/images/voice-controlled-power-plug-nicla-voice/Image12.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/voice-controlled-power-plug-nicla-voice/Image13.png?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=f3aa7e8840a5f45c28f7b4247b548465" width="792" height="518" data-path=".assets/images/voice-controlled-power-plug-nicla-voice/Image13.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/voice-controlled-power-plug-nicla-voice/Image14.png?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=d3f865e5af188139f12de767535dc24c" width="791" height="736" data-path=".assets/images/voice-controlled-power-plug-nicla-voice/Image14.png" />
</Frame>

### 5. Upload the Arduino Code

Because there are two MCU's in this solution, two separate applications are needed:

#### Nicla Voice

Upload this code [https://github.com/Jallson/Voice\_Controlled\_PowerPlug/blob/main/relayvoice\_niclavoice.ino](https://github.com/Jallson/Voice_Controlled_PowerPlug/blob/main/relayvoice_niclavoice.ino) to the Arduino Nicla Voice using the Arduino IDE. This code will override the existing application code in the Nicla Voice's MCU, but not the machine learning model on the NDP120. The code basically sends a byte via I2C every time a keyword is detected, the value of the byte will depend on the keyword detected.

#### Pro Micro

Upload this code [https://github.com/Jallson/Voice\_Controlled\_PowerPlug/blob/main/relayvoice\_promicro.ino](https://github.com/Jallson/Voice_Controlled_PowerPlug/blob/main/relayvoice_promicro.ino) to the Pro Micro using the Arduino IDE. This application receives the incoming byte via I2C and will switch on or off the relay based on the values of the data received from the Nicla Voice.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/voice-controlled-power-plug-nicla-voice/Image15.png?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=954a4a3a418b52e4a5886150894a02bf" width="1360" height="975" data-path=".assets/images/voice-controlled-power-plug-nicla-voice/Image15.png" />
</Frame>

## Demo

<iframe src="https://www.youtube.com/embed/9PRjhA38jBE" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Conclusion

Finally we succeeded in making this **Non IoT** Voice Controlled Power-plug idea a reality and implemented in a home appliances setting. I believe in the future this kind of non-IoT smart home system will be widely implemented, and could be built-in to every home appliance with specific keywords. Concerns about privacy, security, as well as practicality and energy efficiency can be achieved for a more sustainable future.


Built with [Mintlify](https://mintlify.com).