# Source: https://code.kx.com/kdbai/latest/reference/dynamic-time-warping.html

Title: Learn Dynamic Time Warping (DTW)

URL Source: https://code.kx.com/kdbai/latest/reference/dynamic-time-warping.html

Markdown Content:
_This page introduces you to Dynamic Time Warping (DTW). You’ll learn what DTW is, how it differs from other temporal similarity methods like TSS, and when to use it for better accuracy, robustness, and performance._

If you're already familiar with this topic, you can skip ahead to the [How-to guide](https://code.kx.com/kdbai/latest/use/dynamic-time-warping-dtw.html).

**Dynamic Time Warping (DTW)** is a powerful algorithm used in temporal search to find patterns or sequences within time-series data that may vary in time or speed. By "warping" the time axis, DTW aligns similar parts of sequences, making it easier to compare them directly, even if they occur at different times or speeds.

DTW vs. Non-Transformed TSS vs. Transformed TSS
-----------------------------------------------

*   **DTW and Non-Transformed Temporal Similarity Search (Non-Transformed TSS)** both operate on scalar entries in the search column, making them alternatives to each other.

*   **Transformed TSS**, on the other hand, deals with vector entries, distinguishing it from DTW and Non-Transformed TSS.

*   **Compared to Non-Transformed TSS, DTW** offers greater flexibility in handling queries of varying lengths. This makes DTW particularly useful in scenarios where the sequences being compared do not align perfectly in time.

