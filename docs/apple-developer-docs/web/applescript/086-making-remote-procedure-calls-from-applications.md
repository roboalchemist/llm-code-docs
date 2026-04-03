# Making Remote Procedure Calls From Applications

# Retired Document
Important:This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Starting with OS X version 10.1, the Apple Event Manager provides support for using the XML-RPC and SOAP protocols to make remote procedure calls from AppleScript scripts and from applications. This chapter provides sample code that show how to make remote procedure calls from applications or other code.
This chapter assumes you are familiar with the conceptual material inIntroduction to XML-RPC and SOAP Programming Guide. To test any of the sample code shown in this book, you must have an Internet connection.

## Making an XML-RPC Call
To make an XML-RPC call from an application or other code, you create an Apple event that describes the remote procedure call, use theAESendfunction to send it, and extract any returned information from the reply Apple event. This process, along with the Apple Event Manager API you use, is described inRemote Procedure Calls From Applications.
This section provides sample code you can use from an application, tool, or other code to send an XML-RPC request to a server. The sample code calls an Internet server that returns the state name for the passed state index. That is, for an index value of 1 it returns Alabama, for 2 it returns Alaska, for 50 it returns Wyoming, and so on.

### Setting Up a Project
You can use the sample code in this section in a number of ways. The following steps show one approach: creating a C++ tool with Project Builder:
- Launch Project Builder.
Launch Project Builder.
- Choose New Project from the File menu.
Choose New Project from the File menu.
- Choose the C++ tool template.
Choose the C++ tool template.
- Replace the code in the automatically generated main.cpp file with the sample code inListing 4-1,Listing 4-2, andListing 4-3, in that order.
Replace the code in the automatically generated main.cpp file with the sample code inListing 4-1,Listing 4-2, andListing 4-3, in that order.
- Use Add Frameworks from the Project menu to addCarbon.frameworkto the project.
Use Add Frameworks from the Project menu to addCarbon.frameworkto the project.
Once youâve built the tool, you can run it in Project Builder and examine its output in the Console pane, or run it in a Terminal window.
You can also build this code directly in a Terminal window with the following compile line:

```applescript
cc -g -o xmlrpc xmlrpc.cp -framework Carbon
```

If you want to compile with a C compiler, rather than a C++ compiler, youâll have to modify the code so that all variables are declared at the beginning of functions, rather than where they are used.

### Includes, Constants, and Declarations
Listing 4-1shows include statements, constants, and declarations to place at the beginning of your code file. This code
- includesCarbon.hto gain access to the scripting API it needs
includesCarbon.hto gain access to the scripting API it needs
- defines a simple error macro that usesfprintfto show an error number and line number, then exits the application
defines a simple error macro that usesfprintfto show an error number and line number, then exits the application
- defines constants that specify the server and method name to call to get state name information
defines constants that specify the server and method name to call to get state name information
- declares a debug function that is defined later
declares a debug function that is defined later
Listing 3-1Includes, constants, and declarations for making an XML-RPC call.

```applescript
#include <Carbon/Carbon.h>
```

```applescript
 
```

```applescript
// Define a simple error macro that just shows the error and line number
```

```applescript
#define checkErr(err) \
```

```applescript
    while (err != noErr) \
```

```applescript
        { fprintf(stderr, "Failed at line %d, error %d\n", __LINE__, err);\
```

```applescript
         exit(-1); }
```

```applescript
 
```

```applescript
// Define constants for the XML-RPC server and method.
```

```applescript
static const char* serverURL = "http://betty.userland.com/RPC2";
```

```applescript
static const char* methodName = "examples.getStateName";
```

```applescript
 
```

```applescript
// Declare our debug function.
```

```applescript
static void dumpDebug(const char* msg, const AppleEvent* replyEvent,
```

```applescript
    OSType debugDataKey);
```

