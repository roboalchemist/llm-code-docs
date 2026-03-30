# Source: https://docs.edgeimpulse.com/knowledge/courses/edge-ai-fundamentals/what-is-machine-learning.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is machine learning (ML)?

Machine learning (ML) is a branch of artificial intelligence (AI) and computer science that focuses on developing algorithms and programs that can learn over time. ML specifically focuses on building systems that learn from data.

In the last article, we discussed the advantages and disadvantages of [edge computing](/knowledge/courses/edge-ai-fundamentals/what-is-edge-computing). This time, we define machine learning, how it relates to AI, and how it differs from traditional, rules-based programming.

<iframe src="https://www.youtube.com/embed/RDGCGho5oaQ" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Differences between human and artificial intelligence

One way to understand AI is to compare it to human intelligence. In general, we consider human intelligence in terms of our ability to solve problems, set and achieve goals, analyze and reason through problems, communicate and collaborate with others, as well as an awareness of our own existence (consciousness).

AI is the ability for machines to simulate and enhance human intelligence. Unlike humans, AI is still a rules-based system and does not need elements of emotions or consciousness to be useful.

In their 2016 book, *Artificial Intelligence: A Modern Approach*, Stuart Russell and Peter Norvig define AI as "the designing and building of intelligent agents that receive precepts from the environment and take actions that affect that environment."

## Machine learning vs. artificial intelligence

Machine learning is a subset of artificial intelligence. AI is a broad category that covers many systems and algorithms.

<Frame caption="Data science vs ai vs ml vs deep learning">
  <img src="https://mintcdn.com/edgeimpulse/cMDYCG0TzQNU7yvn/.assets/images/what-is-ml-ds-vs-ai-vs-ml.png?fit=max&auto=format&n=cMDYCG0TzQNU7yvn&q=85&s=d71b41063ebf0850dd8094eaf8d0e7c7" width="458" height="462" data-path=".assets/images/what-is-ml-ds-vs-ai-vs-ml.png" />
</Frame>

Both AI and ML can be considered subsets of data science, which is the application of the scientific method to extract insights from data to make decisions or predictions. For example, an investment banker might look at stock trends or other factors to figure out the best time to buy and sell securities. Additionally, a software engineer might develop a computer vision model to identify cars in images (as images are a form of data).

As described earlier, AI is the development of algorithms and systems to simulate human intelligence. This can include automatically making decisions based on input data as well as systems that can learn over time.

Machine learning, on the other hand, is the development of algorithms and systems that learn over time from data. Often, such algorithms include the development of mathematical and statistical models that have been trained on input data. These models are capable of extracting patterns from the input data to come up with rules that can make decisions and predictions.