More details in the [When to Use DTW vs. Non-Transformed TSS vs. Transformed TSS](https://code.kx.com/kdbai/latest/reference/dynamic-time-warping.html#when-to-use-dtw-vs-non-transformed-tss-vs-transformed-tss) section.

Key advantages
--------------

Key advantages of Temporal Search with Dynamic Time Warping (DTW):

1.   **Flexibility in time alignment:** DTW can align sequences that vary in speed or timing, making it ideal for comparing time-series data that do not align perfectly.

2.   **Robustness to variability:** It handles variations in the length of sequences, allowing for meaningful comparisons even when the sequences have different durations or are sampled at different rates.

3.   **Improved Pattern Recognition:** DTW can identify similar patterns in sequences despite shifts and distortions in time, which is particularly useful in fields like speech recognition, gesture recognition, and financial market analysis.

4.   **Enhanced predictive modeling:** By aligning historical data with current data, DTW can improve the a ccuracy of predictive models, helping to forecast future trends based on past patterns.

5.   **Versatility across domains:** DTW is applicable in various domains, including finance, healthcare, and multimedia (including speech, gait, gesture etc.), making it a versatile tool for temporal analysis.

6.   **Handling non-linear distortions:** Unlike linear methods, DTW can manage non-linear distortions in time-series data, providing a more accurate comparison of sequences that have undergone complex transformations.

7.   **Applicability to multivariate data:** DTW can be extended to multivariate time-series data, allowing for the comparison of complex datasets with multiple variables.

8.   **Noise tolerance:** It is relatively robust to noise in the data, ensuring that minor fluctuations do not significantly impact the alignment and comparison of sequences.

How DTW works
-------------

DTW is designed to compare two sequences that might be out of sync. Here’s a simplified explanation:

1.   **Alignment:** Imagine two sequences laid out along the sides of a grid.

2.   **Cost calculation:** Each cell in the grid represents a "cost" that quantifies the difference between the corresponding points of the sequences.

3.   **Optimal path:** DTW finds the path through the grid that minimizes the total cost, representing the best alignment of the sequences. This path can zig-zag, allowing flexible alignment.

### Parameters

This section explains two key parameters that control how DTW behaves during a search: Ratio of Warping Radius (`RR`) and Cut-Off Threshold Value (`cutOff`).

The warping radius is the so-called warping window constraint or Sakoe-Chiba band. It limits how far DTW is allowed to "warp" the time axis between the two sequences being compared. In other words, it constrains the alignment to only consider matches that are no more than r steps apart in time.

Therefore, if your query's length is `100` and `RR=0.05`, your warping radius is `r=100*0.05=5`.

### Why is `RR` useful?

1.   **Speed:** It drastically reduces the number of distance computations (from O(n²) to O(n·r)).

2.   **Regularization:** Prevents DTW from over-warping and aligning unrelated features.

3.   **Better matching:** In many real-world time series (for example, stock prices), patterns do shift over time, but usually only within a limited range - RR (for example, r) controls that range.

To speed up the search process, you can also apply a cut-off threshold value which will discard all DTW results with distances higher than the specified cut-off.

|  | `RR` | `cutOff` |
| --- | --- | --- |
| **Meaning** | Ratio of warping radius (constraint) | Cut-off threshold value |
| **Range** | 0 ≤ `RR` ≤ 1 | 0 ≤ `cutOff` ≤ ∞ |
| **Role** | Controls how much time distortion is allowed | DTW results with distances higher than the specified cut-off will be discarded |
| **Benefit** | Speeds up DTW and avoids overfitting | Speeds up DTW |
| **What value to use?** | Set a larger `RR` when you expect significant warping or want more flexible matching, even if it increases search time. Set a smaller `RR` when you expect minimal warping or need faster search performance. | If distances beyond a certain threshold rarely yield meaningful results, set that value as `cutOff`. If search performance is a concern, reduce the `cutOff` to speed up the query. |

Applications of DTW
-------------------

### Stock market data

DTW is particularly effective for analyzing stock market data, which often exhibits patterns that vary in duration and timing. Unlike fixed-alignment methods such as Temporal Similarity Search (TSS), which compare time-series data point by point, DTW flexibly aligns sequences by warping the time axis. This allows DTW to identify similar patterns even when they occur over different time scales or with temporal shifts.

In real-world financial markets, price movements like rallies or reversals rarely unfold uniformly. DTW excels in these scenarios by focusing on the shape of the pattern rather than exact timing, making it more robust to variations and noise in the data. While TSS is efficient and suitable for synchronized patterns, it may miss meaningful similarities when timing discrepancies exist.

**Key use cases for DTW in stock market analysis:**

*   **Real-time monitoring and anomaly detection:** DTW enables the detection of emerging trends that resemble historical events, even if they unfold at different speeds. For instance, a rapid price drop in current trading could mirror a slower historical decline, and DTW can align these patterns early for timely alerts.

*   **Historical pattern discovery:** Technical patterns like "double bottoms" or "head and shoulders" often vary in length. DTW can identify these recurring motifs in historical data regardless of their duration, aiding in comprehensive pattern recognition.

*   **Cross-series similarity and lead-lag relationships:** When comparing multiple assets, DTW can align time-shifted series to detect if one asset's behavior follows another's with a delay. This is valuable for uncovering leading indicators and understanding inter-market dynamics.

*   **Pattern-based forecasting:** DTW facilitates more flexible forecasting by matching current trends with historical patterns of varying lengths. This approach enhances the accuracy of predictions by learning from a broader range of past behaviors.

By accommodating temporal variations and focusing on pattern shapes, DTW provides a powerful tool for analyzing complex and asynchronous financial time-series data.

### DTW outside finance

1.   **Speech and audio recognition**. DTW was originally developed for aligning spoken words that vary in speed or timing. It compares phoneme sequences or waveform patterns to identify the same word spoken slowly or quickly, making it foundational in speech recognition and audio processing.

2.   **Motion and gesture analysis**. In robotics, virtual reality, and gaming, DTW enables systems to recognize gestures or movements, even if performed at different speeds or intensities. It is widely used for comparing sequences like hand motions or gait patterns in real time.

3.   **Medical signal processing**. DTW supports the comparison of time-aligned medical signals such as ECGs, EEGs, and respiratory patterns. It helps detect anomalies by aligning current patient data with known healthy or pathological examples, even when the signals are offset or distorted over time.

4.   **Utilities and smart grids**. In energy monitoring, DTW identifies usage patterns in electricity or water consumption, even when demand spikes occur at different times of day. It enables clustering of behavioral patterns and anomaly detection in smart grid analytics.

5.   **Wearables and climate data**. Wearable devices use DTW to recognize physical activities like walking or running under varied conditions. In bioinformatics, DTW-like techniques compare protein sequences with timing or structural variations. It's also applied in environmental monitoring, aligning patterns in weather data such as temperature or pollution despite seasonal timing shifts.

When to use DTW vs. Non-Transformed TSS vs. Transformed TSS
-----------------------------------------------------------

| **Use case** | **DTW** | **Non-Transformed TSS** | **Transformed TSS** |
| --- | --- | --- | --- |
| Patterns occur at different speeds or lengths | ✅ Best choice for misalignment under similar scale | ❌ Not suitable | ✅ For large scale deformation |
| Patterns are aligned and fixed-length | ⚠️ Works, but overkill | ✅ Ideal | ⚠️ Use only if data is vector-based |
| Data is represented as vectors | ❌ Not applicable | ❌ Not applicable | ✅ Required |
| Shape-based similarity (for example, rallies, reversals) | ✅ Excellent if the warping between shape/data is expected to be within RR | ❌ May miss due to timing mismatch | ⚠️ Possible if shape is embedded |
| High-performance scanning of large datasets | ⚠️ Slower than others (especially for large RR) | ✅ Fastest | ✅ Fast |
| Streaming or real-time anomaly detection | ✅ Suitable with optimizations | ✅ Well-suited | ✅ Well-suited |
| Lead-lag or time-shifted correlation | ✅ Can align automatically | ❌ Requires manual shifting | ❌ Not designed for this |
| Fixed-length Euclidean comparison | ⚠️ Can mimic if no warping needed | ✅ Native behavior | ⚠️ Used only for vector data |

Conclusion
----------

DTW is a versatile tool for temporal search, offering flexibility and precision in aligning sequences that vary over time. Its applications in stock market data highlight its potential for pattern recognition and predictive analysis, making it invaluable for financial analysts and data scientists.

Next steps
----------

*   [How To Use Dynamic Time Warping](https://code.kx.com/kdbai/latest/use/dynamic-time-warping-dtw.html)
