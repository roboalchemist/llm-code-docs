# Source: https://multi-template-matching.github.io/Multi-Template-Matching/doc/Flowchart

Title: Flowchart

URL Source: https://multi-template-matching.github.io/Multi-Template-Matching/doc/Flowchart

Markdown Content:
[View on GitHub](https://github.com/multi-template-matching/Multi-Template-Matching)
Multi-Template Matching for object-detection
--------------------------------------------

HomePage and documentation for the Multi-Template matching project. A simple solution for object-detection from one or several template images. Available for Fiji, Python and KNIME.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Below is a flowchart describing the Multi-Template-Matching implementation.

 The chart illustrates the sequential execution of the tool, in the case of correlation-based score.

 For difference-based score, the pipeline is identical except that a difference map is computed, minima are detected instead of maxima and the lowest minima are returned. (IoU: Intersection over Union)

![Image 1: Image](https://multi-template-matching.github.io/Multi-Template-Matching/doc/images/Flowchart.png)
