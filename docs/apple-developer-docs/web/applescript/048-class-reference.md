# Class Reference

Aclassis a category for objects that share characteristics. AppleScript defines classes for common objects used in AppleScript scripts, such as aliases, Boolean values, integers, text, and so on.
Each object in a script is an instance of a specific class and has the same properties (including theclassproperty), can contain the same kinds of elements, and supports the same kinds of operations and coercions as other objects of that type. Objects that are instances of AppleScript types can be used anywhere in a scriptâthey donât need to be within atellblock that specifies an application.
Scriptable applications also define their own classes, such as windows and documents, which commonly contain properties and elements based on many of the basic AppleScript classes described in this chapter. Scripts obtain these objects in the context of the applications that define them. For more information on the class types applications typically support, see âStandard Classesâ in Technical Note TN2106,Scripting Interface Guidelines.
A persistent reference to an existing file, folder, or volume in the file system.
For related information, seefile,POSIX file, andAliases and Files.

##### Properties of alias objects

##### Coercions Supported

AppleScript supports coercion of analiasobject to atextobject or single-itemlist.

##### Examples

```

set zApp to choose application as alias -- (then choose Finder.app)```

```

--result: alias "Leopard:System:Library:CoreServices:Finder.app:"```

```

class of zApp --result: alias```

```

zApp as text --result: "Leopard:System:Library:CoreServices:Finder.app:"```

```

zApp as list --result: {alias "Leopard:System:Library:CoreServices:Finder.app:"}```
You can use thePOSIX pathproperty to obtain a POSIX-style path to the item referred to by an alias:

```

POSIX path of zApp --result: "/System/Library/CoreServices/Finder.app/"```

##### Discussion

You can only create an alias to a file or folder that already exists.

##### Special Considerations

AppleScript 2.0 attempts to resolve aliases only when you run a script. However, in earlier versions, AppleScript attempts to resolve aliases at compile time.
An application on a local machine or an available server.
An application object in a script has all of the properties described here, which are handled by AppleScript. It may have additional properties, depending on the specific application it refers to.

##### Properties of application objects

##### Coercions Supported

AppleScript supports coercion of anapplicationobject to a single-itemlist.

##### Examples

You can determine whether an application on the current computer is running without launching it (this wonât work if your target is on a remote computer):

```

tell application "iTunes" -- doesn't automatically launch app```

```

    if it is running then```

```

        pause```

```

    end if```

```

end tell```
You can also use this format:

```

if application "iTunes" is running```

```

    tell application "iTunes" to pause```

```

end if```
The following statements specify the TextEdit application by, respectively, its signature, its bundle id, and by a POSIX path to a specific version of TextEdit:

```

application id "ttxt"```

```

application id "com.apple.TextEdit"```

```

application "/Applications/TextEdit.app"```
You can target a remote application with atellstatement. For details, seeRemote Applications.

##### Special Considerations

Starting in OS X v10.5, there are several changes in application behavior:

- Applications launch hidden.AppleScript has always launched applications if it needed to in order to send them a command. However, they would always launch visibly, which could be visually disruptive. AppleScript now launches applications hidden by default. They will not be visible unless the script explicitly says otherwise usingactivate.
Applications launch hidden.
AppleScript has always launched applications if it needed to in order to send them a command. However, they would always launch visibly, which could be visually disruptive. AppleScript now launches applications hidden by default. They will not be visible unless the script explicitly says otherwise usingactivate.

- Applications are located lazily.When running a script, AppleScript will not attempt to locate an application until it needs to in order to send it a command. This means that a compiled script or script application may contain references to applications that do not exist on the userâs system, but AppleScript will not ask where the missing applications are until it encounters a relevanttellblock. Previous versions of AppleScript would attempt to locate every referenced application before running the script.When opening a script for editing, AppleScript will attempt to locate all the referenced applications in the entire script, which may mean asking where one is. Pressing the Cancel button only cancels the search for that application; the script will continue opening normally, though custom terminology for that application will display as raw codes. In older versions, pressing Cancel would cancel opening the script.
Applications are located lazily.
When running a script, AppleScript will not attempt to locate an application until it needs to in order to send it a command. This means that a compiled script or script application may contain references to applications that do not exist on the userâs system, but AppleScript will not ask where the missing applications are until it encounters a relevanttellblock. Previous versions of AppleScript would attempt to locate every referenced application before running the script.
When opening a script for editing, AppleScript will attempt to locate all the referenced applications in the entire script, which may mean asking where one is. Pressing the Cancel button only cancels the search for that application; the script will continue opening normally, though custom terminology for that application will display as raw codes. In older versions, pressing Cancel would cancel opening the script.

