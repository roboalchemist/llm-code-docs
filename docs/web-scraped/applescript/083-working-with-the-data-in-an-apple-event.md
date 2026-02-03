# Working With the Data in an Apple Event

# Retired Document
Important:This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

This chapter describes how your application gets various kinds of data from Apple events and the data structures that comprise them.
Your application responds to Apple events in the Apple event handlers it registers, or in routines your handlers call. Within a handler, you know that the passed Apple event matches the expected event class and event ID, although there can be some variation if the handler is registered with one or more wildcards. In either case, your handler has at least a general idea of what information the Apple event should contain. In the case of a wildcard handler, it can obtain information from the Apple event to identify the type more closely.

## About Extracting Data From an Apple Event
The parameters and attributes of an Apple event, as well as the data within an individual descriptor, are stored in a format that is opaque to your application. You use Apple Event Manager functions to extract the data you need from a received Apple event. To obtain data in a format your application can use, you typically follow a common series of steps:
- You call a function that returns the descriptor for a high-level data structure you are interested in, such as an Apple event attribute or parameter. For example, you can call theAEGetAttributeDescfunction to obtain the descriptor for an attribute, specifying the attribute by its keyword.
You call a function that returns the descriptor for a high-level data structure you are interested in, such as an Apple event attribute or parameter. For example, you can call theAEGetAttributeDescfunction to obtain the descriptor for an attribute, specifying the attribute by its keyword.
- If the returned descriptor is a list, you use another function to iterate over the items in the list. For example, you can useAEGetNthDescto get descriptors from a list by index.
If the returned descriptor is a list, you use another function to iterate over the items in the list. For example, you can useAEGetNthDescto get descriptors from a list by index.
- Once you have obtained an individual descriptor, you use other functions to extract its data. For example, you can callAEGetDescDataSizeto determine the size of the data in a descriptor andAEGetDescDatato get the data.
Once you have obtained an individual descriptor, you use other functions to extract its data. For example, you can callAEGetDescDataSizeto determine the size of the data in a descriptor andAEGetDescDatato get the data.
Many of the functions for getting data from an Apple event are available in two forms:
- One that returns a copy of the descriptor for the data.
One that returns a copy of the descriptor for the data.
- One that returns a copy of the data in a buffer you have supplied.
One that returns a copy of the data in a buffer you have supplied.
For example,AEGetParamDescreturns a copy of the descriptor for a parameter, whileAEGetParamPtrreturns the data from an Apple event parameter in a specified buffer. You typically use the buffer form to extract data of fixed length or known maximum length, such as a result code. You use the descriptor form to extract data of variable length, such as a list of unknown length.
You can also use Apple Event Manager functions to get data from descriptors, descriptor lists, and Apple events. For example, you can use theAESizeOfAttributefunction to get the size and descriptor type of an Apple event attribute from an Apple event. And you can use theAESizeOfParamfunction to get the size and descriptor type of an Apple event parameter from an Apple event or an Apple event record (typeAERecord).
Where performance is critical, you can useAECreateDescFromExternalPtrto efficiently create a descriptor containing large amounts of data, and callAEGetDescDataRangeto efficiently get data from a descriptor.
Other functions allow you to count the number of items in a descriptor list (AECountItems) or iterate through those descriptors (AEGetNthPtrorAEGetNthDesc).
This chapter provides examples of how to work with some of these functions, whileFunctions for Working With Apple Event Data Structureslists these and other Apple Event Manager functions. For complete reference, seeApple Event Manager Reference.

## Coercing Data From an Apple Event
Coercionis the process of converting a descriptor and, if necessary, the data it contains, from one type to another. When your handler receives an Apple event, you typically use one or more of the functionsAEGetParamPtr,AEGetAttributePtr,AEGetParamDesc,AEGetAttributeDesc,AEGetNthPtr, andAEGetNthDescto get data from the Apple event. Each of these Apple Event Manager functions allows your application to specify a desired descriptor type for the resulting data. If the original data is of a different type, the Apple Event Manager attempts to coerce the data to the requested descriptor type. To prevent coercion and ensure that the descriptor type of the result is of the same type as the original, you specifytypeWildCardfor the desired type.
The following code snippet shows how to specify a desired descriptor type when calling the functionAEGetParamPtr.
Listing 4-1Getting and coercing an Apple event parameter

