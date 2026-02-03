# Source: https://docs.aporia.com/core-concepts/analyzing-performance.md

# Source: https://docs.aporia.com/v1/core-concepts/analyzing-performance.md

# Analyzing Performance

### Your model's success is your success

Hooray! Your model is running in production, making predictions in order to improve your business KPIs.

Unfortunately, when encountering real world pipelines and data our model might not perform as well as it did in our training process.

That's why we would like to analyze our model's performance over-time in order to make sure we catch possible degradation in time.

![It's Performance Review Time](https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FXemV5x5HfbdRr4xymkIH%2Fits-performance-review-time.jpeg?alt=media)

### Measuring Model Performance

To measure how well your model performs in production, you can use a variety of **performance metrics**. Each metric teaches us about different aspects of our model's performance.

While some people might care about not missing potential leads (e.g. focus on **recall** score) others might prefer to reduce dead ends to minimum costs (e.g. focus on **precision** score).

In addition, no matter which use case are you trying to solve with your model, you'll probably want to analyze its activity over time and ensure there are no anomalous events or ongoing trends with the model's usage.

{% hint style="info" %}

#### How often should I carry out performance analysis?

As models can vary dramatically in their purpose, usage, or production pipelines, the answer isn't unequivocal.

However, here are some questions you should consider while deciding - What is the frequency of the predictions? How frequently do we get the actuals? Are concept drifts common in this domain?&#x20;
{% endhint %}

### Common Performance metrics

Depending on your use case, you might want to use different performance metrics in order to decide how well our model performs. For example, nDCG is common when you want to understand the quality of your ranking model. AUC-ROC is useful when you want to evaluate you binary classification model.

You can read more about all the different metrics and the use cases which you will find useful in our [metric glossary.](https://docs.aporia.com/v1/api-reference/metrics-glossary)<br>

## Actuals / Ground Truth

In some cases, you will have access to the *actual* value of the prediction - the ground truth from real-world data.

For example, if your model predicted that a client will buy insurance, and a few days later the client actually does so, then the actual value of that prediction would be `True`.

In these scenarios, we can compare our predictions to the actual values and then calculate performance metrics like Precision, Recall, MSE, etc. - just like in training.

By connecting Aporia with your actual values, the system will be able to calculate performance metrics in real-time for you.

In this example, you can see the Precision metric across two model versions in production:

<figure><img src="https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2F4zjD6mEUlJS1XcdSkhp9%2FScreenshot%202022-11-20%20165649.png?alt=media&#x26;token=c9ce6115-db5c-4bc0-953a-027ee6db23f7" alt=""><figcaption><p>Timeseries</p></figcaption></figure>
