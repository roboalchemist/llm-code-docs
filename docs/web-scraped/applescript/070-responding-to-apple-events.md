# Responding to Apple Events

# Retired Document
Important:This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

# Responding to Apple Events
Your application must be able to respond to certain Apple events sent by the Mac OS, such as theopen applicationandquitevents. If your application has defined additional Apple events that it supports, either to supply services to other applications or to make itself scriptable, it must be ready to respond to those events as well.
This chapter describes how you write handlers to respond to the Apple events your application receives. It also provides an overview of how Carbon applications work with Apple events sent by the Mac OS.

## About Apple Event Handlers
To respond to Apple events, your application registers handler functions with the Apple Event Manager for the events it can handle, as described inApple Event Dispatching. Your application will only receive Apple events that target itâthat is, events that specify your application in their target address descriptor. These include the events described inHandling Apple Events Sent by the Mac OS. Should your application receive an Apple event it is not expecting, the Apple Event Manager will not find it in your dispatch table, so the event will not be dispatched to one of your handlers, unless you have installed a wildcard handler.
Note:One exception is the case where an event handler is installed automatically for your application. For example,Processing Apple Events With the Carbon Event Modeldescribes a case in which a systemquitevent handler is installed automatically.
As a result, your event handlers should generally be called only for events they understand. If a problem occurs, it is most commonly due to an error in constructing the event that was sent to your application. Because of this possibility, you may want to test the error handling in your Apple event code by intentionally sending your application Apple events containing unexpected information.

### Definition of an Apple Event Handler
When you declare an Apple event handler, the syntax must match theAEEventHandlerProcPtrdata type, which is described in detail inApple Event Manager Reference.Listing 5-1shows the declaration for a function that handles theopen documentsApple eventâall your handler declarations use a similar declaration.
Listing 5-1Definition for an Apple event handler
```
static pascal OSErr HandleOpenDocAE (// 1```
```
    const AppleEvent * theAppleEvent,// 2```
```
    AppleEvent * reply,// 3```
```
    SInt32 handlerRefcon);// 4```
Hereâs a description of this function declaration:
- Thepascalkeyword ensures proper ordering of parameters on the stack.
Thepascalkeyword ensures proper ordering of parameters on the stack.
- The Apple event for the function to handle. Youâll often extract information from it to help you process the Apple event.
The Apple event for the function to handle. Youâll often extract information from it to help you process the Apple event.
- The default reply (provided by the Apple Event Manager). It contains no parameters. If no reply is requested, the reply event is a null descriptor.
The default reply (provided by the Apple Event Manager). It contains no parameters. If no reply is requested, the reply event is a null descriptor.
- The 32-bit reference constant you supplied for the handler when you first registered it by callingAEInstallEventHandler. You can use the reference constant to provide information about the Apple event, or for any other purpose you want.For example, you can install, for multiple Apple events, dispatch table entries that specify the same handler but different reference constants. Your handler can then use the reference constant to distinguish between the different Apple events it receives.
The 32-bit reference constant you supplied for the handler when you first registered it by callingAEInstallEventHandler. You can use the reference constant to provide information about the Apple event, or for any other purpose you want.
For example, you can install, for multiple Apple events, dispatch table entries that specify the same handler but different reference constants. Your handler can then use the reference constant to distinguish between the different Apple events it receives.

