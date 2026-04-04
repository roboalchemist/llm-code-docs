# Default Coercion Handlers

# Retired Document
Important:This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

This appendix lists the type conversions performed by the default coercion handlers provided by the Mac OS. These handlers may be implemented by the Apple Event Manager, the Open Scripting framework, or other frameworks.
Support for the following  coercions was added in Mac OS X version 10.4:
- Between these types:typeStyledText,typeUnicodeText,typeUTF8Text, andtypeUTF16ExternalRepresentationand these types:typeType,typeEnumerated, and the numeric typestypeSInt16,typeSInt32,typeUInt32,typeSInt64,typeIEEE32BitFloatingPoint,typeIEEE64BitFloatingPoint, andtypeExtended.Important:See the description for thetypePixelMapenum inApple Event Manager Referencefor important information about restrictions on coercions involving typeStyledText.See tableTable C-1for a mapping  between the preferred and non-preferred numeric constant names.
Between these types:
typeStyledText,typeUnicodeText,typeUTF8Text, andtypeUTF16ExternalRepresentation
and these types:
typeType,typeEnumerated, and the numeric typestypeSInt16,typeSInt32,typeUInt32,typeSInt64,typeIEEE32BitFloatingPoint,typeIEEE64BitFloatingPoint, andtypeExtended.
Important:See the description for thetypePixelMapenum inApple Event Manager Referencefor important information about restrictions on coercions involving typeStyledText.
See tableTable C-1for a mapping  between the preferred and non-preferred numeric constant names.
- FromtypeChartotypeStyledText.Note:Starting in Mac OS X version 10.3,typeCharis deprecated in favor of one of the Unicode string types. For details, see the descriptions fortypeCharand for the Unicode string types (typeUnicodeText) inApple Event Manager Reference.
FromtypeChartotypeStyledText.
Note:Starting in Mac OS X version 10.3,typeCharis deprecated in favor of one of the Unicode string types. For details, see the descriptions fortypeCharand for the Unicode string types (typeUnicodeText) inApple Event Manager Reference.

## Coercion Handler Tables
Table C-1shows some older, non-preferred numeric constant names and their preferred equivalents. To find available coercions for a non-preferred name fromTable C-1, look up its equivalent preferred name inTable C-2.
Non-preferred numeric constant name
Preferred numeric constant name
typeSMInt,typeShortInteger
typeSInt16
typeInteger,typeLongInteger
typeSInt32
typeMagnitude
typeUInt32
typeComp
typeSInt64
typeSMFloat,typeShortFloat
typeIEEE32BitFloatingPoint
typeFloat,typeLongFloat
typeIEEE64BitFloatingPoint
Table C-2lists the default coercions handled by the Apple Event Manager.
Coerce from descriptor type
To descriptor type
Comment
typeChar
typeStyledText
typeUnicodeText
typeUTF8Text
typeUTF16ExternalRepresentation
typeSInt16
typeSInt32
typeSInt64
typeIEEE32BitFloatingPoint
typeIEEE64BitFloatingPoint
typeExtended
Any string that is a valid representation of a number can be coerced into an equivalent numeric value.
typeSInt16
typeSInt32
typeSInt64
typeIEEE32BitFloatingPoint
typeIEEE64BitFloatingPoint
typeExtended
typeChar
typeStyledText
typeUnicodeText
typeUTF8Text
typeUTF16ExternalRepresentation
Any numeric descriptor type can be coerced into the equivalent text string.
typeSInt16
typeSInt32
typeSInt64
typeIEEE32BitFloatingPoint
typeIEEE64BitFloatingPoint
typeExtended
typeSInt16
typeSInt32
typeSInt64
typeIEEE32BitFloatingPoint
typeIEEE64BitFloatingPoint
typeExtended
Any numeric descriptor type can be coerced into any other numeric descriptor type.
typeChar
typeIntlText
typeStyledText
typeUnicodeText
typeUTF8Text
typeUTF16ExternalRepresentation
typeChar
typeIntlText
typeStyledText
typeUnicodeText
typeUTF8Text
typeUTF16ExternalRepresentation
If the destination encoding cannot represent a character in the source text, the result is undefined.
typeChar
typeStyledText
typeUnicodeText
typeUTF8Text
typeUTF16ExternalRepresentation
typeType
typeEnumerated
typeKeyword
typeProperty
Any four-character string can be coerced to one of these descriptor types.
typeEnumerated
typeKeyword
typeProperty
typeType
typeChar
typeStyledText
typeUnicodeText
typeUTF8Text
typeUTF16ExternalRepresentation
Any of these descriptor types can be coerced to the equivalent text string.
typeIntlText
typeChar
typeStyledText
typeUnicodeText
typeUTF8Text
typeUTF16ExternalRepresentation
The result contains text only, without the script code or language code from the original descriptor.
typeTrue
typeBoolean
The result is the Boolean valuetrue.
typeFalse
typeBoolean
The result is the Boolean valuefalse.
typeEnumerated
typeBoolean
The enumerated value'true'becomes the Boolean value true. The enumerated value'fals'becomes the Boolean value false.
typeBoolean
typeEnumerated
The Boolean valuefalsebecomes the enumerated value'fals'. The Boolean valuetruebecomes the enumerated value'true'.
typeSInt16
typeBoolean
A value of 1 becomes the Boolean valuetrue. A value of 0 becomes the Boolean valuefalse.
typeBoolean
typeSInt16
A value offalsebecomes 0. A value oftruebecomes 1.
typeAlias
typeFSS
An alias is coerced into a file system specification. Not recommendedâusetypeFSRefinstead.
typeAlias
typeFSRef
An alias is coerced into a file system reference.
typeAppleEvent
typeAppParameters
An Apple event is coerced into a list of application parameters for theLaunchParamBlockRecparameter block.
any descriptor type
typeAEList
A descriptor is coerced into a descriptor list containing a single item.
typeAEList
type of list item
A descriptor list containing a single descriptor is coerced into a descriptor.
Copyright © 2005, 2007 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2007-10-31