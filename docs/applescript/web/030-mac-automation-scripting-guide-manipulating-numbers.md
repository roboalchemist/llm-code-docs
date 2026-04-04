# Mac Automation Scripting Guide: Manipulating Numbers

## Manipulating Numbers

Working with and manipulating numbers is an important and regular occurrence in scripting. Basic mathematic operationsâsuch as addition, subtraction, multiplication, and divisionâare language-level features, but some other commonly performed operations require custom scripting.
Note
AppleScriptâs language-level mathematical operators are listed inOperators ReferenceinAppleScript Language Guide.
JavaScriptâs language-level arithmetic operators can be foundhere. JavaScript also includes a built-inMathobject, which provides a variety of properties and methods for performing common mathematical operations. Information about this object can be foundhere. Several of the JavaScript examples in this chapter call theMath.abs()method to get the absolute value of a number. AppleScript does not have an equivalent method.

### Converting a Number to a String

Scripts often need to convert numbers to string format to display information to the user or populate a document. In AppleScript, this conversion can be accomplished most of the time simply by using the coercion operatoras, as shown inListing 20-1.
APPLESCRIPT
Open in Script Editor

- 12 as string
- --> Result: "12"
In JavaScript, the same conversion can be accomplished by calling thetoString()method, as shown inListing 20-2.
JAVASCRIPT
Open in Script Editor

- num = 12
- num.toString()
- // Result: "12"

### Converting a Long Number to a String

In AppleScript, long numeric values are displayed in scientific notation. For example,1234000000is displayed by a script as1.234E+9. When this value is coerced to a string, it becomes:"1.234E+9". The handler inListing 20-3converts a number, regardless of length, to a string of numeric characters instead of a numeric string in scientific notation.
APPLESCRIPT
Open in Script Editor

- on convertNumberToString(theNumber)
- set theNumberString to theNumber as string
- set theOffset to offset of "E" in theNumberString
- if theOffset = 0 then return theNumberString
- set thePrefix to text 1 thru (theOffset - 1) of theNumberString
- set theConvertedNumberPrefix to ""
- if thePrefix begins with "-" then
- set theConvertedNumberPrefix to "-"
- if thePrefix = "-" then
- set thePrefix to ""
- else
- set thePrefix to text 2 thru -1 of thePrefix
- end if
- end if
- set theDecimalAdjustment to (text (theOffset + 1) thru -1 of theNumberString) as number
- set isNegativeDecimalAdjustment to theDecimalAdjustment is less than 0
- if isNegativeDecimalAdjustment then
- set thePrefix to (reverse of (characters of thePrefix)) as string
- set theDecimalAdjustment to -theDecimalAdjustment
- end if
- set theDecimalOffset to offset of "." in thePrefix
- if theDecimalOffset = 0 then
- set theFirstPart to ""
- else
- set theFirstPart to text 1 thru (theDecimalOffset - 1) of thePrefix
- end if
- set theSecondPart to text (theDecimalOffset + 1) thru -1 of thePrefix
- set theConvertedNumber to theFirstPart
- set theRepeatCount to theDecimalAdjustment
- if (length of theSecondPart) is greater than theRepeatCount then set theRepeatCount to length of theSecondPart
- repeat with a from 1 to theRepeatCount
- try
- set theConvertedNumber to theConvertedNumber & character a of theSecondPart
- on error
- set theConvertedNumber to theConvertedNumber & "0"
- end try
- if a = theDecimalAdjustment and a is not equal to (length of theSecondPart) then set theConvertedNumber to theConvertedNumber & "."
- end repeat     if theConvertedNumber ends with "." then set theConvertedNumber to theConvertedNumber & "0"
- if isNegativeDecimalAdjustment then set theConvertedNumber to (reverse of (characters of theConvertedNumber)) as string
- return theConvertedNumberPrefix & theConvertedNumber
- end convertNumberToString
Listing 20-3shows how to call the handler inListing 20-3.
APPLESCRIPT
Open in Script Editor

- convertNumberToString(8.72124243234E+11)
- --> Result: "872124243234"

### Adding a Descriptive Suffix to a Number

The handlersListing 20-5andListing 20-6convert a number to a string and appends a suffix of"st","nd","rd", or"th", resulting in strings such as"1st","2nd","3rd", and"4th".
APPLESCRIPT
Open in Script Editor

