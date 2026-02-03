# Mac Automation Scripting Guide: Manipulating Lists of Items

## Manipulating Lists of Items
In scripting, a listâtypically referred to as an array in JavaScriptâis a an ordered collection of values thatâs stored in a single object. A script can loop through the items of a list in order to process the items individually. There are many other tasks scripts commonly performed with lists, such as joining and sorting, which usually require custom scripting.
Note
For general information about working with lists in AppleScript, see thelistclass reference documentation inAppleScript Language Guide.
In JavaScript, theArrayobject provides a range of processing functions. Information about this object can be foundhere.

### Looping through a List
Listing 21-1andListing 21-2show how to incrementally loop through a list. In these examples, a variableâain AppleScript andiin JavaScriptârepresents an integer value from1through the number of items in the list. Each loop causes this variable value to increase, and you can use the increment variable to target a specific list item.
APPLESCRIPT
Open in Script Editor
- set theList to {"Sal", "Ben", "David", "Chris"}
- repeat with a from 1 to length of theList
- set theCurrentListItem to item a of theList
- -- Process the current list item
- display dialog theCurrentListItem & " is item " & a & " in the list."
- end repeat
JAVASCRIPT
Open in Script Editor
- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- var array = ["Sal", "Ben", "David", "Chris"]
- var arrayLength = array.length
- for (var i = 0; i < arrayLength; i++) {
- var currentArrayItem = array[i]
- // Process the current array item
- app.displayDialog(`${currentArrayItem} is item ${i + 1} in the array.`)
- }
A script can also loop through a list of items more directly by dynamically assigning a list item to a variable. InListing 21-3andListing 21-4, a variableâtheCurrentListItemin AppleScript andcurrentArrayItemin JavaScriptârepresents the item matching the current loop.
APPLESCRIPT
Open in Script Editor
- set theList to {"Sal", "Ben", "David", "Chris"}
- repeat with theCurrentListItem in theList
- -- Process the current list item
- display dialog theCurrentListItem & " is an item in the list."
- end repeat
JAVASCRIPT
Open in Script Editor
- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- var array = ["Sal", "Ben", "David", "Chris"]
- var arrayLength = array.length
- for (var currentArrayItem of array) {
- // Process the current array item
- app.displayDialog(`${currentArrayItem} is an item in the array.`)
- }
Note
For more information about looping through list items in AppleScript, seeControl Statements ReferenceinAppleScript Language Guide.

### Converting a List to a String
The handler inListing 21-5joins a list of strings together in AppleScript, separating them by a specific delimiter.
APPLESCRIPT
Open in Script Editor
- on convertListToString(theList, theDelimiter)
- set AppleScript's text item delimiters to theDelimiter
- set theString to theList as string
- set AppleScript's text item delimiters to ""
- return theString
- end convertListToString
Listing 21-6shows how to call the handler inListing 21-5.
APPLESCRIPT
Open in Script Editor
- set theList to {"The", "quick", "brown", "fox", "jumps", "over", "a", "lazy", "dog."}
- convertListToString(theList, space)
- --> Result: "The quick brown fox jumps over a lazy dog."
In JavaScript, custom scripting isnât required to perform this operation. TheArrayobject has ajoin()method, which can be called to merge a list of items together, as shown inListing 21-7.
JAVASCRIPT
Open in Script Editor
- var array = ["The", "quick", "brown", "fox", "jumps", "over", "a", "lazy", "dog."]
- var array.join(" ")
- // Result: "The quick brown fox jumps over a lazy dog."
Note
SeeSplitting Textto learn how to break text apart, based on a specific delimiter.
When you use AppleScriptObjC or JavaScriptObjC, you can use methods of theNSArrayclass to convert a list of strings into a single string. The handlers inListing 21-8andListing 21-9demonstrate how to do this.
APPLESCRIPT
Open in Script Editor
- on convertListToString(theList, theDelimiter)
- set theArray to arrayWithArray_(theList) of NSArray of current application
- set theString to componentsJoinedByString_(theDelimiter) of theArray
- return (theString as string)
- end convertListToString
JAVASCRIPT
Open in Script Editor
- function convertArrayToString(array, delimiter) {
- array = $(array)
- array = array.componentsJoinedByString(delimiter)
- return array.js
- }

