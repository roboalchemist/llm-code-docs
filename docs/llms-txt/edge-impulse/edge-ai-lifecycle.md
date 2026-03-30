# Source: https://docs.edgeimpulse.com/knowledge/courses/edge-ai-fundamentals/edge-ai-lifecycle.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Edge AI lifecycle

The edge AI lifecycle includes the steps involved in planning, implementing, and maintaining an edge AI project. It follows the same general flow as most engineering and programming undertakings with the added complexity of managing data and models.

Previously, we examined [techniques for choosing hardware for edge AI projects](/knowledge/courses/edge-ai-fundamentals/how-to-choose-an-edge-ai-device). In this lesson, we will look at the machine learning (ML) pipeline and how to approach an edge AI project.

<iframe src="https://www.youtube.com/embed/EJtiBwHVxP8" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Identify need and scope

Before starting a machine learning project, it is imperative that you examine the actual need for such a project: what problem are you trying to solve? For example, you could improve user experience, such as creating a more accurate fall detection or voice-activated smart speaker. You might want to monitor machinery to identify anomalies before problems become unmanageable, which could save you time and money in the long run. Alternatively, you could count people in a retail store to identify peak times and shopping trends.

Once you have identified your requirements, you can begin scoping your project:

* Can the project be solved through traditional, rules-based methods, or is AI needed to solve the problem?
* Is cloud AI or edge AI the better approach?
* What kind of hardware is the best fit for the problem?

Note that the hardware selection might not be apparent until you have constructed a prototype ML model, as that will determine the amount of processing power required. As a result, it can be helpful to quickly build a proof-of-concept and iterate on the design, including hardware selection, to arrive at a complete solution.

## Machine learning pipeline

Most ML projects follow a similar flow when it comes to collecting data, examining that data, training an ML model, and deploying that model.

<Frame caption="Machine learning pipeline and workflow">
  <img src="https://mintcdn.com/edgeimpulse/LSbqkaU8tx8Cie9-/.assets/images/edge-ai-lifecycle-ml-pipeline.png?fit=max&auto=format&n=LSbqkaU8tx8Cie9-&q=85&s=dac1c6f37469337dd3096c01ec76e025" width="960" height="540" data-path=".assets/images/edge-ai-lifecycle-ml-pipeline.png" />
</Frame>

This complete process is known as a *machine learning pipeline*.

### Data collection

To start the process, you need to collect raw data. For most deep learning models, you need a lot of data (think thousands or tens of thousands of samples).