```applescript
    DescType        returnedType;
```

```applescript
    long            multResult;
```

```applescript
    Size            actualSize;
```

```applescript
    OSErr           err;
```

```applescript
 
```

```applescript
    err = AEGetParamPtr(
```

```applescript
            theAppleEvent,// 1
```

```applescript
            keyMultResult,// 2
```

```applescript
            typeSInt32,// 3
```

```applescript
            &returnedType,// 4
```

```applescript
            &multResult,// 5
```

```applescript
            sizeof(multResult),// 6
```

```applescript
            &actualSize);// 7
```

Hereâs a description of the parameters used in this call:
- A pointer to the Apple event to get the parameter data from.
A pointer to the Apple event to get the parameter data from.
- A keyword constant specifying the parameter to get the data from. In this example, the keyword is defined by the application and indicates a parameter containing the result of a multiplication operation.
A keyword constant specifying the parameter to get the data from. In this example, the keyword is defined by the application and indicates a parameter containing the result of a multiplication operation.
- A constant specifying the type to coerce the returned value to (if it isnât already that type).
A constant specifying the type to coerce the returned value to (if it isnât already that type).
- The address of a variable in which the function stores the actual type of the returned value, which may not match the requested type.
The address of a variable in which the function stores the actual type of the returned value, which may not match the requested type.
- The address of a variable in which the function stores the returned data.
The address of a variable in which the function stores the returned data.
- The maximum size of the returned data. TheAEGetParamPtrfunction wonât return more data than you specify in this parameter.
The maximum size of the returned data. TheAEGetParamPtrfunction wonât return more data than you specify in this parameter.
- The address of a variable in which the function stores the actual size of the requested data. If the returned value is greater than the amount your application allocated to store the returned data, you can increase the size of your buffer to this amount and call the function again. You can also choose to use theAEGetParamDescfunction when your application doesnât know the size of the data.
The address of a variable in which the function stores the actual size of the requested data. If the returned value is greater than the amount your application allocated to store the returned data, you can increase the size of your buffer to this amount and call the function again. You can also choose to use theAEGetParamDescfunction when your application doesnât know the size of the data.
If the coercion fails, theAEGetParamPtrfunction returns the result codeerrAECoercionFail.
By default, the Apple Event Manager can coerce between many different data types, listed inTable C-2. To perform other coercions, such as those involving data types you have defined, you can provide your own coercion handlers. SeeWriting and Installing Coercion Handlersfor more information on working with coercion handlers.

## Getting Data From an Apple Event Parameter
Apple event parameters are keyword-specified descriptors. You can use theAEGetParamDescfunction to get the descriptor for a parameter or to extract the descriptor list from a parameter; you can useAEGetParamPtrto get the data from the descriptor for a parameter. In general, use the former to extract data of variable length, and the latter to extract data of fixed length or known maximum length.
Listing 4-2shows how to callAEGetParamDescto extract a parameter descriptor from an Apple event such as anopen documentsevent.
Listing 4-2Getting a parameter as a descriptor

```applescript
    AEDescList  docList;
```

```applescript
    OSErr       myErr;
```

```applescript
 
```

```applescript
    myErr = AEGetParamDesc( theAppleEvent,// 1
```

```applescript
                            keyDirectObject,// 2
```

```applescript
                            typeAEList,// 3
```

```applescript
                            &docList);// 4
```

```applescript
 
```

```applescript
    // Check the returned value from AEGetParamDesc for any error.
```

```applescript
    // (Not shown.)
```

