# Source: https://docs.edgeimpulse.com/knowledge/courses/edge-ai-fundamentals/what-is-edge-ai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is edge AI?

Edge AI is the development and deployment of artificial intelligence (AI) algorithms and programs on edge devices. It is a form of [edge computing](/knowledge/courses/edge-ai-fundamentals/what-is-edge-computing) where data is analyzed and processed near where the data is generated or collected. Edge AI contrasts cloud-based AI, which involves data being transmitted across the internet to be processed on a remote server.

<iframe src="https://www.youtube.com/embed/QXuvUW4B7jU" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Machine learning training and deployment

In [machine learning (ML)](/knowledge/courses/edge-ai-fundamentals/what-is-machine-learning), data is fed into the training process. For supervised learning, the ground-truth labels are also provided along with each sample. The training algorithm automatically updates the parameters (also known as "weights") in the ML model.

<Frame caption="Machine learning model training">
  <img src="https://mintcdn.com/edgeimpulse/cMDYCG0TzQNU7yvn/.assets/images/what-is-edge-ai-training.png?fit=max&auto=format&n=cMDYCG0TzQNU7yvn&q=85&s=6705b0a4618abfb466e01855edc4ee6a" width="848" height="260" data-path=".assets/images/what-is-edge-ai-training.png" />
</Frame>

During each step of the training process, we evaluate the model to see how good it is at predicting the correct label given some data. Over time, we ideally want this accuracy to increase to some acceptable level. In most cases, training a machine learning model is computationally expensive, and training does not need to be performed on an edge device. As a result, we can do model training in the cloud with the help of powerful accelerator hardware, such as graphics processing units (GPUs).

Once we are happy with the performance of the model, we can deploy it to our end device. At this point, the model accepts new, never-before-seen data and produces an output. For supervised learning and classification, this output is a label that the model believes most accurately represents the input data. In regression, this output is a numerical value (or values). This process of making predictions based on new data after training is known as *inference*.

In traditional, cloud-based ML model deployment, inference is run on a remote server. Clients connect to the inference service, supply new data along with their request, and the server responds with the result. This cloud-based inference process is known as *prediction serving*.

<Frame caption="Machine learning model inference">
  <img src="https://mintcdn.com/edgeimpulse/cMDYCG0TzQNU7yvn/.assets/images/what-is-edge-ai-inference.png?fit=max&auto=format&n=cMDYCG0TzQNU7yvn&q=85&s=ef8397a398ce109f8c66967a92e24268" width="846" height="257" data-path=".assets/images/what-is-edge-ai-inference.png" />
</Frame>

In the majority of cases, inference is not nearly as computationally intensive as training. As a result, we could run inference on an edge device instead of on a powerful cloud server.

Because edge devices often offer less compute power than their cloud counterparts, ML models trained for the edge often need to be less complex. With that in mind, edge AI offers several benefits over cloud AI.

## Benefits of edge AI

Assuming that you can run your ML model on an edge device, such as a laptop, smartphone, single-board computer, or embedded Internet of Things (IoT) device, edge AI has the following advantages over a cloud-based approach:

