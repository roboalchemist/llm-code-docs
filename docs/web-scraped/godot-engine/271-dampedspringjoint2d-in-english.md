# DampedSpringJoint2D in English

# DampedSpringJoint2D

Inherits:Joint2D<Node2D<CanvasItem<Node<Object
A physics joint that connects two 2D physics bodies with a spring-like force.

## Description

A physics joint that connects two 2D physics bodies with a spring-like force. This behaves like a spring that always wants to stretch to a given length.

## Properties

| float | damping | 1.0 |
|---|---|---|
| float | length | 50.0 |
| float | rest_length | 0.0 |
| float | stiffness | 20.0 |

float
damping
float
length
50.0
float
rest_length
float
stiffness
20.0

## Property Descriptions

floatdamping=1.0🔗

- voidset_damping(value:float)
voidset_damping(value:float)
- floatget_damping()
floatget_damping()
The spring joint's damping ratio. A value between0and1. When the two bodies move into different directions the system tries to align them to the spring axis again. A highdampingvalue forces the attached bodies to align faster.
floatlength=50.0🔗
- voidset_length(value:float)
voidset_length(value:float)
- floatget_length()
floatget_length()
The spring joint's maximum length. The two attached bodies cannot stretch it past this value.
floatrest_length=0.0🔗
- voidset_rest_length(value:float)
voidset_rest_length(value:float)
- floatget_rest_length()
floatget_rest_length()
When the bodies attached to the spring joint move they stretch or squash it. The joint always tries to resize towards this length.
floatstiffness=20.0🔗
- voidset_stiffness(value:float)
voidset_stiffness(value:float)
- floatget_stiffness()
floatget_stiffness()
The higher the value, the less the bodies attached to the joint will deform it. The joint applies an opposing force to the bodies, the product of the stiffness multiplied by the size difference from its resting length.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
