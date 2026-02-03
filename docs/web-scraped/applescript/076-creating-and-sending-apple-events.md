# Creating and Sending Apple Events

# Retired Document
Important:This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

# Creating and Sending Apple Events
This chapter provides information and sample code that will help you create and send Apple events and handle Apple events you receive in response to those you send. Before reading this chapter, you should be familiar with the information inBuilding an Apple Event.
Applications most commonly create and send Apple events for one of the reasons described inWhen Applications Use Apple Events: to communicate directly with other applications or to support recording in a scriptable application. And as described inTwo Approaches to Creating an Apple Event, you can create an Apple event in one step with theAEBuildAppleEventfunction, or you can create a possibly incomplete Apple event withAECreateAppleEvent, then add attributes and parameters to complete the event.
Note:Two Approaches to Creating an Apple Eventalso briefly describes a third approach, using stream-oriented calling conventions, and points to documentation for that approach.

## Functions for Creating Apple Event Data Structures
In addition to theAEBuildAppleEventandAECreateAppleEventfunctions for creating Apple events, you use the following functions for creating other data structures you use with Apple events:
- For creating descriptor records and lists and adding items to lists:AEBuildDesc,AECreateDesc,AECreateList,AEPutPtr,AEPutDesc
For creating descriptor records and lists and adding items to lists:
AEBuildDesc,AECreateDesc,AECreateList,AEPutPtr,AEPutDesc
- For adding attributes and parameters to Apple events and Apple event records:AEBuildParameters,AEPutParameter,AEPutParamDesc,AEPutAttributePtr,AEPutAttributeDesc
For adding attributes and parameters to Apple events and Apple event records:
AEBuildParameters,AEPutParameter,AEPutParamDesc,AEPutAttributePtr,AEPutAttributeDesc
Table A-1lists these and other Apple Event Manager functions. For complete function descriptions, seeApple Event Manager Reference.

## Specifying a Target Address
When you create an Apple event, you must specify the address of the target. Thetarget addressidentifies the particular application or process to send the Apple event to. You can send Apple events to applications on the local computer or on remote computers on the network. You specify a target address with atarget address descriptor.
The preferred descriptor types for identifying the address in an address descriptor are shown inAddress Descriptor Type Constants.You can also use another type if your application provides a coercion handler that coerces that type into one of the address types that the Apple Event Manager recognizes. SeeWriting and Installing Coercion Handlersfor more information on coercion handlers.
To address an Apple event to a target on a remote computer on the network, you generally usetypeApplicationURLfor the address descriptor type. To address an Apple event to a target on the local computer you can use any of the address types.
The fastest way for your application to send an Apple event to itself is to use a target address with a process serial number ofkCurrentProcess. For more information, seeAddressing an Apple Event for Direct Dispatching.

### Creating a Target Address Descriptor
If you want to create an Apple event with theAECreateAppleEventfunction, you need to create a target address descriptor to pass to the function. You can do so by calling theAECreateDescfunction.Listing 6-1shows how to create an address descriptor for a process serial number (typeProcessSerialNumber). Other target address descriptor types are shown inAddress Descriptor Type Constants.
Listing 6-1Creating an address descriptor using a process serial number
```
OSErr               err;```
```
ProcessSerialNumber thePSN;```
```
AEAddressDesc       addressDesc;```
```
 ```
```
err = GetProcessNumber(&thePSN);// 1```
```
if (err == noErr)```
```
{```
```
    err = AECreateDesc(typeProcessSerialNumber,```
```
                        &thePSN, sizeof(thePSN), &addressDesc);// 2```
```
}```
Hereâs a description of how this code snippet works:
- It calls an application-defined function,GetProcessNumber, to obtain the process serial number of another process.To create a target address descriptor for the current process, seeListing 6-2.
It calls an application-defined function,GetProcessNumber, to obtain the process serial number of another process.
To create a target address descriptor for the current process, seeListing 6-2.
- It callsAECreateDescto create a target address based on the specified process serial number.Your application should callAEDisposeDescto dispose of the address descriptor when it is finished with it.
It callsAECreateDescto create a target address based on the specified process serial number.
Your application should callAEDisposeDescto dispose of the address descriptor when it is finished with it.
When you create an Apple event with theAEBuildAppleEventfunction, it uses information from the following three parameters to create a target address descriptor:
The address type for the address information described in the next two parameters: for example,typeProcessSerialNumberortypeKernelProcessID.
A pointer to the address information.
The number of bytes pointed to by theaddressDataparameter.
For a code example that usesAEBuildAppleEvent, seeListing 6-4.

