# Operators Reference

# Operators Reference
This chapter describes AppleScript operators. Anoperatoris a symbol, word, or phrase that derives a value from another value or pair of values. Anoperationis the evaluation of an expression that contains an operator. Anoperandis an expression from which an operator derives a value.
AppleScript provides logical and mathematical operators, as well as operators for containment, concatenation, and obtaining a reference to an object. Operators that operate on two values are calledbinary operators, while operators that operate on a single value are known asunary operators.
The first part of this chapter contains two tables:Table 9-1summarizes all of the operators that AppleScript uses, andTable 9-2shows the order in which AppleScript evaluates operators within expressions. The rest of the chapter shows how AppleScript evaluates representative operators in script expressions.
AppleScript operator
Description
Logical conjunction.
A binary logical operator that combines two Boolean values. The result istrueonly if both operands evaluate totrue.
AppleScript checks the left-hand operand first and, if its isfalse, ignores the right-hand operand. (This behavior is calledshort-circuiting.)
Class of operands:boolean
Class of result:boolean
Logical disjunction.
A binary logical operator that combines two Boolean values. The result istrueif either operand evaluates totrue.
AppleScript checks the left-hand operand first and, if its istrue, ignores the right-hand operand. (This behavior is called short-circuiting.)
Class of operands:boolean
Class of result:boolean
Concatenation.
A binary operator that joins two values. If the left-hand operand is atextobject, the result is atextobject (and only in this case does AppleScript try to coerce the value of the right-hand operand to match that of the left).
If the operand to the left is a record, the result is a record. If the operand to the left belongs to any other class, the result is a list.
For more information, see& (concatenation).
Class of operands: any
Class of result:list,record,text
isÂ equal
equals
[is]Â equalÂ to
Equality.
A binary comparison operator that results intrueif both operands have the same value. The operands can be of any class.
For more information, seeequal, is not equal to.
Class of operands:boolean
Class of result:boolean
âÂ (Option-equalÂ sign on U.S. keyboard)
isÂ not
isn't
isn'tÂ equalÂ [to]
isÂ notÂ equalÂ [to]
doesn'tÂ equal
doesÂ notÂ equal
Inequality.
A binary comparison operator that results intrueif its two operands have different values. The operands can be of any class.
For more information, seeequal, is not equal to.
Class of operands:boolean
Class of result:boolean
[is]Â greaterÂ than
comesÂ after
isÂ notÂ lessÂ thanÂ orÂ equalÂ [to]
isn't less than or equal [to]
Greater than.
A binary comparison operator that results intrueif the value of the left-hand operand is greater than the value of the right-hand operand.
Both operands must evaluate to values of the same class. If they donât, AppleScript attempts to coerce the right-hand operand to the class of the left-hand operand.
For more information, seegreater than, less than.
Class of operands:date,integer,real,text
Class of result:boolean
[is] less than
comes before
is not greater than or equal [to]
isn't greater than or equal [to]
Less than.
A binary comparison operator that results intrueif the value of the left-hand operand is less than the value of the right-hand operand.
Both operands must evaluate to values of the same class. If they donât, AppleScript attempts to coerce the right-hand operand to the class of the operand to the left.
For more information, seegreater than, less than.
Class of operands:date,integer,real,text
Class of result:boolean
â¥(Option-period on U.S. keyboard)
[is] greater than or equal [to]
is not less than
isn't less than
does not come before
doesn't come before
Greater than or equal to.
A binary comparison operator that results intrueif the value of the left-hand operand is greater than or equal to the value of the right-hand operand.
Both operands must evaluate to values of the same class. If they donât, AppleScript attempts to coerce the right-hand operand to the class of the operand to the left.
The method AppleScript uses to determine which value is greater depends on the class of the operands.
Class of operands:date,integer,real,text
Class of result:boolean
â¤(Option-comma on U.S. keyboard)
[is] less than or equal [to]
is not greater than
isn't greater than
does not come after
doesn't come after
Less than or equal to.
A binary comparison operator that results intrueif the value of the left-hand operand is less than or equal to the value of the right-hand operand.
Both operands must evaluate to values of the same class. If they donât, AppleScript attempts to coerce the right-hand operand to the class of the operand to the left.
The method AppleScript uses to determine which value is greater depends on the class of the operands.
Class of operands:date,integer,real,text
Class of result:boolean
start[s] with
begin[s] with
Starts with.
A binary containment operator that results intrueif the list ortextobject to its right matches the beginning of the list ortextobject to its left.
Both operands must evaluate to values of the same class. If they donât, AppleScript attempts to coerce the right-hand operand to the class of the operand to the left.
For more information, seestarts with, ends with.
Class of operands:list,text
Class of result:boolean
end[s] with
Ends with.
A binary containment operator that results intrueif the list ortextobject to its right matches the end of the list ortextobject to its left.
Both operands must evaluate to values of the same class. If they donât, AppleScript attempts to coerce the right-hand operand to the class of the operand to the left.
For more information, seestarts with, ends with.
Class of operands:list,text
Class of result:boolean
contain[s]
Containment.
A binary containment operator that results intrueif the list, record, ortextobject to its right matches any part of the list, record, ortextobject to its left.
Both operands must evaluate to values of the same class. If they donât, AppleScript attempts to coerce the right-hand operand to the class of the operand to the left.
For more information, seecontains, is contained by.
Class of operands:list,record,text
Class of result:boolean
does not contain
doesn't contain
Non-containment.
A binary containment operator that results intrueif the list, record, ortextobject to its right does not match any part of the list, record, ortextobject to its left.
Both operands must evaluate to values of the same class. If they donât, AppleScript attempts to coerce the right-hand operand to the class of the left-hand operand.
For more information, seecontains, is contained by.
Class of operands:list,record,text
Class of result:boolean
is in
is contained by
Containment.
A binary containment operator that results intrueif the list, record, ortextobject to its left matches any part of the list, record, ortextobject to its right.
Both operands must evaluate to values of the same class. If they donât, AppleScript attempts to coerce the left-hand operand to the class of the right-hand operand.
For more information, seecontains, is contained by.
Class of operands:list,record,text
Class of result:boolean
is not in
is not contained by
isn't contained by
Non-containment.
A binary containment operator that results intrueif the list, record, ortextobject to its left does not match any part of the list, record, ortextobject to its right.
Both operands must evaluate to values of the same class. If they donât, AppleScript attempts to coerce the left-hand operand to the class of the right-hand operand.
For more information, seecontains, is contained by.
Class of operands:list,record,text
Class of result:boolean
Multiplication.
A binary arithmetic operator that multiplies the number to its left and the number to its right.
Class of operands:integer,real
Class of result:integer,real
Addition.
A binary arithmetic operator that adds the number or date to its left and the number or date to its right. Only integers can be added to dates. AppleScript interprets such an integer as a number of seconds.
As a unary operator,+has no effect and is removed on compile.
Class of operands:date,integer,real
Class of result:date,integer,real
Subtraction.
A binary or unary arithmetic operator.
The binary operator subtracts the number to its right from the number or date to its left.
The unary operator makes the number to its right negative.
Only integers can be subtracted from dates. AppleScript interprets such an integer as a number of seconds.
Class of operands:date,integer,real
Class of result:date,integer,real
Ã·(Option-slash on U.S. keyboard)
Division.
A binary arithmetic operator that divides the number to its left by the number to its right.
Class of operands:integer,real
Class of result:real
Integral division.
A binary arithmetic operator that divides the number to its left by the number to its right and returns the integral part of the answer as its result.
Class of operands:integer,real
Class of result:integer
Remainder.
A binary arithmetic operator that divides the number to its left by the number to its right and returns the remainder as its result.
Class of operands:integer,real
Class of result:integer,real
Exponentiation.
A binary arithmetic operator that raises the number to its left to the power of the number to its right.
Class of operands:integer,real
Class of result:real
Coercion (orobject conversion).
A binary operator that converts the left-hand operand to the class listed to its right.
Not all values can be coerced to all classes. The coercions that AppleScript can perform are listed inCoercion (Object Conversion). The additional coercions, if any, that an application can perform is listed in its dictionary.
Class of operands: The right-hand operand must be a class identifier or list of class identifiers; the left-hand operand must be a value that can be converted to that class or one of the listed classes.
Class of result: The class specified by the class identifier to the right of the operator
Negation.
A unary logical operator that results intrueif the operand to its right isfalse, andfalseif the operand istrue.
Class of operand:boolean
Class of result:boolean
[a] (ref [to] | reference to)
A reference to.
A unary operator that causes AppleScript to return areferenceobject that specifies the location of the operand to its right. A reference is evaluated at run time, not at compile time.
Seea reference tofor more information.
Class of operand: any class type
Class of result:reference
When evaluating expressions, AppleScript uses operator precedence to determine which operations are evaluated first. In the following expression, for example, AppleScript does not simply perform operations from left to rightâit performs the multiplication operation2 * 5first, because multiplication has higher precedence than addition.
```
12 + 2 * 5 --result: 22```
Table 9-2shows the order in which AppleScript performs operations. The column labeled âAssociativityâ indicates the order in the case where there are two or more operands of the same precedence in an expression. The word âNoneâ in the Associativity column indicates that you cannot have multiple consecutive occurrences of the operation in an expression. For example, the expression3 = 3 = 3is not legal because the associativity for the equal operator is ânone.â
To evaluate expressions with multiple unary operators of the same order, AppleScript applies the operator closest to the operand first, then applies the next closest operator, and so on. For example, the expressionnot not not trueis evaluated asnot (not (not true)).
You can enforce the order in which AppleScript performs operations by grouping expressions in parentheses, which are evaluated first, starting with the innermost pair of parentheses.
Order
Operators
Associativity
Type of operator
Innermost to outermost
Grouping
Unary
Plus or minus sign for numbers
Right to left
Exponentiation
(note that this is different from standard math, in which exponentiation takes precedence over unary plus or minus)
Left to right
Multiplication and division
Left to right
Addition and subtraction
Left to right
Concatenation
Left to right
Coercion
None
Comparison
None
Equality and inequality
Unary
Logical negation
Left to right
Logical and
Left to right
Logical or
The following sections provide additional detail about how AppleScript evaluates operators in expressions:
- & (concatenation)
& (concatenation)
- a reference to
a reference to
- Para
Para
- contains, is contained by
contains, is contained by
- equal, is not equal to
equal, is not equal to
- greater than, less than
greater than, less than
- starts with, ends with
starts with, ends with
The concatenation operator (&) concatenatestextobjects, joinsrecordobjects into a record, and joins other objects into a list.
Table 9-1summarizes the use of use of this operator.

