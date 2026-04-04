# Source: https://openjpa.apache.org/builds/3.2.0/apache-openjpa/RELEASE-NOTES.html

Title: Release Notes for Apache OpenJPA 3.2.0

URL Source: https://openjpa.apache.org/builds/3.2.0/apache-openjpa/RELEASE-NOTES.html

Markdown Content:
*   [Overview](https://openjpa.apache.org/builds/3.2.0/apache-openjpa/RELEASE-NOTES.html#Overview)
*   [Prerequisites](https://openjpa.apache.org/builds/3.2.0/apache-openjpa/RELEASE-NOTES.html#Prerequisites)
*   [Documentation](https://openjpa.apache.org/builds/3.2.0/apache-openjpa/RELEASE-NOTES.html#Documentation)
*   [Getting Involved](https://openjpa.apache.org/builds/3.2.0/apache-openjpa/RELEASE-NOTES.html#GetInvolved)
*   [License](https://openjpa.apache.org/builds/3.2.0/apache-openjpa/RELEASE-NOTES.html#License)
*   [Notice](https://openjpa.apache.org/builds/3.2.0/apache-openjpa/RELEASE-NOTES.html#Notice)
*   [Release Notes](https://openjpa.apache.org/builds/3.2.0/apache-openjpa/RELEASE-NOTES.html#ReleaseNotes)
*   [Release Notes for previous OpenJPA releases](https://openjpa.apache.org/builds/3.2.0/apache-openjpa/RELEASE-NOTES.html#Previous)

* * *

[](https://openjpa.apache.org/builds/3.2.0/apache-openjpa/RELEASE-NOTES.html)Overview
-------------------------------------------------------------------------------------

The Apache OpenJPA community is proud to release a distribution of OpenJPA 3.2.0. This distribution is based on the final JSR 338 Java Persistence API, Version 2.2 specification while not beeing fully TCK tested. We remain backwards compatible with prior releases based on the Java Persistence API 1.0 and 2.0.

Additional information on the OpenJPA project may be found at the project web site: [http://openjpa.apache.org](http://openjpa.apache.org/)

[](https://openjpa.apache.org/builds/3.2.0/apache-openjpa/RELEASE-NOTES.html)Prerequisites
------------------------------------------------------------------------------------------

OpenJPA requires Java 8 or higher and a relational database of some sort.

[](https://openjpa.apache.org/builds/3.2.0/apache-openjpa/RELEASE-NOTES.html)Documentation
------------------------------------------------------------------------------------------

If you have questions about OpenJPA, a good source of information is the online product manual. You can find the manual for the current release as well as older releases of OpenJPA at [http://openjpa.apache.org/documentation.html](http://openjpa.apache.org/documentation.html)

If you can't find what you are looking for in the manual or would like more clarification, please post to the OpenJPA development mailing list. Information on all of the OpenJPA mailing lists may be found here: [http://openjpa.apache.org/mailing-lists.html](http://openjpa.apache.org/mailing-lists.html)

[](https://openjpa.apache.org/builds/3.2.0/apache-openjpa/RELEASE-NOTES.html)Getting Involved
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

[](https://openjpa.apache.org/builds/3.2.0/apache-openjpa/RELEASE-NOTES.html)License
------------------------------------------------------------------------------------

Licensed to the Apache Software Foundation (ASF) under one or more contributor license agreements. See the NOTICE file distributed with this work for additional information regarding copyright ownership. The ASF licenses this file to you under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. 

You may obtain a copy of the License at: [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

The license may also be found in LICENSE.txt which is included in each release of OpenJPA.

[](https://openjpa.apache.org/builds/3.2.0/apache-openjpa/RELEASE-NOTES.html)Notice
-----------------------------------------------------------------------------------

Copyright 2006,2021 The Apache Software Foundation 

This product includes software developed at The Apache Software Foundation (http://www.apache.org/).

Apache OpenJPA includes the persistence and orm schemas from the JPA specifications. 

Copyright 2005-2009 Sun Microsystems, Inc. All rights reserved. 

Apache OpenJPA elects to include this software in this distribution under the CDDL license. 

You can obtain a copy of the License at: [https://glassfish.dev.java.net/public/CDDL+GPL.html](https://glassfish.dev.java.net/public/CDDL+GPL.html)

The source code is available at: [http://java.net/projects/glassfish](http://java.net/projects/glassfish)

The complete list of notices can be found in NOTICE.txt included in each assembly.

* * *

[Release Notes](https://openjpa.apache.org/builds/3.2.0/apache-openjpa/RELEASE-NOTES.html)
------------------------------------------------------------------------------------------

* * *

### [OpenJPA 3.2.0](https://openjpa.apache.org/builds/3.2.0/apache-openjpa/RELEASE-NOTES.html)

Release Notes - OpenJPA - Version 3.2.0
---------------------------------------

Sub-task
--------

*   [[OPENJPA-1594](https://issues.apache.org/jira/browse/OPENJPA-1594)] - Tests not handling new QueryTimeOut and LockTimeOut exceptions correctly 

Bug
---

*   [[OPENJPA-1303](https://issues.apache.org/jira/browse/OPENJPA-1303)] - Reserved words are not mapped correctly in table definition 
*   [[OPENJPA-2182](https://issues.apache.org/jira/browse/OPENJPA-2182)] - DB dictionaries do not properly process reserved words for column names 
*   [[OPENJPA-2648](https://issues.apache.org/jira/browse/OPENJPA-2648)] - hsqldb @Id long create table as interger instead of bigint 
*   [[OPENJPA-2731](https://issues.apache.org/jira/browse/OPENJPA-2731)] - Problems with Boolean Representation with Postgres 
*   [[OPENJPA-2788](https://issues.apache.org/jira/browse/OPENJPA-2788)] - Anonymous parameters are not being picked when adding via CriteriaBuilder 
*   [[OPENJPA-2789](https://issues.apache.org/jira/browse/OPENJPA-2789)] - JDBC connection not closed when running named query in explicitly opened connection 
*   [[OPENJPA-2795](https://issues.apache.org/jira/browse/OPENJPA-2795)] - generate foreign key indexes for Oracle 
*   [[OPENJPA-2814](https://issues.apache.org/jira/browse/OPENJPA-2814)] - Memory Leak in ForeignKey class 
*   [[OPENJPA-2821](https://issues.apache.org/jira/browse/OPENJPA-2821)] - Subclassing enhancer must use AsmAdapter 
*   [[OPENJPA-2828](https://issues.apache.org/jira/browse/OPENJPA-2828)] - org.apache.openjpa.kernel.conf.Specification.equals() : returns true even if different 
*   [[OPENJPA-2829](https://issues.apache.org/jira/browse/OPENJPA-2829)] - javax script execution does not ignore empty lines 
*   [[OPENJPA-2830](https://issues.apache.org/jira/browse/OPENJPA-2830)] - javax.persistence.sql-load-script-source does not support ";" in strings 
*   [[OPENJPA-2832](https://issues.apache.org/jira/browse/OPENJPA-2832)] - DROP COLUMN does not use delimiters and always add double quotes 
*   [[OPENJPA-2834](https://issues.apache.org/jira/browse/OPENJPA-2834)] - Performance issue while deploying in Wildfly EAP with OpenJPA-3.1.1 
*   [[OPENJPA-2842](https://issues.apache.org/jira/browse/OPENJPA-2842)] - openjpa.Log=log4j vs log4j2 - reintroduce log4j support and add explicit log4j2 support 
*   [[OPENJPA-2843](https://issues.apache.org/jira/browse/OPENJPA-2843)] - try to get rid of com.ibm dependency 
*   [[OPENJPA-2846](https://issues.apache.org/jira/browse/OPENJPA-2846)] - Enhancement does not work with JDK 16 
*   [[OPENJPA-2849](https://issues.apache.org/jira/browse/OPENJPA-2849)] - select(max) etc of LocalDate, LocalDateTime etc leads to ClassCastException 
*   [[OPENJPA-2850](https://issues.apache.org/jira/browse/OPENJPA-2850)] - [MSSQL] BLOB column type is not supported 
*   [[OPENJPA-2851](https://issues.apache.org/jira/browse/OPENJPA-2851)] - argument CURRENT_DATE cannot handle java.time.LocalDateTime entity fields 
*   [[OPENJPA-2854](https://issues.apache.org/jira/browse/OPENJPA-2854)] - fix OffsetTime handling for PostgreSQL 
*   [[OPENJPA-2855](https://issues.apache.org/jira/browse/OPENJPA-2855)] - primary keys do no respect naming rules 
*   [[OPENJPA-2856](https://issues.apache.org/jira/browse/OPENJPA-2856)] - [MariaDB] improve TIME handling 
*   [[OPENJPA-2857](https://issues.apache.org/jira/browse/OPENJPA-2857)] - [MariaDB] locking in some cases gets handled via sqlState 70100 
*   [[OPENJPA-2858](https://issues.apache.org/jira/browse/OPENJPA-2858)] - update dbcp2 to 2.8.0 
*   [[OPENJPA-2859](https://issues.apache.org/jira/browse/OPENJPA-2859)] - [HSQLDB] HSQLDictionary wrongly maps double to NUMERIC without precision 
*   [[OPENJPA-2860](https://issues.apache.org/jira/browse/OPENJPA-2860)] - [Postgres] use setQueryTimeout for PostgreSQL >= 10 
*   [[OPENJPA-2861](https://issues.apache.org/jira/browse/OPENJPA-2861)] - select sum(CASE x WHEN x THEN 1 ELSE 0 ) returns String instead of Long. 
*   [[OPENJPA-2862](https://issues.apache.org/jira/browse/OPENJPA-2862)] - select SUM doesn't return spec defined types 
*   [[OPENJPA-2863](https://issues.apache.org/jira/browse/OPENJPA-2863)] - java.time.LocalDateTime in Oracle gets rounded to just 3 digits 
*   [[OPENJPA-2864](https://issues.apache.org/jira/browse/OPENJPA-2864)] - respect the Columns precision when persisting a java.sql.Timestamp value 
*   [[OPENJPA-2865](https://issues.apache.org/jira/browse/OPENJPA-2865)] - [Oracle] use native java.time JDBC features 
*   [[OPENJPA-2866](https://issues.apache.org/jira/browse/OPENJPA-2866)] - [Oracle] add GenerationType#IDENTITY support for Oracle 
*   [[OPENJPA-2871](https://issues.apache.org/jira/browse/OPENJPA-2871)] - upgrade to xbean-4.20 to remove transitive ASM dependency 

New Feature
-----------

*   [[OPENJPA-2816](https://issues.apache.org/jira/browse/OPENJPA-2816)] - Add HerdDB DBDictionary 
*   [[OPENJPA-2873](https://issues.apache.org/jira/browse/OPENJPA-2873)] - Add ProductDerivation for persistence_2_2.xsd 

Improvement
-----------

*   [[OPENJPA-84](https://issues.apache.org/jira/browse/OPENJPA-84)] - Escape sql reserved words in column names 
*   [[OPENJPA-2665](https://issues.apache.org/jira/browse/OPENJPA-2665)] - refactore code to use more Java7 features. 
*   [[OPENJPA-2765](https://issues.apache.org/jira/browse/OPENJPA-2765)] - Fix documentation of JPA spec compliance 
*   [[OPENJPA-2820](https://issues.apache.org/jira/browse/OPENJPA-2820)] - Track when a DBIdentifier is already delimited in order to save memory allocations and cpu 
*   [[OPENJPA-2822](https://issues.apache.org/jira/browse/OPENJPA-2822)] - enhancer can rely on at least java8 
*   [[OPENJPA-2823](https://issues.apache.org/jira/browse/OPENJPA-2823)] - treat jakarta.* as spec class in enhancer 
*   [[OPENJPA-2852](https://issues.apache.org/jira/browse/OPENJPA-2852)] - Maven Plugin should be marked thread safe 
*   [[OPENJPA-2853](https://issues.apache.org/jira/browse/OPENJPA-2853)] - [MSSQL Server] support sendTimeAsDatetime handling 
*   [[OPENJPA-2867](https://issues.apache.org/jira/browse/OPENJPA-2867)] - generate list of reserved Words via unit test 
*   [[OPENJPA-2868](https://issues.apache.org/jira/browse/OPENJPA-2868)] - update reserved column names list for various of our DBDictionaries 
*   [[OPENJPA-2870](https://issues.apache.org/jira/browse/OPENJPA-2870)] - update specification-version to 2.2 

Task
----

*   [[OPENJPA-2819](https://issues.apache.org/jira/browse/OPENJPA-2819)] - Add simple GitHub Actions validation for Pull Requests 
*   [[OPENJPA-2824](https://issues.apache.org/jira/browse/OPENJPA-2824)] - When @OpenJPASupport (junit5 extension) is used, ensure to not do auto enhancement more than once 
*   [[OPENJPA-2831](https://issues.apache.org/jira/browse/OPENJPA-2831)] - Import commons-collections4 classes instead of the dependency in openjpa-lib 
*   [[OPENJPA-2833](https://issues.apache.org/jira/browse/OPENJPA-2833)] - Upgrade to ASM 9 
*   [[OPENJPA-2835](https://issues.apache.org/jira/browse/OPENJPA-2835)] - update to xbean-asm9 for Java16 support 
*   [[OPENJPA-2838](https://issues.apache.org/jira/browse/OPENJPA-2838)] - Add a JUL LogFactory 
*   [[OPENJPA-2840](https://issues.apache.org/jira/browse/OPENJPA-2840)] - Enable a light SPI for asm support in kernel module 

* * *

[](https://openjpa.apache.org/builds/3.2.0/apache-openjpa/RELEASE-NOTES.html)Previous Releases
----------------------------------------------------------------------------------------------

Release notes for earlier releases of OpenJPA may be found in our repos at the following locations.

*   [OpenJPA 3.1.2 RELEASE-NOTES.html](https://github.com/apache/openjpa/blob/3.1.2/openjpa-project/RELEASE-NOTES.html)
*   [OpenJPA 3.1.1 RELEASE-NOTES.html](https://github.com/apache/openjpa/blob/3.1.1/openjpa-project/RELEASE-NOTES.html)
*   [OpenJPA 3.1.0 RELEASE-NOTES.html](https://github.com/apache/openjpa/blob/3.1.0/openjpa-project/RELEASE-NOTES.html)
*   [OpenJPA 3.0.0 RELEASE-NOTES.html](https://github.com/apache/openjpa/blob/3.0.0/openjpa-project/RELEASE-NOTES.html)
*   [OpenJPA 2.4.3 RELEASE-NOTES.html](http://svn.apache.org/viewvc/openjpa/tags/2.4.3/openjpa-project/RELEASE-NOTES.html?view=co)
*   [OpenJPA 2.4.2 RELEASE-NOTES.html](http://svn.apache.org/viewvc/openjpa/tags/2.4.2/openjpa-project/RELEASE-NOTES.html?view=co)
*   [OpenJPA 2.4.1 RELEASE-NOTES.html](http://svn.apache.org/viewvc/openjpa/tags/2.4.1/openjpa-project/RELEASE-NOTES.html?view=co)
*   [OpenJPA 2.4.0 RELEASE-NOTES.html](http://svn.apache.org/viewvc/openjpa/tags/2.4.0/openjpa-project/RELEASE-NOTES.html?view=co)
*   [OpenJPA 2.3.0 RELEASE-NOTES.html](http://svn.apache.org/viewvc/openjpa/tags/2.3.0/openjpa-project/RELEASE-NOTES.html?view=co)
*   [OpenJPA 2.2.2 RELEASE-NOTES.html](http://svn.apache.org/viewvc/openjpa/tags/2.2.2/openjpa-project/RELEASE-NOTES.html?view=co)
*   [OpenJPA 2.2.1 RELEASE-NOTES.html](http://svn.apache.org/viewvc/openjpa/tags/2.2.1/openjpa-project/RELEASE-NOTES.html?view=co)
*   [OpenJPA 2.2.0 RELEASE-NOTES.html](http://svn.apache.org/viewvc/openjpa/tags/2.2.0/openjpa-project/RELEASE-NOTES.html?view=co)
*   [OpenJPA 2.1.1 RELEASE-NOTES.html](http://svn.apache.org/viewvc/openjpa/tags/2.1.1/openjpa-project/RELEASE-NOTES.html?view=co)
*   [OpenJPA 2.1.1 RELEASE-NOTES.html](http://svn.apache.org/viewvc/openjpa/tags/2.1.1/openjpa-project/RELEASE-NOTES.html?view=co)
*   [OpenJPA 2.1.0 RELEASE-NOTES.html](http://svn.apache.org/viewvc/openjpa/tags/2.1.0/openjpa-project/RELEASE-NOTES.html?view=co)
*   [OpenJPA 2.0.1 RELEASE-NOTES.html](http://svn.apache.org/viewvc/openjpa/tags/2.0.1/openjpa-project/RELEASE-NOTES.html?view=co)
*   [OpenJPA 2.0.0 RELEASE-NOTES.html](http://svn.apache.org/viewvc/openjpa/tags/2.0.0/openjpa-project/RELEASE-NOTES.html?view=co)
*   [OpenJPA 2.0.0-Beta 3 RELEASE-NOTES.html](http://svn.apache.org/viewvc/openjpa/tags/2.0.0-beta3/openjpa-project/RELEASE-NOTES.html?view=co)
*   [OpenJPA 2.0.0-Beta 2 RELEASE-NOTES.html](http://svn.apache.org/viewvc/openjpa/tags/2.0.0-beta2/openjpa-project/RELEASE-NOTES.html?view=co)
*   [OpenJPA 2.0.0-Beta RELEASE-NOTES.html](http://svn.apache.org/viewvc/openjpa/tags/2.0.0-beta/openjpa-project/RELEASE-NOTES.html?view=co)
*   [OpenJPA 2.0.0-Milestone 3 RELEASE-NOTES.html](http://svn.apache.org/viewvc/openjpa/tags/2.0.0-M3/openjpa-project/RELEASE-NOTES.html?view=co)
*   [OpenJPA 1.2.2 RELEASE-NOTES.html](http://svn.apache.org/viewvc/openjpa/tags/1.2.2/openjpa-project/RELEASE-NOTES.html?view=co)
*   [OpenJPA 1.2.2 RELEASE-NOTES.html](http://svn.apache.org/viewvc/openjpa/tags/1.2.2/openjpa-project/RELEASE-NOTES.html?view=co)
*   [OpenJPA 1.2.1 RELEASE-NOTES.html](http://svn.apache.org/viewvc/openjpa/tags/1.2.1/openjpa-project/RELEASE-NOTES.html?view=co)
*   [OpenJPA 1.1.0 RELEASE-NOTES.html](http://svn.apache.org/viewvc/openjpa/tags/1.1.0/openjpa-project/RELEASE-NOTES.html?view=co)
*   [OpenJPA 1.0.4 RELEASE-NOTES.html](http://svn.apache.org/viewvc/openjpa/tags/1.0.4/openjpa-project/RELEASE-NOTES.html?view=co)
*   [OpenJPA 1.0.3 RELEASE-NOTES.html](http://svn.apache.org/viewvc/openjpa/tags/1.0.3/openjpa-project/RELEASE-NOTES.html?view=co)

* * *

Copyright (C) 2006,2021 Apache Software Foundation. Licensed under Apache License 2.0.

 Apache, the Apache feather logo and OpenJPA are trademarks of Apache Software Foundation.
