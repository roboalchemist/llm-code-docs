# Source: https://docs.edgeimpulse.com/studio/projects/learning-blocks/blocks/regression.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Regression

Solving regression problems is one of the most common applications for machine learning models, especially in supervised machine learning. Models are trained to understand the relationship between independent variables and an outcome or dependent variable. The model can then be leveraged to predict the outcome of new and unseen input data, or to fill a gap in missing data.

## Prerequisites

### Labeling

To build a regression model you collect data as usual, but rather than setting the label to a text value, you set it to a numeric value.

<Frame caption="Regression data samples labeled with numerical values">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/regression-labelling.png?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=9d393546a90d34717b525ddf4db61b06" width="1198" height="414" data-path=".assets/images/regression-labelling.png" />
</Frame>

### Processing blocks

You can use any of the built-in signal processing blocks to pre-process your vibration, audio or image data, or use custom processing blocks to extract novel features from other types of sensor data.

<Frame caption="An impulse with a regression block">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/regression-create-impulse.png?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=923ccb0d648a8c5052dc8161d9bbe16d" width="1422" height="468" data-path=".assets/images/regression-create-impulse.png" />
</Frame>

## Train your regression block

You have full freedom in modifying your neural network architecture - whether visually or through writing Keras code.

<Frame caption="Regression view">
  <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-regession-overview-2024.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=dafc88de5a8825923c6bed577a99a40c" width="1167" height="1000" data-path=".assets/images/studio-regession-overview-2024.png" />
</Frame>

## Neural Network settings

See [Neural Network Settings](/studio/projects/learning-blocks#neural-network-settings) on the Learning Block page.

## Neural Network architecture

See [Neural Network Architecture](/studio/projects/learning-blocks#neural-network-architecture) on the Learning Block page.

## Expert mode

See [Expert mode](/studio/projects/learning-blocks#expert-mode) on the Learning Block page.

## Test your regression model

If you want to see the accuracy of your model across your test dataset, go to **Model testing**. You can adjust the **Maximum error percentage** by clicking on the "⋮" button.

<Frame caption="Testing regression model">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/regression-testing.png?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=7a992731ad9f0e1c3bf9c2d92d269bdb" width="1600" height="797" data-path=".assets/images/regression-testing.png" />
</Frame>

## Additional resources

* [Predict the Future with Regression Models](https://edgeimpulse.com/blog/predict-the-future-with-regression-models)
* [Estimate Weight From a Photo Using Visual Regression in Edge Impulse](https://edgeimpulse.com/blog/estimate-weight-from-a-photo-using-visual-regression-in-edge-impulse)


Built with [Mintlify](https://mintlify.com).