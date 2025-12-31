# Source: https://docs.aporia.com/api-reference/metrics-glossary.md

# Source: https://docs.aporia.com/v1/api-reference/metrics-glossary.md

# Source: https://docs.aporia.com/api-reference/metrics-glossary.md

# Source: https://docs.aporia.com/v1/api-reference/metrics-glossary.md

# Metrics Glossary

Here you can find information about all the performance metrics supported by Aporia.

Can't find what you are looking for? :hushed: We are constantly expanding our metrics support, but in the meantime you can always define your own custom metric  :raised\_hands:.

## Statistic metrics

### Missing Count

This metric counts the amount of records that didn't report a specific field while logging the data.\
It can be useful for surfacing data pipeline or infrastructure problems that may affect your model.

### Average

This metric calculates the average value of the given data. It can be applied on any numeric field.

### Minimum

This metric finds the minimal value out of the given data. It can be applied on ant numeric field.

### Maximum

This metric finds the maximal value out of the given data. It can be applied on ant numeric field.

### Sum

This metric calculates the sum of all values of the given data. It can be applied on any numeric field.

## Performance metrics

### Variance

Variance is the [expectation](https://en.wikipedia.org/wiki/Expected_value) of the squared [deviation](https://en.wikipedia.org/wiki/Deviation_\(statistics\)) of a [random variable](https://en.wikipedia.org/wiki/Random_variable) from its [sample mean](https://en.wikipedia.org/wiki/Sample_mean).

For sample variables, it is calculated using the following formula:

$$
Var(x) = \frac{\sum{(x\_i-\mu)^2}}{n-1}
$$

### Standard Deviation (STD)

The standard deviation is a statistical metric that measures the amount of variation or [dispersion](https://en.wikipedia.org/wiki/Statistical_dispersion) of a set of values.

STD is calculated using the following formula:

$$
\sigma = \sqrt{\frac{\sum{(x\_i-\mu)^2}}{N}}
$$

### Mean Squared Error (MSE)

Mean squared error is an estimator which measures the average squared difference between the estimated value and the actual value.\
MSE is calculated using the following formula:

$$
MSE = \frac{1}{n}\sum\_{i=1}^{n}(y\_i-x\_i)^2
$$

### Root Mean Squared Error (RMSE)

Root mean squared error is the root of MSE.\
RMSE is calculated using the following formula:

$$
RMSE = \sqrt{\sum\_{i=1}^n\frac{(y\_i - x\_i)^2}{n}}
$$

### Mean Absolute Error (MAE)

Mean absolute error is an estimator which measures the average absolute difference between the estimated value and the actual value.\
MAE is calculated using the following formula:

$$
MAE = \frac{\sum\_{i-1}^{n} |y\_i - x\_i|}{n}
$$

### Confusion matrix

![](https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FypnRoY57h1NST9zLS43V%2Fimage.png?alt=media\&token=f6a12cf7-ce8c-4c71-aa1c-377aedd76bbb)

#### True Positive Count (TP)

This metric measures the amount of correctly predicted to be positive for a specific characteristic. It is commonly used in classification problems.

#### True Negative Count (TN)

This metric measures the amount of correctly predicted to be negative for a specific characteristic. It is commonly used in classification problems.

#### False Positive Count (FP)

This metric measures the amount of incorrectly predicted to be positive for a specific characteristic. It is commonly used in classification problems.

#### False Negative Count (FN)

This metric measures the amount of incorrectly predicted to be negative for a specific characteristic. It is commonly used in classification problems.

### Precision

This metric measures the percentage of our correctly predicted positive for a specific class, out of all of the positive predictions. The higher score we get, the more concise our classification is.

Precision is useful to measure when the cost of a False Positive is high. For example, let's say that your model predicts whether an email is spam (positive) or not (negative). The cost of classifying an email as spam when it's not (FP) is high so we would like to monitor that our model's precision score remains high to avoid bad business impact.

Precision is calculated using the following formula:

$$
Precision = \frac{TP}{TP + FP}
$$

### Recall

This metric measures the percentage of our correctly predicted positive for a specific class, out of all the actual positives. The higher score we get, the fewer positives we missed.

Recall is useful to measure when the cost of a False Negative is high. For example, let's say that your model predicts whether a certain seller is a fraud (positive) or not(negative). The cost of miss detecting the fraud seller (FN) is high so we would like to monitor that our model's recall score remains high to avoid bad business impact.

Recall is calculated using the following formula:

$$
Recall = \frac{TP}{TP + FN}
$$

### Accuracy

This metric measures the percentage of our correct predictions out of all the predictions. The higher score we get, the "closer to reality" our classifications are.

Accuracy is useful when we have a balanced class distribution and we want to give more weight to the business value of the TP and TN.

Accuracy is calculated using the following formula:&#x20;

$$
Accuracy = \frac{TP + TN}{TP + TN + FP + FN}
$$

###

### F1

This metric is trying to balance between the precision and the recall metrics. It fits when we have an uneven class distribution and we want to give more weight to the business cost of the FP and FN.

F1 is calculated using the following formula:

$$
F1 = 2\cdot\frac{Precision\times Recall}{Precision + Recall}
$$

### Normalized Discounted Commutative Gain (nDCG)

This metric measures the quality of ranking.

Using the DCG metric we assume two things: First, an object with high relevance will produce more gain if it gets a higher rank. Second, that giving the same rank objects with higher relevance will produce more gain.

DCG is calculated using the following formula:

$$
DCG\_p = \sum\_{i=1}^{p}\frac{2^{rel\_i}-1}{log\_2(i-1)}
$$

Where RELi is the list of top i objects ordered by their rank.

The normalized version of the metric (nDCG) gives you the ability to compare between two rankings of different lengths.

nDCG is calculated using the following formula:<br>

$$
nDCG = \frac{DCG\_p}{IDCG\_p}
$$

where IDCG is the ideal DCG calculated by:

$$
DCG\_p = \sum\_{i=1}^{REL\_p}\frac{2^{rel\_i}-1}{log\_2(i-1)}
$$