Hereâs a description of the parameters used in this call:
- A pointer to the Apple event to get the parameter descriptor from (obtained previously).
A pointer to the Apple event to get the parameter descriptor from (obtained previously).
- A constant specifying that the function should get the descriptor for the direct parameter.
A constant specifying that the function should get the descriptor for the direct parameter.
- A constant specifying that the descriptor should be returned as a descriptor list, coercing it if necessary. If the coercion fails, the function returns the result codeerrAECoercionFail.
A constant specifying that the descriptor should be returned as a descriptor list, coercing it if necessary. If the coercion fails, the function returns the result codeerrAECoercionFail.
- The address of a variable in which the function stores the returned descriptor list.
The address of a variable in which the function stores the returned descriptor list.
SeeGetting Data From a Descriptor Listfor details on working with a descriptor list.
TheAEGetParamDescfunction supplies a copy of the descriptor for the parameter, so you must dispose of it when youâre finished with it by calling theAEDisposeDescfunction. For an example, seeListing 4-6.
If an Apple event parameter contains an object specifier, your handler should use theAEResolvefunction, other Apple Event Manager functions, and your own application-defined functions to resolve the object specifierâthat is, to locate the Apple event object in your application that the specifier describes. For more information, seeâResolving and Creating Object Specifier RecordsâinInside Macintosh: Interapplication Communication.

## Getting Data From an Apple Event Attribute
To get the descriptor for an attribute or to get the data from an attribute you use routines that are similar to those you use with parameters: theAEGetAttributePtrandAEGetAttributeDescfunctions.
For example,Listing 4-3shows how to useAEGetAttributePtrto get the data from thekeyEventSourceAttrattribute of an Apple event.
Listing 4-3Getting a value from an attribute

```applescript
    DescType        returnedType;
```

```applescript
    AEEventSource   sourceOfAE;
```

```applescript
    Size            actualSize;
```

```applescript
    OSErr           myErr;
```

```applescript
 
```

```applescript
myErr = AEGetAttributePtr( theAppleEvent,// 1
```

```applescript
                            keyEventSourceAttr,// 2
```

```applescript
                            typeShortInteger,// 3
```

```applescript
                            &returnedType,// 4
```

```applescript
                            (void *) &sourceOfAE,// 5
```

```applescript
                            sizeof (sourceOfAE),// 6
```

```applescript
                            &actualSize);// 7
```

```applescript
 
```

```applescript
    // Check the returned value from AEGetParamDesc for any error.
```

```applescript
    // (Not shown.)
```

Hereâs a description of the parameters used in this call:
- A pointer to the Apple event to get the attribute data from (obtained previously).
A pointer to the Apple event to get the attribute data from (obtained previously).
- A constant specifying the attribute from which to get the data.
A constant specifying the attribute from which to get the data.
- A constant specifying that the data should be returned as a short integer.
A constant specifying that the data should be returned as a short integer.
- The address of a variable in which the function stores the type of the actual descriptor returned.
The address of a variable in which the function stores the type of the actual descriptor returned.
- The address of a variable in which the function stores the requested data. If the data is not already a short integer, the Apple Event Manager coerces it as necessary. The value should equal one of the event source constant values described inEvent Source Constants.If you allocate a buffer for this parameter, itâs up to you to free it when you are finished with it.
The address of a variable in which the function stores the requested data. If the data is not already a short integer, the Apple Event Manager coerces it as necessary. The value should equal one of the event source constant values described inEvent Source Constants.
If you allocate a buffer for this parameter, itâs up to you to free it when you are finished with it.
- The size of the return buffer.
The size of the return buffer.
- The address of a variable in which the function stores the actual size of the returned data after coercion has taken place. You can check this value to make sure you got all the data.
The address of a variable in which the function stores the actual size of the returned data after coercion has taken place. You can check this value to make sure you got all the data.