- Applications are located and re-located dynamically.Object specifiers that refer to applications, including those intellblocks, are evaluated every time a script runs. This alleviates problems with scripts getting âstuckâ to a particular copy of an application.
Applications are located and re-located dynamically.
Object specifiers that refer to applications, including those intellblocks, are evaluated every time a script runs. This alleviates problems with scripts getting âstuckâ to a particular copy of an application.
In prior versions of AppleScript, use of the new built-in application properties will fall back to sending an event to the application, but the application may not handle these properties in the same way, or handle them at all. (Most applications will handlename,version, andfrontmost;idandrunningare uncommon.) The other new features described above require AppleScript 2.0.
A logical truth value.
Abooleanobject evaluates to one of the AppleScript constantstrueorfalse. ABoolean expressioncontains one or morebooleanobjects and evaluates totrueorfalse.

##### Properties of boolean objects

##### Operators

The operators that takebooleanobjects as operands areand,or,not,&,=, andâ, as well as their text equivalents:is equal to,is not equal to,equals, and so on.
The=operator returnstrueif both operands evaluate to the same value (eithertrueorfalse); theâoperator returnstrueif the operands evaluate to different values.
The binary operatorsandandortakebooleanobjects as operands and return Boolean values. Anandoperation, such as(2 > 1) and (4 > 3), has the valuetrueif both its operands aretrue, andfalseotherwise. Anoroperation, such as(theString = "Yes") or (today = "Tuesday"), has the valuetrueif either of its operands istrue.
The unarynotoperator changes atruevalue tofalseor afalsevalue totrue.
The concatenation operator (&) creates a list containing the two boolean values on either side of it; for example:

```

true & false --result: {true, false}```
For additional information on these operators, seeOperators Reference.

##### Coercions Supported

AppleScript supports coercion of abooleanobject to a single-itemlist, atextobject, or aninteger.

##### Examples

The following are simple Boolean expressions:

```

true```

```

false```

```

paragraphCount > 2```
AppleScript supplies the Boolean constantstrueandfalseto serve as the result of evaluating a Boolean operation. But scripts rarely need to use these literals explicitly because a Boolean expression itself evaluates to a Boolean value. For example, consider the following two script snippets:

```

if companyName is equal to "Acme Baking" then```

```

    return true```

```

else```

```

    return false```

```

end if```

```

 ```

```

return companyName is equal to "Acme Baking"```
The second, simpler version, just returns the value of the Boolean comparisoncompanyName is equal to "Acme Baking", so it doesnât need to use a Boolean constant.

##### Discussion

When you pass a Boolean value as a parameter to a command, the form may change when you compile the command. For example, the following line

```

choose folder showing package contents true```
is converted to this when compiled by AppleScript:

```

choose folder with showing package contents```
It is standard for AppleScript to compile parameter expressions from the Boolean form (such asshowing package contents trueorinvisibles false) into thewithform (with showing package contentsorwithout invisibles, respectively).
Specifies the class of an object or value.
All classes have aclassproperty that specifies the class type. The value of theclassproperty is an identifier.

##### Properties of class objects

##### Operators

The operators that take class identifier values as operands are&,=,â, andas.
The coercion operatorastakes an object of one class type and coerces it to an object of a type specified by a class identifier. For example, the following statement coerces atextobject into a correspondingreal:

```

"1.5" as real --result: 1.5```

##### Coercions Supported

AppleScript supports coercion of a class identifier to a single-itemlistor atextobject.

##### Examples

Asking for the class of a type such asintegerresults in a value ofclass:

```

class of text --result: class```

```

class of integer --result: class```
Here is the class of a boolean literal:

```

class of true --result: boolean```
And here are some additional examples:

```

class of "Some text" --result: text```

```

class of {1, 2, "hello"} --result: list```
A word with a predefined value.
Constants are generally used for enumerated types. You cannot define constants in scripts; constants can be defined only by applications and by AppleScript. SeeGlobal Constants in AppleScriptfor more information.

##### Properties of constant objects

##### Operators

The operators that takeconstantobjects as operands are&,=,â, andas.

##### Coercions Supported

AppleScript supports coercion of aconstantobject to a single-itemlistor atextobject.

##### Examples

One place you use constants defined by AppleScript is in text comparisons performed withconsideringorignoringstatements (described inconsidering / ignoring (text comparison)). For example, in the following script statements,punctuation,hyphens, andwhite spaceare constants:

```

considering punctuation but ignoring hyphens and white space```

```

    "bet-the farm," = "BetTheFarm," --result: true```

```

end considering```

```

class of hyphens --result: constant```
The final statement shows that the class ofhyphensisconstant.

##### Discussion

Constants are not text strings, and they must not be surrounded by quotation marks.
Literal constants are defined inLiterals and Constants.
In addition to the constants defined by AppleScript, applications often define enumerated types to be used for command parameters or property values. For example, the iTunessearchcommand defines these constants for specifying the search area:

```

albums```