In many cases, data collection involves deploying sensors to the field or your target environment and let them collect raw data. You might collect audio data with a smartphone or vibration data using an IoT sensor. You can create custom software that automatically transmits the data to a [data lake](https://aws.amazon.com/what-is/data-lake/) or store it directly to an Edge Impulse project. Alternatively, you can store data directly to the device, such as on an SD card, that you later upload to your data storage.

Examples of data can include raw time-series data in a [CSV file](https://en.wikipedia.org/wiki/Comma-separated_values), audio saved as a [WAV file](https://en.wikipedia.org/wiki/WAV), or images in [JPEG format](https://en.wikipedia.org/wiki/JPEG).

Note that sensors can vary. As a result, it's usually a good idea to collect data using the same device and/or sensors that you plan to ultimately deploy to. For example, if you plan to deploy your ML model to a smartphone, you likely want to collect data using smartphones.

### Data cleaning

Raw data often contains errors in the forms of omissions (some fields missing), corrupted samples, or duplicate entries. If you do not fix these errors, the machine learning training process will either not work or contain errors.

<Frame caption="Machine learning data cleaning">
  <img src="https://mintcdn.com/edgeimpulse/LSbqkaU8tx8Cie9-/.assets/images/edge-ai-lifecycle-data-cleaning.png?fit=max&auto=format&n=LSbqkaU8tx8Cie9-&q=85&s=bb7514da251247ba2fd9b60f8b83a53f" width="759" height="404" data-path=".assets/images/edge-ai-lifecycle-data-cleaning.png" />
</Frame>

A common practice is to employ the [medallion architecture](https://dataengineering.wiki/Concepts/Medallion+Architecture) for scrubbing data, which involves copying data, cleaning out an errors or filling missing fields, and storing the results into a different bucket. The buckets have different labels: bronze, silver, gold. As the data is successively cleaned and aggregated, it moves up from bronze to silver, then silver to gold. The gold bucket is ready for analysis or to be fed to a machine learning pipeline.

The process of downloading, manipulating, and re-uploading the data back into a separate storage is known as *extract, transform, load* (ETL). A number of tools, such as [Edge Impulse transformation blocks](/studio/organizations/custom-blocks/custom-transformation-blocks) and [AWS Glue](https://aws.amazon.com/glue/), can be used to build automated ETL pipelines once you have an understanding of how the data is structured and what cleaning processes are required.

### Data analysis

Once the data is cleaned, it can be analyzed by domain experts and data scientists to identify patterns and extract meaning. This is often a manual process that utilizes various algorithms (e.g. unsupervised ML) and tools (e.g. Python, R). Such patterns can be used to construct ML models that automatically generalize meaning from the raw input data.

Additionally, data can contain any number of [biases](https://developers.google.com/machine-learning/crash-course/fairness/types-of-bias) that can lead to a biased machine learning model. Analyzing your data for biases can create a much more robust and fair model down the road.

### Feature extraction

Sometimes, the raw data is not sufficient or might cause the ML model to be overly complex. As a result, manual features can be extracted from the raw data to be fed into the ML model. While feature engineering is a manual step, it can potentially save time and inference compute resources by not having to train a larger model. In other words, feature extraction can simplify the data going to a model to help make the model smaller and faster.

<Frame caption="Feature extraction and engineering">
  <img src="https://mintcdn.com/edgeimpulse/LSbqkaU8tx8Cie9-/.assets/images/edge-ai-lifecycle-feature-extraction.png?fit=max&auto=format&n=LSbqkaU8tx8Cie9-&q=85&s=0712de7e1dbfc45b0ff538d78818a70b" width="948" height="284" data-path=".assets/images/edge-ai-lifecycle-feature-extraction.png" />
</Frame>

For example, a time-series sample might have hundreds or thousands of data points. As the number of such points increases, the model complexity also often increases. To help keep the model small, we can extract some features from each sample. In this case, performing the [Fast Fourier Transform (FFT)](https://en.wikipedia.org/wiki/Fast_Fourier_transform) breaks the signal apart into its frequency components, which helps the model identify repeating patterns. Now, we have a few dozen data points going into a model rather than a few hundred.

In general, smaller models and fewer inputs mean faster execution times.

### Train machine learning model

With the data cleaned and features extracted, you can select or construct an ML model architecture and train that model. In the training process, you attempt to generalize meaning in the input data such that the model's output matches expected values (even when presented with new data).

Deep neural networks are the current popular approach to solving a variety of supervised and unsupervised ML tasks. ML scientists and engineers use a variety of tools, such as [TensorFlow](https://www.tensorflow.org/) and [PyTorch](https://pytorch.org/) to build, train, and test deep neural networks.

In addition to using these lower-level tools to design your own model architecture, you can also rely on pre-built models or tools, like [Edge Impulse](https://edgeimpulse.com/), that contain the building blocks needed to tackle a wide variety of edge AI tasks.

Pretrained models can be retrained using custom data in a process known as [transfer learning](https://en.wikipedia.org/wiki/Transfer_learning). Transfer learning is often faster and requires less data than training from scratch.

The combination of automated feature extraction and ML model is known as an *impulse*. This combination of steps can be deployed to cloud servers and edge devices. The impulse takes in raw data, performs any necessary feature extraction, and runs inference during prediction serving.

### Model testing

In almost all cases, you want to test your model's performance. Good ML practices dictate keeping a part of your data separate from the training data (known as a *test set*, or *holdout set*). Once you have trained the model, you will use this test set to verify the model's functionality. If your model performs well on the training set but poorly on the test set, it might be [overfit](https://aws.amazon.com/what-is/overfitting/), which often requires you to rethink your dataset, feature extraction, and model architecture.

The process of data cleaning, feature extraction, model training, and model testing is almost always iterative. You will often find yourself revisiting each stage in the pipeline to create an impulse that performs well for your particular task and within your hardware constraints.

Additionally, you might need to collect new data if your current dataset does not produce an acceptable model. For example, vibration data from an accelerometer alone might prove insufficient for creating a robust model, so you have to collect supplemental data, such as audio data from a microphone. The combination of vibration and audio data is usually better at identifying mechanical anomalies than one sensor type alone.

### Model deployment

For cloud-based AI, you can use tools like [SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-deployment.html) to deploy your model to a server as part of a prediction serving application. Edge AI can be somewhat trickier, as you often need to optimize your model for a particular hardware and develop an application around that model.

Optimization can involve a number of processes that reduce the size and complexity of the ML model, such as [pruning unimportant nodes](https://opendatascience.com/what-is-pruning-in-machine-learning/) from the neural network, [quantization](https://huggingface.co/docs/optimum/concept_guides/quantization) to run more efficiently on low-end hardware, and compiling models to run on specialized hardware (e.g. GPUs and NPUs).

The ML model is simply a collection of mathematical operations. On it's own, it cannot do much. Due to this limitation, an application needs to be built around the model to collect data, feed data to the impulse for feature extraction and inference, and take some action based on the inference results.

In cloud-based AI, this application is often a prediction serving program that waits for web requests containing raw data. The application can then respond with inference results. On the other hand, edge AI usually requires a tighter integration between performing inference and doing something with the results, such as notifying a user, stopping a machine, or making a decision on how to steer a car.

Programmers and software engineers are often needed to build the application. In many cases, these developers are experts with the target deployment hardware, such as a particular microcontroller, embedded Linux, or smartphone app creation. They work with the ML engineering team to ensure that the model can run on the target hardware.

### Operations and maintenance (O\&M)

As with any software deployment, operations and maintenance is important to provide continuing support to the edge AI solution. As the data or operating environment changes over time, model performance can begin to degrade. As a result, such deployments often require monitoring model performance, collecting new data, and updating the model.

In the next section on [edge MLOps](/knowledge/courses/edge-ai-fundamentals/what-is-edge-mlops), we will examine the different types of model drift and how parts of the ML pipeline can be automated to create a repeatable system for O\&M.

## Quiz

Test your knowledge on the edge AI lifecycle with the following quiz:

<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSeKp564PdNAYiHfVF8xLZa9spzLcFRoUM6G8pnpSpFwbl-1Bg/viewform?embedded=true" className="w-full aspect-square rounded-xl" />


Built with [Mintlify](https://mintlify.com).