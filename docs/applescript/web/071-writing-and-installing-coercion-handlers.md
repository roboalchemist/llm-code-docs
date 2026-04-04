# Writing and Installing Coercion Handlers

# Retired Document
Important:This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Coercionis the process of converting a descriptor and the data it contains from one type to another. When coercing between types, by definition the descriptor type is changed to the new type. However, if the underlying data representation is the same, data conversion is not required.
Functions that perform coercions are referred to ascoercion handlers. The Mac OS provides default coercion handlers to convert between many different descriptor types. Default handlers can, for example, convert aliases to file system specifications, integers to Boolean data types, and characters to numeric data types. These handlers may be implemented by the Apple Event Manager, the Open Scripting framework, or other frameworks.Table C-2lists descriptor types and the available default coercions.
You can also provide your own coercion handlers to perform coercions that the default handlers donât support. This chapter describes how to write coercion handlers and how to install them so that they are available to your application.
For many of the Apple Event Manager functions that your application uses to extract data from an Apple event, you can specify a desired descriptor type for the returned data. If the original data is of a different type, the Apple Event Manager attempts to coerce the data to the requested descriptor type. For more information on functions that let you specify a desired descriptor type, seeCoercing Data From an Apple Event.

## How Coercion Handlers are Installed and Dispatched
Coercion handling works by a process that is similar to the one described previously for dispatching Apple events to Apple event handlers:
- You write coercion handler functions to coerce data between types that your application works with but that are not handled by a default coercion handler.
You write coercion handler functions to coerce data between types that your application works with but that are not handled by a default coercion handler.
- Your application registers coercion handlers with the Apple Event Manager for all the descriptor data types it can convert between. A handler may handle just one type of coercion or multiple types. To specify multiple types, you use the constanttypeWildCard.
Your application registers coercion handlers with the Apple Event Manager for all the descriptor data types it can convert between. A handler may handle just one type of coercion or multiple types. To specify multiple types, you use the constanttypeWildCard.
- The Apple Event Manager creates an application coercion handler dispatch table for your application. The dispatch table maps the descriptor types your application can coerce to the coercion handlers it provides.The Apple Event Manager also creates a system coercion dispatch handler, described below, for the default coercion handlers.
The Apple Event Manager creates an application coercion handler dispatch table for your application. The dispatch table maps the descriptor types your application can coerce to the coercion handlers it provides.
The Apple Event Manager also creates a system coercion dispatch handler, described below, for the default coercion handlers.
- When the Apple Event Manager needs to perform a coercion in your application, it goes through these steps until the coercion is handled:It looks for a coercion handler in your application coercion dispatch table.It looks for a coercion handler in your system coercion dispatch table, which includes the default coercions described inTable C-2.Note:Default coercion handlers may be installed lazily, as they are needed.If it canât find an appropriate coercion handler, it returns the result codeerrAECoercionFail.
When the Apple Event Manager needs to perform a coercion in your application, it goes through these steps until the coercion is handled:
- It looks for a coercion handler in your application coercion dispatch table.
It looks for a coercion handler in your application coercion dispatch table.
- It looks for a coercion handler in your system coercion dispatch table, which includes the default coercions described inTable C-2.Note:Default coercion handlers may be installed lazily, as they are needed.
It looks for a coercion handler in your system coercion dispatch table, which includes the default coercions described inTable C-2.
Note:Default coercion handlers may be installed lazily, as they are needed.
- If it canât find an appropriate coercion handler, it returns the result codeerrAECoercionFail.
If it canât find an appropriate coercion handler, it returns the result codeerrAECoercionFail.
Although your application can have both a system coercion dispatch table and an application dispatch table, you should generally install all coercion handlers in the application coercion dispatch table. For Carbon applications running in Mac OS 8 or Mac OS 9, a handler in the system coercion dispatch table could reside in the system heap, where it would be available to other applications. However, your application should not install a handler in a system coercion dispatch table with the goal that the handler will get called when other applications perform coercionsâthis wonât necessarily work in Mac OS 8 or Mac OS 9 and will not work in Mac OS X.