```

all```

```

artists```

```

composers```

```

displayed```

```

songs```
Specifies the day of the week, the date (month, day of the month, and year), and the time (hours, minutes, and seconds).
To get the current date, use the commandcurrent date:

```

set theDate to current date```

```

--result: "Friday, November 9, 2007 11:35:50 AM"```
You can get and set the different parts of adateobject through the date and time properties described below.
When you compile a script, AppleScript displays date and time values according to the format specified in System Preferences.

##### Properties of date objects

##### Operators

The operators that takedateobject as operands are&,+,â,=,â,>,â¥,<,â¤,comes before,comes after, andas. In expressions containing>,â¥,<,â¤,comes before, orcomes after, a later time is greater than an earlier time.
AppleScript supports the following operations ondateobjects with the+andâoperators:

```

date + timeDifference```

```

--result: date```

```

date - date```

```

--result: timeDifference```

```

date - timeDifference```

```

--result: date```
wheretimeDifferenceis anintegervalue specifying a time difference in seconds. To simplify the notation of time differences, you can also use one or more of these of these constants:

```

minutes```

```

    60```

```

hours```

```

    60 * minutes```

```

days```

```

    24 * hours```

```

weeks```

```

    7 * days```
Hereâs an example:

```

date "Friday, November 9, 2007" + 4 * days + 3 * hours + 2 *  minutes```

```

--result: date "Tuesday, November 13, 2007 3:02:00 AM"```
To express a time difference in more convenient form, divide the number of seconds by the appropriate constant:

```

31449600 / weeks --result: 52.0```
To get an integral number of hours, days, and so on, use thedivoperator:

```

151200 div days --result: 1```
To get the difference, in seconds, between the current time and Greenwich mean time, use thetime to GMTcommand.

##### Coercions Supported

AppleScript supports coercion of adateobject to a single-itemlistor atextobject.

##### Examples

The following expressions show some options for specifying a date, along with the results of compiling the statements. If you construct a date using only partial information, AppleScript fills in the missing pieces with default values. The actual format is based on the settings in System Preferences.

```

date "8/9/2007, 17:06"```

```

     --result: date "Thursday, August 9, 2007 5:06:00 PM"```

```

date "7/16/70"```

```

     --result: date "Wednesday, July 16, 2070 12:00:00 AM"```

```

date "12:06" -- specifies a time on the current date```

```

     --result: date "Friday, November 9, 2007 12:06:00 PM"```

```

date "Sunday, December 12, 1954 12:06 pm"```

```

     --result: date "Sunday, December 12, 1954 12:06:00 PM"```
The following statements access various date properties (results depend on the date the statements are executed):

```

set theDate to current date --using current date command```

```

--result: date "Friday, November 9, 2007 11:58:38 AM"```

```

weekday of theDate --result: Friday```

```

day of theDate --result: 9```

```

month of theDate --result: November```

```

year of theDate --result: 2007```

```

time of theDate --result: 43118 (seconds since 12:00:00 AM)```

```

time string of theDate --result: "11:58:38 AM"```

```

date string of theDate --result: "Friday, November 9, 2007"```
If you want to specify a time relative to a date, you can do so by usingof,relative to, orin, as shown in the following examples.

```

date "2:30 am" of date "Jan 1, 2008"```

```

    --result: date "Tuesday, January 1, 2008 2:30:00 AM"```

```

date "2:30 am" of date "Sun Jan 27, 2008"```

```

    --result: date "Sunday, January 27, 2008 2:30:00 AM"```

```

date "Nov 19, 2007" relative to date "3PM"```

```

    --result: date "Monday, November 19, 2007 3:00:00 PM"```

```

date "1:30 pm" in date "April 1, 2008"```

```

    --result: date "Tuesday, April 1, 2008 1:30:00 PM"```

##### Special Considerations

You can create adateobject using a string that follows the date format specified in the Formats pane in International preferences. For example, in US English:

```

set myDate to date "3/4/2008"```
When you compile this statement, it is converted to the following:

```

set myDate to date "Tuesday, March 4, 2008 12:00:00 AM"```
A reference to a file, folder, or volume in the file system. Afileobject has exactly the same attributes as analiasobject, with the addition that it can refer to an item that does not exist.
For related information, seealiasandPOSIX file. For a description of the format for a file path, seeAliases and Files.

##### Coercions Supported

AppleScript supports coercion of afileobject to atextobject or single-itemlist.

##### Examples

```

set fp to open for access file "Leopard:Users:myUser:NewFile"```

```

close access fp```

##### Discussion

You can create afileobject that refers to a file or folder that does not exist. For example, you can use thechoose file namecommand to obtain afileobject for a file that need not currently exist.
A number without a fractional part.

##### Properties of integer objects

##### Operators

