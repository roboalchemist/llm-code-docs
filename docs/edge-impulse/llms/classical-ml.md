# Source: https://docs.edgeimpulse.com/studio/projects/learning-blocks/blocks/classical-ml.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Classical ML

<Info>
  **Only available on the Enterprise plan**

  This feature is only available on the Enterprise plan. Review our [plans and pricing](https://edgeimpulse.com/pricing) or sign up for our free [expert-led trial](https://edgeimpulse.com/expert-led-trial) today.
</Info>

Classical machine learning (ML) refers to traditional algorithms in machine learning that predate the current wave of deep learning. Deep learning usually involves large, complex neural networks. Classical ML techniques include various algorithms, such as logistic regression, support vector machines (SVMs), and decision trees. However, these techniques rely heavily on feature engineering to work well.

Deep neural networks can discover or create features from the raw data automatically, but classical ML models often require human domain knowledge expertise to generate these features. This is where Edge Impulse can help! We offer a number of [processing blocks](/studio/projects/processing-blocks) to help generate features based on various use cases. You can also perform autoML with [EON Tuner](/studio/projects/eon-tuner) to see which combinations of processing and machine learning (including classical ML) blocks work best for your dataset.

Traditional ML models are often easier to understand and interpret than their deep learning cousins. The simpler algorithms and structures used in traditional models make it easier to understand the relationship between input features and output predictions.

We implement these modules using scikit-learn, which is an extremely popular ML package used in the creation of models for real-world applications. Once trained, models are converted to Jax, a linear algebra library. That model is then converted to a LiteRT (previously Tensorflow Lite) (float 32) model, which will run on a variety of platforms.

The ability to convert Jax to LiteRT (previously Tensorflow Lite) models opens up a wide variety of possibilities when it comes to deploying different machine learning models to edge devices. If you are interested in developing a custom learning block, see [here](/studio/organizations/custom-blocks/custom-learning-blocks). You can also use this [scikit-learn custom learning block source code](https://github.com/edgeimpulse/example-custom-ml-block-scikit) as a starting point.

You can select one of several algorithms depending on your project type: classification or regression. Here is a quick reminder about the difference between the two types:

* Classification is used when you want to identify a sample as belonging to one particular grouping. It requires the number of possible outputs to be a discrete number. For example, classification is used if you want to determine if a picture is of a dog or a cat (2 possible outputs).
* Regression is used to predict a continuous value based on the input data. For example, predicting the price of a house based on location, average neighborhood sell price, etc.

## Getting started with classical ML

To start, select the **Classification** [learning block](/studio/projects/learning-blocks) when building your impulse.

<Info>
  Classical ML models are also available for **Regression**.
</Info>

<Frame caption="Select the classifier learning block">
  <img src="https://mintcdn.com/edgeimpulse/BnOEP1CPlKpl2ntM/.assets/images/classical-ml-01.png?fit=max&auto=format&n=BnOEP1CPlKpl2ntM&q=85&s=328650f01b0297d3689c0abcf27e0c1c" width="1473" height="882" data-path=".assets/images/classical-ml-01.png" />
</Frame>

After generating features, head to the **Classifier** learn block page. Click **Add an extra layer**. Under **Complete architectures**, you can select one of the many available classical ML models.

<Frame caption="Classical ML models available in Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/BnOEP1CPlKpl2ntM/.assets/images/classical-ml-04.png?fit=max&auto=format&n=BnOEP1CPlKpl2ntM&q=85&s=2e487b34841d31556a39500a2a4b57a6" width="1390" height="1000" data-path=".assets/images/classical-ml-04.png" />
</Frame>

See the [Supported classical ML algorithms](/studio/projects/learning-blocks/blocks/classical-ml#supported-classical-ml-algorithms) section below to learn about the different options.

When training your classical ML model, you should configure the required hyperparameters. Note that some may require far more training cycles (epochs) than what you are used to with deep learning (e.g. 1000 epochs). However, note that these algorithms train much faster than most neural networks!

<Frame caption="Training a classical ML model in Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/BnOEP1CPlKpl2ntM/.assets/images/classical-ml-02.png?fit=max&auto=format&n=BnOEP1CPlKpl2ntM&q=85&s=347095d48f73c8c683fbb17be808f402" width="1398" height="1000" data-path=".assets/images/classical-ml-02.png" />
</Frame>

<Info>
  Note that Expert mode is not available for classical ML models.
</Info>

Once you have your trained model, you can deploy the impulse to a variety of devices, including microcontrollers.

<Frame caption="Training a classical ML model in Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/BnOEP1CPlKpl2ntM/.assets/images/classical-ml-03.png?fit=max&auto=format&n=BnOEP1CPlKpl2ntM&q=85&s=d0e4cecf5f64f82692d825fedda6e934" width="1441" height="883" data-path=".assets/images/classical-ml-03.png" />
</Frame>

The gesture dataset is relatively simple. As a result, feature engineering and a classical ML model work very well. On more complex data, you might need to use deep learning to achieve your desired accuracy.

## Supported classical ML algorithms

Edge Impulse supports a number of classical algorithms to get you started. If you are unsure of which algorithm to use, we recommend using the [EON Tuner](/studio/projects/eon-tuner) to guide you.

### Logistic regression for classification

[Logistic regression](https://en.wikipedia.org/wiki/Logistic_regression) (despite its name) is a classifier; it is used to classify input data into one of several, discrete categories. It works by first fitting a line (or surface) to the data, just like in [linear regression](https://en.wikipedia.org/wiki/Linear_regression). From there, the predicted output (of linear regression) is fed into the [sigmoid function](https://en.wikipedia.org/wiki/Sigmoid_function) to classify the input as belonging to one of several classes.

Logistic regression is simple, fast, and efficient. However, it requires a linear relationship between the input and predicted class probabilities, which means it will not work well on complex data (e.g. non-linear relationships or many input dimensions).

The source code for the logistic regression block can be found in this repository: [sklearn-linear-models](https://github.com/edgeimpulse/example-custom-ml-block-sklearn-linear-models).

### Support vector machine (SVM) for classification

[Support vector machines](https://en.wikipedia.org/wiki/Support_vector_machine) rely on a technique called the “kernel trick” for mapping points in low-dimensional to high-dimensional space. By doing this, groupings of data can often be separated into clearly defined categories.

SVMs make for robust classification systems that work well with high-dimensional data (i.e. a single sample containing many values, such as different sensor values). However, they can struggle if classes in the dataset overlap significantly. If this is the case for your dataset, you may want to turn to neural networks.

An example Edge Impulse project using an SVM can be found here: [sklearn SVM Classification](https://studio.edgeimpulse.com/public/357674/latest).

The source code for the SVM block can be found in this repository: [example-custom-ml-block-svm](https://github.com/edgeimpulse/example-custom-ml-block-svm/).

### Random forest for classification and regression

[Random forest](https://en.wikipedia.org/wiki/Random_forest) is a type of machine learning model that employs multiple [decision trees](https://en.wikipedia.org/wiki/Decision_tree_learning). Random forests are simple to train and offer relatively high accuracy for classical ML approaches.

An example Edge Impulse project using a random forest classifier can be found here: [sklearn Random Forest Classification](https://studio.edgeimpulse.com/public/357645/latest).

The source code for the random forest block can be found in this repository: [example-custom-ml-block-sklearn-random-forest](https://github.com/edgeimpulse/example-custom-ml-block-sklearn-random-forest).

### Extreme gradient boosting (XGBoost) for classification and regression

[XGBoost](https://en.wikipedia.org/wiki/XGBoost) is an open-source implementation of gradient boosting, which is a type of ensemble learning that uses a combination of simpler models, such as decision trees. It works well for classification and regression tasks. Tree-based methods, like XGBoost, compare values only between samples and not between values in a sample. As a result, they work well with features that have different magnitudes and scales.

XGBoost is fast and efficient. It also has built-in methods for handling missing data, and it generally performs better with smaller datasets over LightGBM. However, it does not work as well as neural networks on complex data, and it is prone to overfitting.

An example Edge Impulse project using XGBoost for regression can be found here: [XGBoost Random Forest Regression](https://studio.edgeimpulse.com/public/316774/latest).

The source code for the XGBoost block can be found in this repository: [example-custom-ml-block-xgboost](https://github.com/edgeimpulse/example-custom-ml-block-xgboost/).

### Light gradient boosting machine (LightGBM) for classification and regression

Similar to XGBoost, [LightGBM](https://en.wikipedia.org/wiki/LightGBM) is another type of gradient-boosted ensemble model often constructed with decision trees, and it works well for both classification and regression tasks. Because it is a tree-based method, LightGBM compares values between samples rather than between features in a sample, thus making it robust when dealing with features that have different magnitudes.

LightGBM is also fast and efficient, but slightly less so than XGBoost, making it a better choice for larger datasets. Like XGBoost, it may not work well with complex data and is prone to overfitting.

An example Edge Impulse project using LightGBM for classification can be found here: [LGBM Random Forest Classification](https://studio.edgeimpulse.com/public/245576/latest).

The source code for the LightGBM block can be found in this repository: [example-custom-ml-block-lgbm](https://github.com/edgeimpulse/example-custom-ml-block-lgbm/).

## Going Further

If you want to implement your own learning block for Edge Impulse, see the guide [here](/studio/organizations/custom-blocks/custom-learning-blocks).


Built with [Mintlify](https://mintlify.com).