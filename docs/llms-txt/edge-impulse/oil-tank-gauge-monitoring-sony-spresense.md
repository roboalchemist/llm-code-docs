# Source: https://docs.edgeimpulse.com/projects/expert-network/oil-tank-gauge-monitoring-sony-spresense.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Oil Tank Measurement Using Computer Vision - Sony Spresense

Created By: Mithun Das

Public Project Link: [https://studio.edgeimpulse.com/public/105298/latest](https://studio.edgeimpulse.com/public/105298/latest)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/oil-tank-gauge-monitoring/intro.jpg?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=a08e87f2bd9b58a88c1f0d8d2aaab7c4" width="900" height="675" data-path=".assets/images/oil-tank-gauge-monitoring/intro.jpg" />
</Frame>

## Heating Oil And Usage

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/oil-tank-gauge-monitoring/intro-2.jpg?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=fabcbc717d7a48b6c1c4bc5ecf667c7c" width="740" height="413" data-path=".assets/images/oil-tank-gauge-monitoring/intro-2.jpg" />
</Frame>

Heating oil is mainly used for space heating. Some homes and residential commercial buildings also use heating oil to heat water but in much smaller amounts than what they use for space heating. Because cold weather affects heating demand, most heating oil use occurs during the heating season—October through March.

In the winter of 2020–2021, about 5.3 million households in the United States used heating oil (distillate fuel oil) as their main space heating fuel, and about 82% of those households were in the U.S. Northeast.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/oil-tank-gauge-monitoring/intro-3.jpg?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=dfcdbcef6173d8c51ec1829652710139" width="665" height="555" data-path=".assets/images/oil-tank-gauge-monitoring/intro-3.jpg" />
</Frame>

Heating oil is also used in many countries in Europe. [Source](https://www.upei.org/images/UPEI_Heating_Oil_Fiche_FIN.pdf)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/oil-tank-gauge-monitoring/intro-4.jpg?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=911e762ef1b2fde63895faea1497b61f" width="740" height="500" data-path=".assets/images/oil-tank-gauge-monitoring/intro-4.jpg" />
</Frame>

## Operational Inefficiencies

Usually heating oil companies deliver the oil in a truck. Many heating oil companies monitor your usage to determine when you will need an oil delivery again. These calculations are performed using "degree days" and a K-factor. The degree days calculation adds the high and low temperatures on a given day, divides it by two, and subtracts 65 from the quotient. This number is added to your home’s K-factor.

The K-factor determines “degree days per gallon” (think something similar to “miles per gallon” here) to estimate how quickly you use heating oil. Over time, our heating oil company can settle on a relatively stable K-factor for your home. We can then calculate your next delivery using your unique K-factor and our own calculations.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/oil-tank-gauge-monitoring/intro-5.jpg?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=71623db4ba48bf7daa42a454aad85e30" width="740" height="489" data-path=".assets/images/oil-tank-gauge-monitoring/intro-5.jpg" />
</Frame>

But this calculation is not accurate all the time. Family can go on vacation, resulting in less oil consumption, or relatives visiting during holiday season could result in more oil consumption.

Okay, so what's the big deal?

**Extra cost and additional CO2 emissions** - If the delivery is made when the tank is still 3/4 full, it's a waste of money and extra emission of CO2 in the environment. Delivery during cold weather is expensive in terms of effort as well. It does not make sense to fill the tank when it's already 3/4 full.

**No heat during cold** - On the other hand, if consumption is high suddenly and the tank is empty, there would not be any oil to heat the house. This can be very challenging and life threatening as well.

With **real time reading of oil tanks**, delivery companies can schedule the delivery precisely when it's needed. This will eliminate unwanted visits to the resident, reducing delivery costs and lowering CO2 emissions.

## How AI On The Edge Can Help?

Most oil tanks have analog meters which are not easy to read by machines. Moreover, adding a sensor in an existing tank to measure fuel level is expensive as it needs some poking and prodding, and oil tanks are typically old and there is a risk to damage the tank.

I am looking for a **cost effective and non-invasive** way to read the analog meter in real time.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/oil-tank-gauge-monitoring/device.jpg?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=8cdfa5a6a4a8b3acc679d2a2adb06390" width="607" height="555" data-path=".assets/images/oil-tank-gauge-monitoring/device.jpg" />
</Frame>

Using visual regression, we can train a model to read an analog meter and predict a scalar value between 0 to 100. This value is then sent to the cloud using a cellular connection.

## Edge Impulse And Visual Regression

### Data Capture

With any ML project, data capture is the most important step. To capture data from our heating oil tank is a time consuming task as the meter moves very slow, and I may need to wait for a month to capture all the different readings. So I designed and 3D printed an analog meter similar to a real heating oil tank meter, to capture data.

<Frame caption="Custom 3D printed analog meter">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/oil-tank-gauge-monitoring/gauge.jpg?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=168d9109cf39663a56a74b4625a75f2d" width="360" height="555" data-path=".assets/images/oil-tank-gauge-monitoring/gauge.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/oil-tank-gauge-monitoring/data-acquisition.jpg?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=80fe7085af90faac51f2a558e97572f3" width="740" height="453" data-path=".assets/images/oil-tank-gauge-monitoring/data-acquisition.jpg" />
</Frame>

Precise prediction isn't necessary for this use-case, I mean it's not a big deal if prediction is 5-10% off. So I choose the following readings: 0%, 13%, 25%, 37%, 50%, 65%, 87% and 100%.

Ideally we must refill our tank when it's around a quarter full, meaning around 25-30%.

The Sony Spresense is supported by Edge Impulse out of the box, which means they have firmware to help you connect the board to the EI Studio and capture images. Please checkout this [page](/hardware/boards/sony-spresense) which explains how.

### Creating Impulse

Creating an "Impulse" in Edge Impulse, is basically creating your ML model.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/oil-tank-gauge-monitoring/impulse.jpg?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=90500df34d931c6aa8a115ec13c204b8" width="740" height="431" data-path=".assets/images/oil-tank-gauge-monitoring/impulse.jpg" />
</Frame>

I have collected 96x96 pixel images, but trained the model with 60x60 grayscale. This makes the model size small, but compromises the accuracy a bit. You should experiment with different options and see what works best for you.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/oil-tank-gauge-monitoring/model.jpg?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=1a2dbe8624d642845ae04cd6af428c7d" width="426" height="555" data-path=".assets/images/oil-tank-gauge-monitoring/model.jpg" />
</Frame>

Once you finish training, you may see lot of incorrect regression, but if you take a closer look (above image), you will realize those are not entirely incorrect. For example, 25 was predicted as 25.12, which we can happily accept for our use-case.

You may take a look at the EI project [here](https://studio.edgeimpulse.com/public/105298/latest).

### Deploy

<Frame caption="Deployment">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/oil-tank-gauge-monitoring/deploy.jpg?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=59d633bd80d6568e222053f43c19da8a" width="740" height="526" data-path=".assets/images/oil-tank-gauge-monitoring/deploy.jpg" />
</Frame>

I have decided to download the model as a quantized Arduino library, considering Flash memory & RAM usage. Then used that in my Arduino sketch.

`#include <sony-analog-meter_inferencing.h>`

## Connect To AWS IoT

Once I get the model prediction, I connect to a cellular network and send data to AWS IoT Core over MQTT. Before you can connect to AWS IoT Core, you need to:

* Create a policy
* Create and download certificates ( Root CA, certificate and private key )
* Attach certificates to the created policy
* Create a Thing
* Attach policy to the Thing

It can be overwhelming. So I created a python script which will do all this for you. Locate the `register.py` program, change the variables, and run the program. This will create the AWS resources for you, and download the certificates and private key under the `certs` folder. Now you need to copy those files to the SD card and insert it into the Spresense LTE board.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/oil-tank-gauge-monitoring/code.jpg?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=e75891c7199ec56bf548f0aed4421654" width="693" height="555" data-path=".assets/images/oil-tank-gauge-monitoring/code.jpg" />
</Frame>

## System Architecture

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/oil-tank-gauge-monitoring/architecture.jpg?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=f1bc3c204dfc202519faa117272fd476" width="740" height="421" data-path=".assets/images/oil-tank-gauge-monitoring/architecture.jpg" />
</Frame>

Once data is sent to the AWS IoT topic, the defined IoT Rule invokes a Lambda Function passing the value.

<Frame caption="AWS IoT Rule">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/oil-tank-gauge-monitoring/aws-1.jpg?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=577450fd5dbaae5cc809e779a1bc11da" width="740" height="305" data-path=".assets/images/oil-tank-gauge-monitoring/aws-1.jpg" />
</Frame>

<br />

<Frame caption="Data received by AWS IoT Core">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/oil-tank-gauge-monitoring/aws-2.jpg?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=16d521a7fd446280d29ba0afb2b9b84a" width="740" height="460" data-path=".assets/images/oil-tank-gauge-monitoring/aws-2.jpg" />
</Frame>

The Lambda Function reads the raw value coming from the Topic, maps that to 1/4, 1/2, 3/4 and full, and persists the data to a dynamoDB table through GraphQL mutation.

Mapping of raw data is to flatten the prediction error. Like in below image, raw values came from the Sony Spresense varied between 47 and 51. But in reality the meter did not change. Rounding off those would give us a reading of 50. The reading on the dashboard will change when there is a significant change in the reading, such as 10% decrease.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/oil-tank-gauge-monitoring/dataset.jpg?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=f9c71d06745d798ee57159f70256d8b2" width="740" height="435" data-path=".assets/images/oil-tank-gauge-monitoring/dataset.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/oil-tank-gauge-monitoring/amplify.jpg?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=18a170a4754d022b0fa74662832a1518" width="740" height="458" data-path=".assets/images/oil-tank-gauge-monitoring/amplify.jpg" />
</Frame>

I am using AWS Amplify to create the GraphQL API and Lambda function. I am also using Amplify to host the web app. If you have not worked with [AWS Amplify](https://docs.amplify.aws/start/), I would highly encourage you to check that out.

## Dashboard UI

Before we install and start consuming data from the smart device, we need to register the device on the app.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/oil-tank-gauge-monitoring/application-1.gif?s=ba2b4b44c297212cb3b75fe487125b34" width="600" height="346" data-path=".assets/images/oil-tank-gauge-monitoring/application-1.gif" />
</Frame>

Once the smart meter is installed and powered on, the app will start showing data on the dashboard.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/oil-tank-gauge-monitoring/application-2.gif?s=854c380a66bd33b27c66198efff30fb4" width="800" height="461" data-path=".assets/images/oil-tank-gauge-monitoring/application-2.gif" />
</Frame>

## Demo

<iframe src="https://www.youtube.com/embed/SQk-NNtam38" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Low-Powered Battery Operated

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/oil-tank-gauge-monitoring/battery-power.jpg?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=beaa88cee4eef8d9ca00239ba22fa0a4" width="740" height="555" data-path=".assets/images/oil-tank-gauge-monitoring/battery-power.jpg" />
</Frame>

Another key aspect of this project is to run the smart meter on battery for several months before recharging. This is important, as there may not be a power source near the heating oil tank.

Things considered to maximize the use of battery are:

* Sony Spresense supports 156, 32 or 8 MHz clock frequency. I set clock mode to 32 MHz, as the Camera can work on it. And power consumption is almost half compared to 156 MHz.
* Stored AWS certificates in a header file rather than on the SD card. Typically it draws around 40mA for read/write operations, which is quite high compare to GNSS read (7mA).
* Not reading GNSS to obtain GPS location of the smart meter as its location is static. The location is not going to change once it's installed. Smart meter location is inserted from the app during device registration. This helps save battery power further.
* Reading data once every day. As the oil level is not going to decrease significantly every hour, it's overkill to read the meter very frequently like every few minutes or hours. The smart meter wakes up every 24 hours, takes a picture, runs the inference to predict the reading, connects to the cellular network, and sends data to AWS IoT Core over MQTT. The whole process takes around 150 seconds. The rest of the time the device goes to deep sleep mode, drawing about 300 μA.

<Frame caption="1100mAh With Clock 32MHz">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/oil-tank-gauge-monitoring/current-1.jpg?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=4c9258d76ec36d14d31f307fef9b7b5b" width="740" height="493" data-path=".assets/images/oil-tank-gauge-monitoring/current-1.jpg" />
</Frame>

Based on my brief research, with clock set to 32MHz, average current draw was around 75mA with a spike to 213 mA when the board connects to the cellular network and sends data to AWS. And total execution time was around 76 seconds.

<Frame caption="1100mAh Clock 156MHz">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/oil-tank-gauge-monitoring/current-2.jpg?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=ff780aa0fb48309fbfcf73e8ea78a4a3" width="740" height="493" data-path=".assets/images/oil-tank-gauge-monitoring/current-2.jpg" />
</Frame>

With clock set to 156 MHz, average current draw was around 110 mA with one big spike to 264mA and few spikes to between 150-200mA. We may consider average of 115 mA. Total execution time was 64 seconds compared to 76 seconds.

Hourly consumption is calculated as:

`Cawake × (Tawake / 3600) + Csleep × ((3600-Tawake) / 3600)`

Assuming current draw is 75mA (32 MHz clock), with a 2500mAh battery, it will last about **55** days and with 115mA (156 MHz clock), it will last about **44** days.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/oil-tank-gauge-monitoring/current-3.jpg?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=5933c46865bddd80db7b9968573d216f" width="546" height="555" data-path=".assets/images/oil-tank-gauge-monitoring/current-3.jpg" />
</Frame>

But note, this is an estimate and actual battery life depends on a lot of environmental factors such as temperature, qualify of the battery pack, how fast it discharges, etc.

<iframe src="https://www.youtube.com/embed/N0056G4siW4" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

Read [this article](https://developer.sony.com/develop/spresense/tutorials-sample-projects/spresense-tutorials/how-to-make-spresense-super-power-efficient) for more information.

## Challenges

Of course no project is without challenges. I am not going to discuss any technical challenges I faced to get the Sony Spresense working with LTE over a secured connection or setting up the Truphone Sim card as I believe it's very generic and common with any new development board we try for the first time. Other challenges to point out are:

* Different background of the image has huge impact on the performance of the regression model. So I decided to have a static background. This is a feasible option in production as well.
* Lighting is another aspect. Heating oil tanks are mostly located in the basement without any natural light. We should have an LED light turn on before taking the picture.

## Leak & Anomaly Detection

As I am receiving readings from the board, we can run ML models on AWS to predict any abnormality such as too fast draining of oil, which may indicate some leakage or provide some feedback to the customer to review the usage.

## Code

Code for this project is located here: [https://github.com/just4give/sony-analog-meter](https://github.com/just4give/sony-analog-meter)


Built with [Mintlify](https://mintlify.com).