### Counting the Items in a List
Listing 21-10andListing 21-11show how to get the number of items in a list.
APPLESCRIPT
Open in Script Editor
- set theList to {"Apple Watch", "iMac", "iPhone", "MacBook Pro"}
- length of theList
- --> Result: 4
JAVASCRIPT
Open in Script Editor
- var array = ["Apple Watch", "iMac", "iPhone", "MacBook Pro"]
- array.length
- // Result: 4

### Counting the Occurrences of an Item in a List
The handlers inListing 21-12andListing 21-13count how many times an item appears in a list.
APPLESCRIPT
Open in Script Editor
- on countInstancesOfItemInList(theList, theItem)
- set theCount to 0
- repeat with a from 1 to count of theList
- if item a of theList is theItem then
- set theCount to theCount + 1
- end if
- end repeat
- return theCount
- end countInstancesOfItemInList
JAVASCRIPT
Open in Script Editor
- function countInstancesOfItemInArray(array, item) {
- var count = 0
- for (var element of array) {
- if (element === item) {
- count++
- }
- }
- return count
- }
Listing 21-14andListing 21-15show how to call the handlers inListing 21-12andListing 21-13.
APPLESCRIPT
Open in Script Editor
- set theList to {"Sal", "Jen", "Ben", "David", "Chris", "Jen"}
- countInstancesOfItemInList(theList, "Jen")
- --> Result: 2
JAVASCRIPT
Open in Script Editor
- var array = ["Sal", "Jen", "Ben", "David", "Chris", "Jen"]
- countInstancesOfItemInArray(array, "Jen")
- // Result: 2

### Determining if a List Contains a Specific Item
Listing 21-16andListing 21-17return atrueorfalsevalue, indicating the presence of an item in a list.
APPLESCRIPT
Open in Script Editor
- set theList to {"Sal", "Ben", "David", "Chris"}
- theList contains "Lizzie"
- --> false
JAVASCRIPT
Open in Script Editor
- var array = ["Sal", "Ben", "David", "Chris"]
- array.includes("Lizzie")
- // Result: false
Listing 21-18andListing 21-19demonstrate how to add an item to a list only if the list doesnât already contain the item.
APPLESCRIPT
Open in Script Editor
- set theList to {"Sal", "Ben", "David", "Chris"}
- if theList does not contain "Jen" then
- set end of theList to "Jen"
- end if
- return theList
- --> Result: {"Sal", "Ben", "David", "Chris", "Jen"}
JAVASCRIPT
Open in Script Editor
- var array = ["Sal", "Ben", "David", "Chris"]
- if (!array.includes("Jen")) {
- array.push("Jen")
- }
- array
- // Result: ["Sal", "Ben", "David", "Chris", "Jen"]