### Interacting With the User
When your application handles an Apple event, it may need to interact with the user. For example, your handler for theprint documentsevent may need to display a print dialog before printing. Your application should not just assume it is okay to interact with the user in response to an Apple event. It should always call theAEInteractWithUserfunction to make sure it is in the foreground before it interacts with the user.
IfAEInteractWithUserreturns the valuenoErr, then your application is currently in front and is free to interact with the user. IfAEInteractWithUserreturns the valueerrAENoUserInteraction, your application should not attempt to interact with the user.
You can specify flags to theAESetInteractionAllowedfunction to allow the following types of interaction with your application:
- Only when your application is sending an Apple event to itself.
Only when your application is sending an Apple event to itself.
- Only when the client application is on the same computer as your application.
Only when the client application is on the same computer as your application.
- For any event sent by any client application on any computer.
For any event sent by any client application on any computer.
Both client and server applications specify their preferences for user interaction: the client specifies whether the server should be allowed to interact with the user, and the server (your application) specifies when it allows user interaction while processing an Apple event. For interaction to take place, these two conditions must be met:
- The client application must set flags in thesendModeparameter of theAESendfunction indicating that user interaction is allowed.
The client application must set flags in thesendModeparameter of theAESendfunction indicating that user interaction is allowed.
- The server application must either set no user interaction preferences, in which case it is assumed that only interaction with a client on the local computer is allowed; or it must use theAESetInteractionAllowedfunction to indicate that user interaction is allowed.
The server application must either set no user interaction preferences, in which case it is assumed that only interaction with a client on the local computer is allowed; or it must use theAESetInteractionAllowedfunction to indicate that user interaction is allowed.
If these two conditions are met and ifAEInteractWithUserdetermines that both the client and server applications allow user interaction under the current circumstances,AEInteractWithUserbrings your application to the foreground if it isnât already in the foreground. Your application can then display a dialog or otherwise interact with the user. TheAEInteractWithUserfunction brings your server application to the front either directly or after the user responds to a notification request.
Important:CallingAEInteractWithUserensures that your application will get correct notification in terms of being activated. There is no guarantee that other applications are setting an interaction level, but if they are, your application can respect it.
Interaction is not currently guaranteed to work correctly in the context of fast user switching. For example, your application could ask the user whether it should present UI, but the user might never respond because your application has been switched out.
To track when your Carbon or Cocoa application has been switched in or out, you can sign up for notification of thekEventSystemUserSessionActivatedandkEventSystemUserSessionDeactivatedevents, as described inUser Switch NotificationsinMultiple User Environment Programming Topics.
To determine whether your application is currently running in the active user session, you can use theCGSessionCopyCurrentDictionaryfunction, together with thekCGSessionOnConsoleKey, as described inSupporting Fast User SwitchinginMultiple User Environment Programming Topics.
For more information on working with user interaction, seeSpecifying Send and Reply Optionsin this document, as well as the following inApple Event Manager Reference:
- The section "User Interaction Level Constants.â
The section "User Interaction Level Constants.â
- The constants listed under âAESendMode.â
The constants listed under âAESendMode.â
- The functionsAEInteractWithUser,AESetInteractionAllowed,AEGetInteractionAllowed, andAESend.
The functionsAEInteractWithUser,AESetInteractionAllowed,AEGetInteractionAllowed, andAESend.

## Writing an Apple Event Handler
Your Apple event handler typically performs the following operations:
- It extracts information from the received Apple event.
It extracts information from the received Apple event.
- It performs any requested actions, checking that interaction is allowed before attempting to interact with a user.
It performs any requested actions, checking that interaction is allowed before attempting to interact with a user.
- It adds information to the reply Apple event if appropriate.
It adds information to the reply Apple event if appropriate.
- It returns a result code. If an error occurs in extracting information from the event or if an error occurs in any other operation:It may add error information to the reply Apple event.It returns an appropriate error code.
It returns a result code. If an error occurs in extracting information from the event or if an error occurs in any other operation:
- It may add error information to the reply Apple event.
It may add error information to the reply Apple event.
- It returns an appropriate error code.
It returns an appropriate error code.

### Extracting Information From the Apple Event
For nearly all standard Apple events, your handler extracts data from the event to help determine how to process the event. The following are some kinds of information you are likely to extract:
- The event class and/or the event ID. For example, if you registered your handler with one or more wildcards, you may need to get the event class or event ID to determine which kind of event you actually received. You can obtain this information by calling a function such asAEGetAttributePtr, and passingkeyEventClassAttrorkeyEventIDAttrfor the parameter that specifies the keyword of the attribute to access.
The event class and/or the event ID. For example, if you registered your handler with one or more wildcards, you may need to get the event class or event ID to determine which kind of event you actually received. You can obtain this information by calling a function such asAEGetAttributePtr, and passingkeyEventClassAttrorkeyEventIDAttrfor the parameter that specifies the keyword of the attribute to access.
- The direct parameter, which usually specifies the data to be acted upon.Listing 4-5shows how to get a parameter that contains a list of files from anopen documentsApple event.
The direct parameter, which usually specifies the data to be acted upon.Listing 4-5shows how to get a parameter that contains a list of files from anopen documentsApple event.
- Additional parameters. These can be any kind of data stored in an Apple event. They might include object specifiers, which identify objects within your application on which the Apple event operates. For information on how to work with object specifiers, seeâResolving and Creating Object Specifier RecordsâinInside Macintosh: Interapplication Communication.
Additional parameters. These can be any kind of data stored in an Apple event. They might include object specifiers, which identify objects within your application on which the Apple event operates. For information on how to work with object specifiers, seeâResolving and Creating Object Specifier RecordsâinInside Macintosh: Interapplication Communication.
Working With the Data in an Apple Eventprovides additional information and examples of how you extract data from an Apple event.