The operators that can haveintegervalues as operands are+,-,*,Ã·(or/),div,mod,^,=,â,>,â¥,<, andâ¤.
Thedivoperator always returns anintegervalue as its result. The+,â,*,mod, and^operators return values of typeintegerorreal.

##### Coercions Supported

AppleScript supports coercion of anintegervalue to a single-itemlist, arealnumber, or atextobject.
Coercion of anintegerto anumberdoes nothing:

```

set myCount to 7 as number```

```

class of myCount --result: integer```

##### Examples

```

1```

```

set myResult to 3 - 2```

```

-1```

```

1000```

##### Discussion

The biggest value (positive or negative) that can be expressed as an integer in AppleScript is Â±536870911, which is equal to Â±(2^29 â 1). Larger integers are converted to real numbers, expressed in exponential notation, when scripts are compiled.
Note:The smallest possibleintegervalue is actually -536870912 (-2^29), but it can only be generated as a result of an expression. If you enter it directly into a script, it will be converted to a real when you compile.
An ordered collection of values. The values contained in a list are known as items. Each item can belong to any class.
A list appears in a script as a series of expressions contained within braces and separated by commas. An empty list is a list containing no items. It is represented by a pair of empty braces:{}.

##### Properties of list objects

##### Elements of list objects

A value contained in the list. Each value contained in a list is an item and an item may itself be another list. You can refer to values by their item numbers. For example,item 2 of {"soup", 2, "nuts"}is the integer2.
You can also refer to indexed list items by class. For example,integer 1 of {"oatmeal", 42, "new"}returns42.

##### Operators

The operators that can have list values as operands are&,=,â,starts with,ends with,contains, andis contained by.
For detailed explanations and examples of how AppleScript operators treat lists, seeOperators Reference.

##### Commands Handled

You can count the items in a list or the elements of a specific class in a list with thecountcommand. You can also use thelengthproperty of a list:

```

count {"a", "b", "c", 1, 2, 3} --result: 6```

```

length of {"a", "b", "c", 1, 2, 3} --result: 6```

##### Coercions Supported

AppleScript supports coercion of a single-item list to any class to which the item can be coerced if it is not part of a list.
AppleScript also supports coercion of an entire list to atextobject if each of the items in the list can be coerced to atextobject, as in the following example:

```

{5, "George", 11.43, "Bill"} as text --result: "5George11.43Bill"```
The resultingtextobject concatenates all the items, separated by the current value of the AppleScript propertytext item delimiters. This property defaults to an empty string, so the items are simply concatenated. For more information, seetext item delimiters.
Individual items in a list can be of any class, and AppleScript supports coercion of any value to a list that contains a single item.

##### Examples

The following statement defines a list that contains atextobject, an integer, and a Boolean value:

```

{ "it's", 2, true }```
Each list item can be any valid expression. The following list has the same value as the previous list:

```

{ "it" & "'s", 1 + 1, 4 > 3 }```
The following statements work with lists; note that the concatenation operator (&) joins two lists into a single list:

```

class of {"this", "is", "a", "list"} --result: list```

```

item 3 of {"this", "is", "a", "list"} --result: "a"```

```

items 2 thru 3 of {"soup", 2, "nuts"} --result: {2, "nuts"}```

```

{"This"} & {"is", "a", "list"} --result: {"This", "is", "a", "list"}```
For large lists, it is more efficient to use thea reference to operatorwhen inserting a large number of items into a list, rather than to access the list directly. For example, using direct access, the following script takes about 10 seconds to create a list of 10,000 integers (results will vary depending on the computer and other factors):

```

set bigList to {}```

```

set numItems to 10000```

```

set t to (time of (current date)) --Start timing operations```

```

repeat with n from 1 to numItems```

```

    copy n to the end of bigList```

```

    -- DON'T DO THE FOLLOWING--it's even slower!```

```

    -- set bigList to bigList & n```

```

end```

```

set total to (time of (current date)) - t --End timing```
But the following script, which uses thea reference to operator, creates a list of 100,000 integers (ten times the size) in just a couple of seconds (again, results may vary):

```

set bigList to {}```

```

set bigListRef to a reference to bigList```

```

set numItems to 100000```

```

set t to (time of (current date)) --Start timing operations```

```

repeat with n from 1 to numItems```

```

    copy n to the end of bigListRef```

```

end```

```

set total to (time of (current date)) - t --End timing```
Similarly, accessing the items in the previously created list is much faster usinga reference toâthe following takes just a few seconds:

```

set t to (time of (current date)) --Start timing```

```

repeat with n from 1 to numItems -- where numItems = 100,000```

```

    item n of bigListRef```

```

end repeat```

```

set total to (time of (current date)) - t --End timing```
However, accessing the list directly, even for only 4,000 items, can take over a minute:

```

set numItems to 4000```

```

set t to (time of (current date)) --Start timing```

