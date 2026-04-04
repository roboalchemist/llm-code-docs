# Source: https://boltons.readthedocs.io/en/latest/statsutils.html

Title: Statistics fundamentals — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/statsutils.html

Markdown Content:
`statsutils` - Statistics fundamentals[](https://boltons.readthedocs.io/en/latest/statsutils.html#module-boltons.statsutils "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------

`statsutils` provides tools aimed primarily at descriptive statistics for data analysis, such as [`mean()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.mean "boltons.statsutils.mean") (average), [`median()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.median "boltons.statsutils.median"), [`variance()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.variance "boltons.statsutils.variance"), and many others,

The [`Stats`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats "boltons.statsutils.Stats") type provides all the main functionality of the `statsutils` module. A [`Stats`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats "boltons.statsutils.Stats") object wraps a given dataset, providing all statistical measures as property attributes. These attributes cache their results, which allows efficient computation of multiple measures, as many measures rely on other measures. For example, relative standard deviation ([`Stats.rel_std_dev`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.rel_std_dev "boltons.statsutils.Stats.rel_std_dev")) relies on both the mean and standard deviation. The Stats object caches those results so no rework is done.

The [`Stats`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats "boltons.statsutils.Stats") type’s attributes have module-level counterparts for convenience when the computation reuse advantages do not apply.

>>> stats = Stats(range(42))
>>> stats.mean
20.5
>>> mean(range(42))
20.5

Statistics is a large field, and `statsutils` is focused on a few basic techniques that are useful in software. The following is a brief introduction to those techniques. For a more in-depth introduction, [Statistics for Software](https://www.paypal-engineering.com/2016/04/11/statistics-for-software/), an article I wrote on the topic. It introduces key terminology vital to effective usage of statistics.

Statistical moments[](https://boltons.readthedocs.io/en/latest/statsutils.html#statistical-moments "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------

Python programmers are probably familiar with the concept of the _mean_ or _average_, which gives a rough quantitiative middle value by which a sample can be can be generalized. However, the mean is just the first of four [moment](https://en.wikipedia.org/wiki/Moment_(mathematics))-based measures by which a sample or distribution can be measured.

The four [Standardized moments](https://en.wikipedia.org/wiki/Standardized_moment) are:

> 1.   [Mean](https://en.wikipedia.org/wiki/Mean) - [`mean()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.mean "boltons.statsutils.mean") - theoretical middle value
> 
> 2.   [Variance](https://en.wikipedia.org/wiki/Variance) - [`variance()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.variance "boltons.statsutils.variance") - width of value dispersion
> 
> 3.   [Skewness](https://en.wikipedia.org/wiki/Skewness) - [`skewness()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.skewness "boltons.statsutils.skewness") - symmetry of distribution
> 
> 4.   [Kurtosis](https://en.wikipedia.org/wiki/Kurtosis) - [`kurtosis()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.kurtosis "boltons.statsutils.kurtosis") - “peakiness” or “long-tailed”-ness

For more information check out [the Moment article on Wikipedia](https://en.wikipedia.org/wiki/Moment_(mathematics)).

Keep in mind that while these moments can give a bit more insight into the shape and distribution of data, they do not guarantee a complete picture. Wildly different datasets can have the same values for all four moments, so generalize wisely.

Robust statistics[](https://boltons.readthedocs.io/en/latest/statsutils.html#robust-statistics "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------

Moment-based statistics are notorious for being easily skewed by outliers. The whole field of robust statistics aims to mitigate this dilemma. `statsutils` also includes several robust statistical methods:

> *   [Median](https://en.wikipedia.org/wiki/Median) - The middle value of a sorted dataset
> 
> *   [Trimean](https://en.wikipedia.org/wiki/Trimean) - Another robust measure of the data’s central tendency
> 
> *   [Median Absolute Deviation](https://en.wikipedia.org/wiki/Median_absolute_deviation) (MAD) - A robust measure of variability, a natural counterpart to [`variance()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.variance "boltons.statsutils.variance").
> 
> *   [Trimming](https://en.wikipedia.org/wiki/Trimmed_estimator) - Reducing a dataset to only the middle majority of data is a simple way of making other estimators more robust.

Online and Offline Statistics[](https://boltons.readthedocs.io/en/latest/statsutils.html#online-and-offline-statistics "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------

Unrelated to computer networking, [online](https://en.wikipedia.org/wiki/Online_algorithm) statistics involve calculating statistics in a [streaming](https://en.wikipedia.org/wiki/Streaming_algorithm) fashion, without all the data being available. The [`Stats`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats "boltons.statsutils.Stats") type is meant for the more traditional offline statistics when all the data is available. For pure-Python online statistics accumulators, look at the [Lithoxyl](https://github.com/mahmoud/lithoxyl) system instrumentation package.

_class_ boltons.statsutils.Stats(_data_, _default=0.0_, _use\_copy=True_, _is\_sorted=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/statsutils.html#Stats)[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats "Link to this definition")
The `Stats` type is used to represent a group of unordered statistical datapoints for calculations such as mean, median, and variance.

Parameters:
*   **data** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – List or other iterable containing numeric values.

*   **default** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) – A value to be returned when a given statistical measure is not defined. 0.0 by default, but `float('nan')` is appropriate for stricter applications.

*   **use_copy** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – By default Stats objects copy the initial data into a new list to avoid issues with modifications. Pass `False` to disable this behavior.

*   **is_sorted** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Presorted data can skip an extra sorting step for a little speed boost. Defaults to False.

clear_cache()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/statsutils.html#Stats.clear_cache)[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.clear_cache "Link to this definition")
`Stats` objects automatically cache intermediary calculations that can be reused. For instance, accessing the `std_dev` attribute after the `variance` attribute will be significantly faster for medium-to-large datasets.

If you modify the object by adding additional data points, call this function to have the cached statistics recomputed.

count[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.count "Link to this definition")
The number of items in this Stats object. Returns the same as [`len()`](https://docs.python.org/3/library/functions.html#len "(in Python v3.14)") on a Stats object, but provided for pandas terminology parallelism.

describe(_quantiles=None_, _format=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/statsutils.html#Stats.describe)[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.describe "Link to this definition")
Provides standard summary statistics for the data in the Stats object, in one of several convenient formats.

Parameters:
*   **quantiles** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – A list of numeric values to use as quantiles in the resulting summary. All values must be 0.0-1.0, with 0.5 representing the median. Defaults to `[0.25, 0.5, 0.75]`, representing the standard quartiles.

*   **format** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – Controls the return type of the function, with one of three valid values: `"dict"` gives back a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") with the appropriate keys and values. `"list"` is a list of key-value pairs in an order suitable to pass to an OrderedDict or HTML table. `"text"` converts the values to text suitable for printing, as seen below.

Here is the information returned by a default `describe`, as presented in the `"text"` format:

>>> stats = Stats(range(1, 8))
>>> print(stats.describe(format='text'))
count: 7
mean: 4.0
std_dev: 2.0
mad: 2.0
min: 1
0.25: 2.5
0.5: 4
0.75: 5.5
max: 7

For more advanced descriptive statistics, check out my blog post on the topic [Statistics for Software](https://www.paypal-engineering.com/2016/04/11/statistics-for-software/).

format_histogram(_bins=None_, _**kw_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/statsutils.html#Stats.format_histogram)[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.format_histogram "Link to this definition")
Produces a textual histogram of the data, using fixed-width bins, allowing for simple visualization, even in console environments.

>>> data = list(range(20)) + list(range(5, 15)) + [10]
>>> print(Stats(data).format_histogram(width=30))
 0.0: 5 #########
 4.4: 8 ###############
 8.9: 11 ####################
13.3: 5 #########
17.8: 2 ####

In this histogram, five values are between 0.0 and 4.4, eight are between 4.4 and 8.9, and two values lie between 17.8 and the max.

You can specify the number of bins, or provide a list of bin boundaries themselves. If no bins are provided, as in the example above, [Freedman’s algorithm](https://en.wikipedia.org/wiki/Freedman%E2%80%93Diaconis_rule) for bin selection is used.

Parameters:
*   **bins** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – Maximum number of bins for the histogram. Also accepts a list of floating-point bin boundaries. If the minimum boundary is still greater than the minimum value in the data, that boundary will be implicitly added. Defaults to the bin boundaries returned by [Freedman’s algorithm](https://en.wikipedia.org/wiki/Freedman%E2%80%93Diaconis_rule).

*   **bin_digits** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – Number of digits to round each bin to. Note that bins are always rounded down to avoid clipping any data. Defaults to 1.

*   **width** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – integer number of columns in the longest line in the histogram. Defaults to console width on Python 3.3+, or 80 if that is not available.

*   **format_bin** (_callable_) – Called on each bin to create a label for the final output. Use this function to add units, such as “ms” for milliseconds.

Should you want something more programmatically reusable, see the [`get_histogram_counts()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.get_histogram_counts "boltons.statsutils.Stats.get_histogram_counts") method, the output of is used by format_histogram. The [`describe()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.describe "boltons.statsutils.Stats.describe") method is another useful summarization method, albeit less visual.

get_histogram_counts(_bins=None_, _**kw_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/statsutils.html#Stats.get_histogram_counts)[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.get_histogram_counts "Link to this definition")
Produces a list of `(bin, count)` pairs comprising a histogram of the Stats object’s data, using fixed-width bins. See [`Stats.format_histogram()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.format_histogram "boltons.statsutils.Stats.format_histogram") for more details.

Parameters:
*   **bins** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – maximum number of bins, or list of floating-point bin boundaries. Defaults to the output of Freedman’s algorithm.

*   **bin_digits** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – Number of digits used to round down the bin boundaries. Defaults to 1.

The output of this method can be stored and/or modified, and then passed to `statsutils.format_histogram_counts()` to achieve the same text formatting as the [`format_histogram()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.format_histogram "boltons.statsutils.Stats.format_histogram") method. This can be useful for snapshotting over time.

get_quantile(_q_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/statsutils.html#Stats.get_quantile)[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.get_quantile "Link to this definition")
Get a quantile from the dataset. Quantiles are floating point values between `0.0` and `1.0`, with `0.0` representing the minimum value in the dataset and `1.0` representing the maximum. `0.5` represents the median:

>>> Stats(range(100)).get_quantile(0.5)
49.5

get_zscore(_value_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/statsutils.html#Stats.get_zscore)[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.get_zscore "Link to this definition")
Get the z-score for _value_ in the group. If the standard deviation is 0, 0 inf or -inf will be returned to indicate whether the value is equal to, greater than or below the group’s mean.

iqr[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.iqr "Link to this definition")
Inter-quartile range (IQR) is the difference between the 75th percentile and 25th percentile. IQR is a robust measure of dispersion, like standard deviation, but safer to compare between datasets, as it is less influenced by outliers.

kurtosis[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.kurtosis "Link to this definition")
Indicates how much data is in the tails of the distribution. The result is always positive, with the normal “bell-curve” distribution having a kurtosis of 3.

[http://en.wikipedia.org/wiki/Kurtosis](http://en.wikipedia.org/wiki/Kurtosis)

See the module docstring for more about statistical moments.

mad[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.mad "Link to this definition")
Median Absolute Deviation is a robust measure of statistical dispersion: [http://en.wikipedia.org/wiki/Median_absolute_deviation](http://en.wikipedia.org/wiki/Median_absolute_deviation)

max[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.max "Link to this definition")
The maximum value present in the data.

mean[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.mean "Link to this definition")
The arithmetic mean, or “average”. Sum of the values divided by the number of values.

median[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.median "Link to this definition")
The median is either the middle value or the average of the two middle values of a sample. Compared to the mean, it’s generally more resilient to the presence of outliers in the sample.

median_abs_dev[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.median_abs_dev "Link to this definition")
Median Absolute Deviation is a robust measure of statistical dispersion: [http://en.wikipedia.org/wiki/Median_absolute_deviation](http://en.wikipedia.org/wiki/Median_absolute_deviation)

min[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.min "Link to this definition")
The minimum value present in the data.

pearson_type[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.pearson_type "Link to this definition")rel_std_dev[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.rel_std_dev "Link to this definition")
Standard deviation divided by the absolute value of the average.

[http://en.wikipedia.org/wiki/Relative_standard_deviation](http://en.wikipedia.org/wiki/Relative_standard_deviation)

skewness[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.skewness "Link to this definition")
Indicates the asymmetry of a curve. Positive values mean the bulk of the values are on the left side of the average and vice versa.

[http://en.wikipedia.org/wiki/Skewness](http://en.wikipedia.org/wiki/Skewness)

See the module docstring for more about statistical moments.

std_dev[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.std_dev "Link to this definition")
Standard deviation. Square root of the variance.

trim_relative(_amount=0.15_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/statsutils.html#Stats.trim_relative)[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.trim_relative "Link to this definition")
A utility function used to cut a proportion of values off each end of a list of values. This has the effect of limiting the effect of outliers.

Parameters:
**amount** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) – A value between 0.0 and 0.5 to trim off of each side of the data.

trimean[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.trimean "Link to this definition")
The trimean is a robust measure of central tendency, like the median, that takes the weighted average of the median and the upper and lower quartiles.

variance[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.variance "Link to this definition")
Variance is the average of the squares of the difference between each value and the mean.

boltons.statsutils.describe(_data_, _quantiles=None_, _format=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/statsutils.html#describe)[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.describe "Link to this definition")
A convenience function to get standard summary statistics useful for describing most data. See [`Stats.describe()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.describe "boltons.statsutils.Stats.describe") for more details.

>>> print(describe(range(7), format='text'))
count: 7
mean: 3.0
std_dev: 2.0
mad: 2.0
min: 0
0.25: 1.5
0.5: 3
0.75: 4.5
max: 6

See [`Stats.format_histogram()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.format_histogram "boltons.statsutils.Stats.format_histogram") for another very useful summarization that uses textual visualization.

boltons.statsutils.format_histogram_counts(_bin\_counts_, _width=None_, _format\_bin=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/statsutils.html#format_histogram_counts)[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.format_histogram_counts "Link to this definition")
The formatting logic behind [`Stats.format_histogram()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.format_histogram "boltons.statsutils.Stats.format_histogram"), which takes the output of [`Stats.get_histogram_counts()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats.get_histogram_counts "boltons.statsutils.Stats.get_histogram_counts"), and passes them to this function.

Parameters:
*   **bin_counts** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – A list of bin values to counts.

*   **width** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – Number of character columns in the text output, defaults to 80 or console width in Python 3.3+.

*   **format_bin** (_callable_) – Used to convert bin values into string labels.

boltons.statsutils.iqr(_data_, _default=0.0_)[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.iqr "Link to this definition")
Inter-quartile range (IQR) is the difference between the 75th percentile and 25th percentile. IQR is a robust measure of dispersion, like standard deviation, but safer to compare between datasets, as it is less influenced by outliers.

>>> iqr([1, 2, 3, 4, 5])
2
>>> iqr(range(1001))
500

boltons.statsutils.kurtosis(_data_, _default=0.0_)[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.kurtosis "Link to this definition")
Indicates how much data is in the tails of the distribution. The result is always positive, with the normal “bell-curve” distribution having a kurtosis of 3.

[http://en.wikipedia.org/wiki/Kurtosis](http://en.wikipedia.org/wiki/Kurtosis)

See the module docstring for more about statistical moments.

>>> kurtosis(range(9))
1.99125

With a kurtosis of 1.99125, [0, 1, 2, 3, 4, 5, 6, 7, 8] is more centrally distributed than the normal curve.

boltons.statsutils.mean(_data_, _default=0.0_)[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.mean "Link to this definition")
The arithmetic mean, or “average”. Sum of the values divided by the number of values.

>>> mean(range(20))
9.5
>>> mean(list(range(19)) + [949])  # 949 is an arbitrary outlier
56.0

boltons.statsutils.median(_data_, _default=0.0_)[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.median "Link to this definition")
The median is either the middle value or the average of the two middle values of a sample. Compared to the mean, it’s generally more resilient to the presence of outliers in the sample.

>>> median([2, 1, 3])
2
>>> median(range(97))
48
>>> median(list(range(96)) + [1066])  # 1066 is an arbitrary outlier
48

boltons.statsutils.median_abs_dev(_data_, _default=0.0_)[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.median_abs_dev "Link to this definition")
Median Absolute Deviation is a robust measure of statistical dispersion: [http://en.wikipedia.org/wiki/Median_absolute_deviation](http://en.wikipedia.org/wiki/Median_absolute_deviation)

>>> median_abs_dev(range(97))
24.0

boltons.statsutils.pearson_type(_data_, _default=0.0_)[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.pearson_type "Link to this definition")boltons.statsutils.rel_std_dev(_data_, _default=0.0_)[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.rel_std_dev "Link to this definition")
Standard deviation divided by the absolute value of the average.

[http://en.wikipedia.org/wiki/Relative_standard_deviation](http://en.wikipedia.org/wiki/Relative_standard_deviation)

>>> print('%1.3f' % rel_std_dev(range(97)))
0.583

boltons.statsutils.skewness(_data_, _default=0.0_)[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.skewness "Link to this definition")
Indicates the asymmetry of a curve. Positive values mean the bulk of the values are on the left side of the average and vice versa.

[http://en.wikipedia.org/wiki/Skewness](http://en.wikipedia.org/wiki/Skewness)

See the module docstring for more about statistical moments.

>>> skewness(range(97))  # symmetrical around 48.0
0.0
>>> left_skewed = skewness(list(range(97)) + list(range(10)))
>>> right_skewed = skewness(list(range(97)) + list(range(87, 97)))
>>> round(left_skewed, 3), round(right_skewed, 3)
(0.114, -0.114)

boltons.statsutils.std_dev(_data_, _default=0.0_)[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.std_dev "Link to this definition")
Standard deviation. Square root of the variance.

>>> std_dev(range(97))
28.0

boltons.statsutils.trimean(_data_, _default=0.0_)[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.trimean "Link to this definition")
The trimean is a robust measure of central tendency, like the median, that takes the weighted average of the median and the upper and lower quartiles.

>>> trimean([2, 1, 3])
2.0
>>> trimean(range(97))
48.0
>>> trimean(list(range(96)) + [1066])  # 1066 is an arbitrary outlier
48.0

boltons.statsutils.variance(_data_, _default=0.0_)[](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.variance "Link to this definition")
Variance is the average of the squares of the difference between each value and the mean.

>>> variance(range(97))
784.0