### Determining the Position of an Item in a List
The handler inListing 21-20determines the position of an item the first time it appears in a list.
APPLESCRIPT
Open in Script Editor
- on getPositionOfItemInList(theItem, theList)
- repeat with a from 1 to count of theList
- if item a of theList is theItem then return a
- end repeat
- return 0
- end getPositionOfItemInList
Listing 21-21shows how to call the handler inListing 21-20. In AppleScript, list item positions start at1âthe first item in a list has a position of1.
APPLESCRIPT
Open in Script Editor
- set theList to {"Sal", "Ben", "David", "Chris", "Jen", "Lizzie", "Maddie", "Lillie"}
- getPositionOfItemInList("Maddie", theList)
- --> Result: 7
In JavaScript, theindexOf()method of theArrayobject can be called to determine the position of an item in an array, as shown inListing 21-22. In JavaScript, array item positions start at0âthe first item in an array has an index of0.
JAVASCRIPT
Open in Script Editor
- var array = ["Sal", "Ben", "David", "Chris", "Jen", "Lizzie", "Maddie", "Lillie]
- array.indexOf("Maddie")
- // Result: 6
ThegetPositionOfItemInList()AppleScript handler andindexOf()JavaScript method can be used to cross-reference data between corresponding lists. InListing 21-23andListing 21-24, a person is located in a list by name. Next, the personâs phone extension is located in a corresponding list.
APPLESCRIPT
Open in Script Editor
- set theNames to {"Sal", "Ben", "David", "Chris", "Jen", "Lizzie", "Maddie", "Lillie"}
- set theExtensions to {"x1111", "x2222", "x3333", "x4444", "x5555", "x6666", "x7777", "x8888"}}
- set thePerson to choose from list theNames with prompt "Choose a person:"
- if thePerson is false then error number -128
- set theExtension to item (getPositionOfItemInList((thePerson as string), theNames)) of theExtensions
- display dialog "The phone extension for " & thePerson & " is " & theExtension & "."
JAVASCRIPT
Open in Script Editor
- var app = Application.currentApplication()
- app.includeStandardAdditions = true
- var names = ["Sal", "Ben", "David", "Chris", "Jen", "Lizzie", "Maddie", "Lillie"]
- var extensions = ["x1111", "x2222", "x3333", "x4444", "x5555", "x6666", "x7777", "x8888"]
- var people = app.chooseFromList(names, {withPrompt: "Choose a person:"})
- if (!people) {
- throw new Error(-128)
- }
- var person = people[0]
- var index = names.indexOf(person)
- console.log(index)
- var extension = extensions[index]
- app.displayDialog(`The phone extension for ${person} is ${extension}.`)

### Determining Multiple Positions of an Item in a List
The handlers inListing 21-25andListing 21-26determine every position of an item in a list.
APPLESCRIPT
Open in Script Editor
- on getPositionsOfItemInList(theItem, theList, listFirstPositionOnly)
- set thePositions to {}
- repeat with a from 1 to length of theList
- if item a of theList is theItem then
- if listFirstPositionOnly = true then return a
- set end of thePositions to a
- end if
- end repeat
- if listFirstPositionOnly is true and thePositions = {} then return 0
- return thePositions
- end getPositionsOfItemInList
JAVASCRIPT
Open in Script Editor
- function getPositionsOfItemInArray(item, array, firstPositionOnly) {
- if (firstPositionOnly) {
- return array.indexOf(item)
- }
- var indexes = []
- for (var index = 0; index < array.length; index++) {
- var element = array[index]
- if (element === item) {
- indexes.push(index)
- }
- }
- return indexes
- }
Listing 21-27andListing 21-28show how to call the handlers inListing 21-25andListing 21-26.
APPLESCRIPT
Open in Script Editor
- set theList to {"Sal", "Ben", "Jen", "David", "Chris", "Lizzie", "Maddie", "Jen", "Lillie"}
- getPositionsOfItemInList("Jen", theList, false)
- --> Result: {3, 8}
JAVASCRIPT
Open in Script Editor
- var array = ["Sal", "Ben", "Jen", "David", "Chris", "Lizzie", "Maddie", "Jen", "Lillie"]
- getPositionsOfItemInArray("Jen", array, false)
- // Result: [2, 7]