### Addressing an Apple Event for Direct Dispatching
Applications typically send Apple events to themselves to support recordability, discussed briefly inWhen Applications Use Apple Events. The best way for your application to send Apple events to itself is to use an address descriptor oftypeProcessSerialNumberwith thelowLongOfPSNfield set tokCurrentProcessand thehighLongOfPSNfield set to 0.Listing 6-2shows how to do this.
When you send an Apple event with this type of target address descriptor, the Apple Event Manager jumps directly to the appropriate Apple event handler without going through the normal event-processing sequence. This is not only more efficient, it avoids the situation in which an Apple event sent in response to a user action arrives in the event queue after some other event that really occurred later than the user action. For example, suppose a user chooses Cut from the Edit menu and then clicks in another window. If thecutApple event arrives in the queue after the window activate event, a selection in the wrong window might be cut.
Listing 6-2Creating an address descriptor that specifies the current application
```
    AEAddressDesc addressDesc;```
```
    ProcessSerialNumber selfPSN = { 0, kCurrentProcess };// 1```
```
 ```
```
    OSErr err = AECreateDesc(typeProcessSerialNumber, &selfPSN,```
```
                                sizeof(selfPSN), &addressDesc);// 2```
Hereâs a description of how this code snippet works:
- Sets up a process serial number for the current process, as described above.
Sets up a process serial number for the current process, as described above.
- CallsAECreateDescto create a target address that specifies the current application by its process serial number.Your application should callAEDisposeDescto dispose of the address descriptor when it is finished with it.
CallsAECreateDescto create a target address that specifies the current application by its process serial number.
Your application should callAEDisposeDescto dispose of the address descriptor when it is finished with it.
Your application can send events to itself using other forms of target addressing. However, this can lead to the event dispatching sequence problems just described.
Important:When Apple event recording has been turned on, the Apple Event Manager records every event that your application sends to itself unless you specify thekAEDontRecordflag in thesendModeparameter of theAESendorAESendMessagefunction.

### Obtaining the Addresses of Remote Processes
You can useAECreateRemoteProcessResolverand related functions to obtain the addresses of other processes on the network. To do so you follow these steps:
- CallAECreateRemoteProcessResolverto get a process resolver.
CallAECreateRemoteProcessResolverto get a process resolver.
- CallAERemoteProcessResolverGetProcessesto obtain a dictionary containing, for each remote application, the URL of the application and its human readable name (and possibly other information).
CallAERemoteProcessResolverGetProcessesto obtain a dictionary containing, for each remote application, the URL of the application and its human readable name (and possibly other information).
- CallAEDisposeRemoteProcessResolverto dispose of the process resolver.
CallAEDisposeRemoteProcessResolverto dispose of the process resolver.
- Create a target address descriptor based on a specified URL.Extract the URL from the dictionary entry as aCFURLRef.Convert it to aCFStringRef(for example, withCFURLGetString).Extract a text string in UTF-8 encoding. (For an example of code that extracts unicode text from aCFStringRef, seeListing 5-3.)Put the text into an address descriptor using the typetypeApplicationURL. The format of the URL associated with this type is described in the Discussion section of âDescriptor Type Constantsâ inApple Event Manager Reference.
Create a target address descriptor based on a specified URL.
- Extract the URL from the dictionary entry as aCFURLRef.
Extract the URL from the dictionary entry as aCFURLRef.
- Convert it to aCFStringRef(for example, withCFURLGetString).
Convert it to aCFStringRef(for example, withCFURLGetString).
- Extract a text string in UTF-8 encoding. (For an example of code that extracts unicode text from aCFStringRef, seeListing 5-3.)
Extract a text string in UTF-8 encoding. (For an example of code that extracts unicode text from aCFStringRef, seeListing 5-3.)
- Put the text into an address descriptor using the typetypeApplicationURL. The format of the URL associated with this type is described in the Discussion section of âDescriptor Type Constantsâ inApple Event Manager Reference.
Put the text into an address descriptor using the typetypeApplicationURL. The format of the URL associated with this type is described in the Discussion section of âDescriptor Type Constantsâ inApple Event Manager Reference.
- Alternatively, if the dictionary entry contains a process ID for the remote process, you can create an address descriptor based on the typetypeKernelProcessID.
Alternatively, if the dictionary entry contains a process ID for the remote process, you can create an address descriptor based on the typetypeKernelProcessID.
You can use the remote process resolver technology, for example, to present an interface to allow a user to select a remote application. For more information on these functions, see the section âLocating Processes on Remote Computersâ inApple Event Manager Reference.