### Performing the Requested Action
When your application responds to an Apple event, it should perform the standard action requested by that event. For example, your application should respond to theprint documentsevent by printing the specified documents.
Many Apple events can ask your application to return data. For instance, if your application is a spelling checker, the client application might expect your application to return data in the form of a list of misspelled words.

### Adding Information to a Reply Apple Event
If the application that sent the Apple event requested a reply, the Apple Event Manager passes a default reply Apple event to your handler. The reply event has event classkCoreEventClassand event IDkAEAnswer. If the client application does not request a reply, the Apple Event Manager passes a null descriptor insteadâthat is, a descriptor of typetypeNullwhose data handle has the valueNULL.
The default reply Apple event has no parameters, but your handler can add parameters or attributes to it. If your application is a spelling checker, for example, you can return a list of misspelled words in a parameter. However, your handler should check whether the reply Apple event exists before attempting to add to it. Attempting to add to a null descriptor generates an error.
Your handler may need to add error information to the reply event, as described in subsequent sections.

### Returning a Result Code
When your handler finishes processing an Apple event, it should dispose of any Apple event descriptors or other data it has acquired. It should then return a result code to the Apple Event Manager. Your handler should returnnoErrif it successfully handles the Apple event or a nonzero result code if an error occurs.
If an error occurs because your application cannot understand the event, it should returnerrAEEventNotHandled. This allows the Apple Event Manager to look for a handler in the system dispatch table that might be able to handle the event. If the error occurs because the event is impossible to handle as specified, return the result code returned by whatever function caused the failure, or whatever other result code is appropriate.
For example, suppose your application receives aget dataevent requesting the name of the current printer, but it cannot handle such an event. In this situation, you can returnerrAEEventNotHandledin case another available handler can handle theget dataevent. However, this strategy is only useful if your application has installed such a system handler, or the event is one of the few for which a system handler may be installed automatically. (For information on handlers that are installed automatically, seeHandling Apple Events Sent by the Mac OS.)
However, if your application cannot handle aget dataevent that requests the fifth paragraph in a document because the document contains only four paragraphs, you should return some other nonzero error, because further attempts to handle the event are pointless.
In addition to returning a result code, your handler can also return an error string by adding akeyErrorStringparameter to the reply Apple event. The client can use this string in an error message to the user. For more information, seeReturning Error Information.
For scriptable applications, the client is often the Script Editor, or some other application, executing a script. When you return an error code that the Apple Event Manager understands, the Script Editor automatically displays an appropriate error message to the user. You can find tables of error codes documented inApple Event Manager ReferenceandOpen Scripting Architecture Reference.

### Returning Error Information
If your handler returns a nonzero result code, the Apple Event Manager adds akeyErrorNumberparameter to the reply Apple event (unless you have already added akeyErrorNumberparameter). This parameter contains the result code that your handler returns. This can be useful because it associates the error number directly with the return event, which the client application may pass around without the result code.
Rather than just returning an error code, your handler itself can add error information to the reply Apple event. It can add both an error number and an error string. As noted previously, in many cases returning an Apple Event Manager error code will result in an appropriate error message. You should only add your own error text in cases where you can provide information the Apple Event Manager cannot, such as information specific to the operation of your application.
Note:Handlers can return several additional types of error information. For details, see theOSAScriptErrorfunction and the constant section âOSAScriptError Selectorsâ inOpen Scripting Architecture Reference.
To directly add an error number parameter to a reply Apple event, your handler can call a function like the one inListing 5-2.
Listing 5-2A function to add an error number to a reply Apple event
```
static void AddErrNumberToEvent(OSStatus err, AppleEvent* reply)// 1```
```
{```
```
    OSStatus returnVal = errAEEventFailed;// 2```