### A Main Function That Makes an XML-RPC Call
Listing 4-2shows amainfunction that prepares an XML-RPC Apple event, sends it, and displays information from the reply Apple event. To do so, it performs the following steps:
- It callsAECreateDescto create a target address descriptor of typetypeApplicationURLthat specifies the target for the request (a remote server). It uses the constantserverURLdefined previously to specify the desired Internet server.
It callsAECreateDescto create a target address descriptor of typetypeApplicationURLthat specifies the target for the request (a remote server). It uses the constantserverURLdefined previously to specify the desired Internet server.
- It callsAECreateAppleEventto create an Apple event with event classkAERPCClass, event IDKAEXMLRPCScheme, and with the target address descriptor from step 1.
It callsAECreateAppleEventto create an Apple event with event classkAERPCClass, event IDKAEXMLRPCScheme, and with the target address descriptor from step 1.
- It callsAECreateListto create the direct object for the Apple event.
It callsAECreateListto create the direct object for the Apple event.
- It callsAEPutParamPtrto insert the method name, using the keykeyRPCMethodNameand the constantmethodNamedefined previously.
It callsAEPutParamPtrto insert the method name, using the keykeyRPCMethodNameand the constantmethodNamedefined previously.
- It callsAECreateListto create a list descriptor for the remote procedure call parameters.
It callsAECreateListto create a list descriptor for the remote procedure call parameters.
- It callsAEPutPtrto insert the only parameter for theexamples.getStateNamefunction, the state index, into the parameter list. It passestypeSInt32for the type code and an index value of 41. The index number was chosen randomly from the legal values of 1 to 50 (the fifty states).
It callsAEPutPtrto insert the only parameter for theexamples.getStateNamefunction, the state index, into the parameter list. It passestypeSInt32for the type code and an index value of 41. The index number was chosen randomly from the legal values of 1 to 50 (the fifty states).
- It callsAEPutParamDescto add the parameter list to the Apple eventâs direct object.
It callsAEPutParamDescto add the parameter list to the Apple eventâs direct object.
- It callsAEPutParamDescto insert the direct object into the Apple event.
It callsAEPutParamDescto insert the direct object into the Apple event.
- It callsAEPutAttributePtrto turn on debugging by adding an attribute to the event with keykeyXMLDebuggingAttrand the valuekAEDebugXMLDebugAll. This step is optional.
It callsAEPutAttributePtrto turn on debugging by adding an attribute to the event with keykeyXMLDebuggingAttrand the valuekAEDebugXMLDebugAll. This step is optional.
- It initializes a reply Apple event.
It initializes a reply Apple event.
- It callsAESendto send the Apple event, passingkAEWaitReplyto indicate it will wait for a reply.
It callsAESendto send the Apple event, passingkAEWaitReplyto indicate it will wait for a reply.
- If the previous call succeeds, it callsAEGetParamPtrwith keykeyDirectObjectand desired type oftypeCharto extract the direct object of the reply Apple event. For a successful call with state index 41, the returned value is the string âSouth Dakotaâ.It callsfprintfto display the state name. For exampleState is South Dakota!Note:Starting in OS X version 10.3,typeCharis deprecated in favor of one of the Unicode string types. For details, see the descriptions fortypeCharand for the Unicode string types inApple Event Manager Reference.
If the previous call succeeds, it callsAEGetParamPtrwith keykeyDirectObjectand desired type oftypeCharto extract the direct object of the reply Apple event. For a successful call with state index 41, the returned value is the string âSouth Dakotaâ.
It callsfprintfto display the state name. For example

```applescript
    State is South Dakota!
```

Note:Starting in OS X version 10.3,typeCharis deprecated in favor of one of the Unicode string types. For details, see the descriptions fortypeCharand for the Unicode string types inApple Event Manager Reference.
- The main function then calls the functiondumpDebug, shown inListing 4-3, once each to display the header and data for the original XML-RPC request and for the reply from the server.Listing 4-4shows the possible result of these calls.
The main function then calls the functiondumpDebug, shown inListing 4-3, once each to display the header and data for the original XML-RPC request and for the reply from the server.Listing 4-4shows the possible result of these calls.
Listing 3-2main function to send an XML-RPC Apple event.

```applescript
//------------------------- main ----------------------------------
```

```applescript
// Builds and sends an XML-RPC Apple event.
```

```applescript
// Sends the Apple event to a server that returns the state
```

```applescript
//   name corresponding to the passed number; e.g., the number
```

```applescript
//   5 corresponds to the state California.
```

```applescript
// Prints the returned state name, then calls function
```

```applescript
//   to dump debug information from reply
```

```applescript
int main()
```

```applescript
{
```

```applescript
    OSErr err;
```

```applescript
    AEDesc targetAddress;
```

```applescript
 
```

```applescript
    // Create the target address.
```

```applescript
    //   Using type typeApplicationURL makes it a remote procedure call event.
```

```applescript
    err = AECreateDesc(typeApplicationURL, serverURL, strlen(serverURL), &targetAddress);
```

```applescript
    checkErr(err);
```

```applescript
 
```

```applescript
    // Create an XML-RPC Apple event
```

```applescript
    AppleEvent xmlrpcEvent;
```

```applescript
    err = AECreateAppleEvent(kAERPCClass, kAEXMLRPCScheme, &targetAddress,
```

