# Building an Apple Event

# Retired Document
Important:This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

This chapter provides an overview of Apple event data structures and describes how to build an Apple event.
An Apple event is capable of describing complex commands and the data necessary to carry them out. For example, an Apple event might request that a database application return data from records that meet certain criteria. An event sent by the Mac OS might request that the receiving application print a specified list of documents. The Apple Event Manager provides a relatively small number of Apple event data structures that together can be used to represent commands of great complexity.
Your application typically works with Apple events and the data they contain when:
- It receives an Apple event and must extract information to figure out what to do with the event.
It receives an Apple event and must extract information to figure out what to do with the event.
- In response to a received Apple event, it must add information to a reply event to return to the sender.
In response to a received Apple event, it must add information to a reply event to return to the sender.
- It creates an Apple event from scratch for internal communication or to request data or services from another application.
It creates an Apple event from scratch for internal communication or to request data or services from another application.
Working effectively with Apple events in these cases requires some knowledge of the data structures and organization of an Apple event, as well as familiarity with the Apple Event Manager functions you use to create Apple events and manipulate their data.

## About Apple Event Data Structures
Understanding a few key concepts can help things go smoothly in creating an Apple event or working with its data:
- Each piece of information in an Apple event is associated with a four-character code (or in some cases, two such codes).
Each piece of information in an Apple event is associated with a four-character code (or in some cases, two such codes).
- A descriptor is a data structure that stores data and an accompanying four-character code. All the information you work with in an Apple event is stored in descriptors and lists of descriptors.
A descriptor is a data structure that stores data and an accompanying four-character code. All the information you work with in an Apple event is stored in descriptors and lists of descriptors.
- The content of an Apple event is conceptually divided into two kinds of items, both constructed from descriptors:Attributes identify characteristics of the task to be performed by the Apple event.Parameters provide additional data to be used in performing the task.
The content of an Apple event is conceptually divided into two kinds of items, both constructed from descriptors:
- Attributes identify characteristics of the task to be performed by the Apple event.
Attributes identify characteristics of the task to be performed by the Apple event.
- Parameters provide additional data to be used in performing the task.
Parameters provide additional data to be used in performing the task.
- To create an Apple event, extract data from an event, or add data to an event, an application calls Apple Event Manager functions and passes the appropriate four-character codes and other information.
To create an Apple event, extract data from an event, or add data to an event, an application calls Apple Event Manager functions and passes the appropriate four-character codes and other information.
- To operate effectively with Apple events, you just need to find the right function for the task at hand.
To operate effectively with Apple events, you just need to find the right function for the task at hand.

## Apple Event Building Blocks
This section describes the constants and data structures used to construct an Apple event.

### Apple Event Constants
The Apple Event Manager uses four-character codes (also referred to as Apple event codes) to identify the data within an Apple event. A four-character code is just four bytes of data that can be expressed as a string of four characters in the Mac OS Roman encoding. For example,'capp'is the four-character code that specifies an application.
The Apple Event Manager defines four-character-code constants for many common commands (or verbs) and data objects (or nouns) that can be used in Apple events. These constants are defined primarily in the header filesAppleEvents.handAERegistry.hin the AE framework. They are documented inApple Event Manager Reference. A subset of these constants is described inSelected Apple Event Constantsin this document.
Listing 2-1shows some constants fromAERegistry.h. Each constant definition includes a comment showing the actual numeric value as a hex number.
Listing 2-1Some four-character codes from AERegistry.h

```applescript
enum {
```

```applescript
  cApplication                  = 'capp', /*  0x63617070  */
```

```applescript
  cArc                          = 'carc', /*  0x63617263  */
```

```applescript
  cBoolean                      = 'bool', /*  0x626f6f6c  */
```

```applescript
  cCell                         = 'ccel', /*  0x6363656c  */
```

```applescript
  cChar                         = 'cha ', /*  0x63686120  */
```

```applescript
  cDocument                     = 'docu', /*  0x646f6375  */
```

```applescript
  cGraphicLine                  = 'glin', /*  0x676c696e  */
```

```applescript
...
```

```applescript
};
```