## Writing a Coercion Handler
When you write a coercion handler, it must do the following things:
- Validate the information passed to it so that it has a reasonable chance of success.
Validate the information passed to it so that it has a reasonable chance of success.
- Gain access to the information to be coerced.
Gain access to the information to be coerced.
- Convert the information to the specified type.
Convert the information to the specified type.
- Create a new descriptor of the specified type.
Create a new descriptor of the specified type.
Warning:This coercion handler usestypeChar, which should be avoided starting in Mac OS X version 10.3, as noted inDefault Coercion Handlers.
There are two types of coercion handlers. The first, which matches the format defined for theAECoerceDescProcPtrdata type, expects the caller to pass a descriptor containing the data to be coerced. The second, which matches the format defined for theAECoercePtrProcPtrdata type, expects the caller to pass a a pointer to the data to be coerced. These data types are described inApple Event Manager Reference.
The examples in this chapter show how to work with a coercion handler that uses descriptors. However the differences in working with the pointer-based type are fairly straight-forward.
To write a a coercion handler namedCoerceApplesToOranges, based on theAECoerceDescProcPtrdata type, you would declare the handler as shown inListing 7-1.
Listing 7-1Declaring a coercion handler

```applescript
OSErr CoerceApplesToOranges (
```

```applescript
    const AEDesc * fromDesc,// 1
```

```applescript
    DescType toType,// 2
```

```applescript
    long handlerRefcon,// 3
```

```applescript
    AEDesc * toDesc// 4
```

```applescript
);
```

The following are descriptions of the numbered parameters:
- A pointer to the descriptor to be coerced.
A pointer to the descriptor to be coerced.
- The type to coerce to.
The type to coerce to.
- A reference variable that will be passed to your handlerâyou can use it for any purpose.
A reference variable that will be passed to your handlerâyou can use it for any purpose.
- A descriptor pointer where the handler will store the coerced descriptor.This routine creates a new descriptor, so it is up to the calling routine to dispose of the descriptor.
A descriptor pointer where the handler will store the coerced descriptor.
This routine creates a new descriptor, so it is up to the calling routine to dispose of the descriptor.
Suppose that you want to write a coercion handler to convert text strings into your internal âbarâ data type. ThetypeBartype is defined as shown inListing 7-2.
Listing 7-2An application-defined data type

```applescript
enum {
```

```applescript
  typeBar = 'bar!'
```

```applescript
};
```

Listing 7-3provides a slightly simplified version of the handler you might write.
Listing 7-3A simple coercion handler

```applescript
static OSErr TextToBarCoercionHandler(const AEDesc* fromDesc, DescType toType, long handlerRefcon, AEDesc* toDesc)
```

```applescript
{
```

```applescript
    require_noerr((fromDesc->descriptorType != typeChar),CoercionFailed);// 1
```

```applescript
    require_noerr((toType != typeBar), CoercionFailed);
```

```applescript
    require_noerr((handlerRefcon != 1234), CoercionFailed);// 2
```

```applescript
 
```

```applescript
    long dataSize = AEGetDescDataSize(fromDesc);// 3
```

```applescript
    char dataPtr[dataSize];
```

```applescript
    OSErr err = AEGetDescData(fromDesc, dataPtr, dataSize);
```

```applescript
    require_noerr(err, CoercionFailed);
```

```applescript
 
```

```applescript
    long result = 0;
```

```applescript
    const char* pChar = (const char*) dataPtr;
```

```applescript
    while (dataSize-- > 0)// 4
```

```applescript
        result += *pChar++;
```

```applescript
 
```

```applescript
    err = AECreateDesc(typeBar, &result, sizeof(result), toDesc);// 5
```

```applescript
 
```

```applescript
    if (err != noErr)// 6
```

```applescript
        err = errAECoercionFail;
```

```applescript
 
```

```applescript
CoercionFailed:// 7
```

```applescript
        return err;
```

