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

boofcv.abst.sfm

## Interface AccessPointTracks

- 

All Known Subinterfaces:
AccessPointTracks3D

All Known Implementing Classes:
MonoOverhead_to_MonocularPlaneVisualOdometry, MonoPlaneInfinity_to_MonocularPlaneVisualOdometry, MsToGrayMotion2D, VisOdomPixelDepthPnP_to_DepthVisualOdometry, WrapImageMotionPtkSmartRespawn, WrapVisOdomDualTrackPnP, WrapVisOdomPixelDepthPnP, WrapVisOdomQuadPnP

---

```
public interface AccessPointTracks
```

Provides access to the location of point tracks.  Location of tracks are provided in terms
 of pixel coordinates.
Author:
  Peter Abeles

- 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`java.util.List<Point2D_F64>`
`**getAllTracks**()`
All the points being actively tracked in pixel coordinates.

`long`
`**getTrackId**(int index)`
Used to get the track ID of an active Track

`boolean`
`**isInlier**(int index)`
True if the specified track is an inlier used in motion estimation

`boolean`
`**isNew**(int index)`
True if the specified track was just spawned

- 

  - 

### Method Detail

    - 

#### getTrackId

```
long getTrackId(int index)
```

Used to get the track ID of an active Track
Parameters:`index` - which track
Returns:The track's ID

    - 

#### getAllTracks

```
java.util.List<Point2D_F64> getAllTracks()
```

All the points being actively tracked in pixel coordinates.
Returns:all active tracks in pixel coordinates

    - 

#### isInlier

```
boolean isInlier(int index)
```

True if the specified track is an inlier used in motion estimation
Parameters:`index` - The index in all
Returns:if it is an inlier or not

    - 

#### isNew

```
boolean isNew(int index)
```

True if the specified track was just spawned
Parameters:`index` - The index in all
Returns:if it is new or not

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