##### text
The concatenation of twotextobjects joins the characters from the left-handtextobject to the characters from the right-handtextobject, without intervening spaces. For example,"dump" & "truck"evaluates to thetextobject"dumptruck".
If the left-hand operand is atextobject, but the right-hand operand is not, AppleScript attempts to coerce the right-hand operand to atextobject. For example, when AppleScript evaluates the expression"Route " & 66it coerces the integer66to thetextobject"66", and the result is thetextobject"Route 66".
However, you get a different result if you reverse the order of the operands:
```
66 & "Route " --result: {66, "Route "} (a list)```
In the following example, the left-hand operand is atextobject and the right-hand operand is a list, so concatenation results in atextobject:
```
item 1 of {"This"} & {"and", "that"} -- "Thisandthat"```

##### record
The concatenation of two records joins the properties of the left-hand record to the properties of the right-hand record. If both records contain properties with the same name, the value of the property from the left-hand record appears in the result. For example, the result of the expression
```
{ name:"Matt", mileage:"8000" } & { name:"Steve", framesize:58 }```
```
{ name:"Matt", mileage:"8000", frameSize:58 }```

##### All Other Classes
Except for the cases described above fortextobjects andrecordobjects, the concatenation operator (&) joins lists. A non-list operand is considered to be a list containing that operand. The following example shows concatenation of two integers, a list and a text string, and a list and a record, respectively:
```
1 & 2 --result: {1, 2}```
```
{"this"} & "hello" --result: {"this", "hello"}```
```
{"this"} & {a:1, b:2} --result: {"this", 1, 2}```
If both the operands to be concatenated are lists, then the result is a list containing all the items in the left-hand list, followed by all the items in the right-hand list. For example:
```
{"This"} & {"and", "that"} --result: {"This", "and", "that"}```
```
{"This"} & item 1 of {"and", "that"} --result: {"This", "and"}```
To join two lists and create a list of lists, rather than a single list, you can enclose each list in two sets of brackets:
```
{{1, 2}} & {{3, 4}} --result: {{1, 2}, {3, 4}}```
For information on working efficiently with large lists, seelist.
Thea reference tooperator is a unary operator that returns areferenceobject. You can abbreviate this operator toa ref to, orref to, or even justref.
For related information, see thereferenceclass andObject Specifiers.

