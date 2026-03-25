# Source: https://docs.edgeimpulse.com/projects/expert-network/elevator-passenger-counting-arduino-nicla-vision.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Elevator Passenger Counting - Arduino Nicla Vision

Created By: Nekhil R.

Public Project Link: [https://studio.edgeimpulse.com/public/109997/latest](https://studio.edgeimpulse.com/public/109997/latest)

## Project Demo

<iframe src="https://www.youtube.com/embed/yD8CJGDpgfY" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/IMG_2204.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=01a9cf714170b1d232f363da80d1c8bd" width="1500" height="1000" data-path=".assets/images/elevator-passenger-counting/IMG_2204.jpg" />
</Frame>

## Story

As elevators become more and more indispensable in people's lives, safety has become more of a concern. Overloading is an important contributing factor to elevator accidents. Most existing elevators use weight sensors to determine the total load in an elevator, and those systems can sometimes fail. Additionally, their maintenance is expensive.

To avoid such accidents, we are going to design a proof-of-concept device which can count passengers in real-time at high speed, and can give an alert if the number of people in an elevator is above a threshold.

This device can be attached anywhere in the elevator. And compared with existing technology, its implementation cost is low, and maintenance is easy.

## How does it work?

In this prototype, we only consider two floors, the ground floor and the 2nd floor. After all the passengers enter the elevator, someone needs to press the close button. Then we count the number of passengers, and if it is above the threshold the device will sound an alarm. Thus, some people can leave the elevator, before it will begin ascending. If the number of people detected is not above the threshold, the elevator will move on.

The threshold passenger limit can be set by the user in the code, and should be set based on the size and capacity of the elevator.

In addition to the overload alert, we also provide elevator statistics. This means that the device can upload the count in elevators with the specific time stamp to a database or spreadsheet for tracking. The count will be always updated after pressing the close button in the elevator.

One of the interesting aspects of this data is that it can be easily visualised by any graphs or charts. So, it can be useful for any person who analyses elevator usage and pedestrian movement.

Here is an example of the passenger count data coming from the device, when it is viewed in Excel.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/excel_data2.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=99f2196915520aa0e4f50e1ad168e9f1" width="717" height="1000" data-path=".assets/images/elevator-passenger-counting/excel_data2.jpg" />
</Frame>

Below are the various graphs generated from the above data.

#### Clustered Column

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/clustered_column.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=cab0d50f87cd5313d30e6155f262e381" width="1173" height="1000" data-path=".assets/images/elevator-passenger-counting/clustered_column.jpg" />
</Frame>

#### Line chart

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/line_chart.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=79ea44686792246eaae4b22818f0406a" width="1169" height="1000" data-path=".assets/images/elevator-passenger-counting/line_chart.jpg" />
</Frame>

#### Pie chart

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/pie_chart.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=a85ded113669d90fc320a02b0fbda9a1" width="1502" height="1000" data-path=".assets/images/elevator-passenger-counting/pie_chart.jpg" />
</Frame>

Consider the case of elevators in a shopping mall. By using this type of information, the mall owner or operator can easily add up elevators, and if the usage of an elevator is too high can make changes, such as adding capacity or redirecting pedestrians as needed.

## Nicla Vision

In this project, we are using the [Nicla Vision](https://store.arduino.cc/products/nicla-vision), a tiny AI board from Arduino. It features a 2MP color camera, and has the intelligence to process and extract useful information from anything it sees.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/IMG_2167.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=50383c7e296afad9de24f7b43cf8c8ee" width="1272" height="1000" data-path=".assets/images/elevator-passenger-counting/IMG_2167.jpg" />
</Frame>

## Data collection and Labeling

For the data collection, we mounted the board on a tripod and connected it to a laptop using a lengthy USB cable. The below image shows the data acquisition setup.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/IMG_2163.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=b5ca632f9fdf8db02250df0485a4e226" width="1600" height="985" data-path=".assets/images/elevator-passenger-counting/IMG_2163.jpg" />
</Frame>

The whole setup was on one end of the room and we actually stood on the opposite end. This allowed a good perspective for training data, teaching the Nicla to detect and count passengers.

You can follow this [tutorial](/hardware/boards/arduino-nicla-vision) to connect Nicla vision to Edge Impulse.

We captured 73 images and split them between Testing and Training. Our images contain only one person or two people at a time, but you could easily do more. Then we labeled each image one by one, and here we have only one class named "people".

## Impulse Design

This is the machine learning pipeline for this project:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/Impulse.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=114e862d7ece54b137d7b91f01ad598b" width="1600" height="681" data-path=".assets/images/elevator-passenger-counting/Impulse.jpg" />
</Frame>

To keep the model size small, we choose an image width and height of 96x96 pixels, and the resize mode to "Fit the shortest axis". After saving the impulse we moved onto the *Image* tab and chose "Grayscale" as the colour depth, and saved the parameters and generated features for our images.

The image below shows the generated features:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/feature_generation.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=d6c5430d955dbcaa49ce596701ec80ab" width="1076" height="1000" data-path=".assets/images/elevator-passenger-counting/feature_generation.jpg" />
</Frame>

## Model Training

Here is our Neural Network training settings and architecture for generating the model:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/NN_and_architecture.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=9f7f29e66dd9cb667fd3f222bc7074ab" width="929" height="1000" data-path=".assets/images/elevator-passenger-counting/NN_and_architecture.jpg" />
</Frame>

We only changed the training cycle from **60** to **70**. Further increasing a training cycle or learning rate can overfit the data, so we stuck to this.

For the Neural Network architecture, we used **FOMO (MobileNet V2 0.35)**. The results are great, achieving a bit over 95% accuracy for the model (using quantized int version).

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/Model_output.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=3f90da14c3b02da1f75e220f028f3241" width="1304" height="790" data-path=".assets/images/elevator-passenger-counting/Model_output.jpg" />
</Frame>

## Model Testing

It's time to test the model. First, we used the test data which we separated earlier and got around 84% accuracy. That is not great, but seems to be fine in this use case.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/testing.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=322054df7f5ac0627a8c352eaac7ab2c" width="1600" height="874" data-path=".assets/images/elevator-passenger-counting/testing.jpg" />
</Frame>

Now let's move on to the Live classification. Here we are testing 3 sample images captured from the Nicla vision and let's see how our model performs.

#### Test 1

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/test1.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=8a194ad4becd4a0b83599378e129c5a3" width="1600" height="969" data-path=".assets/images/elevator-passenger-counting/test1.jpg" />
</Frame>

#### Test 2

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/test2.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=d85d08c3d4d7b92e2d753608d35930d3" width="1600" height="963" data-path=".assets/images/elevator-passenger-counting/test2.jpg" />
</Frame>

#### Test 3

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/test3.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=b2422d13b244fd770324f8af7eb13d39" width="1600" height="993" data-path=".assets/images/elevator-passenger-counting/test3.jpg" />
</Frame>

In all our testing samples, the model performed very well, so we can go ahead and deploy it to the device.

## Deployment

Now we have our ML model, and it has been tested, so we need to deploy it to our Nicla Vision. We just created an Arduino library by pressing the Build button, and a Zip file will be downloaded.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/deploy.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=d04fea4e1906ff789e6ccac28a1bc675" width="1600" height="910" data-path=".assets/images/elevator-passenger-counting/deploy.jpg" />
</Frame>

Then we add that library to the Arduino IDE. Next, we modified the example sketch that is provided. You can find code and assets in this [GitHub Repository](https://github.com/Nekhil-haxh/Elevator_Passenger_Counting).

## Additional Hardware and Casing

In addition to the Nicla Vision, we used a buzzer and a LED to create an alarm.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/IMG_2150.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=f748aec8224d93e66ce5c93be1c1b235" width="1349" height="1000" data-path=".assets/images/elevator-passenger-counting/IMG_2150.jpg" />
</Frame>

But the output current of the Nicla (4.7 mA) is not enough to properly power up an LED and buzzer. So we used a 2N222A transistor to drive these devices. This required the use of an external power supply of 5V, in addition to the USB power supply for powering the Nicla Vision itself. A push button is also used, to check whether the door is closed or not.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/IMG_2178.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=f096ab4b93977964c878abc47f4ca720" width="1500" height="1000" data-path=".assets/images/elevator-passenger-counting/IMG_2178.jpg" />
</Frame>

Finally, we made a nice, tiny case for this device.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/IMG_2174.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=cc17a4df13491689b978ef4c21b03f87" width="1500" height="1000" data-path=".assets/images/elevator-passenger-counting/IMG_2174.jpg" />
</Frame>

Then we inserted each component into it:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/IMG_2213.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=da4c718ec6d3110cbd90c44421b675d5" width="1500" height="1000" data-path=".assets/images/elevator-passenger-counting/IMG_2213.jpg" />
</Frame>

Now, our device is ready to implement.

## TeraTerm

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/tera_term.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=f0a5a50c604c2b9b7d193e801b1e7c67" width="1600" height="884" data-path=".assets/images/elevator-passenger-counting/tera_term.jpg" />
</Frame>

We used TeraTerm to stream data from the Nicla Vision. The streaming data can be logged anywhere in any format. Here we proceeded with CSV format, so the file can be easily opened with Microsoft Excel.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/tera_term_log.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=8eec18e3d29abf523d58a78e5f5f7d3f" width="836" height="804" data-path=".assets/images/elevator-passenger-counting/tera_term_log.jpg" />
</Frame>

Make sure to check the box for *Timestamp* before logging the data.

The below image shows sample data streamed from our device, which is then opened in Excel.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/original_excel.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=647e802e6ced7d2257bd28fc64c79fbc" width="1600" height="847" data-path=".assets/images/elevator-passenger-counting/original_excel.jpg" />
</Frame>

We can easily generate graphical reports from this data by selecting that text. The below figure represents the line chart for the above data.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/countwithgraph.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=2659f2e6b41050abb1175f9d63212940" width="1600" height="702" data-path=".assets/images/elevator-passenger-counting/countwithgraph.jpg" />
</Frame>

There is a wide variety of options available and they are shown below.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/elevator-passenger-counting/options_available.jpg?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=42191c90ba05559da024486d2f0cb333" width="1060" height="1000" data-path=".assets/images/elevator-passenger-counting/options_available.jpg" />
</Frame>

## Conclusion

This device can be easily integrated and installed in an elevator, making it so that the elevator will only start when the passenger count is in the permissible range.

To reduce the cost of the unit, we can also try using an ESP32-EYE or similar microcontroller unit, instead of the Nicla Vision, though the quality and capability will need to be tested similar to how the Nicla was evaluated.


Built with [Mintlify](https://mintlify.com).