JavaScript is disabled on your browser.

- Overview

- Package

- Class

- Use

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

boofcv.alg.feature.detect.grid

## Class AutoThresholdCalibrationGrid

- java.lang.Object

- 

  - boofcv.alg.feature.detect.grid.AutoThresholdCalibrationGrid

- 

---

```
public class AutoThresholdCalibrationGrid
extends java.lang.Object
```

Automatically selects a threshold for detecting calibration targets. The initial threshold is found
 by doing a binary search through the possible thresholds until it finds a valid target.  Once a
 valid target has been found it computes the statistics of pixels around the corners.  Then a threshold
 is selected based on the mean value of white and dark regions.
Author:
  Peter Abeles

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**AutoThresholdCalibrationGrid**(double initialThreshold)`
Configures auto threshold.

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`ImageUInt8`
`**getBinary**()`
Binary image that target was detected inside of

`double`
`**getThreshold**()`
Optimal target threshold

`boolean`
`**process**(DetectSquareCalibrationPoints detector,
       ImageFloat32 gray)`
Processes the image and automatically detects calibration grid.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AutoThresholdCalibrationGrid

```
public AutoThresholdCalibrationGrid(double initialThreshold)
```

Configures auto threshold.
Parameters:`initialThreshold` - Threshold used for computing binary image. If < 0 then mean intensity is used.

  - 

### Method Detail

    - 

#### process

```
public boolean process(DetectSquareCalibrationPoints detector,
              ImageFloat32 gray)
```

Processes the image and automatically detects calibration grid.  If successful then
 true is returned and the found target is contained in the target detector.
Parameters:`detector` - Target detection algorithm.`gray` - Gray scale image which is being thresholded
Returns:true if a threshold was successfully found and target detected.

    - 

#### getThreshold

```
public double getThreshold()
```

Optimal target threshold
Returns:threshold

    - 

#### getBinary

```
public ImageUInt8 getBinary()
```

Binary image that target was detected inside of

- Overview

- Package

- Class

- Use

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

**Copyright © 2011-2012 Peter Abeles**