##### Examples
The following statement creates areferenceobject that contains an object specifier to the Finder startup disk:
```
tell app "Finder" to set diskRef to a ref to startup disk```
```
--result: startup disk of application "Finder"```
The following shows how to obtain a reference object that refers to an item in a list:
```
set itemRef to a reference to item 3 of {1, "hello", 755, 99}```
```
    --result: item 3 of {1, "hello", 755, 99}```
```
set newTotal to itemRef + 45 --result: 800```
In the final line, AppleScript automatically resolves the object specifier contained in the referenceitemRefand obtains its value to use in the addition operation. To cause AppleScript to explicitly resolve areferenceobject, you can use itscontentsproperty:
```
contents of itemRef --result: 755```
The next examples demonstrate how using a reference object can result in a different outcome than accessing an object directly. The first example obtains a current track object from iTunes, gets the name, changes the track, then gets the name again:
```
tell application "iTunes"```
```
    set curTrack to current track```
```
    --result: file track id 2703 of user playlist id 2425```
```
    --        of source id 46 of application "iTunes"```
```
    display dialog (name of curTrack as string)  -- "Shattered"```
```
    next track -- play next song```
```
    display dialog (name of curTrack as string) -- "Shattered"```
```
end tell```
BecausecurTrackis a specifictrackobject, its name doesnât change when the current track changes. But observe the result when using a reference to the current track:
```
tell application "iTunes"```
```
    set trackRef to a reference to current track```
