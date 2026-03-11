# Source: https://docs.edgeimpulse.com/projects/expert-network/smart-smoke-alarm-arduino-nano-33.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Smart Smoke Alarm - Arduino Nano 33

Created By: Nick Bild

Public Project Link: [https://studio.edgeimpulse.com/public/142241/latest](https://studio.edgeimpulse.com/public/142241/latest)

## Project Demo

<iframe src="https://www.youtube.com/embed/IZDHoQUmEg8" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Intro

Thousands of people die each year in fires in both residential and commercial settings. Offices, warehouses, industrial, and manufacturing plants account for well over 1,000 fire-related injuries in the US annually. First responders work hard to rescue individuals that are either trapped in or incapacitated by a building fire, but without knowing where to look, they may not find them in time.

Smart Smoke Alarm attempts to solve this problem by providing firefighters with precise information about the locations of persons trapped inside a burning building. This device uses a thermal camera and a machine learning classifier to identify people in the event that the smoke detector is tripped. By using thermal imaging, it is possible to recognize people in the dark and through smoke. Location information is wirelessly transmitted to a remote server where it could be viewed by first responders on the scene to help them focus their efforts.

<Frame caption="">
  <img src="https://raw.githubusercontent.com/nickbild/smart_smoke_alarm/main/media/assembly_case_close_annotated_sm.jpg" />
</Frame>

## Hardware Requirements

* 1 x Adafruit MLX90640 24x32 IR Thermal Camera (110 Degree FoV)
* 1 x Adafruit Feather M4 Express
* 1 x Arduino Nano 33 IoT
* 1 x 350 mAh or greater LiPo battery
* 1 x Piezo buzzer
* 1 x Push button
* 1 x 10K ohm resistor
* 1 x 3D printed case (optional)

## Software Requirements

* Edge Impulse Studio
* Arduino IDE

## How It Works

There are two development boards — an Arduino Nano 33 IoT and an Adafruit Feather M4 Express. The Feather M4 Express handles capturing measurements from the thermal camera and provides the processing power to run the machine learning algorithm that was developed with Edge Impulse. The Nano 33 IoT provides WiFi for wireless communications, and also serves as a simulated smoke detector.

<Frame caption="">
  <img src="https://raw.githubusercontent.com/nickbild/smart_smoke_alarm/main/media/assembly_boards_sm.jpg" />
</Frame>

Since smoke detection is already a solved problem, and I didn't want to have to start a fire to test my device, I simulated this function with a push button on the side of the case. Pressing this button starts a simulated smoke alarm which turns on an audible alert using a piezo buzzer. This also triggers the thermal camera to start capturing data and passing it to a neural network classifier that was trained to detect people by their heat signatures. If a person is detected during an active alarm, that fact is communicated to a [remote web API](https://github.com/nickbild/smart_smoke_alarm/blob/main/alarm_api.py) via WiFi. The API records the location and timestamp in a database that could be used to identify where rescue efforts should be focused.

The hardware was placed in a [3D printed case](https://github.com/nickbild/smart_smoke_alarm/blob/main/case.stl) that was mounted near the ceiling where it has a good view of the entire room.

<Frame caption="">
  <img src="https://raw.githubusercontent.com/nickbild/smart_smoke_alarm/main/media/assembly_case_close_sm.jpg" />
</Frame>

## Data Preparation

An [Arduino sketch](https://github.com/nickbild/smart_smoke_alarm/tree/main/smoke_detector_data_collection) was created to capture thermal images to train the neural network. I captured measurements for two classes — person and empty room. For the person class, I took many images of myself standing, sitting, walking, and otherwise moving about the room. The empty room class is self-explanatory. In total, I collected 189 'person' images, and 130 'empty' images. These measurements were processed with a simple [Python script](https://github.com/nickbild/smart_smoke_alarm/blob/main/parse_training_data.py) that formatted the data as CSV files, then they were uploaded to my [Edge Impulse project](https://studio.edgeimpulse.com/public/142241/latest) using the data acquisition tool.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-smoke-alarm/ei_data_sm.jpg?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=a4820d86c3f035b35e575e87cb84069a" width="1024" height="552" data-path=".assets/images/smart-smoke-alarm/ei_data_sm.jpg" />
</Frame>

To give a better idea of what the thermal camera "sees," I wrote another [Arduino sketch](https://github.com/nickbild/smart_smoke_alarm/tree/main/smoke_detector_rgb) that converts the measurements into RGB values, which are then transformed into PNG images with [this script](https://github.com/nickbild/smart_smoke_alarm/blob/main/rgb2png.py). A few examples follow.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/smart-smoke-alarm/me_standing2_lg.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=986ba65f0689022c70ccafc9abd1895c" width="640" height="480" data-path=".assets/images/smart-smoke-alarm/me_standing2_lg.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/smart-smoke-alarm/me_standing_lg.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=8438b1e4e9b52284314488b887fb14d2" width="640" height="480" data-path=".assets/images/smart-smoke-alarm/me_standing_lg.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/smart-smoke-alarm/me_working_at_desk_lg.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=43c9729ce4ec26b9ea2a76bea6c0f2c0" width="640" height="480" data-path=".assets/images/smart-smoke-alarm/me_working_at_desk_lg.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/smart-smoke-alarm/me_sitting_lg.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=7db8ae86b612285489e8775e7678c015" width="640" height="480" data-path=".assets/images/smart-smoke-alarm/me_sitting_lg.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/G6r7oAnu84JpYZaM/.assets/images/smart-smoke-alarm/me_bending_down_lg.jpg?fit=max&auto=format&n=G6r7oAnu84JpYZaM&q=85&s=c6cd240ede7f78771d06c105a5032b7f" width="640" height="480" data-path=".assets/images/smart-smoke-alarm/me_bending_down_lg.jpg" />
</Frame>

## Building the ML Model

Building the model turned out to be the simplest part of the entire project. I created a new impulse that forwards the raw thermal image data into a neural network classification block. I kept the default model design and hyperparameters and clicked the "Start training" button. Surprisingly, the classification accuracy was reported as being at 100% right off the bat.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-smoke-alarm/ei_nn_sm.jpg?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=f6b8338759de8af8f3ae89d604a346e1" width="1024" height="551" data-path=".assets/images/smart-smoke-alarm/ei_nn_sm.jpg" />
</Frame>

That sounded too good to be true, so I used the model testing tool as a secondary validation that uses 20% of the uploaded data that was not included in the training process. That showed an average classification accuracy of 96.88%, confirming that the model is working very well. There is really no need to improve on this for a proof of concept, so I moved on to loading this model onto my hardware.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-smoke-alarm/ei_model_testing_sm.jpg?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=d4189c61fbfb24109d4053854ebda5b5" width="1024" height="557" data-path=".assets/images/smart-smoke-alarm/ei_model_testing_sm.jpg" />
</Frame>

## Deploying the Model

Edge Impulse offers many options for deployment, but in my case the best option was the "Arduino library" download. This packaged up the entire classification pipeline as a compressed archive that I could import into Arduino IDE, then modify as needed to add my own logic (like to communicate with the Nano 33 IoT to send messages over WiFi, for example). That sketch can be found [here](https://github.com/nickbild/smart_smoke_alarm/tree/main/smoke_detector_ei). And the sketch that runs the simulated smoke detector on the Nano 33 IoT can be found [here](https://github.com/nickbild/smart_smoke_alarm/tree/main/smoke_detector_companion).

<Frame caption="">
  <img src="https://raw.githubusercontent.com/nickbild/smart_smoke_alarm/main/media/installed_off_sm.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://raw.githubusercontent.com/nickbild/smart_smoke_alarm/main/media/installed_off_distance_sm.jpg" />
</Frame>

## Conclusion

This device worked surprisingly well in my real world testing. In dozens of tests I didn't have a single false positive or false negative. While my testing was done in my relatively small home office, I expect this method would scale up to cover a large office space, factory floor, or warehouse with similar accuracy. To cover a larger area a higher resolution thermal camera would be needed, however. Feel free to have a look around my public [Edge Impulse project](https://studio.edgeimpulse.com/public/142241/latest) if you want to experiment with this idea yourself. Even if you don't have the same hardware, it would be pretty trivial to deploy it to alternate platforms.


Built with [Mintlify](https://mintlify.com).