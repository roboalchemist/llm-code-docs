# Selected Apple Event Manager Functions

# Retired Document
Important:This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

# Selected Apple Event Manager Functions
This appendix provides a table of functions that you use to work with the data in Apple event data structures. For complete descriptions of these functions (and the underlying data types), seeApple Event Manager Reference.

## Functions for Working With Apple Event Data Structures
Figure A-1shows the hierarchy for key Apple event data structures. An Apple Event Manager function that operates on one of these data structures can also operate on any type that inherits from it. For example, the same function that works on a descriptor (AEDesc) also works on a descriptor list (AEDescList).
However, if there is a specific function for working with a data type, you should use that function. For example, becauseAppleEventinherits fromAEDesc, it is theoretically possible to create an Apple event with theAECreateDescfunction (assuming you have access to the raw data for the Apple event). However, you should instead use theAEBuildfunction or theAECreateAppleEventfunction, which are designed specifically for creating Apple events. For information on using these functions, seeTwo Approaches to Creating an Apple Event.
Table A-1shows some of the functions the Apple Event Manager provides for working with Apple event data structures. Functions listed for structure types higher in the table also work for types lower in the table, though as noted, you should generally use the most specific function available for a type. For structures that are stored by key value (such as Apple event attributes and parameters), you typically use a function that accesses data by key, rather than by index.
Some functions have both a pointer and a descriptor version (for example,AECoerceDescandAECoercePtr). The pointer version works with data in a pointed to buffer, while the descriptor version works with data that is in a descriptor.
Data type
Operation
Function
Descriptor
(AEdesc)
create
AECreateDesc,AEBuildDesc
dispose of
AEDisposeDesc
get data
AEGetDescData,AEGetDescDataSize,
AEGetDescDataRange(valid forAEDesctypes only)
set data
AEReplaceDescData
coerce
AECoerceDesc,AECoercePtr
Descriptor list
(AEDescList)
create
AECreateList
count
AECountItems
get by index (base 1)
AEGetNthDesc,AEGetNthPtr
delete by index (base 1)
AEDeleteItem
AEPutDesc,AEPutPtr,AEBuildDesc
Apple event record
(AERecord)
get by key
AEGetKeyDesc,AEGetKeyPtr
delete by key
AEDeleteKeyDesc
put by key
AEPutKeyDesc,AEPutKeyPtr
Apple event
(AppleEvent)
create
AECreateAppleEvent,
AEBuildAppleEvent
get by parameter
AEGetParamDesc,AEGetParamPtr
get by attribute
AEGetAttributeDesc,AEGetAttributePtr
delete by parameter
AEDeleteParam
put by parameter
AEPutParamDesc,AEPutParamPtr,AEBuildParameters
put by attribute
AEPutAttributeDesc,AEPutAttributePtr,AEBuildParameters
For the following functions, you can specify the descriptor type of the resulting data; if the actual descriptor type of the attribute or parameter is different from the specified type, the Apple Event Manager attempts to coerce it to the specified type:
- AEGetParamPtr
AEGetParamPtr
- AEGetParamDesc
AEGetParamDesc
- AEGetAttributePtr
AEGetAttributePtr
- AEGetAttributeDesc
AEGetAttributeDesc
- AEGetNthPtr
AEGetNthPtr
- AEGetNthDesc
AEGetNthDesc
Copyright © 2005, 2007 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2007-10-31