```
    --result: current track of application "iTunes"```
```
    display dialog (name of trackRef as string) -- "Shattered"```
```
    next track -- play next song```
```
    display dialog (name of trackRef as string) -- "Strange Days"```
```
end tell```
BecausetrackRefis areferenceobject containing an object specifier, the specifier identifies the new track when the current track changes.
Theasoperator converts, orcoerces, a value of one class to a value of another class. Not all values are coercible to all classes; seeCoercion (Object Conversion)for a list of allowed coercions.
The right-hand operand ofasmay be a single class, such astext, or a list of classes, such as{integer, text}.When given a list, theasoperator processes the list from the first type to the last, checking if the value is an instance of that type; if one matches, the result is the original value. If none match, then it again processes the list from the first type to the last, attempting to coerce the value to that type; the result is the result of the first successful coercion. If none succeed, it throws an error.
Note:Coercing to a list of classes is supported in OS X Yosemite v10.10 and later.

##### Examples
This expression returnsxas a number, suitable for use with a math operator. For example, ifxwas the text"1.5", it would return therealvalue1.5.
```
x as number```
This expression returnsxas either an integer or text, whichever succeeds first. For example, consider ifxwasdate "Wednesday, May 27, 2015 at 12:03:15 PM":dateobjects cannot be coerced to integers, but they can be coerced to text, so the result is the date as text:"Wednesday, May 27, 2015 at 12:03:15 PM".
```
x as {integer, text}```
The way lists of classes are processed means that the result ofascan depend on the order of the classes. For example, the result of1.5 as {integer, text}is2, but1.5 as {text, integer}is"1.5". It is also possible to have types that will never be reached. For example, in the expressionx as {number, integer}, theintegercoercion will never trigger, becausenumberwill always succeed first.
Thecontainsandis contained byoperators work with lists, records, andtextobjects.
Table 9-1summarizes the use of these operators and their synonyms.

##### list
A listcontainsanother list if the right-hand list is a sublist of the left-hand list. A sublist is a list whose items appear in the same order and have the same values as any series of items in the other list. For example, the following statement istruebecause1 + 1evaluates to2, so that all the items in the right-hand list appear, in the same order, in the left-hand list:
```
{ "this", "is", 1 + 1, "cool" } contains { "is", 2 }```
The following statement isfalsebecause the items in the right-hand list are not in the same order as the matching items in the left-hand list:
```
{ "this", "is", 2, "cool" } contains { 2, "is" }```
A listis contained byanother list if the left-hand list is a sublist of the right-hand list. For example, the following expression istrue:
```
{ "is", 2} is contained by { "this", "is", 2, "cool" }```
Bothcontainsandis contained bywork if the sublist is a single valueâas with the concatenation operator (&), single values are coerced to one-item lists. For example, both of the following expressions evaluate totrue:
```
{ "this", "is", 2, "cool" } contains 2```
```
2 is contained by { "this", "is", 2, "cool" }```
However, the following expressions, containing nested lists, both evaluate to false:
```
{"this", "is", {2}, "cool"} contains 2 -- false```
```
{"this", "is", {2}, "cool"} contains {2} -- false```

##### record
A record contains another record if all the properties in the right-hand record are included in the left-hand record, and the values of properties in the right-hand record are equal to the values of the corresponding properties in the left-hand record. A record is contained by another record if all the properties in the left-hand record are included in the right-hand record, and the values of the properties in the left-hand record are equal to the values of the corresponding properties in the right-hand record. The order in which the properties appear does not matter. For example, the following istrue:
```
{ name:"Matt", mileage:"8000", description:"fast"} Â¬```
```
    contains { description:"fast", name:"Matt" }```