- on addDescriptiveSuffixToNumber(theNumber)
- -- Determine the suffix to add, based on the last two digits
- set theLastDigit to theNumber mod 10
- set theLastTwoDigits to theNumber mod 100
- set theSuffix to "th"
- if {1, -1} contains theLastDigit and {11, -11} does not contain theLastTwoDigits then
- set theSuffix to "st"
- else if {2, -2} contains theLastDigit and {12, -12} does not contain theLastTwoDigits then
- set theSuffix to "nd"
- else if {3, -3} contains theLastDigit and {13, -13} does not contain theLastTwoDigits then
- set theSuffix to "rd"
- end if
- -- Return the number and suffix
- return (theNumber as string) & theSuffix
- end addDescriptiveSuffixToNumber
JAVASCRIPT
Open in Script Editor

- function addDescriptiveSuffixToNumber(num) {
- // Convert the number to absolute value
- var integer = Math.abs(num)
- // Determine the suffix to add, based on the last two digits
- var suffix = "th"
- var lastDigit = integer % 10
- var lastTwoDigits = integer % 100
- if (lastDigit === 1 && lastTwoDigits !== 11) {
- suffix = "st"
- }
- else if (lastDigit === 2 && lastTwoDigits !== 12) {
- suffix = "nd"
- }
- else if (lastDigit === 3 && lastTwoDigits !== 13) {
- suffix = "rd"
- }
- // Return the number and suffix
- return num.toString() + suffix
- }
Listing 20-7andListing 20-8show how to test the handlers inListing 20-5andListing 20-6by looping through a range of positive and negative numbers.
APPLESCRIPT
Open in Script Editor

- set theTestResults to ""
- repeat with a from -10 to 10
- set theTestResults to theTestResults & addDescriptiveSuffixToNumber(a)
- if a is less than 10 then set theTestResults to theTestResults & ", "
- end repeat
- theTestResults
- --> Result: "-10th, -9th, -8th, -7th, -6th, -5th, -4th, -3rd, -2nd, -1st, 0, 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th, 10th"
JAVASCRIPT
Open in Script Editor

- var testResults = ""
- for (var i = -10; i <= 10; i++) {
- testResults += addDescriptiveSuffixToNumber(i)
- if (i < 10) {
- testResults += ", "
- }
- }
- testResults
- // Result: "-10th, -9th, -8th, -7th, -6th, -5th, -4th, -3rd, -2nd, -1st, 0th, 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th, 10th"
Listing 20-9andListing 20-10show how to call the handlers inListing 20-5andListing 20-6to identify positions of items in a list.
APPLESCRIPT
Open in Script Editor

- set thePersonList to {"Sal", "Ben", "Chris", "David"}
- set theListLength to length of thePersonList
- repeat with a from 1 to theListLength
- set theSuffixedNumber to addDescriptiveSuffixToNumber(a)
- set thePerson to item a of thePersonList
- display dialog "The " & theSuffixedNumber & " person in list is " & thePerson & "."
- end repeat
JAVASCRIPT
Open in Script Editor

- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- var personList = ["Sal", "Ben", "Chris", "David"]
- var listLength = personList.length
- for (var i = 0; i < listLength; i++) {
- var suffixedNum = addDescriptiveSuffixToNumber(i + 1)
- var person = personList[i]
- app.displayDialog(`The ${suffixedNum} person in list is ${person}.`)
- }

### Adding Leading Zeros to a Number

The handlers inListing 20-11andListing 20-12convert a number to a string and prepends it with leading zeros until it reaches a certain length. They accept two parametersâthe number to add leading zeros to and the maximum number of leading zeros to add. For example, if the maximum number of leading zeros is set to2, the results range from001to999. If the maximum number of leading zeros is3, the results range from0001to9999, and so on.
APPLESCRIPT
Open in Script Editor

- on addLeadingZerosToNumber(theNumber, theMaxLeadingZeroCount)
- -- Determine if the number is negative
- set isNegative to theNumber is less than 0
- -- Determine when the maximum number of digits will be reached
- set theThreshold to (10 ^ theMaxLeadingZeroCount) as integer
- -- If the number is shorter than the maximum number of digits
- if theNumber is less than theThreshold then
- -- If the number is negative, convert it to positive
- if isNegative = true then set theNumber to -theNumber
- -- Add the zeros to the number
- set theLeadingZeros to ""
- set theDigitCount to length of ((theNumber div 1) as string)
- set theCharacterCount to (theMaxLeadingZeroCount + 1) - theDigitCount
- repeat theCharacterCount times
- set theLeadingZeros to (theLeadingZeros & "0") as string
- end repeat
- -- Make the number negative, if it was previously negative
- if isNegative = true then set theLeadingZeros to "-" & theLeadingZeros
- -- Return the prefixed number
- return (theLeadingZeros & (theNumber as text)) as string
- -- If the number is greater than or equal to the maximum number of digits
- else
- -- Return the original number
- return theNumber as text
- end if
- end addLeadingZerosToNumber
JAVASCRIPT
Open in Script Editor

