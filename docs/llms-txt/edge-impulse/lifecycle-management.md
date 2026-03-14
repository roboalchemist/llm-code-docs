# Source: https://docs.edgeimpulse.com/knowledge/concepts/lifecycle/lifecycle-management.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Lifecycle management

At Edge Impulse, we recognize that the lifecycle of your impulse is dynamic. As data grows, unanticipated factors, or drift occurs retraining and redeployment becomes essential. Many of our partners have already starting to address this with integrations to our platform, or documenting details for implementation on aspects like OTA updates to your impulse, and Lifecycle Management. We have put together this section to help you understanding and explore how to create your own implementation of a Lifecycle Management system.

## MLOps

MLOps is a set of practices that combines Machine Learning, DevOps, and Data Engineering. The goal of MLOps is to streamline and automate the machine learning lifecycle, including integration, testing, releasing, deployment, and infrastructure management.\\

<Frame caption="MLOps Venn Diagram">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/MLOps_Venn.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=b9e3376ed28277829ad720cba5082c82" width="810" height="790" data-path=".assets/images/MLOps_Venn.png" />
</Frame>

### Continuous Integration, Continuous Deployment and Continuous Learning

Continuous Learning is a key concept in the domain of Machine Learning Operations (MLOps), which is a set of practices that combines Machine Learning, DevOps, and Data Engineering. Here is an example of the process:

<Frame caption="Continuous Learning Sample Architecture">
  <img src="https://mintcdn.com/edgeimpulse/YmjKhgkCrlx3Nxh9/.assets/images/continuous_cycle.png?fit=max&auto=format&n=YmjKhgkCrlx3Nxh9&q=85&s=dba2ae7000299e0e767a134f796b6e26" width="1600" height="957" data-path=".assets/images/continuous_cycle.png" />
</Frame>

### OTA Infrastructure

In this section we will explore how firmware updates and other scenarios are currently addressed, with traditional OTA. It should help you to get started planning your own updated impulse across a range of platforms. Starting with platform-specific examples like Arduino Cloud, Nordic nRF Connect SDK, Zephyr, and Golioth, Particle Workbench and Blues Wireless.

Finally we will explore building an end-to-end example on the Espressif IDF. By covering a cross section of platforms we hope to provide a good overview of the process and how it can be applied to your own project.

With more generic examples like Arduino, Zephyr and C++ which can be applicable to all other vendors.

These [OTA Model Update Tutorials](/knowledge/concepts/lifecycle/ota-model-updates) tutorials will help you to get started.

### Closing the Loop

Edge AI solutions are typically not just about deploying once; it’s about building a Lifecycle Management ecosystem. You can configure your device to send labeled data back to Edge Impulse for ongoing model refinement, and leverage our version control to track your model performance over time.

This bidirectional data flow can be established with a straightforward call to our ingestion API you can explore how to collect data from your board in the following tutorial:

* [Collect Data from Board](/tutorials/tools/apis/studio/collect-data-device)

By integrating these elements, you establish an Lifecycle Management cycle, where the impulse is not static but evolves, learns, and adapts. This adaptation is can be as simple as adding new data to the existing model, or as complex as retraining the model with new data and deploying a new model to the device. Based on metrics you can define, you can trigger this process automatically, or manually. In the esp-idf example, we will explore how to trigger this process manually, and conditionally based on metrics.

* [Espressif IDF end-to-end example](/tutorials/topics/lifecycle-management/ota-espressif-idf)

### Conclusion

We hope this section has helped you to understand the process of Lifecycle Management and how to implement it in your own project. If you have any questions, please reach out to us on our [forum](https://forum.edgeimpulse.com/).


Built with [Mintlify](https://mintlify.com).