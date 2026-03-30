# Source: https://docs.edgeimpulse.com/tutorials/topics/data/label-image-data-gpt-4o.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Label image data using GPT-4o

In this tutorial, we will explore how to label image data using GPT-4o, a powerful language model developed by OpenAI. GPT-4o is capable of generating accurate and meaningful labels for images, making it a valuable tool for image classification tasks. By leveraging the capabilities of GPT-4o, we can automate the process of labeling image data, saving time and effort in data preprocessing.

We packaged in a "pre-built [Transformation block](/studio/organizations/custom-blocks/custom-transformation-blocks)" (available for all Enterprise plans), an innovative method to distill LLM knowledge.

This pre-built transformation block can be found under the [Data sources](/studio/projects/data-acquisition/data-sources) tab in the **Data acquisition** view.

The block takes all your unlabeled image files and asks GPT-4o to label them based on your prompt - and we automatically add the reasoning as metadata to your items!

**Your prompt should return a single label**, e.g.

```
Is there a person in this picture? Answer with just 'yes' or 'no'.
```

<iframe src="https://www.youtube.com/embed/Jou0aRgGiis" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## How to use it

The GPT-4o model processes images and assigns labels based on the content, filtering out any images that do not meet the quality criteria.

### Step 1: Data Collection

Navigate to the [Data acquisition](/studio/projects/data-acquisition) page and add images to your project's dataset.
In the video tutorial above, we show how to collect a video recorded directly from a phone, upload it to Edge Impulse and split the video into individual frames.

### Step 2: Add the labeling block

In the [Data sources](/studio/projects/data-acquisition/data-sources) tab, add the "Label image data using GPT-4o" block:

<Frame caption="Add pre-built transformation block">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gpt-4o-labeling.gif?s=ea960ef4d0786be4485940b6c5e10ce3" width="1132" height="738" data-path=".assets/images/gpt-4o-labeling.gif" />
</Frame>

### Step 4: Configure the labeling block

* **OpenAI API key:** Add your OpenAI API key. This value will be stored as a secret, and won't be shown again.
* **Prompt:** Your prompt should return a single label. For example:

```
Is there a person in this picture? Respond only with "yes", "no" or "unsure" if you're not sure.
```

* **Disable samples w/ label:** If a certain label is output, disable the data item - these are excluded from training. Multiple labels are accepted, separate them with a coma.
* **Max. no. of samples to label:** Number of samples to label.
* **Concurrency:** Number of samples to label in parallel.
* **Auto-convert videos:** If set, all videos are automatically split into individual images before labeling.

### Optional: Editing your labeling block

To edit your configuration, you need to update the json-like steps of your block:

<Frame caption="Edit block">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gpt-4o-edit.png?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=2e8db25ad3f33cc5032c8ed0d525b59e" width="1541" height="1000" data-path=".assets/images/gpt-4o-edit.png" />
</Frame>

### Step 5: Execute

Then, run the block to automatically label the frames.

<Frame caption="Job ran successfully">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gpt-4o-execute.png?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=46d52d0f483b5b784d96418da201d3bc" width="1600" height="751" data-path=".assets/images/gpt-4o-execute.png" />
</Frame>

And here is an example of the returned logs:

<Frame caption="GPT-4o labeling block logs">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/gpt-4o-logs.png?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=072a4d7b90f0c1fbb8b05f28fea212af" width="1600" height="835" data-path=".assets/images/gpt-4o-logs.png" />
</Frame>

### Step 6: Train your model

Use the labeled data to train a machine learning model.
See the end-to-end tutorial [Image classification](/tutorials/end-to-end/image-classification).

### Step 7: Deployment

In the video tutorial, we deployed the trained model to an MCU-based edge device - the Arduino Nicla Vision.

## Results

The small model we tested this on performed exceptionally well, identifying toys in various scenes quickly and accurately. By distilling knowledge from the large LLM, we created a specialized, efficient model suitable for edge deployment.

## Conclusion

The latest multimodal LLMs are incredibly powerful but too large for many practical applications. At Edge Impulse, we enable the transfer of knowledge from these large models to smaller, specialized models that run efficiently on edge devices.

Our "Label image data using GPT-4o" block is available for enterprise customers, allowing you to experiment with this technology.

For further assistance, visit our [forum](https://forum.edgeimpulse.com).

## Examples & Resources

* Blog post: [Label image data using GPT-4o blog post](https://www.edgeimpulse.com/blog/llm-knowledge-distillation-gpt-4o/)


Built with [Mintlify](https://mintlify.com).