### Finding the Highest Numeric Value in a List
The handlers inListing 21-29andListing 21-30determine the highest numeric value in a list of items. The passed list can contain non-numeric data as well as lists within lists.
APPLESCRIPT
Open in Script Editor
- on getHighestNumberInList(theList)
- set theHighestNumber to false
- repeat with a from 1 to count of theList
- set theCurrentItem to item a of theList
- set theClass to class of theCurrentItem
- if theClass is in {integer, real} then
- if theHighestNumber is "" then
- set theHighestNumber to theCurrentItem
- else if theCurrentItem is greater than theHighestNumber then
- set theHighestNumber to item a of theList
- end if
- else if theClass is list then
- set theHighValue to getHighestNumberInList(theCurrentItem)
- if theHighValue is greater than theHighestNumber then
- set theHighestNumber to theHighValue
- end if
- end if
- end repeat
- return theHighestNumber
- end getHighestNumberInList
JAVASCRIPT
Open in Script Editor
- function getHighestNumberInList(list) {
- var highestNumber = undefined
- for (var item of list) {
- var number = undefined
- if (item.constructor === Number) {
- number = item
- }
- else if (item.constructor === Array) {
- number = getHighestNumberInList(item)
- }
- if (number != undefined && (highestNumber === undefined || number > highestNumber)) {
- highestNumber = number
- }
- }
- return highestNumber
- }
Listing 21-31andListing 21-32show how to call the handlers inListing 21-29andListing 21-30for a list containing a mixture of numbers and strings.
APPLESCRIPT
Open in Script Editor
- getHighestNumberInList({-3.25, 23, 2345, "sid", 3, 67})
- --> Result: 2345
JAVASCRIPT
Open in Script Editor
- getHighestNumberInList([-3.25, 23, 2345, "sid", 3, 67])
- // Result: 2345
Listing 21-33andListing 21-34show how to call the handlers inListing 21-29andListing 21-30for a list containing a mixture of numbers, strings, booleans, and lists.
APPLESCRIPT
Open in Script Editor
- getHighestNumberInList({-3.25, 23, {23, 78695, "bob"}, 2345, true, "sid", 3, 67})
- --> Result: 78695
JAVASCRIPT
Open in Script Editor
- getHighestNumberInList([-3.25, 23, [23, 78695, "bob"], 2345, true, "sid", 3, 67])
- // Result: 78695
Listing 21-35andListing 21-36show how to call the handlers inListing 21-29andListing 21-30for a list containing only strings.
APPLESCRIPT
Open in Script Editor
- getHighestNumberInList({"this", "list", "contains", "only", "text"})
- --> Result: false
JAVASCRIPT
Open in Script Editor
- getHighestNumberInList(["this", "list", "contains", "only", "text"])
- // Result: undefined

### Finding the Lowest Numeric Value in a List
The handlers inListing 21-37andListing 21-38determines the lowest numeric value in a list of items. The passed list can contain non-numeric data as well as lists within lists.
APPLESCRIPT
Open in Script Editor
- on getLowestNumberInList(theList)
- set theLowestNumber to false
- repeat with a from 1 to count of theList
- set theCurrentItem to item a of theList
- set theClass to class of theCurrentItem
- if theClass is in {integer, real} then
- if theLowestNumber is "" then
- set theLowestNumber to theCurrentItem
- else if theCurrentItem is less than theLowestNumber then
- set theLowestNumber to item a of theList
- end if
- else if theClass is list then
- set theLowValue to getLowestNumberInList(theCurrentItem)
- if theLowValue is less than theLowestNumber then
- set theLowestNumber to theLowValue
- end if
- end if
- end repeat
- return theLowestNumber
- end getLowestNumberInList
JAVASCRIPT
Open in Script Editor
- function getLowestNumberInList(list) {
- var lowestNumber = undefined
- for (var item of list) {
- var number = undefined
- if (item.constructor === Number) {
- number = item
- }
- else if (item.constructor === Array) {
- number = getLowestNumberInList(item)
- }
- if (number != undefined && (lowestNumber === undefined || number < lowestNumber)) {
- lowestNumber = number
- }
- }
- return lowestNumber
- }
Listing 21-39andListing 21-40show how to call the handlers inListing 21-37andListing 21-38for a list containing a mixture of numbers and strings.
APPLESCRIPT
Open in Script Editor
- getLowestNumberInList({-3.25, 23, 2345, "sid", 3, 67})
- --> Result: -3.25
JAVASCRIPT
Open in Script Editor
- getLowestNumberInList([-3.25, 23, 2345, "sid", 3, 67])
- // Result: -3.25
Listing 21-41andListing 21-42show how to call the handlers inListing 21-37andListing 21-38for a list containing a mixture of numbers, strings, booleans, and lists.
APPLESCRIPT
Open in Script Editor
- getLowestNumberInList({-3.25, 23, {-22, 78695, "Sal"}, 2345, true, "sid", 3, 67})
- --> Result: -22
JAVASCRIPT
Open in Script Editor
- getLowestNumberInList([-3.25, 23, [-22, 78695, "bob"], 2345, true, "sid", 3, 67])
- // Result: -22
Listing 21-43andListing 21-44show how to call the handlers inListing 21-37andListing 21-38for a list containing only strings.
APPLESCRIPT
Open in Script Editor
- getLowestNumberInList({"this", "list", "contains", "only", "text"})
- --> Result: false
JAVASCRIPT
Open in Script Editor
- getLowestNumberInList(["this", "list", "contains", "only", "text"])
- // Result: undefined

