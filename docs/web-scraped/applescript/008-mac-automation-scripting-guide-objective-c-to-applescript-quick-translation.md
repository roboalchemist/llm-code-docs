# Mac Automation Scripting Guide: Objective-C to AppleScript Quick Translation Guide

## Objective-C to AppleScript Quick Translation Guide
This appendix provides AppleScript equivalents for typical Objective-C features of a class. Below the table is a list of notes that correspond to the numbers in column 1.
Note
Objective-C
AppleScript
@interface MyClass : NSObject {
script MyClass
Â Â Â property parent: class "NSObject"
Â Â Â int myProperty;
Â Â Â IBOutlet NSTextField *myField;
IBOutlet @property (retain) NSButton *myButton;
property myProperty: 0
property myField: missing value
property myButton: missing value
@end
@implementation MyClass
- (IBAction) myAction:(id) object {
-- Handler with interleaved parameters
Â Â Â on myAction:object
-- or
-- Handler with positional parameters
Â Â Â on myAction_(object)
// No Arguments
Â Â Â [object method];
// One Argument
Â Â Â [object method:parameterName];
// Multiple Argument
Â Â Â [object methodWithArgument1:parameter1 Argument2:parameter2];
-- No Arguments
Â Â Â Â Â Â object's methodName()
-- or
methodName() of object
-- or
tell object to methodName()
-- One Argument
object's methodName:parameterName
-- or
methodName_(parameterName) of object
-- or
tell object to methodName:parameterName
-- Multiple Arguments
object's methodWithArgument1:parameter1 Argument2:parameter2
-- or
methodWithArgument1_Argument2_(parameter1, parameter2) of object
-- or
tell object to methodWithArgument1:parameter1 Argument2:parameter2
Â Â Â [object propertyName];
Â Â Â object.propertyName;
Â Â Â Â Â Â object's propertyName()
-- or
propertyName() of object
Â Â Â Â Â Â object's propertyName
-- or
propertyName of object
@end
Â Â Â end myAction_
end script
- An Objective-C class corresponds to an AppleScriptscriptobject. In AppleScript, inheritance is denoted using theparentproperty.
An Objective-C class corresponds to an AppleScriptscriptobject. In AppleScript, inheritance is denoted using theparentproperty.
- An instance variable or@propertyin Objective-C corresponds to apropertyin AppleScript.AppleScript doesnât require explicit tagging of Interface Builder outlet properties (IBOutlet). Interface Builder sees any property with a value ofmissing valueas a potential outlet.
An instance variable or@propertyin Objective-C corresponds to apropertyin AppleScript.
AppleScript doesnât require explicit tagging of Interface Builder outlet properties (IBOutlet). Interface Builder sees any property with a value ofmissing valueas a potential outlet.
- Objective-C divides class definitions into an@interfacesection containing properties and an@implementationsection containing method definitions. AppleScript has no such division. Properties and methods are all contained within the samescriptobject.
Objective-C divides class definitions into an@interfacesection containing properties and an@implementationsection containing method definitions. AppleScript has no such division. Properties and methods are all contained within the samescriptobject.
- An Objective-C method definition corresponds to an AppleScript handler that uses either an interleaved- or positional-style for parameter placement.Interleaved parameters are preceded by colons and separated by spaces, similar to Objective-C syntax. SeeHandlers with Interleaved ParametersinAppleScript Language Guide.A positional parameter hander name is the Objective-C selector name, with colons changed to underscores. This handler name is followed by parentheses enclosing comma-separated parameters. SeeHandlers with Positional ParametersinAppleScript Language Guide.AppleScript doesnât require explicit tagging of Interface Builder action methods (IBAction). Interface Builder sees any method with a single parameter as a potential action method.
An Objective-C method definition corresponds to an AppleScript handler that uses either an interleaved- or positional-style for parameter placement.
Interleaved parameters are preceded by colons and separated by spaces, similar to Objective-C syntax. SeeHandlers with Interleaved ParametersinAppleScript Language Guide.
A positional parameter hander name is the Objective-C selector name, with colons changed to underscores. This handler name is followed by parentheses enclosing comma-separated parameters. SeeHandlers with Positional ParametersinAppleScript Language Guide.
AppleScript doesnât require explicit tagging of Interface Builder action methods (IBAction). Interface Builder sees any method with a single parameter as a potential action method.
- A method call in Objective-C corresponds to an AppleScript handler call that uses either interleaved- or positional-style parameters. Regardless of style, parameters must always be provided in the order the method definition specifies.AppleScript has three equivalent syntaxes for addressing object handlers and properties:object's method,method of object, andtell object to method.
A method call in Objective-C corresponds to an AppleScript handler call that uses either interleaved- or positional-style parameters. Regardless of style, parameters must always be provided in the order the method definition specifies.
AppleScript has three equivalent syntaxes for addressing object handlers and properties:object's method,method of object, andtell object to method.
- An Objective-C method with no parameters, such as a property or constant, can be called using an explicit accessor method call or more concise dot syntax. Similarly in AppleScript, a method with no parameters can be called using a handler call with empty parentheses, or as a property without the parentheses.
An Objective-C method with no parameters, such as a property or constant, can be called using an explicit accessor method call or more concise dot syntax. Similarly in AppleScript, a method with no parameters can be called using a handler call with empty parentheses, or as a property without the parentheses.
- In AppleScript, handlers andscriptobjects are closed using theendsyntax.
In AppleScript, handlers andscriptobjects are closed using theendsyntax.

### Resolving Terminology Conflicts in AppleScriptObjC
AppleScript distinguishes betweenreserved words,application identifiers, anduser identifiers. Reserved words are terms defined by AppleScript itself. Application identifiers, also known asapplication keywords, are terms defined by an appâs scripting dictionary. User identifiers are variable or subroutine names defined by the script writer.
Identifiers passed to AppleScriptObjC, in particular, Cocoa method names, must be user identifiers. If an identifier conflicts with a reserved word or an application identifier, you can force it to be considered a user identifier by escaping itâenclosing it in vertical bars. For example, theNSColorclass has asetmethod for setting the current drawing color. However,setis a reserved AppleScript term for assigning variables. Calling thesetmethod without escaping it would produce a syntax error.Listing 43-1shows the correct usage.
APPLESCRIPT
Open in Script Editor
- myColor's |set|()
- -- OR
- |set|() of myColor
- -- OR
- tell myColor to |set|()
Similarly,NSWindowhas aboundsproperty, butboundsis an application-defined term. Therefore, any references to this property must also be escaped. SeeListing 43-2.
APPLESCRIPT
Open in Script Editor
- get myWindow's |bounds|
- -- OR
- get |bounds| of myWindow
- -- OR
- tell myColor to get |bounds|
When in doubt, add the vertical bars. If theyâre unnecessary, they are merely redundant and harmless.

### Importing Frameworks
To import a framework in AppleScript, use theusecommand, followed by the framework name. SeeListing 43-3.
APPLESCRIPT
Open in Script Editor
- use framework "Foundation"
- set theString to "Hello World"
- set theString to stringWithString_(theString) of NSString of current application
- set theString to (uppercaseString() of theString) as string
- --> Result: "HELLO WORLD"

### Accessing Scripting Additions
A normal AppleScript automatically loads and has access to terminology from scripting additions that are installed on the system. In AppleScriptObjC scripts, you must explicitly state that you want to use scripting addition terminology.Listing 43-4shows how to do this.
APPLESCRIPT
Open in Script Editor
- use scripting additions
- display dialog "Hello World" as string

### Classes and Constants
In AppleScriptObjC, Objective-C classes and constants are referred to in the context of thecurrent applicationconstantâa reference to the app thatâs running the script.
In this context, classes are referenced using theclassspecifier, followed by the class name, as shown inListing 43-5.
APPLESCRIPT
Open in Script Editor
- use framework "Foundation"
- class "NSView" of current application
Constants are referenced without a preceding identifier. SeeListing 43-6.
APPLESCRIPT
Open in Script Editor
- use framework "Foundation"
- current application's NSCalibratedRGBColorSpace
- -- OR
- NSCalibratedRGBColorSpace of current application
Listing 43-7demonstrates how to reference both Objective-C classes and constants.
APPLESCRIPT
Open in Script Editor
- script MyView
- property parent : class "NSView"
- on drawRect:rect
- set theWhiteColor to current application's class "NSColor"'s whiteColor()
- -- OR
- set theWhiteColor to whiteColor() of class "NSColor" of current application
- -- OR
- tell class "NSColor" of current application to set theWhiteColor to whiteColor()
- theWhiteColor's colorUsingColorSpaceName:(current application's NSCalibratedRGBColorSpace)
- -- OR
- colorUsingColorSpaceName_(NSCalibratedRGBColorSpace of current application) of theWhiteColor
- end drawRect:
- end script
In places wherecurrent applicationis the current context, such as the top level of a script,current applicationmay be shortened tomyorme. In the case of class specifiers, it may be omitted entirely. SeeListing 43-8.
APPLESCRIPT
Open in Script Editor
- use framework "Foundation"
- class "NSView"
- my NSCalibratedRGBColorSpace
- -- OR
- NSCalibratedRGBColorSpace of me
As a convenience technique to save typing, itâs good practice to define properties for classes at the top of your script. This way, you can refer to them by property name throughout your script.
APPLESCRIPT
Open in Script Editor
- script MyView
- property parent : class "NSView"
- property NSColor : class "NSColor"
- on drawRect:rect
- set theWhiteColor to NSColor's whiteColor()
- theWhiteColor's colorUsingColorSpaceName:NSCalibratedRGBColorSpace
- end drawRect:
- end script

### Resources
For additional information about AppleScriptObjC, seeAppleScriptObjC Release Notesand the third-party bookEveryDay AppleScriptObjC.
Using Dictation to Run Scripts
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13