```
 ```
```
    if (reply->descriptorType != typeNull)// 3```
```
    {```
```
        returnVal = AESizeOfParam(reply, keyErrorNumber, NULL, NULL);```
```
        if (returnVal != noErr))// 4```
```
        {```
```
            AEPutParamPtr(reply, keyErrorNumber,```
```
                        typeSInt32, &err, sizeof(err));// 5```
```
        }```
```
    }```
```
    return returnVal;```
```
}```
Hereâs a description of how this function works:
- It receives an error number and a pointer to the reply Apple event to modify.
It receives an error number and a pointer to the reply Apple event to modify.
- It declares a variable for the return value and sets it to the Apple Event Manager error constant for âApple event handler failed.â If the function is successful, this value is changed.
It declares a variable for the return value and sets it to the Apple Event Manager error constant for âApple event handler failed.â If the function is successful, this value is changed.
- It checks the descriptor type of the reply Apple event to make sure it is not a null event.
It checks the descriptor type of the reply Apple event to make sure it is not a null event.
- It verifies that the event doesnât already contain an error number parameter (AESizeOfParamreturns an error if it doesnât find the parameter).
It verifies that the event doesnât already contain an error number parameter (AESizeOfParamreturns an error if it doesnât find the parameter).
- It callsAEPutParamPtrto add an error number parameter to the reply event:keyErrorNumberspecifies the keyword for the added parameter.typeSInt32specifies the descriptor type for the added parameter.errspecifies the error number to store in the added parameter.
It callsAEPutParamPtrto add an error number parameter to the reply event:
- keyErrorNumberspecifies the keyword for the added parameter.
keyErrorNumberspecifies the keyword for the added parameter.
- typeSInt32specifies the descriptor type for the added parameter.
typeSInt32specifies the descriptor type for the added parameter.
- errspecifies the error number to store in the added parameter.
errspecifies the error number to store in the added parameter.
In addition to returning a result code, your handler can return an error string in thekeyErrorStringparameter of the reply Apple event. Your handler should provide meaningful text in thekeyErrorStringparameter, so that the client can display this string to the user if desired.
Listing 5-3shows a function that adds a parameter, from a string reference that refers to Unicode text, to a passed descriptor. You pass the desired keyword to identify the parameter to add. TheAEPutParamStringfunction callsAEPutParamPtr, which adds a parameter to an Apple event record or an Apple event, so those are the types of descriptors you should pass to it. (Descriptors, Descriptor Lists, and Apple Eventsdescribes the inheritance relationship between common Apple event data types.)
Listing 5-3A function that adds a string parameter to a descriptor
```
OSErr AEPutParamString(AppleEvent *event,```
```
                    AEKeyword keyword, CFStringRef stringRef)// 1```
```
{```
```
    UInt8 *textBuf;```
```
    CFIndex length, maxBytes, actualBytes;```
```
 ```
```
    length = CFStringGetLength(stringRef);// 2```
```
 ```
```
    maxBytes = CFStringGetMaximumSizeForEncoding(length,```
```
                                    kCFStringEncodingUTF8);// 3```
```
    textBuf = malloc(maxBytes);// 4```
```
    if (textBuf)```
```
    {```
```
        CFStringGetBytes(stringRef, CFRangeMake(0, length),```
```
                kCFStringEncodingUTF8, 0, true,```
```
                (UInt8 *) textBuf, maxBytes, &actualBytes);// 5```
```
 ```
```
        OSErr err = AEPutParamPtr(event, keyword,```
```
                typeUTF8Text, textBuf, actualBytes);// 6```
```
 ```
```
        free(textBuf);// 7```
```
        return err;```
```
    }```
```
    else```
```
        return memFullErr;```