- function addLeadingZerosToNumber(num, maxLeadingZeroCount) {
- var leadingZeros = ""
- // Convert the number to absolute value
- var absNum = Math.abs(num)
- // Determine when the maximum number of digits will be reached
- var threshold = Math.pow(10, maxLeadingZeroCount)
- // If the number is shorter than the maximum number of digits
- if (absNum < threshold) {
- // Prepare a leading zeros string
- var digitCount = Math.trunc(absNum).toString().length
- var charCount = maxLeadingZeroCount + 1 - digitCount
- for (var i = 0 ; i < charCount; i++) {
- leadingZeros += "0"
- }
- }
- // Add the zeros to the number
- var result = `${leadingZeros}${absNum}`
- // Make the number negative, if it was previously negative
- if (num < 0) {
- result = `-${result}`
- }
- // Return the prefixed number
- return result
- }
Listing 20-13andListing 20-14show how to call the handlers inListing 20-11andListing 20-12.
APPLESCRIPT
Open in Script Editor

- addLeadingZerosToNumber(9, 3)
- --> Result: "0009"
JAVASCRIPT
Open in Script Editor

- addLeadingZerosToNumber(9, 3)
- // Result: "0009"

### Comma-Delimiting a Number

The handlersListing 20-15andListing 20-16comma-delimit a numeric value and converts it to a string.
Note
These handlers call theconvertNumberToString()handler. SeeListing 20-3.
APPLESCRIPT
Open in Script Editor

- on convertNumberToCommaDelimitedString(theNumber)
- -- Convert the number to a string
- set theNumber to convertNumberToString(theNumber)
- -- Determine the length of the number
- set theNumberLength to length of theNumber
- -- Reverse the number so a comma can be added every 3 digits
- set theNumber to (reverse of every character of theNumber) as string
- -- Loop through the number's digits, add commas, and put the numbers back in the correct order
- set theConvertedNumber to ""
- repeat with a from 1 to theNumberLength
- if a is theNumberLength or (a mod 3) is not 0 then
- set theConvertedNumber to (character a of theNumber & theConvertedNumber) as string
- else
- set theConvertedNumber to ("," & character a of theNumber & theConvertedNumber) as string
- end if
- end repeat
- -- Return the comma delimited number
- return theConvertedNumber
- end convertNumberToCommaDelimitedString
JAVASCRIPT
Open in Script Editor

- function convertNumberToCommaDelimitedString(num) {
- // Convert the number to a string
- var numString = num.toString()
- if (numString.indexOf("e") != - 1) {
- numString = convertNumberToString(numString)
- }
- // Reverse the number so a comma can be added every 3 digits
- numString = numString.split("").reverse().join("")
- var numStringWithCommas = ""
- // Determine the length of the number
- var numStringLength = numString.length
- // Loop through the number's digits, add commas, and put the numbers back in the correct order
- for (var i = 0; i < numStringLength; i++) {
- var toPrepend = numString[i]
- if (i != numStringLength - 1 && ((i + 1) % 3) == 0) {
- toPrepend = "," + toPrepend
- }
- numStringWithCommas = toPrepend + numStringWithCommas
- }
- // Return the comma delimited number
- return numStringWithCommas
- }
Listing 20-17andListing 20-18shows how to call the handlers inListing 20-15andListing 20-16.
APPLESCRIPT
Open in Script Editor

- convertNumberToCommaDelimitedString(872124243234)
- --> Result: "872,124,243,234"
JAVASCRIPT
Open in Script Editor

