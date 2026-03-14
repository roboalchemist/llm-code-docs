# Source: https://docs.edgeimpulse.com/studio/projects/retrain-model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrain model

Training and deploying high performing ML models is usually considered as a continuous process rather than a one time exercise. When you are validating your model and discover an overfit, you might consider adding some more diverse data then perform model retraining while maintaining the initially set DSP and Neural Network block configurations.

Also during inference If you find that the data distribution has drifted significantly from the initial training distribution, it is usually a good common practice to retrain your model on the newer data distribution to keep up with the high model performance.

The **Retrain model** feature in the Edge Impulse Studio is useful when adding new data to your project. It uses already known parameters from your selected DSP and ML blocks then uses them to automatically regenerate new features and retrain the Neural Network model in one single step. You can consider this a shortcut for retraining your model since you don’t need to go through all the blocks in your impulse one by one again.

To retrain your model after adding some data, navigate to the **Retrain model** tab and click **Train model**.

<Frame caption="Model retraining.">
  <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/retrain.PNG?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=21b0268cdd532d0079b248ecbe6a3adf" width="1130" height="496" data-path=".assets/images/retrain.PNG" />
</Frame>


Built with [Mintlify](https://mintlify.com).