```applescript
            kAutoGenerateReturnID, kAnyTransactionID, &xmlrpcEvent);
```

```applescript
    checkErr(err);
```

```applescript
    AEDisposeDesc(&targetAddress);
```

```applescript
 
```

```applescript
    // Create the parameters for the event - the direct object is a record
```

```applescript
    //   that contains the method name, and a list of parameters
```

```applescript
    AEDesc directObject;
```

```applescript
    err = AECreateList(NULL, 0, true, &directObject);
```

```applescript
    checkErr(err);
```

```applescript
 
```

```applescript
    // Insert the method name
```

```applescript
    err = AEPutParamPtr(&directObject, keyRPCMethodName, typeChar,
```

```applescript
        methodName, strlen(methodName));
```

```applescript
    checkErr(err);
```

```applescript
 
```

```applescript
    // Create the list for the actual parameters
```

```applescript
    AEDesc paramList;
```

```applescript
    err = AECreateList(NULL, 0, false, &paramList);
```

```applescript
    checkErr(err);
```

```applescript
 
```

```applescript
    // Put the state index into the parameter array
```

```applescript
    SInt32 stateIndex = 41; // Should correspond to South Dakota
```

```applescript
    err = AEPutPtr(&paramList, 0, typeSInt32, &stateIndex,
```

```applescript
        sizeof(stateIndex));
```

```applescript
    checkErr(err);
```

```applescript
 
```

```applescript
    // Put the parameter list into the direct object
```

```applescript
    err = AEPutParamDesc(&directObject, keyRPCMethodParam, &paramList);
```

```applescript
    checkErr(err);
```

```applescript
    AEDisposeDesc(&paramList);
```

```applescript
 
```

```applescript
    // Put the direct object into the event
```

```applescript
    err = AEPutParamDesc(&xmlrpcEvent, keyDirectObject, &directObject);
```

```applescript
    checkErr(err);
```

```applescript
    AEDisposeDesc(&directObject);
```

```applescript
 
```

```applescript
    // Request all available debugging information. That will include
```

```applescript
    //   the header and body for both the XML-RPC request and the reply
```

```applescript
    //   from the server.
```

```applescript
    SInt32 debugAttr = kAEDebugXMLDebugAll;
```

```applescript
    err = AEPutAttributePtr(&xmlrpcEvent, keyXMLDebuggingAttr, typeSInt32,
```

```applescript
        &debugAttr, sizeof(debugAttr));
```

```applescript
 
```

```applescript
    // Send the event
```

```applescript
    AppleEvent replyEvent;
```

```applescript
    AEInitializeDescInline(&replyEvent);
```

```applescript
    err = AESend(&xmlrpcEvent, &replyEvent, kAEWaitReply, kAENormalPriority,
```

```applescript
        kAEDefaultTimeout, NULL, NULL);
```

```applescript
    checkErr(err);
```

```applescript
 
```

```applescript
    // The direct object of the reply Apple event contains
```

```applescript
    // our result (the name of the state)
```

```applescript
    char buffer[255];
```

```applescript
    Size actualSize;
```

```applescript
    err = AEGetParamPtr(&replyEvent, keyDirectObject, typeChar, NULL,
```

```applescript
        buffer, sizeof(buffer), &actualSize);
```

```applescript
    checkErr(err);
```

```applescript
 
```

```applescript
    fprintf(stderr, "State is %.*s!\n", actualSize, buffer);
```

```applescript
 
```

```applescript
    // Dump debug information
```

```applescript
    dumpDebug("HTTP POST header", &replyEvent, keyAEPOSTHeaderData);
```

```applescript
    dumpDebug("XML Request", &replyEvent, keyAEXMLRequestData);
```

```applescript
    dumpDebug("HTTP Reply header", &replyEvent, keyAEReplyHeaderData);
```

```applescript
    dumpDebug("XML Reply", &replyEvent, keyAEXMLReplyData);
```

```applescript
 
```

```applescript
    return 0;
```

```applescript
}
```

### Displaying XML-RPC Debug Information
Listing 4-3shows a function that extracts debug information from a passed Apple event and displays it withfprintf. The information displayed depends on the key passed in thedebugDataKeyparameter. To display debug data, this function:
- CallsAEGetParamDesc, passing the key specified by thedebugDataKeyparameter and the desired typetypeChar, to extract character data for that debug key.The possible debug keys are shown inApple Event Manager API for Remote Procedure Calls.
CallsAEGetParamDesc, passing the key specified by thedebugDataKeyparameter and the desired typetypeChar, to extract character data for that debug key.
The possible debug keys are shown inApple Event Manager API for Remote Procedure Calls.
- If step 1 fails, it usesfprintfto display an error message.Otherwise, it formats the retrieved character data to show tabs, carriage returns, and line feeds, and displays it withfprintf.
If step 1 fails, it usesfprintfto display an error message.
Otherwise, it formats the retrieved character data to show tabs, carriage returns, and line feeds, and displays it withfprintf.
Listing 3-3A function to display debug information from an XML-RPC reply Apple event.

