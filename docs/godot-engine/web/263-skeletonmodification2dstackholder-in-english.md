# SkeletonModification2DStackHolder in English

# SkeletonModification2DStackHolder

Experimental:This class may be changed or removed in future versions.
Inherits:SkeletonModification2D<Resource<RefCounted<Object
A modification that holds and executes aSkeletonModificationStack2D.

## Description

ThisSkeletonModification2Dholds a reference to aSkeletonModificationStack2D, allowing you to use multiple modification stacks on a singleSkeleton2D.
Note:The modifications in the heldSkeletonModificationStack2Dwill only be executed if their execution mode matches the execution mode of the SkeletonModification2DStackHolder.

## Methods

| SkeletonModificationStack2D | get_held_modification_stack()const |
|---|---|
| void | set_held_modification_stack(held_modification_stack:SkeletonModificationStack2D) |

SkeletonModificationStack2D
get_held_modification_stack()const
void
set_held_modification_stack(held_modification_stack:SkeletonModificationStack2D)

## Method Descriptions

SkeletonModificationStack2Dget_held_modification_stack()const🔗
Returns theSkeletonModificationStack2Dthat this modification is holding.
voidset_held_modification_stack(held_modification_stack:SkeletonModificationStack2D)🔗
Sets theSkeletonModificationStack2Dthat this modification is holding. This modification stack will then be executed when this modification is executed.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