* **Reduced bandwidth** - Rather than transmitting raw data over the network, you can perform inference on the edge device directly. From there, you would only need to transmit the results, which is often much less data than the raw input.
* **Reduced latency** - Transmitting data across networks (including the internet) can take time, as that data has to travel through multiple switches, routers, and servers. The round trip latency is often measured in 100s of milliseconds when waiting for a response from a cloud server. On the other hand, there is little or no network latency with edge AI, as inference is performed on or relatively close to where the data was collected.
* **Better energy efficiency** - Most cloud servers require large overhead with [containerized](https://aws.amazon.com/what-is/containerization/) operating systems and various abstraction layers. By running inference on edge devices, you can often do away with these layers and overhead.
* **Increased reliability** - If you are operating in an environment with little or no internet connection, your edge devices can still continue to operate. This is important in remote environments or applications like self-driving cars.
* **Improved data privacy** - While IoT devices require care when implementing security plans, you can rest assured that your raw data does not leave your device or edge network. Users can raw data, such as images of their faces, is not leaving the network to be intercepted by malicious actors.

Just like with edge computing, the benefits can be summarized by the acronym BLERP: bandwidth, latency, energy usage, reliability, and privacy.

## Limitations of edge AI

Edge AI has a number of limitations that you should take into consideration and, you should weigh your options carefully versus cloud deployment.

* **Resource constraints** - In general, edge devices offer fewer computational resources than their cloud-based counterparts. Cloud servers can offer powerful processors and large amounts of memory. If your ML model cannot be optimized or constrained to run on an edge device, you should consider a cloud-based solution.
* **Limited remote access** - Prediction serving from the cloud offers easy access from any device that has internet access. Remotely access edge devices often requires special network configuration, such as running a [VPN service](https://en.wikipedia.org/wiki/Virtual_private_network).
* **Scaling** - Scaling prediction services of cloud models usually requires simply cloning your server and paying the service provider more money for additional computing power. With edge computing, you need to purchase and configure additional hardware.

## Examples of edge AI

Edge AI is already being used in our everyday lives as well as offering money savings as an extension of industrial IoT applications. One of the most prominent home automation example of edge AI is the smart speaker.

<Frame caption="Smart speaker">
  <img src="https://mintcdn.com/edgeimpulse/cMDYCG0TzQNU7yvn/.assets/images/what-is-edge-ai-smart-speaker.png?fit=max&auto=format&n=cMDYCG0TzQNU7yvn&q=85&s=24a192feaef47f5435d8b3c1c9046dc0" width="1600" height="900" data-path=".assets/images/what-is-edge-ai-smart-speaker.png" />
</Frame>

The speaker is constantly listening for a key word or phrase ("Alexa" or "Hey Google"). This process is known as "keyword spotting," and it involves performing inference on incoming sound data with a small ML model trained to recognize only that word or phrase. Latency is important here; the speaker needs to respond to the listener within a few milliseconds. It also saves on bandwidth, as the raw audio does not need to be constantly transmitted over the network.

Once the speaker recognizes the keyword, it "wakes up" and begins streaming audio over the internet to a powerful server where a more complex model can perform *intent analysis* to determine what the user is requesting. The smart speaker is a perfect combination of edge AI and cloud AI working in tandem to provide a unique user interaction.

Many smart watches also rely on edge AI.

<Frame caption="Smart watch">
  <img src="https://mintcdn.com/edgeimpulse/cMDYCG0TzQNU7yvn/.assets/images/what-is-edge-ai-smart-watch.png?fit=max&auto=format&n=cMDYCG0TzQNU7yvn&q=85&s=6ac31058ee8b9369af4152b55af9fef2" width="1600" height="900" data-path=".assets/images/what-is-edge-ai-smart-watch.png" />
</Frame>

Some can perform keyword spotting directly on the the watch hardware or are capable of streaming that audio to a connected smartphone for analysis. Either way, the processing is performed on an edge device. They also work with smartphones to analyze sleep patterns and track fitness activities.

Factories and industrial plants are turning to edge AI to help monitor equipment and measure workflows. For example, the [Lexmark Optra](https://www.lexmark.com/en_us/solutions/iot-solutions/optra-platform.html) is a single-board computer that acts as an IoT hub and can perform important analysis jobs like [automated optical inspection](https://en.wikipedia.org/wiki/Automated_optical_inspection) of assembly line parts.

<Frame caption="Lexmark Optra">
  <img src="https://mintcdn.com/edgeimpulse/cMDYCG0TzQNU7yvn/.assets/images/what-is-edge-ai-lexmark-optra.png?fit=max&auto=format&n=cMDYCG0TzQNU7yvn&q=85&s=2658996c29156e2b8ad2ed3e0963ce75" width="1200" height="840" data-path=".assets/images/what-is-edge-ai-lexmark-optra.png" />
</Frame>

Finally, a popular example of edge AI is the self-driving vehicle. These cars, trucks, and buses promise to transport people and goods without needing a human driver.

<Frame caption="Self-driving bus">
  <img src="https://mintcdn.com/edgeimpulse/cMDYCG0TzQNU7yvn/.assets/images/what-is-edge-ai-self-driving.png?fit=max&auto=format&n=cMDYCG0TzQNU7yvn&q=85&s=054be629aad1bac7791b22a08bc14ade" width="1000" height="563" data-path=".assets/images/what-is-edge-ai-self-driving.png" />
</Frame>

Because vehicles cannot rely on a constant internet connection, much of the data processing from the myriad sensors must be performed on the vehicle itself. This means engineers must find a balance between computing power, size, and ML model complexity.

## Market size

The International Data Corporation (IDC) predicts 41.6 billion IoT devices will produce nearly [80 zettabytes that year](https://www.forbes.com/sites/forbestechcouncil/2023/08/08/innovate-or-perish-the-importance-of-modernizing-data-infrastructure/). Additionally, Gartner predicts that [55% of all data analysis by AI and ML](https://www.gartner.com/en/newsroom/press-releases/2023-08-01-gartner-identifies-top-trends-shaping-future-of-data-science-and-machine-learning) algorithms will occur on the same device that captured the raw data in 2025. This figure shows massive growth in edge AI capabilities, up from 10% of on-device processing in 2021. Gartner also predicts that [revenue from specialized AI processors](https://www.gartner.com/en/documents/4848131), such as GPUs and neural processing units (NPUs), will be "\$137 billion by 2027, growing by a five-year CAGR of 26.5%."

The rapid adoption of AI technology and deployment of IoT devices shows how the market is expanding to include edge AI solutions. Note that this is not a shift from cloud-based AI; cloud solutions will continue to grow in addition to edge deployments.

## Going further

Edge AI can be seen as an extension of IoT where data analysis and processing is performed on or close to the sensors that captured the data. While edge AI does not offer the same raw compute power as cloud-based applications, it does help limit bandwidth usage, lower latency, reduce energy consumption, avoid reliance on constant network connection, and enhance data privacy.

To learn more about edge AI, see our guides on [embedded ML](/knowledge/concepts/what-is-embedded-machine-learning-anyway) and [edge ML](/knowledge/concepts/what-is-edge-machine-learning).

## Quiz

Test your knowledge on edge AI with this quiz:

<iframe src="https://docs.google.com/forms/d/e/1FAIpQLScB5-Qq74coBErzEEut0WgGIDOUKAXEOorw5OGZM_CUL4ZozQ/viewform?embedded=true" className="w-full aspect-square rounded-xl" />


Built with [Mintlify](https://mintlify.com).