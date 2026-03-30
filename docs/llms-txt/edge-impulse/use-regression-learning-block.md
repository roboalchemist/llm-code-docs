# Source: https://docs.edgeimpulse.com/tutorials/topics/machine-learning/use-regression-learning-block.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Use the regression learning block

This tutorial shows you how to use Edge Impulse's regression block to design an Embedded Machine Learning model based on the concept of linear regression. Linear Regression can be useful for Predictive Maintenance applications. We'll use the \[cold chain use case\[([https://edgeimpulse.com/blog/embedded-machine-learning-cold-chain](https://edgeimpulse.com/blog/embedded-machine-learning-cold-chain))] discussed in our previous blog post and explain how to apply the regression learning block to the same training dataset.

As a quick refresher, here is part of the training dataset from our previous anomaly detection model, which captures the slope increase from the temperature of 26 degrees F to 38 degrees F. This training data represents the time from when the freezer door was open (time t = 0) to 1 min after the freezer door was opened (time t = 60). With the regression model we can predict how "far" the current temperature sensor readings are from hitting a critical temperature, let's say to be designated here at time = 60 seconds. Our prediction output will tell us how close we are to hitting that critical temperature. The lower the score, the closer the system is to hitting that critical temperature range.

<Frame caption="Temperature Increase 'Slope of Interest'">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/528c8af-screenhunter_204_jan_15_1512.jpg?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=e1b18bd45b394fcd90244398261968bd" width="587" height="377" data-path=".assets/images/528c8af-screenhunter_204_jan_15_1512.jpg" />
</Frame>

\##Step 1: Split up the previous training data set into overlapping training windows

The first step is to take our 60 second slope of interest and create training data samples that represent each graduation on the slope. For this example, we chose to use a window size of 2 seconds, with a 1 second overlapping window. If things were done correctly, you will end up with a training data set like so with 60 labels, each labeled from 1 through 60.

<Frame caption="Training Data Set for Regression">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/43eee69-screenhunter_240_feb_24_1427.jpg?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=dee25c846f27f23a34e05d553bc6e9a1" width="795" height="811" data-path=".assets/images/43eee69-screenhunter_240_feb_24_1427.jpg" />
</Frame>

\##Step 2: Design the Impulse and train the regression model

The next step is to design the impulse and for this we again use a window size of 2 seconds and a window increase of 1 second. We select "Raw Data" for the processing block and select "Regression (Keras) for the learning block. Follow the usual steps of saving the parameters then generating the features and you will end up with something looking like the following. The color coding is a nice visual representation as well of how close we are to hitting the critical temperature the system is trying to avoid. For example, a prediction value of 59 based on the current temperature is shown here as "purple", meaning that the system is not close to being in any danger of hitting the critical temperature. However, a prediction value of 10 or less means that the system is dangerously close to hitting the critical temperature.

<Frame caption="Impulse Design for Regression">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/aa024d3-screenhunter_241_feb_24_1448.jpg?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=d066d13db667e0f703b2639e16be8a9a" width="1246" height="633" data-path=".assets/images/aa024d3-screenhunter_241_feb_24_1448.jpg" />
</Frame>

<Frame caption="Features representing each graduation along the slope of interest">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/7586357-screenhunter_239_feb_24_1426.jpg?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=da635570ebe6d3e954a839373dd4718e" width="626" height="628" data-path=".assets/images/7586357-screenhunter_239_feb_24_1426.jpg" />
</Frame>

The final step in the Impulse design is to train the model as shown below and one thing important to note here is the number of training cycles required for the regression model to get an acceptable level of accuracy in this context.

<Frame caption="NN Classifier Block Design for Regression">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/954dd9b-screenhunter_238_feb_24_1425.jpg?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=4ccdf2e2d43f3c620f465763cb5b4c25" width="655" height="889" data-path=".assets/images/954dd9b-screenhunter_238_feb_24_1425.jpg" />
</Frame>

\##Step 3: Validate the Regression Model

The final step is to validate our model and for this we have used the similar splicing method from before to assemble some data samples in our test dataset. We label the expected outcome according to where the data was gathered from along the slope, and then use the "Model Testing" tab to validate our model. Our results are within acceptable accuracy. From an end application standpoint, it can make sense to use these numbers to create similar color coded "zones" as mentioned before for indicating to the system operator how close the system is to arriving at a failure condition.

<Frame caption="Validated Results">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/3646b10-screenhunter_237_feb_24_1424.jpg?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=9350f1797bc4730f6f07f406e8f5b7cc" width="876" height="730" data-path=".assets/images/3646b10-screenhunter_237_feb_24_1424.jpg" />
</Frame>

Access the [public version](https://studio.edgeimpulse.com/public/17972/latest) of the Edge Impulse project to see how this is all setup in more detail. Clone the project if you want to experiment with this in your own account.


Built with [Mintlify](https://mintlify.com).