### Inserting Items into a List
The handlers inListing 21-45andListing 21-46insert an item into a list. Provide the item to insert, the list, and the position where the item should be inserted. Note that position can be specified in relation to the end of the list by using a negative number.
Note
In JavaScript, theArrayclass has built-in methodsâunshift(inserts at the beginning),splice(inserts at a specific position), andpush(inserts at the end)âfor inserting items into a list, requiring less custom scripting than is necessary in AppleScript.
APPLESCRIPT
Open in Script Editor
- on insertItemInList(theItem, theList, thePosition)
- set theListCount to length of theList
- if thePosition is 0 then
- return false
- else if thePosition is less than 0 then
- if (thePosition * -1) is greater than theListCount + 1 then return false
- else
- if thePosition is greater than theListCount + 1 then return false
- end if
- if thePosition is less than 0 then
- if (thePosition * -1) is theListCount + 1 then
- set beginning of theList to theItem
- else
- set theList to reverse of theList
- set thePosition to (thePosition * -1)
- if thePosition is 1 then
- set beginning of theList to theItem
- else if thePosition is (theListCount + 1) then
- set end of theList to theItem
- else
- set theList to (items 1 thru (thePosition - 1) of theList) & theItem & (items thePosition thru -1 of theList)
- end if
- set theList to reverse of theList
- end if
- else
- if thePosition is 1 then
- set beginning of theList to theItem
- else if thePosition is (theListCount + 1) then
- set end of theList to theItem
- else
- set theList to (items 1 thru (thePosition - 1) of theList) & theItem & (items thePosition thru -1 of theList)
- end if
- end if
- return theList
- end insertItemInList
JAVASCRIPT
Open in Script Editor
- function insertItemInArray(item, array, position) {
- var arrayCount = array.length
- if (Math.abs(position) > arrayCount) {
- return false
- }
- else if (position === 0) {
- array.unshift(item)
- }
- else if (position < arrayCount) {
- array.splice(position, 0, item)
- }
- else {
- array.push(item)
- }
- return array
- }
Listing 21-47andListing 21-48show how to call the handlers inListing 21-45andListing 21-46to insert a single item into a list at a specific position.
APPLESCRIPT
Open in Script Editor
- set theList to {"Sal", "Ben", "David", "Chris"}
- insertItemInList("Jen", theList, 3)
- --> Result: {"Sal", "Ben", "Jen", "David", "Chris"}
JAVASCRIPT
Open in Script Editor
- var array = ["Sal", "Ben", "David", "Chris"]
- array = insertItemInArray("Jen", array, 2)
- // Result = ["Sal", "Ben", "Jen", "David", "Chris"]
Listing 21-49andListing 21-50show how to call the handlers inListing 21-45andListing 21-46to insert multiple items into a list at a specific position.
APPLESCRIPT
Open in Script Editor
- set theList to {"Sal", "Ben", "David", "Chris"}
- insertItemInList({"Lizzie", "Maddie", "Lillie"}, theList, 3)
- --> Result: {"Sal", "Ben", "Lizzie", "Maddie", "Lillie", "David", "Chris"}
JAVASCRIPT
Open in Script Editor
- var array = ["Sal", "Ben", "David", "Chris"]
- var items = ["Lizzie", "Maddie", "Lillie"]
- for (var item of items) {
- array = insertItemInArray(item, array, 2)
- }
- // Result = ["Sal", "Ben", "Lillie", "Maddie", "Lizzie", "David", "Chris"]
Listing 21-51andListing 21-52show how to call the handlers inListing 21-45andListing 21-46to insert a list into a list at a specific position.
APPLESCRIPT
Open in Script Editor
- set theList to {"Sal", "Ben", "David", "Chris"}
- insertItemInList({{"Lizzie", "Maddie", "Lillie"}}, theList, 3)
- --> Result: {"Sal", "Ben", {"Lizzie", "Maddie", "Lillie"}, "David", "Chris"}
JAVASCRIPT
Open in Script Editor
- var array = ["Sal", "Ben", "David", "Chris"]
- array = insertItemInArray(["Lizzie", "Maddie", "Lillie"], array, 2)
- // Result = ["Sal", "Ben", ["Lizzie", "Maddie", "Lillie"], "David", "Chris"]
Listing 21-53andListing 21-54show how to call the handlers inListing 21-45andListing 21-46to insert a single item at the end of a list.
APPLESCRIPT
Open in Script Editor
- set theList to {"Sal", "Ben", "David", "Chris"}
- insertItemInList("Jen", theList, -1)
- --> {"Sal", "Ben", "David", "Chris", "Jen"}
JAVASCRIPT
Open in Script Editor
- var array = ["Sal", "Ben", "David", "Chris"]
- array = insertItemInArray("Jen", array, array.length)
- // Result = ["Sal", "Ben", "David", "Chris", "Jen"]
Listing 21-55andListing 21-56show how to call the handlers inListing 21-45andListing 21-46to insert a single item at the second-to-last position in a list.
APPLESCRIPT
Open in Script Editor
- set theList to {"Sal", "Ben", "David", "Chris"}
- insertItemInList("Wanda", theList, -2)
- --> {"Sal", "Sue", "Bob", "Wanda", "Carl"}
JAVASCRIPT
Open in Script Editor
- var array = ["Sal", "Ben", "David", "Chris"]
- array = insertItemInArray("Jen", array, -1)
- // Result = ["Sal", "Ben", "David", "Jen", "Chris"]
Listing 21-57andListing 21-58show how to call the handlers inListing 21-45andListing 21-46to insert a single item at a nonexistent position in a list.
APPLESCRIPT
Open in Script Editor
- set theList to {"Sal", "Ben", "David", "Chris"}
- insertItemInList("Jen", theList, 15)
- --> Result: false
JAVASCRIPT
Open in Script Editor
- var array = ["Sal", "Ben", "David", "Chris"]
- array = insertItemInArray("Jen", array, 14)
- // Result = false

