# Source: https://openjpa.apache.org/openjpa-3.1.x.html

Title: Apache OpenJPA -- OpenJPA 3.1.X

URL Source: https://openjpa.apache.org/openjpa-3.1.x.html

Markdown Content:
This distribution is based on the final [JSR 338 Java Persistence API, Version 2.2](http://jcp.org/en/jsr/detail?id=338) specification.

Additional information on the OpenJPA project may be found at [the project web site](http://openjpa.apache.org/).

Changes in OpenJPA 3.1.2[¶](https://openjpa.apache.org/openjpa-3.1.x.html#changes-in-openjpa-312 "Permalink")
-------------------------------------------------------------------------------------------------------------

Bug [¶](https://openjpa.apache.org/openjpa-3.1.x.html#bug "Permalink")
----------------------------------------------------------------------

*   [[OPENJPA-2807](https://issues.apache.org/jira/browse/OPENJPA-2807)] - javax.persistence.Index#columnList should strip spaces 
*   [[OPENJPA-2810](https://issues.apache.org/jira/browse/OPENJPA-2810)] - Major version is returned instead of minor 

Improvement [¶](https://openjpa.apache.org/openjpa-3.1.x.html#improvement "Permalink")
--------------------------------------------------------------------------------------

*   [[OPENJPA-2790](https://issues.apache.org/jira/browse/OPENJPA-2790)] - Convert build from SVN to GIT 
*   [[OPENJPA-2798](https://issues.apache.org/jira/browse/OPENJPA-2798)] - OpenJPA need to be more Java11 friendly 

Task [¶](https://openjpa.apache.org/openjpa-3.1.x.html#task "Permalink")
------------------------------------------------------------------------

*   [[OPENJPA-2809](https://issues.apache.org/jira/browse/OPENJPA-2809)] - Add openjpa-junit5 helper to enhance entities at test run 
*   [[OPENJPA-2811](https://issues.apache.org/jira/browse/OPENJPA-2811)] - Upgrade to ASM 8 
*   [[OPENJPA-2812](https://issues.apache.org/jira/browse/OPENJPA-2812)] - Enable to force snake_case for column names 
*   [[OPENJPA-2813](https://issues.apache.org/jira/browse/OPENJPA-2813)] - Implement basic support of PersistenceProvidergenerateSchema 
*   [[OPENJPA-2815](https://issues.apache.org/jira/browse/OPENJPA-2815)] - Basic jakarta bundle 

Changes in OpenJPA 3.1.1[¶](https://openjpa.apache.org/openjpa-3.1.x.html#changes-in-openjpa-311 "Permalink")
-------------------------------------------------------------------------------------------------------------

Sub-task [¶](https://openjpa.apache.org/openjpa-3.1.x.html#sub-task "Permalink")
--------------------------------------------------------------------------------

*   [[OPENJPA-2713](https://issues.apache.org/jira/browse/OPENJPA-2713)] - [JPA-2.2] add support for Java8 Date/Time types 

Bug [¶](https://openjpa.apache.org/openjpa-3.1.x.html#bug_1 "Permalink")
------------------------------------------------------------------------

*   [[OPENJPA-2743](https://issues.apache.org/jira/browse/OPENJPA-2743)] - AttributeConverter fails to enhance 
*   [[OPENJPA-2799](https://issues.apache.org/jira/browse/OPENJPA-2799)] - Karaf features contains mistake on the commons-collections4 location 

Improvement [¶](https://openjpa.apache.org/openjpa-3.1.x.html#improvement_1 "Permalink")
----------------------------------------------------------------------------------------

*   [[OPENJPA-2801](https://issues.apache.org/jira/browse/OPENJPA-2801)] - Kubernetes TCPRemoteCommitProvider 

Task [¶](https://openjpa.apache.org/openjpa-3.1.x.html#task_1 "Permalink")
--------------------------------------------------------------------------

*   [[OPENJPA-2803](https://issues.apache.org/jira/browse/OPENJPA-2803)] - DBCP2 should be optional in OSGi 

Changes in OpenJPA 3.1.0[¶](https://openjpa.apache.org/openjpa-3.1.x.html#changes-in-openjpa-310 "Permalink")
-------------------------------------------------------------------------------------------------------------

Sub-task [¶](https://openjpa.apache.org/openjpa-3.1.x.html#sub-task_1 "Permalink")
----------------------------------------------------------------------------------

*   [[OPENJPA-2710](https://issues.apache.org/jira/browse/OPENJPA-2710)] - Create and update to geronimo-jpa_2.2_spec 

Bug [¶](https://openjpa.apache.org/openjpa-3.1.x.html#bug_2 "Permalink")
------------------------------------------------------------------------

*   [[OPENJPA-1993](https://issues.apache.org/jira/browse/OPENJPA-1993)] - Deadlock Potential with ORM XML Processing 
*   [[OPENJPA-2555](https://issues.apache.org/jira/browse/OPENJPA-2555)] - Timestamp precision from manual schema not respected 
*   [[OPENJPA-2567](https://issues.apache.org/jira/browse/OPENJPA-2567)] - TINY/MEDIUM/LONG TEXT fields for MySQL and MariaDB are not supported 
*   [[OPENJPA-2673](https://issues.apache.org/jira/browse/OPENJPA-2673)] - Table is not created in openjpa 3.0.0-SNAPSHOT and OSGi 
*   [[OPENJPA-2704](https://issues.apache.org/jira/browse/OPENJPA-2704)] - The openjpa.jdbc.Schema no longer overrides orm.xml default 
*   [[OPENJPA-2733](https://issues.apache.org/jira/browse/OPENJPA-2733)] - Subquery parameters are incorrectly assigned 
*   [[OPENJPA-2742](https://issues.apache.org/jira/browse/OPENJPA-2742)] - SchemaTool fails with MySQL 
*   [[OPENJPA-2746](https://issues.apache.org/jira/browse/OPENJPA-2746)] - OpenJPA Karaf feature is not complete 
*   [[OPENJPA-2756](https://issues.apache.org/jira/browse/OPENJPA-2756)] - PostgreSQL requires escaping of search strings in all versions 
*   [[OPENJPA-2757](https://issues.apache.org/jira/browse/OPENJPA-2757)] - upgrade to xbean-asm7 to support Java11 
*   [[OPENJPA-2761](https://issues.apache.org/jira/browse/OPENJPA-2761)] - problem inserting more than 4000 charcters in oracle XMLTYPE column 
*   [[OPENJPA-2764](https://issues.apache.org/jira/browse/OPENJPA-2764)] - Map path expression tests behave random 
*   [[OPENJPA-2768](https://issues.apache.org/jira/browse/OPENJPA-2768)] - XMLStore SAXParser doesn't distinguish between element and extent 
*   [[OPENJPA-2770](https://issues.apache.org/jira/browse/OPENJPA-2770)] - false boolean literal doesn't work 
*   [[OPENJPA-2771](https://issues.apache.org/jira/browse/OPENJPA-2771)] - It seems like h2 'unlimited' is not "LIMIT 0" but rather "LIMIT -1" 
*   [[OPENJPA-2772](https://issues.apache.org/jira/browse/OPENJPA-2772)] - list of h2 reserved words is incomplete 
*   [[OPENJPA-2777](https://issues.apache.org/jira/browse/OPENJPA-2777)] - Indices specified using javax.persistence.Index annotation are not being created 
*   [[OPENJPA-2780](https://issues.apache.org/jira/browse/OPENJPA-2780)] - ReverseMappingTool does not generate @Enumerated annotation 
*   [[OPENJPA-2781](https://issues.apache.org/jira/browse/OPENJPA-2781)] - OpenJPA need internet connection to read the persistence.xml 
*   [[OPENJPA-2785](https://issues.apache.org/jira/browse/OPENJPA-2785)] - Queries invoked by Spring data that have parameters fail 
*   [[OPENJPA-2791](https://issues.apache.org/jira/browse/OPENJPA-2791)] - Parsing persistence.xml throws premature end of file error 

Improvement [¶](https://openjpa.apache.org/openjpa-3.1.x.html#improvement_2 "Permalink")
----------------------------------------------------------------------------------------

*   [[OPENJPA-2745](https://issues.apache.org/jira/browse/OPENJPA-2745)] - Clean up try-catch implementation for DB2Dictionary 
*   [[OPENJPA-2747](https://issues.apache.org/jira/browse/OPENJPA-2747)] - Upgrade to JPA 2.2 and use javax.persistence-api spec 
*   [[OPENJPA-2748](https://issues.apache.org/jira/browse/OPENJPA-2748)] - commons-collections should be updated to most recent version 
*   [[OPENJPA-2750](https://issues.apache.org/jira/browse/OPENJPA-2750)] - commons-dbcp need to be updated to most recent version 
*   [[OPENJPA-2751](https://issues.apache.org/jira/browse/OPENJPA-2751)] - Code clean-up should be performed 
*   [[OPENJPA-2752](https://issues.apache.org/jira/browse/OPENJPA-2752)] - More libraries can be updated 
*   [[OPENJPA-2753](https://issues.apache.org/jira/browse/OPENJPA-2753)] - Create profiles to start various databases via Docker 
*   [[OPENJPA-2755](https://issues.apache.org/jira/browse/OPENJPA-2755)] - support MySQL DATETIME and TIMESTAMP fractions (milliseconds, nanos) 
*   [[OPENJPA-2773](https://issues.apache.org/jira/browse/OPENJPA-2773)] - set minIdle to > 0 in DBCPDriverDataSource 
*   [[OPENJPA-2775](https://issues.apache.org/jira/browse/OPENJPA-2775)] - hsqldb doesn't support NullTable to retrieve meta information 

Task [¶](https://openjpa.apache.org/openjpa-3.1.x.html#task_2 "Permalink")
--------------------------------------------------------------------------

*   [[OPENJPA-2744](https://issues.apache.org/jira/browse/OPENJPA-2744)] - commons-pool should be updated to most recent version 
*   [[OPENJPA-2754](https://issues.apache.org/jira/browse/OPENJPA-2754)] - update to latest dbcp and verify moving from maxActive to maxTotal 
*   [[OPENJPA-2758](https://issues.apache.org/jira/browse/OPENJPA-2758)] - JPA 2.2 compliance 

Dependency upgrade [¶](https://openjpa.apache.org/openjpa-3.1.x.html#dependency-upgrade "Permalink")
----------------------------------------------------------------------------------------------------

*   [[OPENJPA-2784](https://issues.apache.org/jira/browse/OPENJPA-2784)] - update docs before our release