## Getting Data From a Descriptor
Because the data within a descriptor is opaque, you use Apple Event Manager functions to extract it. In some cases, such as the example shown inListing 4-3, the data is of known type and size, or can be coerced to a known type, and you can store it in a variable of that type.
It is common, however, for a descriptor to contain data, such as text or an image, of unknown size. In situations of that type, you can call theAEGetDescDataSizefunction to find out how much memory you will need to store the data, allocate a buffer of that size, then callAEGetDescDatato get the actual data from the descriptor. The code snippet inListing 4-4shows how you might use these functions to get data into a buffer.
Listing 4-4Determining the size, then obtaining descriptor data

```applescript
    Size dataSize = AEGetDescDataSize(desc);// 1
```

```applescript
    UInt8* buffer = malloc(dataSize);// 2
```

```applescript
    if (buffer)
```

```applescript
    {
```

```applescript
        OSErr err = AEGetDescData(desc, buffer, dataSize);// 3
```

```applescript
 
```

```applescript
        // If no error, use the data.// 4
```

```applescript
 
```

```applescript
        free(buffer);// 5
```

```applescript
    }
```

Hereâs a description of what this code does:
- Calls an Apple Event Manager function to get the data size for the descriptor.
Calls an Apple Event Manager function to get the data size for the descriptor.
- Creates a buffer of that size.
Creates a buffer of that size.
- Calls an Apple Event Manager function to get the data from the descriptor into the buffer.
Calls an Apple Event Manager function to get the data from the descriptor into the buffer.
- If no error occurred in getting the data, your application can use it as needed.
If no error occurred in getting the data, your application can use it as needed.
- Frees the allocated buffer.
Frees the allocated buffer.
Alternatively, you can do the following:
- Call theAEGetParamPtrfunction (shown inListing 4-1), passing a size of zero for the maximum size (line 6 in the listing).
Call theAEGetParamPtrfunction (shown inListing 4-1), passing a size of zero for the maximum size (line 6 in the listing).
- Get the actual size value returned byAEGetParamPtr.
Get the actual size value returned byAEGetParamPtr.
- Allocate a buffer of that size.
Allocate a buffer of that size.
- CallAEGetParamPtragain to get the data into the buffer.
CallAEGetParamPtragain to get the data into the buffer.
- If you allocated memory for the buffer, free it when you are finished with it.
If you allocated memory for the buffer, free it when you are finished with it.

## Getting Data From a Descriptor List
To get descriptors and their data from a descriptor list, you can call theAECountItemsfunction to get the number of descriptors in the list, then set up a loop that callsAEGetNthDescorAEGetNthPtrto get the data from each descriptor.
For example, anopen documentsevent contains a direct parameter that specifies a list of documents to open. The parameter contains a descriptor list in which each descriptor specifies an alias to a file to open.Listing 4-5shows how you can extract the descriptor list from the parameter, determine the number of items it contains, and extract each descriptor from the list.
Listing 4-5Getting a descriptor list and its items

```applescript
    AEDescList  docList;
```

```applescript
    FSRef       theFSRef;
```

```applescript
    long        index;
```

```applescript
    long        count = 0;
```

```applescript
    OSErr       err;
```

```applescript
 
```

```applescript
    err = AEGetParamDesc(theAppleEvent, keyDirectObject,
```

```applescript
                         typeAEList, &docList);// 1
```

```applescript
 
```

```applescript
    err = AECountItems(&docList, &count);// 2
```

```applescript
 
```

```applescript
    for(index = 1; index <= count; index++)// 3
```

```applescript
    {
```

```applescript
        err = AEGetNthPtr(&docList, index, typeFSRef,
```

```applescript
                        NULL, NULL, &theFSRef,
```

```applescript
                        sizeof(theFSRef), NULL);// 4
```

```applescript
 
```

```applescript
        // Call routine to open document with current reference.// 5
```

```applescript
    }
```

