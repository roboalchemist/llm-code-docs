# Source: https://docs.aporia.com/core-concepts/understanding-data-drift.md

# Source: https://docs.aporia.com/v1/core-concepts/understanding-data-drift.md

# Understanding Data Drift

### What is Data Drift?

Data drift occurs when the distribution of *production data* is different from a certain baseline (e.g *training data*).

The model isn't designed to deal with this change in the feature space and so, its predictions may not be reliable. Drift can be caused by changes in the real world or by data pipeline issues - missing data, new values, changes to the schema, etc.

It's important to look at the data that has drifted and follow it back through its pipeline to find out **when** and **where** the drift started.

{% hint style="info" %}
**When should I retrain my model?**

As the data begins to drift, we may not notice significant degradation in our model's performance immediately.

However, this is an excellent opportunity to retrain before the drift has a negative impact on performance.
{% endhint %}

### Measuring Data Drift

To measure how distributions differ from each other, you can use a **statistical distance**. This is a metric that quantifies the distance between two distributions, and it is extremely useful.

There are many different statistical distances for different scenarios.

<figure><img src="https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FEMfp9zJ2aI25aicXymtU%2FScreen%20Shot%202022-11-20%20at%2016.13.49.png?alt=media&#x26;token=7b903425-f0e0-42ff-8836-2db727846e21" alt=""><figcaption><p>Is there a data drift here? :)</p></figcaption></figure>

By default, Aporia calculates a metric called **Drift Score**, which is a smart combination of statistical distances such as [Hellinger Distance](https://en.wikipedia.org/wiki/Hellinger_distance) for categorical variables and [Jensen-Shannon Divergence](https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence) for numeric variables.

Besides the default drift score, you can customize and add your own statistical distances.

### Intuition to Drift Score

Let's say we have a categorical feature called `pet_type` with 2 possible values:

* 🐶 Dog
* 🐱 Cat

In our training set, the distribution of this feature was **100% 🐶** + **0% 🐱**. This means that when we trained our model, we only had dogs and no cats.

Now, let's evaluate different scenarios in production, and see what would be the drift score:

* If the current distribution is **0% 🐶** + **100% 🐱**, the drift score would be **1.0**.
  * Tons of drift!
* If the current distribution is **50% 🐶** + **50% 🐱**, the drift score would be **0.54**.
* If the current distribution is **60% 🐶** + **40% 🐱**, the drift score would be **0.47**.
* If the current distribution is **100% 🐶** + **0% 🐱**, the drift score would be **0.0**.
  * No drift at all!