## Creating an Apple Event
This section provides examples of how to create an Apple event withAECreateAppleEventand withAEBuildAppleEvent. These functions are introduced inTwo Approaches to Creating an Apple Event.

### Creating an Apple Event With AEBuildAppleEvent
TheAEBuildAppleEventfunction provides a mechanism for converting a specially formatted string into a complete Apple event. This function is similar toAECreateAppleEvent, but contains additional parameters it uses in creating the Apple event and constructing parameters for it.
TheAEBuildAppleEventfunction is similar to theprintffamily of routines in the standard C library. The syntax for the format string defines an Apple event as a sequence of name-value pairs, with optional parameters preceded with a tilde (~) character. For details, see Technical Note TN2106,AEBuild*, AEPrint*, and Friends.
The next two code listings show how you might useAEBuildAppleEventto create an Apple event that tells the Finder to reveal the startup disk (make it visible on the desktop).
Listing 6-3Constants used in creating a reveal Apple event for the Finder
```
const CFStringRef startupDiskPath = CFSTR("/");// 1```
```
const OSType finderSignature = 'MACS';// 2```
Hereâs a description of these constants, which are defined inAERegistry.hand used by the Finder in its Apple event support:
- Defines a string reference for the POSIX-style path of the startup disk.
Defines a string reference for the POSIX-style path of the startup disk.
- Defines the application signature for the Mac OS Finder application.Because the Finder is always running in Mac OS X, it is generally safe to send it an Apple event without first making sure it has been launched.
Defines the application signature for the Mac OS Finder application.
Because the Finder is always running in Mac OS X, it is generally safe to send it an Apple event without first making sure it has been launched.
Listing 6-4shows a function that creates an Apple event to reveal the startup disk in the Finder.
Listing 6-4Creating a reveal Apple event with AEBuildAppleEvent
```
OSErr BuildRevealStartupDiskAE (AppleEvent * revealEvent)// 1```
```
{```
```
    FSRef startupDiskFSRef;```
```
    AliasHandle startupDiskAlias;```
```
    OSErr err = noErr;```
```
 ```
```
    CFURLRef startupURLRef =```
```
        CFURLCreateWithFileSystemPath(kCFAllocatorDefault,```
```
            startupDiskPath, kCFURLPOSIXPathStyle, true);// 2```
```
 ```
```
    if (CFURLGetFSRef(startupURLRef, &startupDiskFSRef))// 3```
```
    {```
```
        err = FSNewAlias(NULL, &startupDiskFSRef, &startupDiskAlias);// 4```
```
        if (err == noErr)```
```
        {```
```
            err = AEBuildAppleEvent(// 5```
```
                    kAEMiscStandards,// 6```
```
                    kAEMakeObjectsVisible,// 7```
```
                    typeApplSignature,// 8```
```
                    &finderSignature,// 9```
```
                    sizeof(finderSignature),// 10```
```
                    kAutoGenerateReturnID, // 11```
```
                    kAnyTransactionID,// 12```
```
                    revealEvent,// 13```
```
                    NULL,// 14```
```
                    "'----':[alis(@@)]",// 15```
```
                    startupDiskAlias);// 16```
```
        }```
```
    }```
```
    else```
```
        err = memFullErr;// 17```
```
 ```
```
    return err;// 18```