```
}```
Hereâs a description of how this function works:
- It receives a pointer to a descriptor to add a parameter to, a key word to identify the parameter, and a string reference from which to obtain the text for the parameter.
It receives a pointer to a descriptor to add a parameter to, a key word to identify the parameter, and a string reference from which to obtain the text for the parameter.
- It gets the length of the string from the passed reference.
It gets the length of the string from the passed reference.
- It determines the maximum number of bytes needed to store the text, based on its encoding.
It determines the maximum number of bytes needed to store the text, based on its encoding.
- It allocates a buffer of that size.
It allocates a buffer of that size.
- It gets the text from the string reference.
It gets the text from the string reference.
- It adds the text as a parameter to the passed descriptor. (If called with the keywordkeyErrorString, for example, it adds an error string parameter.)
It adds the text as a parameter to the passed descriptor. (If called with the keywordkeyErrorString, for example, it adds an error string parameter.)
- It frees its local buffer.
It frees its local buffer.
Listing 5-4shows how you could callAEPutParamStringto add an error string to a reply Apple event.
Listing 5-4Adding an error string to an Apple event with AEPutParamString
```
CFStringRef errStringRef = getLocalizedErrMsgForErrNumber(err);```
```
OSErr anErr = AEPutParamString(reply, keyErrorString, errStringRef);```
Hereâs a description of how this code snippet works:
- It calls an application-defined function to obtain a localized error message as a string reference, based on a passed error number. (For information on localized strings, seeWorking With Localized StringsinBundle Programming Guide.)
It calls an application-defined function to obtain a localized error message as a string reference, based on a passed error number. (For information on localized strings, seeWorking With Localized StringsinBundle Programming Guide.)
- It callsAEPutParamString, passing the event (obtained previously) to add the error text to, the error string keyword, and the string reference for the error message text.
It callsAEPutParamString, passing the event (obtained previously) to add the error text to, the error string keyword, and the string reference for the error message text.

### A Handler for the Open Documents Apple Event
Listing 5-5shows a handler that responds to theopen documentsApple event.
Listing 5-5An Apple event handler for the open documents event
```
static pascal OSErrOpenDocumentsAE(const AppleEvent *theAppleEvent, AppleEvent *reply, long handlerRefcon)```
```
{```
```
    AEDescList  docList;```
```
    FSRef       theFSRef;```
```
    long        index;```
```
    long        count = 0;```
```
    OSErr       err = AEGetParamDesc(theAppleEvent,```
```
                            keyDirectObject, typeAEList, &docList);// 1```
```
    require_noerr(err, CantGetDocList);// 2```
```
 ```
```
    err = AECountItems(&docList, &count);// 3```
```
    require_noerr(err, CantGetCount);```
```
 ```
```
    for(index = 1; index <= count; index++)// 4```
```
    {```
```
        err = AEGetNthPtr(&docList, index, typeFSRef,```
```
                        NULL, NULL, &theFSRef, sizeof(FSRef), NULL);// 5```
```
        require_noerr(err, CantGetDocDescPtr);```
```
 ```
```
        err = OpenDocument(&theFSRef);// 6```
```
    }```
```
    AEDisposeDesc(&docList);// 7```
```
 ```
```
CantGetDocList:```
```
CantGetCount:```
```
CantGetDocDescPtr:```
```
    if (err != noErr)// 8```
```
    {```
```
        // For handlers that expect a reply, add error information here.```
```
    }```
```
    return(err);// 9```
