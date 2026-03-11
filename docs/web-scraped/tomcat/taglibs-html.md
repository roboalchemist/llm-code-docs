# Source: https://tomcat.apache.org/taglibs.html

Title: Apache Tomcat® - Apache Taglibs

URL Source: https://tomcat.apache.org/taglibs.html

Markdown Content:
Apache Taglibs provides open source implementations of Tag Libraries for use with Java Server Pages (JSPs). In particular, it hosts the Apache Standard Taglib, an open source implementation of the [Java Standard Tag Library (JSTL)](https://jcp.org/en/jsr/detail?id=52) specification.

The Apache Standard Taglib implements JSTL 1.2 and supports request-time expressions that are evaluated by the JSP container.

In addition, compatibility for applications using 1.0 expression language tags can be enabled in one of two ways:

*   Using the **-jstlel** jar supports JSTL 1.0 EL expressions by using the EL implementation originally defined by JSTL itself. 
*   Using the **-compat** jar supports JSTL 1.0 EL expressions by using the container's implementation of EL to take advantage of newer functionality and potential performance improvements in more modern versions. 

[Download](https://tomcat.apache.org/download-taglibs.cgi) | [Changes](https://tomcat.apache.org/taglibs/CHANGES.txt)

Please see the [README](https://www.apache.org/dist/tomcat/taglibs/taglibs-standard-1.2.5/README_bin.txt) file for more detailed information on using the library.

For performance reasons the XML tags use Apache Xalan directly for evaluating XPath expressions. The Xalan 2.7.1 implementation jars xalan.jar and serializer.jar must be added to the classpath.

The Standard Taglib jars may be packaged with a web-application in its /WEB-INF/lib directory, or may be made available to all applications in a container by adding them to the container's classpath.

Apache Taglibs were originally developed as part of the Apache Jakarta project. That project has [officially been retired](http://attic.apache.org/projects/jakarta-taglibs.html) and the original tag libraries moved to the [Apache Attic](http://attic.apache.org/).
