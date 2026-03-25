# Source: https://docs.edgeimpulse.com/knowledge/concepts/what-is-embedded-machine-learning-anyway.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is embedded ML, anyway?

Machine learning (ML) is a way of writing computer programs. Specifically, it’s a way of writing programs that process raw data and turn it into information that is meaningful at an application level.

For example, one ML program might be designed to determine when an industrial machine has broken down based on readings from its various sensors, so that it can alert the operator. Another ML program might take raw audio data from a microphone and determine if a word has been spoken, so it can activate a smart home device.

Unlike normal computer programs, the rules of ML programs are not determined by a developer. Instead, ML uses specialized algorithms to *learn* rules from data, in a process known as *training*.

In a traditional piece of software, an engineer designs an algorithm that takes an input, applies various rules, and returns an output. The algorithm’s internal operations are planned out by the engineer and implemented explicitly through lines of code. To predict breakdowns in an industrial machine, the engineer would need to understand which measurements in the data indicate a problem and write code that deliberately checks for them.

This approach works fine for many problems. For example, we know that water boils at 100°C at sea level, so it’s easy to write a program that can predict whether water is boiling based on its current temperature and altitude. But in many cases, it can be difficult to know the exact combination of factors that predicts a given state. To continue with our industrial machine example, there might be various different combinations of production rate, temperature, and vibration level that might indicate a problem but are not immediately obvious from looking at the data.

To create an ML program, an engineer first collects a substantial set of training data. They then feed this data into a special kind of algorithm, and let the algorithm discover the rules. This means that as ML engineers, we can create programs that make predictions based on complex data without having to understand all of the complexity ourselves.

Through the training process, the ML algorithm builds a *model* of the system based on the data we provide. We run data through this model to make predictions, in a process called *inference*.

<Info>
  There are many different types of machine learning algorithms, each with their own unique benefits and drawbacks. Edge Impulse helps engineers select the right algorithm for a given task.
</Info>

## Where can machine learning help?

Machine learning is an excellent tool for solving problems that involve pattern recognition, especially patterns that are complex and might be difficult for a human observer to identify. ML algorithms excel at turning messy, high-bandwidth raw data into usable signals, especially combined with conventional signal processing.

For example, the average person might struggle to recognize the signs of a machine failure given ten different streams of dense, noisy sensor data. However, a machine learning algorithm can often learn to spot the difference.

But ML is not always the best tool for the job. If the rules of a system are well defined and can be easily expressed with hard-coded logic, it’s usually more efficient to work that way.

<Warning>
  #### Limitations of machine learning

  Machine learning algorithms are powerful tools, but they can have the following drawbacks:

  * They output estimates and approximations, not exact answers
  * ML models can be computationally expensive to run
  * Training data can be time consuming and expensive to obtain

  It can be tempting to try and apply ML everywhere—but if you can solve a problem without ML, it is usually better to do so.
</Warning>

## What is embedded ML?

Recent advances in microprocessor architecture and algorithm design have made it possible to run sophisticated machine learning workloads on even the smallest of microcontrollers. Embedded machine learning, also known as TinyML, is the field of machine learning when applied to embedded systems such as these.

There are some major advantages to deploying ML on embedded devices. The key advantages are neatly expressed in the unfortunate acronym BLERP, [coined by Jeff Bier](https://www.eetimes.com/ai-and-vision-at-the-edge/#). They are:

**Bandwidth**—ML algorithms on edge devices can extract meaningful information from data that would otherwise be inaccessible due to bandwidth constraints.

**Latency**—On-device ML models can respond in real-time to inputs, enabling applications such as autonomous vehicles, which would not be viable if dependent on network latency.

**Economics**—By processing data on-device, embedded ML systems avoid the costs of transmitting data over a network and processing it in the cloud.

**Reliability**—Systems controlled by on-device models are inherently more reliable than those which depend on a connection to the cloud.

**Privacy**—When data is processed on an embedded system and is never transmitted to the cloud, user privacy is protected and there is less chance of abuse.

## Learn more

The best way to learn about embedded machine learning is to see it for yourself. To train your own model and deploy it to any device, including your mobile phone, follow our [Getting started for beginners](/knowledge/guides/getting-started-for-beginners) guide. You can also check out our [Edge AI Fundamentals](/knowledge/courses/edge-ai-fundamentals/intro-to-edge-ai) course to learn more about edge computing, machine learning, and edge MLOps.


Built with [Mintlify](https://mintlify.com).