```
}```
Hereâs a description of how thisopen documentshandler works:
- It calls an Apple Event Manager function (AEGetParamDesc) to obtain a descriptor list from the direct object of the received Apple event. This is a list of file aliases, one for each document to open.
It calls an Apple Event Manager function (AEGetParamDesc) to obtain a descriptor list from the direct object of the received Apple event. This is a list of file aliases, one for each document to open.
- It uses therequire_noerrmacro (defined inAssertMacros.h) to jump to a labeled location as a simple form of error handling.
It uses therequire_noerrmacro (defined inAssertMacros.h) to jump to a labeled location as a simple form of error handling.
- It calls an Apple Event Manager function (AECountItems) to obtain the number of items in the descriptor list.
It calls an Apple Event Manager function (AECountItems) to obtain the number of items in the descriptor list.
- It sets up a loop over the items in the descriptor list.
It sets up a loop over the items in the descriptor list.
- It calls an Apple Event Manager function (AEGetNthPtr) to get an item from the list, by index, asking for a type oftypeFSRef. This causes the function to coerce the retrieved item (a file alias) to the requested type.
It calls an Apple Event Manager function (AEGetNthPtr) to get an item from the list, by index, asking for a type oftypeFSRef. This causes the function to coerce the retrieved item (a file alias) to the requested type.
- It calls a function you have written (OpenDocument) to open the current document from the list.Aprint documentsevent handler would be very similar to this one, but in this step could call yourPrintDocumentfunction.
It calls a function you have written (OpenDocument) to open the current document from the list.
Aprint documentsevent handler would be very similar to this one, but in this step could call yourPrintDocumentfunction.
- It disposes of the document list descriptor.
It disposes of the document list descriptor.
- Theopen documentsevent sent by the Mac OS doesnât expect a reply, so thereplyparameter is a null event. For event handlers that expect a reply, this is where you can use the techniques described earlier in this chapter to add an error number or an error string. Some examples of events that expect a reply (and thus supply a non-null reply event) includeget dataevents andquitevents.
Theopen documentsevent sent by the Mac OS doesnât expect a reply, so thereplyparameter is a null event. For event handlers that expect a reply, this is where you can use the techniques described earlier in this chapter to add an error number or an error string. Some examples of events that expect a reply (and thus supply a non-null reply event) includeget dataevents andquitevents.
- It returns an error code (noErrif no error has occurred).
It returns an error code (noErrif no error has occurred).
As an alternative to code shown in this handler, you might use an approach that extracts the document list in the event handler, then passes it to a separate function,OpenDocuments, to iterate over the items in the list. This has the advantage that you can also call theOpenDocumentsfunction with the document list obtained fromNavDialogGetReplywhen you are working with Navigation Services. Theselectionfield of the returnedNavReplyRecordis a descriptor list like the one described above.

## Handling Apple Events Sent by the Mac OS
Mac OS X sends Apple events to communicate with applications in certain common situations, such as when launching the application or asking it to open a list of documents. These events are sometimes referred to as the ârequiredâ events, although applications are not required to support all of them. For example, if your application isnât document-based, it wonât support theopen documentsorprint documentsevents. However, any application that presents a graphical user interface through the Human Interface Toolbox or the Cocoa application framework should respond to as many of these events as it makes sense for that application to support.
Carbon applications typically install Apple event handlers to handle these events, though in some cases a default handler may be installed automatically (as described inCommon Apple Events Sent by the Mac OS).
For Cocoa applications, most of the work of responding to events sent by the Mac OS happens automatically, though in some cases applications may want to step in and modify the default behavior. For more details, including some information of general interest, seeHow Cocoa Applications Handle Apple EventsinCocoa Scripting Guide.