```applescript
// ------------------------- dumpDebug ----------------------------------
```

```applescript
// Extract and display debug information from a reply Apple event.
```

```applescript
 
```

```applescript
static void dumpDebug(const char* msg, const AppleEvent* replyEvent,
```

```applescript
    OSType debugDataKey)
```

```applescript
{
```

```applescript
    fprintf(stderr, "%s:\n", msg);
```

```applescript
 
```

```applescript
    AEDesc paramDesc;
```

```applescript
    OSErr err = AEGetParamDesc(replyEvent, debugDataKey,
```

```applescript
                                typeChar, &paramDesc);
```

```applescript
    if (err != noErr)
```

```applescript
        fprintf(stderr, "\tCan't get debug data %4.4s - %d returned\n",
```

```applescript
            &debugDataKey, err);
```

```applescript
    else
```

```applescript
    {
```

```applescript
        int len = AEGetDescDataSize(&paramDesc);
```

```applescript
        char* buffer = new char[len];
```

```applescript
        AEGetDescData(&paramDesc, buffer, len);
```

```applescript
 
```

```applescript
        char* p = buffer;
```

```applescript
        char* pEnd = buffer + len;
```

```applescript
 
```

```applescript
        while (p < pEnd)
```

```applescript
        {
```

```applescript
            char* pNext = strpbrk(p, "\r\n");
```

```applescript
            if (pNext == NULL)
```

```applescript
                pNext = pEnd;
```

```applescript
            else
```

```applescript
            {
```

```applescript
                while (pNext < pEnd && (*pNext == '\r' || *pNext == '\n'))
```

```applescript
                {
```

```applescript
                    *pNext++ = '\0';
```

```applescript
                }
```

```applescript
            }
```

```applescript
            fprintf(stderr, "\t%.*s\n", pNext - p, p);
```

```applescript
            p = pNext;
```

```applescript
        }
```

```applescript
 
```

```applescript
        AEDisposeDesc(&paramDesc);
```

```applescript
        delete[] buffer;
```

```applescript
    }
```

```applescript
    fprintf(stderr, "\n\n");
```

```applescript
}
```

The following listing shows sample output from thedumpDebugfunction for an XML-RPC Apple event.
Listing 3-4Sample header and data from an XML-RPC post and the reply.

```applescript
HTTP POST header:
```

```applescript
    POST /RPC2 HTTP/1.0
```

```applescript
    User-Agent: OS X; AEServer (1.0)
```

```applescript
    Host: betty.userland.com
```

```applescript
    Content-Type: text/xml
```

```applescript
    Content-length: 216
```

```applescript
 
```

```applescript
 
```

```applescript
XML Request:
```

```applescript
    <?xml version="1.0" encoding="UTF-8"?>
```

```applescript
        <methodCall>
```

```applescript
            <methodName>examples.getStateName</methodName>
```

```applescript
            <params>
```

```applescript
                <param>
```

```applescript
                    <value>
```

```applescript
                        <i4>41</i4>
```

```applescript
                    </value>
```

```applescript
                </param>
```

```applescript
            </params>
```

```applescript
        </methodCall>
```

```applescript
 
```

```applescript
 
```

```applescript
HTTP Reply header:
```

```applescript
    HTTP/1.1 200 OK
```

```applescript
    Connection: close
```

```applescript
    Content-Length: 141
```

```applescript
    Content-Type: text/xml
```

```applescript
    Date: Mon, 13 Aug 2001 03:56:34 GMT
```

```applescript
    Server: UserLand Frontier/7.0.1-WinNT
```

```applescript
 
```

```applescript
 
```

```applescript
XML Reply:
```

```applescript
    <?xml version="1.0"?>
```

```applescript
    <methodResponse>
```

```applescript
        <params>
```

```applescript
            <param>
```

```applescript
                <value>South Dakota</value>
```

```applescript
                </param>
```

```applescript
            </params>
```

```applescript
        </methodResponse>
```

