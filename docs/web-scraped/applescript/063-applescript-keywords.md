# AppleScript Keywords

# AppleScript Keywords
This appendix lists AppleScript keywords (orreserved words), provides a brief description for each, and points to related information, where available. (See alsoKeywordsinAppleScript Lexical Conventions.)
The keywords inTable A-1are part of the AppleScript language. You should not attempt to reuse them in your scripts for variable names or other purposes. Developers should not re-define keywords in the terminology for their scriptable applications. You can view many additional scripting terms defined by Apple, but not part of the AppleScript language, inAppleScript Terminology and Apple Event Codes.
about
handler parameter labelâseeHandler Syntax (Labeled Parameters)
above
handler parameter labelâseeHandler Syntax (Labeled Parameters)
after
used to describe position in theRelativereference form; used as part of operator (comes after,does not come after) with classes such asdate,integer, andtext
against
handler parameter labelâseeHandler Syntax (Labeled Parameters)
logicalandoperatorâseeTable 9-1
apart from
handler parameter labelâseeHandler Syntax (Labeled Parameters)
around
handler parameter labelâseeHandler Syntax (Labeled Parameters)
coercion operatorâseeTable 9-1
aside from
handler parameter labelâseeHandler Syntax (Labeled Parameters)
handler parameter labelâseeHandler Syntax (Labeled Parameters)
back
used withIndexandRelativereference forms;in back ofis synonymous withafterandbehind
before
used to describe position in theRelativereference form; used as an operator (comes before,does not come before) with classes such asdate,integer, andtext; synonymous within front of
beginning
specifies an insertion location at the beginning of a containerâsee the boundary specifier descriptions for theRangereference form
behind
synonymous withafterandin back of
below
handler parameter labelâseeHandler Syntax (Labeled Parameters)
beneath
handler parameter labelâseeHandler Syntax (Labeled Parameters)
beside
handler parameter labelâseeHandler Syntax (Labeled Parameters)
between
handler parameter labelâseeHandler Syntax (Labeled Parameters)
used inconsidering and ignoring Statements
used with binary containment operatorcontains, is contained by; also used as handler parameter labelâseeHandler Syntax (Labeled Parameters)
considering
a control statementâseeconsidering and ignoring Statements
contain, contains
binary containment operatorâseecontains, is contained by
continue
changes the flow of executionâseecontinue
copy
an AppleScript commandâseecopy
division operatorâseeTable 9-1
does
used with operators such asdoes not equal,does not come before, anddoes not containâseeTable 9-1
eighth
specifies a position in a containerâseeIndexreference form
else
used withifcontrol statementâseeif Statements
marks the end of a script or handler definition, or of a compound statement, such as atellorrepeatstatement; also specifies an insertion location at the end of a containerâsee the boundary specifier descriptions for theRangereference form
equal, equals
binary comparison operatorâseeequal, is not equal to
error
errorcontrol statement; also used withtrystatement
every
specifies every object in a containerâseeEveryreference form
exit
terminates arepeatloopâseeexit
false
a Boolean literalâseeBoolean
fifth
specifies a position in a containerâseeIndexreference form
first
specifies a position in a containerâseeIndexreference form
handler parameter labelâseeHandler Syntax (Labeled Parameters)
fourth
specifies a position in a containerâseeIndexreference form
from
used in specifying a range of objects in a containerâseeRangereference form; also used as handler parameter labelâseeHandler Syntax (Labeled Parameters)
front
in front ofis used to describe position in theRelativereference form; synonymous withbefore
an AppleScript commandâseeget
given
a special handler parameter labelâseeHandler Syntax (Labeled Parameters)
global
specifies the scope for a variable (see alsolocal)âseeGlobal Variables
a control statementâseeif Statements
ignoring
a control statementâseeconsidering and ignoring Statements
used in construction object specifiersâseeContainers; also used with theRelativereference formâfor examplein front ofandin back of
instead of
handler parameter labelâseeHandler Syntax (Labeled Parameters)
into
put intois a deprecated synonym for thecopycommand; also used as handler parameter labelâseeHandler Syntax (Labeled Parameters)
used with various comparison operatorsâseeTable 9-1
refers to the current target (of it)âseeThe it and me Keywords
synonym forof itâseeThe it and me Keywords
last
specifies a position in a containerâseeIndexreference form
local
specifies the scope for a variable (see alsoglobal)âseeLocal Variables
refers to the current script (of me)âseeThe it and me Keywords
middle
specifies a position in a containerâseeIndexreference form
remainder operatorâseeTable 9-1
synonym forof meâseeThe it and me Keywords
ninth
specifies a position in a containerâseeMiddlereference form
logical negation operatorâseeTable 9-1
used in construction object specifiersâseeContainers; used with or as part of many other terms, includingof me,in front of, and so on
handler parameter labelâseeHandler Syntax (Labeled Parameters)
onto
handler parameter labelâseeHandler Syntax (Labeled Parameters)
logicaloroperatorâseeTable 9-1
out of
handler parameter labelâseeHandler Syntax (Labeled Parameters)
over
handler parameter labelâseeHandler Syntax (Labeled Parameters)
prop, property
propis an abbreviation forpropertyâseeThe it and me Keywords
put intois a deprecated synonym for thecopycommand
ref/reference
refis an abbreviation forreferenceâseereference
repeat
a control statementâseerepeat Statements
return
exits from a handlerâseereturn
returning
deprecated
script
used to declare a script object; also the class of a script objectâsee thescriptclass andScript Objects
second
specifies a position in a containerâseeIndexreference form
an AppleScript commandâseeset
seventh
specifies a position in a containerâseeIndexreference form
since
handler parameter labelâseeHandler Syntax (Labeled Parameters)
sixth
specifies an index position in a containerâseeIndexreference form
some
specifies an object in a containerâseeArbitraryreference form
tell
a control statementâseetell Statements
tenth
specifies a position in a containerâseeIndexreference form
that
synonym forwhose
syntactic no-op, used to make script statements look more like natural language
then
used withifcontrol statementâseeif Statements
third
specifies a position in a containerâseeIndexreference form
through, thru
used in specifying a range of objects in a containerâseeRangereference form
timeout
used withwith timeoutcontrol statementâseewith timeout
times
used withrepeatcontrol statementâseerepeat (number) times
used in many places, includingcopyandsetcommands; in theRangereference form; by operators such asis equal toanda reference to; with the control statementrepeat with loopVariable (from startValue to stopValue); with the partial result parameter intry Statements
transaction
used withwith transactioncontrol statementâseewith transaction
true
a Boolean literalâseeBoolean
an error-handling statementâseetry Statements
until
used withrepeatcontrol statementâseerepeat until
a requirement statementâseeuse Statements
where
used with theFilterreference form to specify a Boolean test expression (synonymous withwhose)
while
used withrepeatcontrol statementâseerepeat while
whose
used with theFilterreference form to specify a Boolean test expression (synonymous withwhere)
with
used in commands to specify various kinds of parameters, includingtruefor some Boolean for parametersâsee, for example, thewith promptandmultiple selections allowedparameters to thechoose from listcommand; also used with applicationmakecommands to specify properties (with properties)
without
used in commands to specifyfalsefor a Boolean for a parameterâsee, for example, themultiple selections allowedparameter to thechoose from listcommand
Copyright © 2016 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2016-01-25