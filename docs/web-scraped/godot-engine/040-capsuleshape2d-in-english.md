# CapsuleShape2D in English

# CapsuleShape2D

Inherits:Shape2D<Resource<RefCounted<Object
A 2D capsule shape used for physics collision.

## Description

A 2D capsule shape, intended for use in physics. Usually used to provide a shape for aCollisionShape2D.
Performance:CapsuleShape2Dis fast to check collisions against, but it is slower thanRectangleShape2DandCircleShape2D.

## Properties

| float | height | 30.0 |
|---|---|---|
| float | mid_height |  |
| float | radius | 10.0 |

float
height
30.0
float
mid_height
float
radius
10.0

## Property Descriptions

floatheight=30.0🔗

- voidset_height(value:float)
voidset_height(value:float)
- floatget_height()
floatget_height()
The capsule's full height, including the semicircles.
Note:Theheightof a capsule must be at least twice itsradius. Otherwise, the capsule becomes a circle. If theheightis less than twice theradius, the properties adjust to a valid value.
floatmid_height🔗
- voidset_mid_height(value:float)
voidset_mid_height(value:float)
- floatget_mid_height()
floatget_mid_height()
The capsule's height, excluding the semicircles. This is the height of the central rectangular part in the middle of the capsule, and is the distance between the centers of the two semicircles. This is a wrapper forheight.
floatradius=10.0🔗
- voidset_radius(value:float)
voidset_radius(value:float)
- floatget_radius()
floatget_radius()
The capsule's radius.
Note:Theradiusof a capsule cannot be greater than half of itsheight. Otherwise, the capsule becomes a circle. If theradiusis greater than half of theheight, the properties adjust to a valid value.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