## Making a SOAP Request
To make a SOAP request from an application or other code, you create an Apple event that describes the request, use theAESendfunction to send it, and extract any returned information from the reply Apple event. This process, along with the Apple Event Manager API you use, is described inRemote Procedure Calls From Applications.
This section provides sample code for sending a SOAP request to a server. Like the sample code inMaking an XML-RPC Call, it makes a request to an Internet server that returns the state name for the passed state index. That is, for an index value of 1 it returns Alabama, for 2 it returns Alaska, and so on. In this case, however, the sample code calls thegetStateNamemethod, a SOAP method on an entirely different server.

You can use the sample code in this task in a number of ways. The following steps show how to create a C++ tool with Project Builder:
- Launch Project Builder.
Launch Project Builder.
- Choose New Project from the File menu.
Choose New Project from the File menu.
- Choose the C++ tool template.
Choose the C++ tool template.
- Replace the code in the automatically generated main.cpp file with the sample code inListing 4-5,Listing 4-6,Listing 4-7, andListing 4-3, in that order.
Replace the code in the automatically generated main.cpp file with the sample code inListing 4-5,Listing 4-6,Listing 4-7, andListing 4-3, in that order.
- Use Add Frameworks from the Project menu to addCarbon.frameworkto the project.
Use Add Frameworks from the Project menu to addCarbon.frameworkto the project.
Once youâve built the tool, you can run it in Project Builder and examine its output in the Console pane, or run it in a Terminal window.
You can also build this code directly in a Terminal window with the following compile line:

```applescript
cc -g -o soap soap.cp -framework Carbon
```

If you want to compile with a C compiler, rather than a C++ compiler, youâll have to modify the code so that all variables are declared at the beginning of functions, rather than where they are used.

Listing 4-5shows include statements, constants, and declarations to place at the beginning of your code file. This code
- includes Carbon.h to gain access to the scripting API it needs
includes Carbon.h to gain access to the scripting API it needs
- defines a simple error macro that usesfprintfto show an error number and line number, then exits the application
defines a simple error macro that usesfprintfto show an error number and line number, then exits the application
- defines constants that specify the server and method name to call to get state name information
defines constants that specify the server and method name to call to get state name information
- declares a function (defined later) that creates a parameter list record
declares a function (defined later) that creates a parameter list record
- declares a debug function that is defined later
declares a debug function that is defined later
Listing 3-5Includes, constants, and declarations for making a SOAP request.

```applescript
#include <Carbon/Carbon.h>
```

```applescript
 
```

```applescript
#define checkErr(err) \
```

```applescript
    while (err != noErr) \
```

```applescript
    { fprintf(stderr, "Failed at line %d, error %d\n", __LINE__, err); \
```

```applescript
    exit(-1); }
```

```applescript
 
```

```applescript
static const char* serverURL = "http://www.soapware.org/examples";
```

```applescript
static const char* methodName = "getStateName";
```

```applescript
static const char* methodNameSpaceURI = "http://www.soapware.org/";
```

```applescript
 
```

```applescript
static OSStatus createUserRecord(AEDesc* desc, const char* paramName,
```

```applescript
    OSType dataType, const void* data, UInt32 dataSize);
```

```applescript
static void dumpDebug(const char* msg, const AppleEvent* reply,
```

```applescript
    OSType debugDataKey);
```