```
}```
Hereâs a description of how theBuildRevealStartupDiskAEfunction works:
- It is passed a pointer to an Apple event data structure for the event to be created.
It is passed a pointer to an Apple event data structure for the event to be created.
- It callsCFURLCreateWithFileSystemPathto create aCFURLReffor the path to the startup disk, passing the constantstartupDiskPathdeclared inListing 6-3.
It callsCFURLCreateWithFileSystemPathto create aCFURLReffor the path to the startup disk, passing the constantstartupDiskPathdeclared inListing 6-3.
- It callsCFURLGetFSRefto get anFSReffile reference to the startup disk from theCFURLRef.
It callsCFURLGetFSRefto get anFSReffile reference to the startup disk from theCFURLRef.
- It callsFSNewAliasto convert theFSRefto an alias handle for the startup disk, to use in creating the Apple event.
It callsFSNewAliasto convert theFSRefto an alias handle for the startup disk, to use in creating the Apple event.
- It callsAEBuildAppleEventto create the Apple event. The next several items describe the parameters you pass to that function.
It callsAEBuildAppleEventto create the Apple event. The next several items describe the parameters you pass to that function.
- SpecifieskAEMiscStandards, a constant defined inAERegistry.h, for the event class.
SpecifieskAEMiscStandards, a constant defined inAERegistry.h, for the event class.
- SpecifieskAEMakeObjectsVisible, also defined inAERegistry.h, for the event ID.
SpecifieskAEMakeObjectsVisible, also defined inAERegistry.h, for the event ID.
- PassestypeApplSignatureto specify a target address type.
PassestypeApplSignatureto specify a target address type.
- PassesfinderSignature, defined inListing 6-3, to specify the application signature for the Finder.
PassesfinderSignature, defined inListing 6-3, to specify the application signature for the Finder.
- Passes the size of the application signature.
Passes the size of the application signature.
- Passes the Apple Event Manager constantkAutoGenerateReturnID, indicating the Apple Event Manager should set a return ID for the event. Your application can specify its own return ID, if needed.
Passes the Apple Event Manager constantkAutoGenerateReturnID, indicating the Apple Event Manager should set a return ID for the event. Your application can specify its own return ID, if needed.
- Passes the Apple Event Manager constantkAnyTransactionID, indicating the event is not part of a series of interdependent transactions.
Passes the Apple Event Manager constantkAnyTransactionID, indicating the event is not part of a series of interdependent transactions.
- Passes a pointer to the Apple event to be built.
Passes a pointer to the Apple event to be built.
- Passes a value ofNULL, indicating no error information is required.See Technical Note TN2106,AEBuild*, AEPrint*, and Friendsfor information on working with error information when usingAEBuildAppleEvent.
Passes a value ofNULL, indicating no error information is required.
See Technical Note TN2106,AEBuild*, AEPrint*, and Friendsfor information on working with error information when usingAEBuildAppleEvent.
- Passes a format string containing information for any attributes and parameters to add to the Apple event. In this case, there is just one parameter, an alias ('----').The identifier for the direct parameter in an Apple event is specified by the constantkeyDirectObject('----'). The minus sign has special meaning in AEBuild strings, so it should always be enclosed in single quotes when it is used to identify the direct parameter for an Apple event.
Passes a format string containing information for any attributes and parameters to add to the Apple event. In this case, there is just one parameter, an alias ('----').
The identifier for the direct parameter in an Apple event is specified by the constantkeyDirectObject('----'). The minus sign has special meaning in AEBuild strings, so it should always be enclosed in single quotes when it is used to identify the direct parameter for an Apple event.
- Passes the previously created alias handle as the data corresponding to the entry in the format string.
Passes the previously created alias handle as the data corresponding to the entry in the format string.
- In the case where the function could not create anFSRef, it sets a return error value.
In the case where the function could not create anFSRef, it sets a return error value.
- It returns a value indicating whether an error occurred.
It returns a value indicating whether an error occurred.
To see how theBuildRevealStartupDiskAEfunction is called, and how you can send the resulting Apple event, seeListing 6-7.

