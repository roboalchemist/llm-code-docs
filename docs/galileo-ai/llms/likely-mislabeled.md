# Source: https://docs.galileo.ai/galileo-ai-research/likely-mislabeled.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Likely Mislabeled

> Garbage in, Garbage out

Training ML models with noisy, mislabeled data can dramatically affect model performance. Dataset errors easily permeate the training process, leading to issues in convergence, inaccurate decision boundaries, and poor model generalization.

On the evaluation side, mislabeled data in a test set will also hurt the ML model's performance, often resulting in lower benchmark scores. Since this is one the biggest factor in deciding whether a model is ready to deploy, we cannot overstate the importance of also having clean test sets.

Therefore, identifying and fixing labeling errors is extremely crucial for both training effective and reliable ML models, and evaluating them accordingly. However, accurately identifying labeling errors is challenging and deploying ineffective algorithms can lead to large, manual efforts with little realized return on investment.

Galileo's mislabel detection algorithm addresses these challenges by employing state of the art statistical methods for identifying data that are highly likely to be *mislabeled*. In the Galileo Console, these samples can be accessed through the *Likely Mislabeled* data tab.

In addition, we surface a tunable parameter which allows the user to fine-tune the method for their use case. The slider balances between precision (minimize number of mistakes) and recall (maximize number of mislabeled samples detected). Hovering over the slider will display a short description, while hovering over the thumb button displays the number of likely mislabeled samples to expect in that position.

For illustration, we highlight a few data samples from the [**Conversational Intent**](https://www.kaggle.com/datasets/joydeb28/nlp-benchmarking-data-for-intent-and-entity) dataset that are correctly identified as mislabeled.

<Frame>
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-1.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=ad6352fff54bd7e6b2ee9d524cb8bacd" data-og-width="1440" width="1440" data-og-height="589" height="589" data-path="images/likely-mislabeled-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-1.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=c982d3a3745607062b431090d48eb4bb 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-1.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=b207316cab2c65b77e091537f04ac83e 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-1.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=7261cf46cf411200dd5b22cab05ce984 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-1.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=1949079ee17317c321843720a37fc03e 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-1.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=3d817217c948918e6ccf9ad7cc9e5b8d 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-1.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=4b8f91c0eaaba60d4d0bd60421b498ad 2500w" />
</Frame>

### Adjusting the slider for your use-case

The *Likely Mislabeled* slider allows the user to fine-tune both the qualitative and quantitive output of the algorithm, depending on your use-case.

<Frame>
  <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-2.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=73498c5ad19bd9fc2e3cc14e46d24923" data-og-width="323" width="323" data-og-height="160" height="160" data-path="images/likely-mislabeled-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-2.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=3f78c4f3c134e31033f4829070dd05f6 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-2.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=37a6f57a885e61b37be28b3986618df5 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-2.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=fb622f298f7cf461609e8635d86e7c93 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-2.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=d343ab46e7496c3a63b7e4f432caa745 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-2.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=07b571df9c69152aa71fb312bf7079b2 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-2.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=b2ccbde391f43696acd970accd83d7d4 2500w" />
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
      <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-3.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=23edbfbd72ae2f58b1ba0ae1251b4815" alt="10-20% Noise" data-og-width="955" width="955" data-og-height="451" height="451" data-path="images/likely-mislabeled-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-3.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=6492cbb5f70bf03a6af910c4fd950767 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-3.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=407837cf53ce70a95061515baad7506d 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-3.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=a0b148814dcada1312276eaf4e30e925 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-3.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=edf6cee18a3930e3f9af8c6a2a63c612 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-3.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=55ca86f9712a83b4967c7f61d7a3fd80 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-3.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=2c471ca347a78832897a2259eafd2f5d 2500w" />
    </Frame>
  </Tab>

  <Tab title="5-10% Noise">
    <Frame caption="The horizontal alignment of the bars matches the position of the slider: the bars to the left are for better Precision and the bars to the right for better Recall.">
      <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-4.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=2fb0c95994ec110e2b79c46051a0595c" alt="5-10% Noise" data-og-width="964" width="964" data-og-height="457" height="457" data-path="images/likely-mislabeled-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-4.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=7976f3af1485551c1b7af8b8d93d16e9 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-4.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=80b84d92d162058fa4101701ff5b92e6 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-4.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=c3d26edafd63d4f051505de392ec60a4 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-4.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=7e1974298034bb59b9f7aa94b6aace63 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-4.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=5e38b3832a909e4a5e26a50c57ae43e5 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-4.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=77f3f0818b304a5b8059f5a775189874 2500w" />
    </Frame>
  </Tab>

  <Tab title="2-5% Noise">
    <Frame caption="The horizontal alignment of the bars matches the position of the slider: the bars to the left are for better Precision and the bars to the right for better Recall.">
      <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-5.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=366301b5a7f43432dc6415086343a3e2" alt="2-5% Noise" data-og-width="964" width="964" data-og-height="461" height="461" data-path="images/likely-mislabeled-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-5.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=e54d0ea37c786ef78b7df91018a7b10c 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-5.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=1a1b243dfde22cdd1a08b863bdfa5368 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-5.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=b1ab663528886cbaf242a8af08a02640 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-5.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=d41101b2638cfd9e3907e1a899973d00 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-5.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=2fd2b08c313c937e00b558ee05be688c 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-5.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=3ab6499f78efaba244810e75b86db016 2500w" />
    </Frame>
  </Tab>

  <Tab title="0-2% Noise">
    <Frame caption="The horizontal alignment of the bars matches the position of the slider: the bars to the left are for better Precision and the bars to the right for better Recall.">
      <img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-6.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=7f09736e2ea7897686d8ce4fd1a0b60b" alt="0-2% Noise" data-og-width="950" width="950" data-og-height="454" height="454" data-path="images/likely-mislabeled-6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-6.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=396d9da8423e08c4f76248c1f8b19877 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-6.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=f5a8aaf0aa3ffe8f8537b580688f06b4 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-6.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=332617c834870de8672b15151d649fc5 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-6.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=59f08f5869d6b1dd109f33ed20653063 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-6.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=0bb4253d5f6f31995b08080a2926cf7a 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/likely-mislabeled-6.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=2319fcceac86eada318293652209c992 2500w" />
    </Frame>
  </Tab>
</Tabs>
