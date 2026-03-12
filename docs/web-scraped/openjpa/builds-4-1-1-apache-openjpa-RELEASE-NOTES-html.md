# Source: https://openjpa.apache.org/builds/4.1.1/apache-openjpa/RELEASE-NOTES.html

Title: Release Notes for Apache OpenJPA 4.1.1

URL Source: https://openjpa.apache.org/builds/4.1.1/apache-openjpa/RELEASE-NOTES.html

Markdown Content:
*   [Overview](https://openjpa.apache.org/builds/4.1.1/apache-openjpa/RELEASE-NOTES.html#Overview)
*   [Prerequisites](https://openjpa.apache.org/builds/4.1.1/apache-openjpa/RELEASE-NOTES.html#Prerequisites)
*   [Documentation](https://openjpa.apache.org/builds/4.1.1/apache-openjpa/RELEASE-NOTES.html#Documentation)
*   [Getting Involved](https://openjpa.apache.org/builds/4.1.1/apache-openjpa/RELEASE-NOTES.html#GetInvolved)
*   [License](https://openjpa.apache.org/builds/4.1.1/apache-openjpa/RELEASE-NOTES.html#License)
*   [Notice](https://openjpa.apache.org/builds/4.1.1/apache-openjpa/RELEASE-NOTES.html#Notice)
*   [Release Notes](https://openjpa.apache.org/builds/4.1.1/apache-openjpa/RELEASE-NOTES.html#ReleaseNotes)
*   [Release Notes for previous OpenJPA releases](https://openjpa.apache.org/builds/4.1.1/apache-openjpa/RELEASE-NOTES.html#Previous)

* * *

[](https://openjpa.apache.org/builds/4.1.1/apache-openjpa/RELEASE-NOTES.html)Overview
-------------------------------------------------------------------------------------

The Apache OpenJPA community is proud to release a distribution of OpenJPA 4.1.1. This distribution is based on the final Jakarta Persistence API, Version 3.1 specification while not beeing fully TCK tested. We remain backwards compatible with prior releases based on the Java Persistence API up to 3.0.

Additional information on the OpenJPA project may be found at the project web site: [http://openjpa.apache.org](http://openjpa.apache.org/)

[](https://openjpa.apache.org/builds/4.1.1/apache-openjpa/RELEASE-NOTES.html)Prerequisites
------------------------------------------------------------------------------------------

OpenJPA requires Java 11 or higher and a relational database of some sort.

[](https://openjpa.apache.org/builds/4.1.1/apache-openjpa/RELEASE-NOTES.html)Documentation
------------------------------------------------------------------------------------------

If you have questions about OpenJPA, a good source of information is the online product manual. You can find the manual for the current release as well as older releases of OpenJPA at [http://openjpa.apache.org/documentation.html](http://openjpa.apache.org/documentation.html)

If you can't find what you are looking for in the manual or would like more clarification, please post to the OpenJPA development mailing list. Information on all of the OpenJPA mailing lists may be found here: [http://openjpa.apache.org/mailing-lists.html](http://openjpa.apache.org/mailing-lists.html)

[](https://openjpa.apache.org/builds/4.1.1/apache-openjpa/RELEASE-NOTES.html)Getting Involved
---------------------------------------------------------------------------------------------

The Apache OpenJPA project is being built by the open source community for the open source community - we welcome your input and contributions!

What we are looking for:

*    Source code and fixes contributions 
*    Documentation assistance 
*    Product and feature suggestions 
*    Detailed and constructive feedback 
*    Articles and whitepapers 

How do I contribute?

*    To discuss Apache OpenJPA topics check out the mailing lists. 
*    Informal discussion also occurs on the #openjpa IRC channel on freenode.net. 
*    Bugs and other issues can be posted on [the issue tracker](https://issues.apache.org/jira/browse/OPENJPA). 

* * *

[](https://openjpa.apache.org/builds/4.1.1/apache-openjpa/RELEASE-NOTES.html)License
------------------------------------------------------------------------------------

Licensed to the Apache Software Foundation (ASF) under one or more contributor license agreements. See the NOTICE file distributed with this work for additional information regarding copyright ownership. The ASF licenses this file to you under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. 

You may obtain a copy of the License at: [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

The license may also be found in LICENSE.txt which is included in each release of OpenJPA.

[](https://openjpa.apache.org/builds/4.1.1/apache-openjpa/RELEASE-NOTES.html)Notice
-----------------------------------------------------------------------------------

Copyright 2006,2025 The Apache Software Foundation 

This product includes software developed at The Apache Software Foundation (http://www.apache.org/).

Apache OpenJPA includes the persistence and orm schemas from the JPA specifications. 

Copyright 2005-2009 Sun Microsystems, Inc. All rights reserved. 

Apache OpenJPA elects to include this software in this distribution under the CDDL license. 

You can obtain a copy of the License at: [https://glassfish.dev.java.net/public/CDDL+GPL.html](https://glassfish.dev.java.net/public/CDDL+GPL.html)

The source code is available at: [http://java.net/projects/glassfish](http://java.net/projects/glassfish)

The complete list of notices can be found in NOTICE.txt included in each assembly.

* * *

[Release Notes](https://openjpa.apache.org/builds/4.1.1/apache-openjpa/RELEASE-NOTES.html)
------------------------------------------------------------------------------------------

* * *

### [OpenJPA 4.1.1](https://openjpa.apache.org/builds/4.1.1/apache-openjpa/RELEASE-NOTES.html)

Release Notes - OpenJPA - Version 4.1.1
---------------------------------------

Bug
---

*   [[OPENJPA-2925](https://issues.apache.org/jira/browse/OPENJPA-2925)] - Accessing a non-recursive relation of an instance that has been loaded via a recursive relation may produce wrong result 
*   [[OPENJPA-2936](https://issues.apache.org/jira/browse/OPENJPA-2936)] - Usage of JPA @Index without name prevents creating schema and queries 

* * *

Copyright (C) 2006,2025 Apache Software Foundation. Licensed under Apache License 2.0.

 Apache, the Apache feather logo and OpenJPA are trademarks of Apache Software Foundation.