### Replacing Items in a List
You can replace an item in a list using the syntax shown inListing 21-59andListing 21-60if you know the position of the item you want to replace.
APPLESCRIPT
Open in Script Editor
- set theList to {"Sal", "Ben", "David", "Chris"}
- set item 3 of theList to "Wanda"
- return theList
- --> Result: {"Sal", "Sue", "Wanda", "Carl"}
JAVASCRIPT
Open in Script Editor
- var array = ["Sal", "Ben", "David", "Chris"]
- array[2] = "Wanda"
- array
- // Result: ["Sal", "Ben", "Wanda", "Chris"]
The handlers inListing 21-61andListing 21-62can be used to replace an item in a list when you donât know its position. Provide the item you want to replace, the list, the replacement item, and specify whether to replace all instances of the item, or just the first one.
APPLESCRIPT
Open in Script Editor
- on replaceItemInList(theItem, theList, theReplacementItem, replaceAll)
- repeat with a from 1 to the count of theList
- set theCurrentItem to item a of theList
- if theCurrentItem is theItem then
- set item a of theList to theReplacementItem
- if replaceAll is false then return theList
- end if
- end repeat
- return theList
- end replaceItemInList
JAVASCRIPT
Open in Script Editor
- function replaceItemInArray(item, array, replacementItem, replaceAll) {
- var arrayLength = array.length
- for (var i = 0; i < arrayLength; i++) {
- var currentArrayItem = array[i]
- if (currentArrayItem === item) {
- array.splice(i, 1, replacementItem)
- if (!replaceAll) {
- break
- }
- }
- }
- return array
- }
Listing 21-63andListing 21-64show how to call the handlers inListing 21-61andListing 21-62.
APPLESCRIPT
Open in Script Editor
- set theList to {"Sal", "Jen", "Ben", "David", "Chris", "Jen"}
- replaceItemInList("Jen", theList, "Lizzie", true)
- --> {"Sal", "Lizzie", "Ben", "David", "Chris", "Lizzie"}
JAVASCRIPT
Open in Script Editor
- var array = ["Sal", "Jen", "Ben", "David", "Chris", "Jen"]
- replaceItemInArray("Jen", array, "Lizzie", true)
- // Result: ["Sal", "Lizzie", "Ben", "David", "Chris", "Lizzie"]

