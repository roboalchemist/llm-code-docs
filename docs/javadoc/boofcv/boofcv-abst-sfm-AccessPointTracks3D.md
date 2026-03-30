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

## Interface AccessPointTracks3D

- 

All Superinterfaces:
AccessPointTracks

All Known Implementing Classes:
MonoOverhead_to_MonocularPlaneVisualOdometry, MonoPlaneInfinity_to_MonocularPlaneVisualOdometry, VisOdomPixelDepthPnP_to_DepthVisualOdometry, WrapVisOdomDualTrackPnP, WrapVisOdomPixelDepthPnP, WrapVisOdomQuadPnP

---

```
public interface AccessPointTracks3D
extends AccessPointTracks
```

Provides information on point feature based SFM tracking algorithm
Author:
  Peter Abeles

- 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`Point3D_F64`
`**getTrackLocation**(int index)`
Returns the 3D location of the active track.

    - 

### Methods inherited from interface boofcv.abst.sfm.AccessPointTracks

`getAllTracks, getTrackId, isInlier, isNew`

- 

  - 

### Method Detail

    - 

#### getTrackLocation

```
Point3D_F64 getTrackLocation(int index)
```

Returns the 3D location of the active track.  If there is no location estimate
 yet then return null.
Parameters:`index` - The track's index in the active list
Returns:Location of the track or null otherwise

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