```applescript
}
```

Hereâs what the code inTextToBarCoercionHandlerdoes:
- Checks the passed parameters to validate that it can handle the requested coercion, using the macrorequire_noerr, which jumps to the error labelCoercionFailedif a value isnât supported.Coercion handlers that support multiple types will have additional work to do here.
Checks the passed parameters to validate that it can handle the requested coercion, using the macrorequire_noerr, which jumps to the error labelCoercionFailedif a value isnât supported.
Coercion handlers that support multiple types will have additional work to do here.
- Checks that the passed reference constant matches the expected value. You previously set the reference constant when you installed the coercion handler (shown inInstalling a Coercion Handler).
Checks that the passed reference constant matches the expected value. You previously set the reference constant when you installed the coercion handler (shown inInstalling a Coercion Handler).
- Gets the size of the data in the descriptor to be coerced and uses it to get the actual data from the descriptor.
Gets the size of the data in the descriptor to be coerced and uses it to get the actual data from the descriptor.
- In a while loop, converts the data from type text to type bar (by summing the bytes).
In a while loop, converts the data from type text to type bar (by summing the bytes).
- Creates a new descriptor of type bar, using the coerced data.
Creates a new descriptor of type bar, using the coerced data.
- If it was unable to create the coerced descriptor, returns an error indicating the coercion failed.
If it was unable to create the coerced descriptor, returns an error indicating the coercion failed.
- Whether it jumped to the error label or fell through on success, returns an error code indicating whether the coercion succeeded or failed.
Whether it jumped to the error label or fell through on success, returns an error code indicating whether the coercion succeeded or failed.
These are the main differences if you want to write a coercion handler based on theAECoercePtrProcPtrdata type, which works with a pointer to data:
- The coercion handler has two additional parameters: one specifies the descriptor type of the data the pointer parameter points to; the other specifies the size of the data.
The coercion handler has two additional parameters: one specifies the descriptor type of the data the pointer parameter points to; the other specifies the size of the data.
- When obtaining the data to convert, you use the size and type information to extract the data from the pointer, rather than getting the type and the data from a passed descriptor.
When obtaining the data to convert, you use the size and type information to extract the data from the pointer, rather than getting the type and the data from a passed descriptor.

## Installing a Coercion Handler
To install a coercion handler, you use theAEInstallCoercionHandlerfunction, which is declared as shown inListing 7-4.
Listing 7-4Declaration of AEInstallCoercionHandler

```applescript
OSErr AEInstallCoercionHandler (
```

```applescript
    DescType fromType,// 1
```

```applescript
    DescType toType,// 2
```

```applescript
    AECoercionHandlerUPP handler,// 3
```

```applescript
    long handlerRefcon,// 4
```

```applescript
    Boolean fromTypeIsDesc,// 5
```

```applescript
    Boolean isSysHandler// 6
```

```applescript
);
```

You specify as parameters to this function:
- The descriptor type of the data coerced by the handler. You can passtypeWildCardto accept all types.
The descriptor type of the data coerced by the handler. You can passtypeWildCardto accept all types.
- The descriptor type of the resulting data. You can passtypeWildCardto accept all types.
The descriptor type of the resulting data. You can passtypeWildCardto accept all types.
- The address of the coercion handler for this descriptor type; the handler is declared as described inWriting a Coercion Handler.
The address of the coercion handler for this descriptor type; the handler is declared as described inWriting a Coercion Handler.
- A reference constant to pass to the handler when it is called. You can use the reference constant for any purpose you want.
A reference constant to pass to the handler when it is called. You can use the reference constant for any purpose you want.
- A Boolean value that indicates whether your coercion handler expects the data to be specified as a descriptor or as a pointer to the actual data.
A Boolean value that indicates whether your coercion handler expects the data to be specified as a descriptor or as a pointer to the actual data.
- A Boolean value that indicates whether your coercion handler should be added to your applicationâs coercion dispatch table or the system coercion dispatch table.
A Boolean value that indicates whether your coercion handler should be added to your applicationâs coercion dispatch table or the system coercion dispatch table.
To call theTextToBarCoercionHandlerhandler defined inListing 7-3, you can use code like that shown inListing 7-5.
Listing 7-5Installing a coercion handler

