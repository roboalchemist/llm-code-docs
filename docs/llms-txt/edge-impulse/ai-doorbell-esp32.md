# Source: https://docs.edgeimpulse.com/projects/expert-network/ai-doorbell-esp32.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM-powered Doorbell - ESP32

Created By: Roni Bandini

Public Project Link: [https://studio.edgeimpulse.com/public/541658/latest](https://studio.edgeimpulse.com/public/541658/latest)

GitHub Repo: [https://github.com/ronibandini/aicamdoorbell](https://github.com/ronibandini/aicamdoorbell)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ro0OmglK1rhOymd3/.assets/images/ai-doorbell-esp32/cover.jpg?fit=max&auto=format&n=ro0OmglK1rhOymd3&q=85&s=c928a0e744fbf68a7c9f6b95edc4da02" width="1920" height="2560" data-path=".assets/images/ai-doorbell-esp32/cover.jpg" />
</Frame>

## Intro

Build an AI-powered doorbell with computer vision face recognition, and LLM-based decision-making.

## Parts Required

For this project, I use the ESP32S3 AI Camera module 1.0 (DFR1154) by DFRobot and a microSD card.  The AI Camera Module is a 1.5" x 1.5" ESP32-based board featuring:

* A 2MP OV3660 wide IR camera
* Onboard I2S PDM microphone
* microSD card slot
* Built-in LEDs
* An amplifier and micro speaker

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/en149vbvJlDSUXiw/.assets/images/ai-doorbell-esp32/dfrobot-esp32s3.jpg?fit=max&auto=format&n=en149vbvJlDSUXiw&q=85&s=8fcd62e00df658c4696c8e77526cac67" width="1920" height="2548" data-path=".assets/images/ai-doorbell-esp32/dfrobot-esp32s3.jpg" />
</Frame>

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/en149vbvJlDSUXiw/.assets/images/ai-doorbell-esp32/hardware.jpg?fit=max&auto=format&n=en149vbvJlDSUXiw&q=85&s=74e3de70341b6baca74982128ba63e9a" width="1450" height="621" data-path=".assets/images/ai-doorbell-esp32/hardware.jpg" />
</Frame>

## Workflow

1. The module captures pictures at regular intervals.
2. Each picture is sent to a local ML model trained with Edge Impulse.
3. The model returns a score answering: "Does this picture contain a face?"
4. If the result passes a configurable threshold, a greeting is played asking for the visitor's name.
5. The visitor's answer is recorded and transcribed using OpenAI Whisper.
6. The transcription is sent to ChatGPT, which decides whether to open the door (via relay) or notify remotely via Telegram.

Using ChatGPT adds flexibility — for instance, my name was transcribed as Ronnie Bandini, but the LLM still recognized that I had an appointment. It also allows decision-making based on complex, unforeseen logic.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/en149vbvJlDSUXiw/.assets/images/ai-doorbell-esp32/workflow.jpg?fit=max&auto=format&n=en149vbvJlDSUXiw&q=85&s=73b4f0bbf4fbd077c12fee8a2c1b4ca1" width="1024" height="768" data-path=".assets/images/ai-doorbell-esp32/workflow.jpg" />
</Frame>

## Face Detection (Edge Impulse)

Why Edge Impulse? Because it simplifies the full ML workflow — data collection, labeling, training, testing, deployment — and even generates inference code and an optimized model for embedded systems.

### Steps:

1. Create a free developer account at Edge Impulse.
2. In the dashboard, ensure Bounding Boxes is selected as the labeling method.
3. Upload \~100 images containing faces. Draw a square around each face and label it as "face"

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/en149vbvJlDSUXiw/.assets/images/ai-doorbell-esp32/dataset.jpg?fit=max&auto=format&n=en149vbvJlDSUXiw&q=85&s=beedd45c9901227aa94e16953ac22473" width="2874" height="1517" data-path=".assets/images/ai-doorbell-esp32/dataset.jpg" />
</Frame>

4. Create an Impulse with:

* 96x96 px
* Object Detection
* 1 output feature

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/en149vbvJlDSUXiw/.assets/images/ai-doorbell-esp32/impulse.jpg?fit=max&auto=format&n=en149vbvJlDSUXiw&q=85&s=c123f2041ad7a82c04d6e9402de1ec7f" width="2878" height="1526" data-path=".assets/images/ai-doorbell-esp32/impulse.jpg" />
</Frame>

5. Under Image, choose grayscale for color depth, then generate features.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/en149vbvJlDSUXiw/.assets/images/ai-doorbell-esp32/features.jpg?fit=max&auto=format&n=en149vbvJlDSUXiw&q=85&s=3b943cecf73ca937f022bdfc549e4caa" width="2872" height="1518" data-path=".assets/images/ai-doorbell-esp32/features.jpg" />
</Frame>

6. Train the model. (In my case, 70 cycles and a learning rate of 0.00015 yielded a 0.77 F1 score — your mileage may vary.)

Note: You can skip training by cloning my project or using the provided trained model [https://github.com/ronibandini/aicamdoorbell/blob/main/Person\_Detection\_inferencing.zip](https://github.com/ronibandini/aicamdoorbell/blob/main/Person_Detection_inferencing.zip)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/en149vbvJlDSUXiw/.assets/images/ai-doorbell-esp32/training.jpg?fit=max&auto=format&n=en149vbvJlDSUXiw&q=85&s=f81e1b99528e34c5c2dbf88004a5ec29" width="2878" height="1522" data-path=".assets/images/ai-doorbell-esp32/training.jpg" />
</Frame>

## Model Deployment

1. Test the model using unseen images that were set aside during data collection.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/en149vbvJlDSUXiw/.assets/images/ai-doorbell-esp32/testing.jpg?fit=max&auto=format&n=en149vbvJlDSUXiw&q=85&s=94ccf88ede46be1783738a24e861e05c" width="2880" height="1519" data-path=".assets/images/ai-doorbell-esp32/testing.jpg" />
</Frame>

2. On Deployment, choose an Arduino Library and click Build to download the trained model.

3. Unzip it into Documents/Arduino/libraries.

4. Replace `depthwise_conv.cpp` and `conv.cpp` in src/edge-impulse-sdk/tensorflow/lite/micro/kernels with files from [https://github.com/ronibandini/aicamdoorbell/tree/main/edgeimpulse](https://github.com/ronibandini/aicamdoorbell/tree/main/edgeimpulse)

5. Edit `aibell1.ino` to include the model header:

```
#include <persondetection_inferencing.h>
```

## Audio Setup

1. Connect the micro speaker to the connector

2. Copy WAV files to the microSD card and insert it into the AI Cam.

3. To customize audio, use [ElevenLabs TTS](https://elevenlabs.io/app/speech-synthesis/text-to-speech).

4. Export MP3 and convert to WAV, 16kHz.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/en149vbvJlDSUXiw/.assets/images/ai-doorbell-esp32/audio-setup.jpg?fit=max&auto=format&n=en149vbvJlDSUXiw&q=85&s=d0f98c7c69bf873e40533d22ebccbd18" width="2880" height="1696" data-path=".assets/images/ai-doorbell-esp32/audio-setup.jpg" />
</Frame>

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/en149vbvJlDSUXiw/.assets/images/ai-doorbell-esp32/speaker.jpg?fit=max&auto=format&n=en149vbvJlDSUXiw&q=85&s=67a2495efc48cd0ea4d75399f4a48192" width="1920" height="2560" data-path=".assets/images/ai-doorbell-esp32/speaker.jpg" />
</Frame>

## Software Setup

1. Install the **Universal Telegram Bot** library in Arduino IDE.

2. Get an OpenAI API key (for Whisper and GPT) at: [https://platform.openai.com/settings/organization/api-keys](https://platform.openai.com/settings/organization/api-keys)

3. Get a Telegram bot token from: [https://core.telegram.org/bots/tutorial](https://core.telegram.org/bots/tutorial)

4. Edit the following in `aibell1.ino`:

```
threshold = 0.7;                 // face detection threshold
const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASS";
const char* openai_api_key = "sk-proj-…";
```

5. Edit system instructions:

```
systemMessage["content"] = "You are a receptionist at an office. Today, only Roni Bandini and John Smith are allowed to enter. If a visitor's name matches either of them — even with spelling variations — greet them with: "Welcome, push the door". For all other visitors, respond with: "Sorry, I cannot let you in.";
```

6. Upload Settings:

* Board: ESP32S3 Dev Module
* USB: Correct USB port
* Options: USB CDC On Boot
* Partition: 16MB Flash (3MB app, 9.9MB FS)
* Flash mode: QIO
* PSRAM: OPI

## Serial Monitor

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/en149vbvJlDSUXiw/.assets/images/ai-doorbell-esp32/serial.jpg?fit=max&auto=format&n=en149vbvJlDSUXiw&q=85&s=871976763d389187a39dc2e53794e516" width="2880" height="1380" data-path=".assets/images/ai-doorbell-esp32/serial.jpg" />
</Frame>

## Door Relay

The AI module doesn't have header pins, but you can still connect a relay using the Gravity cable, which exposes:

* VCC
* GND
* GPIO 44
* GPIO 43

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/en149vbvJlDSUXiw/.assets/images/ai-doorbell-esp32/relay.jpg?fit=max&auto=format&n=en149vbvJlDSUXiw&q=85&s=ad66a3d62efad14b5a7912846e008144" width="1920" height="2559" data-path=".assets/images/ai-doorbell-esp32/relay.jpg" />
</Frame>

Use Dupont male-to-female cables to connect your relay — no soldering needed.

## Enclosure

Download the 3D printable case from: [https://cults3d.com/en/3d-model/gadget/aibell](https://cults3d.com/en/3d-model/gadget/aibell)

Print in PLA. No supports needed.

Optional: Pause mid-print to change filament color for a custom cover.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/en149vbvJlDSUXiw/.assets/images/ai-doorbell-esp32/enclosure.jpg?fit=max&auto=format&n=en149vbvJlDSUXiw&q=85&s=5db170398c4e46e04152b719090a0ece" width="2878" height="1650" data-path=".assets/images/ai-doorbell-esp32/enclosure.jpg" />
</Frame>

## Final Notes

A tiny 1.5" x 1.5" board can:

* Run an embedded ML model
* Play WAV files
* Record audio
* Transcribe it with Whisper
* Query a remote LLM
* Control hardware (like a relay)
* Send notifications over Telegram

## Room for Improvement

* Replace fixed audio responses with dynamic ones using OpenAI TTS.
* Route transcriptions to [n8n](https://n8n.io/) to check:
  \-- Calendar availability
  \-- Authorized visitor list (e.g. Google Sheets)
  \-- Complex workflows

## Links

ESP32S3 software and ML model: [https://github.com/ronibandini/aicamdoorbell](https://github.com/ronibandini/aicamdoorbell)
Edge Impulse Project: [https://studio.edgeimpulse.com/studio/541658](https://studio.edgeimpulse.com/studio/541658)
ESP32S3 AI Cam: [https://www.dfrobot.com/product-2899.html](https://www.dfrobot.com/product-2899.html)

## Contact

Roni Bandini
[https://www.linkedin.com/in/ronibandini](https://www.linkedin.com/in/ronibandini/)
[https://www.instagram.com/ronibandini](https://www.instagram.com/ronibandini)
[https://x.com/RoniBandini](https://x.com/RoniBandini)


Built with [Mintlify](https://mintlify.com).