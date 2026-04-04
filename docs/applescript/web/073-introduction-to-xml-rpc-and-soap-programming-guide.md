# Introduction to XML-RPC and SOAP Programming Guide

# Retired Document
Important:This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Important:This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.
Note:This document was previously titled âXML-RPC and SOAP Support.â
XML-RPC and SOAP Programming Guidedescribes how to use Apple Script and the Apple Event Manager in OS X to make remote procedure calls using the XML-RPC and SOAP (Simple Object Access Protocol) protocols.
XML-RPCis a protocol for using XML and HTTP to make remote procedure calls over the Internet.SOAP (Simple Object Access Protocol)is a remote procedure call protocol designed for exchanging information in a distributed environment, where a server may consist of a hierarchy of objects.
This book describes only how to send XML-RPC and SOAP requests, not how to serve them.
Note:Web service protocols such as XML-RPC and SOAP are evolving, as is the support for them in OS X. The scripts and code samples in this document depend on third-party web services that are also subject to change. Though the samples have been tested as published, your experience may vary.
The sample code in this book can be adapted for Carbon applications, Cocoa applications, simple tools, or other code. However, there is no specific Cocoa class support provided.

## Who Should Read This Document
To take full advantage of this document, you should be familiar with AppleScript, either through writing AppleScript scripts or creating scriptable applications. You can learn more about these topics inAppleScript Documentation. In particular, seeAppleScript OverviewandApple Events Programming Guide.
You should also be familiar with the XML-RPC and SOAP protocols. You can find information on these protocols at third-party websites. For example, the XML-RPC specification is currently described athttp://www.xmlrpc.com/specand the SOAP specification athttp://www.w3.org/TR/.

## Organization of This Document
This document is organized into the following chapters:
- About AppleScriptâs Support for XML-RPC and SOAPprovides a brief introduction to the XML-RPC and SOAP protocols, then describes the scripting support in OS X version 10.1 (and later) for these protocols, including the syntax for script statements and the APIs for making remote procedure calls from applications or other code.
About AppleScriptâs Support for XML-RPC and SOAPprovides a brief introduction to the XML-RPC and SOAP protocols, then describes the scripting support in OS X version 10.1 (and later) for these protocols, including the syntax for script statements and the APIs for making remote procedure calls from applications or other code.
- Making Remote Procedure Calls From Scriptsprovides sample scripts and step by step descriptions for making XML-RPC and SOAP requests from scripts.
Making Remote Procedure Calls From Scriptsprovides sample scripts and step by step descriptions for making XML-RPC and SOAP requests from scripts.
- Making Remote Procedure Calls From Applicationsprovides sample code and step by step descriptions for making XML-RPC and SOAP requests from applications and other code.
Making Remote Procedure Calls From Applicationsprovides sample code and step by step descriptions for making XML-RPC and SOAP requests from applications and other code.
- Document Revision Historydescribes the history of this book.
Document Revision Historydescribes the history of this book.
Copyright © 2001, 2014 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2014-07-15