##### text
Atextobject contains anothertextobject if the characters in the right-handtextobject are equal to any contiguous series of characters in the left-handtextobject. For example,
```
"operand" contains "era"```
istrue, but
```
"operand" contains "dna"```
isfalse.
Atextobject is contained by anothertextobject if the characters in the left-handtextobject are equal to any series of characters in the right-handtextobject. For example, this statement istrue:
```
"era" is contained by "operand"```
Text comparisons can be affected byconsideringandignoringstatements, as described in the Text section ofequal, is not equal to.
Theequalandis not equal tooperators can handle operands of any class. Two expressions of different classes are generally not equal, although for scalar operands, such as booleans, integers, and reals, two operands are the same if they have the same value.
Table 9-1summarizes the use of these operators and their synonyms.

##### list
Two lists are equal if they both contain the same number of items and if the value of an item in one list is identical to the value of the item at the corresponding position in the other list:
```
{ 7, 23, "Hello" } = {7, 23, "Goodbye"} --result: false```

##### record
Two records are equal if they both contain the same collection of properties and if the values of properties with the same label are equal. They are not equal if the records contain different collections of properties, or if the values of properties with the same label are not equal. The order in which properties are listed does not affect equality. For example, the following expression istrue:
```
{ name:"Matt", mileage:"8000" } = { mileage:"8000", name:"Matt"}```

##### text
Twotextobjects are equal if they are both the same series of characters. They are not equal if they are different series of characters. For related information, see thetextclass.
Text comparisons can be affected byconsideringandignoringstatements, which instruct AppleScript to selectively consider or ignore attributes of characters or types of characters. For example, unless you use anignoringstatement, AppleScript comparestextobjects by considering all characters and punctuation.
AppleScript does not distinguish uppercase from lowercase letters unless you use aconsideringstatement to consider thecaseattribute. For example:
```
"DUMPtruck" is equal to "dumptruck" --result: true```
```
considering case```
```
    "DUMPtruck" is equal to "dumptruck" --result: false```
```
end considering```
When comparing twotextobjects, if the test is not enclosed in aconsideringorignoringstatement, then the comparison uses default values for considering and ignoring attributes (described inconsidering / ignoring (text comparison)).
Thegreater thanandless thanoperators work with dates, integers, real numbers, andtextobjects.
Table 9-1summarizes the use of these operators and their synonyms.

##### date
A date is greater than another date if it represents a later time. A date is less than another date if it represents an earlier time.

##### integer, real
An integer or a real number is greater than another integer or real number if it represents a larger number. It is less than another integer or real number if it represents a smaller number.

##### text
To determine the ordering of twotextobjects, AppleScript uses the collation order set in the Language pane of International preferences. Atextobject is greater than (comes after) anothertextobject based on the lexicographic ordering of the userâs language preference. With the preference set to English, the following two statements both evaluate totrue:
```
"zebra" comes after "aardvark"```
```
"zebra" > "aardvark"```
The following two statements also evaluate totrue:
```
"aardvark" comes before "zebra"```
```
"aardvark" < "zebra"```
Text comparisons can be affected byconsideringandignoringstatements, as described in the Text section ofequal, is not equal to.
Thestarts withandends withoperators work with lists andtextobjects.
Table 9-1summarizes the use of these operators and their synonyms.

##### list
A liststarts withthe items in a second list if all the items in the second list are found at the beginning of the first list. A listends withthe items in a second list if all the items in the second list are found at the end of the first list. For example, the following three expressions are alltrue:
```
{ "this", "is", 2, "cool" } ends with "cool"```
```
{ "this", "is", 2, "cool" } starts with "this"```
```
{ "this", "is", 2, "cool" } starts with { "this", "is" }```

##### text
Atextobjectstarts withthe text in a secondtextobject if all the characters in the second object are found at the beginning of the first object. Atextobjectends withthe text in a secondtextobject if all the characters in the second object are found at the end of the first object. For example, the following expression istrue:
```
"operand" starts with "opera"```
Atextobject ends with anothertextobject if the characters in the right-handtextobject are the same as the characters at the end of the left-handtextobject. For example, the following expression istrue:
```
"operand" ends with "and"```
Text comparisons can be affected byconsideringandignoringstatements, as described in the Text section ofequal, is not equal to.
Copyright © 2016 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2016-01-25