### Common Apple Events Sent by the Mac OS
The following are Apple events your application is likely to receive from the Mac OS. For information on the constants associated with these events, seeEvent ID Constants for Apple Events Sent by the Mac OS.
- open application(orlaunch)Received when your application is launched. The application should perform any tasks required when a user launches it without opening or printing any existing documents, though it may of course open a new, untitled document.Starting in Mac OS X version 10.4, anopen applicationApple event may contain information about whether the application was launched as a login item or as a service item. For details on working with this kind of information, see âLaunch Apple Event Constantsâ in âApple Event Manager Constantsâ inApple Event Manager Reference.
open application(orlaunch)
Received when your application is launched. The application should perform any tasks required when a user launches it without opening or printing any existing documents, though it may of course open a new, untitled document.
Starting in Mac OS X version 10.4, anopen applicationApple event may contain information about whether the application was launched as a login item or as a service item. For details on working with this kind of information, see âLaunch Apple Event Constantsâ in âApple Event Manager Constantsâ inApple Event Manager Reference.
- reopen applicationReceived when the application is reopenedâfor example, when the application is open but not frontmost, and the user clicks its icon in the Dock. The application should perform appropriate tasksâfor example, it might create a new document if none is open.
reopen application
Received when the application is reopenedâfor example, when the application is open but not frontmost, and the user clicks its icon in the Dock. The application should perform appropriate tasksâfor example, it might create a new document if none is open.
- open documentsReceived with a list of documents for the application to open.Listing 5-5shows a complete Apple event handler for this event.Starting in Mac OS X version 10.4, theopen documentsApple event may contain an optional parameter identified by the keykeyAESearchText. If present, the parameter contains the search text from the Spotlight search that identified the documents to be opened. The application should make a reasonable effort to display an occurrence of the search text in each opened documentâfor example by scrolling text into view that contains all or part of the search text.
open documents
Received with a list of documents for the application to open.Listing 5-5shows a complete Apple event handler for this event.
Starting in Mac OS X version 10.4, theopen documentsApple event may contain an optional parameter identified by the keykeyAESearchText. If present, the parameter contains the search text from the Spotlight search that identified the documents to be opened. The application should make a reasonable effort to display an occurrence of the search text in each opened documentâfor example by scrolling text into view that contains all or part of the search text.
- print documentsReceived with a list of documents for the application to print. You can obtain file system references to the items in the list using code like that you use when handling anopen documentsevent. SeeInteracting With the Userfor information on when it is appropriate to display a dialog or perform other interaction.Starting in Mac OS X version 10.3, the print documents event was extended to include an optionalprint settingsparameter that defines the settings for the print job or jobs, and an optionalprint dialogparameter that specifies whether the application should display the Print dialog. By default, the application should not show the Print dialog if the caller doesn't specify a print dialog parameter. For details, see Technical Note TN2082,The Enhanced Print Apple Event.
print documents
Received with a list of documents for the application to print. You can obtain file system references to the items in the list using code like that you use when handling anopen documentsevent. SeeInteracting With the Userfor information on when it is appropriate to display a dialog or perform other interaction.
Starting in Mac OS X version 10.3, the print documents event was extended to include an optionalprint settingsparameter that defines the settings for the print job or jobs, and an optionalprint dialogparameter that specifies whether the application should display the Print dialog. By default, the application should not show the Print dialog if the caller doesn't specify a print dialog parameter. For details, see Technical Note TN2082,The Enhanced Print Apple Event.
- open contentsAvailable starting in Mac OS X version 10.4. Received when content, such as text or an image, is dropped on the application iconâfor example, when a dragged image is dropped on the icon in the Dock.The structure of this event is very similar to theopen documentsevent. The direct object parameter consists of a list of content data items to be opened. ThedescriptorTypefor each item in the list indicates the type of the content ('PICT','TIFF','utf8', and so on).The application should use the content in an appropriate wayâfor example, if a document is open, it might insert the content at the current insertion point; if no document is open, it might open a new document and insert the provided text or image.If your Carbon application provides a service that can accept the type of data in anopen contentsApple event it receives, you can handle the event without even installing an event handler for itâa default handler will be installed, if one isnât present, and invoked automatically. As a result, your service provider will receive a{kEventClassService, kEventServicePerform}Carbon event.Because there is no way to return data from anopen contentsApple event, the default handler only invokes a service that accepts the given data type but returns nothing.If your application doesnât support services, or if you want to provide special handling for theopen contentsApple event, your application can install a handler for the event.For information on working with services, seeSetting Up Your Carbon Application to Use the Services Menu.
open contents
Available starting in Mac OS X version 10.4. Received when content, such as text or an image, is dropped on the application iconâfor example, when a dragged image is dropped on the icon in the Dock.
The structure of this event is very similar to theopen documentsevent. The direct object parameter consists of a list of content data items to be opened. ThedescriptorTypefor each item in the list indicates the type of the content ('PICT','TIFF','utf8', and so on).
The application should use the content in an appropriate wayâfor example, if a document is open, it might insert the content at the current insertion point; if no document is open, it might open a new document and insert the provided text or image.
If your Carbon application provides a service that can accept the type of data in anopen contentsApple event it receives, you can handle the event without even installing an event handler for itâa default handler will be installed, if one isnât present, and invoked automatically. As a result, your service provider will receive a{kEventClassService, kEventServicePerform}Carbon event.
Because there is no way to return data from anopen contentsApple event, the default handler only invokes a service that accepts the given data type but returns nothing.
If your application doesnât support services, or if you want to provide special handling for theopen contentsApple event, your application can install a handler for the event.
For information on working with services, seeSetting Up Your Carbon Application to Use the Services Menu.
- quit applicationReceived when the application should quit. The application can perform any special operations required at that time.If your application callsRunApplicationEventLoop, a simplequithandler is installed automatically. If you install your own handler, it can perform any required operations, then returnerrAEEventNotHandledso that the default handler continues quitting the application. If you return another error value, the application will not quit. However, yourquithandler can callQuitApplicationEventLoop, which causesRunApplicationEventLoopto quit and return back tomain(). In that case you can returnnoErrfrom your handler instead oferrAEEventNotHandled.If your application does not callRunApplicationEventLoop, you should supply your ownquithandler.You should not terminate your application from within aquitevent handler. Instead, you should set a flag that you check outside the handler.
quit application
Received when the application should quit. The application can perform any special operations required at that time.
If your application callsRunApplicationEventLoop, a simplequithandler is installed automatically. If you install your own handler, it can perform any required operations, then returnerrAEEventNotHandledso that the default handler continues quitting the application. If you return another error value, the application will not quit. However, yourquithandler can callQuitApplicationEventLoop, which causesRunApplicationEventLoopto quit and return back tomain(). In that case you can returnnoErrfrom your handler instead oferrAEEventNotHandled.
If your application does not callRunApplicationEventLoop, you should supply your ownquithandler.
You should not terminate your application from within aquitevent handler. Instead, you should set a flag that you check outside the handler.
- show preferencesReceived when the user chooses the Preferences menu item. Carbon applications that handle the Preferences command can install an Apple event handler for this event, but they more commonly install a Carbon event handler forkEventCommandProcessand check for thekHICommandPreferencescommand ID.
show preferences
Received when the user chooses the Preferences menu item. Carbon applications that handle the Preferences command can install an Apple event handler for this event, but they more commonly install a Carbon event handler forkEventCommandProcessand check for thekHICommandPreferencescommand ID.
- application diedReceived by an application that launched another application when the launched application quits or terminates. Your application can respond to the information that the other application is no longer running.
application died
Received by an application that launched another application when the launched application quits or terminates. Your application can respond to the information that the other application is no longer running.