### A Main Function That Makes a SOAP Request
Listing 4-2shows amainfunction that prepares a SOAP request Apple event, sends it, and displays information from the reply Apple event. To do so, it performs the following steps:
- It callsAECreateDescto create a target address descriptor of typetypeApplicationURLthat specifies the target for the request (a remote server). It uses the constantserverURLdefined previously to specify the desired Internet server.
It callsAECreateDescto create a target address descriptor of typetypeApplicationURLthat specifies the target for the request (a remote server). It uses the constantserverURLdefined previously to specify the desired Internet server.
- It callsAECreateAppleEventto create an Apple event with event classkAERPCClass, event IDkAESOAPScheme, and with the target address descriptor from step 1.
It callsAECreateAppleEventto create an Apple event with event classkAERPCClass, event IDkAESOAPScheme, and with the target address descriptor from step 1.
- It callsAECreateListto create the direct object for the Apple event.
It callsAECreateListto create the direct object for the Apple event.
- It callsAEPutParamPtrto insert the method name, using the keykeyRPCMethodNameand the constantmethodNamedefined previously.
It callsAEPutParamPtrto insert the method name, using the keykeyRPCMethodNameand the constantmethodNamedefined previously.
- It calls the functioncreateUserRecord, shown inListing 4-7, to create anAEDescrecord that stores the parameter name and value for a method that has one of each.
It calls the functioncreateUserRecord, shown inListing 4-7, to create anAEDescrecord that stores the parameter name and value for a method that has one of each.
- It callsAEPutParamDescto add the parameter record to the Apple eventâs direct object.
It callsAEPutParamDescto add the parameter record to the Apple eventâs direct object.
- It callsAEPutParamPtrto insert the method namespace URI, using the keykeySOAPMethodNameSpaceURIand the constantmethodNameSpaceURIdefined previously.
It callsAEPutParamPtrto insert the method namespace URI, using the keykeySOAPMethodNameSpaceURIand the constantmethodNameSpaceURIdefined previously.
- It callsAEPutParamDescto insert the direct object into the Apple event.
It callsAEPutParamDescto insert the direct object into the Apple event.
- It callsAEPutAttributePtrto turn on debugging by adding an attribute to the event with keykeyXMLDebuggingAttrand the valuekAEDebugXMLDebugAll. This step is optional.
It callsAEPutAttributePtrto turn on debugging by adding an attribute to the event with keykeyXMLDebuggingAttrand the valuekAEDebugXMLDebugAll. This step is optional.
- It initializes a reply Apple event.
It initializes a reply Apple event.
- It callsAESendto send the Apple event, passingkAEWaitReplyto indicate it will wait for a reply.
It callsAESendto send the Apple event, passingkAEWaitReplyto indicate it will wait for a reply.
- If the previous call succeeds, it callsAEGetParamPtrwith keykeyDirectObjectand desired type oftypeCharto extract the direct object of the reply Apple event. For a successful call with state index 41, the returned value is the string âSouth Dakotaâ.It callsfprintfto display the state name. For exampleState is South Dakota!
If the previous call succeeds, it callsAEGetParamPtrwith keykeyDirectObjectand desired type oftypeCharto extract the direct object of the reply Apple event. For a successful call with state index 41, the returned value is the string âSouth Dakotaâ.
It callsfprintfto display the state name. For example

```applescript
    State is South Dakota!
```

- The main function then calls the functiondumpDebug, shown inListing 4-3, once each to display the header and data for the original XML-RPC request and for the reply from the server.Listing 4-8shows the possible result of these calls.
The main function then calls the functiondumpDebug, shown inListing 4-3, once each to display the header and data for the original XML-RPC request and for the reply from the server.Listing 4-8shows the possible result of these calls.
Listing 3-6main function to send a SOAP Apple event.

```applescript
//------------------------- main ----------------------------------
```

```applescript
// Builds and sends a SOAP request Apple event.
```

```applescript
// Sends the Apple event to a server that returns the state
```

```applescript
//   name corresponding to the passed number; e.g., the number
```

```applescript
//   5 corresponds to the state California.
```

```applescript
// Prints the returned state name, then calls function
```

```applescript
//   to dump debug information from reply
```

```applescript
int main()
```

```applescript
{
```

```applescript
    OSErr err;
```

```applescript
    AEDesc targetAddress;
```

```applescript
 
```

```applescript
    // Create the target address
```

```applescript
    //   Using type typeApplicationURL makes it a remote procedure
```

```applescript
    //   call event.
```

```applescript
    err = AECreateDesc(typeApplicationURL, serverURL, strlen(serverURL),
```

```applescript
        &targetAddress);
```

```applescript
    checkErr(err);
```

```applescript
 
```

```applescript
    // Create a SOAP request Apple event
```

```applescript
    AppleEvent event;
```

```applescript
    err = AECreateAppleEvent(kAERPCClass, kAESOAPScheme, &targetAddress,
```

```applescript
        kAutoGenerateReturnID, kAnyTransactionID, &event);
```

```applescript
    checkErr(err);
```

```applescript
    AEDisposeDesc(&targetAddress);
```

```applescript
 
```

```applescript
    // Create the parameters for the event - the direct object is a
```

```applescript
    // record that contains the method name, and a list of parameters
```

```applescript
 
```

```applescript
    AEDesc directObject;
```

```applescript
    err = AECreateList(NULL, 0, true, &directObject);
```

```applescript
    checkErr(err);
```

```applescript
 
```

```applescript
    // Put the method name
```

```applescript
    err = AEPutParamPtr(&directObject, keyRPCMethodName, typeChar,
```

```applescript
        methodName, strlen(methodName));
```

```applescript
    checkErr(err);
```

```applescript
 
```

```applescript
    // The parameters for a SOAP request are a record. We use the
```

```applescript
    // "AppleScript" format for records that contain user readable
```

```applescript
    // names, and call a helper routine to construct this record.
```