- convertNumberToCommaDelimitedString(872124243234)
- // Result: "872,124,243,234"
Note
When you use AppleScriptObjC or JavaScriptObjC, you can use methods of theNSNumberFormatterto format numbers in different ways.
The handlers inListing 20-19andListing 20-20convert a number to a string by returning a comma-delimited, rounded, localized decimal value. For example: (3.64525432506E+5at 0 places converts to"364525",3.64525432506E+5at 3 places converts to"364525.433", and0.2375at 2 places converts"0.24".
APPLESCRIPT
Open in Script Editor

- use framework "Foundation"
- on convertNumberToDecimalString(theNumber, theNumberOfDecimalPlaces)
- if theNumberOfDecimalPlaces is greater than 0 then
- set theDecimalIndicators to "."
- repeat theNumberOfDecimalPlaces times
- set theDecimalIndicators to theDecimalIndicators & "#"
- end repeat
- else
- set theDecimalIndicators to ""
- end if
- set theFormatter to init() of alloc() of NSNumberFormatter of current application
- setFormat_("0" & theDecimalIndicators) of theFormatter
- set theFormattedNumber to stringFromNumber_(theNumber) of theFormatter
- return (theFormattedNumber as string)
- end convertNumberToDecimalString
JAVASCRIPT
Open in Script Editor

- function convertNumberToDecimalString(number, numberOfDecimalPlaces) {
- var decimalIndicators = ""
- if (numberOfDecimalPlaces > 0) {
- decimalIndicators = "."
- for (var i = 0; i < numberOfDecimalPlaces; i++) {
- decimalIndicators += "#"
- }
- }
- var formatter = $.NSNumberFormatter.new
- formatter.format = `0${decimalIndicators}`
- var formattedNumber = formatter.stringFromNumber(number)
- return formattedNumber.js
- }
The handlers inListing 20-21andListing 20-22convert a number to a string by returning a comma-delimited, rounded, localized percentage value. For example:0.2345to"23%"or0.2375to"24%".
APPLESCRIPT
Open in Script Editor

- use framework "Foundation"
- on convertNumberToPercentageString(theNumber)
- set theStyle to NSNumberFormatterPercentStyle of current application
- set theFormattedNumber to localizedStringFromNumber_numberStyle_(theNumber, theStyle) of NSNumberFormatter of current application
- return (theFormattedNumber as string)
- end convertNumberToPercentageString
JAVASCRIPT
Open in Script Editor

- function convertNumberToPercentageString(number) {
- var style = $.NSNumberFormatterPercentStyle
- var formattedNumber = $.NSNumberFormatter.localizedStringFromNumberNumberStyle(number, style)
- return formattedNumber.js
- }
The handlers inListing 20-23andListing 20-24convert a number to a string by returning a comma-delimited, rounded, localized currency value. For example:9128to"$9,128.00"or9978.2485to"$9,978.25".
APPLESCRIPT
Open in Script Editor

- use framework "Foundation"
- on convertNumberToCurrencyString(theNumber)
- set theStyle to NSNumberFormatterCurrencyStyle of current application
- set theFormattedNumber to localizedStringFromNumber_numberStyle_(theNumber, theStyle) of NSNumberFormatter of current application
- return (theFormattedNumber as string)
- end convertNumberToCurrencyString
JAVASCRIPT
Open in Script Editor

- function convertNumberToCurrencyString(number) {
- var style = $.NSNumberFormatterCurrencyStyle
- var formattedNumber = $.NSNumberFormatter.localizedStringFromNumberNumberStyle(number, style)
- return formattedNumber.js
- }
The handlers inListing 20-25andListing 20-26convert a number to a string by returning a string of a numeric value in words. For example:23to âtwenty-three",23.75to"twenty-three point seven five".
APPLESCRIPT
Open in Script Editor

- use framework "Foundation"
- on convertNumberToWords(theNumber)
- set theStyle to NSNumberFormatterSpellOutStyle of current application
- set theFormattedNumber to localizedStringFromNumber_numberStyle_(theNumber, theStyle) of NSNumberFormatter of current application
- return (theFormattedNumber as string)
- end convertNumberToWords
JAVASCRIPT
Open in Script Editor

- function convertNumberToWords(number) {
- var style = $.NSNumberFormatterSpellOutStyle
- var formattedNumber = $.NSNumberFormatter.localizedStringFromNumberNumberStyle(number, style)
- return formattedNumber.js
- }
In JavaScript,regular expressionscan also be used to convert a number to a comma-delimited string even more efficiently, as shown inListing 20-27.
JAVASCRIPT
Open in Script Editor

- function convertNumberToCommaDelimitedString(num) {
- var numPieces = num.toString().split(".")
- numPieces[0] = numPieces[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
- return numPieces.join(".")
- }

### Determining if a Number is an Odd Number

The handlers inListing 20-28andListing 20-29determine whether a whole number is even or odd. A returned value offalseindicates the passed number is even; a returned value oftrueindicates the passed number is odd.
APPLESCRIPT
Open in Script Editor

- on isNumberOdd(theNumber)
- if theNumber mod 2 is not 0 then
- return true
- else
- return false
- end if
- end isNumberOdd
JAVASCRIPT
Open in Script Editor

- function isNumberOdd(num) {
- return num % 2 !== 0
- }
Listing 20-30andListing 20-31show how to call the handlers inListing 20-28andListing 20-29.
APPLESCRIPT
Open in Script Editor

- isNumberOdd(3)
- --> Result: true
JAVASCRIPT
Open in Script Editor

- isNumberOdd(3)
- // Result: true
Listing 20-32andListing 20-33show how to call the handlers inListing 20-28andListing 20-29by prompting the user to enter an even number.
APPLESCRIPT
Open in Script Editor

- repeat
- display dialog "Enter an even integer:" default answer ""
- try
- if text returned of result is not "" then set theNumberProvided to text returned of result as integer
- if isNumberOdd(theNumberProvided) is false then exit repeat
- end try
- end repeat
JAVASCRIPT
Open in Script Editor

- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- while (true) {
- var result = app.displayDialog("Enter an even integer:", {defaultAnswer: ""})
- var text = result.textReturned
- if (text !== "") {
- var num = Number(text)
- if (!isNumberOdd(num)) {
- break
- }
- }
- }

### Rounding and Truncating a Number

The handlers inListing 20-34andListing 20-35round and truncate a numeric value, and convert it to a string. Provide a numeric value and indicate a number of decimal places.
Note
These handlers call theconvertNumberToString()handler. SeeListing 20-3.
APPLESCRIPT
Open in Script Editor

- on roundAndTruncateNumber(theNumber, numberOfDecimalPlaces)
- if numberOfDecimalPlaces is 0 then
- set theNumber to theNumber + 0.5
- return convertNumberToString(theNumber div 1)
- end if
- set theRoundingValue to "5"
- repeat numberOfDecimalPlaces times
- set theRoundingValue to "0" & theRoundingValue
- end repeat
- set theRoundingValue to ("." & theRoundingValue) as number
- set theNumber to theNumber + theRoundingValue
- set theModValue to "1"
- repeat numberOfDecimalPlaces - 1 times
- set theModValue to "0" & theModValue
- end repeat
- set theModValue to ("." & theModValue) as number
- set theSecondPart to (theNumber mod 1) div theModValue
- if length of (theSecondPart as text) is less than numberOfDecimalPlaces then
- repeat numberOfDecimalPlaces - (the length of (theSecondPart as text)) times
- set theSecondPart to ("0" & theSecondPart) as string
- end repeat
- end if
- set theFirstPart to theNumber div 1
- set theFirstPart to convertNumberToString(theFirstPart)
- set theNumber to (theFirstPart & "." & theSecondPart)
- return theNumber
- end roundAndTruncateNumber
JAVASCRIPT
Open in Script Editor

- function roundAndTruncateNumber(num, numDecimalPlaces) {
- if (numDecimalPlaces === 0) {
- num = num + 0.5
- return convertNumberToString(num / 1)
- }
- var roundingValue = "5"
- for (var i = 0; i < numDecimalPlaces; i++) {
- roundingValue = "0" + roundingValue
- }
- roundingValue = Number("0." + roundingValue)
- num += roundingValue
- var modValue = "1"
- for (var i = 0; i < numDecimalPlaces - 1; i++) {
- modValue = "0" + modValue
- }
- modValue = Number("0." + modValue)
- var secondPart = Math.floor((num % 1) / modValue)
- var secondPartStringLength = secondPart.toString().length
- if (secondPartStringLength < numDecimalPlaces) {
- var count = numDecimalPlaces - secondPartStringLength
- for (var i = 0; i < count; i++) {
- secondPart = "0" + secondPart
- }
- }
- var firstPart = Math.floor(num)
- firstPart = convertNumberToString(firstPart)
- return `${firstPart}.${secondPart}`
- }
Listing 20-36shows how to call the handler inListing 20-34.
APPLESCRIPT
Open in Script Editor

- roundAndTruncateNumber(1.04575, 3)
- --> Result: "1.046"
Manipulating Text
Manipulating Lists of Items
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13