```applescript
OSErr err = AEInstallCoercionHandler(
```

```applescript
                typeChar, // Coerce from this type
```

```applescript
                typeBar, // to this type,
```

```applescript
                TextToBarCoercionHandler, //using this handler,
```

```applescript
                1234,   //  passing this reference constant.
```

```applescript
                true,   //  The handler operates on descriptors,
```

```applescript
                false); //  and resides in the application table.
```

Hereâs what the parameters in this call specify:
- Coerce from type'TEXT'.
Coerce from type'TEXT'.
- Coerce to typetypeBar.
Coerce to typetypeBar.
- Use the handlerTextToBarCoercionHandlerto perform the coercion.
Use the handlerTextToBarCoercionHandlerto perform the coercion.
- Pass the reference constant 1234.
Pass the reference constant 1234.
- The handler operates on descriptors.
The handler operates on descriptors.
- The handler resides in the applicationâs coercion dispatch table.
The handler resides in the applicationâs coercion dispatch table.

## Testing a Coercion Handler
You can use code like that shown inListing 7-6to test theTextToBarCoercionHandlerhandler defined inListing 7-3.
Listing 7-6Testing a coercion handler

```applescript
    AEDesc textDesc;
```

```applescript
    const char* kText = "1234";
```

```applescript
    OSErr err = AECreateDesc(typeChar, kText, strlen(kText), &textDesc);// 1
```

```applescript
 
```

```applescript
    AEDesc barDesc;
```

```applescript
    err = AECoerceDesc(&textDesc, typeBar, &barDesc);// 2
```

```applescript
    if (err == noErr)
```

```applescript
    {
```

```applescript
        // Use the descriptor as needed.
```

```applescript
 
```

```applescript
        // Dispose of the descriptor when finished with it.
```

```applescript
        err = AEDisposeDesc(&barDesc);// 3
```

```applescript
    }
```

```applescript
    err = AEDisposeDesc(&textDesc);// 4
```

Here is what the code in this snippet does:
- Creates a descriptor containing the text string â1234â.
Creates a descriptor containing the text string â1234â.
- Calls the Apple Event Manager functionAECoerceDesc, passing the text descriptor, the desired type (type bar), and the address of a descriptor in which to store the coerced descriptor.
Calls the Apple Event Manager functionAECoerceDesc, passing the text descriptor, the desired type (type bar), and the address of a descriptor in which to store the coerced descriptor.
- If the coercion is successful, disposes of the coerced descriptor. Because a coercion returns a new descriptor, your application must dispose of the descriptor when it is finished with it. (This code snippet does not include full error handling.)
If the coercion is successful, disposes of the coerced descriptor. Because a coercion returns a new descriptor, your application must dispose of the descriptor when it is finished with it. (This code snippet does not include full error handling.)
- Disposes of the text descriptor.
Disposes of the text descriptor.
If the coercion fails, you can set a breakpoint in your coercion handler to determine if it is ever called. Possible problems include:
- You didnât install the coercion handler.
You didnât install the coercion handler.
- The type you passed toAECoerceDescwas different than the type you registered for your coercion handler.
The type you passed toAECoerceDescwas different than the type you registered for your coercion handler.
- The text descriptor you created has a different descriptor type than you registered for your coercion handler.
The text descriptor you created has a different descriptor type than you registered for your coercion handler.
You can install a single coercion handler that specifies the constanttypeWildCardfor both the to and from types. Then any time the Apple Event Manager attempts to dispatch a coercion to the application, it will invoke that handler. This provides a convenient bottleneck for debugging.
Using wildcards can also be convenient as a general way to handle coercions, with one or a small number of handlers converting between supported types and the applicationâs private data types.
Copyright © 2005, 2007 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2007-10-31