```applescript
    AEDesc paramRecord;
```

```applescript
    SInt32 stateIndex = 41;
```

```applescript
    err = createUserRecord(&paramRecord, "statenum", typeSInt32,
```

```applescript
        &stateIndex, sizeof(stateIndex));
```

```applescript
    checkErr(err);
```

```applescript
 
```

```applescript
    // Put the parameter record into the direct object
```

```applescript
    err = AEPutParamDesc(&directObject, keyRPCMethodParam,
```

```applescript
        &paramRecord);
```

```applescript
    checkErr(err);
```

```applescript
    AEDisposeDesc(&paramRecord);
```

```applescript
 
```

```applescript
    // Additional pieces for soap are the SOAP schema, method
```

```applescript
    //      namespaceURI and SOAPAction.
```

```applescript
    // If the SOAP schema is not explicitly specified, it defaults
```

```applescript
    //      to kSOAP1999Schema for the 1999 schema
```

```applescript
    //      (corresponding to the 1.1 specification).
```

```applescript
    // If the SOAPAction is not explicitly specified, it will be
```

```applescript
    //    the path part of the URL (in this case, "/examples")
```

```applescript
 
```

```applescript
    err = AEPutParamPtr(&directObject, keySOAPMethodNameSpaceURI,
```

```applescript
        typeChar, methodNameSpaceURI, strlen(methodNameSpaceURI));
```

```applescript
    checkErr(err);
```

```applescript
 
```

```applescript
    // Put the direct object into the event
```

```applescript
    err = AEPutParamDesc(&event, keyDirectObject, &directObject);
```

```applescript
    checkErr(err);
```

```applescript
    AEDisposeDesc(&directObject);
```

```applescript
 
```

```applescript
    // Request debugging information
```

```applescript
    SInt32 debugAttr = kAEDebugXMLDebugAll;
```

```applescript
    err = AEPutAttributePtr(&event, keyXMLDebuggingAttr, typeSInt32,
```

```applescript
        &debugAttr, sizeof(debugAttr));
```

```applescript
 
```

```applescript
    // Send the event
```

```applescript
    AppleEvent reply;
```

```applescript
    AEInitializeDescInline(&reply);
```

```applescript
    err = AESend(&event, &reply, kAEWaitReply, kAENormalPriority,
```

```applescript
        kAEDefaultTimeout, NULL, NULL);
```

```applescript
    checkErr(err);
```

```applescript
 
```

```applescript
    // The direct object contains our result (the name of the state)
```

```applescript
    char buffer[255];
```

```applescript
    Size actualSize;
```

```applescript
    err = AEGetParamPtr(&reply, keyDirectObject, typeChar, NULL,
```

```applescript
        buffer, sizeof(buffer), &actualSize);
```

```applescript
    checkErr(err);
```

```applescript
 
```

```applescript
    fprintf(stderr, "State is %.*s!\n", actualSize, buffer);
```

```applescript
 
```

```applescript
    // Dump debug information
```

```applescript
    dumpDebug("HTTP POST header", &reply, keyAEPOSTHeaderData);
```

```applescript
    dumpDebug("XML Request", &reply, keyAEXMLRequestData);
```

```applescript
    dumpDebug("HTTP Reply header", &reply, keyAEReplyHeaderData);
```

```applescript
    dumpDebug("XML Reply", &reply, keyAEXMLReplyData);
```

```applescript
 
```

```applescript
    return 0;
```

```applescript
}
```

### Creating Parameter List Records
Listing 4-7shows a function that creates a record containing the parameter name and value for a SOAP method with one parameter.
To prepare a parameter list record, this function performs the following steps:
- It callsAECreateListto create a list descriptor record for the SOAP request parameters.
It callsAECreateListto create a list descriptor record for the SOAP request parameters.
- It callsAECreateListagain to create a list descriptor for the parameter name and value.
It callsAECreateListagain to create a list descriptor for the parameter name and value.
- CallsAEPutPtrto insert the passed parameter name in the parameter name and value list, with the typetypeChar.
CallsAEPutPtrto insert the passed parameter name in the parameter name and value list, with the typetypeChar.
- CallsAEPutPtragain to insert the passed parameter data in the parameter name and value list, with the type specified the passed type.
CallsAEPutPtragain to insert the passed parameter data in the parameter name and value list, with the type specified the passed type.
- It callsAEPutParamDescto add the parameter name and value list to the parameter list record.
It callsAEPutParamDescto add the parameter name and value list to the parameter list record.
If you need to create a parameter list record for a SOAP request with multiple parameters, you can define a function with a variable length argument list. The function can iterate over the arguments, performing steps 3 and 4 (adding the name and data) for each pair of parameter arguments.
Listing 3-7A function to create a parameter list record for a SOAP request Apple event.