Deep learning, a term coined by computer scientist [Rina Dechter](https://en.wikipedia.org/wiki/Rina_Dechter) in 1986, describes ML models that are more complex and can learn representations from the data in successive layers. Deep learning has been the most studied and hyped form of ML since 2010.

## A brief history of AI

While AI seems like a recent invention, the study of mathematical models that can update themselves dates back to the 1700s.

<Frame caption="Brief history of AI">
  <img src="https://mintcdn.com/edgeimpulse/cMDYCG0TzQNU7yvn/.assets/images/what-is-ml-ai-history.png?fit=max&auto=format&n=cMDYCG0TzQNU7yvn&q=85&s=3d985b159d06bfca4ec0b9d54592873e" width="960" height="485" data-path=".assets/images/what-is-ml-ai-history.png" />
</Frame>

Carl Friedrich Gauss studied linear regression, which is evidenced by the [Gauss-Markov theorem](https://en.wikipedia.org/wiki/Gauss%E2%80%93Markov_theorem). The theorem, a collaboration between Gauss and Andrey Markov, was released in a 1821 publication. As regression algorithms are a form of mathematical model that improves over time given additional data, we consider them part of machine learning (and, as a result, a part of AI).

The term "artificial intelligence" came from John McCarthy's proposal to host a conference in 1956 for academics to discuss the possibility of developing intelligent machines. This gathering was known as the "Dartmouth Summer Research Project on Artificial Intelligence."

After the Dartmouth conference, research and public interest in AI flourished. Computer technology improved exponentially, which allowed for early AI and ML systems to be developed. However, AI eventually stalled in the 1970s, when computers could not store information or process data fast enough to keep up with the algorithm research.

The late 1970s and early 1980s witnessed the first "AI winter," where public interest in AI died, and research funding evaporated. The mid-1980s saw a resurgence of interest with [symbolic AI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence) and [expert systems](https://en.wikipedia.org/wiki/Expert_system). As computers at the time were powerful enough to run these complex algorithms, AI programs could be employed to solve real problems in industry.

The technique of automatically adjusting weights in a weighted sum of inputs was well known in [Guass's time](https://en.wikipedia.org/wiki/Neural_network_\(machine_learning\)#History). This formed the basis for the "perceptron," which eventually gave way to the "[multilayer perceptron](https://en.wikipedia.org/wiki/Feedforward_neural_network)" in the 1950s. The idea of using multiple perceptrons to predict values as a machine learning tool was inspired by the human brain's massive interconnected network of neurons, thus inspiring the name "neural network" (or more specifically, "artificial neural network"). Even though Rina Dechter published her paper in 1986 coining the term "deep learning," it would be at least 20 years before neural networks became popular.

The second AI winter occurred in the early 2000s. Government research funding died as did public interest in AI. However, the current deep learning revolution started in 2010 with newfound interest in large, complex machine learning models, mostly built using neural networks. This AI renaissance came about thanks to several important factors:

1. Massive amounts of data is being generated from personal computers easily accessible via the internet
2. Computers, including accelerators like graphics processing units (GPU), became powerful enough to run deep learning models with relative ease
3. New, complex deep learning models were developed that surpassed classical, non-neural-network algorithms in accuracy
4. Public interest surged with renewed vigor after several high-profile media publications, including Microsoft's Kinect for Xbox 360 released in 2010, IBM Watson winning on Jeopardy in 2011, and Apple unveiling Siri in 2011

[AlexNet](https://en.wikipedia.org/wiki/AlexNet), a deep neural network designed in 2012, surpassed all previous computer vision models at recognizing images. This marked the turning point in AI development, where deep learning became the primary model architecture and focus for researchers.

Since 2010, we have seen a resurgence in AI funding and interest. The availability of large amounts of data and capable computers have kept pace with machine learning research. As a result, ML has entered our lives through nearly every piece of computing equipment.

## Categories of ML

Machine learning can be broadly categorized into supervised learning, unsupervised learning, and reinforcement learning.

<Frame caption="Machine learning categories">
  <img src="https://mintcdn.com/edgeimpulse/cMDYCG0TzQNU7yvn/.assets/images/what-is-ml-categories.png?fit=max&auto=format&n=cMDYCG0TzQNU7yvn&q=85&s=3f1c5910514b8dcf4bae97de3d3e10ca" width="955" height="417" data-path=".assets/images/what-is-ml-categories.png" />
</Frame>

Supervised learning is concerned with finding a function (or mathematical model) that maps input data to some output, such as a predicted value or classification. Supervised learning requires ground-truth labels to be present with the data during training. Such labels are usually set by humans.

Supervised learning can be subdivided into two further categories. In regression, the model attempts to predict a continuous value. For example, regression can be used to predict a house's price based on various input factors (such as livable area, location, size, etc.). Classification is the process of predicting how well the input data belongs to one (or more) of several discrete classes.

Unsupervised learning is used to identify patterns in data. As such, no ground-truth labels are used. Examples of unsupervised learning are clustering, outlier (anomaly) detection, and segmentation.

Reinforcement learning focuses on models that learn a policy that selects actions based on provided input. Such models attempt to achieve goals through trial and error by interacting with the environment.

Other categories of ML exist, such as semi-supervised learning, and they often involve combinations of the main three categories.

## Traditional vs. machine learning algorithms

When developing traditional algorithms, the parameters and rules of the system are designed by a human. Such algorithms accept data as input and produce results.

<Frame caption="Traditional algorithm development">
  <img src="https://mintcdn.com/edgeimpulse/cMDYCG0TzQNU7yvn/.assets/images/what-is-ml-traditional-algorithms.png?fit=max&auto=format&n=cMDYCG0TzQNU7yvn&q=85&s=3142f2d94ced7aec7b6159ec218ae5d7" width="662" height="133" data-path=".assets/images/what-is-ml-traditional-algorithms.png" />
</Frame>

Some examples of traditional programming algorithms include:

* [Edge detection](https://en.wikipedia.org/wiki/Edge_detection) filters are used to extract meaning from images
* [Sorting algorithms](https://en.wikipedia.org/wiki/Sorting_algorithm) are popular with search engines to present web search results
* The [Fourier transform](https://en.wikipedia.org/wiki/Fourier_transform) is used in signal processing to convert a time-series data sample into its various frequency components
* [Advanced Encryption Standard (AES)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) is a popular encryption protocol to keep data secret during transmission

Note that some artificial intelligence algorithms, including classical [symbolic AI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence) and [expert systems](https://en.wikipedia.org/wiki/Expert_system), fall into this category, as the rules are built by humans. They are AI algorithms but not considered "machine learning."

<Frame caption="Machine learning rules creation and deployment">
  <img src="https://mintcdn.com/edgeimpulse/cMDYCG0TzQNU7yvn/.assets/images/what-is-ml-training-inference.png?fit=max&auto=format&n=cMDYCG0TzQNU7yvn&q=85&s=0f3f0be35f3f06a7134867f0f1f3be4f" width="835" height="376" data-path=".assets/images/what-is-ml-training-inference.png" />
</Frame>

In machine learning, the ML training algorithm automatically develops the parameters and rules based on the input data. For supervised learning, you provide the input data along with the ground-truth answers or labels. During the training phase, the ML algorithm develops the rules to classify the input data as accurately as possible.

The rules developed during the training phase is a mathematical or statistical model and is often referred to as a "model."

The rules (model) can then be used to predict answers and values from new data that was never seen during training. This process is known as "inference," as the model is attempting to infer values or meaning from new data. If the rules perform well on this task (with never-before-seen input data), then we can say that the ML model is "generalizing" well.

## Going further

Machine learning can help solve unique problems where traditional rules-based designs fall short. If you would like to dive into the technical details of how neural networks operate, see our [neural networks](/knowledge/concepts/machine-learning/neural-networks) concepts article.

## Quiz

Test your knowledge of machine learning with the following quiz.

<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSepVwShKv-J966pEfNiArOALGVvoee_aKvtJ9EHNBV0ofV63w/viewform?embedded=true" className="w-full aspect-square rounded-xl" />


Built with [Mintlify](https://mintlify.com).