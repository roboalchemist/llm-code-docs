# Source: https://jmeter.apache.org/usermanual/index.html

Title: Apache JMeter - User's Manual

URL Source: https://jmeter.apache.org/usermanual/index.html

Markdown Content:
Apache JMeter - User's Manual
===============
[Main content](https://jmeter.apache.org/usermanual/index.html#content)

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

*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/get-started.html)

User's Manual[¶](https://jmeter.apache.org/usermanual/index.html#index "Link to here")
======================================================================================

Click on the section name to go straight to the section. Click on the "+" to go to the relevant section of the detailed section list, where you can select individual subsections.

Section Summary[¶](https://jmeter.apache.org/usermanual/index.html#summary "Link to here")
------------------------------------------------------------------------------------------

*   [Changes](https://jmeter.apache.org/changes.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#get-started)...[1. Getting Started](https://jmeter.apache.org/usermanual/get-started.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#build-test-plan)...[2. Building a Test Plan](https://jmeter.apache.org/usermanual/build-test-plan.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#test_plan)...[3. Elements of a Test Plan](https://jmeter.apache.org/usermanual/test_plan.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#build-web-test-plan)...[4. Building a Web Test Plan](https://jmeter.apache.org/usermanual/build-web-test-plan.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#build-adv-web-test-plan)...[5. Building an Advanced Web Test Plan](https://jmeter.apache.org/usermanual/build-adv-web-test-plan.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#build-db-test-plan)...[6. Building a Database Test Plan](https://jmeter.apache.org/usermanual/build-db-test-plan.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#build-ftp-test-plan)...[7. Building an FTP Test Plan](https://jmeter.apache.org/usermanual/build-ftp-test-plan.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#build-ldap-test-plan)...[8a. Building an LDAP Test Plan](https://jmeter.apache.org/usermanual/build-ldap-test-plan.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#build-ldapext-test-plan)...[8b. Building an Extended LDAP Test Plan](https://jmeter.apache.org/usermanual/build-ldapext-test-plan.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#build-ws-test-plan)...[9. Building a Webservice Test Plan](https://jmeter.apache.org/usermanual/build-ws-test-plan.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#build-jms-point-to-point-test-plan)...[10. Building a JMS Point to point Test Plan](https://jmeter.apache.org/usermanual/build-jms-point-to-point-test-plan.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#build-jms-topic-test-plan)...[11. Building a JMS Topic Test Plan](https://jmeter.apache.org/usermanual/build-jms-topic-test-plan.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#build-programmatic-test-plan)...[11. Building a Test Plan Programmatically](https://jmeter.apache.org/usermanual/build-programmatic-test-plan.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#listeners)...[12. Listeners](https://jmeter.apache.org/usermanual/listeners.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#remote-test)...[13. Remote Testing](https://jmeter.apache.org/usermanual/remote-test.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#generating-dashboard)...[14. Dashboard Report](https://jmeter.apache.org/usermanual/generating-dashboard.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#realtime-results)...[15. Real time Results](https://jmeter.apache.org/usermanual/realtime-results.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#best-practices)...[16. Best Practices](https://jmeter.apache.org/usermanual/best-practices.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#boss)...[17. Help! My boss wants me to load test our web app!](https://jmeter.apache.org/usermanual/boss.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#component_reference)...[18. Component Reference](https://jmeter.apache.org/usermanual/component_reference.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#properties_reference)...[19. Properties Reference](https://jmeter.apache.org/usermanual/properties_reference.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#functions)...[20. Functions](https://jmeter.apache.org/usermanual/functions.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#regex)...[21. Regular Expressions](https://jmeter.apache.org/usermanual/regular_expressions.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#hints)...[22. Hints and Tips](https://jmeter.apache.org/usermanual/hints_and_tips.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#glossary)...[23. Glossary](https://jmeter.apache.org/usermanual/glossary.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#curl)...[24. Curl](https://jmeter.apache.org/usermanual/curl.html)
*   [+](https://jmeter.apache.org/usermanual/index.html#history_future)...[25. History / Future](https://jmeter.apache.org/usermanual/history_future.html)

Detailed Section List[¶](https://jmeter.apache.org/usermanual/index.html#details "Link to here")
------------------------------------------------------------------------------------------------

*   [](https://jmeter.apache.org/usermanual/index.html)[1. Getting Started](https://jmeter.apache.org/usermanual/get-started.html)
    *   [1.0 Overview](https://jmeter.apache.org/usermanual/get-started.html#overview)

    
        *   [Test plan building](https://jmeter.apache.org/usermanual/get-started.html#test_plan_building)
        *   [Load Test running](https://jmeter.apache.org/usermanual/get-started.html#load_test_running)
        *   [Load Test analysis](https://jmeter.apache.org/usermanual/get-started.html#load_test_analysis)
        *   [Let's start](https://jmeter.apache.org/usermanual/get-started.html#lets_start)

    *   [1.1 Requirements](https://jmeter.apache.org/usermanual/get-started.html#requirements)

    
        *   [1.1.1 Java Version](https://jmeter.apache.org/usermanual/get-started.html#java_versions)
        *   [1.1.2 Operating Systems](https://jmeter.apache.org/usermanual/get-started.html#os)

    *   [1.2 Optional](https://jmeter.apache.org/usermanual/get-started.html#optional)
        *   [1.2.1 Java Compiler](https://jmeter.apache.org/usermanual/get-started.html#opt_compiler)
        *   [1.2.2 SAX XML Parser](https://jmeter.apache.org/usermanual/get-started.html#opt_sax)
        *   [1.2.3 Email Support](https://jmeter.apache.org/usermanual/get-started.html#opt_email)
        *   [1.2.4 SSL Encryption](https://jmeter.apache.org/usermanual/get-started.html#opt_ssl)
        *   [1.2.5 JDBC Driver](https://jmeter.apache.org/usermanual/get-started.html#opt_jdbc)
        *   [1.2.6 JMS client](https://jmeter.apache.org/usermanual/get-started.html#opt_jms)
        *   [1.2.7 Libraries for ActiveMQ JMS](https://jmeter.apache.org/usermanual/get-started.html#libraries_activemq)

    *   [1.3 Installation](https://jmeter.apache.org/usermanual/get-started.html#install)
    *   [1.4 Running JMeter](https://jmeter.apache.org/usermanual/get-started.html#running)
        *   [1.4.1 JMeter's Classpath](https://jmeter.apache.org/usermanual/get-started.html#classpath)
        *   [1.4.2 Create Test Plan from Template](https://jmeter.apache.org/usermanual/get-started.html#template)
        *   [1.4.3 Using JMeter behind a proxy](https://jmeter.apache.org/usermanual/get-started.html#proxy_server)
        *   [1.4.4 CLI mode](https://jmeter.apache.org/usermanual/get-started.html#non_gui)
        *   [1.4.5 Server Mode](https://jmeter.apache.org/usermanual/get-started.html#server)
        *   [1.4.6 Overriding Properties Via The Command Line](https://jmeter.apache.org/usermanual/get-started.html#override)
        *   [1.4.7 Logging and Error Messages](https://jmeter.apache.org/usermanual/get-started.html#logging)
        *   [1.4.8 Full list of command-line options](https://jmeter.apache.org/usermanual/get-started.html#options)
        *   [1.4.9 CLI mode shutdown](https://jmeter.apache.org/usermanual/get-started.html#shutdown)

    *   [1.5 Configuring JMeter](https://jmeter.apache.org/usermanual/get-started.html#configuring_jmeter)

*   [](https://jmeter.apache.org/usermanual/index.html)[2. Building a Test Plan](https://jmeter.apache.org/usermanual/build-test-plan.html)
    *   [2.1 Adding and Removing Elements](https://jmeter.apache.org/usermanual/build-test-plan.html#add_remove)
    *   [2.2 Loading and Saving Elements](https://jmeter.apache.org/usermanual/build-test-plan.html#load_save)
    *   [2.3 Configuring Tree Elements](https://jmeter.apache.org/usermanual/build-test-plan.html#config_element)
    *   [2.4 Saving the Test Plan](https://jmeter.apache.org/usermanual/build-test-plan.html#save)
    *   [2.5 Running a Test Plan](https://jmeter.apache.org/usermanual/build-test-plan.html#run)
    *   [2.6 Stopping a Test](https://jmeter.apache.org/usermanual/build-test-plan.html#stop)
    *   [2.7 Error reporting](https://jmeter.apache.org/usermanual/build-test-plan.html#error_reporting)

*   [](https://jmeter.apache.org/usermanual/index.html)[3. Elements of a Test Plan](https://jmeter.apache.org/usermanual/test_plan.html)
    *   [3.1 Thread Group](https://jmeter.apache.org/usermanual/test_plan.html#thread_group)
    *   [3.2 Controllers](https://jmeter.apache.org/usermanual/test_plan.html#controllers)
        *   [3.2.1 Samplers](https://jmeter.apache.org/usermanual/test_plan.html#samplers)
        *   [3.2.2 Logic Controllers](https://jmeter.apache.org/usermanual/test_plan.html#logic_controller)
        *   [3.2.3 Test Fragments](https://jmeter.apache.org/usermanual/test_plan.html#test_fragments)

    *   [3.3 Listeners](https://jmeter.apache.org/usermanual/test_plan.html#listeners)
    *   [3.4 Timers](https://jmeter.apache.org/usermanual/test_plan.html#timers)
    *   [3.5 Assertions](https://jmeter.apache.org/usermanual/test_plan.html#assertions)
    *   [3.6 Configuration Elements](https://jmeter.apache.org/usermanual/test_plan.html#config_elements)
    *   [3.7 Pre-Processor Elements](https://jmeter.apache.org/usermanual/test_plan.html#preprocessors)
    *   [3.8 Post-Processor Elements](https://jmeter.apache.org/usermanual/test_plan.html#postprocessors)
    *   [3.9 Execution order](https://jmeter.apache.org/usermanual/test_plan.html#executionorder)
    *   [3.10 Scoping Rules](https://jmeter.apache.org/usermanual/test_plan.html#scoping_rules)
    *   [3.11 Properties and Variables](https://jmeter.apache.org/usermanual/test_plan.html#properties)
    *   [3.12 Using Variables to parameterise tests](https://jmeter.apache.org/usermanual/test_plan.html#using_variables)

*   [](https://jmeter.apache.org/usermanual/index.html)[4. Building a Web Test Plan](https://jmeter.apache.org/usermanual/build-web-test-plan.html)
    *   [4.1 Adding Users](https://jmeter.apache.org/usermanual/build-web-test-plan.html#adding_users)
    *   [4.2 Adding Default HTTP Request Properties](https://jmeter.apache.org/usermanual/build-web-test-plan.html#adding_defaults)
    *   [4.3 Adding Cookie Support](https://jmeter.apache.org/usermanual/build-web-test-plan.html#adding_cookie_support)
    *   [4.4 Adding HTTP Requests](https://jmeter.apache.org/usermanual/build-web-test-plan.html#adding_requests)
    *   [4.5 Adding a Listener to View/Store the Test Results](https://jmeter.apache.org/usermanual/build-web-test-plan.html#adding_listener)
    *   [4.6 Logging in to a web-site](https://jmeter.apache.org/usermanual/build-web-test-plan.html#logging_in)

*   [](https://jmeter.apache.org/usermanual/index.html)[5. Building an Advanced Web Test Plan](https://jmeter.apache.org/usermanual/build-adv-web-test-plan.html)
    *   [5.1 Handling User Sessions With URL Rewriting](https://jmeter.apache.org/usermanual/build-adv-web-test-plan.html#session_url_rewriting)
    *   [5.2 Using a Header Manager](https://jmeter.apache.org/usermanual/build-adv-web-test-plan.html#header_manager)

*   [](https://jmeter.apache.org/usermanual/index.html)[6. Building a Database Test Plan](https://jmeter.apache.org/usermanual/build-db-test-plan.html)
    *   [6.1 Adding Users](https://jmeter.apache.org/usermanual/build-db-test-plan.html#adding_users)
    *   [6.2 Adding JDBC Requests](https://jmeter.apache.org/usermanual/build-db-test-plan.html#adding_requests)
    *   [6.3 Adding a Listener to View/Store the Test Results](https://jmeter.apache.org/usermanual/build-db-test-plan.html#adding_listener)

*   [](https://jmeter.apache.org/usermanual/index.html)[7. Building an FTP Test Plan](https://jmeter.apache.org/usermanual/build-ftp-test-plan.html)
    *   [7.1 Adding Users](https://jmeter.apache.org/usermanual/build-ftp-test-plan.html#adding_users)
    *   [7.2 Adding Default FTP Request Properties](https://jmeter.apache.org/usermanual/build-ftp-test-plan.html#adding_defaults)
    *   [7.3 Adding FTP Requests](https://jmeter.apache.org/usermanual/build-ftp-test-plan.html#adding_requests)
    *   [7.4 Adding a Listener to View/Store the Test Results](https://jmeter.apache.org/usermanual/build-ftp-test-plan.html#adding_listener)

*   [](https://jmeter.apache.org/usermanual/index.html)[8a. Building an LDAP Test Plan](https://jmeter.apache.org/usermanual/build-ldap-test-plan.html)
    *   [8a.1 Adding Users](https://jmeter.apache.org/usermanual/build-ldap-test-plan.html#adding_users)
    *   [8a.2 Adding Login Config Element](https://jmeter.apache.org/usermanual/build-ldap-test-plan.html#add_login)
    *   [8a.3 Adding LDAP Request Defaults](https://jmeter.apache.org/usermanual/build-ldap-test-plan.html#add_defaults)
    *   [8a.4 Adding LDAP Requests](https://jmeter.apache.org/usermanual/build-ldap-test-plan.html#add_requests)
    *   [8a.5 Adding a Response Assertion](https://jmeter.apache.org/usermanual/build-ldap-test-plan.html#ResponseAssertion)
    *   [8a.6 Adding a Listener to View/Store the Test Results](https://jmeter.apache.org/usermanual/build-ldap-test-plan.html#add_listener)

*   [](https://jmeter.apache.org/usermanual/index.html)[8b. Building an Extended LDAP Test Plan](https://jmeter.apache.org/usermanual/build-ldap-test-plan.html)
    *   [8b.1 Adding Users](https://jmeter.apache.org/usermanual/build-ldapext-test-plan.html#ext_adding_users)
    *   [8b.2 Adding LDAP Extended Request Defaults](https://jmeter.apache.org/usermanual/build-ldapext-test-plan.html#add_login)
    *   [8b.3 Adding LDAP Requests](https://jmeter.apache.org/usermanual/build-ldapext-test-plan.html#add_extrequests)
    *   [8b.4 Adding a Listener to View/Store the Test Results](https://jmeter.apache.org/usermanual/build-ldapext-test-plan.html#add_ldapext_listener)

*   [](https://jmeter.apache.org/usermanual/index.html)[9. Building a Webservice Test Plan](https://jmeter.apache.org/usermanual/build-ws-test-plan.html)
*   [](https://jmeter.apache.org/usermanual/index.html)[10. Building a JMS Point to point Test Plan](https://jmeter.apache.org/usermanual/build-jms-point-to-point-test-plan.html)
*   [](https://jmeter.apache.org/usermanual/index.html)[11. Building a JMS topic Test Plan](https://jmeter.apache.org/usermanual/build-jms-topic-test-plan.html)
*   [](https://jmeter.apache.org/usermanual/index.html)[11. Building a Test Plan Programatically](https://jmeter.apache.org/usermanual/build-programmatic-test-plan.html)
*   [](https://jmeter.apache.org/usermanual/index.html)[12. Introduction to Listeners](https://jmeter.apache.org/usermanual/listeners.html)
*   [](https://jmeter.apache.org/usermanual/index.html)[13. Remote Testing](https://jmeter.apache.org/usermanual/remote-test.html)
*   [](https://jmeter.apache.org/usermanual/index.html)[14. Dashboard Report](https://jmeter.apache.org/usermanual/generating-dashboard.html)
    *   [14.1 Overview](https://jmeter.apache.org/usermanual/generating-dashboard.html#overview)
    *   [14.2 Configuring Dashboard Generation](https://jmeter.apache.org/usermanual/generating-dashboard.html#configuration)
    *   [14.3 Generating reports](https://jmeter.apache.org/usermanual/generating-dashboard.html#report)
    *   [14.4 Default graphs](https://jmeter.apache.org/usermanual/generating-dashboard.html#default_graphs)
    *   [14.5 Want to improve Report Dashboard](https://jmeter.apache.org/usermanual/generating-dashboard.html#development)

*   [](https://jmeter.apache.org/usermanual/index.html)[15. Real time Results](https://jmeter.apache.org/usermanual/realtime-results.html)
*   [](https://jmeter.apache.org/usermanual/index.html)[16. Best Practices](https://jmeter.apache.org/usermanual/best-practices.html)
*   [](https://jmeter.apache.org/usermanual/index.html)[17. Help! My boss wants me to load test our web app!](https://jmeter.apache.org/usermanual/boss.html)
*   [](https://jmeter.apache.org/usermanual/index.html)[18. Component Reference](https://jmeter.apache.org/usermanual/component_reference.html)
*   [](https://jmeter.apache.org/usermanual/index.html)[19. Properties reference](https://jmeter.apache.org/usermanual/properties_reference.html)
*   [](https://jmeter.apache.org/usermanual/index.html)[20. Functions](https://jmeter.apache.org/usermanual/functions.html)
*   [](https://jmeter.apache.org/usermanual/index.html)[21. Regular Expressions](https://jmeter.apache.org/usermanual/regular_expressions.html)
*   [](https://jmeter.apache.org/usermanual/index.html)[22. Hints and Tips](https://jmeter.apache.org/usermanual/hints_and_tips.html)
*   [](https://jmeter.apache.org/usermanual/index.html)[23. Glossary](https://jmeter.apache.org/usermanual/glossary.html)
*   [](https://jmeter.apache.org/usermanual/index.html)[24. Curl](https://jmeter.apache.org/usermanual/curl.html)
    *   [24.1 How to enter (a) command(s)](https://jmeter.apache.org/usermanual/curl.html#enter_command)
    *   [24.2 Curl options supported](https://jmeter.apache.org/usermanual/curl.html#curl_options)
    *   [24.3 Warning](https://jmeter.apache.org/usermanual/curl.html#warning)
    *   [24.4 Some Examples](https://jmeter.apache.org/usermanual/curl.html#example)

*   [](https://jmeter.apache.org/usermanual/index.html)[25. History / Future](https://jmeter.apache.org/usermanual/history_future.html)

*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/get-started.html)

 Share this page: 
*   [share](https://facebook.com/sharer/sharer.php?u=https%3A%2F%2Fjmeter.apache.org%2Fusermanual%2Findex.html "Share on facebook")
*   [tweet](https://twitter.com/intent/tweet?url=https%3A%2F%2Fjmeter.apache.org%2Fusermanual%2Findex.html "Tweet on twitter")

[Go to top](https://jmeter.apache.org/usermanual/index.html#top)

 Copyright © 1999 – 2024 , Apache Software Foundation 

Apache, Apache JMeter, JMeter, the Apache feather, and the Apache JMeter logo are trademarks of the Apache Software Foundation.
