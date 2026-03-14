# Source: https://jmeter.apache.org/usermanual/build-db-test-plan.html

Title: Building a Simple Database Test Plan

URL Source: https://jmeter.apache.org/usermanual/build-db-test-plan.html

Published Time: Sun, 07 Jan 2024 17:19:24 GMT

Markdown Content:
Apache JMeter - User's Manual: Building a Simple Database Test Plan
===============
[Main content](https://jmeter.apache.org/usermanual/build-db-test-plan.html#content)

[![Image 1: Logo ASF](https://jmeter.apache.org/images/asf-logo.svg)](https://www.apache.org/)

[![Image 2: Apache JMeter](https://jmeter.apache.org/images/logo.svg)](https://jmeter.apache.org/)

[![Image 3: Current Apache event teaser](https://www.apache.org/events/current-event-234x60.png)](https://www.apache.org/events/current-event.html)

*   About 
    *   [Overview](https://jmeter.apache.org/index.html)
    *   [License](https://www.apache.org/licenses/)

*   Download 
    *   [Download Releases](https://jmeter.apache.org/download_jmeter.cgi)
    *   [Release Notes](https://jmeter.apache.org/changes.html)

*   Documentation 
    *   [Get Started](https://jmeter.apache.org/usermanual/get-started.html)
    *   [User Manual](https://jmeter.apache.org/usermanual/index.html)
    *   [Best Practices](https://jmeter.apache.org/usermanual/best-practices.html)
    *   [Component Reference](https://jmeter.apache.org/usermanual/component_reference.html)
    *   [Functions Reference](https://jmeter.apache.org/usermanual/functions.html)
    *   [Properties Reference](https://jmeter.apache.org/usermanual/properties_reference.html)
    *   [Change History](https://jmeter.apache.org/changes_history.html)
    *   [Javadocs](https://jmeter.apache.org/api/index.html)
    *   [JMeter Wiki](https://cwiki.apache.org/confluence/display/JMETER/Home)
    *   [FAQ (Wiki)](https://cwiki.apache.org/confluence/display/JMETER/JMeterFAQ)

*   Tutorials 
    *   [Distributed Testing](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.html)
    *   [Recording Tests](https://jmeter.apache.org/usermanual/jmeter_proxy_step_by_step.html)
    *   [JUnit Sampler](https://jmeter.apache.org/usermanual/junitsampler_tutorial.html)
    *   [Access Log Sampler](https://jmeter.apache.org/usermanual/jmeter_accesslog_sampler_step_by_step.html)
    *   [Extending JMeter](https://jmeter.apache.org/usermanual/jmeter_tutorial.html)

*   Community 
    *   [Issue Tracking](https://jmeter.apache.org/issues.html)
    *   [Security](https://jmeter.apache.org/security.html)
    *   [Mailing Lists](https://jmeter.apache.org/mail.html)
    *   [Source Repositories](https://jmeter.apache.org/svnindex.html)
    *   [Building and Contributing](https://jmeter.apache.org/building.html)
    *   [Project info at Apache](https://projects.apache.org/project.html?jmeter)
    *   [Contributors](https://cwiki.apache.org/confluence/display/JMETER/JMeterCommitters)

*   Foundation 
    *   [The Apache Software Foundation (ASF)](https://www.apache.org/)
    *   [Get Involved in the ASF](https://www.apache.org/foundation/getinvolved.html)
    *   [Privacy Policy](https://privacy.apache.org/policies/privacy-policy-public.html)
    *   [Sponsorship](https://www.apache.org/foundation/sponsorship.html)
    *   [Thanks](https://www.apache.org/foundation/thanks.html)

*   [Twitter](https://twitter.com/ApacheJMeter "Follow us on Twitter")
*   [github](https://github.com/apache/jmeter "Fork us on github")

*   [< Prev](https://jmeter.apache.org/usermanual/build-adv-web-test-plan.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/build-ftp-test-plan.html)

6. Building a Database Test Plan[¶](https://jmeter.apache.org/usermanual/build-db-test-plan.html#building "Link to here")
=========================================================================================================================

In this section, you will learn how to create a basic [Test Plan](https://jmeter.apache.org/usermanual/build-test-plan.html) to test a database server. You will create fifty users that send 2 SQL requests to the database server. Also, you will tell the users to run their tests 100 times. So, the total number of requests is (50 users) x (2 requests) x (repeat 100 times) = 10'000 JDBC requests. To construct the Test Plan, you will use the following elements: [Thread Group](https://jmeter.apache.org/usermanual/test_plan.html#thread_group), [JDBC Request](https://jmeter.apache.org/usermanual/component_reference.html#JDBC_Request), [Summary Report](https://jmeter.apache.org/usermanual/component_reference.html#Summary_Report).

 This example uses the MySQL database driver. To use this driver, its containing .jar file (ex. mysql-connector-java-X.X.X-bin.jar) must be copied to the JMeter ./lib directory (see [JMeter's Classpath](https://jmeter.apache.org/usermanual/get-started.html#classpath) for more details). 

6.1 Adding Users[¶](https://jmeter.apache.org/usermanual/build-db-test-plan.html#adding_users "Link to here")
=============================================================================================================

The first step you want to do with every JMeter Test Plan is to add a [Thread Group](https://jmeter.apache.org/usermanual/test_plan.html#thread_group) element. The Thread Group tells JMeter the number of users you want to simulate, how often the users should send requests, and how many requests they should send.

Go ahead and add the ThreadGroup element by first selecting the Test Plan, clicking your right mouse button to get the Add menu, and then select Add→ThreadGroup.

You should now see the Thread Group element under Test Plan. If you do not see the element, then _expand_ the Test Plan tree by clicking on the Test Plan element.

Next, you need to modify the default properties. Select the Thread Group element in the tree, if you have not already selected it. You should now see the Thread Group Control Panel in the right section of the JMeter window (see Figure 6.1 below)

[![Image 4: Figure 6.1. Thread Group with Default Values](https://jmeter.apache.org/images/screenshots/jdbctest/threadgroup1.png)](https://jmeter.apache.org/images/screenshots/jdbctest/threadgroup1.png)

 Figure 6.1. Thread Group with Default Values

Start by providing a more descriptive name for our Thread Group. In the name field, enter JDBC Users.

 You will need a valid database, database table, and user-level access to that table. In the example shown here, the database is 'cloud' and the table name is 'vm_instance'. 

Next, increase the number of users to 50.

In the next field, the Ramp-Up Period, leave the value of 10 seconds. This property tells JMeter how long to delay between starting each user. For example, if you enter a Ramp-Up Period of 10 seconds, JMeter will finish starting all of your users by the end of the 10 seconds. So, if we have 50 users and a 10 second Ramp-Up Period, then the delay between starting users would be 200 milliseconds (10 seconds / 50 users = 0.2 second per user). If you set the value to 0, then JMeter will immediately start all of your users.

Finally, enter a value of 100 in the Loop Count field. This property tells JMeter how many times to repeat your test. To have JMeter repeatedly run your Test Plan, select the Forever checkbox.

In most applications, you have to manually accept changes you make in a Control Panel. However, in JMeter, the Control Panel automatically accepts your changes as you make them. If you change the name of an element, the tree will be updated with the new text after you leave the Control Panel (for example, when selecting another tree element).

See Figure 6.2 for the completed JDBC Users Thread Group.

[![Image 5: Figure 6.2. JDBC Users Thread Group](https://jmeter.apache.org/images/screenshots/jdbctest/threadgroup2.png)](https://jmeter.apache.org/images/screenshots/jdbctest/threadgroup2.png)

 Figure 6.2. JDBC Users Thread Group

6.2 Adding JDBC Requests[¶](https://jmeter.apache.org/usermanual/build-db-test-plan.html#adding_requests "Link to here")
========================================================================================================================

Now that we have defined our users, it is time to define the tasks that they will be performing. In this section, you will specify the JDBC requests to perform.

Begin by selecting the JDBC Users element. Click your right mouse button to get the **Add** menu, and then select Add→Config Element→JDBC Connection Configuration. Then, select this new element to view its Control Panel (see Figure 6.3).

Set up the following fields (these assume we will be using a MySQL database called 'cloud'):

*    Variable name (here: myDatabase) bound to pool. This needs to uniquely identify the configuration. It is used by the JDBC Sampler to identify the configuration to be used. 
*    Database URL: jdbc:mysql://ipOfTheServer:3306/cloud
*    JDBC Driver class: com.mysql.jdbc.Driver
*    Username: _the username of database_
*    Password: _password for the username_

The other fields on the screen can be left as the defaults.

JMeter creates a database connection pool with the configuration settings as specified in the Control Panel. The pool is referred to in JDBC Requests in the 'Variable Name' field. Several different JDBC Configuration elements can be used, but they must have unique names. Every JDBC Request must refer to a JDBC Configuration pool. More than one JDBC Request can refer to the same pool.

[![Image 6: Figure 6.3. JDBC Configuration](https://jmeter.apache.org/images/screenshots/jdbctest/jdbc-config.png)](https://jmeter.apache.org/images/screenshots/jdbctest/jdbc-config.png)

 Figure 6.3. JDBC Configuration

Selecting the JDBC Users element again. Click your right mouse button to get the **Add** menu, and then select Add→Sampler→JDBC Request. Then, select this new element to view its Control Panel (see Figure 6.4).

[![Image 7: Figure 6.4. JDBC Request](https://jmeter.apache.org/images/screenshots/jdbctest/JDBCRequest.png)](https://jmeter.apache.org/images/screenshots/jdbctest/JDBCRequest.png)

 Figure 6.4. JDBC Request

In our Test Plan, we will make two JDBC requests. The first one is for select all 'Running' VM instances, and the second is to select 'Expunging' VM instance (obviously you should change these to examples appropriate for your particular database). These are illustrated below.

JMeter sends requests in the order that you add them to the tree.

Start by editing the following properties (see Figure 6.5):

*    Change the Name to 'VM Running'. 
*    Enter the Pool Name: 'myDatabase' (same as in the configuration element) 
*   Enter the SQL Query String field.
*    Enter the Parameter values field with 'Running' value. 
*    Enter the Parameter types with 'VARCHAR'. 

[![Image 8: Figure 6.5. JDBC Request for the first SQL request](https://jmeter.apache.org/images/screenshots/jdbctest/JDBCRequest2.png)](https://jmeter.apache.org/images/screenshots/jdbctest/JDBCRequest2.png)

 Figure 6.5. JDBC Request for the first SQL request

Next, add the second JDBC Request and edit the following properties (see Figure 6.6):

*    Change the Name to 'VM Expunging'. 
*    Change the value of Parameter values to 'Expunging'. 

[![Image 9: Figure 6.6. JDBC Request for the second request](https://jmeter.apache.org/images/screenshots/jdbctest/JDBCRequest3.png)](https://jmeter.apache.org/images/screenshots/jdbctest/JDBCRequest3.png)

 Figure 6.6. JDBC Request for the second request

6.3 Adding a Listener to View/Store the Test Results[¶](https://jmeter.apache.org/usermanual/build-db-test-plan.html#adding_listener "Link to here")
====================================================================================================================================================

The final element you need to add to your Test Plan is a [Listener](https://jmeter.apache.org/usermanual/component_reference.html#listeners). This element is responsible for storing all of the results of your JDBC requests in a file and presenting the results.

Select the _JDBC Users_ element and add a [Summary Report](https://jmeter.apache.org/usermanual/component_reference.html#Summary_Report) listener (Add→Listener→Summary Report).

Save the test plan, and run the test with the menu Run→Start or Ctrl+R

The listener shows the results.

[![Image 10: Figure 6.7. Graph results Listener](https://jmeter.apache.org/images/screenshots/jdbctest/jdbc-results.png)](https://jmeter.apache.org/images/screenshots/jdbctest/jdbc-results.png)

 Figure 6.7. Graph results Listener

*   [< Prev](https://jmeter.apache.org/usermanual/build-adv-web-test-plan.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/build-ftp-test-plan.html)

 Share this page: 
*   [share](https://jmeter.apache.org/usermanual/build-db-test-plan.html "Share on facebook")
*   [tweet](https://jmeter.apache.org/usermanual/build-db-test-plan.html "Tweet on twitter")

[Go to top](https://jmeter.apache.org/usermanual/build-db-test-plan.html#top)

 Copyright © 1999 – 2024 , Apache Software Foundation 

Apache, Apache JMeter, JMeter, the Apache feather, and the Apache JMeter logo are trademarks of the Apache Software Foundation.
