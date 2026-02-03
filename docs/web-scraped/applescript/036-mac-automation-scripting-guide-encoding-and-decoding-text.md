# Mac Automation Scripting Guide: Encoding and Decoding Text

## Encoding and Decoding Text

A standard practice when creating URL's is to encode spaces and special characters (high-level ASCII) to hexadecimal equivalents. For example, spaces in URL's are routinely converted to%20. The process of encoding and decoding URLs and other text in this manner can be accomplished through scripting.

### Encoding Characters

The handler inListing 32-1encodes a single character.
APPLESCRIPT
Open in Script Editor

- on encodeCharacter(theCharacter)
- set theASCIINumber to (the ASCII number theCharacter)
- set theHexList to {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"}
- set theFirstItem to item ((theASCIINumber div 16) + 1) of theHexList
- set theSecondItem to item ((theASCIINumber mod 16) + 1) of theHexList
- return ("%" & theFirstItem & theSecondItem) as string
- end encodeCharacter
Listing 32-2shows how to call the handler inListing 32-1.
APPLESCRIPT
Open in Script Editor

- encodeCharacter("$")
- --> Result: "%24"

### Encoding Text

The handler inListing 32-3encodes an entire string. Provide a string and indicate whether to encode two levels of special characters. The first level includes commonly encoded special characters, such as$,%, and*. The second level includes extended special characters that arenât typically encodedâ.,-,_, and:. High-level ASCII characters, such as copyright symbols, trademark symbols, and spaces, are always encoded.
APPLESCRIPT
Open in Script Editor

- on encodeText(theText, encodeCommonSpecialCharacters, encodeExtendedSpecialCharacters)
- set theStandardCharacters to "abcdefghijklmnopqrstuvwxyz0123456789"
- set theCommonSpecialCharacterList to "$+!'/?;&@=#%><{}\"~`^\\|*"
- set theExtendedSpecialCharacterList to ".-_:"
- set theAcceptableCharacters to theStandardCharacters
- if encodeCommonSpecialCharacters is false then set theAcceptableCharacters to theAcceptableCharacters & theCommonSpecialCharacterList
- if encodeExtendedSpecialCharacters is false then set theAcceptableCharacters to theAcceptableCharacters & theExtendedSpecialCharacterList
- set theEncodedText to ""
- repeat with theCurrentCharacter in theText
- if theCurrentCharacter is in theAcceptableCharacters then
- set theEncodedText to (theEncodedText & theCurrentCharacter)
- else
- set theEncodedText to (theEncodedText & encodeCharacter(theCurrentCharacter)) as string
- end if
- end repeat
- return theEncodedText
- end encodeText
Note
This handler calls theencodeCharacter()handler. SeeListing 32-1.
Listing 32-4shows how to call the handler inListing 32-3to encode only high-level ASCII characters.
APPLESCRIPT
Open in Script Editor

- encodeText("*smith-wilsonÂ© report_23.txt", false, false)
- --> Result: "*smith-wilson%A9%20report_23.txt"
Listing 32-5shows how to call the handler inListing 32-3to encode high-level ASCII characters and all special characters.
APPLESCRIPT
Open in Script Editor

- encodeText("*smith-wilsonÂ© report_23.txt", true, true)
- --> Result: "%2Asmith%2Dwilson%A9%20report%5F23%2Etxt"
Listing 32-6shows how to call the handler inListing 32-3to encode high-level ASCII characters and special characters, excluding periods, hyphens, underscores, and colons.
APPLESCRIPT
Open in Script Editor

- encodeText("annual smith-wilson_report.txt", true, false)
- --> Result: "annual%20smith-wilson_report.txt"
Note
When you use AppleScriptObjC, you can use methods of theNSStringclass to encode text. The handler inListing 32-7demonstrates how to do this.
APPLESCRIPT
Open in Script Editor

- on encodeText(theText)
- set theString to stringWithString_(theText) of NSString of current application
- set theEncoding to NSUTF8StringEncoding of current application
- set theAdjustedString to stringByAddingPercentEscapesUsingEncoding_(theEncoding) of theString
- return (theAdjustedString as string)
- end encodeText

### Decoding Text

The handler inListing 32-8decodes an encoded character hex string.
APPLESCRIPT
Open in Script Editor

- on decodeCharacterHexString(theCharacters)
- copy theCharacters to {theIdentifyingCharacter, theMultiplierCharacter, theRemainderCharacter}
- set theHexList to "123456789ABCDEF"
- if theMultiplierCharacter is in "ABCDEF" then
- set theMultiplierAmount to offset of theMultiplierCharacter in theHexList
- else
- set theMultiplierAmount to theMultiplierCharacter as integer
- end if
- if theRemainderCharacter is in "ABCDEF" then
- set theRemainderAmount to offset of theRemainderCharacter in theHexList
- else
- set theRemainderAmount to theRemainderCharacter as integer
- end if
- set theASCIINumber to (theMultiplierAmount * 16) + theRemainderAmount
- return (ASCII character theASCIINumber)
- end decodeCharacterHexString
Listing 32-9shows how to call the handler inListing 32-8.
APPLESCRIPT
Open in Script Editor

- decodeCharacterHexString("%24")
- --> Result: "$"
The handler inListing 32-10decodes any encoded character hex strings in the specified text.
APPLESCRIPT
Open in Script Editor

- on decodeText(theText)
- set flagA to false
- set flagB to false
- set theTempCharacter to ""
- set theCharacterList to {}
- repeat with theCurrentCharacter in theText
- set theCurrentCharacter to contents of theCurrentCharacter
- if theCurrentCharacter is "%" then
- set flagA to true
- else if flagA is true then
- set theTempCharacter to theCurrentCharacter
- set flagA to false
- set flagB to true
- else if flagB is true then
- set end of theCharacterList to decodeCharacterHexString(("%" & theTempCharacter & theCurrentCharacter) as string)
- set theTempCharacter to ""
- set flagA to false
- set flagB to false
- else
- set end of theCharacterList to theCurrentCharacter
- end if
- end repeat
- return theCharacterList as string
- end decodeText
Note
This handler calls thedecodeCharacterHexString()handler. SeeListing 32-8.
Listing 32-11shows how to call the handler inListing 32-10.
APPLESCRIPT
Open in Script Editor

- decodeText("%2Asmith%2Dwilson%A9%20report%5F23%2Etxt")
- --> Result: "*smith-wilsonÂ© report_23.txt"
Note
When you use AppleScriptObjC, you can use methods of theNSStringclass to decode URL encoded text. The handler inListing 32-12demonstrates how to do this.
APPLESCRIPT
Open in Script Editor

- on decodeText(theText)
- set theString to stringWithString_(theText) of NSString of current application
- set theEncoding to NSUTF8StringEncoding of current application
- set theAdjustedString to stringByReplacingPercentEscapesUsingEncoding_(theEncoding) of theString
- return (theAdjustedString as string)
- end decodeText
Converting RGB to HTML Color
Parsing HTML
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13