For the Apple event support in your application, you should use existing constants wherever they make sense, rather than defining new constants. For example, if your application supports an Apple event to get the name of a document, you can use the constantcDocumentto denote a document.
Apple reserves all values that consist entirely of lowercase letters and spaces. You can generally avoid conflicts with Apple-defined constants by including at least one uppercase letter when defining a four-character code.

### Event Class and Event ID
An Apple event is uniquely identified by itsevent classandevent IDattributes, each of which is an arbitrary four-character code (described inApple Event Constants). The Apple Event Manager uses these values in dispatching Apple events to code in your application (described inApple Event Dispatching).
Apple defines event class and event ID values for standard Apple events, including those that it sends. For example, adeleteApple event has an event class value of'core'(represented by the constantkAECoreSuite) and an event ID value of'delo'(kAEDelete). For examples and descriptions of Apple-defined event class and event ID values, seeEvent Class Constants,Event ID Constants for Apple Events Sent by the Mac OS, andEvent ID Constants for Standard AppleScript Commands.
You define the event class and event ID values for application-specific Apple events your application supports. While these values are arbitrary, you should follow the simple guidelines described inApple Event Constantsin choosing values.
You can use a common event class for multiple Apple events as a way to group related events that your application supports. For example, many Apple-defined Apple events share a common event class. This can be useful in organizing the name space for your Apple events and may simplify your coding, but it doesnât result in any special treatment by the Apple Event Manager.
If you want other applications to be able to send Apple events to your application, you must publish event class and event ID values for those events. You should also describe the contents your application expects to find in each type of Apple event.
Similarly, if you want to send Apple events to other applications, you are dependent on those applications to provide the event class, event ID, and any other information you need to construct an Apple event the application can understand. One exception is that most applications, including yours, should be able to handle the Apple events described inCommon Apple Events Sent by the Mac OS. So, for example, you might construct aquitApple event that targets almost any Mac OS X application, and expect the application to handle it.

### Descriptors, Descriptor Lists, and Apple Events
Descriptors and descriptor lists are the basic structural elements used in Apple events. Adescriptorstores data and an accompanying descriptor type to form the basic building block of all Apple Events. Thedescriptor typeis a four-character code that identifies the type of data associated with the descriptor.Table B-4lists constants for some of the main descriptor typesâfor a complete list, seeApple Event Manager Reference.Figure 2-1shows the format of a descriptor.
The data field of a descriptor is opaqueâyou should not attempt to access it directly.Table A-1lists functions provided by the Apple Event Manager for accessing the data in a descriptor (and related data types).
Figure 2-2shows a descriptor with a descriptor type oftypeUTF8Text, which specifies that the descriptorâs data is text in UTF-8 encodingâin this case, the text is âSummary of Salesâ.
Akeywordis a four-character code used by the Apple Event Manager to identify a specific descriptor within an Apple event. Akeyword-specified descriptorcombines a keyword with a descriptor. This is the basic type used to specify attributes and parameters, which are described in detail inApple Event Attributes and Parameters.Figure 2-3shows the format of a keyword-specified descriptor.
Anaddress descriptoris a descriptor that specifies a target address for an Apple eventâthat is, it specifies the application or other process to send the event to. The descriptor type can be specified by one of the constants shown inTable B-5.
Adescriptor listis a descriptor whose data consists of a list of zero or more descriptors (it can be an empty list). A descriptor list can contain other lists, which allows for the construction of complex descriptors, and hence complex Apple events.Figure 2-4shows the format of a descriptor list.
AnApple event recordis a descriptor list whose data is a set of keyword-specified descriptors that describe Apple event parameters.
AnApple eventis an Apple event record whose contents are conceptually divided into two parts, one for attributes and one for parameters, as shown inFigure 2-6.
Figure 2-5shows the inheritance for descriptors and related data structures, with the corresponding data types shown in parentheses.
An Apple Event Manager function that operates on one of these data structures can also operate on any type that inherits from it. For example, Apple events inherit from Apple event records, which inherit from descriptor lists. As a result, you can pass an Apple event to any Apple Event Manager function that expects an Apple event record or a descriptor list. Similarly, you can pass Apple events and Apple event records, as well as descriptor lists and descriptors, to any Apple Event Manager function that expects a descriptor. SeeTable A-1for a list of functions for working with the various data types.

