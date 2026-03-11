# Source: https://docs.edgeimpulse.com/knowledge/concepts/what-is-edge-machine-learning.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is edge machine learning (edge ML)?

Edge machine learning (edge ML) is the process of running machine learning algorithms on computing devices at the periphery of a network to make decisions and predictions as close as possible to the originating source of data. It is also referred to as edge artificial intelligence or edge AI.

In traditional machine learning, we often find large servers processing heaps of data collected from the Internet to provide some benefit, such as predicting what movie to watch next or to label a cat video automatically. By running machine learning algorithms on edge devices like laptops, smartphones, and embedded systems (such as those found in smartwatches, washing machines, cars, manufacturing robots, etc.), we can produce such predictions faster and without the need to transmit large amounts of raw data across a network.

<iframe src="https://www.youtube.com/embed/_1Pl6TmJugE" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

To accurately describe edge ML, we first need to understand the history of artificial intelligence (AI).

> Check out our [Edge AI Fundamentals course](/knowledge/courses/edge-ai-fundamentals/intro-to-edge-ai) to learn more about edge computing, the difference between AI and machine learning, and edge MLOps.

### Artificial intelligence vs. machine learning

The name “artificial intelligence” originates from a [proposal in 1956](http://www-formal.stanford.edu/jmc/whatisai.pdf) by John McCarty, Marvin Minsky, Nathaniel Rochester, and Claude Shannon to host a summer research conference exploring the possibility of programming computers to “simulate many of the higher functions of the human brain.”

Many years later, [McCarthy would define AI](http://www-formal.stanford.edu/jmc/whatisai.pdf) as “the science and engineering of making intelligent machines, especially intelligent computer programs,” where the definition of intelligence is “the computational part of the ability to achieve goals in the world.” From this definition, we see that AI is an extremely broad field of study involving the use of computers to make decisions to achieve arbitrary goals.

AI researcher Arthur Samuel trained a computer to play checkers better than most humans by having the program play thousands of games against itself and learning from each iteration. He coined the term “machine learning” in his [1959 paper](http://www.cs.virginia.edu/~evans/greatworks/samuel1959.pdf) to mean any program that can learn from experience.

The term “deep learning” (DL) comes from a [1986 paper](https://aaai.org/conference/aaai/aaai86/) by the mathematician and computer scientist Rina Dechter. She used the term to describe ML models that can be trained to automatically learn features or representations. We often use the term deep learning to describe [artificial neural networks with more than a few layers](https://en.wikipedia.org/wiki/Deep_learning), but it can be used more broadly to refer to other forms of machine learning.

From these definitions, we can view deep learning as a subset of machine learning, which is a subset of artificial intelligence. As a result, all DL algorithms can be considered ML and AI. However, not all AI is ML.

<Frame caption="Artificial intelligence vs. machine learning vs. deep learning">
  <img src="https://mintcdn.com/edgeimpulse/cMDYCG0TzQNU7yvn/.assets/images/what-is-edge-machine-learning.ai-ml-dl.png?fit=max&auto=format&n=cMDYCG0TzQNU7yvn&q=85&s=7fc08b6a7b3d8a78c2d6529de3262140" width="1600" height="855" data-path=".assets/images/what-is-edge-machine-learning.ai-ml-dl.png" />
</Frame>

Since the early days of AI, advances in algorithms, software, and hardware have allowed us to begin using machine learning in helpful and unique ways.

### Modern machine learning

In the early 2010s, the [Google Brain team](https://research.google.com/teams/brain/?authuser=2) worked to make deep learning more accessible, which resulted in the creation of the popular [TensorFlow](https://www.tensorflow.org/) framework. The team made headlines in 2012 when they created a model that could accurately classify an image as “cat or not cat.”

Since then, AI has soared in popularity, mostly due to the research and development of complex deep neural networks. Powerful graphics cards and server clusters could be employed to speed up the training and inference processes required for deep learning.

<Frame caption="Graphics cards">
  <img src="https://mintcdn.com/edgeimpulse/cMDYCG0TzQNU7yvn/.assets/images/what-is-edge-machine-learning.gfx-cards.jpeg?fit=max&auto=format&n=cMDYCG0TzQNU7yvn&q=85&s=9a58981f220b0d67ca1b44d38b6e479e" width="1500" height="1000" data-path=".assets/images/what-is-edge-machine-learning.gfx-cards.jpeg" />
</Frame>

These powerful algorithms are used everyday to perform a variety of helpful tasks, such as:

* Image and video labeling
* Speech recognition and synthesis
* Language translation
* Product and content recommendations
* Email spam filtering
* Credit card fraud detection
* Market and customer segmentation
* Stock market trading

To train these complex machine learning models, we need enormous amounts of data. Thanks to the Internet, that data can be readily obtained by sharing pre-made datasets or through actively collecting information in real time (e.g. usage statistics of a website). If we want to collect data from the world around us, we need to rely on sensors.

### The Internet of Things

The Internet of Things (IoT) is the collection of sensors, hardware devices, and software that exchange information with other devices and computers across communication networks. We often think of IoT as a series of sensors with WiFi or Bluetooth connectivity that can relay to us information about the environment.

<Frame caption="Graphic depicting the Internet of Things (IoT)">
  <img src="https://mintcdn.com/edgeimpulse/cMDYCG0TzQNU7yvn/.assets/images/what-is-edge-machine-learning.iot-diagram.jpeg?fit=max&auto=format&n=cMDYCG0TzQNU7yvn&q=85&s=3a8b3e56cb62a389c0001c4c85fb3903" width="1600" height="941" data-path=".assets/images/what-is-edge-machine-learning.iot-diagram.jpeg" />
</Frame>

In 1982, a few graduate students in the computer science department at Carnegie-Mellon [connected a Coca-Cola vending machine to the Internet](https://www.cs.cmu.edu/~coke/history_long.txt) for fun. The machine would display its temperature and various soda stock in real time to a web page. This project is the first known instance of IoT.

For many years, IoT was known as “[machine to machine](https://en.wikipedia.org/wiki/Machine_to_machine)” (M2M). It involved connecting sensors and automating control processes between various computing devices, and it saw wide adoption in industrial machines and processes.

Machine learning offers the ability to create further advancements in automation by introducing models that can make predictions or decisions without human intervention. Due to the complex nature of many machine learning algorithms, the traditional integration of IoT and ML involves sending raw sensor data to a central server, which performs the necessary inference calculations to generate a prediction.

<Frame caption="Data flow diagram for machine learning with connected sensors">
  <img src="https://mintcdn.com/edgeimpulse/cMDYCG0TzQNU7yvn/.assets/images/what-is-edge-machine-learning.iot-ml.png?fit=max&auto=format&n=cMDYCG0TzQNU7yvn&q=85&s=75280aa6535869970b38ace1fb4fc446" width="1600" height="381" data-path=".assets/images/what-is-edge-machine-learning.iot-ml.png" />
</Frame>

For low volumes of raw data and complex models, this configuration may be acceptable. However, there are several potential issues that arise:

* Transmitting large sensor data, such as images, may hog network bandwidth
* Transmitting data also requires power
* The sensors require constant connection to the server to provide near real time ML computations

To counter the need to transmit large amounts of raw data across networks, data storage and some computations can be accomplished on devices closer to the user or sensor, known as the “edge.” Qualcomm’s Karim Arabi, in his 2014 IEEE DAC keynote and [2015 MIT MTL Seminar](https://www.mtl.mit.edu/seminars/trends-opportunities-and-challenges-driving-architecture-and-design-next-generation-mobile), defined edge computing as all computing happening outside of the cloud. Edge computing stands in contrast to [cloud computing](https://en.wikipedia.org/wiki/Cloud_computing), where remote data and services are available on demand to users.

Edge computing includes personal computers and smartphones in addition to embedded systems (such as those that comprise the Internet of things). To make all of these devices smarter and less reliant on backend servers, we turn to edge machine learning.

### Edge and embedded machine learning

Advances in hardware and machine learning have paved the way for running deep ML models efficiently on edge devices. Complex tasks, such as object detection, natural language processing, and model training, still require powerful computers. In these cases, raw data is often collected and sent to a server for processing.

However, performing ML on low-power devices offers a variety of benefits:

* Less network bandwidth is spent on transmitting raw data
* While some information may need to be transmitted over a network (e.g. inference results), less communication often means reduced power usage
* Prediction results are available immediately without the need to send them across a network
* Inference can be performed without a connection to a network
* User privacy is ensured, as data is only stored long enough to perform inference (not including data collected for model training)

Edge ML includes personal computers, smartphones, and embedded systems. As a result, [embedded ML](/knowledge/concepts/what-is-embedded-machine-learning-anyway), also known as [tinyML](https://www.tinyml.org/), is a subset of edge ML that focuses on running machine learning algorithms on embedded systems, such as microcontrollers and headless single board computers.

In most cases, training a machine learning model is more computational intensive than performing inference.

<Info>
  **Model**: the mathematical formula that attempts to generalize information from a given set of data.

  **Training**: the process of automatically updating the parameters in a model from data. The model “learns” to draw conclusions and make generalizations about the data.

  **Inference**: the process of providing new, unseen data to a trained model to make a prediction, decision, or classification about the new data.
</Info>

As a result, we often rely on powerful server farms to train new models. This requires collecting data from the field (with sensors, scraping Internet images, etc.) to construct a dataset and using that dataset to train our machine learning model.

<Frame caption="Machine learning model training in the cloud using data from IoT sensors">
  <img src="https://mintcdn.com/edgeimpulse/cMDYCG0TzQNU7yvn/.assets/images/what-is-edge-machine-learning.edge-ml-training.png?fit=max&auto=format&n=cMDYCG0TzQNU7yvn&q=85&s=9a5c2b3c7f13d9a96026560c756813f5" width="1600" height="364" data-path=".assets/images/what-is-edge-machine-learning.edge-ml-training.png" />
</Frame>

Note that in some cases, we can perform on-device training. However, this is often infeasible due to the memory and processing limitations of such edge devices.

Once we have a trained model, which is just a mathematical model (in the form of a software library), we can deploy it to our smart sensor or other edge device. We can write firmware or software using the model to gather new raw sensor readings, perform inference, and take some action based on those inference results.

Such actions might be autonomously driving a car, moving a robotic arm, or sending a notification of a faulty motor to a user. Because inference is performed locally on the edge device, the device does not need to maintain a network connection (optional connection shown as a dotted line in the diagram).

<Frame caption="How a machine learning model is deployed to an edge device">
  <img src="https://mintcdn.com/edgeimpulse/cMDYCG0TzQNU7yvn/.assets/images/what-is-edge-machine-learning.edge-ml-deployment.png?fit=max&auto=format&n=cMDYCG0TzQNU7yvn&q=85&s=aa9bc532663954d79317660ba6a057d4" width="1117" height="407" data-path=".assets/images/what-is-edge-machine-learning.edge-ml-deployment.png" />
</Frame>

ML models are not perfect. They provide a generalization of the training data. In other words, the model is only as good as the data used to train it. As a result, machine learning (and the subsequent field of data-driven engineering) will not replace traditional programming. However, it nicely complements other types of software engineering, and it opens new possibilities for solving difficult problems.

### Edge ML use cases

The ability to run machine learning on edge devices without the need to maintain a connection to a more powerful computer allows for a variety of automation tools and smarter IoT systems. Here are a few examples where edge ML is enabling innovation in various industries.

<Frame caption="Example of an edge machine learning device used to monitor power lines">
  <img src="https://mintcdn.com/edgeimpulse/cMDYCG0TzQNU7yvn/.assets/images/what-is-edge-machine-learning.smart-grid.png?fit=max&auto=format&n=cMDYCG0TzQNU7yvn&q=85&s=72058c6d1fea67cb53d57561d365cf14" width="1302" height="746" data-path=".assets/images/what-is-edge-machine-learning.smart-grid.png" />
</Frame>

Agriculture

* [Automatically identifying irrigation requirements](https://assets-global.website-files.com/618cdeef45d18e4ef2fd85f3/621cef64de63616986408c70_AI-Managed-Crops-Irrigation.pdf)
* [ML-powered robots](https://assets-global.website-files.com/618cdeef45d18e4ef2fd85f3/621cee6500297d2199a183b0_ML-Powered-Agricultural-Robotics.pdf) for recording crop trials

Smart buildings

* [Smart HVAC systems](https://environment.umn.edu/education/susteducation/pathways-to-renewable-energy/how-a-smart-hvac-system-can-increase-efficiency-while-saving-you-money/) that can adapt to the number of people in a room
* Security sensors that listen for the unique sound signature of glass breaking

Environment conservation

* [Smart grid monitoring](https://assets-global.website-files.com/618cdeef45d18e4ef2fd85f3/621cef966699cbc24cdae67e_Smart-Grid-Monitoring.pdf) that looks for early faults in power lines
* [Wildlife tracking](https://edgeimpulse.com/blog/smartparks)

Health and fitness

* [Portable medical devices](https://assets-global.website-files.com/618cdeef45d18e4ef2fd85f3/621cef625e602ddcddf070fe_Early-Blindness-%26-Diabetic-Retinophaty-Detection.pdf) that can identify diseases from images
* [Digital Health Solution Guide](https://assets.website-files.com/618cdeef45d18e4ef2fd85f3/6564d926ffd281023e5fb356_next-generation-digital-health-gecomprimeerd_1.pdf)

Human-computer interaction (HCI)

* Keyword spotting and wake word detection to control household appliances
* Gesture control as assistive technology

Industry

* [Safety systems](https://assets-global.website-files.com/618cdeef45d18e4ef2fd85f3/621cef628758fd1c35be832b_AI-Automated-Hard-Hat-Detection.pdf) that automatically detect the presence of hard hats
* Predictive maintenance that identities faults in machinery before larger problems arise

The computational power required to perform machine learning at the edge is generally much higher than simply needing to poll a sensor and transmit raw data. However, performing such calculations locally often requires less electrical power than transmitting the raw data to a remote server.

The following chart offers some insights into the types of hardware required to perform machine learning inference at the edge depending on the desired application.

<Frame caption="Chart showing machine learning use cases with their respective hardware requirements">
  <img src="https://mintcdn.com/edgeimpulse/cMDYCG0TzQNU7yvn/.assets/images/what-is-edge-machine-learning.ml-hw-vs-applications.png?fit=max&auto=format&n=cMDYCG0TzQNU7yvn&q=85&s=e9b10a51e7486b67f085687939a8239c" width="1600" height="737" data-path=".assets/images/what-is-edge-machine-learning.ml-hw-vs-applications.png" />
</Frame>

Edge ML is enabling technologies in new areas and allowing for novel solutions to problems. Some of these applications will be visible to consumers (such as keyword spotting on smart speakers) while others will be transforming our lives in invisible ways (such as smart grids delivering power more efficiently).

### Learn more

Edge Impulse is the leading development platform for machine learning on edge devices. One of the fastest ways to try Edge Impulse is to follow this guided tour of [creating your own keyword spotting model in 5 minutes](https://studio.edgeimpulse.com/studio/profile/projects?createNewProject=1\&tutorial=kws) or our [computer vision walkthrough](https://studio.edgeimpulse.com/studio/profile/projects?createNewProject=1\&tutorial=cv). No programming experience is required!


Built with [Mintlify](https://mintlify.com).