```

repeat with n from 1 to numItems```

```

    item n of bigList```

```

end repeat```

```

set total to (time of (current date)) - t --End timing```
An abstract class that can represent anintegeror areal.
There is never an object whose class isnumber; the actual class of a "number" object is always one of the more specific types,integerorreal.

##### Properties of number objects

##### Operators

Because values identified as values of classnumberare really values of either classintegeror classreal, the operators available are the operators described in the definitions of theintegerorrealclasses.

##### Coercions Supported

Coercing an object tonumberresults in anintegerobject if the result of the coercion is aninteger, or arealobject if the result is a non-integer number.

##### Examples

Any valid literal expression for anintegeror arealvalue is also a valid literal expression for anumbervalue:

```

1```

```

2```

```

-1```

```

1000```

```

10.2579432```

```

1.0```

```

1.```
A pseudo-class equivalent to thefileclass.
There is never an object whose class isPOSIX file; the result of evaluating a POSIX file specifier is afileobject. The difference betweenfileandPOSIX fileobjects is in how they interpret name specifiers: aPOSIX fileobject interprets"name"as a POSIX path, while afileobject interprets it as an HFS path.
For related information, seealiasandfile. For a description of the format for a POSIX path, seeAliases and Files.

##### Properties of POSIX file objects

Seefile.

##### Coercions Supported

Seefile.

##### Examples

The following example asks the user to specify a file name, starting in the temporary directory/tmp, which is difficult to specify using a file specifier:

```

set fileName to choose file name default location (POSIX file "/tmp")```

```

    -result: dialog starts in /tmp folder```
Numbers that can include a fractional part, such as 3.14159 and 1.0.

##### Properties of real objects

##### Operators

The operators that can haverealvalues as operands are+,-,*,Ã·(or/),div,mod,^,=,â,>,â¥,<, andâ¤.
TheÃ·and/operators always returnrealvalues as their results. The+,-,*,mod, and^operators returnrealvalues if either of their operands is arealvalue.

##### Coercions Supported

AppleScript supports coercion of arealvalue to anintegervalue, rounding any fractional part.
AppleScript also supports coercion of arealvalue to a single-itemlistor atextobject. Coercion to text uses the decimal separator specified in Numbers in the Formats pane in International preferences.

##### Examples

```

10.2579432```

```

1.0```

```

1.```
As shown in the third example, a decimal point indicates a real number, even if there is no fractional part.
Real numbers can also be written using exponential notation. A lettereis preceded by a real number (without intervening spaces) and followed by an integer exponent (also without intervening spaces). The exponent can be either positive or negative. To obtain the value, therealnumber is multiplied by 10 to the power indicated by the exponent, as in these examples:

```

1.0e5 --equivalent to 1.0 * 10^5, or 100000```

```

1.0e+5 --same as 1.0e5```

```

1.0e-5 --equivalent to 1.0 * 10^-5, or .00001```

##### Discussion

Real numbers that are greater than or equal to 10,000.0 or less than or equal to 0.0001 are converted to exponential notation when scripts are compiled. The largest value that can be evaluated (positive or negative) is 1.797693e+308.
An unordered collection of labeled properties. The only AppleScript classes that support user-defined properties arerecordandscript.
A record appears in a script as a series of property definitions contained within braces and separated by commas. Each property definition consists of a label, a colon, and the value of the property. For example, this is a record with two properties:{product:"pen", price:2.34}.
Each property in a record has a unique label which distinguishes it from other properties in the collection. The values assigned to properties can belong to any class. You can change the class of a property simply by assigning a value belonging to another class.

##### Properties of record objects

##### Operators

The operators that can have records as operands are&,=,â,contains, andis contained by.
For detailed explanations and examples of how AppleScript operators treat records, seeOperators Reference.

##### Commands Handled

You can count the properties in a record with thecountcommand:

```

count {name:"Robin", mileage:400} --result: 2```

##### Coercions Supported

AppleScript supports coercion of records to lists; however, all labels are lost in the coercion and the resulting list cannot be coerced back to a record.

##### Examples

The following example shows how to change the value of a property in a record:

```

set myRecord to {product:"pen", price:2.34}```

```

product of myRecord -- result: "pen"```

```

 ```

```

set product of myRecord to "pencil"```

```

product of myRecord -- result: "pencil"```
AppleScript evaluates expressions in a record before using the record in other expressions. For example, the following two records are equivalent:

```

{ name:"Steve", height:76 - 1.5, weight:150 + 20 }```

```

{ name:"Steve", height:74.5, weight:170 }```
You cannot refer to properties in records by numeric index. For example, the following object specifier, which uses the index reference form on a record, is not valid.

```

item 2 of { name:"Rollie", IQ:186, city:"Unknown" } --result: error```
You can access thelengthproperty of a record to count the properties it contains:

