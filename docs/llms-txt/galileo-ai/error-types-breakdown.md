# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/galileo-product-features/error-types-breakdown.md

# Error Types Breakdown

> For use cases with complex data and error types (e.g. Named Entity Recognition, Object Detection or Semantic Segmentation), the **Error Types Chart** gives you an insight into exactly how the Ground Truth differed from your model's predictions

It allows you to get a sense of what types of mistakes your model is making, with what frequency and, in the case of Object Detection, what impact these errors had on your overall performance metric.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/e-t.png" />
</Frame>

Error Types for a Object Detection model

**How does this work?**

For Named Entity Recognition, Galileo surfaces *Ghost Spans, Span Shifts, Missed Spans* or *Wrong Tag Errors*.

For Object Detection, Galileo leverages the [TIDE](https://arxiv.org/abs/2008.08115) framework to find associations between Ground Truth and Predicted objects and break differences between the two into one of: *Localization*, *Classification*, *Background*, *Missed*, *Duplicates* or *Localization and Classification* mistakes. See a thorough write-up of how that's done and the definition of each error type [here](/galileo/gen-ai-studio-products/galileo-ai-research/errors-in-object-detection).

**How should I leverage this chart?**

Click on an error type to filter the dataset to samples with that error type. From there, you can inspect your erroneous samples and fix them.

One common flow we see is selecting *Ghost Spans (NER)* or *Background Confusion Errors* (Obj. Detection) combined with a high DEP filter can be used to surface Missed Annotations from your labelers. You can send these samples to your labeling tool or fix them with the Galileo console.