### Apple Event Attributes and Parameters
Every Apple event consists of attributes and, often, parameters, as shown inFigure 2-6. Taken together, the attributes of an Apple event denote the task to be performed, while the parameters provide additional information to be used in performing the task.
You use Apple Event Manager functions to create an Apple event, to add attributes or parameters to an Apple event, and to extract and examine the attributes or parameters from an Apple event.

#### Apple Event Attributes
AnApple event attributeis a keyword-specified descriptor that identifies a characteristic of an Apple event. For example, every Apple event must include attributes for event class, event ID, and target address:
- The event classand event IDattributes provide a pair of arbitrary four-character codes that together uniquely identify an Apple event. For more information, seeEvent Class and Event ID.
The event classand event IDattributes provide a pair of arbitrary four-character codes that together uniquely identify an Apple event. For more information, seeEvent Class and Event ID.
- Thetarget address attributespecifies the process to send the Apple event to.
Thetarget address attributespecifies the process to send the Apple event to.
Apple events can include other kinds of attributesâseeTable B-6for a list of keyword constants for Apple event attributes.

#### Apple Event Parameters
AnApple event parameteris a keyword-specified descriptor that contains additional data for the command. Keywords for common Apple event parameters are shown inTable B-7.
As with attributes, there are various kinds of Apple event parameters. Adirect parameterusually specifies the data to be acted upon by the target application. For example,Figure 2-7shows the main Apple event attributes and the direct parameter for anopen documentsevent that targets the AppleWorks application. The direct parameter specifies a descriptor list containing file aliases to the documents to open. An Apple event has at most one direct parameter.
Apple event parameters can contain standard data types, such as text strings, integers of various lengths, Boolean values, and others, listed inTable B-4.
An Apple event can include other parameters, in addition to the direct parameter. For example, an Apple event that represents an arithmetic operation might contain a direct parameter that specifies a pair of values to operate on, as well as an additional parameter that specifies the operator. A reply Apple event may contain an error number parameter and an error string parameter, added by your application when an error occurs, as described inReturning Error Information.

#### Accessing Attributes and Parameters
Your application cannot examine the attributes and parameters of an assembled Apple event directly. Instead, it calls Apple Event Manager functions such asAEGetAttributeDescandAEGetParamDescto request an attribute or parameter by keyword. Because attributes and parameters are descriptors, you can also operate on them by index, using the functionsAEGetNthDescorAEGetNthPtr. However, that only makes sense if, for example, you are iterating over every descriptorâyou should not assume that the parameters or attributes in an Apple event are in any particular order.
Apple event parameters often contain descriptions of Apple event objects within the target application. For example, aget dataApple event contains a parameter that describes the Apple event object that contains the requested data. Thus, an event might request, for example, the first paragraph of text from a named document. Apple event objects are described inâResolving and Creating Object Specifier RecordsâinInside Macintosh: Interapplication Communication.
For more information on accessing attributes and parameters in an Apple event, seeWorking With the Data in an Apple Event.

#### Optional Parameters
An Apple event may be defined so that it has optional parameters. Anoptional parameteris one that the sending application may or may not include. A target application must be prepared to handle the event whether or not the optional parameter is present. However, it can choose to ignore an optional parameter, even if present. This allows optional parameters to be added to an Apple event retroactively, without breaking existing code.
If an optional parameter is not present, or if your application chooses to ignore it, you should provide the default behavior for the Apple event. To determine if an optional parameter is present, you call a function such asAEGetParamDesc, specifying the keyword for the parameter. If the function returns successfully, you can extract information from the parameter and respond accordingly. If the function returns an error, you can assume the parameter is not present and provide the default behavior.

