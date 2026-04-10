# Source: https://docs.edgeimpulse.com/knowledge/guides/combining-impulses.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Combining impulses

Are you not sure how to design complex impulses? Here are some ways you can combine your impulses or data to suit your needs.

**Multi-impulse vs multi-model vs sensor fusion**

<Frame caption="Multi-impulse vs sensor fusion vs multi-model">
  <img src="https://mintcdn.com/edgeimpulse/knIbhhrHdvFnasBb/.assets/images/multi-impulse-vs-multi-model-vs-sensor-fusion.png?fit=max&auto=format&n=knIbhhrHdvFnasBb&q=85&s=3d86fc46f7209394cf6bfda493a3aaa4" width="1600" height="903" data-path=".assets/images/multi-impulse-vs-multi-model-vs-sensor-fusion.png" />
</Frame>

**Multi-impulse** refers to running two separate impulses (different data, different processing blocks, and different learning blocks) on the same device. It requires creating two projects and modifying some files in the EI-generated SDK. To make this easier, we have created a [multi-impulse deployment block](https://github.com/edgeimpulse/multi-impulse-deployment-block/) to generate the export package. This deployment block is available for users on the Enterprise plan. Please see the [Multi-impulse](/tutorials/topics/inference/run-multiple-impulses-cpp) tutorial for further details.

**Multi-model** refers to running two different learning blocks (same data, same processing block, and different learning blocks) on the same device. See how to run a motion classifier model and an anomaly detection model on the same device in the [Continuous motion recognition](/tutorials/end-to-end/motion-recognition) tutorial. Currently, we only support stacking a Keras learning block with an anomaly detection learning block.

**Sensor fusion** refers to the process of combining data from different types of sensors to give more information to the learning block. To extract meaningful information from this data, you can use the same processing block (like in the [Sensor fusion](/tutorials/end-to-end/environmental-sensor-fusion) tutorial), multiple processing blocks, or use neural network embeddings (like in the [Sensor fusion using embeddings](/tutorials/topics/feature-extraction/use-embeddings-sensor-fusion) tutorial).

These concepts are also discussed in the video below (starting at min 13):

<iframe src="https://www.youtube.com/embed/ts1e3_aMQ8Y?start=783" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />


Built with [Mintlify](https://mintlify.com).