Hereâs a description of what this code does:
- CallsAEGetParamDescto obtain, in the variabledocList, a copy of the descriptor list from the direct parameter of the Apple event. Passes the constantkeyDirectObjectto identify the direct parameter and the constanttypeAEListto indicate the desired descriptor type. (theAppleEventis a pointer to the Apple event, obtained previously, to get the parameter descriptor from).
CallsAEGetParamDescto obtain, in the variabledocList, a copy of the descriptor list from the direct parameter of the Apple event. Passes the constantkeyDirectObjectto identify the direct parameter and the constanttypeAEListto indicate the desired descriptor type. (theAppleEventis a pointer to the Apple event, obtained previously, to get the parameter descriptor from).
- CallsAECountItems, passing the previously obtained descriptor list, to get the number of items in the list.
CallsAECountItems, passing the previously obtained descriptor list, to get the number of items in the list.
- Sets up a loop based on the count.
Sets up a loop based on the count.
- CallsAEGetNthPtrto obtain the indexed descriptor from the list. PassestypeFSRefto indicate the descriptor should be coerced to a file system reference, if necessary (otherwise the returned value will be a file alias). Passes the address of the variabletheFSRefas a buffer to store the reference.PassesNULLfor the fourth and fifth parameters, indicating the keyword and descriptor type of the returned item arenât needed.Also passesNULLfor the last parameter, indicating the actual size of the returned data isnât required. (If the returned size is larger than the size of the buffer you provided, you know that you didnât get all of the data for the descriptor.)
CallsAEGetNthPtrto obtain the indexed descriptor from the list. PassestypeFSRefto indicate the descriptor should be coerced to a file system reference, if necessary (otherwise the returned value will be a file alias). Passes the address of the variabletheFSRefas a buffer to store the reference.
PassesNULLfor the fourth and fifth parameters, indicating the keyword and descriptor type of the returned item arenât needed.
Also passesNULLfor the last parameter, indicating the actual size of the returned data isnât required. (If the returned size is larger than the size of the buffer you provided, you know that you didnât get all of the data for the descriptor.)
- Here you would call your own routine to open a document specified by the extracted file system reference.
Here you would call your own routine to open a document specified by the extracted file system reference.
For a more complete version of this code, including simple error handling, seeListing 5-5.

## Disposing of Apple Event Data Structures
If you create a descriptor, you must dispose of it when you are finished with it to prevent memory leaks. For example, when you extract a descriptor using theAEGetParamDesc,AEGetAttributeDesc,AEGetNthDesc, orAEGetKeyDescfunction, you get a copy of the descriptor. You call theAEDisposeDescfunction to dispose of your copy, thereby deallocating the memory used by its data.
Listing 4-6shows how to dispose of a descriptor list returned byAEGetParamDesc.
Listing 4-6Disposing of a descriptor list obtained from the direct object of an Apple event

```applescript
AEDescList  docList;
```

```applescript
OSErr       err;
```

```applescript
err = AEGetParamDesc(theAppleEvent, keyDirectObject, typeAEList, &docList);
```

```applescript
 
```

```applescript
// Check for error, then perform operations on the descriptor list here.
```

```applescript
 
```

```applescript
AEDisposeDesc(&docList);
```

You can safely callAEDisposeDescon a null descriptor (but not on a null pointer!) Anull descriptoris one that has been initialized as shown in the following code snippet.

```applescript
AEDesc      someDesc = { typeNull, 0L };
```

```applescript
 
```

```applescript
// Code to obtain a descriptor, which may fail.
```

```applescript
 
```

```applescript
// Safe to dispose, whether or not previous code succeeded.
```

```applescript
AEDisposeDesc(&someDesc);
```

You can perform the same initialization using theAEInitializeDescfunction, as shown in this code snippet.

```applescript
    AEDesc      someDesc;
```

```applescript
 
```

```applescript
    AEInitializeDesc(&someDesc);
```

When you obtain a copy of a descriptor with one of the buffer-based functions, such asAEGetAttributePtrorAEGetNthPtr, the data is copied into a buffer provided by your application. You must then free any allocated memory when finished with the buffer.
Copyright © 2005, 2007 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2007-10-31