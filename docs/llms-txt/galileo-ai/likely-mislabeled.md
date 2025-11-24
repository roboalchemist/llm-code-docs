# Source: https://docs.galileo.ai/galileo-ai-research/likely-mislabeled.md

# Likely Mislabeled

> Garbage in, Garbage out

Training ML models with noisy, mislabeled data can dramatically affect model performance. Dataset errors easily permeate the training process, leading to issues in convergence, inaccurate decision boundaries, and poor model generalization.

On the evaluation side, mislabeled data in a test set will also hurt the ML model's performance, often resulting in lower benchmark scores. Since this is one the biggest factor in deciding whether a model is ready to deploy, we cannot overstate the importance of also having clean test sets.

Therefore, identifying and fixing labeling errors is extremely crucial for both training effective and reliable ML models, and evaluating them accordingly. However, accurately identifying labeling errors is challenging and deploying ineffective algorithms can lead to large, manual efforts with little realized return on investment.

Galileo's mislabel detection algorithm addresses these challenges by employing state of the art statistical methods for identifying data that are highly likely to be *mislabeled*. In the Galileo Console, these samples can be accessed through the *Likely Mislabeled* data tab.

In addition, we surface a tunable parameter which allows the user to fine-tune the method for their use case. The slider balances between precision (minimize number of mistakes) and recall (maximize number of mislabeled samples detected). Hovering over the slider will display a short description, while hovering over the thumb button displays the number of likely mislabeled samples to expect in that position.

For illustration, we highlight a few data samples from the [**Conversational Intent**](https://www.kaggle.com/datasets/joydeb28/nlp-benchmarking-data-for-intent-and-entity) dataset that are correctly identified as mislabeled.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/likely-mislabeled-1.png" />
</Frame>

### Adjusting the slider for your use-case

The *Likely Mislabeled* slider allows the user to fine-tune both the qualitative and quantitive output of the algorithm, depending on your use-case.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/likely-mislabeled-2.png" />
</Frame>

On one extreme it will optimize for maximum Recall: this maximizes the number of mislabeled samples caught by the algorithm and in most cases ensures 90% of mislabeled points caught (see results below).

On the other extreme it will optimize for maximum Precision: this minimizes the number of errors made by the algorithm, i.e., it minimizes the number of datapoints which are not mislabeled but are marked as likely mislabeled.

#### Setting the threshold for a common use-case: fixed re-labelling budget

Suppose that we have a relabelling budget of only 200 samples. Start with the slider on the Recall side where the algorithm returns all the samples that are likely to be mislabeled. As you move the thumb of the slider towards the Precision side, a hovering box will appear and you should notice the number of samples decreasing, allowing you to fine-tune the algorithm for returning the 200 samples that are most likely to be mislabeled.

### Likely Mislabeled Computation

Galileo's *Likely Mislabeled* *Algorithm* is adapted from the well known '**Confident Learning**' algorithm. The working hypothesis of confident learning is that counting and comparing a model's "confident" predictions to the ground truth can reveal class pairs that are most likely to have class confusion. We then leverage and combine this global information with per-sample level scores, such as [DEP](/galileo/gen-ai-studio-products/galileo-ai-research/galileo-data-error-potential-dep) (which summarizes individual data sample training dynamics), to identify samples most likely to be mislabeled.

This technique particularly shines in multi-class settings with potentially overlapping class definitions, where labelers are more likely to confuse specific scenarios.

### DEP vs. Likely Mislabeled

Although related, [Galileo's DEP score](/galileo/gen-ai-studio-products/galileo-ai-research/galileo-data-error-potential-dep) is distinctly different from the *Likely Mislabeled* algorithm: samples with a higher DEP score are not necessarily more likely to be mislabeled (even though the opposite is true). While *Likely Mislabeled* focuses solely on the potential for being mislabeled, DEP more generally measures the potential for "misfit" of an observation to the given model. As described in our documentation, the categorization of "misfit" data samples includes:

* *Mislabeled* *samples* (annotation mistakes)
* Boundary samples or overlapping classes
* Outlier samples or Anomalies
* Noisy Input
* Misclassified samples
* Other errors

Through summarizing per-sample training dynamics, DEP captures and categorizes *many* different sample level errors without specifically differentiating / pinpointing a specific one.

### Likely Mislabeled evaluation

To measure the effectiveness of the *Likely Mislabeled* algorithm, we performed experiments on 10+ datasets covering various scenarios such as binary/multi-class text classification, balanced/unbalanced distribution of classes, etc. We then added various degrees of noise to these datasets and trained different models on them. Finally, we evaluated the algorithm on how well it is able to identify the noise manually added.

Below are plots indicating the Precision and Recall of the algorithm.

<Tabs>
  <Tab title="10-20% Noise">
    <Frame caption="The horizontal alignment of the bars matches the position of the slider: the bars to the left are for better Precision and the bars to the right for better Recall.">
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/likely-mislabeled-3.png" alt="10-20% Noise" />
    </Frame>
  </Tab>

  <Tab title="5-10% Noise">
    <Frame caption="The horizontal alignment of the bars matches the position of the slider: the bars to the left are for better Precision and the bars to the right for better Recall.">
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/likely-mislabeled-4.png" alt="5-10% Noise" />
    </Frame>
  </Tab>

  <Tab title="2-5% Noise">
    <Frame caption="The horizontal alignment of the bars matches the position of the slider: the bars to the left are for better Precision and the bars to the right for better Recall.">
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/likely-mislabeled-5.png" alt="2-5% Noise" />
    </Frame>
  </Tab>

  <Tab title="0-2% Noise">
    <Frame caption="The horizontal alignment of the bars matches the position of the slider: the bars to the left are for better Precision and the bars to the right for better Recall.">
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/likely-mislabeled-6.png" alt="0-2% Noise" />
    </Frame>
  </Tab>
</Tabs>