### Creating an Apple Event With AECreateAppleEvent
To create an Apple event withAECreateAppleEvent, you perform these steps:
- Prepare a target address descriptor, as described inCreating a Target Address Descriptor.
Prepare a target address descriptor, as described inCreating a Target Address Descriptor.
- CallAECreateAppleEventto create the Apple event, passing the event class, event ID, and other information.
CallAECreateAppleEventto create the Apple event, passing the event class, event ID, and other information.
- If necessary, call other Apple Event Manager functions to add additional information to the event, until it contains all the information required for the task you want to perform.
If necessary, call other Apple Event Manager functions to add additional information to the event, until it contains all the information required for the task you want to perform.
For example, suppose your application wants to send aquitApple event to another application. It might do this to terminate an application it launched previously, or perhaps to make sure an application is not running so it can perform an update.Listing 6-5shows how to create aquitapplication Apple event.
Listing 6-5Creating a quit Apple event with AECreateAppleEvent
```
AppleEvent someAE;```
```
 ```
```
err = AECreateAppleEvent(// 1```
```
        kCoreEventClass,// 2```
```
        kAEQuitApplication,// 3```
```
        &theTarget,// 4```
```
        kAutoGenerateReturnID,// 5```
```
        kAnyTransactionID,// 6```
```
        &someAE);// 7```
Hereâs how the code inListing 6-5works:
- It callsAECreateAppleEventto create the Apple event. The following items describe the parameters you pass to that function.
It callsAECreateAppleEventto create the Apple event. The following items describe the parameters you pass to that function.
- SpecifieskCoreEventClass, a constant defined inAppleEvents.h, for the event class.
SpecifieskCoreEventClass, a constant defined inAppleEvents.h, for the event class.
- SpecifieskAEQuitApplication, also defined inAppleEvents.h, for the event ID.
SpecifieskAEQuitApplication, also defined inAppleEvents.h, for the event ID.
- Passes the address of the previously constructed target address descriptor, which identifies the application to send thequitevent to.
Passes the address of the previously constructed target address descriptor, which identifies the application to send thequitevent to.
- Passes the Apple Event Manager constantkAutoGenerateReturnID, indicating the Apple Event Manager should set a return ID for the event. Your application can specify its own return ID, if needed.
Passes the Apple Event Manager constantkAutoGenerateReturnID, indicating the Apple Event Manager should set a return ID for the event. Your application can specify its own return ID, if needed.
- Passes the Apple Event Manager constantkAnyTransactionID, indicating the event is not part of a series of interdependent transactions.
Passes the Apple Event Manager constantkAnyTransactionID, indicating the event is not part of a series of interdependent transactions.
- It passes the address of an Apple event data structure for the event to be created.
It passes the address of an Apple event data structure for the event to be created.
Thatâs all you need to do to create aquitApple event. However, to create a more complicated Apple event, you typically need to add attributes or parameters to the event. For example, your application might receive aget dataApple event for which it returns some specified text as the direct parameter of the reply Apple event.Listing 6-6shows how to add such a direct parameter, using a previously defined function.
Listing 6-6Adding a direct parameter to an Apple event
```
OSErr anErr = AEPutParamString(// 1```
```
                    reply,// 2```
```
                    keyDirectObject,// 3```
```
                    textStringRef);// 4```
Hereâs how the code inListing 6-6works:
- It calls the application-defined functionAEPutParamString, shown inListing 5-3. The following items describe the parameters you pass to add a direct parameter to the Apple event.
It calls the application-defined functionAEPutParamString, shown inListing 5-3. The following items describe the parameters you pass to add a direct parameter to the Apple event.
- A pointer to the Apple event to add the parameter to.
A pointer to the Apple event to add the parameter to.
- An Apple Event Manager keyword constant specifying that the parameter is to be added as the direct parameter of the Apple event.
An Apple Event Manager keyword constant specifying that the parameter is to be added as the direct parameter of the Apple event.
- ACFStringRef, obtained prior to the call, that specifies the text for the direct parameter.
ACFStringRef, obtained prior to the call, that specifies the text for the direct parameter.
You can also use theAEBuildParametersfunction, introduced inTwo Approaches to Creating an Apple Event, to add more complicated attributes or parameters to an existing Apple event.

