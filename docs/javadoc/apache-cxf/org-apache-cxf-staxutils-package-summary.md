# Package org.apache.cxf.staxutils

---

package org.apache.cxf.staxutils

- 

Related Packages

Package
Description
org.apache.cxf

Contains the Bus, which is the central touch point of CXF, and its related classes.

org.apache.cxf.staxutils.transform
 
org.apache.cxf.staxutils.validation
 

- 

Class
Description
AbstractDOMStreamReader<T,I>

Abstract logic for creating XMLStreamReader from DOM documents.

AbstractDOMStreamReader.ElementFrame<T,I>
 
AutoCloseableXMLStreamReader
 
CachingXmlEventWriter
 
CachingXmlEventWriter.NSContext
 
DelegatingXMLStreamWriter
 
DepthExceededStaxException
 
DepthRestrictingStreamReader

XMLStreamReader implementation which can be used to enforce a number of
 depth-restricting policies.

DepthXMLStreamReader
 
DocumentDepthProperties
 
FastStack<T>
 
FragmentStreamReader

Wraps a XMLStreamReader and provides optional START_DOCUMENT and END_DOCUMENT events.

OverlayW3CDOMStreamWriter

Special StreamWriter that will "overlay" any write events onto the DOM.

PartialXMLStreamReader

Read from a StaX reader, stopping when the next element is a specified element.

PrettyPrintXMLStreamWriter
 
PropertiesExpandingStreamReader

A StreamReaderDelegate that expands property references in element and attribute values.

StaxSource
 
StaxStreamFilter
 
StaxUtils
 
StaxUtils.StreamToDOMContext
 
StreamWriterContentHandler
 
W3CDOMStreamReader
 
W3CDOMStreamWriter
 
W3CNamespaceContext
 
XMLStreamReaderWrapper

Interface for XMLStreamReader wrappers