# Source: https://docs.edgeimpulse.com/projects/expert-network/acoustic-pipe-leak-detection-arduino-portenta-h7.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Acoustic Pipe Leakage Detection - Arduino Portenta H7

Created By: Manivannan Sivan

Public Project Link: [https://studio.edgeimpulse.com/public/111978/latest](https://studio.edgeimpulse.com/public/111978/latest)

## Project Demo

<iframe src="https://www.youtube.com/embed/EzDfbBDurm4" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Impact of Leakages in Pipes

Water is the world's most precious resource, yet it is also the one which is almost universally mismanaged. As a result, water shortages are becoming ever more common. In the case of water supply and distribution networks, these manifest themselves in the intermittent operation of the system. Not only is this detrimental to the structural condition of the pipes, but can also adversely affect the quality of the water delivered to the customer's taps. Further, leakage often exceeds 50% of the production. Not only does this have a significant economic impact, but an environmental one too. But to recover leakage has a cost to undertake a hydraulic study of the network, create a permanent monitoring system, and eliminate the leaks. So how low should leakage go and how can a lower leakage level be maintained over time? This is the objective of the very innovative EU funded PALM project recently completed in central Italy.

### Increase in Carbon Level Due to Water Leakage

There is an increased carbon footprint of having pumps constantly running to make up for the water lost due to leakage. It is the increased pump use, and pump maintenance/replacement costs that increase CO2 in the air from the fossil fuels being burned to support it. According to a study done by Von Sacken in 2001, water utilities are the largest user of electricity accounting for 3% of the total electricity consumption in the US. In addition, it is estimated that 2-3 billion kW/h of electricity is expended pumping water due to leakage.

*Costs, health, the environment, and infrastructure are just a few things that can come into play when water system leakage goes uncorrected.*&#x20;

More than 2 billion people globally live in countries with high water stress, per the 2018 statistics provided by the United Nations (UN). In order to tackle this problem, it is necessary to conserve and utilize water safely. Installation of proper water pipeline leak detection systems assist in specifying the leakages in installed water pipes, which ultimately avoids wasting water through cracks and holes. Therefore, the increasing scarcity of water is propelling the demand for water leak solutions, which in turn drives the market.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/qzz8ALldRag_9UsW/.assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/intro.jpg?fit=max&auto=format&n=qzz8ALldRag_9UsW&q=85&s=3445fac925017773d333abc531a249a5" width="546" height="288" data-path=".assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/intro.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/qzz8ALldRag_9UsW/.assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/intro-2.jpg?fit=max&auto=format&n=qzz8ALldRag_9UsW&q=85&s=9aef9aa36436b5622faeb0ef29160737" width="382" height="274" data-path=".assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/intro-2.jpg" />
</Frame>

### Global Market for Pipe Leakage Detection Systems

The global water pipeline leak detection systems market size is expected to reach $2,349.6 million in 2027, from $1,748.6 million in 2019, growing at a CAGR of 6.8% from 2020 to 2027. Water pipeline leak detection systems are utilized to determine the location of the leak in water transmission pipelines. Around 30% to 50% of water is lost through aging pipelines, which also contributes toward loss of revenue. Water pipeline leak detection systems are available for both underground and overground water pipelines to precisely locate and check the severity of pipeline leaks.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/qzz8ALldRag_9UsW/.assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/intro-3.jpg?fit=max&auto=format&n=qzz8ALldRag_9UsW&q=85&s=ff172aa4cca43eea41ae920a1de1d938" width="902" height="532" data-path=".assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/intro-3.jpg" />
</Frame>

On the contrary, in recent years, pipeline leak detection systems have undergone various technological advancements by adoption of computerized systems and digital survey systems. The traditional acoustic detection sensors are upgraded with more efficient sound detection functions which has increased their efficiency. Introduction and implementation of such advanced technologies are likely to create lucrative opportunities for the growth of the water pipeline leak detection systems market during the forecast period.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/qzz8ALldRag_9UsW/.assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/intro-4.jpg?fit=max&auto=format&n=qzz8ALldRag_9UsW&q=85&s=ed8ed8513a0ad786f5a117d7ba50a5ba" width="902" height="502" data-path=".assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/intro-4.jpg" />
</Frame>

In recent years, the increase in acoustic-based pipe leakage detection has started increasing due to investment in R\&D.

## A TinyML-based Solution for Pipe Leakage Detection:

In this fast growing sector, TinyML-based systems will play a major role due to low power consumption and developing EdgeML models with more accuracy in predicting leakage detection.

My prototype is based on acoustic data collected on an Arduino Portenta H7 and a model is trained using Edge Impulse. In my prototype, The Arduino Portenta Vision Shield is used because it contains two microphones (MP34DT05) which runs on 16 MHz. The Vision Shield is placed on top of the pipe for data acquisition as the microphone faces the pipe. This will help to collect the noise of the water flowing.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/qzz8ALldRag_9UsW/.assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/prototype-1.jpg?fit=max&auto=format&n=qzz8ALldRag_9UsW&q=85&s=7623c74326426a1473622430646f6448" width="657" height="356" data-path=".assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/prototype-1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/qzz8ALldRag_9UsW/.assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/prototype-2.jpg?fit=max&auto=format&n=qzz8ALldRag_9UsW&q=85&s=eb978007e13ae1b4a50c60d3374d6fce" width="902" height="574" data-path=".assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/prototype-2.jpg" />
</Frame>

In the data acquisition stage, the pipe is simulated with "Idle" mode, where the tap is fully closed so no water flows, and then slightly opened to simulate "leakage mode". Finally, is it fully opened to simulate "water flow" mode.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/qzz8ALldRag_9UsW/.assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/data-acquisition.jpg?fit=max&auto=format&n=qzz8ALldRag_9UsW&q=85&s=ea896d26bb20eac2f6741ae0680ad341" width="902" height="610" data-path=".assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/data-acquisition.jpg" />
</Frame>

## Pre-Processing

In a pre processing stage, the Window size is set as 2000ms and Window increase is set as 500ms.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/qzz8ALldRag_9UsW/.assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/pre-processing.jpg?fit=max&auto=format&n=qzz8ALldRag_9UsW&q=85&s=0b7d8785fe13983a5b671296ac3b810c" width="902" height="472" data-path=".assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/pre-processing.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/qzz8ALldRag_9UsW/.assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/feature-extraction.jpg?fit=max&auto=format&n=qzz8ALldRag_9UsW&q=85&s=ab7562186a16ef41008a4a1799583bfb" width="902" height="606" data-path=".assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/feature-extraction.jpg" />
</Frame>

For Neural Network configuration, I have used couple of 1D-Conv layers followed by DNN layers.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/qzz8ALldRag_9UsW/.assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/nn-architecture.jpg?fit=max&auto=format&n=qzz8ALldRag_9UsW&q=85&s=a25bf8aeacc40a70b10e88d26d16c56f" width="902" height="702" data-path=".assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/nn-architecture.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/qzz8ALldRag_9UsW/.assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/nn-settings.jpg?fit=max&auto=format&n=qzz8ALldRag_9UsW&q=85&s=d540eb458a6f1bbffc0b15c925351fd9" width="820" height="452" data-path=".assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/nn-settings.jpg" />
</Frame>

The number of Training cycles is set to 100 and Learning rate is set to 0.005. The accuracy obtained was 99.1 % with loss of 0.02 only. As the model is performing well at classifying the data, we can move on.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/qzz8ALldRag_9UsW/.assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/model-accuracy.jpg?fit=max&auto=format&n=qzz8ALldRag_9UsW&q=85&s=14ed22f5d9b3ee7abc12f0c08705d8c7" width="840" height="706" data-path=".assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/model-accuracy.jpg" />
</Frame>

## Model Testing

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/qzz8ALldRag_9UsW/.assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/model-testing.jpg?fit=max&auto=format&n=qzz8ALldRag_9UsW&q=85&s=8f3f92eab6edc2f8813ae0a9a695834e" width="1137" height="388" data-path=".assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/model-testing.jpg" />
</Frame>

In Model testing, the trained model is tested with data and it is able to predict all 3 conditions we trained on with 100% accuracy.

## Deployment

<Info>
  For initial setup of the Portenta, follow the steps outlined [here](/hardware/boards/arduino-portenta-h7).
</Info>

Then in Deployment section, select Arduino Portenta H7 and download the firmware files to your computer.

Press the Reset button twice on the Portenta to change it to Flash mode. Then run the .bat file if you are on Windows, or the Mac or Linux commands if you are on those platforms.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/qzz8ALldRag_9UsW/.assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/deployment-1.jpg?fit=max&auto=format&n=qzz8ALldRag_9UsW&q=85&s=e194759133f6690d8c3fe580f3173a91" width="902" height="360" data-path=".assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/deployment-1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/qzz8ALldRag_9UsW/.assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/deployment-2.jpg?fit=max&auto=format&n=qzz8ALldRag_9UsW&q=85&s=21fd2131f6b092436376d9e32e125a0b" width="522" height="262" data-path=".assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/deployment-2.jpg" />
</Frame>

## Summary

The prototype demonstrated an acoustic method to predict leakage in a pipe. The model was able to determine whether the pipe is in Idle (no water flowing), flowing normally, or if there is a small flow, representing leakage in this case. The use case is simple enough to apply to any industry to monitor the leakages in pipe, though this is of course only a prototype project.

By integrating well-designed enclosures with higher quality microphones, the Arduino Portenta H7 will be ideal for industrial use-cases for pipe leakage detection.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/qzz8ALldRag_9UsW/.assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/summary.jpg?fit=max&auto=format&n=qzz8ALldRag_9UsW&q=85&s=948110fe26dd02325578c0311e95bd08" width="1024" height="518" data-path=".assets/images/acoustic-pipe-leak-detection-arduino-portenta-h7/summary.jpg" />
</Frame>


Built with [Mintlify](https://mintlify.com).