### Disposing of Apple Events You Create
Regardless of how you create an Apple event, your application is responsible for disposing of it with theAEDisposeDescfunction when you are finished with it. Your application must also dispose of all the descriptor records it creates when adding parameters and attributes to an Apple eventâremember, many Apple Event Manager functions make copies of descriptors and of their associated data, as noted inDisposing of Apple Event Data Structures.
You normally dispose of your Apple event and its reply, if any, after you send the event and receive a result (either fromAESendorAESendMessage). You should dispose of the data structures you created even if the sending function returns an error. If you are sending the event asynchronously, you need not wait for the reply Apple event before disposing of the sent Apple event.

## Sending an Apple Event
Once you have created an Apple event, the Apple Event Manager provides two choices for sending it. TheAESendfunction provides more options but higher overhead, while theAESendMessagefunction provides fewer options but less overhead.

### When to Use AESend
TheAESendfunction has parameters for specifying how to handle timeouts, idle processing, and event filtering. It requires your application to link with the entire Carbon framework, which brings in the HIToolbox framework and requires a connection to the window server.
UsingAESendis appropriate only for applications that require the use of idle processing and event filtering. This type of processing is not generally needed, or recommended, for applications that handle events with Carbon event handlers. Therefore, only Carbon applications that use older style event handling are likely to need to useAESend.
Note:If you callAESendand passNULLfor the filter and idle functions,AESendwill call through to the less expensiveAESendMessagefunction.
TheAESendfunction provides these parameters that are not available toAESendMessage:
This parameter is deprecated in Mac OS X.
A universal procedure pointer to a function that handles events (such as update, operating-system, activate, and null events) that your application receives while waiting for a reply. Your idle function can also perform other tasks (such as displaying a delay cursor) while waiting for a reply or a return receipt.
If your application specifies thekAEWaitReplyflag in thesendModeparameter and you wish your application to get periodic time while waiting for the reply to return, you must provide an idle function. Otherwise, you can pass a value ofNULLfor this parameter.
For advice on whether to use idle functions, seeSpecifying Send and Reply Options.
A universal procedure pointer to a function that determines which incoming Apple events should be received while the handler waits for a reply or a return receipt. If your application doesnât need to filter Apple events, you can pass a value ofNULLfor this parameter. If you do so, no application-oriented Apple events are processed while waiting.

### When to Use AESendMessage
TheAESendMessagefunction requires less overhead than theAESendfunction. It also allows you to send Apple events by linking with just the Application Services framework, and not the entire Carbon framework (and window server), as required byAESend.
Using theAESendMessagefunction is appropriate for applications that donât require idle processing and event filtering (most modern Carbon applications), and where any of the following applies:
- Efficiency is a key concern.
Efficiency is a key concern.
- The application has no user interface.
The application has no user interface.
- The application should not link with Carbon.
The application should not link with Carbon.

### Specifying Send and Reply Options
Regardless of which function you use to send Apple events, youâll need to specify certain options, such as how to interact with the user, whether you want a reply Apple event, and if so, how to receive it. You do this by setting flags in thesendModeparameter, present in bothAESendandAESendMessage. Hereâs a brief description of that parameter:
Specifies options for how the server application should handle the Apple event. To obtain a value for this parameter, you add together constants to set bits that specify the reply mode, the interaction level, and possibly flags for other options.
You can read a full description of all the constants for setting send mode flags in the constant section "AESendModeâ inApple Event Manager Reference. But here are some of the more common choices you might make for these flags.

#### Specifying a Reply in the Send Mode Parameter
If you do not want a reply to the Apple event you are sending, you specify thekAENoReplyflag in thesendModeparameter.
If youâre willing to wait a certain amount of time for a reply, specifykAEWaitReplyâthe function does not return until the timeout specified by thetimeoutInTicksparameter expires or the server application returns a reply. When the server application returns a reply, thereplyparameter contains the reply Apple event.
If you specify thekAEWaitReplyflag toAESend, you should provide an idle function to process any non-high-level events that occur while your application is waiting for a reply. You supply a pointer to your idle function as a parameter to theAESendfunction. So that your application can process other Apple events while it is waiting for a reply, you can also specify an optional filter function.
You don't provide an idle function or a  filter function when you call theAESendMessagefunction because it doesnât provide parameters for them. If you specifykAEWaitReplytoAESendMessage, it executes in such a way that any timers or event sources added to your run loop are not called while insideAESendMessage.
Rather than wait for a reply, you can send Apple events asynchronously and receive reply events when theyâre ready through normal event processing. To do this, you specify thekAEQueueReplyflag and register a handler for reply events with the event classkCoreEventClassand event IDkAEAnswer. Your application processes reply events in the same way it does other Apple events. This approach is recommended because it is far more efficient than waiting in an idle routine. In addition, it avoids the possibility of getting into odd states, such as loops within loops while waiting for replies as the idle routine processes events.
If you specifykAEWaitReplyorkAEQueueReply, the Apple Event Manager automatically passes a default reply Apple event to the server. The Apple Event Manager returns any nonzero result code from the serverâs handler in thekeyErrorNumberparameter of the reply Apple event. The server can return an error string in thekeyErrorStringparameter of the reply Apple event. The server can also use the reply Apple event to return any data you requestedâfor example, the results of a numeric calculation or a list of misspelled words.
If you specify thekAENoReplyflag, the reply Apple event passed to the server application consists of a null descriptor record.