```applescript
// -------------------- createUserRecord -----------------------------
```

```applescript
// Creates a record containing the parameters for a SOAP request.
```

```applescript
// Uses the "AppleScript" format for records that contain user readable
```

```applescript
// names.
```

```applescript
 
```

```applescript
static OSStatus createUserRecord(AEDesc* desc, const char* paramName,
```

```applescript
    OSType dataType, const void* data, UInt32 dataSize)
```

```applescript
{
```

```applescript
    OSErr err = AECreateList(0, NULL, true, desc);
```

```applescript
    if (err == noErr) {
```

```applescript
        AEDesc termsList;
```

```applescript
        err = AECreateList(0, NULL, false, &termsList);
```

```applescript
 
```

```applescript
        if (err == noErr)
```

```applescript
            err = AEPutPtr(&termsList, 0, typeChar,
```

```applescript
                paramName, strlen(paramName));
```

```applescript
        if (err == noErr)
```

```applescript
            err = AEPutPtr(&termsList, 0, dataType,
```

```applescript
                data, dataSize);
```

```applescript
 
```

```applescript
        if (err == noErr)
```

```applescript
            err = AEPutParamDesc(desc, keyASUserRecordFields,
```

```applescript
                &termsList);
```

```applescript
 
```

```applescript
        AEDisposeDesc(&termsList);
```

```applescript
    }
```

```applescript
    return err;
```

```applescript
}
```

### Displaying SOAP Request Debug Information
The sample code to display debug information from a SOAP request Apple event uses the samedumpDebugfunction as the sample code for making an XML-RPC call. That code is shown inListing 4-3. However, because the XML-RPC and SOAP protocols are different, the requests, the Apple events that represent them, and the debug output are all different. ListingListing 4-8shows sample output from thedumpDebugfunction for a SOAP request Apple event.
Listing 3-8Sample header and data from a SOAP post and the reply.

```applescript
HTTP POST header:
```

```applescript
    POST /examples HTTP/1.0
```

```applescript
    Host: www.soapware.org
```

```applescript
    SOAPAction: "/examples"
```

```applescript
    User-Agent: OS X; AEServer (1.0)
```

```applescript
    Content-Type: text/xml
```

```applescript
    Content-length: 538
```

```applescript
 
```

```applescript
 
```

```applescript
XML Request:
```

```applescript
    <?xml version="1.0" encoding="UTF-8"?>
```

```applescript
    <SOAP-ENV:Envelope
```

```applescript
        xmlns:xsd="http://www.w3.org/1999/XMLSchema"
```

```applescript
        xmlns:xsi="http://www.w3.org/1999/XMLSchema-instance"
```

```applescript
        SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
```

```applescript
        xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"
```

```applescript
        xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
```

```applescript
        <SOAP-ENV:Body>
```

```applescript
            <m:getStateName xmlns:m="http://www.soapware.org/">
```

```applescript
                    <statenum xsi:type="xsd:int">41</statenum>
```

```applescript
            </m:getStateName>
```

```applescript
        </SOAP-ENV:Body>
```

```applescript
    </SOAP-ENV:Envelope>
```

```applescript
 
```

```applescript
 
```

```applescript
HTTP Reply header:
```

```applescript
    HTTP/1.1 200 OK
```

```applescript
    Connection: close
```

```applescript
    Content-Length: 499
```

```applescript
    Content-Type: text/xml; charset="us-ascii"
```

```applescript
    Date: Mon, 13 Aug 2001 05:07:46 GMT
```

```applescript
    Server: UserLand Frontier/7.0.1-WinNT
```

```applescript
 
```

```applescript
 
```

```applescript
XML Reply:
```

```applescript
    <?xml version="1.0"?>
```

```applescript
    <SOAP-ENV:Envelope SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
```

```applescript
        xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-ENV="http://
```

```applescript
        schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/1999/XMLSchema"
```

```applescript
        xmlns:xsi="http://www.w3.org/1999/XMLSchema-instance">
```

```applescript
        <SOAP-ENV:Body>
```

```applescript
            <getStateNameResponse>
```

```applescript
                <Result xsi:type="xsd:string">South Dakota</Result>
```

```applescript
                </getStateNameResponse>
```

```applescript
            </SOAP-ENV:Body>
```

```applescript
        </SOAP-ENV:Envelope>
```

Copyright © 2001, 2014 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2014-07-15