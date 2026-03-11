# Source: https://docs.edgeimpulse.com/knowledge/courses/edge-ai-fundamentals/intro-to-edge-ai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Introduction to edge AI

Edge AI is the process of running artificial intelligence (AI) algorithms on devices at the edge of the Internet or other networks. The traditional approach to AI and machine learning (ML) is to use powerful, cloud-based servers to perform model training as well as inference (prediction serving). While edge devices might have limited resources compared to their cloud-based cousins, they offer reduced bandwidth usage, lower latency, and additional data privacy.

<iframe src="https://www.youtube.com/embed/z5lIrWTebOY" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Edge AI series

The following series of articles and videos will guide you through the various concepts and techniques that make up edge AI. We will also present a few case studies that demonstrate how edge AI is being used to solve real-world problems. We encourage you to work through each video and reading section.

You will find a quiz at the end of each written section to test your knowledge. At the end of the course, you will find a comprehensive test. If you pass it with a score of at least 80%, you will be sent a digital certificate showing your completion of the course. You may take the test as many times as you like.

## Contents

We will cover the following concepts with the given learning objectives:

1. [What is edge computing?](/knowledge/courses/edge-ai-fundamentals/what-is-edge-computing)
   * Understand the differences between cloud and edge computing
   * Advantages and disadvantages of processing data on edge devices
   * What is the Internet of Things (IoT)
2. [What is machine learning (ML)?](/knowledge/courses/edge-ai-fundamentals/what-is-machine-learning)
   * What are the differences between artificial intelligence, machine learning, and deep learning
   * Understand the history of AI
   * What are the different categories of machine learning, and what problems do they tackle
3. [What is edge AI?](/knowledge/courses/edge-ai-fundamentals/what-is-edge-ai)
   * Articulate the difference between training and inference
   * How does traditional cloud-based AI inference work
   * What are the benefits of running AI algorithms on edge devices
   * Examples of edge AI systems
   * What are the business implications for future edge AI growth
4. [How to choose an edge AI device](/knowledge/courses/edge-ai-fundamentals/how-to-choose-an-edge-ai-device)
   * Define and provide examples for the different edge computing devices
   * How to choose a particular edge computing device for your edge AI application
5. [Edge AI lifecycle](/knowledge/courses/edge-ai-fundamentals/edge-ai-lifecycle)
   * How to identify a use case where edge AI can uniquely solve a problem
   * Identify constraints to edge AI implementations
   * Understand the edge AI pipeline of collecting data, analyzing the data, feature engineering, training a model, testing the model, deploying the model, and monitoring the model's performance
6. [What is edge MLOPs?](/knowledge/courses/edge-ai-fundamentals/what-is-edge-mlops)
   * Identify the three principles of MLOps: version control, automation, governance
   * Describe the benefits of automating various parts of the edge AI lifecycle
   * Define operations and maintenance (O\&M)
   * How does edge MLOps differ from cloud-based MLOps
   * Define the causes of model drift: data drift and concept drift
7. [What is Edge Impulse?](/knowledge/courses/edge-ai-fundamentals/what-is-edge-impulse)
   * How does a short learning curve lead to faster go-to-market times
   * Articulate the advantages and disadvantages of using an edge AI platform versus building one from scratch
8. [Case study: Izoelectro](/knowledge/courses/edge-ai-fundamentals/case-study-izoelektro)
   * How is edge AI used to detect anomalies on power lines
   * How anomaly detection on edge devices saves power over cloud-based approaches
9. [Going further and certification](/knowledge/courses/edge-ai-fundamentals/test-and-certification)
   * Resources to dive deeper into the technology and use cases of edge AI
   * How to get started with Edge Impulse
   * Comprehensive test and certification

## The network edge

Edge computing is a strategy where data is processed and stored at the periphery of a computer network. In most cases, processing and storing data on remote servers, especially internet servers, is known as "cloud computing." The edge includes all computing devices not part of the cloud.

<Frame caption="Cloud computing vs. edge computing">
  <img src="https://mintcdn.com/edgeimpulse/yWZVbRGeek_I_Jpe/.assets/images/intro-to-edge-ai-cloud-vs-edge.png?fit=max&auto=format&n=yWZVbRGeek_I_Jpe&q=85&s=18c660c0b26e19495cabdb90d6fc7859" width="960" height="540" data-path=".assets/images/intro-to-edge-ai-cloud-vs-edge.png" />
</Frame>

Edge computing devices includes personal computers, smartphones, IoT devices, home and enterprise routing equipment, and remote or regional servers. As these devices become more powerful, we can start to run various AI algorithms on them, which opens up new ways to solve problems.

In the [next section](/knowledge/courses/edge-ai-fundamentals/what-is-edge-computing), we will dive into the advantages and disadvantages of edge computing.

## Quiz

Practice your understanding with the quiz below. Submit your answer and click **View accuracy** to see your score. Note that this will open a new browser tab.

<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSdTp3CwQUL9WaXzJpVH3AMgXgb_-T8Iv3aas_lNBO4x4d63gw/viewform?embedded=true" className="w-full aspect-square rounded-xl" />


Built with [Mintlify](https://mintlify.com).