### Installing Handlers for Apple Events Sent by the Mac OS
Listing 5-6shows how your application installs handlers for various Apple events that are sent by the Mac OS. The listing assumes that you have defined the functionsOpenApplicationAE,ReopenApplicationAE,OpenDocumentsAE, andPrintDocumentsAEto handle the Apple eventsopen application,reopen,open documents, andprint documents, respectively.
This function doesnât install handlers for theopen contentsandquitApple events, so the application will rely on the default handlers for those events (described previously inCommon Apple Events Sent by the Mac OS).
Listing 5-6Installing event handlers for Apple events from the Mac OS
```
static  OSErr   InstallMacOSEventHandlers(void)```
```
{```
```
    OSErr       err;```
```
 ```
```
    err     = AEInstallEventHandler(kCoreEventClass, kAEOpenApplication,```
```
                NewAEEventHandlerUPP(OpenApplicationAE), 0, false);```
```
    require_noerr(err, CantInstallAppleEventHandler);```
```
 ```
```
    err     = AEInstallEventHandler(kCoreEventClass, kAEReopenApplication,```
```
                NewAEEventHandlerUPP(ReopenApplicationAE), 0, false);```
```
    require_noerr(err, CantInstallAppleEventHandler);```
```
 ```
```
    err     = AEInstallEventHandler(kCoreEventClass, kAEOpenDocuments,```
```
                NewAEEventHandlerUPP(OpenDocumentsAE), 0, false);```
```
    require_noerr(err, CantInstallAppleEventHandler);```
```
 ```
```
    err     = AEInstallEventHandler(kCoreEventClass, kAEPrintDocuments,```
```
                NewAEEventHandlerUPP(PrintDocumentsAE), 0, false);```
```
    require_noerr(err, CantInstallAppleEventHandler);```
```
 ```
```
 ```
```
CantInstallAppleEventHandler:```
```
    return err;```
```
}```
For a description of the parameters you pass to theAEInstallEventHandlerfunction, seeInstalling Apple Event Handlers.
Copyright © 2005, 2007 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2007-10-31