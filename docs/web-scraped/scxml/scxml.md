# Source: https://commons.apache.org/scxml/

Title: SCXML - Commons SCXML

URL Source: https://commons.apache.org/scxml/

Markdown Content:
[State Chart XML (SCXML)](http://www.w3.org/TR/scxml/) is currently a Working Draft specification published by the World Wide Web Consortium (W3C). SCXML provides a generic state-machine based execution environment based on Harel State Tables. SCXML is a candidate for the control language within multiple markup languages coming out of the W3C (see the latest Working Draft for details). _Commons SCXML_ is an implementation aimed at creating and maintaining a Java SCXML engine capable of executing a state machine defined using a SCXML document, while abstracting out the environment interfaces.

![Image 1: Development cycle when using Commons SCXML](https://commons.apache.org/proper/commons-scxml/images/scxml-dev-cycle.png)

The use cases for an SCXML engine are multiple and varied. Anything that can be represented as a UML state chart -- business process flows, view navigation bits, interaction or dialog management, and many more -- can leverage an SCXML engine library.

Commons SCXML 2.0 Roadmap[](https://commons.apache.org/scxml/)
--------------------------------------------------------------

The current development for Commons SCXML is targeted towards a 2.0 release which will be aligned and compliant with the SCXML specification.

A high-level overview of the technical and functional changes needed towards this goal are available on the [Commons SCXML 2.0 Roadmap](https://commons.apache.org/proper/commons-scxml/roadmap.html).

Documentation[](https://commons.apache.org/scxml/)
--------------------------------------------------

Latest documentation is available:

*   The latest [Javadoc](https://commons.apache.org/proper/commons-scxml/apidocs/index.html).
*   The latest [source](https://commons.apache.org/proper/commons-scxml/xref/index.html).
*   The [wiki](http://wiki.apache.org/commons/SCXML).
*   Commons SCXML [usecases](https://commons.apache.org/proper/commons-scxml/usecases.html) (case studies).
*   A [user guide](https://commons.apache.org/proper/commons-scxml/guide.html) containing assorted API notes and tutorials.

Documentation for the most recent release is also available via the left side menu bar.

Releases[](https://commons.apache.org/scxml/)
---------------------------------------------

The latest release is v0.9. Read [v0.9 release notes](http://svn.apache.org/viewvc/commons/proper/scxml/tags/SCXML_0_9/RELEASE-NOTES.txt?view=markup) before upgrading. [Download v0.9!](http://commons.apache.org/scxml/download_scxml.cgi)

The first release was v0.5. The initial release version number was chosen to be 0.5 (rather than a 1.0) to better convey the fact that the underlying W3C specification is still a Working Draft, and subsequent changes to the Draft may warrant changes to portions of the library API. The core Commons SCXML APIs (SCXMLParser, SCXMLExecutor etc.) are stable. Portions such as processing of <datamodel> and <invoke> SCXML elements, on the other hand, are subject to change as further changes are expected in these sections of the W3C Working Draft. See Working Draft for details.

Support[](https://commons.apache.org/scxml/)
--------------------------------------------

The [commons mailing lists](https://commons.apache.org/proper/commons-scxml/mail-lists.html) act as the main support forum. The user list is suitable for most library usage queries. The dev list is intended for the development discussion. Please remember that the lists are shared between all commons components, so prefix your email by [SCXML].

Issues may be reported via [ASF JIRA](https://commons.apache.org/proper/commons-scxml/issue-tracking.html).

Who is using it?[](https://commons.apache.org/scxml/)
-----------------------------------------------------

Projects that use Commons SCXML:

Related Projects[](https://commons.apache.org/scxml/)
-----------------------------------------------------

Related projects providing some SCXML-related functionality (based on Commons SCXML 0.9):

*   [Commons SCXML - Eclipse](http://commons.apache.org/sandbox/gsoc/2010/scxml-eclipse/) - This project aims to provide an Eclipse and GMF based visual editor and debugger for SCXML, which can also be used to generate SCXML documents and code from a state chart. 
*   [SCION](https://github.com/jbeard4/SCION) - SCION provides an implementation of SCXML in portable JavaScript. 
In the browser, SCION can be used to facilitate the development of rich, web-based user interfaces with complex behavioural requirements; on the server, SCION can be used to manage asynchronous control flow.

*   [SCION-Java](https://github.com/jbeard4/SCION-Java) - SCION-Java provides lightweight bindings to the SCION library for Java. 
*   [scxmlgui](http://code.google.com/p/scxmlgui/) - This project aims to provide a simple GUI to edit SCXML state charts.