```

length of {name:"Chris", mileage:1957, city:"Kalamazoo"} --result: 3```
You can get the same value with thecountcommand:

```

count {name:"Chris", mileage:1957, city:"Kalamazoo"} --result: 3```

##### Discussion

After you define a record, you cannot add additional properties to it. You can, however, concatenate records. For more information, see& (concatenation).
An object that encapsulates an object specifier.
The result of thea reference tooperator is areferenceobject, and object specifiers returned from application commands are implicitly turned intoreferenceobjects.
Areferenceobject âwrapsâ an object specifier. If you target areferenceobject with thegetcommand, the command returns thereferenceobject itself. If you ask areferenceobject for itscontentsproperty, it returns the enclosed object specifier. All other requests to areferenceobject are forwarded to its enclosed object specifier. For example, if you ask for theclassof areferenceobject, you get theclassof the object specified by its object specifier.
For related information, seeObject Specifiers.

##### Properties of reference objects

Other than thecontentsproperty, all other property requests are forwarded to the enclosed object specifier, so the reference object appears to have all the properties of the referenced object.

##### Operators

All operators are forwarded to the enclosed object specifier, so the reference object appears to support all the operators of referenced object.
Thea reference tooperator returns a reference object as its result.

##### Coercions Supported

All coercions are forwarded to the enclosed object specifier, so the reference object appears to support all the coercions of referenced object.

##### Examples

Reference objects are most often used to specify application objects. The following example creates a reference to a window within the TextEdit application:

```

set myWindow to a ref to window "top.rtf" of application "TextEdit"```

```

--result: window "top.rtf" of application "TextEdit"```
In subsequent script statements, you can use the variablemyWindowin place of the longer termwindow "top.rtf" of application "TextEdit".
Because all property requests other thancontents ofare forwarded to its enclosed specifier, thereferenceobject appears to have all the properties of the referenced object. For example, bothclass ofstatements in the following example returnwindow:

```

set myRef to a reference to window 1```

```

class of contents of myRef  -- explicit dereference using "contents of"```

```

class of myRef  -- implicit dereference```
For additional examples, see thea reference tooperator.
A type definition for a three-item list ofintegervalues, from 0 to 65535, that specify the red, green, and blue components of a color.
Otherwise, behaves exactly like alistobject.

##### Examples

```

set whiteColor to {65535, 65535, 65535} -- white```

```

set yellowColor to {65535, 65535, 0} -- yellow```

```

yellowColor as string --result: "65535655350"```

```

set redColor to {65535, 0, 0} -- red```

```

set userColor to choose color default color redColor```
A collection of AppleScript declarations and statements that can be executed as a group.
The syntax for ascriptobject is described inDefining Script Objects.

##### Properties of script objects

##### Commands Handled

You can copy ascriptobject with thecopycommand or create a reference to it with thesetcommand.

##### Coercions Supported

AppleScript supports coercion of ascriptobject to a single-itemlist.

##### Examples

The following example shows a simplescriptobject that displays a dialog. It is followed by a statement that shows how to run the script:

```

script helloScript```

```

    display dialog "Hello."```

```

end script```

```

 ```

```

run helloScript -- invoke the script```

##### Discussion

Ascriptobject can contain otherscriptobjects, called child scripts, and can have a parent object. For additional information, including more detailed examples, seeScript Objects.
Thename,id, andversionproperties are automatically defined in OS X Mavericks v10.9 (AppleScript 2.3) and later, and are used to identify scripts used as libraries, as described inScript Objects.
An ordered series of Unicode characters.
Starting in AppleScript 2.0, AppleScript is entirely Unicode-based. There is no longer a distinction between Unicode and non-Unicode text. Comments and text constants in scripts may contain any Unicode characters, and all text processing is done in Unicode, so all characters are preserved correctly regardless of the userâs language preferences.
For example, the following script works correctly in AppleScript 2.0, where it would not have in previous versions:

```

set jp to "æ¥æ¬èª"```

```

set ru to "Ð ÑÑÑÐºÐ¸Ð¹"```

```

jp & " and " & ru -- returns "æ¥æ¬èª and Ð ÑÑÑÐºÐ¸Ð¹"```
For information on compatibility with previous AppleScript versions, including the use ofstringandUnicode textas synonyms fortext, see the Special Considerations section.

##### Properties of text objects

##### Elements of text objects

