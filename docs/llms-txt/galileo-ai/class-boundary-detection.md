# Source: https://docs.galileo.ai/galileo-ai-research/class-boundary-detection.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Class Boundary Detection

> Detecting samples on the decision boundary

Stay tuned for future announcements.

Understanding a model's decision boundaries and the samples that exist near or on these decision boundaries is critical when evaluating a model's robustness and performance. A model with poorly defined decision boundaries is prone to making low confidence and erroneous predictions.

Galileo's **On the Boundary** feature highlights data cohorts that exist near or on these decision boundaries - i.e. data that the model struggles to discern between distinct classes. Identifying these samples reveals high ROI data that are not well distinguished by the model (i.e. confidently predicted as a certain class) and are likely to be poorly classified. Moreover, tracking these samples in production can reveal overlapping class definitions and signal a need for model and data tuning to better differentiate select classes.

Within the Galileo Console, selecting the **On the Boundary** tab filters exactly the samples existing between the model's learned definition of classes:

<img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-class-boundary-detection-1.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=6a88c44129a8c7d582e6f730b854f7ed" alt="Full Dataset View - Samples Colored by Class Label" data-og-width="2680" width="2680" data-og-height="1840" height="1840" data-path="images/nlp-class-boundary-detection-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-class-boundary-detection-1.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=dd5a070d722177e27de918dad9c1ad95 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-class-boundary-detection-1.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=2290508b1f4d5b5c2815592b212969ad 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-class-boundary-detection-1.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=915f102944afd2a24687433a4de17781 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-class-boundary-detection-1.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=6e247e68944f07f6b3c97480e73dc417 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-class-boundary-detection-1.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=266a61547d5b104f4e51472da3430fd5 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-class-boundary-detection-1.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=9a035659674ac399c4ccdb9ecf117401 2500w" />

<img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-class-boundary-detection-2.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=caaa82ce8f5b2eef601dacdeb5075dec" alt="On the boundary - samples on the model's decision boundary" data-og-width="2680" width="2680" data-og-height="1840" height="1840" data-path="images/nlp-class-boundary-detection-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-class-boundary-detection-2.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=16861907e0b1278068a71aa703061196 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-class-boundary-detection-2.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=7f562bdf2f11ef2d3dc23d73c3fc4f97 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-class-boundary-detection-2.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=84d3590ff777ca3b7cfe8c2aa605da95 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-class-boundary-detection-2.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=6f151cc207b306b5a707708bf6479557 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-class-boundary-detection-2.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=d7d1a25ef1355548a3f28601015cafba 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/nlp-class-boundary-detection-2.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=1db16e77fc8e4e90cd1845f4a1df1949 2500w" />

#### On the Boundary Calculation

On the boundary samples are identified by analyzing the model's output probability distribution. Given the model's output probabilities, we analyze the model's class confusion through computing per-sample certainty ratios - a metric computed as the ratio between a model's most confident predictions. Certainty ratios provide intuitive measures of class confusion not captured by traditional methods such as confidence. Through smart thresholding, we then identify samples that are particularly confused between two or more prediction classes.