#### Specifying User Interaction in the Send Mode Parameter
If your Apple event may require the user to interact with the server application (for example, to specify print or file options), you can communicate your user interaction preferences to the server by specifying additional flags in thesendModeparameter. These flags specify the conditions, if any, under which the server application can interact with the user and, if interaction is allowed, whether the server should come directly to the foreground or post a notification request.
The server application specifies its own preferences for user interaction by specifying flags to theAESetInteractionAllowedfunction, as described inInteracting With the User.

### Sending an Apple Event With AESend
Listing 6-7shows how you can build an Apple event withAEBuildAppleEventand send the event withAESend.
Listing 6-7Sending an Apple event with the AESend function
```
    OSErr err = noErr;```
```
    AppleEvent revealEvent;```
```
 ```
```
    err = BuildRevealStartupDiskAE(&revealEvent);// 1```
```
 ```
```
    if (err == noErr)```
```
    {```
```
        err = AESend(&revealEvent,// 2```
```
                    NULL,       // No reply event needed.// 3```
```
                    kAENoReply | kAECanInteract,// 4```
```
                    kAENormalPriority,// Normal priority.// 5```
```
                    kAEDefaultTimeout,// Let AE Mgr decide on timeout.// 6```
```
                    NULL,           // No idle function.// 7```
```
                    NULL);          // No filter function.// 8```
```
 ```
```
        err = AEDisposeDesc(&revealEvent);// 9```
```
    }```
Hereâs how the code inListing 6-7works:
- Calls the application-defined functionBuildRevealStartupDiskAE, shown inListing 6-4, to build an Apple event that tells the Finder to reveal the startup disk.
Calls the application-defined functionBuildRevealStartupDiskAE, shown inListing 6-4, to build an Apple event that tells the Finder to reveal the startup disk.
- Calls the functionAESend, passing the Apple event obtained by the previous function call. The next several items describe the remaining parameters you pass to theAESendfunction.
Calls the functionAESend, passing the Apple event obtained by the previous function call. The next several items describe the remaining parameters you pass to theAESendfunction.
- PassesNULLfor the reply event because no reply is expected.
PassesNULLfor the reply event because no reply is expected.
- Passes a logical combination of constants indicating that no reply is expected and that interaction with the user is allowed (although none is likely for this event).In the case where your application wants an asynchronous reply and does not allow interaction, you would passkAEQueueReply | kAENeverInteract.
Passes a logical combination of constants indicating that no reply is expected and that interaction with the user is allowed (although none is likely for this event).
In the case where your application wants an asynchronous reply and does not allow interaction, you would passkAEQueueReply | kAENeverInteract.
- Passes a constant indicating the event should have normal priority. However, priority is ignored on Mac OS X.
Passes a constant indicating the event should have normal priority. However, priority is ignored on Mac OS X.
- Passes a constant indicating the Apple Event Manager should use the default timeout length (usually about thirty seconds). You can, instead, pass a specific value for the number of ticks (sixtieths of a second) to delay.
Passes a constant indicating the Apple Event Manager should use the default timeout length (usually about thirty seconds). You can, instead, pass a specific value for the number of ticks (sixtieths of a second) to delay.
- PassesNULL, indicating it will not use an idle function (needed only in specific cases where your application waits for a reply).
PassesNULL, indicating it will not use an idle function (needed only in specific cases where your application waits for a reply).
- PassesNULL, indicating it will not use a filter function (needed, in conjunction with an idle function, only in specific cases where your application waits for a reply).
PassesNULL, indicating it will not use a filter function (needed, in conjunction with an idle function, only in specific cases where your application waits for a reply).
- CallsAEDisposeDescto dispose of the Apple event.In cases where you expect a reply Apple event, your application should dispose of that event as well, once it is finished with it. If the reply is handled asynchronously, dispose of the reply event in the reply handler.
CallsAEDisposeDescto dispose of the Apple event.
In cases where you expect a reply Apple event, your application should dispose of that event as well, once it is finished with it. If the reply is handled asynchronously, dispose of the reply event in the reply handler.
In this example, the call toAESenddoes not supply an idle function or a filter function. As a result,AESendwill fall through and call theAESendMessagefunction, which has less overhead. When you donât require idle and filter functions, you can, of course, callAESendMessagedirectly, as described in the next section.
As noted inSpecifying a Reply in the Send Mode Parameter, even in the case where your application expects a delayed reply to an Apple event it sends, the most efficient mechanism is to ask for queued replies and register a handler to receive them.