Atextobject can contain these elements (which may behave differently than similar elements used in applications):
One or more Unicode characters that make up the text.
Starting in AppleScript 2.0, elements oftextobject count a combining character cluster (also known as a Unicode grapheme cluster) as a single character. (This relates to a feature of Unicode that is unlikely to have an impact on most scripters: some âcharactersâ may be represented as either a single entity or as a base character plus a series of combining marks.
For example, âÃ©â may be encoded as either U+00E9 (LATIN SMALL LETTER E WITH ACUTE) or as U+0065 (LATIN SMALL LETTER E), U+0301 (COMBINING ACUTE ACCENT). Nonetheless, AppleScript 2.0 will count both as one character, where older versions counted the base character and combining mark separately.
A series of characters beginning immediately after either the first character after the end of the preceding paragraph or the beginning of the text and ending with either a carriage return character (\r), a linefeed character (\n), a return/linefeed pair (\r\n), or the end of the text. The Unicode "paragraph separator" character (U+2029) is not supported.
Becauseparagraphelements areseparatedby a carriage return, linefeed, or carriage return/linefeed pair, text ending with a paragraph break specifies a following (empty) paragraph. For example,"this\nthat\n"has three paragraphs, not two: "this", "that", and "" (the empty paragraph after the trailing linefeed).
Similarly, two paragraph breaks in a row specify an empty paragraph between them:
paragraphs of "this\n\nthat" --result: {"this", "", "that"}
All of the text contained in thetextobject, including spaces, tabs, and all other characters.
You can usetextto access contiguous characters (but see also the Discussion section below):
text 1 thru 5 of "Bring me the mouse." --result: "Bring"
A continuous series of characters, with word elements parsed according to the word-break rules set in the International preference pane.
Because the rules for parsing words are thus under user control, your scripts should not count on a deterministic text parsing of words.

##### Operators

The operators that can havetextobjects as operands are&,=,â,>,â¥,<,â¤,starts with,ends with,contains,is contained by, andas.
In text comparisons, you can specify whether white space should be considered or ignored. For more information, seeconsidering and ignoring Statements.
For detailed explanations and examples of how AppleScript operators treattextobjects, seeOperators Reference.

##### Special String Characters

The backslash (\) and double-quote (") characters have special meaning in text. AppleScript encloses text in double-quote characters and uses the backslash character to represent return (\r), tab (\t), and linefeed (\n) characters (described below). So if you want to include an actual backslash or double-quote character in atextobject, you must use the equivalent two-character sequence. As a convenience, AppleScript also provides the text constantquote, which has the value\".
Character
To insert in text
Backslash character (\)
Double quote (")
quote(text constant)
To declare atextobject that looks like this when displayed:

```

He said "Use the '\' character."```
you can use the following:

```

"He said \"Use the '\\' character.\""```
White space refers to text characters that display as vertical or horizontal space. AppleScript defines the white spaceconstantsreturn,linefeed,space, andtabto represent, respectively, a return character, a linefeed character, a space character, and a tab character. (Thelinefeedconstant became available in AppleScript 2.0.)
Although you effectively use these values as text constants, they are actually defined as properties of the global constantAppleScript.
Constant
Value
space
"\t"
return
"\r"
linefeed
"\nâ
To enter white space in a string, you can just type the characterâthat is, you can press the Space bar to insert a space, the Tab key to insert a tab character, or the Return key to insert a return. In the latter case, the string will appear on two lines in the script, like the following:

```

display dialog "Hello" & "```

```

" & "Goodbye"```
When you run this script, "Hello" appears above âGoodbyeâ in the dialog.
You can also enter a tab, return, or linefeed with the equivalent two-character sequences. When atextobject containing any of the two-character sequences is displayed to the user, the sequences are converted. For example, if you use the followingtextobject in adisplay dialogcommand:

```

display dialog "item 1\t1\ritem 2\t2"```
it is displayed like this (unless you enable âEscape tabs and line breaks in stringsâ in the Editing tab of the of Script Editor preferences):

```

item 1      1```

```

item 2      2```
To use the white space constants, you use the concatenation operator to join multipletextobjects together, as in the following example:

```

"Year" & tab & tab & "Units sold" & return & "2006" & tab Â¬```

```

    & tab & "300" & return & "2007" & tab & tab & "453"```
When passed todisplay dialog, this text is displayed as follows:

```

Year       Units sold```

```

2006            300```

```

2007            453```

##### Coercions Supported

AppleScript supports coercion of antextobject to a single-itemlist. If atextobject represents an appropriate number, AppleScript supports coercion of thetextobject to an integer or a real number.

##### Examples

You can define atextobject in a script by surrounding text characters with quotation marks, as in these examples:

```

set theObject to "some text"```

```

set clientName to "Mr. Smith"```

```

display dialog "This is a text object."```
Suppose you use the following statement to obtain atextobject nameddocTextthat contains all the text extracted from a particular document:

```

set docText to text of document "MyFavoriteFish.rtf" of application "TextEdit"```
The following statements show various ways to work with thetextobjectdocText:

```

class of docText --result: text```

```

first character of docText --result: a character```

```

every paragraph of docText --result: a list containing all paragraphs```

```

paragraphs 2 thru 3 of docText --result: a list containing two paragraphs```
The next example prepares atextobject to use with thedisplay dialogcommand. It uses thequoteconstant to insert\"into the text. When this text is displayed in the dialog (above a text entry field), it looks like this:Enter the text in quotes ("text in quotes"):

```

set promptString to "Enter the text in quotes (" & quote Â¬```

```

    & "text in quotes" & quote & "): "```

```

display dialog promptString default answer ""```
The following example gets a POSIX path to a chosen folder and uses thequoted formproperty to ensure correct quoting of the resulting string for use with shell commands:

```

set folderName to quoted form of POSIX path of (choose folder)```
Suppose that you choose the folder namediWork '08in yourApplicationsfolder. The previous statement would return the following result, which properly handles the embedded single quote and space characters in the folder name:

```

"'/Applications/iWork '\\''08/'"```

##### Discussion

To get a contiguous range of characters within atextobject, use thetextelement. For example, the value of the following statement is thetextobject"y thi":

```

get text 3 thru 7 of "Try this at home"```

```

--result: "y thi"```
The result of a similar statement using the character element instead of the text element is a list:

```

get characters 3 thru 7 of "Try this at home"```

```

--result: {"y", " ", "t", "h", "i"}```
You cannot set the value of an element of atextobject. For example, if you attempt to change the value of the first character of the text objectmyNameas shown next, youâll get an error:

```

set myName to "Boris"```

```

set character 1 of myName to "D"```

```

--result: error: you cannot set the values of elements of text objects```
However, you can achieve the same result by getting the last four characters and concatenating them with "D":

```

set myName to "boris"```

```

set myName to "D" & (get text 2 through 5 of myName)```

```

--result: "Doris"```
This example doesnât actually modify the existingtextobjectâit sets the variablemyNameto refer to a newtextobject with a different value.

##### Special Considerations

For compatibility with versions prior to AppleScript 2.0,stringandUnicode textare still defined, but are considered synonyms fortext. For example, all three of these statements have the same effect:

```

someObject as text```

```

someObject as string```

```

someObject as Unicode text```
In addition,text,string, andUnicode textwill all compare as equal. For example,class of "foo" is stringistrue, even thoughclass of "foo"returnstext. However, it is still possible for applications to distinguish between the three different types, even though AppleScript itself does not.
Starting with AppleScript 2.0, there is no style information stored withtextobjects.
Because all text is Unicode text, scripts now always get the Unicode text behavior. This may be different from the formerstringbehavior for some locale-dependent operations, in particularwordelements. To get the same behavior with 2.0 and pre-2.0, add an explicitas Unicode textcoercion, for example,words of (someText as Unicode text).
Becausetext item delimiters(described intext item delimiters) respectconsideringandignoringattributes in AppleScript 2.0, delimiters are case-insensitive by default. Formerly, they were always case-sensitive. To enforce the previous behavior, add an explicitconsidering casestatement.
Because AppleScript 2.0 scripts store all text as Unicode, any text constants count as a use of the formerUnicode textclass, which will work with any version of AppleScript back to version 1.3. A script that contains Unicode-only characters such as Arabic or Thai will run, but will not be correctly editable using versions prior to AppleScript 2.0: the Unicode-only characters will be lost.
Used for working with measurements of length, area, cubic and liquid volume, mass, and temperature.
The unit type classes support simple objects that do not contain other values and have only a single property, theclassproperty.

##### Properties of unit type objects

##### Operators

None. You must explicitly coerce a unit type to a number type before you can perform operations with it.

##### Coercions Supported

You can coerce a unit type object tointeger, single-itemlist,real, ortext. You can also coerce between unit types in the same category, such asinchestokilometers(length) orgallonstoliters(liquid volume). As you would expect, there is no coercion between categories, such as fromgallonstodegrees Centigrade.

##### Examples

The following statements calculate the area of a circle with a radius of 7 yards, then coerce the area to square feet:

```

set circleArea to (pi * 7 * 7) as square yards --result: square yards 153.9380400259```

```

circleArea as square feet --result: square feet 1385.4423602331```
The following statements set a variable to a value of 5.0 square kilometers, then coerce it to various other units of area:

```

set theArea to 5.0 as square kilometers --result: square kilometers 5.0```

```

theArea as square miles --result: square miles 1.930510792712```

```

theArea as square meters --result: square meters 5.0E+6```
However, you cannot coerce an area measurement to a unit type in a different 
category:

```

set theArea to 5.0 as square meters --result: square meters 5.0```

```

theArea as cubic meters --result: error```

```

theArea as degrees Celsius --result: error```
The following statements demonstrate coercion of a unit type to atextobject:

```

set myPounds to 2.2 as pounds --result: pounds 2.2```

```

set textValue to myPounds as text --result: "2.2"```
Copyright © 2016 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2016-01-25