## Two Approaches to Creating an Apple Event
How do you put together the data structures described in this chapter to create an Apple event? The Apple Event Manager provides functions that lend themselves to two main approaches, which you can combine as needed:
- You can create an Apple event with one call, passing all the information needed for a complete Apple event.Related functions allow you to create a complex descriptor, attribute, or parameter and add it to an existing Apple event in one step.
You can create an Apple event with one call, passing all the information needed for a complete Apple event.
Related functions allow you to create a complex descriptor, attribute, or parameter and add it to an existing Apple event in one step.
- You can create an Apple event sequentially, by first creating a potentially incomplete event, then adding information to it with subsequent calls.With this approach, you build descriptors into more complex data structures from the bottom up.
You can create an Apple event sequentially, by first creating a potentially incomplete event, then adding information to it with subsequent calls.
With this approach, you build descriptors into more complex data structures from the bottom up.
In either case, your application relies on the Apple Event Manager to construct Apple event data structures based on the arguments you pass.
Note:There is a third way, not shown in this document, to create Apple event records and Apple event descriptors using stream-oriented calling conventions. The stream APIs are documented inApple Event Manager Reference, while Technical Note 2046AEStream and Friendsprovides conceptual overview and examples. You can use the stream functions independently, or combine them with the other mechanisms.

### Creating an Apple Event in One Step
You can call theAEBuildAppleEventfunction to create an Apple event in one step. To do so, you pass event class, event ID, and other information that is used to create the Apple eventâs attributes. TheAEBuildAppleEventfunction includes parameters for specifying the target addressâyou donât have to separately create an address descriptor. You may need to prepare data youâll pass toAEBuildAppleEventâfor example, you may need to create aliases to files you will insert into the Apple event as a descriptor list.
Note:In this discussion, the word âparameterâ is overloaded. When you callAEBuildAppleEvent, you pass information infunction parametersto specify how to createApple event parameters(and attributes), which are just Apple event data structures.
In addition, you provide a specially formatted string, similar to the string you might pass to aprintffunction, along with parameters that specify the data that corresponds to items in the format string. As a result,AEBuildAppleEventcan also create the parameters for your Apple event, resulting in a full-fledged Apple event.
The Apple Event Manager also provides theAEBuildDescfunction as a one-step mechanism for adding potentially complex descriptors to an existing Apple event, and theAEBuildParametersfunction for adding parameters or attributes.
The one-step functions are most useful in situations where your application knows in advance all the information needed to create an Apple event or other data structure. They also make it easier to do parameterized substitution of values. For an example of this approach, seeCreating an Apple Event With AEBuildAppleEvent.

### Creating an Apple Event Sequentially
You can create the basic structure for an Apple event by calling theAECreateAppleEventfunction. You pass information specifying event class, event ID, target address, return ID, and transaction ID; the function creates an Apple event containing the corresponding attributes. However, before you can callAECreateAppleEvent, you have to create a target address descriptor to pass to it, using a function such asAECreateDesc.
After callingAECreateAppleEvent, the resulting Apple event contains attributes for the event but no parameters. To add parameters to the event, you can use theAEBuildDescandAEBuildParametersfunctions described in the previous section, or you can continue to work sequentially. For example, if the direct object of the event you are creating is a list of file aliases, you could create it sequentially by performing the following steps:
- CallAECreateDesconce for each file alias to create a descriptor for it.
CallAECreateDesconce for each file alias to create a descriptor for it.
- CallAECreateListto create a descriptor list.
CallAECreateListto create a descriptor list.
- CallAEPutDesconce for each descriptor to add it to the descriptor list.
CallAEPutDesconce for each descriptor to add it to the descriptor list.
- CallAEPutParamDescto add the descriptor list to the Apple event as a parameter.
CallAEPutParamDescto add the descriptor list to the Apple event as a parameter.
This sequential approach is most useful for creating simple Apple events, or in situations where your application must factor the creation of an Apple event across several layers of codeâfor example, where you create an event, then pass it to various subsystems to add data to it.
For an example of how to create an Apple event step by step, seeCreating an Apple Event With AECreateAppleEvent.

### The Completed Apple Event
Figure 2-8shows the main data structures of a complete Apple event, containing a list of keyword-specified descriptors that specify the attributes and parameters of anopen documentsApple event. Although this is an event sent to your application by the Mac OS, events you create have a similar structure.
The figure includes attributes for the event class, event ID, and target address. It also shows the direct parameterâa keyword-specified descriptor with the keywordkeyDirectObject. The entire figure corresponds to theopen documentsevent shown inFigure 2-7.
Copyright © 2005, 2007 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2007-10-31