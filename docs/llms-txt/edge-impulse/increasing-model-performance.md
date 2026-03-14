# Source: https://docs.edgeimpulse.com/knowledge/guides/increasing-model-performance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Increasing model performance

If your impulse is performing poorly, these could be the culprits:

1. There is not enough data. Neural networks need to learn patterns in data sets, and the more data the better. You can also lower the window increase (in the *Create Impulse* screen) to create more overlap from windows, but this does not lead to more variance in your data set. More data is thus always better.
2. The data does not look like other data the network has seen before. This is common when someone uses the device in a way that you didn't add to the test set. If you see this in the test set or during live classification you can push the sample to the training set by clicking `⋮`, then selecting **Move to training set**. Make sure to update the label before training.
3. The model has not been trained enough. Up the number of training cycles and see if performance increases. If there's no difference then you probably don't have enough data, or the data does not separate well enough.
4. If you have a high accuracy on your neural network, but the model performs poorly on new data, then your model might be overfitting. It has learned the features in your dataset too well. Try adding more data, or reduce the learning rate.
5. The neural network architecture is not a great fit for your data. Play with the number of layers and neurons and see if performance improves.

### Class imbalance

If you have much more data in one class than for other classes, say 90% of your data is labeled as "idle" and only 10% as "wave", your neural network will have trouble learning due to class imbalance. If this is the case your best bet is to increase the amount of data in the misrepresented class. However, if this is not possible you can try to rebalance your dataset during training. To do this, go to your learning block and enable the **Auto-weight classes** option (it may not be available for all learning block types):

<Frame caption="Auto-weight classes">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/studio-auto-weight-classes.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=d6f99e7225e08161c6b811078e83c5d8" width="1152" height="478" data-path=".assets/images/studio-auto-weight-classes.png" />
</Frame>

Alternatively, you can also do this in the [expert mode](/studio/projects/learning-blocks/expert-mode):

1. On the Neural Network page click `⋮` and select `Switch to Keras (expert) mode`.
2. Below the imports (the lines starting with `from`) add:

```
from sklearn.utils.class_weight import compute_class_weight

class_weights = dict(enumerate(compute_class_weight('balanced', np.unique(np.argmax(Y_train, axis=1)), np.argmax(Y_train, axis=1))))
```

1. At the last line (where `fit()` is called), add `class_weight=classweights`. E.g.:

```
model.fit(X_train, Y_train, batch_size=50, epochs=200, validation_data=(X_test, Y_test), class_weight=class_weights)
```

For [FOMO](/studio/projects/learning-blocks/blocks/object-detection/fomo) projects, have a look at [this project](https://studio.edgeimpulse.com/public/494157/latest/impulses).
This project uses 3 different methods. You can compare the results in the [Impulse Experiments tab](/studio/projects/experiments) and have a look at each of the Learning block's expert mode:

* The default method: We apply by default a weighted loss function (`weighted_cross_entropy_with_logits`). We set the background class to a weight of 1 and the other classes to 100. This helps the model to focus on the objects rather than the background.
* Rebalance per class: Use more or less the same default methodology (keep a weight of 1 for the background), use a weighting strategy for the non-background classes (weighted per number of items per class) and apply an extra weight to force the model to focus more on these classes. The `construct_weighted_xent_fn` function is overwritten to use a `sigmoid_cross_entropy_with_logits` loss.
* Rebalance using the pixels per class: Here, as the background is usually predominant, no need to force the background weight to 1, it will automatically be much lower than the others because the number of pixels will be larger than the other classes. Although we calculate the weights by adding each pixels from a subset of the entire dataset (BATCH\_SIZE \* 4), keep in mind that the training time will be increased. The `construct_weighted_xent_fn` function is overwritten to use a `sparse_softmax_cross_entropy_with_logits` loss.

### Large difference between quantized (int8) and unoptimized (float32) model performances

Quantization works by reducing the precision of the model's weights, so there will often be a bit of reduction in performance. If it performs too poorly, here are some things that can help:

* Add more data. It is especially likely that performance will be lost for classes that are in a minority in the training set. If you are working with time series (such as accelerometers), try reducing the window increase, it will generate more samples.
* Add some regularization (for example, some dropout layers). This helps force the network to be more resilient against the kind of error introduced by quantization. You may have to train a few more epochs to make up for the regularization.
* Increase the capacity of the network. Quantization error is worse for networks that are at their capacity limit, e.g. where every parameter is super important. If you add a few more neurons or layers you might find that the issue is not as bad.

### No solution?

If you still have issues, the community might be able to help through the [forums](https://forum.edgeimpulse.com).

For our valued enterprise tier customers, we offer machine learning solutions engineer consultation you can [Schedule a consultation](https://edgeimpulse.com/contact) or [Contact Sales](https://edgeimpulse.com/contact) to discuss your specific needs.

```
```


Built with [Mintlify](https://mintlify.com).