### Sorting a List
The handler inListing 21-65sorts a list of strings or numbers in AppleScript.
APPLESCRIPT
Open in Script Editor
- on sortList(theList)
- set theIndexList to {}
- set theSortedList to {}
- repeat (length of theList) times
- set theLowItem to ""
- repeat with a from 1 to (length of theList)
- if a is not in theIndexList then
- set theCurrentItem to item a of theList as text
- if theLowItem is "" then
- set theLowItem to theCurrentItem
- set theLowItemIndex to a
- else if theCurrentItem comes before theLowItem then
- set theLowItem to theCurrentItem
- set theLowItemIndex to a
- end if
- end if
- end repeat
- set end of theSortedList to theLowItem
- set end of theIndexList to theLowItemIndex
- end repeat
- return theSortedList
- end sortList
Listing 21-66shows how to call the handler inListing 21-65.
APPLESCRIPT
Open in Script Editor
- set theList to {"Sal", "Ben", "David", "Chris"}
- sortList(theList)
- --> Result: {"Ben", "Chris", "David", "Sal"}
To perform a reverse (descending) sort, use the reverse command, as shown inListing 21-67.
APPLESCRIPT
Open in Script Editor
- set theList to {"Sal", "Ben", "David", "Chris"}
- reverse of sortList(theList)
- --> Result: {"Sal", "David", "Chris", "Ben"}
In JavaScript, theArrayobject has asortmethod, which sorts the arrayâs items. SeeListing 21-68.
JAVASCRIPT
Open in Script Editor
- var array = ["Sal", "Ben", "David", "Chris"]
- array.sort()
- // Result: ["Ben", "Chris", "David", "Sal"]
As in AppleScript, a sorted JavaScript array can be reversed, as shown inListing 21-69.
JAVASCRIPT
Open in Script Editor
- var array = ["Sal", "Ben", "David", "Chris"]
- array.sort()
- array.reverse()
- // Result: ["Sal", "David", "Chris", "Ben"]
Note
When you use AppleScriptObjC or JavaScriptObjC, you can use methods of theNSArrayclass to convert a list of strings into a single string. The handlers inListing 21-70andListing 21-71demonstrate how to do this.
APPLESCRIPT
Open in Script Editor
- on sortList(theList)
- set theArray to arrayWithArray_(theList) of NSArray of current application
- set theSortedList to sortedArrayUsingSelector_("localizedStandardCompare:") of theArray
- return (theSortedList as list)
- end sortList
JAVASCRIPT
Open in Script Editor
- function sortArray(array) {
- array = $(array)
- var sortedArray = array.sortedArrayUsingSelector("localizedStandardCompare:")
- return ObjC.deepUnwrap(sortedArray)
- }
Manipulating Numbers
Displaying Dialogs and Alerts
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13