### Sending an Apple Event With AESendMessage
Listing 6-8shows how you can send an Apple event withAESendMessage.
Listing 6-8Sending an Apple event with the AESendMessage function
```
    OSErr err = noErr;```
```
    AppleEvent revealEvent;```
```
 ```
```
    err = BuildRevealStartupDiskAE(&revealEvent);// 1```
```
 ```
```
    if (err == noErr)```
```
    {```
```
        err = AESendMessage(&revealEvent,// 2```
```
                    NULL,// 3```
```
                    kAENoReply | kAENeverInteract,// 4```
```
                    kAEDefaultTimeout);// 5```
```
 ```
```
        err = AEDisposeDesc(&revealEvent);// 6```
```
    }```
Hereâs how the code inListing 6-7works:
- Calls the application-defined functionBuildRevealStartupDiskAE, shown inListing 6-4, to build an Apple event that tells the Finder to reveal the startup disk.
Calls the application-defined functionBuildRevealStartupDiskAE, shown inListing 6-4, to build an Apple event that tells the Finder to reveal the startup disk.
- Calls the functionAESendMessage, passing the Apple event obtained by the previous function call. The next several items describe the remaining parameters you pass to theAESendMessagefunction.
Calls the functionAESendMessage, passing the Apple event obtained by the previous function call. The next several items describe the remaining parameters you pass to theAESendMessagefunction.
- PassesNULLfor the reply event because no reply is expected.
PassesNULLfor the reply event because no reply is expected.
- Passes a logical combination of constants indicating that no reply is expected and that interaction with the user is not allowed.
Passes a logical combination of constants indicating that no reply is expected and that interaction with the user is not allowed.
- Passes a constant indicating the Apple Event Manager should use the default timeout length (usually about thirty seconds). You can, instead, pass a specific value for the number of ticks (sixtieths of a second) to delay.
Passes a constant indicating the Apple Event Manager should use the default timeout length (usually about thirty seconds). You can, instead, pass a specific value for the number of ticks (sixtieths of a second) to delay.
- CallsAEDisposeDescto dispose of the Apple event.
CallsAEDisposeDescto dispose of the Apple event.

## Handling a Reply Apple Event
When your application receives a reply event, either as a return parameter from the sending routine or in a return event handler, it uses Apple Event Manager functions to extract the information it needs from the event. This process is the same as the one described inResponding to Apple Events.
Whenever a server application provides an error string parameter in a reply event, it should also provide an error number. However, you canât count on all server applications to do so. A client application should therefore check for both thekeyErrorNumber(for example, seeListing 5-2) andkeyErrorStringparameters before assuming that no error has occurred.
When your application has finished using the reply Apple event, it should dispose of it by calling theAEDisposeDescfunction. The Apple Event Manager takes care of disposing of both the Apple event and the reply Apple event after a server applicationâs handler returns, but the server is responsible for disposing of any data structures it creates while extracting data from the event.
Copyright © 2005, 2007 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2007-10-31