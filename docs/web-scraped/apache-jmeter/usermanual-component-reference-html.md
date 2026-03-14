# Source: https://jmeter.apache.org/usermanual/component_reference.html

Title: Apache JMeter
          -
          User's Manual: Component Reference

URL Source: https://jmeter.apache.org/usermanual/component_reference.html

Published Time: Sun, 07 Jan 2024 17:19:24 GMT

Markdown Content:
Apache JMeter - User's Manual: Component Reference
===============
[Main content](https://jmeter.apache.org/usermanual/component_reference.html#content)

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

*   [< Prev](https://jmeter.apache.org/usermanual/boss.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/properties_reference.html)

*   [18 Introduction](https://jmeter.apache.org/usermanual/component_reference.html#introduction)

*   [18.1 Samplers](https://jmeter.apache.org/usermanual/component_reference.html#samplers)
    *   [FTP Request](https://jmeter.apache.org/usermanual/component_reference.html#FTP_Request)
    *   [HTTP Request](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request)
    *   [JDBC Request](https://jmeter.apache.org/usermanual/component_reference.html#JDBC_Request)
    *   [Java Request](https://jmeter.apache.org/usermanual/component_reference.html#Java_Request)
    *   [LDAP Request](https://jmeter.apache.org/usermanual/component_reference.html#LDAP_Request)
    *   [LDAP Extended Request](https://jmeter.apache.org/usermanual/component_reference.html#LDAP_Extended_Request)
    *   [Access Log Sampler](https://jmeter.apache.org/usermanual/component_reference.html#Access_Log_Sampler)
    *   [BeanShell Sampler](https://jmeter.apache.org/usermanual/component_reference.html#BeanShell_Sampler)
    *   [JSR223 Sampler](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_Sampler)
    *   [TCP Sampler](https://jmeter.apache.org/usermanual/component_reference.html#TCP_Sampler)
    *   [JMS Publisher](https://jmeter.apache.org/usermanual/component_reference.html#JMS_Publisher)
    *   [JMS Subscriber](https://jmeter.apache.org/usermanual/component_reference.html#JMS_Subscriber)
    *   [JMS Point-to-Point](https://jmeter.apache.org/usermanual/component_reference.html#JMS_Point-to-Point)
    *   [JUnit Request](https://jmeter.apache.org/usermanual/component_reference.html#JUnit_Request)
    *   [Mail Reader Sampler](https://jmeter.apache.org/usermanual/component_reference.html#Mail_Reader_Sampler)
    *   [Flow Control Action (was: Test Action )](https://jmeter.apache.org/usermanual/component_reference.html#Flow_Control_Action)
    *   [SMTP Sampler](https://jmeter.apache.org/usermanual/component_reference.html#SMTP_Sampler)
    *   [OS Process Sampler](https://jmeter.apache.org/usermanual/component_reference.html#OS_Process_Sampler)
    *   [MongoDB Script (DEPRECATED)](https://jmeter.apache.org/usermanual/component_reference.html#MongoDB_Script_(DEPRECATED))
    *   [Bolt Request](https://jmeter.apache.org/usermanual/component_reference.html#Bolt_Request)

*   [18.2 Logic Controllers](https://jmeter.apache.org/usermanual/component_reference.html#logic_controllers)
    *   [Simple Controller](https://jmeter.apache.org/usermanual/component_reference.html#Simple_Controller)
    *   [Loop Controller](https://jmeter.apache.org/usermanual/component_reference.html#Loop_Controller)
    *   [Once Only Controller](https://jmeter.apache.org/usermanual/component_reference.html#Once_Only_Controller)
    *   [Interleave Controller](https://jmeter.apache.org/usermanual/component_reference.html#Interleave_Controller)
    *   [Random Controller](https://jmeter.apache.org/usermanual/component_reference.html#Random_Controller)
    *   [Random Order Controller](https://jmeter.apache.org/usermanual/component_reference.html#Random_Order_Controller)
    *   [Throughput Controller](https://jmeter.apache.org/usermanual/component_reference.html#Throughput_Controller)
    *   [Runtime Controller](https://jmeter.apache.org/usermanual/component_reference.html#Runtime_Controller)
    *   [If Controller](https://jmeter.apache.org/usermanual/component_reference.html#If_Controller)
    *   [While Controller](https://jmeter.apache.org/usermanual/component_reference.html#While_Controller)
    *   [Switch Controller](https://jmeter.apache.org/usermanual/component_reference.html#Switch_Controller)
    *   [ForEach Controller](https://jmeter.apache.org/usermanual/component_reference.html#ForEach_Controller)
    *   [Module Controller](https://jmeter.apache.org/usermanual/component_reference.html#Module_Controller)
    *   [Include Controller](https://jmeter.apache.org/usermanual/component_reference.html#Include_Controller)
    *   [Transaction Controller](https://jmeter.apache.org/usermanual/component_reference.html#Transaction_Controller)
    *   [Recording Controller](https://jmeter.apache.org/usermanual/component_reference.html#Recording_Controller)
    *   [Critical Section Controller](https://jmeter.apache.org/usermanual/component_reference.html#Critical_Section_Controller)

*   [18.3 Listeners](https://jmeter.apache.org/usermanual/component_reference.html#listeners)
    *   [Sample Result Save Configuration](https://jmeter.apache.org/usermanual/component_reference.html#Sample_Result_Save_Configuration)
    *   [Graph Results](https://jmeter.apache.org/usermanual/component_reference.html#Graph_Results)
    *   [Assertion Results](https://jmeter.apache.org/usermanual/component_reference.html#Assertion_Results)
    *   [View Results Tree](https://jmeter.apache.org/usermanual/component_reference.html#View_Results_Tree)
    *   [Aggregate Report](https://jmeter.apache.org/usermanual/component_reference.html#Aggregate_Report)
    *   [View Results in Table](https://jmeter.apache.org/usermanual/component_reference.html#View_Results_in_Table)
    *   [Simple Data Writer](https://jmeter.apache.org/usermanual/component_reference.html#Simple_Data_Writer)
    *   [Aggregate Graph](https://jmeter.apache.org/usermanual/component_reference.html#Aggregate_Graph)
    *   [Response Time Graph](https://jmeter.apache.org/usermanual/component_reference.html#Response_Time_Graph)
    *   [Mailer Visualizer](https://jmeter.apache.org/usermanual/component_reference.html#Mailer_Visualizer)
    *   [BeanShell Listener](https://jmeter.apache.org/usermanual/component_reference.html#BeanShell_Listener)
    *   [Summary Report](https://jmeter.apache.org/usermanual/component_reference.html#Summary_Report)
    *   [Save Responses to a file](https://jmeter.apache.org/usermanual/component_reference.html#Save_Responses_to_a_file)
    *   [JSR223 Listener](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_Listener)
    *   [Generate Summary Results](https://jmeter.apache.org/usermanual/component_reference.html#Generate_Summary_Results)
    *   [Comparison Assertion Visualizer](https://jmeter.apache.org/usermanual/component_reference.html#Comparison_Assertion_Visualizer)
    *   [Backend Listener](https://jmeter.apache.org/usermanual/component_reference.html#Backend_Listener)

*   [18.4 Configuration Elements](https://jmeter.apache.org/usermanual/component_reference.html#config_elements)
    *   [CSV Data Set Config](https://jmeter.apache.org/usermanual/component_reference.html#CSV_Data_Set_Config)
    *   [FTP Request Defaults](https://jmeter.apache.org/usermanual/component_reference.html#FTP_Request_Defaults)
    *   [DNS Cache Manager](https://jmeter.apache.org/usermanual/component_reference.html#DNS_Cache_Manager)
    *   [HTTP Authorization Manager](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Authorization_Manager)
    *   [HTTP Cache Manager](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Cache_Manager)
    *   [HTTP Cookie Manager](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Cookie_Manager)
    *   [HTTP Request Defaults](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request_Defaults)
    *   [HTTP Header Manager](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Header_Manager)
    *   [Java Request Defaults](https://jmeter.apache.org/usermanual/component_reference.html#Java_Request_Defaults)
    *   [JDBC Connection Configuration](https://jmeter.apache.org/usermanual/component_reference.html#JDBC_Connection_Configuration)
    *   [Keystore Configuration](https://jmeter.apache.org/usermanual/component_reference.html#Keystore_Configuration)
    *   [Login Config Element](https://jmeter.apache.org/usermanual/component_reference.html#Login_Config_Element)
    *   [LDAP Request Defaults](https://jmeter.apache.org/usermanual/component_reference.html#LDAP_Request_Defaults)
    *   [LDAP Extended Request Defaults](https://jmeter.apache.org/usermanual/component_reference.html#LDAP_Extended_Request_Defaults)
    *   [TCP Sampler Config](https://jmeter.apache.org/usermanual/component_reference.html#TCP_Sampler_Config)
    *   [User Defined Variables](https://jmeter.apache.org/usermanual/component_reference.html#User_Defined_Variables)
    *   [Random Variable](https://jmeter.apache.org/usermanual/component_reference.html#Random_Variable)
    *   [Counter](https://jmeter.apache.org/usermanual/component_reference.html#Counter)
    *   [Simple Config Element](https://jmeter.apache.org/usermanual/component_reference.html#Simple_Config_Element)
    *   [MongoDB Source Config (DEPRECATED)](https://jmeter.apache.org/usermanual/component_reference.html#MongoDB_Source_Config_(DEPRECATED))
    *   [Bolt Connection Configuration](https://jmeter.apache.org/usermanual/component_reference.html#Bolt_Connection_Configuration)

*   [18.5 Assertions](https://jmeter.apache.org/usermanual/component_reference.html#assertions)
    *   [Response Assertion](https://jmeter.apache.org/usermanual/component_reference.html#Response_Assertion)
    *   [Duration Assertion](https://jmeter.apache.org/usermanual/component_reference.html#Duration_Assertion)
    *   [Size Assertion](https://jmeter.apache.org/usermanual/component_reference.html#Size_Assertion)
    *   [XML Assertion](https://jmeter.apache.org/usermanual/component_reference.html#XML_Assertion)
    *   [BeanShell Assertion](https://jmeter.apache.org/usermanual/component_reference.html#BeanShell_Assertion)
    *   [MD5Hex Assertion](https://jmeter.apache.org/usermanual/component_reference.html#MD5Hex_Assertion)
    *   [HTML Assertion](https://jmeter.apache.org/usermanual/component_reference.html#HTML_Assertion)
    *   [XPath Assertion](https://jmeter.apache.org/usermanual/component_reference.html#XPath_Assertion)
    *   [XPath2 Assertion](https://jmeter.apache.org/usermanual/component_reference.html#XPath2_Assertion)
    *   [XML Schema Assertion](https://jmeter.apache.org/usermanual/component_reference.html#XML_Schema_Assertion)
    *   [JSR223 Assertion](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_Assertion)
    *   [Compare Assertion](https://jmeter.apache.org/usermanual/component_reference.html#Compare_Assertion)
    *   [SMIME Assertion](https://jmeter.apache.org/usermanual/component_reference.html#SMIME_Assertion)
    *   [JSON Assertion](https://jmeter.apache.org/usermanual/component_reference.html#JSON_Assertion)
    *   [JSON JMESPath Assertion](https://jmeter.apache.org/usermanual/component_reference.html#JSON_JMESPath_Assertion)

*   [18.6 Timers](https://jmeter.apache.org/usermanual/component_reference.html#timers)
    *   [Constant Timer](https://jmeter.apache.org/usermanual/component_reference.html#Constant_Timer)
    *   [Gaussian Random Timer](https://jmeter.apache.org/usermanual/component_reference.html#Gaussian_Random_Timer)
    *   [Uniform Random Timer](https://jmeter.apache.org/usermanual/component_reference.html#Uniform_Random_Timer)
    *   [Constant Throughput Timer](https://jmeter.apache.org/usermanual/component_reference.html#Constant_Throughput_Timer)
    *   [Precise Throughput Timer](https://jmeter.apache.org/usermanual/component_reference.html#Precise_Throughput_Timer)
    *   [Synchronizing Timer](https://jmeter.apache.org/usermanual/component_reference.html#Synchronizing_Timer)
    *   [BeanShell Timer](https://jmeter.apache.org/usermanual/component_reference.html#BeanShell_Timer)
    *   [JSR223 Timer](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_Timer)
    *   [Poisson Random Timer](https://jmeter.apache.org/usermanual/component_reference.html#Poisson_Random_Timer)

*   [18.7 Pre Processors](https://jmeter.apache.org/usermanual/component_reference.html#preprocessors)
    *   [HTML Link Parser](https://jmeter.apache.org/usermanual/component_reference.html#HTML_Link_Parser)
    *   [HTTP URL Re-writing Modifier](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_URL_Re-writing_Modifier)
    *   [User Parameters](https://jmeter.apache.org/usermanual/component_reference.html#User_Parameters)
    *   [BeanShell PreProcessor](https://jmeter.apache.org/usermanual/component_reference.html#BeanShell_PreProcessor)
    *   [JSR223 PreProcessor](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_PreProcessor)
    *   [JDBC PreProcessor](https://jmeter.apache.org/usermanual/component_reference.html#JDBC_PreProcessor)
    *   [RegEx User Parameters](https://jmeter.apache.org/usermanual/component_reference.html#RegEx_User_Parameters)
    *   [Sample Timeout](https://jmeter.apache.org/usermanual/component_reference.html#Sample_Timeout)

*   [18.8 Post-Processors](https://jmeter.apache.org/usermanual/component_reference.html#postprocessors)
    *   [Regular Expression Extractor](https://jmeter.apache.org/usermanual/component_reference.html#Regular_Expression_Extractor)
    *   [CSS Selector Extractor (was: CSS/JQuery Extractor )](https://jmeter.apache.org/usermanual/component_reference.html#CSS_Selector_Extractor)
    *   [XPath2 Extractor](https://jmeter.apache.org/usermanual/component_reference.html#XPath2_Extractor)
    *   [XPath Extractor](https://jmeter.apache.org/usermanual/component_reference.html#XPath_Extractor)
    *   [JSON JMESPath Extractor](https://jmeter.apache.org/usermanual/component_reference.html#JSON_JMESPath_Extractor)
    *   [Result Status Action Handler](https://jmeter.apache.org/usermanual/component_reference.html#Result_Status_Action_Handler)
    *   [BeanShell PostProcessor](https://jmeter.apache.org/usermanual/component_reference.html#BeanShell_PostProcessor)
    *   [JSR223 PostProcessor](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_PostProcessor)
    *   [JDBC PostProcessor](https://jmeter.apache.org/usermanual/component_reference.html#JDBC_PostProcessor)
    *   [JSON Extractor](https://jmeter.apache.org/usermanual/component_reference.html#JSON_Extractor)
    *   [Boundary Extractor](https://jmeter.apache.org/usermanual/component_reference.html#Boundary_Extractor)

*   [18.9 Miscellaneous Features](https://jmeter.apache.org/usermanual/component_reference.html#Miscellaneous_Features)
    *   [Test Plan](https://jmeter.apache.org/usermanual/component_reference.html#Test_Plan)
    *   [Open Model Thread Group](https://jmeter.apache.org/usermanual/component_reference.html#Open_Model_Thread_Group)
    *   [Thread Group](https://jmeter.apache.org/usermanual/component_reference.html#Thread_Group)
    *   [WorkBench](https://jmeter.apache.org/usermanual/component_reference.html#WorkBench)
    *   [SSL Manager](https://jmeter.apache.org/usermanual/component_reference.html#SSL_Manager)
    *   [HTTP(S) Test Script Recorder (was: HTTP Proxy Server )](https://jmeter.apache.org/usermanual/component_reference.html#HTTP(S)_Test_Script_Recorder)
    *   [HTTP Mirror Server](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Mirror_Server)
    *   [Property Display](https://jmeter.apache.org/usermanual/component_reference.html#Property_Display)
    *   [Debug Sampler](https://jmeter.apache.org/usermanual/component_reference.html#Debug_Sampler)
    *   [Debug PostProcessor](https://jmeter.apache.org/usermanual/component_reference.html#Debug_PostProcessor)
    *   [Test Fragment](https://jmeter.apache.org/usermanual/component_reference.html#Test_Fragment)
    *   [setUp Thread Group](https://jmeter.apache.org/usermanual/component_reference.html#setUp_Thread_Group)
    *   [tearDown Thread Group](https://jmeter.apache.org/usermanual/component_reference.html#tearDown_Thread_Group)

18 Introduction[¶](https://jmeter.apache.org/usermanual/component_reference.html#introduction "Link to here")
=============================================================================================================

 Several test elements use JMeter properties to control their behaviour. These properties are normally resolved when the class is loaded. This generally occurs before the test plan starts, so it's not possible to change the settings by using the [__setProperty()](https://jmeter.apache.org/usermanual/functions.html#__setProperty) function. 

18.1 Samplers[¶](https://jmeter.apache.org/usermanual/component_reference.html#samplers "Link to here")
=======================================================================================================

Samplers perform the actual work of JMeter. Each sampler (except [Flow Control Action](https://jmeter.apache.org/usermanual/component_reference.html#Flow_Control_Action)) generates one or more sample results. The sample results have various attributes (success/fail, elapsed time, data size etc.) and can be viewed in the various listeners.

FTP Request[¶](https://jmeter.apache.org/usermanual/component_reference.html#FTP_Request "Link to here")
--------------------------------------------------------------------------------------------------------

 This controller lets you send an FTP "retrieve file" or "upload file" request to an FTP server. If you are going to send multiple requests to the same FTP server, consider using a [FTP Request Defaults](https://jmeter.apache.org/usermanual/component_reference.html#FTP_Request_Defaults) Configuration Element so you do not have to enter the same information for each FTP Request Generative Controller. When downloading a file, it can be stored on disk (Local File) or in the Response Data, or both. 
Latency is set to the time it takes to login.

[![Image 4: Screenshot for Control-Panel of FTP Request](https://jmeter.apache.org/images/screenshots/ftptest/ftp-request.png)](https://jmeter.apache.org/images/screenshots/ftptest/ftp-request.png)

Screenshot of Control-Panel of FTP Request

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#FTP_Request_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Server Name or IP

Domain name or IP address of the FTP server.

Yes

Port

 Port to use. If this is >0, then this specific port is used, otherwise JMeter uses the default FTP port. 

No

Remote File:

File to retrieve or name of destination file to upload.

Yes

Local File:

File to upload, or destination for downloads (defaults to remote file name).

Yes, if uploading (*)

Local File Contents:

Provides the contents for the upload, overrides the Local File property.

Yes, if uploading (*)

get(RETR) / put(STOR)

Whether to retrieve or upload a file.

Yes

Use Binary mode?

Check this to use Binary mode (default ASCII)

Yes

Save File in Response?

 Whether to store contents of retrieved file in response data. If the mode is ASCII, then the contents will be visible in the [View Results Tree](https://jmeter.apache.org/usermanual/component_reference.html#View_Results_Tree). 

Yes, if downloading

Username

FTP account username.

Usually

Password

FTP account password. N.B. This will be visible in the test plan.

Usually

See also:

*   [Assertions](https://jmeter.apache.org/usermanual/test_plan.html#assertions)
*   [FTP Request Defaults](https://jmeter.apache.org/usermanual/component_reference.html#FTP_Request_Defaults)
*   [Building an FTP Test Plan](https://jmeter.apache.org/usermanual/build-ftp-test-plan.html)

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

HTTP Request[¶](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request "Link to here")
----------------------------------------------------------------------------------------------------------

This sampler lets you send an HTTP/HTTPS request to a web server. It also lets you control whether or not JMeter parses HTML files for images and other embedded resources and sends HTTP requests to retrieve them. The following types of embedded resource are retrieved:

*   images
*   applets
*   stylesheets (CSS) and resources referenced from those files
*   external scripts
*   frames, iframes
*   background images (body, table, TD, TR)
*   background sound

The default parser is org.apache.jmeter.protocol.http.parser.LagartoBasedHtmlParser. This can be changed by using the property "htmlparser.className" - see jmeter.properties for details.

If you are going to send multiple requests to the same web server, consider using an [HTTP Request Defaults](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request_Defaults) Configuration Element so you do not have to enter the same information for each HTTP Request.

Or, instead of manually adding HTTP Requests, you may want to use JMeter's [HTTP(S) Test Script Recorder](https://jmeter.apache.org/usermanual/component_reference.html#HTTP(S)_Test_Script_Recorder) to create them. This can save you time if you have a lot of HTTP requests or requests with many parameters.

**There are three different test elements used to define the samplers:**

AJP/1.3 Sampler uses the Tomcat mod_jk protocol (allows testing of Tomcat in AJP mode without needing Apache httpd) The AJP Sampler does not support multiple file upload; only the first file will be used. HTTP Request this has an implementation drop-down box, which selects the HTTP protocol implementation to be used: Java uses the HTTP implementation provided by the JVM. This has some limitations in comparison with the HttpClient implementations - see below.HTTPClient4 uses Apache HttpComponents HttpClient 4.x.Blank Value does not set implementation on HTTP Samplers, so relies on HTTP Request Defaults if present or on jmeter.httpsampler property defined in jmeter.properties GraphQL HTTP Request this is a GUI variation of the **HTTP Request** to provide more convenient UI elements to view or edit GraphQL **Query**, **Variables** and **Operation Name**, while converting them into HTTP Arguments automatically under the hood using the same sampler. This hides or customizes the following UI elements as they are less convenient for or irrelevant to GraphQL over HTTP/HTTPS requests: 
*   **Method**: Only POST and GET methods are available conforming the GraphQL over HTTP specification. POST method is selected by default. 
*   **Parameters** and **Post Body** tabs: you may view or edit parameter content through Query, Variables and Operation Name UI elements instead. 
*   **File Upload** tab: irrelevant to GraphQL queries. 
*   **Embedded Resources from HTML Files** section in the Advanced tab: irrelevant in GraphQL JSON responses. 

The Java HTTP implementation has some limitations:

*   There is no control over how connections are re-used. When a connection is released by JMeter, it may or may not be re-used by the same thread.
*   The API is best suited to single-threaded usage - various settings are defined via system properties, and therefore apply to all connections.
*   No support of Kerberos authentication
*   It does not support client based certificate testing with Keystore Config.
*   Better control of Retry mechanism
*   It does not support virtual hosts.
*    It supports only the following methods: GET, POST, HEAD, OPTIONS, PUT, DELETE and TRACE
*    Better control on DNS Caching with [DNS Cache Manager](https://jmeter.apache.org/usermanual/component_reference.html#DNS_Cache_Manager)

 Note: the FILE protocol is intended for testing purposes only. It is handled by the same code regardless of which HTTP Sampler is used. 

If the request requires server or proxy login authorization (i.e. where a browser would create a pop-up dialog box), you will also have to add an [HTTP Authorization Manager](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Authorization_Manager) Configuration Element. For normal logins (i.e. where the user enters login information in a form), you will need to work out what the form submit button does, and create an HTTP request with the appropriate method (usually POST) and the appropriate parameters from the form definition. If the page uses HTTP, you can use the JMeter Proxy to capture the login sequence.

A separate SSL context is used for each thread. If you want to use a single SSL context (not the standard behaviour of browsers), set the JMeter property:

https.sessioncontext.shared=true
 By default, since version 5.0, the SSL context is retained during a Thread Group iteration and reset for each test iteration. If in your test plan the same user iterates multiple times, then you should set this to false. 
httpclient.reset_state_on_thread_group_iteration=true

 Note: this does not apply to the Java HTTP implementation. 

 JMeter defaults to the SSL protocol level TLS. If the server needs a different level, e.g. SSLv3, change the JMeter property, for example: 
https.default.protocol=SSLv3

JMeter also allows one to enable additional protocols, by changing the property https.socket.protocols.

If the request uses cookies, then you will also need an [HTTP Cookie Manager](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Cookie_Manager). You can add either of these elements to the Thread Group or the HTTP Request. If you have more than one HTTP Request that needs authorizations or cookies, then add the elements to the Thread Group. That way, all HTTP Request controllers will share the same Authorization Manager and Cookie Manager elements.

If the request uses a technique called "URL Rewriting" to maintain sessions, then see section [6.1 Handling User Sessions With URL Rewriting](https://jmeter.apache.org/usermanual/build-adv-web-test-plan.html#session_url_rewriting) for additional configuration steps.

[![Image 5: Screenshot for Control-Panel of HTTP Request](https://jmeter.apache.org/images/screenshots/http-request.png)](https://jmeter.apache.org/images/screenshots/http-request.png)

Screenshot of Control-Panel of HTTP Request

[![Image 6: HTTP Request Advanced config fields](https://jmeter.apache.org/images/screenshots/http-request-advanced-tab.png)](https://jmeter.apache.org/images/screenshots/http-request-advanced-tab.png)

HTTP Request Advanced config fields

[![Image 7: Screenshot of Control-Panel of GraphQL HTTP Request](https://jmeter.apache.org/images/screenshots/graphql-http-request.png)](https://jmeter.apache.org/images/screenshots/graphql-http-request.png)

Screenshot of Control-Panel of GraphQL HTTP Request

[![Image 8: Variables field for GraphQL HTTP Request](https://jmeter.apache.org/images/screenshots/graphql-http-request-vars.png)](https://jmeter.apache.org/images/screenshots/graphql-http-request-vars.png)

Variables field for GraphQL HTTP Request

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Server

 Domain name or IP address of the web server, e.g. www.example.com. [Do not include the http:// prefix.] Note: If the "Host" header is defined in a Header Manager, then this will be used as the virtual host name. 

 Server is required, unless: 
*    it is provided by [HTTP Request Defaults](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request_Defaults)
*    or a full URL including scheme, host and port (scheme://host:port) is set in **Path** field 

No

Port

 Port the web server is listening to. Default: 80

No

Connect Timeout

Connection Timeout. Number of milliseconds to wait for a connection to open.

No

Response Timeout

 Response Timeout. Number of milliseconds to wait for a response. Note that this applies to each wait for a response. If the server response is sent in several chunks, the overall elapsed time may be longer than the timeout. 
A [Duration Assertion](https://jmeter.apache.org/usermanual/component_reference.html#Duration_Assertion) can be used to detect responses that take too long to complete.

No

Server (proxy)

 Hostname or IP address of a proxy server to perform request. [Do not include the http:// prefix.] 

No

Port

Port the proxy server is listening to.

No, unless proxy hostname is specified

Username

(Optional) username for proxy server.

No

Password

(Optional) password for proxy server. (N.B. this is stored unencrypted in the test plan)

No

Implementation

Java, HttpClient4. If not specified (and not defined by HTTP Request Defaults), the default depends on the value of the JMeter property jmeter.httpsampler, failing that, the HttpClient4 implementation is used. 

No

Protocol

HTTP, HTTPS or FILE. Default: HTTP

No

Method

GET, POST, HEAD, TRACE, OPTIONS, PUT, DELETE, PATCH (not supported for JAVA implementation). With HttpClient4, the following methods related to WebDav are also allowed: COPY, LOCK, MKCOL, MOVE, PROPFIND, PROPPATCH, UNLOCK, REPORT, MKCALENDAR, SEARCH. 
More methods can be pre-defined for the HttpClient4 by using the JMeter property httpsampler.user_defined_methods.

Yes

Content Encoding

 Content encoding to be used (for POST, PUT, PATCH and FILE). This is the character encoding to be used, and is not related to the Content-Encoding HTTP header. 

No

Redirect Automatically

 Sets the underlying http protocol handler to automatically follow redirects, so they are not seen by JMeter, and thus will not appear as samples. Should only be used for GET and HEAD requests. The HttpClient sampler will reject attempts to use it for POST or PUT. 

Warning: see below for information on cookie and header handling.

No

Follow Redirects

 This only has any effect if "Redirect Automatically" is not enabled. If set, the JMeter sampler will check if the response is a redirect and follow it if so. The initial redirect and further responses will appear as additional samples. The URL and data fields of the parent sample will be taken from the final (non-redirected) sample, but the parent byte count and elapsed time include all samples. The latency is taken from the initial response. Note that the HttpClient sampler may log the following message: "Redirect requested but followRedirects is disabled" This can be ignored. 

 JMeter will collapse paths of the form '/../segment' in both absolute and relative redirect URLs. For example http://host/one/../two will be collapsed into http://host/two. If necessary, this behaviour can be suppressed by setting the JMeter property httpsampler.redirect.removeslashdotdot=false

No

Use KeepAlive

 JMeter sets the Connection: keep-alive header. This does not work properly with the default HTTP implementation, as connection re-use is not under user-control. It does work with the Apache HttpComponents HttpClient implementations. 

No

Use multipart/form-data for HTTP POST

 Use a multipart/form-data or application/x-www-form-urlencoded post request 

No

Browser-compatible headers

 When using multipart/form-data, this suppresses the Content-Type and Content-Transfer-Encoding headers; only the Content-Disposition header is sent. 

No

Path

 The path to resource (for example, /servlets/myServlet). If the resource requires query string parameters, add them below in the "Send Parameters With the Request" section. 

 As a special case, if the path starts with "http://" or "https://" then this is used as the full URL. 

 In this case, the server, port and protocol fields are ignored; parameters are also ignored for GET and DELETE methods. Also please note that the path is not encoded - apart from replacing spaces with %20 - so unsafe characters may need to be encoded to avoid errors such as URISyntaxException. 

No

Send Parameters With the Request

 The query string will be generated from the list of parameters you provide. Each parameter has a name and value, the options to encode the parameter, and an option to include or exclude an equals sign (some applications don't expect an equals sign when the value is the empty string). The query string will be generated in the correct fashion, depending on the choice of "Method" you made (i.e. if you chose GET or DELETE, the query string will be appended to the URL, if POST or PUT, then it will be sent separately). Also, if you are sending a file using a multipart form, the query string will be created using the multipart form specifications. **See below for some further information on parameter handling.**
Additionally, you can specify whether each parameter should be URL encoded. If you are not sure what this means, it is probably best to select it. If your values contain characters such as the following then encoding is usually required.:

*   ASCII Control Chars
*   Non-ASCII characters
*    Reserved characters:URLs use some characters for special use in defining their syntax. When these characters are not used in their special role inside a URL, they need to be encoded, example: '$', '&', '+', ',' , '/', ':', ';', '=', '?', '@' 
*    Unsafe characters: Some characters present the possibility of being misunderstood within URLs for various reasons. These characters should also always be encoded, example: '', '<', '>', '#', '%', … 

No

File Path:

 Name of the file to send. If left blank, JMeter does not send a file, if filled in, JMeter automatically sends the request as a multipart form request. 
When MIME Type is empty, JMeter will try to guess the MIME type of the given file.

If it is a POST or PUT or PATCH request and there is a single file whose 'Parameter name' attribute (below) is omitted, then the file is sent as the entire body of the request, i.e. no wrappers are added. This allows arbitrary bodies to be sent. This functionality is present for POST requests, and also for PUT requests. **See below for some further information on parameter handling.**

No

Parameter name:

 Value of the "name" web request parameter. 

No

MIME Type

 MIME type (for example, text/plain). If it is a POST or PUT or PATCH request and either the 'name' attribute (below) are omitted or the request body is constructed from parameter values only, then the value of this field is used as the value of the content-type request header. 

No

Retrieve All Embedded Resources from HTML Files

Tell JMeter to parse the HTML file and send HTTP/HTTPS requests for all images, Java applets, JavaScript files, CSSs, etc. referenced in the file. See below for more details. 

No

Save response as MD5 hash?

 If this is selected, then the response is not stored in the sample result. Instead, the 32 character MD5 hash of the data is calculated and stored instead. This is intended for testing large amounts of data. 

No

URLs must match:

 If present, this must be a regular expression that is used to match against any embedded URLs found. So if you only want to download embedded resources from http://example.invalid/, use the expression: http://example\.invalid/.*

No

URLs must not match:

 If present, this must be a regular expression that is used to filter out any embedded URLs found. So if you don't want to download PNG or SVG files from any source, use the expression: .*\.(?i:svg|png)

No

Use concurrent pool

Use a pool of concurrent connections to get embedded resources.

No

Size

Pool size for concurrent connections used to get embedded resources.

No

Source address type

_[Only for HTTP Request with HTTPClient implementation]_

 To distinguish the source address value, select the type of these: 
*    Select _IP/Hostname_ to use a specific IP address or a (local) hostname 
*    Select _Device_ to pick the first available address for that interface which this may be either IPv4 or IPv6 
*    Select _Device IPv4_ to select the IPv4 address of the device name (like eth0, lo, em0, etc.) 
*    Select _Device IPv6_ to select the IPv6 address of the device name (like eth0, lo, em0, etc.) 

No

Source address field

_[Only for HTTP Request with HTTPClient implementation]_

 This property is used to enable IP Spoofing. It overrides the default local IP address for this sample. The JMeter host must have multiple IP addresses (i.e. IP aliases, network interfaces, devices). The value can be a host name, IP address, or a network interface device such as "eth0" or "lo" or "wlan0". 

 If the property httpclient.localaddress is defined, that is used for all HttpClient requests. 

No

The following parameters are available only for **GraphQL HTTP Request**:

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request_parms2 "Link to here")

Attribute

Description

Required

Query

 GraphQL query (or mutation) statement. 

Yes

Variables

 GraphQL query (or mutation) variables in a valid JSON string. **Note**: If the input string is not a valid JSON string, this will be ignored with an ERROR log. 

No

Operation Name

 Optional GraphQL operation name when making a request for multi-operation documents. 

No

 When using Automatic Redirection, cookies are only sent for the initial URL. This can cause unexpected behaviour for web-sites that redirect to a local server. E.g. if www.example.com redirects to www.example.co.uk. In this case the server will probably return cookies for both URLs, but JMeter will only see the cookies for the last host, i.e. www.example.co.uk. If the next request in the test plan uses www.example.com, rather than www.example.co.uk, it will not get the correct cookies. Likewise, Headers are sent for the initial request, and won't be sent for the redirect. This is generally only a problem for manually created test plans, as a test plan created using a recorder would continue from the redirected URL. 

**Parameter Handling:**

 For the POST and PUT method, if there is no file to send, and the name(s) of the parameter(s) are omitted, then the body is created by concatenating all the value(s) of the parameters. Note that the values are concatenated without adding any end-of-line characters. These can be added by using the [__char()](https://jmeter.apache.org/usermanual/functions.html#__char) function in the value fields. This allows arbitrary bodies to be sent. The values are encoded if the encoding flag is set. See also the MIME Type above how you can control the content-type request header that is sent. 

 For other methods, if the name of the parameter is missing, then the parameter is ignored. This allows the use of optional parameters defined by variables.

You have the option to switch to Body Data tab when a request has only unnamed parameters (or no parameters at all). This option is useful in the following cases (amongst others):

*   GWT RPC HTTP Request
*   JSON REST HTTP Request
*   XML REST HTTP Request
*   SOAP HTTP Request

 Note that once you leave the Tree node, you cannot switch back to the parameter tab unless you clear the Body Data tab from its data. 

In Body Data mode, each line will be sent with CRLF appended, apart from the last line. To send a CRLF after the last line of data, just ensure that there is an empty line following it. (This cannot be seen, except by noting whether the cursor can be placed on the subsequent line.)

[![Image 9: Figure 1 - HTTP Request with one unnamed parameter](https://jmeter.apache.org/images/screenshots/http-request-raw-single-parameter.png)](https://jmeter.apache.org/images/screenshots/http-request-raw-single-parameter.png)

Figure 1 - HTTP Request with one unnamed parameter

[![Image 10: Figure 2 - Confirm dialog to switch](https://jmeter.apache.org/images/screenshots/http-request-confirm-raw-body.png)](https://jmeter.apache.org/images/screenshots/http-request-confirm-raw-body.png)

Figure 2 - Confirm dialog to switch

[![Image 11: Figure 3 - HTTP Request using Body Data](https://jmeter.apache.org/images/screenshots/http-request-raw-body.png)](https://jmeter.apache.org/images/screenshots/http-request-raw-body.png)

Figure 3 - HTTP Request using Body Data

**Method Handling:**

 The GET, DELETE, POST, PUT and PATCH request methods work similarly, except that as of 3.1, only POST method supports multipart requests or file upload. The PUT and PATCH method body must be provided as one of the following:

*   define the body as a file with empty Parameter name field; in which case the MIME Type is used as the Content-Type
*   define the body as parameter value(s) with no name
*    use the Body Data tab 

The GET, DELETE and POST methods have an additional way of passing parameters by using the Parameters tab. GET, DELETE, PUT and PATCH require a Content-Type. If not using a file, attach a Header Manager to the sampler and define the Content-Type there.

JMeter scan responses from embedded resources. It uses the property HTTPResponse.parsers, which is a list of parser ids, e.g. htmlParser, cssParser and wmlParser. For each id found, JMeter checks two further properties:

*   id.types - a list of content types 
*   id.className - the parser to be used to extract the embedded resources 

See jmeter.properties file for the details of the settings. If the HTTPResponse.parser property is not set, JMeter reverts to the previous behaviour, i.e. only text/html responses will be scanned

**Emulating slow connections:**

HttpClient4 and Java Sampler support emulation of slow connections; see the following entries in jmeter.properties:

# Define characters per second > 0 to emulate slow connections
#httpclient.socket.http.cps=0
#httpclient.socket.https.cps=0
 However the Java sampler only supports slow HTTPS connections. 
**Response size calculation**

 The Java implementation does not include transport overhead such as chunk headers in the response body size. 

 The HttpClient4 implementation does include the overhead in the response body size, so the value may be greater than the number of bytes in the response content. 

**Retry handling**

 By default retry has been set to 0 for both HttpClient4 and Java implementations, meaning no retry is attempted. 

 For HttpClient4, the retry count can be overridden by setting the relevant JMeter property, for example:

httpclient4.retrycount=3

 With HC4 Implementation, retry will be done on Idempotent Http Methods by default. If you want to retry for all methods, then set property 
httpclient4.request_sent_retry_enabled=true

 Note that the Java implementation does not retry neither by default, you can change this by setting http.java.sampler.retries=3
**Note: Certificates does not conform to algorithm constraints**

 You may encounter the following error: java.security.cert.CertificateException: Certificates does not conform to algorithm constraints if you run a HTTPS request on a web site with a SSL certificate (itself or one of SSL certificates in its chain of trust) with a signature algorithm using MD2 (like md2WithRSAEncryption) or with a SSL certificate with a size lower than 1024 bits.

This error is related to increased security in Java 8.

To allow you to perform your HTTPS request, you can downgrade the security of your Java installation by editing the Java jdk.certpath.disabledAlgorithms property. Remove the MD2 value or the constraint on size, depending on your case.

This property is in this file:

JAVA_HOME/jre/lib/security/java.security
See [Bug 56357](https://bz.apache.org/bugzilla/show_bug.cgi?id=56357) for details.

See also:

*   [Assertion](https://jmeter.apache.org/usermanual/test_plan.html#assertions)
*   [Building a Web Test Plan](https://jmeter.apache.org/usermanual/build-web-test-plan.html)
*   [Building an Advanced Web Test Plan](https://jmeter.apache.org/usermanual/build-adv-web-test-plan.html)
*   [HTTP Authorization Manager](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Authorization_Manager)
*   [HTTP Cookie Manager](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Cookie_Manager)
*   [HTTP Header Manager](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Header_Manager)
*   [HTML Link Parser](https://jmeter.apache.org/usermanual/component_reference.html#HTML_Link_Parser)
*   [HTTP(S) Test Script Recorder](https://jmeter.apache.org/usermanual/component_reference.html#HTTP(S)_Test_Script_Recorder)
*   [HTTP Request Defaults](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request_Defaults)
*   [HTTP Requests and Session ID's: URL Rewriting](https://jmeter.apache.org/usermanual/build-adv-web-test-plan.html#session_url_rewriting)

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

JDBC Request[¶](https://jmeter.apache.org/usermanual/component_reference.html#JDBC_Request "Link to here")
----------------------------------------------------------------------------------------------------------

This sampler lets you send a JDBC Request (an SQL query) to a database.

Before using this you need to set up a [JDBC Connection Configuration](https://jmeter.apache.org/usermanual/component_reference.html#JDBC_Connection_Configuration) Configuration element

If the Variable Names list is provided, then for each row returned by a Select statement, the variables are set up with the value of the corresponding column (if a variable name is provided), and the count of rows is also set up. For example, if the Select statement returns 2 rows of 3 columns, and the variable list is A,,C, then the following variables will be set up:

A_#=2 (number of rows)
A_1=column 1, row 1
A_2=column 1, row 2
C_#=2 (number of rows)
C_1=column 3, row 1
C_2=column 3, row 2

If the Select statement returns zero rows, then the A_# and C_# variables would be set to 0, and no other variables would be set.

Old variables are cleared if necessary - e.g. if the first select retrieves six rows and a second select returns only three rows, the additional variables for rows four, five and six will be removed.

The latency time is set from the time it took to acquire a connection.

[![Image 12: Screenshot for Control-Panel of JDBC Request](https://jmeter.apache.org/images/screenshots/jdbctest/jdbc-request.png)](https://jmeter.apache.org/images/screenshots/jdbctest/jdbc-request.png)

Screenshot of Control-Panel of JDBC Request

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#JDBC_Request_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Variable Name of Pool declared in JDBC Connection Configuration

 Name of the JMeter variable that the connection pool is bound to. This must agree with the 'Variable Name' field of a [JDBC Connection Configuration](https://jmeter.apache.org/usermanual/component_reference.html#JDBC_Connection_Configuration). 

Yes

Query Type

 Set this according to the statement type: 
*   Select Statement
*   Update Statement - use this for Inserts and Deletes as well
*   Callable Statement
*   Prepared Select Statement
*   Prepared Update Statement - use this for Inserts and Deletes as well
*   Commit
*   Rollback
*   Autocommit(false)
*   Autocommit(true)
*   Edit - this should be a variable reference that evaluates to one of the above

 The types Commit, Rollback, Autocommit(false) and Autocommit(true) are special, as they are ignoring the given SQL statements and are changing the state of the connection, only. 

Yes

SQL Query

 SQL query. 

Do not enter a trailing semi-colon.

 There is generally no need to use { and } to enclose Callable statements; however they may be used if the database uses a non-standard syntax. 

 The JDBC driver automatically converts the statement if necessary when it is enclosed in {}. 

 For example: 
*   select * from t_customers where id=23
*   CALL SYSCS_UTIL.SYSCS_EXPORT_TABLE (null, ?, ?, null, null, null)
    *    Parameter values: tablename,filename
    *    Parameter types: VARCHAR,VARCHAR

 The second example assumes you are using Apache Derby. 

Yes

Parameter values

 Comma-separated list of parameter values. Use ]NULL[ to indicate a NULL parameter. (If required, the null string can be changed by defining the property "jdbcsampler.nullmarker".) 

 The list must be enclosed in double-quotes if any of the values contain a comma or double-quote, and any embedded double-quotes must be doubled-up, for example: "Dbl-Quote: "" and Comma: ,"

 There must be as many values as there are placeholders in the statement even if your parameters are OUT ones. Be sure to set a value even if the value will not be used (for example in a CallableStatement). 

Yes, if a prepared or callable statement has parameters

Parameter types

 Comma-separated list of SQL parameter types (e.g. INTEGER, DATE, VARCHAR, DOUBLE) or integer values of Constants. Those integer values can be used, when you use custom database types proposed by driver (For example OracleTypes.CURSOR could be represented by its integer value -10). 

 These are defined as fields in the class java.sql.Types, see for example: 

[Javadoc for java.sql.Types](http://docs.oracle.com/javase/8/docs/api/java/sql/Types.html). 

Note: JMeter will use whatever types are defined by the runtime JVM, so if you are running on a different JVM, be sure to check the appropriate documentation

**If the callable statement has INOUT or OUT parameters, then these must be indicated by prefixing the appropriate parameter types, e.g. instead of "INTEGER", use "INOUT INTEGER".**

 If not specified, "IN" is assumed, i.e. "DATE" is the same as "IN DATE". 

 If the type is not one of the fields found in java.sql.Types, JMeter also accepts the corresponding integer number, e.g. since OracleTypes.CURSOR == -10, you can use "INOUT -10". 

 There must be as many types as there are placeholders in the statement. 

Yes, if a prepared or callable statement has parameters

Variable Names

 Comma-separated list of variable names to hold values returned by Select statements, Prepared Select Statements or CallableStatement. Note that when used with CallableStatement, list of variables must be in the same sequence as the OUT parameters returned by the call. If there are less variable names than OUT parameters only as many results shall be stored in the thread-context variables as variable names were supplied. If more variable names than OUT parameters exist, the additional variables will be ignored 

No

Result Variable Name

 If specified, this will create an Object variable containing a list of row maps. Each map contains the column name as the key and the column data as the value. Usage: 

columnValue = vars.getObject("resultObject").get(0).get("Column Name");

No

Query timeout(s)

 Set a timeout in seconds for query, empty value means 0 which is infinite. -1 means don't set any query timeout which might be needed for use case or when certain drivers don't support timeout. Defaults to 0. 

No

Limit ResultSet

 Limits the number of rows to iterate through the ResultSet. Empty value means -1, e.g. no limitation, which is also the default. This can help to reduce the amount of data to be fetched from the database via the JDBC driver, but affects all possible options of Handle ResultSet respectively – e.g. incomplete ResultSet and a record count ≤ the limit. 

No

Handle ResultSet

 Defines how ResultSet returned from callable statements be handled: 
*   Store As String (default) - All variables on Variable Names list are stored as strings, will not iterate through a ResultSet when present on the list. CLOB s will be converted to Strings. BLOB s will be converted to Strings as if they were an UTF-8 encoded byte-array. Both CLOB s and BLOB s will be cut off after jdbcsampler.max_retain_result_size bytes. 
*   Store As Object - Variables of ResultSet type on Variables Names list will be stored as Object and can be accessed in subsequent tests/scripts and iterated, will not iterate through the ResultSet. CLOB s will be handled as if Store As String was selected. BLOBs will be stored as a byte array. Both CLOB s and BLOB s will be cut off after jdbcsampler.max_retain_result_size bytes. 
*   Count Records - Variables of ResultSet types will be iterated through showing the count of records as result. Variables will be stored as Strings. For BLOB s the size of the object will be stored. 

No

See also:

*   [Building a Database Test Plan](https://jmeter.apache.org/usermanual/build-db-test-plan.html)
*   [JDBC Connection Configuration](https://jmeter.apache.org/usermanual/component_reference.html#JDBC_Connection_Configuration)

Current Versions of JMeter use UTF-8 as the character encoding. Previously the platform default was used.

Ensure Variable Name is unique across Test Plan.

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Java Request[¶](https://jmeter.apache.org/usermanual/component_reference.html#Java_Request "Link to here")
----------------------------------------------------------------------------------------------------------

This sampler lets you control a java class that implements the org.apache.jmeter.protocol.java.sampler.JavaSamplerClient interface. By writing your own implementation of this interface, you can use JMeter to harness multiple threads, input parameter control, and data collection.

The pull-down menu provides the list of all such implementations found by JMeter in its classpath. The parameters can then be specified in the table below - as defined by your implementation. Two simple examples (JavaTest and SleepTest) are provided.

The JavaTest example sampler can be useful for checking test plans, because it allows one to set values in almost all the fields. These can then be used by Assertions, etc. The fields allow variables to be used, so the values of these can readily be seen.

[![Image 13: Screenshot for Control-Panel of Java Request](https://jmeter.apache.org/images/screenshots/java_request.png)](https://jmeter.apache.org/images/screenshots/java_request.png)

Screenshot of Control-Panel of Java Request

 If the method teardownTest is not overridden by a subclass of [AbstractJavaSamplerClient](https://jmeter.apache.org/api/org/apache/jmeter/protocol/java/sampler/AbstractJavaSamplerClient.html), its teardownTest method will not be called. This reduces JMeter memory requirements. This will not have any impact on existing Test plans. 

The Add/Delete buttons don't serve any purpose at present.

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Java_Request_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Classname

The specific implementation of the JavaSamplerClient interface to be sampled.

Yes

Send Parameters with Request

A list of arguments that will be passed to the sampled class. All arguments are sent as Strings. See below for specific settings.

No

The following parameters apply to the SleepTest and JavaTest implementations:

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Java_Request_parms2 "Link to here")

Attribute

Description

Required

Sleep_time

How long to sleep for (ms)

Yes

Sleep_mask

 How much "randomness" to add: 

 The sleep time is calculated as follows: totalSleepTime = SleepTime + (System.currentTimeMillis() % SleepMask)

Yes

The following parameters apply additionally to the JavaTest implementation:

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Java_Request_parms3 "Link to here")

Attribute

Description

Required

Label

 The label to use. If provided, overrides Name

No

ResponseCode

If provided, sets the SampleResult ResponseCode.

No

ResponseMessage

If provided, sets the SampleResult ResponseMessage.

No

Status

 If provided, sets the SampleResult Status. If this equals "OK" (ignoring case) then the status is set to success, otherwise the sample is marked as failed. 

No

SamplerData

If provided, sets the SampleResult SamplerData.

No

ResultData

If provided, sets the SampleResult ResultData.

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

LDAP Request[¶](https://jmeter.apache.org/usermanual/component_reference.html#LDAP_Request "Link to here")
----------------------------------------------------------------------------------------------------------

 This Sampler lets you send a different LDAP request(Add, Modify, Delete and Search) to an LDAP server. 
If you are going to send multiple requests to the same LDAP server, consider using an [LDAP Request Defaults](https://jmeter.apache.org/usermanual/component_reference.html#LDAP_Request_Defaults) Configuration Element so you do not have to enter the same information for each LDAP Request.

 The same way the [Login Config Element](https://jmeter.apache.org/usermanual/component_reference.html#Login_Config_Element) also using for Login and password. 

[![Image 14: Screenshot for Control-Panel of LDAP Request](https://jmeter.apache.org/images/screenshots/ldap_request.png)](https://jmeter.apache.org/images/screenshots/ldap_request.png)

Screenshot of Control-Panel of LDAP Request

There are two ways to create test cases for testing an LDAP Server.

1.   Inbuilt Test cases.
2.   User defined Test cases.

There are four test scenarios of testing LDAP. The tests are given below:

1.    Add Test 
    1.    Inbuilt test: 
This will add a pre-defined entry in the LDAP Server and calculate the execution time. After execution of the test, the created entry will be deleted from the LDAP Server.

    2.    User defined test: 
This will add the entry in the LDAP Server. User has to enter all the attributes in the table.The entries are collected from the table to add. The execution time is calculated. The created entry will not be deleted after the test.

2.    Modify Test 
    1.    Inbuilt test: 
This will create a pre-defined entry first, then will modify the created entry in the LDAP Server.And calculate the execution time. After execution of the test, the created entry will be deleted from the LDAP Server.

    2.    User defined test: 
This will modify the entry in the LDAP Server. User has to enter all the attributes in the table. The entries are collected from the table to modify. The execution time is calculated. The entry will not be deleted from the LDAP Server.

3.    Search Test 
    1.    Inbuilt test: 
This will create the entry first, then will search if the attributes are available. It calculates the execution time of the search query. At the end of the execution,created entry will be deleted from the LDAP Server.

    2.    User defined test: 
This will search the user defined entry(Search filter) in the Search base (again, defined by the user). The entries should be available in the LDAP Server. The execution time is calculated.

4.    Delete Test 
    1.    Inbuilt test: 
This will create a pre-defined entry first, then it will be deleted from the LDAP Server. The execution time is calculated.

    2.    User defined test: 
This will delete the user-defined entry in the LDAP Server. The entries should be available in the LDAP Server. The execution time is calculated.

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#LDAP_Request_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Server Name or IP

 Domain name or IP address of the LDAP server. JMeter assumes the LDAP server is listening on the default port (389). 

Yes

Port

 Port to connect to (default is 389). 

Yes

root DN

Base DN to use for LDAP operations

Yes

Username

LDAP server username.

Usually

Password

LDAP server password. (N.B. this is stored unencrypted in the test plan)

Usually

Entry DN

 the name of the context to create or Modify; may not be empty. 

 You have to set the right attributes of the object yourself. So if you want to add cn=apache,ou=test you have to add in the table name and value to cn and apache. 

Yes, if User Defined Test and Add Test or Modify Test is selected

Delete

the name of the context to Delete; may not be empty

Yes, if User Defined Test and Delete Test is selected

Search base

the name of the context or object to search

Yes, if User Defined Test and Search Test is selected

Search filter

 the filter expression to use for the search; may not be null

Yes, if User Defined Test and Search Test is selected

add test

 Use these name, value pairs for creation of the new object in the given context 

Yes, if User Defined Test and add Test is selected

modify test

 Use these name, value pairs for modification of the given context object 

Yes, if User Defined Test and Modify Test is selected

See also:

*   [Building an LDAP Test Plan](https://jmeter.apache.org/usermanual/build-ldap-test-plan.html)
*   [LDAP Request Defaults](https://jmeter.apache.org/usermanual/component_reference.html#LDAP_Request_Defaults)

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

LDAP Extended Request[¶](https://jmeter.apache.org/usermanual/component_reference.html#LDAP_Extended_Request "Link to here")
----------------------------------------------------------------------------------------------------------------------------

 This Sampler can send all 8 different LDAP requests to an LDAP server. It is an extended version of the LDAP sampler, therefore it is harder to configure, but can be made much closer resembling a real LDAP session. 
If you are going to send multiple requests to the same LDAP server, consider using an [LDAP Extended Request Defaults](https://jmeter.apache.org/usermanual/component_reference.html#LDAP_Extended_Request_Defaults) Configuration Element so you do not have to enter the same information for each LDAP Request.

[![Image 15: Screenshot for Control-Panel of LDAP Extended Request](https://jmeter.apache.org/images/screenshots/ldapext_request.png)](https://jmeter.apache.org/images/screenshots/ldapext_request.png)

Screenshot of Control-Panel of LDAP Extended Request

There are nine test operations defined. These operations are given below:

**Thread bind**
Any LDAP request is part of an LDAP session, so the first thing that should be done is starting a session to the LDAP server. For starting this session a thread bind is used, which is equal to the LDAP "bind" operation. The user is requested to give a username (Distinguished name) and password, which will be used to initiate a session. When no password, or the wrong password is specified, an anonymous session is started. Take care, omitting the password will not fail this test, a wrong password will. (N.B. this is stored unencrypted in the test plan)

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Servername

The name (or IP-address) of the LDAP server.

Yes

Port

The port number that the LDAP server is listening to. If this is omitted JMeter assumes the LDAP server is listening on the default port(389).

No

DN

The distinguished name of the base object that will be used for any subsequent operation. It can be used as a starting point for all operations. You cannot start any operation on a higher level than this DN!

No

Username

Full distinguished name of the user as which you want to bind.

No

Password

Password for the above user. If omitted it will result in an anonymous bind. If it is incorrect, the sampler will return an error and revert to an anonymous bind. (N.B. this is stored unencrypted in the test plan)

No

Connection timeout (in milliseconds)

Timeout for connection, if exceeded connection will be aborted

No

Use Secure LDAP Protocol

 Use ldaps:// scheme instead of ldap://

No

Trust All Certificates

 Trust all certificates, only used if Use Secure LDAP Protocol is checked 

No

**Thread unbind**
This is simply the operation to end a session. It is equal to the LDAP "unbind" operation.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

**Single bind/unbind**
This is a combination of the LDAP "bind" and "unbind" operations. It can be used for an authentication request/password check for any user. It will open a new session, just to check the validity of the user/password combination, and end the session again.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Username

Full distinguished name of the user as which you want to bind.

Yes

Password

Password for the above user. If omitted it will result in an anonymous bind. If it is incorrect, the sampler will return an error. (N.B. this is stored unencrypted in the test plan)

No

**Rename entry**
This is the LDAP "moddn" operation. It can be used to rename an entry, but also for moving an entry or a complete subtree to a different place in the LDAP tree.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Old entry name

The current distinguished name of the object you want to rename or move, relative to the given DN in the thread bind operation.

Yes

New distinguished name

The new distinguished name of the object you want to rename or move, relative to the given DN in the thread bind operation.

Yes

**Add test**
This is the LDAP "add" operation. It can be used to add any kind of object to the LDAP server.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Entry DN

Distinguished name of the object you want to add, relative to the given DN in the thread bind operation.

Yes

Add test

A list of attributes and their values you want to use for the object. If you need to add a multiple value attribute, you need to add the same attribute with their respective values several times to the list.

Yes

**Delete test**
This is the LDAP "delete" operation, it can be used to delete an object from the LDAP tree

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Delete

Distinguished name of the object you want to delete, relative to the given DN in the thread bind operation.

Yes

**Search test**
This is the LDAP "search" operation, and will be used for defining searches.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Search base

Distinguished name of the subtree you want your search to look in, relative to the given DN in the thread bind operation.

No

Search Filter

searchfilter, must be specified in LDAP syntax.

Yes

Scope

 Use 0 for baseobject-, 1 for onelevel- and 2 for a subtree search. (Default=0) 

No

Size Limit

 Specify the maximum number of results you want back from the server. (default=0, which means no limit.) When the sampler hits the maximum number of results, it will fail with errorcode 4

No

Time Limit

 Specify the maximum amount of (cpu)time (in milliseconds) that the server can spend on your search. Take care, this does not say anything about the response time. (default is 0, which means no limit) 

No

Attributes

Specify the attributes you want to have returned, separated by a semicolon. An empty field will return all attributes

No

Return object

 Whether the object will be returned (true) or not (false). Default=false

No

Dereference aliases

 If true, it will dereference aliases, if false, it will not follow them (default=false) 

No

Parse the search results?

 If true, the search results will be added to the response data. If false, a marker - whether results where found or not - will be added to the response data. 

No

**Modification test**
This is the LDAP "modify" operation. It can be used to modify an object. It can be used to add, delete or replace values of an attribute.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Entry name

Distinguished name of the object you want to modify, relative to the given DN in the thread bind operation

Yes

Modification test

 The attribute-value-opCode triples. 

 The opCode can be any valid LDAP operationCode (add, delete, remove or replace). 

 If you don't specify a value with a delete operation, all values of the given attribute will be deleted. 

 If you do specify a value in a delete operation, only the given value will be deleted. 

 If this value is non-existent, the sampler will fail the test. 

Yes

**Compare**
This is the LDAP "compare" operation. It can be used to compare the value of a given attribute with some already known value. In reality this is mostly used to check whether a given person is a member of some group. In such a case you can compare the DN of the user as a given value, with the values in the attribute "member" of an object of the type groupOfNames. If the compare operation fails, this test fails with errorcode 49.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Entry DN

The current distinguished name of the object of which you want to compare an attribute, relative to the given DN in the thread bind operation.

Yes

Compare filter

 In the form "attribute=value" 

Yes

See also:

*   [Building an LDAP Test Plan](https://jmeter.apache.org/usermanual/build-ldapext-test-plan.html)
*   [LDAP Extended Request Defaults](https://jmeter.apache.org/usermanual/component_reference.html#LDAP_Extended_Request_Defaults)

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Access Log Sampler[¶](https://jmeter.apache.org/usermanual/component_reference.html#Access_Log_Sampler "Link to here")
----------------------------------------------------------------------------------------------------------------------

AccessLogSampler was designed to read access logs and generate http requests. For those not familiar with the access log, it is the log the webserver maintains of every request it accepted. This means every image, CSS file, JavaScript file, html file, …

Tomcat uses the common format for access logs. This means any webserver that uses the common log format can use the AccessLogSampler. Server that use common log format include: Tomcat, Resin, Weblogic, and SunOne. Common log format looks like this:

127.0.0.1 - - [21/Oct/2003:05:37:21 -0500] "GET /index.jsp?%2Findex.jsp= HTTP/1.1" 200 8343

 The current implementation of the parser only looks at the text within the quotes that contains one of the HTTP protocol methods (GET, PUT, POST, DELETE, …). Everything else is stripped out and ignored. For example, the response code is completely ignored by the parser. 

For the future, it might be nice to filter out entries that do not have a response code of 200. Extending the sampler should be fairly simple. There are two interfaces you have to implement:

*   org.apache.jmeter.protocol.http.util.accesslog.LogParser
*   org.apache.jmeter.protocol.http.util.accesslog.Generator

The current implementation of AccessLogSampler uses the generator to create a new HTTPSampler. The servername, port and get images are set by AccessLogSampler. Next, the parser is called with integer 1, telling it to parse one entry. After that, HTTPSampler.sample() is called to make the request.

samp = (HTTPSampler) GENERATOR.generateRequest();
samp.setDomain(this.getDomain());
samp.setPort(this.getPort());
samp.setImageParser(this.isImageParser());
PARSER.parse(1);
res = samp.sample();
res.setSampleLabel(samp.toString());
 The required methods in LogParser are: 
*   setGenerator(Generator)
*   parse(int)

Classes implementing Generator interface should provide concrete implementation for all the methods. For an example of how to implement either interface, refer to StandardGenerator and TCLogParser.

[![Image 16: Screenshot for Control-Panel of Access Log Sampler](https://jmeter.apache.org/images/screenshots/accesslogsampler.png)](https://jmeter.apache.org/images/screenshots/accesslogsampler.png)

Screenshot of Control-Panel of Access Log Sampler

(Beta Code)
-----------

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Access_Log_Sampler_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Server

Domain name or IP address of the web server.

Yes

Protocol

Scheme

No (defaults to http

Port

Port the web server is listening to.

No (defaults to 80)

Log parser class

The log parser class is responsible for parsing the logs.

Yes (default provided)

Filter

The filter class is used to filter out certain lines.

No

Location of log file

The location of the access log file.

Yes

The TCLogParser processes the access log independently for each thread. The SharedTCLogParser and OrderPreservingLogParser share access to the file, i.e. each thread gets the next entry in the log.

The SessionFilter is intended to handle Cookies across threads. It does not filter out any entries, but modifies the cookie manager so that the cookies for a given IP are processed by a single thread at a time. If two threads try to process samples from the same client IP address, then one will be forced to wait until the other has completed.

The LogFilter is intended to allow access log entries to be filtered by filename and regex, as well as allowing for the replacement of file extensions. However, it is not currently possible to configure this via the GUI, so it cannot really be used.

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

BeanShell Sampler[¶](https://jmeter.apache.org/usermanual/component_reference.html#BeanShell_Sampler "Link to here")
--------------------------------------------------------------------------------------------------------------------

This sampler allows you to write a sampler using the BeanShell scripting language.

**For full details on using BeanShell, please see the [BeanShell website.](http://www.beanshell.org/)**

 Migration to [JSR223 Sampler](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_Sampler)+Groovy is highly recommended for performance, support of new Java features and limited maintenance of the BeanShell library. 

The test element supports the ThreadListener and TestListener interface methods. These must be defined in the initialisation file. See the file BeanShellListeners.bshrc for example definitions.

The BeanShell sampler also supports the Interruptible interface. The interrupt() method can be defined in the script or the init file.

[![Image 17: Screenshot for Control-Panel of BeanShell Sampler](https://jmeter.apache.org/images/screenshots/beanshellsampler.png)](https://jmeter.apache.org/images/screenshots/beanshellsampler.png)

Screenshot of Control-Panel of BeanShell Sampler

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#BeanShell_Sampler_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree. The name is stored in the script variable Label

No

Reset bsh.Interpreter before each call

 If this option is selected, then the interpreter will be recreated for each sample. This may be necessary for some long running scripts. For further information, see [Best Practices - BeanShell scripting](https://jmeter.apache.org/usermanual/best-practices.html#bsh_scripting). 

Yes

Parameters

 Parameters to pass to the BeanShell script. This is intended for use with script files; for scripts defined in the GUI, you can use whatever variable and function references you need within the script itself. The parameters are stored in the following variables: Parameters string containing the parameters as a single variable bsh.args String array containing parameters, split on white-space

No

Script file

 A file containing the BeanShell script to run. The file name is stored in the script variable FileName

No

Script

 The BeanShell script to run. The return value (if not null) is stored as the sampler result. 

Yes (unless script file is provided)

 N.B. Each Sampler instance has its own BeanShell interpreter, and Samplers are only called from a single thread 

If the property "beanshell.sampler.init" is defined, it is passed to the Interpreter as the name of a sourced file. This can be used to define common methods and variables. There is a sample init file in the bin directory: BeanShellSampler.bshrc.

If a script file is supplied, that will be used, otherwise the script will be used.

 JMeter processes function and variable references before passing the script field to the interpreter, so the references will only be resolved once. Variable and function references in script files will be passed verbatim to the interpreter, which is likely to cause a syntax error. In order to use runtime variables, please use the appropriate props methods, e.g.props.get("START.HMS"); props.put("PROP1","1234");

 BeanShell does not currently support Java 5 syntax such as generics and the enhanced for loop. 

Before invoking the script, some variables are set up in the BeanShell interpreter:

The contents of the Parameters field is put into the variable "Parameters". The string is also split into separate tokens using a single space as the separator, and the resulting list is stored in the String array bsh.args.

The full list of BeanShell variables that is set up is as follows:

*   log - the [Logger](https://www.slf4j.org/api/org/slf4j/Logger.html)
*   Label - the Sampler label 
*   FileName - the file name, if any 
*   Parameters - text from the Parameters field 
*   bsh.args - the parameters, split as described above 
*   SampleResult - pointer to the current [SampleResult](https://jmeter.apache.org/api/org/apache/jmeter/samplers/SampleResult.html)
*   ResponseCode defaults to 200
*   ResponseMessage defaults to "OK" 
*   IsSuccess defaults to true
*   ctx - [JMeterContext](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterContext.html)
*   vars - [JMeterVariables](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterVariables.html) - e.g. vars.get("VAR1");
vars.put("VAR2","value");
vars.remove("VAR3");
vars.putObject("OBJ1",new Object());
*   props - JMeterProperties (class [java.util.Properties](https://docs.oracle.com/javase/8/docs/api/java/util/Properties.html)) - e.g. props.get("START.HMS");
props.put("PROP1","1234");

When the script completes, control is returned to the Sampler, and it copies the contents of the following script variables into the corresponding variables in the [SampleResult](https://jmeter.apache.org/api/org/apache/jmeter/samplers/SampleResult.html):

*   ResponseCode - for example 200
*   ResponseMessage - for example "OK" 
*   IsSuccess - true or false

The SampleResult ResponseData is set from the return value of the script. If the script returns null, it can set the response directly, by using the method SampleResult.setResponseData(data), where data is either a String or a byte array. The data type defaults to "text", but can be set to binary by using the method SampleResult.setDataType(SampleResult.BINARY).

The SampleResult variable gives the script full access to all the fields and methods in the SampleResult. For example, the script has access to the methods setStopThread(boolean) and setStopTest(boolean). Here is a simple (not very useful!) example script:

if (bsh.args[0].equalsIgnoreCase("StopThread")) {
    log.info("Stop Thread detected!");
    SampleResult.setStopThread(true);
}
return "Data from sample with Label "+Label;
//or
SampleResult.setResponseData("My data");
return null;

Another example: 

 ensure that the property beanshell.sampler.init=BeanShellSampler.bshrc is defined in jmeter.properties. The following script will show the values of all the variables in the ResponseData field:

return getVariables();

For details on the methods available for the various classes ([JMeterVariables](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterVariables.html), [SampleResult](https://jmeter.apache.org/api/org/apache/jmeter/samplers/SampleResult.html) etc.) please check the Javadoc or the source code. Beware however that misuse of any methods can cause subtle faults that may be difficult to find.

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

JSR223 Sampler[¶](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_Sampler "Link to here")
--------------------------------------------------------------------------------------------------------------

The JSR223 Sampler allows JSR223 script code to be used to perform a sample or some computation required to create/update variables.

 If you don't want to generate a [SampleResult](https://jmeter.apache.org/api/org/apache/jmeter/samplers/SampleResult.html) when this sampler is run, call the following method: SampleResult.setIgnore(); This call will have the following impact: 
*   SampleResult will not be delivered to SampleListeners like View Results Tree, Summariser ...
*   SampleResult will not be evaluated in Assertions nor PostProcessors
*   SampleResult will be evaluated to computing last sample status (${JMeterThread.last_sample_ok}), and ThreadGroup "Action to be taken after a Sampler error" (since JMeter 5.4)

The JSR223 test elements have a feature (compilation) that can significantly increase performance. To benefit from this feature:

*   Use Script files instead of inlining them. This will make JMeter compile them if this feature is available on ScriptEngine and cache them.
*    Or Use Script Text and check Cache compiled script if available property.  When using this feature, ensure your script code does not use JMeter variables or JMeter function calls directly in script code as caching would only cache first replacement. Instead use script parameters.    To benefit from caching and compilation, the language engine used for scripting must implement JSR223 [Compilable](https://docs.oracle.com/javase/8/docs/api/javax/script/Compilable.html) interface (Groovy is one of these, java, beanshell and javascript are not)    

 When using Groovy as scripting language and not checking Cache compiled script if available (while caching is recommended), you should set this JVM Property -Dgroovy.use.classvalue=true due to a Groovy Memory leak as of version 2.4.6, see: 
    *   [GROOVY-7683](https://issues.apache.org/jira/browse/GROOVY-7683)
    *   [GROOVY-7591](https://issues.apache.org/jira/browse/GROOVY-7591)
    *   [JDK-8136353](https://bugs.openjdk.java.net/browse/JDK-8136353)

 Cache size is controlled by the following JMeter property (jmeter.properties): jsr223.compiled_scripts_cache_size=100

 Unlike the [BeanShell Sampler](https://jmeter.apache.org/usermanual/component_reference.html#BeanShell_Sampler), the interpreter is not saved between invocations. 

 JSR223 Test Elements using Script file or Script text + checked Cache compiled script if available are now compiled if ScriptEngine supports this feature, this enables great performance enhancements. 

[![Image 18: Screenshot for Control-Panel of JSR223 Sampler](https://jmeter.apache.org/images/screenshots/jsr223-sampler.png)](https://jmeter.apache.org/images/screenshots/jsr223-sampler.png)

Screenshot of Control-Panel of JSR223 Sampler

 JMeter processes function and variable references before passing the script field to the interpreter, so the references will only be resolved once. Variable and function references in script files will be passed verbatim to the interpreter, which is likely to cause a syntax error. In order to use runtime variables, please use the appropriate props methods, e.g. props.get("START.HMS");
props.put("PROP1","1234");

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_Sampler_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Scripting Language

 Name of the JSR223 scripting language to be used. 

 There are other languages supported than those that appear in the drop-down list. Others may be available if the appropriate jar is installed in the JMeter lib directory. 

 Notice that some languages such as Velocity may use a different syntax for JSR223 variables, e.g. $log.debug("Hello " + $vars.get("a")); for Velocity. 

Yes

Script File

 Name of a file to be used as a JSR223 script, if a relative file path is used, then it will be relative to directory referenced by "user.dir" System property 

No

Parameters

List of parameters to be passed to the script file or the script.

No

Cache compiled script if available

 If checked (advised) and the language used supports [Compilable](https://docs.oracle.com/javase/8/docs/api/javax/script/Compilable.html) interface (Groovy is one of these, java, beanshell and javascript are not), JMeter will compile the Script and cache it using its MD5 hash as unique cache key 

No

Script

Script to be passed to JSR223 language

Yes (unless script file is provided)

If a script file is supplied, that will be used, otherwise the script will be used.

Before invoking the script, some variables are set up. Note that these are JSR223 variables - i.e. they can be used directly in the script.

*   log - the [Logger](https://www.slf4j.org/api/org/slf4j/Logger.html)
*   Label - the Sampler label 
*   FileName - the file name, if any 
*   Parameters - text from the Parameters field 
*   args - the parameters, split as described above 
*   SampleResult - pointer to the current [SampleResult](https://jmeter.apache.org/api/org/apache/jmeter/samplers/SampleResult.html)
*   sampler - ([Sampler](https://jmeter.apache.org/api/org/apache/jmeter/samplers/Sampler.html)) - pointer to current Sampler 
*   ctx - [JMeterContext](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterContext.html)
*   vars - [JMeterVariables](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterVariables.html) - e.g. vars.get("VAR1");
vars.put("VAR2","value");
vars.remove("VAR3");
vars.putObject("OBJ1",new Object());
*   props - JMeterProperties (class [java.util.Properties](https://docs.oracle.com/javase/8/docs/api/java/util/Properties.html)) - e.g. props.get("START.HMS");
props.put("PROP1","1234");
*   OUT - System.out - e.g. OUT.println("message")

The [SampleResult](https://jmeter.apache.org/api/org/apache/jmeter/samplers/SampleResult.html) ResponseData is set from the return value of the script. If the script returns null, it can set the response directly, by using the method SampleResult.setResponseData(data), where data is either a String or a byte array. The data type defaults to "text", but can be set to binary by using the method SampleResult.setDataType(SampleResult.BINARY).

The SampleResult variable gives the script full access to all the fields and methods in the SampleResult. For example, the script has access to the methods setStopThread(boolean) and setStopTest(boolean).

Unlike the BeanShell Sampler, the JSR223 Sampler does not set the ResponseCode, ResponseMessage and sample status via script variables. Currently the only way to changes these is via the [SampleResult](https://jmeter.apache.org/api/org/apache/jmeter/samplers/SampleResult.html) methods:

*   SampleResult.setSuccessful(true/false)
*   SampleResult.setResponseCode("code")
*   SampleResult.setResponseMessage("message")

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

TCP Sampler[¶](https://jmeter.apache.org/usermanual/component_reference.html#TCP_Sampler "Link to here")
--------------------------------------------------------------------------------------------------------

The TCP Sampler opens a TCP/IP connection to the specified server. It then sends the text, and waits for a response.

If "Re-use connection" is selected, connections are shared between Samplers in the same thread, provided that the exact same host name string and port are used. Different hosts/port combinations will use different connections, as will different threads. If both of "Re-use connection" and "Close connection" are selected, the socket will be closed after running the sampler. On the next sampler, another socket will be created. You may want to close a socket at the end of each thread loop.

If an error is detected - or "Re-use connection" is not selected - the socket is closed. Another socket will be reopened on the next sample.

The following properties can be used to control its operation:

tcp.status.prefix text that precedes a status number tcp.status.suffix text that follows a status number tcp.status.properties name of property file to convert status codes to messages tcp.handler Name of TCP Handler class (default TCPClientImpl) - only used if not specified on the GUI  The class that handles the connection is defined by the GUI, failing that the property tcp.handler. If not found, the class is then searched for in the package org.apache.jmeter.protocol.tcp.sampler. 
Users can provide their own implementation. The class must extend org.apache.jmeter.protocol.tcp.sampler.TCPClient.

The following implementations are currently provided.

*   TCPClientImpl
*   BinaryTCPClientImpl
*   LengthPrefixedBinaryTCPClientImpl

 The implementations behave as follows: TCPClientImpl This implementation is fairly basic. When reading the response, it reads until the end of line byte, if this is defined by setting the property tcp.eolByte, otherwise until the end of the input stream. You can control charset encoding by setting tcp.charset, which will default to Platform default encoding. BinaryTCPClientImpl This implementation converts the GUI input, which must be a hex-encoded string, into binary, and performs the reverse when reading the response. When reading the response, it reads until the end of message byte, if this is defined by setting the property tcp.BinaryTCPClient.eomByte, otherwise until the end of the input stream. LengthPrefixedBinaryTCPClientImpl This implementation extends BinaryTCPClientImpl by prefixing the binary message data with a binary length byte. The length prefix defaults to 2 bytes. This can be changed by setting the property tcp.binarylength.prefix.length. **Timeout handling** If the timeout is set, the read will be terminated when this expires. So if you are using an eolByte/eomByte, make sure the timeout is sufficiently long, otherwise the read will be terminated early. **Response handling** If tcp.status.prefix is defined, then the response message is searched for the text following that up to the suffix. If any such text is found, it is used to set the response code. The response message is then fetched from the properties file (if provided). 

 Usage of pre- and suffix[¶](https://jmeter.apache.org/usermanual/component_reference.html#tcp-prefix-example "Link to here")

 For example, if the prefix = "[" and the suffix = "]", then the following response: [J28] XI123,23,GBP,CR would have the response code J28. 

 Response codes in the range "400"-"499" and "500"-"599" are currently regarded as failures; all others are successful. [This needs to be made configurable!] 

The login name/password are not used by the supplied TCP implementations.

 Sockets are disconnected at the end of a test run. 

[![Image 19: Screenshot for Control-Panel of TCP Sampler](https://jmeter.apache.org/images/screenshots/tcpsampler.png)](https://jmeter.apache.org/images/screenshots/tcpsampler.png)

Screenshot of Control-Panel of TCP Sampler

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#TCP_Sampler_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

TCPClient classname

 Name of the TCPClient class. Defaults to the property tcp.handler, failing that TCPClientImpl. 

No

ServerName or IP

Name or IP of TCP server

Yes

Port Number

Port to be used

Yes

Re-use connection

If selected, the connection is kept open. Otherwise it is closed when the data has been read.

Yes

Close connection

If selected, the connection will be closed after running the sampler.

Yes

SO_LINGER

 Enable/disable SO_LINGER with the specified linger time in seconds when a socket is created. If you set "SO_LINGER" value as 0, you may prevent large numbers of sockets sitting around with a TIME_WAIT status. 

No

End of line(EOL) byte value

 Byte value for end of line, set this to a value outside the range -128 to +127 to skip eol checking. You may set this in jmeter.properties file as well with eolByte property. If you set this in TCP Sampler Config and in jmeter.properties file at the same time, the setting value in the TCP Sampler Config will be used. 

No

Connect Timeout

 Connect Timeout (milliseconds, 0 disables). 

No

Response Timeout

 Response Timeout (milliseconds, 0 disables). 

No

Set NoDelay

 See java.net.Socket.setTcpNoDelay(). If selected, this will disable Nagle's algorithm, otherwise Nagle's algorithm will be used. 

Yes

Text to Send

Text to be sent

Yes

Login User

User Name - not used by default implementation

No

Password

Password - not used by default implementation (N.B. this is stored unencrypted in the test plan)

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

JMS Publisher[¶](https://jmeter.apache.org/usermanual/component_reference.html#JMS_Publisher "Link to here")
------------------------------------------------------------------------------------------------------------

JMS Publisher will publish messages to a given destination (topic/queue). For those not familiar with JMS, it is the J2EE specification for messaging. There are numerous JMS servers on the market and several open source options.

JMeter does not include any JMS implementation jar; this must be downloaded from the JMS provider and put in the lib directory

[![Image 20: Screenshot for Control-Panel of JMS Publisher](https://jmeter.apache.org/images/screenshots/jmspublisher.png)](https://jmeter.apache.org/images/screenshots/jmspublisher.png)

Screenshot of Control-Panel of JMS Publisher

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#JMS_Publisher_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

use JNDI properties file

 use jndi.properties. Note that the file must be on the classpath - e.g. by updating the user.classpath JMeter property. If this option is not selected, JMeter uses the "JNDI Initial Context Factory" and "Provider URL" fields to create the connection. 

Yes

JNDI Initial Context Factory

Name of the context factory

No

Provider URL

The URL for the JMS provider

Yes, unless using jndi.properties

Destination

The message destination (topic or queue name)

Yes

Setup

 The destination setup type. With At startup, the destination name is static (i.e. always same name during the test), with Each sample, the destination name is dynamic and is evaluate at each sample (i.e. the destination name may be a variable) 

Yes

Authentication

Authentication requirement for the JMS provider

Yes

User

User Name

No

Password

Password (N.B. this is stored unencrypted in the test plan)

No

Expiration

 The expiration time (in milliseconds) of the message before it becomes obsolete. If you do not specify an expiration time, the default value is 0 (never expires). 

No

Priority

 The priority level of the message. There are ten priority levels from 0 (lowest) to 9 (highest). If you do not specify a priority level, the default level is 4. 

No

Reconnect on error codes (regex)

Regular expression for JMSException error codes which force reconnection. If empty no reconnection will be done

No

Number of samples to aggregate

Number of samples to aggregate

Yes

Message source

 Where to obtain the message: From File means the referenced file will be read and reused by all samples. If file name changes it is reloaded since JMeter 3.0 Random File from folder specified below means a random file will be selected from folder specified below, this folder must contain either files with extension .dat for Bytes Messages, or files with extension .txt or .obj for Object or Text messages Text area The Message to use either for Text or Object message

Yes

Message type

Text, Map, Object message or Bytes Message

Yes

Content encoding

 Specify the encoding for reading the message source file: RAW: No variable support from the file and load it with default system charset.DEFAULT: Load file with default system encoding, except for XML which relies on XML prolog. If the file contain variables, they will be processed.Standard charsets: The specified encoding (valid or not) is used for reading the file and processing variables

Yes

Use non-persistent delivery mode?

 Whether to set DeliveryMode.NON_PERSISTENT (defaults to false) 

No

JMS Properties

 The JMS Properties are properties specific for the underlying messaging system. You can setup the name, the value and the class (type) of value. Default type is String. For example: for WebSphere 5.1 web services you will need to set the JMS Property targetService to test webservices through JMS. 

No

For the MapMessage type, JMeter reads the source as lines of text. Each line must have 3 fields, delimited by commas. The fields are:

*   Name of entry
*    Object class name, e.g. "String" (assumes java.lang package if not specified) 
*   Object string value

valueOf(String)
name,String,Example
size,Integer,1234

 The Object message is implemented and works as follow: 
*    Put the JAR that contains your object and its dependencies in jmeter_home/lib/ folder 
*   Serialize your object as XML using XStream
*    Either put result in a file suffixed with .txt or .obj or put XML content directly in Text Area 

 Note that if message is in a file, replacement of properties will not occur while it will if you use Text Area. 

The following table shows some values which may be useful when configuring JMS:

| Apache [ActiveMQ](http://activemq.apache.org/) | Value(s) | Comment |
| --- | --- | --- |
| Context Factory | org.apache.activemq.jndi.ActiveMQInitialContextFactory | . |
| Provider URL | vm://localhost |  |
| Provider URL | vm:(broker:(vm://localhost)?persistent=false) | Disable persistence |
| Queue Reference | dynamicQueues/QUEUENAME | [Dynamically define](http://activemq.apache.org/jndi-support.html#JNDISupport-Dynamicallycreatingdestinations) the QUEUENAME to JNDI |
| Topic Reference | dynamicTopics/TOPICNAME | [Dynamically define](http://activemq.apache.org/jndi-support.html#JNDISupport-Dynamicallycreatingdestinations) the TOPICNAME to JNDI |

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

JMS Subscriber[¶](https://jmeter.apache.org/usermanual/component_reference.html#JMS_Subscriber "Link to here")
--------------------------------------------------------------------------------------------------------------

JMS Subscriber will subscribe to messages in a given destination (topic or queue). For those not familiar with JMS, it is the J2EE specification for messaging. There are numerous JMS servers on the market and several open source options.

JMeter does not include any JMS implementation jar; this must be downloaded from the JMS provider and put in the lib directory

[![Image 21: Screenshot for Control-Panel of JMS Subscriber](https://jmeter.apache.org/images/screenshots/jmssubscriber.png)](https://jmeter.apache.org/images/screenshots/jmssubscriber.png)

Screenshot of Control-Panel of JMS Subscriber

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#JMS_Subscriber_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

use JNDI properties file

 use jndi.properties. Note that the file must be on the classpath - e.g. by updating the user.classpath JMeter property. If this option is not selected, JMeter uses the "JNDI Initial Context Factory" and "Provider URL" fields to create the connection. 

Yes

JNDI Initial Context Factory

Name of the context factory

No

Provider URL

The URL for the JMS provider

No

Destination

the message destination (topic or queue name)

Yes

Durable Subscription ID

The ID to use for a durable subscription. On first use the respective queue will automatically be generated by the JMS provider if it does not exist yet.

No

Client ID

 The Client ID to use when you use a durable subscription. Be sure to add a variable like ${__threadNum} when you have more than one Thread. 

No

JMS Selector

Message Selector as defined by JMS specification to extract only messages that respect the Selector condition. Syntax uses subpart of SQL 92.

No

Setup

 The destination setup type. With At startup, the destination name is static (i.e. always same name during the test), with Each sample, the destination name is dynamic and is evaluated at each sample (i.e. the destination name may be a variable) 

Yes

Authentication

Authentication requirement for the JMS provider

Yes

User

User Name

No

Password

Password (N.B. this is stored unencrypted in the test plan)

No

Number of samples to aggregate

number of samples to aggregate

Yes

Save response

should the sampler store the response. If not, only the response length is returned.

Yes

Timeout

 Specify the timeout to be applied, in milliseconds. 0=none. This is the overall aggregate timeout, not per sample. 

Yes

Client

 Which client implementation to use. Both of them create connections which can read messages. However they use a different strategy, as described below: MessageConsumer.receive() calls receive() for every requested message. Retains the connection between samples, but does not fetch messages unless the sampler is active. This is best suited to Queue subscriptions. MessageListener.onMessage()establishes a Listener that stores all incoming messages on a queue. The listener remains active after the sampler completes. This is best suited to Topic subscriptions.

Yes

Stop between samples?

 If selected, then JMeter calls Connection.stop() at the end of each sample (and calls start() before each sample). This may be useful in some cases where multiple samples/threads have connections to the same queue. If not selected, JMeter calls Connection.start() at the start of the thread, and does not call stop() until the end of the thread. 

Yes

Separator

 Separator used to separate messages when there is more than one (related to setting Number of samples to aggregate). Note that \n, \r, \t are accepted. 

No

Reconnect on error codes (regex)

Regular expression for JMSException error codes which force reconnection. If empty no reconnection will be done

No

Pause between errors (ms)

Pause in milliseconds that Subscriber will make when an error occurs

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

JMS Point-to-Point[¶](https://jmeter.apache.org/usermanual/component_reference.html#JMS_Point-to-Point "Link to here")
----------------------------------------------------------------------------------------------------------------------

This sampler sends and optionally receives JMS Messages through point-to-point connections (queues). It is different from pub/sub messages and is generally used for handling transactions.

request_only will typically be used to put load on a JMS System. 

request_reply will be used when you want to test response time of a JMS service that processes messages sent to the Request Queue as this mode will wait for the response on the Reply queue sent by this service. 

browse returns the current queue depth, i.e. the number of messages on the queue. 

read reads a message from the queue (if any). 

clear clears the queue, i.e. remove all messages from the queue.

JMeter use the properties java.naming.security.[principal|credentials] - if present - when creating the Queue Connection. If this behaviour is not desired, set the JMeter property JMSSampler.useSecurity.properties=false

JMeter does not include any JMS implementation jar; this must be downloaded from the JMS provider and put in the lib directory

[![Image 22: Screenshot for Control-Panel of JMS Point-to-Point](https://jmeter.apache.org/images/screenshots/jms/JMS_Point-to-Point.png)](https://jmeter.apache.org/images/screenshots/jms/JMS_Point-to-Point.png)

Screenshot of Control-Panel of JMS Point-to-Point

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#JMS_Point-to-Point_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

QueueConnection Factory

 The JNDI name of the queue connection factory to use for connecting to the messaging system. 

Yes

JNDI Name Request queue

 This is the JNDI name of the queue to which the messages are sent. 

Yes

JNDI Name Reply queue

 The JNDI name of the receiving queue. If a value is provided here and the communication style is Request Response this queue will be monitored for responses to the requests sent. 

No

Number of samples to aggregate

Number of samples to aggregate. Only applicable for Communication style Read.

Yes

JMS Selector

 Message Selector as defined by JMS specification to extract only messages that respect the Selector condition. Syntax uses subpart of SQL 92. 

No

Communication style

 The Communication style can be Request Only (also known as Fire and Forget), Request Response, Read, Browse, Clear: Request Only will only send messages and will not monitor replies. As such it can be used to put load on a system.Request Response will send messages and monitor the replies it receives. Behaviour depends on the value of the JNDI Name Reply Queue. If JNDI Name Reply Queue has a value, this queue is used to monitor the results. Matching of request and reply is done with the message id of the request and the correlation id of the reply. If the JNDI Name Reply Queue is empty, then temporary queues will be used for the communication between the requestor and the server. This is very different from the fixed reply queue. With temporary queues the sending thread will block until the reply message has been received. With Request Response mode, you need to have a Server that listens to messages sent to Request Queue and sends replies to queue referenced by message.getJMSReplyTo(). Read will read a message from an outgoing queue which has no listeners attached. This can be convenient for testing purposes. This method can be used if you need to handle queues without a binding file (in case the jmeter-jms-skip-jndi library is used), which only works with the JMS Point-to-Point sampler. In case binding files are used, one can also use the JMS Subscriber Sampler for reading from a queue.Browse will determine the current queue depth without removing messages from the queue, returning the number of messages on the queue.Clear will clear the queue, i.e. remove all messages from the queue.

Yes

Use alternate fields for message correlation

 These check-boxes select the fields which will be used for matching the response message with the original request. Use Request Message Id if selected, the request JMSMessageID will be used, otherwise the request JMSCorrelationID will be used. In the latter case the correlation id must be specified in the request.Use Response Message Id if selected, the response JMSMessageID will be used, otherwise the response JMSCorrelationID will be used.  There are two frequently used JMS Correlation patterns: JMS Correlation ID Pattern i.e. match request and response on their correlation Ids => deselect both checkboxes, and provide a correlation id.JMS Message ID Pattern i.e. match request message id with response correlation id => select "Use Request Message Id" only.  In both cases the JMS application is responsible for populating the correlation ID as necessary. 

if the same queue is used to send and receive messages, then the response message will be the same as the request message. In which case, either provide a correlation id and clear both checkboxes; or select both checkboxes to use the message Id for correlation. This can be useful for checking raw JMS throughput.

Yes

Timeout

 The timeout in milliseconds for the reply-messages. If a reply has not been received within the specified time, the specific testcase fails and the specific reply message received after the timeout is discarded. Default value is 2000 ms. 0 means no timeout. 

Yes

Expiration

 The expiration time (in milliseconds) of the message before it becomes obsolete. If you do not specify an expiration time, the default value is 0 (never expires). 

No

Priority

 The priority level of the message. There are ten priority levels from 0 (lowest) to 9 (highest). If you do not specify a priority level, the default level is 4. 

No

Use non-persistent delivery mode?

 Whether to set DeliveryMode.NON_PERSISTENT. 

Yes

Content

 The content of the message. 

No

JMS Properties

 The JMS Properties are properties specific for the underlying messaging system. You can setup the name, the value and the class (type) of value. Default type is String. For example: for WebSphere 5.1 web services you will need to set the JMS Property targetService to test webservices through JMS. 

No

Initial Context Factory

 The Initial Context Factory is the factory to be used to look up the JMS Resources. 

No

JNDI properties

 The JNDI Properties are the specific properties for the underlying JNDI implementation. 

No

Provider URL

 The URL for the JMS provider. 

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

JUnit Request[¶](https://jmeter.apache.org/usermanual/component_reference.html#JUnit_Request "Link to here")
------------------------------------------------------------------------------------------------------------

 The current implementation supports standard JUnit convention and extensions. It also includes extensions like oneTimeSetUp and oneTimeTearDown. The sampler works like the [Java Request](https://jmeter.apache.org/usermanual/component_reference.html#Java_Request) with some differences. 
*    rather than use JMeter's test interface, it scans the jar files for classes extending JUnit's TestCase class. That includes any class or subclass. 
*    JUnit test jar files should be placed in jmeter/lib/junit instead of /lib directory. You can also use the "user.classpath" property to specify where to look for TestCase classes. 
*    JUnit sampler does not use name/value pairs for configuration like the [Java Request](https://jmeter.apache.org/usermanual/component_reference.html#Java_Request). The sampler assumes setUp and tearDown will configure the test correctly. 
*    The sampler measures the elapsed time only for the test method and does not include setUp and tearDown. 
*   Each time the test method is called, JMeter will pass the result to the listeners.
*    Support for oneTimeSetUp and oneTimeTearDown is done as a method. Since JMeter is multi-threaded, we cannot call oneTimeSetUp/oneTimeTearDown the same way Maven does it. 
*    The sampler reports unexpected exceptions as errors. There are some important differences between standard JUnit test runners and JMeter's implementation. Rather than make a new instance of the class for each test, JMeter creates 1 instance per sampler and reuses it. This can be changed with checkbox "Create a new instance per sample". 

 The current implementation of the sampler will try to create an instance using the string constructor first. If the test class does not declare a string constructor, the sampler will look for an empty constructor. Example below: 

 JUnit Constructors[¶](https://jmeter.apache.org/usermanual/component_reference.html#junit_constructor_example "Link to here")

 Empty Constructor: 
public class myTestCase {
  public myTestCase() {}
}
 String Constructor: 
public class myTestCase {
  public myTestCase(String text) {
    super(text);
  }
}

 By default, JMeter will provide some default values for the success/failure code and message. Users should define a set of unique success and failure codes and use them uniformly across all tests. 

### General Guidelines

 If you use setUp and tearDown, make sure the methods are declared public. If you do not, the test may not run properly. 

 Here are some general guidelines for writing JUnit tests so they work well with JMeter. Since JMeter runs multi-threaded, it is important to keep certain things in mind. 
*    Write the setUp and tearDown methods so they are thread safe. This generally means avoid using static members. 
*   Make the test methods discrete units of work and not long sequences of actions. By keeping the test method to a discrete operation, it makes it easier to combine test methods to create new test plans.
*   Avoid making test methods depend on each other. Since JMeter allows arbitrary sequencing of test methods, the runtime behavior is different than the default JUnit behavior.
*   If a test method is configurable, be careful about where the properties are stored. Reading the properties from the Jar file is recommended.
*    Each sampler creates an instance of the test class, so write your test so the setup happens in oneTimeSetUp and oneTimeTearDown. 

[![Image 23: Screenshot for Control-Panel of JUnit Request](https://jmeter.apache.org/images/screenshots/junit_sampler.png)](https://jmeter.apache.org/images/screenshots/junit_sampler.png)

Screenshot of Control-Panel of JUnit Request

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#JUnit_Request_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Search for JUnit4 annotations

 Select this to search for JUnit4 tests (@Test annotations) 

Yes

Package filter

 Comma separated list of packages to show. Example, org.apache.jmeter,junit.framework. 

Class name

Fully qualified name of the JUnit test class.

Yes

Constructor string

String pass to the string constructor. If a string is set, the sampler will use the string constructor instead of the empty constructor.

Test method

The method to test.

Yes

Success message

A descriptive message indicating what success means.

Success code

An unique code indicating the test was successful.

Failure message

A descriptive message indicating what failure means.

Failure code

An unique code indicating the test failed.

Error message

A description for errors.

Error code

Some code for errors. Does not need to be unique.

Do not call setUp and tearDown

 Set the sampler not to call setUp and tearDown. By default, setUp and tearDown should be called. Not calling those methods could affect the test and make it inaccurate. This option should only be used with calling oneTimeSetUp and oneTimeTearDown. If the selected method is oneTimeSetUp or oneTimeTearDown, this option should be checked. 

Yes

Append assertion errors

Whether or not to append assertion errors to the response message.

Yes

Append runtime exceptions

 Whether or not to append runtime exceptions to the response message. Only applies if "Append assertion errors" is not selected. 

Yes

Create a new Instance per sample

 Whether or not to create a new JUnit instance for each sample. Defaults to false, meaning JUnit TestCase is created one and reused. 

Yes

The following JUnit4 annotations are recognised:

@Test used to find test methods and classes. The "expected" and "timeout" attributes are supported. @Before treated the same as setUp() in JUnit3 @After treated the same as tearDown() in JUnit3 @BeforeClass, @AfterClass treated as test methods so they can be run independently as required

 Note that JMeter currently runs the test methods directly, rather than leaving it to JUnit. This is to allow the setUp/tearDown methods to be excluded from the sample time. As a consequence, the sampler time excludes the time taken to call setUp/tearDown methods and their annotation based alternatives. 

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Mail Reader Sampler[¶](https://jmeter.apache.org/usermanual/component_reference.html#Mail_Reader_Sampler "Link to here")
------------------------------------------------------------------------------------------------------------------------

The Mail Reader Sampler can read (and optionally delete) mail messages using POP3(S) or IMAP(S) protocols.

[![Image 24: Screenshot for Control-Panel of Mail Reader Sampler](https://jmeter.apache.org/images/screenshots/mailreader_sampler.png)](https://jmeter.apache.org/images/screenshots/mailreader_sampler.png)

Screenshot of Control-Panel of Mail Reader Sampler

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Mail_Reader_Sampler_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Server Type

 The protocol used by the provider: e.g. pop3, pop3s, imap, imaps. or another string representing the server protocol. For example file for use with the read-only mail file provider. The actual provider names for POP3 and IMAP are pop3 and imap

Yes

Server

 Hostname or IP address of the server. See below for use with file protocol. 

Yes

Port

Port to be used to connect to the server (optional)

No

Username

User login name

Password

User login password (N.B. this is stored unencrypted in the test plan)

Folder

 The IMAP(S) folder to use. See below for use with file protocol. 

Yes, if using IMAP(S)

Number of messages to retrieve

Set this to retrieve all or some messages

Yes

Fetch headers only

If selected, only the message headers will be retrieved.

Yes

Delete messages from the server

If set, messages will be deleted after retrieval

Yes

Store the message using MIME

 Whether to store the message as MIME. If so, then the entire raw message is stored in the Response Data; the headers are not stored as they are available in the data. If not, the message headers are stored as Response Headers. A few headers are stored (Date, To, From, Subject) in the body. 

Yes

Use no security features

Indicates that the connection to the server does not use any security protocol.

Use SSL

Indicates that the connection to the server must use the SSL protocol.

Use StartTLS

Indicates that the connection to the server should attempt to start the TLS protocol.

Enforce StartTLS

If the server does not start the TLS protocol the connection will be terminated.

Trust All Certificates

When selected it will accept all certificates independent of the CA.

Use local truststore

When selected it will only accept certificates that are locally trusted.

Local truststore

 Path to file containing the trusted certificates. Relative paths are resolved against the current directory. 

 Failing that, against the directory containing the test script (JMX file). 

 You can pass mail related environment properties by adding to user.properties any of the properties described [here](https://javaee.github.io/javamail/docs/api/com/sun/mail/pop3/package-summary.html). 

Messages are stored as subsamples of the main sampler. Multipart message parts are stored as subsamples of the message.

**Special handling for "file" protocol:**

 The file JavaMail provider can be used to read raw messages from files. The server field is used to specify the path to the parent of the folder. Individual message files should be stored with the name n.msg, where n is the message number. Alternatively, the server field can be the name of a file which contains a single message. The current implementation is quite basic, and is mainly intended for debugging purposes.

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Flow Control Action[(was: Test Action )](https://jmeter.apache.org/usermanual/component_reference.html)[¶](https://jmeter.apache.org/usermanual/component_reference.html#Flow_Control_Action "Link to here")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 The Flow Control Action sampler is a sampler that is intended for use in a conditional controller. Rather than generate a sample, the test element either pauses or stops the selected target. 
This sampler can also be useful in conjunction with the Transaction Controller, as it allows pauses to be included without needing to generate a sample. For variable delays, set the pause time to zero, and add a Timer as a child.

The "Stop" action stops the thread or test after completing any samples that are in progress. The "Stop Now" action stops the test without waiting for samples to complete; it will interrupt any active samples. If some threads fail to stop within the 5 second time-limit, a message will be displayed in GUI mode. You can try using the Stop command to see if this will stop the threads, but if not, you should exit JMeter. In CLI mode, JMeter will exit if some threads fail to stop within the 5 second time limit.

 The time to wait can be changed using the JMeter property jmeterengine.threadstop.wait. The time is given in milliseconds. 

[![Image 25: Screenshot for Control-Panel of Flow Control Action](https://jmeter.apache.org/images/screenshots/test_action.png)](https://jmeter.apache.org/images/screenshots/test_action.png)

Screenshot of Control-Panel of Flow Control Action

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Flow_Control_Action_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Target

Current Thread / All Threads (ignored for Pause and Go to next loop iteration) 

Yes

Action

Pause / Stop / Stop Now / Go to next loop iteration

Yes

Duration

How long to pause for (milliseconds)

Yes, if Pause is selected

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

SMTP Sampler[¶](https://jmeter.apache.org/usermanual/component_reference.html#SMTP_Sampler "Link to here")
----------------------------------------------------------------------------------------------------------

The SMTP Sampler can send mail messages using SMTP/SMTPS protocol. It is possible to set security protocols for the connection (SSL and TLS), as well as user authentication. If a security protocol is used a verification on the server certificate will occur. 

 Two alternatives to handle this verification are available:

Trust all certificates This will ignore certificate chain verification Use a local truststore With this option the certificate chain will be validated against the local truststore file.

[![Image 26: Screenshot for Control-Panel of SMTP Sampler](https://jmeter.apache.org/images/screenshots/smtp_sampler.png)](https://jmeter.apache.org/images/screenshots/smtp_sampler.png)

Screenshot of Control-Panel of SMTP Sampler

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#SMTP_Sampler_parms1 "Link to here")

Attribute

Description

Required

Server

 Hostname or IP address of the server. See below for use with file protocol. 

Yes

Port

Port to be used to connect to the server. Defaults are: SMTP=25, SSL=465, StartTLS=587 

No

Connection timeout

Connection timeout value in milliseconds (socket level). Default is infinite timeout.

No

Read timeout

Read timeout value in milliseconds (socket level). Default is infinite timeout.

No

Address From

The from address that will appear in the e-mail

Yes

Address To

 The destination e-mail address (multiple values separated by ";") 

Yes, unless CC or BCC is specified

Address To CC

 Carbon copy destinations e-mail address (multiple values separated by ";") 

No

Address To BCC

 Blind carbon copy destinations e-mail address (multiple values separated by ";") 

No

Address Reply-To

 Alternate Reply-To address (multiple values separated by ";") 

No

Use Auth

Indicates if the SMTP server requires user authentication

Username

User login name

Password

User login password (N.B. this is stored unencrypted in the test plan)

Use no security features

Indicates that the connection to the SMTP server does not use any security protocol.

Use SSL

Indicates that the connection to the SMTP server must use the SSL protocol.

Use StartTLS

Indicates that the connection to the SMTP server should attempt to start the TLS protocol.

Enforce StartTLS

If the server does not start the TLS protocol the connection will be terminated.

Trust All Certificates

When selected it will accept all certificates independent of the CA.

Use local truststore

When selected it will only accept certificates that are locally trusted.

Local truststore

 Path to file containing the trusted certificates. Relative paths are resolved against the current directory. 

 Failing that, against the directory containing the test script (JMX file). 

Override System SSL/TLS Protocols

 Specify a custom SSL/TLS protocol as space separated list to use on handshake example TLSv1 TLSv1.1 TLSv1.2. Defaults to all supported protocols. 

No

Subject

The e-mail message subject.

Suppress Subject Header

 If selected, the "Subject:" header is omitted from the mail that is sent. This is different from sending an empty "Subject:" header, though some e-mail clients may display it identically. 

Include timestamp in subject

 Includes the System.currentTimemillis() in the subject line. 

Add Header

Additional headers can be defined using this button.

No

Message

The message body.

Send plain body (i.e. not multipart/mixed)

 If selected, then send the body as a plain message, i.e. not multipart/mixed, if possible. If the message body is empty and there is a single file, then send the file contents as the message body. 

 Note: If the message body is not empty, and there is at least one attached file, then the body is sent as multipart/mixed. 

 No 

Attach files

Files to be attached to the message.

Send .eml

 If set, the .eml file will be sent instead of the entries in the Subject, Message, and Attach file(s) fields 

Calculate message size

Calculates the message size and stores it in the sample result.

Enable debug logging?

 If set, then the "mail.debug" property is set to "true" 

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

OS Process Sampler[¶](https://jmeter.apache.org/usermanual/component_reference.html#OS_Process_Sampler "Link to here")
----------------------------------------------------------------------------------------------------------------------

The OS Process Sampler is a sampler that can be used to execute commands on the local machine. 

 It should allow execution of any command that can be run from the command line. 

 Validation of the return code can be enabled, and the expected return code can be specified.

Note that OS shells generally provide command-line parsing. This varies between OSes, but generally the shell will split parameters on white-space. Some shells expand wild-card file names; some don't. The quoting mechanism also varies between OSes. The sampler deliberately does not do any parsing or quote handling. The command and its parameters must be provided in the form expected by the executable. This means that the sampler settings will not be portable between OSes.

Many OSes have some built-in commands which are not provided as separate executables. For example the Windows DIR command is part of the command interpreter (CMD.EXE). These built-ins cannot be run as independent programs, but have to be provided as arguments to the appropriate command interpreter.

For example, the Windows command-line: DIR C:\TEMP needs to be specified as follows:

Command:CMD Param 1:/C Param 2:DIR Param 3:C:\TEMP

[![Image 27: Screenshot for Control-Panel of OS Process Sampler](https://jmeter.apache.org/images/screenshots/os_process_sampler.png)](https://jmeter.apache.org/images/screenshots/os_process_sampler.png)

Screenshot of Control-Panel of OS Process Sampler

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#OS_Process_Sampler_parms1 "Link to here")

Attribute

Description

Required

Command

The program name to execute.

Yes

Working directory

 Directory from which command will be executed, defaults to folder referenced by "user.dir" System property 

No

Command Parameters

Parameters passed to the program name.

No

Environment Parameters

Key/Value pairs added to environment when running command.

No

Standard input (stdin)

 Name of file from which input is to be taken (STDIN). 

No

Standard output (stdout

 Name of output file for standard output (STDOUT). If omitted, output is captured and returned as the response data. 

No

Standard error (stderr)

 Name of output file for standard error (STDERR). If omitted, output is captured and returned as the response data. 

No

Check Return Code

 If checked, sampler will compare return code with Expected Return Code. 

No

Expected Return Code

 Expected return code for System Call, required if "Check Return Code" is checked. Note 500 is used as an error indicator in JMeter so you should not use it. 

No

Timeout

 Timeout for command in milliseconds, defaults to 0, which means _no_ timeout. If the timeout expires before the command finishes, JMeter will attempt to kill the OS process. 

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

MongoDB Script (DEPRECATED)[¶](https://jmeter.apache.org/usermanual/component_reference.html#MongoDB_Script_(DEPRECATED) "Link to here")
----------------------------------------------------------------------------------------------------------------------------------------

This sampler lets you send a Request to a MongoDB.

Before using this you need to set up a [MongoDB Source Config](https://jmeter.apache.org/usermanual/component_reference.html#MongoDB_Source_Config) Configuration element

 This Element currently uses com.mongodb.DB#eval which takes a global write lock causing a performance impact on the database, see [db.eval()](http://docs.mongodb.org/manual/reference/method/db.eval/). So it is better to avoid using this element for load testing and use JSR223+Groovy scripting using [MongoDBHolder](https://jmeter.apache.org/api/org/apache/jmeter/protocol/mongodb/config/MongoDBHolder.html) instead. MongoDB Script is more suitable for functional testing or test setup (setup/teardown threads) 

[![Image 28: Screenshot for Control-Panel of MongoDB Script (DEPRECATED)](https://jmeter.apache.org/images/screenshots/mongodb-script.png)](https://jmeter.apache.org/images/screenshots/mongodb-script.png)

Screenshot of Control-Panel of MongoDB Script (DEPRECATED)

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#MongoDB_Script_(DEPRECATED)_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

MongoDB Source

 Name of the JMeter variable that the MongoDB connection is bound to. This must agree with the 'MongoDB Source' field of a MongoDB Source Config. 

Yes

Database Name

Database Name, will be used in your script 

Yes

Username

No

Password

No

Script

 Mongo script as it would be used in MongoDB shell 

Yes

See also:

*   [MongoDB Source Config](https://jmeter.apache.org/usermanual/component_reference.html#MongoDB_Source_Config)

Ensure Variable Name is unique across Test Plan.

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Bolt Request[¶](https://jmeter.apache.org/usermanual/component_reference.html#Bolt_Request "Link to here")
----------------------------------------------------------------------------------------------------------

This sampler allows you to run Cypher queries through the Bolt protocol.

Before using this you need to set up a [Bolt Connection Configuration](https://jmeter.apache.org/usermanual/component_reference.html#Bolt_Connection_Configuration)

Every request uses a connection acquired from the pool and returns it to the pool when the sampler completes. The connection pool size defaults to 100 and is configurable.

The measured response time corresponds to the "full" query execution, including both the time to execute the cypher query AND the time to consume the results sent back by the database.

[![Image 29: Screenshot for Control-Panel of Bolt Request](https://jmeter.apache.org/images/screenshots/bolt-request.png)](https://jmeter.apache.org/images/screenshots/bolt-request.png)

Screenshot of Control-Panel of Bolt Request

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Bolt_Request_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Comments

Free text for additional details.

No

Cypher statement

 The query to execute. 

Yes

Params

The parameter values, JSON formatted.

No

Record Query Results

 Whether to add or not query result data to the sampler response (default false). Note that activating this has a memory overhead, use it wisely. 

No

Access Mode

Whether to access the database in WRITE or READ mode. Use WRITE for a standalone Neo4j instance. For a Neo4j cluster, select mode depending on whether the query writes to the database. That setting will allow correct routing to the cluster leader, followers or read replicas.

Yes

Database

The database to run the query against. Required for Neo4j 4.0+, unless querying the default database. Must be undefined for Neo4j 3.5.

No

Transaction timeout

Timeout for the transaction.

No

It is strongly advised to use query parameters, allowing the database to cache and reuse execution plans.

See also:

*   [Bolt Connection Configuration](https://jmeter.apache.org/usermanual/component_reference.html#Bolt_Connection_Configuration)

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

18.2 Logic Controllers[¶](https://jmeter.apache.org/usermanual/component_reference.html#logic_controllers "Link to here")
=========================================================================================================================

Logic Controllers determine the order in which Samplers are processed.

Simple Controller[¶](https://jmeter.apache.org/usermanual/component_reference.html#Simple_Controller "Link to here")
--------------------------------------------------------------------------------------------------------------------

The Simple Logic Controller lets you organize your Samplers and other Logic Controllers. Unlike other Logic Controllers, this controller provides no functionality beyond that of a storage device.

[![Image 30: Screenshot for Control-Panel of Simple Controller](https://jmeter.apache.org/images/screenshots/logic-controller/simple-controller.png)](https://jmeter.apache.org/images/screenshots/logic-controller/simple-controller.png)

Screenshot of Control-Panel of Simple Controller

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Simple_Controller_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree.

No

 Using the Simple Controller[¶](https://jmeter.apache.org/usermanual/component_reference.html#simple_controller_example "Link to here")

[Download](https://jmeter.apache.org/demos/SimpleTestPlan.jmx) this example (see Figure 6). In this example, we created a Test Plan that sends two Ant HTTP requests and two Log4J HTTP requests. We grouped the Ant and Log4J requests by placing them inside Simple Logic Controllers. Remember, the Simple Logic Controller has no effect on how JMeter processes the controller(s) you add to it. So, in this example, JMeter sends the requests in the following order: Ant Home Page, Ant News Page, Log4J Home Page, Log4J History Page.

Note, the File Reporter is configured to store the results in a file named "simple-test.dat" in the current directory.

[![Image 31: Figure 6 Simple Controller Example](https://jmeter.apache.org/images/screenshots/logic-controller/simple-example.png)](https://jmeter.apache.org/images/screenshots/logic-controller/simple-example.png)

Figure 6 Simple Controller Example

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Loop Controller[¶](https://jmeter.apache.org/usermanual/component_reference.html#Loop_Controller "Link to here")
----------------------------------------------------------------------------------------------------------------

If you add Generative or Logic Controllers to a Loop Controller, JMeter will loop through them a certain number of times, in addition to the loop value you specified for the Thread Group. For example, if you add one HTTP Request to a Loop Controller with a loop count of two, and configure the Thread Group loop count to three, JMeter will send a total of 2 * 3 = 6 HTTP Requests.

 JMeter will expose the looping index as a variable named  __jm__ <Name of your element>__idx. So for example, if your Loop Controller is named LC, then you can access the looping index through ${__jm__LC__idx}. Index starts at 0 

[![Image 32: Screenshot for Control-Panel of Loop Controller](https://jmeter.apache.org/images/screenshots/logic-controller/loop-controller.png)](https://jmeter.apache.org/images/screenshots/logic-controller/loop-controller.png)

Screenshot of Control-Panel of Loop Controller

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Loop_Controller_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree.

No

Loop Count

 The number of times the subelements of this controller will be iterated each time through a test run. 
The value -1 is equivalent to checking the Forever toggle.

**Special Case:** The Loop Controller embedded in the [Thread Group](https://jmeter.apache.org/usermanual/test_plan.html#thread_group) element behaves slightly different. Unless set to forever, it stops the test after the given number of iterations have been done.

 When using a function in this field, be aware it may be evaluated multiple times. Example using [__Random](https://jmeter.apache.org/usermanual/functions.html#__Random) will evaluate it to a different value for each child samplers of Loop Controller and result into unwanted behaviour. 

Yes, unless "Forever" is checked

 Looping Example[¶](https://jmeter.apache.org/usermanual/component_reference.html#loop_example "Link to here")

[Download](https://jmeter.apache.org/demos/LoopTestPlan.jmx) this example (see Figure 4). In this example, we created a Test Plan that sends a particular HTTP Request only once and sends another HTTP Request five times.

[![Image 33: Figure 4 - Loop Controller Example](https://jmeter.apache.org/images/screenshots/logic-controller/loop-example.png)](https://jmeter.apache.org/images/screenshots/logic-controller/loop-example.png)

Figure 4 - Loop Controller Example

We configured the Thread Group for a single thread and a loop count value of one. Instead of letting the Thread Group control the looping, we used a Loop Controller. You can see that we added one HTTP Request to the Thread Group and another HTTP Request to a Loop Controller. We configured the Loop Controller with a loop count value of five.

JMeter will send the requests in the following order: Home Page, News Page, News Page, News Page, News Page, and News Page.

 Note, the File Reporter is configured to store the results in a file named "loop-test.dat" in the current directory. 

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Once Only Controller[¶](https://jmeter.apache.org/usermanual/component_reference.html#Once_Only_Controller "Link to here")
--------------------------------------------------------------------------------------------------------------------------

The Once Only Logic Controller tells JMeter to process the controller(s) inside it only once per Thread, and pass over any requests under it during further iterations through the test plan.

The Once Only Controller will now execute always during the first iteration of any looping parent controller. Thus, if the Once Only Controller is placed under a Loop Controller specified to loop 5 times, then the Once Only Controller will execute only on the first iteration through the Loop Controller (i.e. every 5 times).

Note this means the Once Only Controller will still behave as previously expected if put under a Thread Group (runs only once per test per Thread), but now the user has more flexibility in the use of the Once Only Controller.

For testing that requires a login, consider placing the login request in this controller since each thread only needs to login once to establish a session.

[![Image 34: Screenshot for Control-Panel of Once Only Controller](https://jmeter.apache.org/images/screenshots/logic-controller/once-only-controller.png)](https://jmeter.apache.org/images/screenshots/logic-controller/once-only-controller.png)

Screenshot of Control-Panel of Once Only Controller

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Once_Only_Controller_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree.

No

 Once Only Example[¶](https://jmeter.apache.org/usermanual/component_reference.html#once_only_example "Link to here")

[Download](https://jmeter.apache.org/demos/OnceOnlyTestPlan.jmx) this example (see Figure 5). In this example, we created a Test Plan that has two threads that send HTTP request. Each thread sends one request to the Home Page, followed by three requests to the Bug Page. Although we configured the Thread Group to iterate three times, each JMeter thread only sends one request to the Home Page because this request lives inside a Once Only Controller.

[![Image 35: Figure 5. Once Only Controller Example](https://jmeter.apache.org/images/screenshots/logic-controller/once-only-example.png)](https://jmeter.apache.org/images/screenshots/logic-controller/once-only-example.png)

Figure 5. Once Only Controller Example

Each JMeter thread will send the requests in the following order: Home Page, Bug Page, Bug Page, Bug Page.

Note, the File Reporter is configured to store the results in a file named "loop-test.dat" in the current directory.

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Interleave Controller[¶](https://jmeter.apache.org/usermanual/component_reference.html#Interleave_Controller "Link to here")
----------------------------------------------------------------------------------------------------------------------------

If you add Generative or Logic Controllers to an Interleave Controller, JMeter will alternate among each of the other controllers for each loop iteration.

[![Image 36: Screenshot for Control-Panel of Interleave Controller](https://jmeter.apache.org/images/screenshots/logic-controller/interleave-controller.png)](https://jmeter.apache.org/images/screenshots/logic-controller/interleave-controller.png)

Screenshot of Control-Panel of Interleave Controller

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Interleave_Controller_parms1 "Link to here")

Attribute

Description

Required

name

Descriptive name for this controller that is shown in the tree.

No

ignore sub-controller blocks

If checked, the interleave controller will treat sub-controllers like single request elements and only allow one request per controller at a time. 

No

Interleave across threads

If checked, the interleave controller will alternate among each of its children controllers for each loop iteration but across all threads, for example in a configuration with 4 threads and 3 child controllers, on first iteration thread 1 will run first child, thread 2 second child, thread 3 third child, thread 4 first child, on next iteration each thread will run the following child controller

No

 Simple Interleave Example[¶](https://jmeter.apache.org/usermanual/component_reference.html#simple_interleave_example "Link to here")

[Download](https://jmeter.apache.org/demos/InterleaveTestPlan.jmx) this example (see Figure 1). In this example, we configured the Thread Group to have two threads and a loop count of five, for a total of ten requests per thread. See the table below for the sequence JMeter sends the HTTP Requests.

[![Image 37: Figure 1 - Interleave Controller Example 1](https://jmeter.apache.org/images/screenshots/logic-controller/interleave.png)](https://jmeter.apache.org/images/screenshots/logic-controller/interleave.png)

Figure 1 - Interleave Controller Example 1

| Loop Iteration | Each JMeter Thread Sends These HTTP Requests |
| --- | --- |
| 1 | News Page |
| 1 | Log Page |
| 2 | FAQ Page |
| 2 | Log Page |
| 3 | Gump Page |
| 3 | Log Page |
| 4 | Because there are no more requests in the controller, JMeter starts over and sends the first HTTP Request, which is the News Page. |
| 4 | Log Page |
| 5 | FAQ Page |
| 5 | Log Page |

 Useful Interleave Example[¶](https://jmeter.apache.org/usermanual/component_reference.html#useful_interleave_example "Link to here")

[Download](https://jmeter.apache.org/demos/InterleaveTestPlan2.jmx) another example (see Figure 2). In this example, we configured the Thread Group to have a single thread and a loop count of eight. Notice that the Test Plan has an outer Interleave Controller with two Interleave Controllers inside of it.

[![Image 38: Figure 2 - Interleave Controller Example 2 ](https://jmeter.apache.org/images/screenshots/logic-controller/interleave2.png)](https://jmeter.apache.org/images/screenshots/logic-controller/interleave2.png)

 Figure 2 - Interleave Controller Example 2 

The outer Interleave Controller alternates between the two inner ones. Then, each inner Interleave Controller alternates between each of the HTTP Requests. Each JMeter thread will send the requests in the following order: Home Page, Interleaved, Bug Page, Interleaved, CVS Page, Interleaved, and FAQ Page, Interleaved.

Note, the File Reporter is configured to store the results in a file named "interleave-test2.dat" in the current directory.

[![Image 39: Figure 3 - Interleave Controller Example 3 ](https://jmeter.apache.org/images/screenshots/logic-controller/interleave3.png)](https://jmeter.apache.org/images/screenshots/logic-controller/interleave3.png)

 Figure 3 - Interleave Controller Example 3 

If the two interleave controllers under the main interleave controller were instead simple controllers, then the order would be: Home Page, CVS Page, Interleaved, Bug Page, FAQ Page, Interleaved.

However, if "ignore sub-controller blocks" was checked on the main interleave controller, then the order would be: Home Page, Interleaved, Bug Page, Interleaved, CVS Page, Interleaved, and FAQ Page, Interleaved.

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Random Controller[¶](https://jmeter.apache.org/usermanual/component_reference.html#Random_Controller "Link to here")
--------------------------------------------------------------------------------------------------------------------

The Random Logic Controller acts similarly to the Interleave Controller, except that instead of going in order through its sub-controllers and samplers, it picks one at random at each pass.

Interactions between multiple controllers can yield complex behavior. This is particularly true of the Random Controller. Experiment before you assume what results any given interaction will give

[![Image 40: Screenshot for Control-Panel of Random Controller](https://jmeter.apache.org/images/screenshots/logic-controller/random-controller.png)](https://jmeter.apache.org/images/screenshots/logic-controller/random-controller.png)

Screenshot of Control-Panel of Random Controller

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Random_Controller_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree.

No

ignore sub-controller blocks

If checked, the interleave controller will treat sub-controllers like single request elements and only allow one request per controller at a time. 

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Random Order Controller[¶](https://jmeter.apache.org/usermanual/component_reference.html#Random_Order_Controller "Link to here")
--------------------------------------------------------------------------------------------------------------------------------

The Random Order Controller is much like a Simple Controller in that it will execute each child element at most once, but the order of execution of the nodes will be random.

[![Image 41: Screenshot for Control-Panel of Random Order Controller](https://jmeter.apache.org/images/screenshots/randomordercontroller.png)](https://jmeter.apache.org/images/screenshots/randomordercontroller.png)

Screenshot of Control-Panel of Random Order Controller

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Random_Order_Controller_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree.

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Throughput Controller[¶](https://jmeter.apache.org/usermanual/component_reference.html#Throughput_Controller "Link to here")
----------------------------------------------------------------------------------------------------------------------------

The Throughput Controller allows the user to control how often it is executed. There are two modes:

*   percent execution
*   total executions

Percent executions causes the controller to execute a certain percentage of the iterations through the test plan.Total executions causes the controller to stop executing after a certain number of executions have occurred. Like the Once Only Controller, this setting is reset when a parent Loop Controller restarts. 

 This controller is badly named, as it does not control throughput. Please refer to the [Constant Throughput Timer](https://jmeter.apache.org/usermanual/component_reference.html#Constant_Throughput_Timer) for an element that can be used to adjust the throughput. 

[![Image 42: Screenshot for Control-Panel of Throughput Controller](https://jmeter.apache.org/images/screenshots/throughput_controller.png)](https://jmeter.apache.org/images/screenshots/throughput_controller.png)

Screenshot of Control-Panel of Throughput Controller

The Throughput Controller can yield very complex behavior when combined with other controllers - in particular with interleave or random controllers as parents (also very useful).

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Throughput_Controller_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree.

No

Execution Style

Whether the controller will run in percent executions or total executions mode.

Yes

Throughput

 A number. For percent execution mode, a number from 0-100 that indicates the percentage of times the controller will execute. "50" means the controller will execute during half the iterations through the test plan. For total execution mode, the number indicates the total number of times the controller will execute. 

Yes

Per User

 If checked, per user will cause the controller to calculate whether it should execute on a per user (per thread) basis. If unchecked, then the calculation will be global for all users. For example, if using total execution mode, and uncheck "per user", then the number given for throughput will be the total number of executions made. If "per user" is checked, then the total number of executions would be the number of users times the number given for throughput. 

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Runtime Controller[¶](https://jmeter.apache.org/usermanual/component_reference.html#Runtime_Controller "Link to here")
----------------------------------------------------------------------------------------------------------------------

The Runtime Controller controls how long its children will run. Controller will run its children until configured Runtime(s) is exceeded.

[![Image 43: Screenshot for Control-Panel of Runtime Controller](https://jmeter.apache.org/images/screenshots/runtimecontroller.png)](https://jmeter.apache.org/images/screenshots/runtimecontroller.png)

Screenshot of Control-Panel of Runtime Controller

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Runtime_Controller_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree, and used to name the transaction.

Yes

Runtime (seconds)

Desired runtime in seconds. 0 means no run.

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

If Controller[¶](https://jmeter.apache.org/usermanual/component_reference.html#If_Controller "Link to here")
------------------------------------------------------------------------------------------------------------

The If Controller allows the user to control whether the test elements below it (its children) are run or not.

By default, the condition is evaluated only once on initial entry, but you have the option to have it evaluated for every runnable element contained in the controller.

The best option (default one) is to check Interpret Condition as Variable Expression?, then in the condition field you have 2 options:

*    Option 1: Use a variable that contains true or false  If you want to test if last sample was successful, you can use ${JMeterThread.last_sample_ok}[![Image 44: If Controller using Variable](https://jmeter.apache.org/images/screenshots/if_controller_variable.png)](https://jmeter.apache.org/images/screenshots/if_controller_variable.png)

If Controller using Variable  
*    Option 2: Use a function (${__jexl3()} is advised) to evaluate an expression that must return true or false[![Image 45: Screenshot for Control-Panel of If Controller](https://jmeter.apache.org/images/screenshots/if_controller_expression.png)](https://jmeter.apache.org/images/screenshots/if_controller_expression.png)

If Controller using expression

 For example, previously one could use the condition: ${__jexl3(${VAR} == 23)} and this would be evaluated as true/false, the result would then be passed to JavaScript which would then return true/false. If the Variable Expression option is selected, then the expression is evaluated and compared with "true", without needing to use JavaScript. 

 To test if a variable is undefined (or null) do the following, suppose var is named myVar, expression will be: "${myVar}" == "\${myVar}" Or use: "${myVar}" != "\${myVar}" to test if a variable is defined and is not null. 

 If you uncheck Interpret Condition as Variable Expression?, If Controller will internally use javascript to evaluate the condition which has a performance penalty that can be very big and make your test less scalable. [![Image 46: If Controller using javascript](https://jmeter.apache.org/images/screenshots/if_controller_javascript.png)](https://jmeter.apache.org/images/screenshots/if_controller_javascript.png)

If Controller using javascript

[![Image 47: Screenshot for Control-Panel of If Controller](https://jmeter.apache.org/images/screenshots/if_controller_expression.png)](https://jmeter.apache.org/images/screenshots/if_controller_expression.png)

Screenshot of Control-Panel of If Controller

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#If_Controller_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree.

No

Condition (default JavaScript)

 By default the condition is interpreted as **JavaScript** code that returns "true" or "false", but this can be overridden (see below) 

Yes

Interpret Condition as Variable Expression?

 If this is selected, then the condition must be an expression that evaluates to "true" (case is ignored). For example, ${FOUND} or ${__jexl3(${VAR} > 100)}. Unlike the JavaScript case, the condition is only checked to see if it matches "true" (case is ignored). 

 Checking this and using [__jexl3](https://jmeter.apache.org/usermanual/functions.html#__jexl3) or [__groovy](https://jmeter.apache.org/usermanual/functions.html#__groovy) function in Condition is advised for performances 

Yes

Evaluate for all children

 Should condition be evaluated for all children? If not checked, then the condition is only evaluated on entry. 

Yes

 Examples (JavaScript)[¶](https://jmeter.apache.org/usermanual/component_reference.html#example_if_javascript "Link to here")

*   ${COUNT} < 10
*   "${VAR}" == "abcd"

 If there is an error interpreting the code, the condition is assumed to be false, and a message is logged in jmeter.log. 

 Note it is advised to avoid using JavaScript mode for performance. 

 When using [__groovy](https://jmeter.apache.org/usermanual/functions.html#__groovy) take care to not use variable replacement in the string, otherwise if using a variable that changes the script cannot be cached. Instead get the variable using: vars.get("myVar"). See the Groovy examples below. 

 Examples (Variable Expression)[¶](https://jmeter.apache.org/usermanual/component_reference.html#example_if_variable "Link to here")

*   ${__groovy(vars.get("myVar") != "Invalid" )} (Groovy check myVar is not equal to Invalid) 
*   ${__groovy(vars.get("myInt").toInteger() <=4 )} (Groovy check myInt is less then or equal to 4) 
*   ${__groovy(vars.get("myMissing") != null )} (Groovy check if the myMissing variable is not set) 
*   ${__jexl3(${COUNT} < 10)}
*   ${RESULT}
*   ${JMeterThread.last_sample_ok} (check if the last sample succeeded) 

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

While Controller[¶](https://jmeter.apache.org/usermanual/component_reference.html#While_Controller "Link to here")
------------------------------------------------------------------------------------------------------------------

The While Controller runs its children until the condition is "false".

 JMeter will expose the looping index as a variable named  __jm__ <Name of your element>__idx. So for example, if your While Controller is named WC, then you can access the looping index through ${__jm__WC__idx}. Index starts at 0 

Possible condition values:

*   blank - exit loop when last sample in loop fails
*   LAST - exit loop when last sample in loop fails. If the last sample just before the loop failed, don't enter loop. 
*    Otherwise - exit (or don't enter) the loop when the condition is equal to the string "false" 

 The condition can be any variable or function that eventually evaluates to the string "false". This allows the use of [__jexl3](https://jmeter.apache.org/usermanual/functions.html#__jexl3), [__groovy](https://jmeter.apache.org/usermanual/functions.html#__groovy) function, properties or variables as needed. 

 Note that the condition is evaluated twice, once before starting sampling children and once at end of children sampling, so putting non idempotent functions in Condition (like [__counter](https://jmeter.apache.org/usermanual/functions.html#__counter)) can introduce issues. 

 For example: 
*   ${VAR} - where VAR is set to false by some other test element 
*   ${__jexl3(${C}==10)}
*   ${__jexl3("${VAR2}"=="abcd")}
*   ${_P(property)} - where property is set to "false" somewhere else 

[![Image 48: Screenshot for Control-Panel of While Controller](https://jmeter.apache.org/images/screenshots/whilecontroller.png)](https://jmeter.apache.org/images/screenshots/whilecontroller.png)

Screenshot of Control-Panel of While Controller

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#While_Controller_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree, and used to name the transaction.

No

Condition

 blank, LAST, or variable/function 

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Switch Controller[¶](https://jmeter.apache.org/usermanual/component_reference.html#Switch_Controller "Link to here")
--------------------------------------------------------------------------------------------------------------------

The Switch Controller acts like the [Interleave Controller](https://jmeter.apache.org/usermanual/component_reference.html#Interleave_Controller) in that it runs one of the subordinate elements on each iteration, but rather than run them in sequence, the controller runs the element defined by the switch value.

 The switch value can also be a name. 

If the switch value is out of range, it will run the zeroth element, which therefore acts as the default for the numeric case. It also runs the zeroth element if the value is the empty string.

If the value is non-numeric (and non-empty), then the Switch Controller looks for the element with the same name (case is significant). If none of the names match, then the element named "default" (case not significant) is selected. If there is no default, then no element is selected, and the controller will not run anything.

[![Image 49: Screenshot for Control-Panel of Switch Controller](https://jmeter.apache.org/images/screenshots/switchcontroller.png)](https://jmeter.apache.org/images/screenshots/switchcontroller.png)

Screenshot of Control-Panel of Switch Controller

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Switch_Controller_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree.

No

Switch Value

The number (or name) of the subordinate element to be invoked. Elements are numbered from 0. Defaults to 0

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

ForEach Controller[¶](https://jmeter.apache.org/usermanual/component_reference.html#ForEach_Controller "Link to here")
----------------------------------------------------------------------------------------------------------------------

A ForEach controller loops through the values of a set of related variables. When you add samplers (or controllers) to a ForEach controller, every sample (or controller) is executed one or more times, where during every loop the variable has a new value. The input should consist of several variables, each extended with an underscore and a number. Each such variable must have a value. So for example when the input variable has the name inputVar, the following variables should have been defined:

*   inputVar_1 = wendy
*   inputVar_2 = charles
*   inputVar_3 = peter
*   inputVar_4 = john

Note: the "_" separator is now optional.

When the return variable is given as "returnVar", the collection of samplers and controllers under the ForEach controller will be executed 4 consecutive times, with the return variable having the respective above values, which can then be used in the samplers.

 JMeter will expose the looping index as a variable named  __jm__ <Name of your element>__idx. So for example, if your Loop Controller is named FEC, then you can access the looping index through ${__jm__FEC__idx}. Index starts at 0 

It is especially suited for running with the regular expression post-processor. This can "create" the necessary input variables out of the result data of a previous request. By omitting the "_" separator, the ForEach Controller can be used to loop through the groups by using the input variable refName_g, and can also loop through all the groups in all the matches by using an input variable of the form refName_${C}_g, where C is a counter variable.

 The ForEach Controller does not run any samples if inputVar_1 is null. This would be the case if the Regular Expression returned no matches. 

[![Image 50: Screenshot for Control-Panel of ForEach Controller](https://jmeter.apache.org/images/screenshots/logic-controller/foreach-controller.png)](https://jmeter.apache.org/images/screenshots/logic-controller/foreach-controller.png)

Screenshot of Control-Panel of ForEach Controller

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#ForEach_Controller_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree.

No

Input variable prefix

Prefix for the variable names to be used as input. Defaults to an empty string as prefix.

No

Start index for loop

Start index (exclusive) for loop over variables (first element is at start index + 1)

No

End index for loop

End index (inclusive) for loop over variables

No

Output variable

 The name of the variable which can be used in the loop for replacement in the samplers. Defaults to an empty variable name, which is most probably not wanted.

No

Use Separator

 If not checked, the "_" separator is omitted. 

Yes

 ForEach Example[¶](https://jmeter.apache.org/usermanual/component_reference.html#foreach_example "Link to here")

[Download](https://jmeter.apache.org/demos/forEachTestPlan.jmx) this example (see Figure 7). In this example, we created a Test Plan that sends a particular HTTP Request only once and sends another HTTP Request to every link that can be found on the page.

[![Image 51: Figure 7 - ForEach Controller Example](https://jmeter.apache.org/images/screenshots/logic-controller/foreach-example.png)](https://jmeter.apache.org/images/screenshots/logic-controller/foreach-example.png)

Figure 7 - ForEach Controller Example

We configured the Thread Group for a single thread and a loop count value of one. You can see that we added one HTTP Request to the Thread Group and another HTTP Request to the ForEach Controller.

After the first HTTP request, a regular expression extractor is added, which extracts all the html links out of the return page and puts them in the inputVar variable

In the ForEach loop, a HTTP sampler is added which requests all the links that were extracted from the first returned HTML page.

 ForEach Example[¶](https://jmeter.apache.org/usermanual/component_reference.html#foreach_example2 "Link to here")

Here is [another example](https://jmeter.apache.org/demos/ForEachTest2.jmx) you can download. This has two Regular Expressions and ForEach Controllers. The first RE matches, but the second does not match, so no samples are run by the second ForEach Controller

[![Image 52: Figure 8 - ForEach Controller Example 2](https://jmeter.apache.org/images/screenshots/logic-controller/foreach-example2.png)](https://jmeter.apache.org/images/screenshots/logic-controller/foreach-example2.png)

Figure 8 - ForEach Controller Example 2

The Thread Group has a single thread and a loop count of two.

Sample 1 uses the JavaTest Sampler to return the string "a b c d".

The Regex Extractor uses the expression (\w)\s which matches a letter followed by a space, and returns the letter (not the space). Any matches are prefixed with the string "inputVar".

The ForEach Controller extracts all variables with the prefix "inputVar_", and executes its sample, passing the value in the variable "returnVar". In this case it will set the variable to the values "a" "b" and "c" in turn.

The For 1 Sampler is another Java Sampler which uses the return variable "returnVar" as part of the sample Label and as the sampler Data.

Sample 2, Regex 2 and For 2 are almost identical, except that the Regex has been changed to "(\w)\sx", which clearly won't match. Thus the For 2 Sampler will not be run.

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Module Controller[¶](https://jmeter.apache.org/usermanual/component_reference.html#Module_Controller "Link to here")
--------------------------------------------------------------------------------------------------------------------

The Module Controller provides a mechanism for substituting test plan fragments into the current test plan at run-time.

A test plan fragment consists of a Controller and all the test elements (samplers etc.) contained in it. The fragment can be located in any Thread Group. If the fragment is located in a Thread Group, then its Controller can be disabled to prevent the fragment being run except by the Module Controller. Or you can store the fragments in a dummy Thread Group, and disable the entire Thread Group.

There can be multiple fragments, each with a different series of samplers under them. The module controller can then be used to easily switch between these multiple test cases simply by choosing the appropriate controller in its drop down box. This provides convenience for running many alternate test plans quickly and easily.

A fragment name is made up of the Controller name and all its parent names. For example:

Test Plan / Protocol: JDBC / Control / Interleave Controller (Module1)

Any **fragments used by the Module Controller must have a unique name**, as the name is used to find the target controller when a test plan is reloaded. For this reason it is best to ensure that the Controller name is changed from the default - as shown in the example above - otherwise a duplicate may be accidentally created when new elements are added to the test plan.

[![Image 53: Screenshot for Control-Panel of Module Controller](https://jmeter.apache.org/images/screenshots/module_controller.png)](https://jmeter.apache.org/images/screenshots/module_controller.png)

Screenshot of Control-Panel of Module Controller

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Module_Controller_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree.

No

Module to Run

The module controller provides a list of all controllers loaded into the gui. Select the one you want to substitute in at runtime.

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Include Controller[¶](https://jmeter.apache.org/usermanual/component_reference.html#Include_Controller "Link to here")
----------------------------------------------------------------------------------------------------------------------

The include controller is designed to use an external JMX file. To use it, create a Test Fragment underneath the Test Plan and add any desired samplers, controllers etc. below it. Then save the Test Plan. The file is now ready to be included as part of other Test Plans.

For convenience, a [Thread Group](https://jmeter.apache.org/usermanual/component_reference.html#Thread_Group) can also be added in the external JMX file for debugging purposes. A [Module Controller](https://jmeter.apache.org/usermanual/component_reference.html#Module_Controller) can be used to reference the Test Fragment. The [Thread Group](https://jmeter.apache.org/usermanual/component_reference.html#Thread_Group) will be ignored during the include process.

If the test uses a Cookie Manager or User Defined Variables, these should be placed in the top-level test plan, not the included file, otherwise they are not guaranteed to work.

 This element does not support variables/functions in the filename field. 

 However, if the property includecontroller.prefix is defined, the contents are used to prefix the pathname. 

 When using Include Controller and including the same JMX file, ensure you name the Include Controller differently to avoid facing known issue [Bug 50898](https://bz.apache.org/bugzilla/show_bug.cgi?id=50898). 

If the file cannot be found at the location given by prefix+Filename, then the controller attempts to open the Filename relative to the JMX launch directory.

[![Image 54: Screenshot for Control-Panel of Include Controller](https://jmeter.apache.org/images/screenshots/includecontroller.png)](https://jmeter.apache.org/images/screenshots/includecontroller.png)

Screenshot of Control-Panel of Include Controller

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Include_Controller_parms1 "Link to here")

Attribute

Description

Required

Filename

The file to include.

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Transaction Controller[¶](https://jmeter.apache.org/usermanual/component_reference.html#Transaction_Controller "Link to here")
------------------------------------------------------------------------------------------------------------------------------

The Transaction Controller generates an additional sample which measures the overall time taken to perform the nested test elements.

 Note: when the check box "Include duration of timer and pre-post processors in generated sample" is checked, the time includes all processing within the controller scope, not just the samples. 

There are two modes of operation:

*   additional sample is added after the nested samples
*   additional sample is added as a parent of the nested samples

The generated sample time includes all the times for the nested samplers excluding by default (since 2.11) timers and processing time of pre/post processors unless checkbox "Include duration of timer and pre-post processors in generated sample" is checked. Depending on the clock resolution, it may be slightly longer than the sum of the individual samplers plus timers. The clock might tick after the controller recorded the start time but before the first sample starts. Similarly at the end.

The generated sample is only regarded as successful if all its sub-samples are successful.

In parent mode, the individual samples can still be seen in the Tree View Listener, but no longer appear as separate entries in other Listeners. Also, the sub-samples do not appear in CSV log files, but they can be saved to XML files.

 In parent mode, Assertions (etc.) can be added to the Transaction Controller. However by default they will be applied to both the individual samples and the overall transaction sample. To limit the scope of the Assertions, use a Simple Controller to contain the samples, and add the Assertions to the Simple Controller. Parent mode controllers do not currently properly support nested transaction controllers of either type. 

[![Image 55: Screenshot for Control-Panel of Transaction Controller](https://jmeter.apache.org/images/screenshots/transactioncontroller.png)](https://jmeter.apache.org/images/screenshots/transactioncontroller.png)

Screenshot of Control-Panel of Transaction Controller

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Transaction_Controller_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree, and used to name the transaction.

Yes

Generate Parent Sample

 If checked, then the sample is generated as a parent of the other samples, otherwise the sample is generated as an independent sample. 

Yes

Include duration of timer and pre-post processors in generated sample

 Whether to include timer, pre- and post-processing delays in the generated sample. Default is false

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Recording Controller[¶](https://jmeter.apache.org/usermanual/component_reference.html#Recording_Controller "Link to here")
--------------------------------------------------------------------------------------------------------------------------

The Recording Controller is a place holder indicating where the proxy server should record samples to. During test run, it has no effect, similar to the Simple Controller. But during recording using the [HTTP(S) Test Script Recorder](https://jmeter.apache.org/usermanual/component_reference.html#HTTP(S)_Test_Script_Recorder), all recorded samples will by default be saved under the Recording Controller.

[![Image 56: Screenshot for Control-Panel of Recording Controller](https://jmeter.apache.org/images/screenshots/logic-controller/recording-controller.png)](https://jmeter.apache.org/images/screenshots/logic-controller/recording-controller.png)

Screenshot of Control-Panel of Recording Controller

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Recording_Controller_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree.

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Critical Section Controller[¶](https://jmeter.apache.org/usermanual/component_reference.html#Critical_Section_Controller "Link to here")
----------------------------------------------------------------------------------------------------------------------------------------

The Critical Section Controller ensures that its children elements (samplers/controllers, etc.) will be executed by only one thread as a named lock will be taken before executing children of controller.

[![Image 57: Screenshot for Control-Panel of Critical Section Controller](https://jmeter.apache.org/images/screenshots/logic-controller/critical-section-controller.png)](https://jmeter.apache.org/images/screenshots/logic-controller/critical-section-controller.png)

Screenshot of Control-Panel of Critical Section Controller

The figure below shows an example of using Critical Section Controller, in the figure below 2 Critical Section Controllers ensure that:

*   DS2-${__threadNum} is executed only by one thread at a time 
*   DS4-${__threadNum} is executed only by one thread at a time 

[![Image 58: Test Plan using Critical Section Controller](https://jmeter.apache.org/images/screenshots/logic-controller/critical-section-controller-tp.png)](https://jmeter.apache.org/images/screenshots/logic-controller/critical-section-controller-tp.png)

Test Plan using Critical Section Controller

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Critical_Section_Controller_parms1 "Link to here")

Attribute

Description

Required

Lock Name

Lock that will be taken by controller, ensure you use different lock names for unrelated sections

Yes

 Critical Section Controller takes locks only within one JVM, so if using Distributed testing ensure your use case does not rely on all threads of all JVMs blocking. 

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

18.3 Listeners[¶](https://jmeter.apache.org/usermanual/component_reference.html#listeners "Link to here")
=========================================================================================================

 Most of the listeners perform several roles in addition to "listening" to the test results. They also provide means to view, save, and read saved test results. 
Note that Listeners are processed at the end of the scope in which they are found.

The saving and reading of test results is generic. The various listeners have a panel whereby one can specify the file to which the results will be written (or read from). By default, the results are stored as XML files, typically with a ".jtl" extension. Storing as CSV is the most efficient option, but is less detailed than XML (the other available option).

**Listeners do _not_ process sample data in CLI mode, but the raw data will be saved if an output file has been configured.** In order to analyse the data generated by a CLI run, you need to load the file into the appropriate Listener.

 To read existing results and display them, use the file panel Browse button to open the file. 

If you want to clear any current data before loading a new file, use the menu item Run→Clear (Ctrl+Shift+E)  or Run→Clear All (Ctrl+E)  before loading the file.

Results can be read from XML or CSV format files. When reading from CSV results files, the header (if present) is used to determine which fields are present. **In order to interpret a header-less CSV file correctly, the appropriate properties must be set in jmeter.properties.**

 XML files written by JMeter have version 1.0 declared in header while actual file is serialized with 1.1 rules. (This is done for historical compatibility reasons; see [Bug 59973](https://bz.apache.org/bugzilla/show_bug.cgi?id=59973) and [Bug 58679](https://bz.apache.org/bugzilla/show_bug.cgi?id=58679)) This causes strict XML parsers to fail. Consider using non-strict XML parsers to read JTL files. 

 The file name can contain function and/or variable references. However variable references do not work in client-server mode (functions work OK). This is because the file is created on the client, and the client does not run the test locally so does not set up variables. 

**Listeners can use a lot of memory if there are a lot of samples.** Most of the listeners currently keep a copy of every sample in their scope, apart from:

*   Simple Data Writer
*   BeanShell/JSR223 Listener
*   Mailer Visualizer
*   Summary Report

The following Listeners no longer need to keep copies of every single sample. Instead, samples with the same elapsed time are aggregated. Less memory is now needed, especially if most samples only take a second or two at most.

*   Aggregate Report
*   Aggregate Graph

To minimise the amount of memory needed, use the Simple Data Writer, and use the CSV format.

 JMeter variables can be saved to the output files. This can only be specified using a property. See the [Listener Sample Variables](https://jmeter.apache.org/usermanual/listeners.html#sample_variables) for details 

For full details on setting up the default items to be saved see the [Listener Default Configuration](https://jmeter.apache.org/usermanual/listeners.html#defaults) documentation. For details of the contents of the output files, see the [CSV log](https://jmeter.apache.org/usermanual/listeners.html#csvlogformat) format or the [XML log](https://jmeter.apache.org/usermanual/listeners.html#xmlformat2.1) format.

 The entries in jmeter.properties are used to define the defaults; these can be overridden for individual listeners by using the Configure button, as shown below. The settings in jmeter.properties also apply to the listener that is added by using the -l command-line flag. 

The figure below shows an example of the result file configuration panel

[![Image 59: Screenshot for Control-Panel of Simple Data Writer](https://jmeter.apache.org/images/screenshots/simpledatawriter.png)](https://jmeter.apache.org/images/screenshots/simpledatawriter.png)

Result file configuration panel

### Parameters

Attribute

Description

Required

Filename

 Name of the file containing sample results. The file name can be specified using either a relative or an absolute path name. Relative paths are resolved relative to the current working directory (which defaults to the bin/ directory). JMeter also support paths relative to the directory containing the current test plan (JMX file). If the path name begins with "~/" (or whatever is in the jmeter.save.saveservice.base_prefix JMeter property), then the path is assumed to be relative to the JMX file location. 

No

Browse …

File Browse Button

No

Errors

Select this to write/read only results with errors

No

Successes

 Select this to write/read only results without errors. If neither Errors nor Successes is selected, then all results are processed. 

No

Configure

Configure Button, see below

No

Sample Result Save Configuration[¶](https://jmeter.apache.org/usermanual/component_reference.html#Sample_Result_Save_Configuration "Link to here")
--------------------------------------------------------------------------------------------------------------------------------------------------

Listeners can be configured to save different items to the result log files (JTL) by using the Config popup as shown below. The defaults are defined as described in the [Listener Default Configuration](https://jmeter.apache.org/usermanual/listeners.html#defaults) documentation. Items with (CSV) after the name only apply to the CSV format; items with (XML) only apply to XML format. CSV format cannot currently be used to save any items that include line-breaks.

Note that cookies, method and the query string are saved as part of the "Sampler Data" option.

[![Image 60: Screenshot for Control-Panel of Sample Result Save Configuration](https://jmeter.apache.org/images/screenshots/sample_result_config.png)](https://jmeter.apache.org/images/screenshots/sample_result_config.png)

Screenshot of Control-Panel of Sample Result Save Configuration

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Graph Results[¶](https://jmeter.apache.org/usermanual/component_reference.html#Graph_Results "Link to here")
------------------------------------------------------------------------------------------------------------

 Graph Results MUST NOT BE USED during load test as it consumes a lot of resources (memory and CPU). Use it only for either functional testing or during Test Plan debugging and Validation. 

The Graph Results listener generates a simple graph that plots all sample times. Along the bottom of the graph, the current sample (black), the current average of all samples (blue), the current standard deviation (red), and the current throughput rate (green) are displayed in milliseconds.

The throughput number represents the actual number of requests/minute the server handled. This calculation includes any delays you added to your test and JMeter's own internal processing time. The advantage of doing the calculation like this is that this number represents something real - your server in fact handled that many requests per minute, and you can increase the number of threads and/or decrease the delays to discover your server's maximum throughput. Whereas if you made calculations that factored out delays and JMeter's processing, it would be unclear what you could conclude from that number.

[![Image 61: Screenshot for Control-Panel of Graph Results](https://jmeter.apache.org/images/screenshots/graph_results.png)](https://jmeter.apache.org/images/screenshots/graph_results.png)

Screenshot of Control-Panel of Graph Results

The following table briefly describes the items on the graph. Further details on the precise meaning of the statistical terms can be found on the web - e.g. Wikipedia - or by consulting a book on statistics.

*   Data - plot the actual data values 
*   Average - plot the Average 
*   Median - plot the [Median](https://jmeter.apache.org/usermanual/glossary.html#Median) (midway value) 
*   Deviation - plot the [Standard Deviation](https://jmeter.apache.org/usermanual/glossary.html#StandardDeviation) (a measure of the variation) 
*   Throughput - plot the number of samples per unit of time 

The individual figures at the bottom of the display are the current values. "Latest Sample" is the current elapsed sample time, shown on the graph as "Data".

The value displayed on the top left of graph is the max of 90 th percentile of response time.

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Assertion Results[¶](https://jmeter.apache.org/usermanual/component_reference.html#Assertion_Results "Link to here")
--------------------------------------------------------------------------------------------------------------------

 Assertion Results MUST NOT BE USED during load test as it consumes a lot of resources (memory and CPU). Use it only for either functional testing or during Test Plan debugging and Validation. 

The Assertion Results visualizer shows the Label of each sample taken. It also reports failures of any [Assertions](https://jmeter.apache.org/usermanual/test_plan.html#assertions) that are part of the test plan.

[![Image 62: Screenshot for Control-Panel of Assertion Results](https://jmeter.apache.org/images/screenshots/assertion_results.png)](https://jmeter.apache.org/images/screenshots/assertion_results.png)

Screenshot of Control-Panel of Assertion Results

See also:

*   [Response Assertion](https://jmeter.apache.org/usermanual/component_reference.html#Response_Assertion)

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

View Results Tree[¶](https://jmeter.apache.org/usermanual/component_reference.html#View_Results_Tree "Link to here")
--------------------------------------------------------------------------------------------------------------------

 View Results Tree MUST NOT BE USED during load test as it consumes a lot of resources (memory and CPU). Use it only for either functional testing or during Test Plan debugging and Validation. 

 The View Results Tree shows a tree of all sample responses, allowing you to view the response for any sample. In addition to showing the response, you can see the time it took to get this response, and some response codes. Note that the Request panel only shows the headers added by JMeter. It does not show any headers (such as Host) that may be added by the HTTP protocol implementation. 
There are several ways to view the response, selectable by a drop-down box at the bottom of the left hand panel.

| **Renderer** | **Description** |
| --- | --- |
| CSS/JQuery Tester | The _CSS/JQuery Tester_ only works for text responses. It shows the plain text in the upper panel. The "Test" button allows the user to apply the CSS/JQuery to the upper panel and the results will be displayed in the lower panel. The CSS/JQuery expression engine can be JSoup or Jodd, syntax of these 2 implementation differs slightly. For example, the Selector a[class=sectionlink] with attribute href applied to the current JMeter functions page gives the following output: Match count: 74 Match[1]=#functions Match[2]=#what_can_do Match[3]=#where Match[4]=#how Match[5]=#function_helper Match[6]=#functions Match[7]=#__regexFunction Match[8]=#__regexFunction_parms Match[9]=#__counter … and so on … |
| Document | The _Document view_ will show the extract text from various type of documents like Microsoft Office (Word, Excel, PowerPoint 97-2003, 2007-2010 (openxml), Apache OpenOffice (writer, calc, impress), HTML, gzip, jar/zip files (list of content), and some meta-data on "multimedia" files like mp3, mp4, flv, etc. The complete list of support format is available on [Apache Tika format page.](http://tika.apache.org/1.2/formats.html) A requirement to the Document view is to download the [Apache Tika binary package](http://tika.apache.org/download.html) (tika-app-x.x.jar) and put this in JMETER_HOME/lib directory. If the document is larger than 10 MB, then it won't be displayed. To change this limit, set the JMeter property document.max_size (unit is byte) or set to 0 to remove the limit. |
| HTML | The _HTML view_ attempts to render the response as HTML. The rendered HTML is likely to compare poorly to the view one would get in any web browser; however, it does provide a quick approximation that is helpful for initial result evaluation. Images, style-sheets, etc. aren't downloaded. |
| HTML (download resources) | If the _HTML (download resources) view_ option is selected, the renderer may download images, style-sheets, etc. referenced by the HTML code. |
| HTML Source formatted | If the _HTML Source formatted view_ option is selected, the renderer will display the HTML source code formatted and cleaned by [Jsoup](https://jsoup.org/). |
| JSON | The _JSON view_ will show the response in tree style (also handles JSON embedded in JavaScript). |
| JSON Path Tester | The _JSON Path Tester view_ will let you test your JSON-PATH expressions and see the extracted data from a particular response. |
| JSON JMESPath Tester | The _JSON JMESPath Tester view_ will let you test your [JMESPath](http://jmespath.org/) expressions and see the extracted data from a particular response. |
| Regexp Tester | The _Regexp Tester view_ only works for text responses. It shows the plain text in the upper panel. The "Test" button allows the user to apply the Regular Expression to the upper panel and the results will be displayed in the lower panel. The regular expression engine is the same as that used in the Regular Expression Extractor. For example, the RE (JMeter\w*).* applied to the current JMeter home page gives the following output: Match count: 26 Match[1][0]=JMeter - Apache JMeter</title> Match[1][1]=JMeter Match[2][0]=JMeter" title="JMeter" border="0"/></a> Match[2][1]=JMeter Match[3][0]=JMeterCommitters">Contributors</a> Match[3][1]=JMeterCommitters … and so on … The first number in [] is the match number; the second number is the group. Group [0] is whatever matched the whole RE. Group [1] is whatever matched the 1 st group, i.e. (JMeter\w*) in this case. See Figure 9b (below). |
| Text | The default _Text view_ shows all of the text contained in the response. Note that this will only work if the response content-type is considered to be text. If the content-type begins with any of the following, it is considered as binary, otherwise it is considered to be text. image/ audio/ video/ |
| XML | The _XML view_ will show response in tree style. Any DTD nodes or Prolog nodes will not show up in tree; however, response may contain those nodes. You can right-click on any node and expand or collapse all nodes below it. |
| XPath Tester | The _XPath Tester_ only works for text responses. It shows the plain text in the upper panel. The "Test" button allows the user to apply the XPath query to the upper panel and the results will be displayed in the lower panel. |
| Boundary Extractor Tester | The _Boundary Extractor Tester_ only works for text responses. It shows the plain text in the upper panel. The "Test" button allows the user to apply the Boundary Extractor query to the upper panel and the results will be displayed in the lower panel. |

Scroll automatically? option permit to have last node display in tree selection

 Starting with version 3.2 the number of entries in the View is restricted to the value of the property view.results.tree.max_results which defaults to 500 entries. The old behaviour can be restored by setting the property to 0. Beware, that this might consume a lot of memory. 

With Search option, most of the views also allow the displayed data to be searched; the result of the search will be high-lighted in the display above. For example the Control panel screenshot below shows one result of searching for "Java". Note that the search operates on the visible text, so you may get different results when searching the Text and HTML views. 

 Note: The regular expression uses the Java engine (not ORO engine like the Regular Expression Extractor or Regexp Tester view).

If there is no content-type provided, then the content will not be displayed in the any of the Response Data panels. You can use [Save Responses to a file](https://jmeter.apache.org/usermanual/component_reference.html#Save_Responses_to_a_file) to save the data in this case. Note that the response data will still be available in the sample result, so can still be accessed using Post-Processors.

If the response data is larger than 200K, then it won't be displayed. To change this limit, set the JMeter property view.results.tree.max_size. You can also use save the entire response to a file using [Save Responses to a file](https://jmeter.apache.org/usermanual/component_reference.html#Save_Responses_to_a_file).

Additional renderers can be created. The class must implement the interface org.apache.jmeter.visualizers.ResultRenderer and/or extend the abstract class org.apache.jmeter.visualizers.SamplerResultTab, and the compiled code must be available to JMeter (e.g. by adding it to the lib/ext directory).

[![Image 63: Screenshot for Control-Panel of View Results Tree](https://jmeter.apache.org/images/screenshots/view_results_tree.png)](https://jmeter.apache.org/images/screenshots/view_results_tree.png)

Screenshot of Control-Panel of View Results Tree

The Control Panel (above) shows an example of an HTML display. 

 Figure 9 (below) shows an example of an XML display. 

 Figure 9a (below) shows an example of a Regexp tester display. 

 Figure 9b (below) shows an example of a Document display.

[![Image 64: Figure 9 Sample XML display](https://jmeter.apache.org/images/screenshots/view_results_tree_xml.png)](https://jmeter.apache.org/images/screenshots/view_results_tree_xml.png)

Figure 9 Sample XML display

[![Image 65: Figure 9a Sample Regexp Test display](https://jmeter.apache.org/images/screenshots/view_results_tree_regex.png)](https://jmeter.apache.org/images/screenshots/view_results_tree_regex.png)

Figure 9a Sample Regexp Test display

[![Image 66: Figure 9b Sample Document (here PDF) display](https://jmeter.apache.org/images/screenshots/view_results_tree_document.png)](https://jmeter.apache.org/images/screenshots/view_results_tree_document.png)

Figure 9b Sample Document (here PDF) display

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Aggregate Report[¶](https://jmeter.apache.org/usermanual/component_reference.html#Aggregate_Report "Link to here")
------------------------------------------------------------------------------------------------------------------

 The aggregate report creates a table row for each differently named request in your test. For each request, it totals the response information and provides request count, min, max, average, error rate, approximate throughput (request/second) and Kilobytes per second throughput. Once the test is done, the throughput is the actual through for the duration of the entire test. 
The throughput is calculated from the point of view of the sampler target (e.g. the remote server in the case of HTTP samples). JMeter takes into account the total time over which the requests have been generated. If other samplers and timers are in the same thread, these will increase the total time, and therefore reduce the throughput value. So two identical samplers with different names will have half the throughput of two samplers with the same name. It is important to choose the sampler names correctly to get the best results from the Aggregate Report.

Calculation of the [Median](https://jmeter.apache.org/usermanual/glossary.html#Median) and 90 % Line (90 th[percentile](https://jmeter.apache.org/usermanual/glossary.html#Percentile)) values requires additional memory. JMeter now combines samples with the same elapsed time, so far less memory is used. However, for samples that take more than a few seconds, the probability is that fewer samples will have identical times, in which case more memory will be needed. Note you can use this listener afterwards to reload a CSV or XML results file which is the recommended way to avoid performance impacts. See the [Summary Report](https://jmeter.apache.org/usermanual/component_reference.html#Summary_Report) for a similar Listener that does not store individual samples and so needs constant memory.

 Starting with JMeter 2.12, you can configure the 3 percentile values you want to compute, this can be done by setting properties: 
*   aggregate_rpt_pct1: defaults to 90 th[percentile](https://jmeter.apache.org/usermanual/glossary.html#Percentile)
*   aggregate_rpt_pct2: defaults to 95 th[percentile](https://jmeter.apache.org/usermanual/glossary.html#Percentile)
*   aggregate_rpt_pct3: defaults to 99 th[percentile](https://jmeter.apache.org/usermanual/glossary.html#Percentile)

*   Label - The label of the sample. If "Include group name in label?" is selected, then the name of the thread group is added as a prefix. This allows identical labels from different thread groups to be collated separately if required. 
*   # Samples - The number of samples with the same label 
*   Average - The average time of a set of results 
*   Median - The [median](https://jmeter.apache.org/usermanual/glossary.html#Median) is the time in the middle of a set of results. 50 % of the samples took no more than this time; the remainder took at least as long. 
*   90% Line - 90 % of the samples took no more than this time. The remaining samples took at least as long as this. (90 th[percentile](https://jmeter.apache.org/usermanual/glossary.html#Percentile)) 
*   95% Line - 95 % of the samples took no more than this time. The remaining samples took at least as long as this. (95 th[percentile](https://jmeter.apache.org/usermanual/glossary.html#Percentile)) 
*   99% Line - 99 % of the samples took no more than this time. The remaining samples took at least as long as this. (99 th[percentile](https://jmeter.apache.org/usermanual/glossary.html#Percentile)) 
*   Min - The shortest time for the samples with the same label 
*   Max - The longest time for the samples with the same label
*   Error % - Percent of requests with errors 
*   Throughput - the [Throughput](https://jmeter.apache.org/usermanual/glossary.html#Throughput) is measured in requests per second/minute/hour. The time unit is chosen so that the displayed rate is at least 1.0. When the throughput is saved to a CSV file, it is expressed in requests/second, i.e. 30.0 requests/minute is saved as 0.5. 
*   Received KB/sec - The throughput measured in received Kilobytes per second 
*   Sent KB/sec - The throughput measured in sent Kilobytes per second 

Times are in milliseconds.

[![Image 67: Screenshot for Control-Panel of Aggregate Report](https://jmeter.apache.org/images/screenshots/aggregate_report.png)](https://jmeter.apache.org/images/screenshots/aggregate_report.png)

Screenshot of Control-Panel of Aggregate Report

The figure below shows an example of selecting the "Include group name" checkbox.

[![Image 68: Sample "](https://jmeter.apache.org/images/screenshots/aggregate_report_grouped.png)](https://jmeter.apache.org/images/screenshots/aggregate_report_grouped.png)

 Sample "Include group name" display 

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

View Results in Table[¶](https://jmeter.apache.org/usermanual/component_reference.html#View_Results_in_Table "Link to here")
----------------------------------------------------------------------------------------------------------------------------

 This visualizer creates a row for every sample result. Like the [View Results Tree](https://jmeter.apache.org/usermanual/component_reference.html#View_Results_Tree), this visualizer uses a lot of memory. 
By default, it only displays the main (parent) samples; it does not display the sub-samples (child samples). JMeter has a "Child Samples?" check-box. If this is selected, then the sub-samples are displayed instead of the main samples.

[![Image 69: Screenshot for Control-Panel of View Results in Table](https://jmeter.apache.org/images/screenshots/table_results.png)](https://jmeter.apache.org/images/screenshots/table_results.png)

Screenshot of Control-Panel of View Results in Table

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Simple Data Writer[¶](https://jmeter.apache.org/usermanual/component_reference.html#Simple_Data_Writer "Link to here")
----------------------------------------------------------------------------------------------------------------------

 This listener can record results to a file but not to the UI. It is meant to provide an efficient means of recording data by eliminating GUI overhead. When running in CLI mode, the -l flag can be used to create a data file. The fields to save are defined by JMeter properties. See the jmeter.properties file for details. 

[![Image 70: Screenshot for Control-Panel of Simple Data Writer](https://jmeter.apache.org/images/screenshots/simpledatawriter.png)](https://jmeter.apache.org/images/screenshots/simpledatawriter.png)

Screenshot of Control-Panel of Simple Data Writer

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Aggregate Graph[¶](https://jmeter.apache.org/usermanual/component_reference.html#Aggregate_Graph "Link to here")
----------------------------------------------------------------------------------------------------------------

The aggregate graph is similar to the aggregate report. The primary difference is the aggregate graph provides an easy way to generate bar graphs and save the graph as a PNG file.

[![Image 71: Screenshot for Control-Panel of Aggregate Graph](https://jmeter.apache.org/images/screenshots/aggregate_graph.png)](https://jmeter.apache.org/images/screenshots/aggregate_graph.png)

Screenshot of Control-Panel of Aggregate Graph

The figure below shows an example of settings to draw this graph.

[![Image 72: Aggregate graph settings](https://jmeter.apache.org/images/screenshots/aggregate_graph_settings.png)](https://jmeter.apache.org/images/screenshots/aggregate_graph_settings.png)

Aggregate graph settings

 Please note: All this parameters _aren't_ saved in JMeter JMX script. 

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Aggregate_Graph_parms1 "Link to here")

Attribute

Description

Required

Column settings

*   Columns to display: Choose the column(s) to display in graph. 
*   Rectangles color: Click on right color rectangle open a popup dialog to choose a custom color for column. 
*   Foreground color Allow to change the value text color. 
*   Value font: Allow to define font settings for the text. 
*   Draw outlines bar? To draw or not the border line on bar chart 
*   Show number grouping? Show or not the number grouping in Y Axis labels. 
*   Value labels vertical? Change orientation for value label. (Default is horizontal) 
*   Column label selection: Filter by result label. A regular expression can be used, example: .*Transaction.*

 Before display the graph, click on Apply filter button to refresh internal data. 

Yes

Title

 Define the graph's title on the head of chart. Empty value is the default value: "Aggregate Graph". The button Synchronize with name define the title with the label of the listener. And define font settings for graph title 

No

Graph size

 Compute the graph size by the width and height depending of the current JMeter's window size. Use Width and Height fields to define a custom size. The unit is pixel. 

No

X Axis settings

Define the max length of X Axis label (in pixel).

No

Y Axis settings

Define a custom maximum value for Y Axis.

No

Legend

Define the placement and font settings for chart legend

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Response Time Graph[¶](https://jmeter.apache.org/usermanual/component_reference.html#Response_Time_Graph "Link to here")
------------------------------------------------------------------------------------------------------------------------

 The Response Time Graph draws a line chart showing the evolution of response time during the test, for each labelled request. If many samples exist for the same timestamp, the mean value is displayed. 

[![Image 73: Screenshot for Control-Panel of Response Time Graph](https://jmeter.apache.org/images/screenshots/response_time_graph.png)](https://jmeter.apache.org/images/screenshots/response_time_graph.png)

Screenshot of Control-Panel of Response Time Graph

The figure below shows an example of settings to draw this graph.

[![Image 74: Response time graph settings](https://jmeter.apache.org/images/screenshots/response_time_graph_settings.png)](https://jmeter.apache.org/images/screenshots/response_time_graph_settings.png)

Response time graph settings

 Please note: All this parameters are saved in JMeter .jmx file. 

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Response_Time_Graph_parms1 "Link to here")

Attribute

Description

Required

Interval (ms)

 The time in milliseconds for X axis interval. Samples are grouped according to this value. Before display the graph, click on Apply interval button to refresh internal data. 

Yes

Sampler label selection

 Filter by result label. A regular expression can be used, ex. .*Transaction.*. Before display the graph, click on Apply filter button to refresh internal data. 

No

Title

 Define the graph's title on the head of chart. Empty value is the default value: "Response Time Graph". The button Synchronize with name define the title with the label of the listener. And define font settings for graph title 

No

Line settings

 Define the width of the line. Define the type of each value point. Choose none to have a line without mark 

Yes

Graph size

 Compute the graph size by the width and height depending of the current JMeter's window size. Use Width and Height fields to define a custom size. The unit is pixel. 

No

X Axis settings

 Customize the date format of X axis label. The syntax is the Java [SimpleDateFormat API](http://docs.oracle.com/javase/8/docs/api/java/text/SimpleDateFormat.html). 

No

Y Axis settings

Define a custom maximum value for Y Axis in milli-seconds. Define the increment for the scale (in ms) Show or not the number grouping in Y Axis labels.

No

Legend

Define the placement and font settings for chart legend

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Mailer Visualizer[¶](https://jmeter.apache.org/usermanual/component_reference.html#Mailer_Visualizer "Link to here")
--------------------------------------------------------------------------------------------------------------------

The mailer visualizer can be set up to send email if a test run receives too many failed responses from the server.

[![Image 75: Screenshot for Control-Panel of Mailer Visualizer](https://jmeter.apache.org/images/screenshots/mailervisualizer.png)](https://jmeter.apache.org/images/screenshots/mailervisualizer.png)

Screenshot of Control-Panel of Mailer Visualizer

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Mailer_Visualizer_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

From

Email address to send messages from.

Yes

Addressee(s)

Email address to send messages to, comma-separated.

Yes

Success Subject

Email subject line for success messages.

No

Success Limit

 Once this number of successful responses is exceeded **after previously reaching the failure limit**, a success email is sent. The mailer will thus only send out messages in a sequence of failed-succeeded-failed-succeeded, etc. 

Yes

Failure Subject

Email subject line for fail messages.

No

Failure Limit

 Once this number of failed responses is exceeded, a failure email is sent - i.e. set the count to 0 to send an e-mail on the first failure. 

Yes

Host

IP address or host name of SMTP server (email redirector) server.

No

Port

 Port of SMTP server (defaults to 25). 

No

Login

Login used to authenticate.

No

Password

Password used to authenticate.

No

Connection security

Type of encryption for SMTP authentication (SSL, TLS or none).

No

Test Mail

Press this button to send a test mail

No

Failures

A field that keeps a running total of number of failures so far received.

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

BeanShell Listener[¶](https://jmeter.apache.org/usermanual/component_reference.html#BeanShell_Listener "Link to here")
----------------------------------------------------------------------------------------------------------------------

The BeanShell Listener allows the use of BeanShell for processing samples for saving etc.

**For full details on using BeanShell, please see the [BeanShell website.](http://www.beanshell.org/)**

 Migration to [JSR223 Listener](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_Listener)+Groovy is highly recommended for performance, support of new Java features and limited maintenance of the BeanShell library. 

The test element supports the ThreadListener and TestListener methods. These should be defined in the initialisation file. See the file BeanShellListeners.bshrc for example definitions.

[![Image 76: Screenshot for Control-Panel of BeanShell Listener](https://jmeter.apache.org/images/screenshots/beanshell_listener.png)](https://jmeter.apache.org/images/screenshots/beanshell_listener.png)

Screenshot of Control-Panel of BeanShell Listener

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#BeanShell_Listener_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree. The name is stored in the script variable Label

Reset bsh.Interpreter before each call

 If this option is selected, then the interpreter will be recreated for each sample. This may be necessary for some long running scripts. For further information, see [Best Practices - BeanShell scripting](https://jmeter.apache.org/usermanual/best-practices.html#bsh_scripting). 

Yes

Parameters

 Parameters to pass to the BeanShell script. The parameters are stored in the following variables: Parameters string containing the parameters as a single variable bsh.args String array containing parameters, split on white-space

No

Script file

 A file containing the BeanShell script to run. The file name is stored in the script variable FileName

No

Script

The BeanShell script to run. The return value is ignored.

Yes (unless script file is provided)

Before invoking the script, some variables are set up in the BeanShell interpreter:

*   log - ([Logger](https://www.slf4j.org/api/org/slf4j/Logger.html)) - can be used to write to the log file 
*   ctx - ([JMeterContext](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterContext.html)) - gives access to the context 
*   vars - ([JMeterVariables](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterVariables.html)) - gives read/write access to variables: vars.get(key);
vars.put(key,val);
vars.putObject("OBJ1",new Object());
*   props - (JMeterProperties - class [java.util.Properties](https://docs.oracle.com/javase/8/docs/api/java/util/Properties.html)) - e.g. props.get("START.HMS");props.put("PROP1","1234");
*   sampleResult, prev - ([SampleResult](https://jmeter.apache.org/api/org/apache/jmeter/samplers/SampleResult.html)) - gives access to the previous [SampleResult](https://jmeter.apache.org/api/org/apache/jmeter/samplers/SampleResult.html)
*   sampleEvent ([SampleEvent](https://jmeter.apache.org/api/org/apache/jmeter/samplers/SampleEvent.html)) gives access to the current sample event 

For details of all the methods available on each of the above variables, please check the Javadoc

If the property beanshell.listener.init is defined, this is used to load an initialisation file, which can be used to define methods etc. for use in the BeanShell script.

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Summary Report[¶](https://jmeter.apache.org/usermanual/component_reference.html#Summary_Report "Link to here")
--------------------------------------------------------------------------------------------------------------

 The summary report creates a table row for each differently named request in your test. This is similar to the [Aggregate Report](https://jmeter.apache.org/usermanual/component_reference.html#Aggregate_Report) , except that it uses less memory. 
The throughput is calculated from the point of view of the sampler target (e.g. the remote server in the case of HTTP samples). JMeter takes into account the total time over which the requests have been generated. If other samplers and timers are in the same thread, these will increase the total time, and therefore reduce the throughput value. So two identical samplers with different names will have half the throughput of two samplers with the same name. It is important to choose the sampler labels correctly to get the best results from the Report.

*   Label - The label of the sample. If "Include group name in label?" is selected, then the name of the thread group is added as a prefix. This allows identical labels from different thread groups to be collated separately if required. 
*   # Samples - The number of samples with the same label 
*   Average - The average elapsed time of a set of results 
*   Min - The lowest elapsed time for the samples with the same label 
*   Max - The longest elapsed time for the samples with the same label 
*   Std. Dev. - the [Standard Deviation](https://jmeter.apache.org/usermanual/glossary.html#StandardDeviation) of the sample elapsed time 
*   Error % - Percent of requests with errors 
*   Throughput - the [Throughput](https://jmeter.apache.org/usermanual/glossary.html#Throughput) is measured in requests per second/minute/hour. The time unit is chosen so that the displayed rate is at least 1.0. When the throughput is saved to a CSV file, it is expressed in requests/second, i.e. 30.0 requests/minute is saved as 0.5. 
*   Received KB/sec - The throughput measured in Kilobytes per second 
*   Sent KB/sec - The throughput measured in Kilobytes per second 
*   Avg. Bytes - average size of the sample response in bytes. 

Times are in milliseconds.

[![Image 77: Screenshot for Control-Panel of Summary Report](https://jmeter.apache.org/images/screenshots/summary_report.png)](https://jmeter.apache.org/images/screenshots/summary_report.png)

Screenshot of Control-Panel of Summary Report

The figure below shows an example of selecting the "Include group name" checkbox.

[![Image 78: Sample "](https://jmeter.apache.org/images/screenshots/summary_report_grouped.png)](https://jmeter.apache.org/images/screenshots/summary_report_grouped.png)

 Sample "Include group name" display 

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Save Responses to a file[¶](https://jmeter.apache.org/usermanual/component_reference.html#Save_Responses_to_a_file "Link to here")
----------------------------------------------------------------------------------------------------------------------------------

This test element can be placed anywhere in the test plan. For each sample in its scope, it will create a file of the response Data. The primary use for this is in creating functional tests, but it can also be useful where the response is too large to be displayed in the [View Results Tree](https://jmeter.apache.org/usermanual/component_reference.html#View_Results_Tree) Listener. The file name is created from the specified prefix, plus a number (unless this is disabled, see below). The file extension is created from the document type, if known. If not known, the file extension is set to 'unknown'. If numbering is disabled, and adding a suffix is disabled, then the file prefix is taken as the entire file name. This allows a fixed file name to be generated if required. The generated file name is stored in the sample response, and can be saved in the test log output file if required.

The current sample is saved first, followed by any sub-samples (child samples). If a variable name is provided, then the names of the files are saved in the order that the sub-samples appear. See below.

[![Image 79: Screenshot for Control-Panel of Save Responses to a file](https://jmeter.apache.org/images/screenshots/savetofile.png)](https://jmeter.apache.org/images/screenshots/savetofile.png)

Screenshot of Control-Panel of Save Responses to a file

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Save_Responses_to_a_file_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Filename Prefix (can include folders)

 Prefix for the generated file names; this can include a directory name. Relative paths are resolved relative to the current working directory (which defaults to the bin/ directory). JMeter also supports paths relative to the directory containing the current test plan (JMX file). If the path name begins with "~/" (or whatever is in the jmeter.save.saveservice.base_prefix JMeter property), then the path is assumed to be relative to the JMX file location. 

 If parent folders in prefix do not exists, JMeter will create them and stop test if it fails. 

 Please note that Filename Prefix must not contain Thread related data, so don't use any Variable (${varName}) or functions like ${__threadNum} in this field 

Yes

Variable Name containing saved file name

 Name of a variable in which to save the generated file name (so it can be used later in the test plan). If there are sub-samples then a numeric suffix is added to the variable name. E.g. if the variable name is FILENAME, then the parent sample file name is saved in the variable FILENAME, and the filenames for the child samplers are saved in FILENAME1, FILENAME2 etc. 

No

Minimum Length of sequence number

 If "Don't add number to prefix" is not checked, then numbers added to prefix will be padded by 0 so that prefix is has size of this value. Defaults to 0. 

No

Save Failed Responses only

If selected, then only failed responses are saved

Yes

Save Successful Responses only

If selected, then only successful responses are saved

Yes

Don't add number to prefix

If selected, then no number is added to the prefix. If you select this option, make sure that the prefix is unique or the file may be overwritten.

Yes

Don't add content type suffix

If selected, then no suffix is added. If you select this option, make sure that the prefix is unique or the file may be overwritten.

Yes

Add timestamp

 If selected, then date will be included in file suffix following format yyyyMMdd-HHmm_

Yes

Don't Save Transaction Controller SampleResult

If selected, then SamplerResult generated by Transaction Controller will be ignored

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

JSR223 Listener[¶](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_Listener "Link to here")
----------------------------------------------------------------------------------------------------------------

The JSR223 Listener allows JSR223 script code to be applied to sample results.

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_Listener_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Language

The JSR223 language to be used

Yes

Parameters

 Parameters to pass to the script. The parameters are stored in the following variables: Parameters string containing the parameters as a single variable args String array containing parameters, split on white-space

No

Script file

 A file containing the script to run, if a relative file path is used, then it will be relative to directory referenced by "user.dir" System property 

No

Script compilation caching

 Unique String across Test Plan that JMeter will use to cache result of Script compilation if language used supports [Compilable](https://docs.oracle.com/javase/8/docs/api/javax/script/Compilable.html) interface (Groovy is one of these, java, beanshell and javascript are not). 

See note in JSR223 Sampler Java System property if you're using Groovy without checking this option

No

Script

The script to run.

Yes (unless script file is provided)

Before invoking the script, some variables are set up. Note that these are JSR223 variables - i.e. they can be used directly in the script.

log ([Logger](https://www.slf4j.org/api/org/slf4j/Logger.html)) - can be used to write to the log file Label the String Label FileName the script file name (if any)Parameters the parameters (as a String)args the parameters as a String array (split on whitespace)ctx ([JMeterContext](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterContext.html)) - gives access to the context vars ([JMeterVariables](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterVariables.html)) - gives read/write access to variables: vars.get(key);
vars.put(key,val);
vars.putObject("OBJ1",new Object());
vars.getObject("OBJ2");props (JMeterProperties - class [java.util.Properties](https://docs.oracle.com/javase/8/docs/api/java/util/Properties.html)) - e.g. props.get("START.HMS");props.put("PROP1","1234");sampleResult, prev ([SampleResult](https://jmeter.apache.org/api/org/apache/jmeter/samplers/SampleResult.html)) - gives access to the SampleResult sampleEvent ([SampleEvent](https://jmeter.apache.org/api/org/apache/jmeter/samplers/SampleEvent.html)) - gives access to the SampleEvent sampler ([Sampler](https://jmeter.apache.org/api/org/apache/jmeter/samplers/Sampler.html))- gives access to the last sampler OUT System.out - e.g. OUT.println("message")
For details of all the methods available on each of the above variables, please check the Javadoc

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Generate Summary Results[¶](https://jmeter.apache.org/usermanual/component_reference.html#Generate_Summary_Results "Link to here")
----------------------------------------------------------------------------------------------------------------------------------

 This test element can be placed anywhere in the test plan. Generates a summary of the test run so far to the log file and/or standard output. Both running and differential totals are shown. Output is generated every n seconds (default 30 seconds) on the appropriate time boundary, so that multiple test runs on the same time will be synchronised. 

Since a summary/differential line is written only if there are samples emitted, the interval for generation may not be respected if your test has no sample generated within the interval

 See jmeter.properties file for the summariser configuration items: 
# Define the following property to automatically start a summariser with that name
# (applies to CLI mode only)
#summariser.name=summary
#
# interval between summaries (in seconds) default 3 minutes
#summariser.interval=30
#
# Write messages to log file
#summariser.log=true
#
# Write messages to System.out
#summariser.out=true
 This element is mainly intended for batch (CLI) runs. The output looks like the following: 
label +     16 in 0:00:12 =    1.3/s Avg:  1608 Min:  1163 Max:  2009 Err:     0 (0.00%) Active: 5 Started: 5 Finished: 0
label +     82 in 0:00:30 =    2.7/s Avg:  1518 Min:  1003 Max:  2020 Err:     0 (0.00%) Active: 5 Started: 5 Finished: 0
label =     98 in 0:00:42 =    2.3/s Avg:  1533 Min:  1003 Max:  2020 Err:     0 (0.00%)
label +     85 in 0:00:30 =    2.8/s Avg:  1505 Min:  1008 Max:  2005 Err:     0 (0.00%) Active: 5 Started: 5 Finished: 0
label =    183 in 0:01:13 =    2.5/s Avg:  1520 Min:  1003 Max:  2020 Err:     0 (0.00%)
label +     79 in 0:00:30 =    2.7/s Avg:  1578 Min:  1089 Max:  2012 Err:     0 (0.00%) Active: 5 Started: 5 Finished: 0
label =    262 in 0:01:43 =    2.6/s Avg:  1538 Min:  1003 Max:  2020 Err:     0 (0.00%)
label +     80 in 0:00:30 =    2.7/s Avg:  1531 Min:  1013 Max:  2014 Err:     0 (0.00%) Active: 5 Started: 5 Finished: 0
label =    342 in 0:02:12 =    2.6/s Avg:  1536 Min:  1003 Max:  2020 Err:     0 (0.00%)
label +     83 in 0:00:31 =    2.7/s Avg:  1512 Min:  1003 Max:  1982 Err:     0 (0.00%) Active: 5 Started: 5 Finished: 0
label =    425 in 0:02:43 =    2.6/s Avg:  1531 Min:  1003 Max:  2020 Err:     0 (0.00%)
label +     83 in 0:00:29 =    2.8/s Avg:  1487 Min:  1023 Max:  2013 Err:     0 (0.00%) Active: 5 Started: 5 Finished: 0
label =    508 in 0:03:12 =    2.6/s Avg:  1524 Min:  1003 Max:  2020 Err:     0 (0.00%)
label +     78 in 0:00:30 =    2.6/s Avg:  1594 Min:  1013 Max:  2016 Err:     0 (0.00%) Active: 5 Started: 5 Finished: 0
label =    586 in 0:03:43 =    2.6/s Avg:  1533 Min:  1003 Max:  2020 Err:     0 (0.00%)
label +     80 in 0:00:30 =    2.7/s Avg:  1516 Min:  1013 Max:  2005 Err:     0 (0.00%) Active: 5 Started: 5 Finished: 0
label =    666 in 0:04:12 =    2.6/s Avg:  1531 Min:  1003 Max:  2020 Err:     0 (0.00%)
label +     86 in 0:00:30 =    2.9/s Avg:  1449 Min:  1004 Max:  2017 Err:     0 (0.00%) Active: 5 Started: 5 Finished: 0
label =    752 in 0:04:43 =    2.7/s Avg:  1522 Min:  1003 Max:  2020 Err:     0 (0.00%)
label +     65 in 0:00:24 =    2.7/s Avg:  1579 Min:  1007 Max:  2003 Err:     0 (0.00%) Active: 0 Started: 5 Finished: 5
label =    817 in 0:05:07 =    2.7/s Avg:  1526 Min:  1003 Max:  2020 Err:     0 (0.00%)
 The "label" is the name of the element. The "+" means that the line is a delta line, i.e. shows the changes since the last output. 

 The "=" means that the line is a total line, i.e. it shows the running total. 

 Entries in the JMeter log file also include time-stamps. The example "817 in 0:05:07 = 2.7/s" means that there were 817 samples recorded in 5 minutes and 7 seconds, and that works out at 2.7 samples per second. 

 The Avg (Average), Min (Minimum) and Max (Maximum) times are in milliseconds. 

 "Err" means number of errors (also shown as percentage). 

 The last two lines will appear at the end of a test. They will not be synchronised to the appropriate time boundary. Note that the initial and final deltas may be for less than the interval (in the example above this is 30 seconds). The first delta will generally be lower, as JMeter synchronizes to the interval boundary. The last delta will be lower, as the test will generally not finish on an exact interval boundary. 
The label is used to group sample results together. So if you have multiple Thread Groups and want to summarize across them all, then use the same label - or add the summariser to the Test Plan (so all thread groups are in scope). Different summary groupings can be implemented by using suitable labels and adding the summarisers to appropriate parts of the test plan.

 In CLI mode by default a Generate Summary Results listener named "summariser" is configured, if you have already added one to your Test Plan, ensure you name it differently otherwise results will be accumulated under this label (summary) leading to wrong results (sum of total samples + samples located under the Parent of Generate Summary Results listener). 

 This is not a bug but a design choice allowing to summarize across thread groups. 

[![Image 80: Screenshot for Control-Panel of Generate Summary Results](https://jmeter.apache.org/images/screenshots/summary.png)](https://jmeter.apache.org/images/screenshots/summary.png)

Screenshot of Control-Panel of Generate Summary Results

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Generate_Summary_Results_parms1 "Link to here")

Attribute

Description

Required

Name

 Descriptive name for this element that is shown in the tree. It appears as the "label" in the output. Details for all elements with the same label will be added together. 

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Comparison Assertion Visualizer[¶](https://jmeter.apache.org/usermanual/component_reference.html#Comparison_Assertion_Visualizer "Link to here")
------------------------------------------------------------------------------------------------------------------------------------------------

 The Comparison Assertion Visualizer shows the results of any [Compare Assertion](https://jmeter.apache.org/usermanual/component_reference.html#Compare_Assertion) elements. 

[![Image 81: Screenshot for Control-Panel of Comparison Assertion Visualizer](https://jmeter.apache.org/images/screenshots/comparison_assertion_visualizer.png)](https://jmeter.apache.org/images/screenshots/comparison_assertion_visualizer.png)

Screenshot of Control-Panel of Comparison Assertion Visualizer

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Comparison_Assertion_Visualizer_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree. 

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Backend Listener[¶](https://jmeter.apache.org/usermanual/component_reference.html#Backend_Listener "Link to here")
------------------------------------------------------------------------------------------------------------------

 The backend listener is an Asynchronous listener that enables you to plug custom implementations of [BackendListenerClient](https://jmeter.apache.org/api/org/apache/jmeter/visualizers/backend/BackendListenerClient.html). By default, a Graphite implementation is provided. 

[![Image 82: Screenshot for Control-Panel of Backend Listener](https://jmeter.apache.org/images/screenshots/backend_listener.png)](https://jmeter.apache.org/images/screenshots/backend_listener.png)

Screenshot of Control-Panel of Backend Listener

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Backend_Listener_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Yes

Backend Listener implementation

 Class of the BackendListenerClient implementation. 

Yes

Async Queue size

Size of the queue that holds the SampleResults while they are processed asynchronously.

Yes

Parameters

 Parameters of the BackendListenerClient implementation. 

Yes

The following parameters apply to the [GraphiteBackendListenerClient](https://jmeter.apache.org/api/org/apache/jmeter/visualizers/backend/graphite/GraphiteBackendListenerClient.html) implementation:

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Backend_Listener_parms2 "Link to here")

Attribute

Description

Required

graphiteMetricsSender

org.apache.jmeter.visualizers.backend.graphite.TextGraphiteMetricsSender or org.apache.jmeter.visualizers.backend.graphite.PickleGraphiteMetricsSender

Yes

graphiteHost

Graphite or InfluxDB (with Graphite plugin enabled) server host

Yes

graphitePort

 Graphite or InfluxDB (with Graphite plugin enabled) server port, defaults to 2003. Note PickleGraphiteMetricsSender (port 2004) can only talk to Graphite server. 

Yes

rootMetricsPrefix

 Prefix of metrics sent to backend. Defaults to "jmeter." Note that JMeter does not add a separator between the root prefix and the samplerName which is why the trailing dot is currently needed. 

Yes

summaryOnly

 Only send a summary with no detail. Defaults to true. 

Yes

samplersList

 Defines the names (labels) of sample results to be sent to the back end. If useRegexpForSamplersList=false this is a list of semi-colon separated names. If useRegexpForSamplersList=true this is a regular expression which will be matched against the names. 

Yes

useRegexpForSamplersList

 Consider samplersList as a regular expression to select the samplers for which you want to report metrics to backend. Defaults to false. 

Yes

percentiles

 The percentiles you want to send to the backend. A percentile may contain a fractional part, for example 12.5. (The separator is always ".") List must be semicolon separated. Generally 3 or 4 values should be sufficient. 

Yes

See also [Real-time results](https://jmeter.apache.org/usermanual/realtime-results.html) for more details.

[![Image 83: Grafana dashboard](https://jmeter.apache.org/images/screenshots/grafana_dashboard.png)](https://jmeter.apache.org/images/screenshots/grafana_dashboard.png)

Grafana dashboard

Since JMeter 3.2, an implementation that allows writing directly in InfluxDB with a custom schema. It is called InfluxdbBackendListenerClient. The following parameters apply to the [InfluxdbBackendListenerClient](https://jmeter.apache.org/api/org/apache/jmeter/visualizers/backend/influxdb/InfluxdbBackendListenerClient.html) implementation:

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Backend_Listener_parms3 "Link to here")

Attribute

Description

Required

influxdbMetricsSender

org.apache.jmeter.visualizers.backend.influxdb.HttpMetricsSender

Yes

influxdbUrl

 Influx URL (example: http://influxHost:8086/write?db=jmeter) 

Yes

influxdbToken

 InfluxDB 2 [authentication token](https://v2.docs.influxdata.com/v2.0/security/) (example: HE9yIdAPzWJDspH_tCc2UvdKZpX==); since 5.2. 

No

application

 Name of tested application. This value is stored in the 'events' measurement as a tag named 'application' 

Yes

measurement

 Measurement as per [Influx Line Protocol Reference](https://docs.influxdata.com/influxdb/v1.1/write_protocols/line_protocol_reference/). Defaults to "jmeter". 

Yes

summaryOnly

 Only send a summary with no detail. Defaults to true. 

Yes

samplersRegex

Regular expression which will be matched against the names of samples and sent to the back end.

Yes

testTitle

 Test name. Defaults to Test name. This value is stored in the 'events' measurement as a field named 'text'. JMeter generate automatically at the start and the end of the test an annotation with this value ending with ' started' and ' ended' 

Yes

eventTags

 Grafana allow to display tag for each annotation. You can fill them here. This value is stored in the 'events' measurement as a tag named 'tags'. 

No

percentiles

 The percentiles you want to send to the backend. A percentile may contain a fractional part, for example 12.5 (The separator is always "."). List must be semicolon separated. Generally three or four values should be sufficient. 

Yes

TAG_WhatEverYouWant

 You can add as many custom tags as you want. For each of them, create a new line and prefix its name by "TAG_" 

No

See also [Real-time results](https://jmeter.apache.org/usermanual/realtime-results.html) and [Influxdb annotations in Grafana](http://docs.grafana.org/reference/annotations/#influxdb-annotations) for more details. There is also a [subsection on configuring the listener for InfluxDB v2](https://jmeter.apache.org/usermanual/realtime-results.html#influxdb_v2).

Since JMeter 5.4, an implementation that writes all sample results to InfluxDB. It is called InfluxDBRawBackendListenerClient. It is worth noting that this will use more resources than the InfluxdbBackendListenerClient, both by JMeter and InfluxDB due to the increase in data and individual writes. The following parameters apply to the [InfluxDBRawBackendListenerClient](https://jmeter.apache.org/api/org/apache/jmeter/visualizers/backend/influxdb/InfluxDBRawBackendListenerClient.html) implementation:

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Backend_Listener_parms4 "Link to here")

Attribute

Description

Required

influxdbMetricsSender

org.apache.jmeter.visualizers.backend.influxdb.HttpMetricsSender

Yes

influxdbUrl

 Influx URL (e.g. http://influxHost:8086/write?db=jmeter or, for the cloud, https://eu-central-1-1.aws.cloud2.influxdata.com/api/v2/write?org=org-id&bucket=jmeter) 

Yes

influxdbToken

 InfluxDB 2 [authentication token](https://v2.docs.influxdata.com/v2.0/security/) (e.g. HE9yIdAPzWJDspH_tCc2UvdKZpX==) 

No

measurement

 Measurement as per [Influx Line Protocol Reference](https://docs.influxdata.com/influxdb/v1.7/write_protocols/line_protocol_reference/). Defaults to "jmeter." 

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

18.4 Configuration Elements[¶](https://jmeter.apache.org/usermanual/component_reference.html#config_elements "Link to here")
============================================================================================================================

 Configuration elements can be used to set up defaults and variables for later use by samplers. Note that these elements are processed at the start of the scope in which they are found, i.e. before any samplers in the same scope. 

CSV Data Set Config[¶](https://jmeter.apache.org/usermanual/component_reference.html#CSV_Data_Set_Config "Link to here")
------------------------------------------------------------------------------------------------------------------------

CSV Data Set Config is used to read lines from a file, and split them into variables. It is easier to use than the [__CSVRead()](https://jmeter.apache.org/usermanual/functions.html#__CSVRead) and [__StringFromFile()](https://jmeter.apache.org/usermanual/functions.html#__StringFromFile) functions. It is well suited to handling large numbers of variables, and is also useful for testing with "random" and unique values.

Generating unique random values at run-time is expensive in terms of CPU and memory, so just create the data in advance of the test. If necessary, the "random" data from the file can be used in conjunction with a run-time parameter to create different sets of values from each run - e.g. using concatenation - which is much cheaper than generating everything at run-time.

JMeter allows values to be quoted; this allows the value to contain a delimiter. If "allow quoted data" is enabled, a value may be enclosed in double-quotes. These are removed. To include double-quotes within a quoted field, use two double-quotes. For example:

1,"2,3","4""5" =>
1
2,3
4"5

JMeter supports CSV files which have a header line defining the column names. To enable this, leave the "Variable Names" field empty. The correct delimiter must be provided.

JMeter supports CSV files with quoted data that includes new-lines.

By default, the file is only opened once, and each thread will use a different line from the file. However the order in which lines are passed to threads depends on the order in which they execute, which may vary between iterations. Lines are read at the start of each test iteration. The file name and mode are resolved in the first iteration.

See the description of the Share mode below for additional options. If you want each thread to have its own set of values, then you will need to create a set of files, one for each thread. For example test1.csv, test2.csv, …, test _n_.csv. Use the filename test${__threadNum}.csv and set the "Sharing mode" to "Current thread".

 CSV Dataset variables are defined at the start of each test iteration. As this is after configuration processing is completed, they cannot be used for some configuration items - such as JDBC Config - that process their contents at configuration time (see [Bug 40394](https://bz.apache.org/bugzilla/show_bug.cgi?id=40394)) However the variables do work in the HTTP Auth Manager, as the username etc. are processed at run-time. 

As a special case, the string "\t" (without quotes) in the delimiter field is treated as a Tab.

When the end of file (EOF) is reached, and the recycle option is true, reading starts again with the first line of the file.

If the recycle option is false, and stopThread is false, then all the variables are set to <EOF> when the end of file is reached. This value can be changed by setting the JMeter property csvdataset.eofstring.

If the Recycle option is false, and Stop Thread is true, then reaching EOF will cause the thread to be stopped.

[![Image 84: Screenshot for Control-Panel of CSV Data Set Config](https://jmeter.apache.org/images/screenshots/csvdatasetconfig.png)](https://jmeter.apache.org/images/screenshots/csvdatasetconfig.png)

Screenshot of Control-Panel of CSV Data Set Config

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#CSV_Data_Set_Config_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Filename

 Name of the file to be read. **Relative file names are resolved with respect to the path of the active test plan.****For distributed testing, the CSV file must be stored on the server host system in the correct relative directory to where the JMeter server is started.** Absolute file names are also supported, but note that they are unlikely to work in remote mode, unless the remote server has the same directory structure. If the same physical file is referenced in two different ways - e.g. csvdata.txt and ./csvdata.txt - then these are treated as different files. If the OS does not distinguish between upper and lower case, csvData.TXT would also be opened separately. 

Yes

File Encoding

The encoding to be used to read the file, if not the platform default.

No

Variable Names

List of variable names. The names must be separated by the delimiter character. They can be quoted using double-quotes. JMeter supports CSV header lines: if the variable name field empty, then the first line of the file is read and interpreted as the list of column names. 

No

Use first line as Variable Names

 Ignore first line of CSV file, it will only be used if Variable Names is not empty, if Variable Names is empty the first line must contain the headers. 

No

Delimiter

Delimiter to be used to split the records in the file. If there are fewer values on the line than there are variables the remaining variables are not updated - so they will retain their previous value (if any).

Yes

Allow quoted data?

 Should the CSV file allow values to be quoted? If enabled, then values can be enclosed in " - double-quote - allowing values to contain a delimiter. 

Yes

Recycle on EOF?

 Should the file be re-read from the beginning on reaching EOF? (default is true) 

Yes

Stop thread on EOF?

 Should the thread be stopped on EOF, if Recycle is false? (default is false) 

Yes

Sharing mode

*   All threads - (the default) the file is shared between all the threads. 
*   Current thread group - each file is opened once for each thread group in which the element appears 
*   Current thread - each file is opened separately for each thread 
*   Identifier - all threads sharing the same identifier share the same file. So for example if you have 4 thread groups, you could use a common id for two or more of the groups to share the file between them. Or you could use the thread number to share the file between the same thread numbers in different thread groups. 

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

FTP Request Defaults[¶](https://jmeter.apache.org/usermanual/component_reference.html#FTP_Request_Defaults "Link to here")
--------------------------------------------------------------------------------------------------------------------------

[![Image 85: Screenshot for Control-Panel of FTP Request Defaults](https://jmeter.apache.org/images/screenshots/ftp-config/ftp-request-defaults.png)](https://jmeter.apache.org/images/screenshots/ftp-config/ftp-request-defaults.png)

Screenshot of Control-Panel of FTP Request Defaults

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

DNS Cache Manager[¶](https://jmeter.apache.org/usermanual/component_reference.html#DNS_Cache_Manager "Link to here")
--------------------------------------------------------------------------------------------------------------------

The DNS Cache Manager element allows to test applications, which have several servers behind load balancers (CDN, etc.), when user receives content from different IP's. By default JMeter uses JVM DNS cache. That's why only one server from the cluster receives load. DNS Cache Manager resolves names for each thread separately each iteration and saves results of resolving to its internal DNS Cache, which is independent from both JVM and OS DNS caches.

A mapping for static hosts can be used to simulate something like /etc/hosts file. These entries will be preferred over the custom resolver. Use custom DNS resolver has to be enabled, if you want to use this mapping.

 Usage of static host table[¶](https://jmeter.apache.org/usermanual/component_reference.html#static_host_table "Link to here")

Say, you have a test server, that you want to reach with a name, that is not (yet) set up in your DNS servers. For our example, this would be www.example.com for the server name, which you want to reach at the IP of the server a123.another.example.org.

You could change your workstation and add an entry to your /etc/hosts file - or the equivalent for your OS, or add an entry to the Static Host Table of the DNS Cache Manager.

You would type www.example.com into the first column (Host) and a123.another.example.org into the second column (Hostname or IP address). As the name of the second column implies, you could even use the IP address of your test server there.

The IP address for the test server will be looked up by using the custom DNS resolver. When none is given, the system DNS resolver will be used.

Now you can use www.example.com in your HTTPClient4 samplers and the requests will be made against a123.another.example.org with all headers set to www.example.com.

[![Image 86: Screenshot for Control-Panel of DNS Cache Manager](https://jmeter.apache.org/images/screenshots/dns-cache-manager.png)](https://jmeter.apache.org/images/screenshots/dns-cache-manager.png)

Screenshot of Control-Panel of DNS Cache Manager

DNS Cache Manager is designed for using in the root of Thread Group or Test Plan. Do not place it as child element of particular HTTP Sampler 

DNS Cache Manager works only with HTTP requests using HTTPClient4 implementation.

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#DNS_Cache_Manager_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree. 

No

Clear cache each Iteration

If selected, DNS cache of every Thread is cleared each time new iteration is started.

No

Use system DNS resolver

 System DNS resolver will be used. For correct work edit $JAVA_HOME/jre/lib/security/java.security and add networkaddress.cache.ttl=0

N/A

Use custom DNS resolver

Custom DNS resolver (from dnsjava library) will be used.

N/A

Hostname or IP address

List of DNS servers to use. If empty, network configuration DNS will used.

No

Add Button

Add an entry to the DNS servers table.

N/A

Delete Button

Delete the currently selected table entry.

N/A

Host and Hostname or IP address

Mapping of hostnames to a static host entry which will be resolved using the custom DNS resolver.

No

Add static host Button

Add an entry to the static hosts table.

N/A

Delete static host Button

Delete the currently selected static host in the table.

N/A

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

HTTP Authorization Manager[¶](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Authorization_Manager "Link to here")
--------------------------------------------------------------------------------------------------------------------------------------

The Authorization Manager lets you specify one or more user logins for web pages that are restricted using server authentication. You see this type of authentication when you use your browser to access a restricted page, and your browser displays a login dialog box. JMeter transmits the login information when it encounters this type of page.

The Authorization headers may not be shown in the Tree View Listener "Request" tab. The Java implementation does pre-emptive authentication, but it does not return the Authorization header when JMeter fetches the headers. The HttpComponents (HC 4.5.X) implementation defaults to pre-emptive since 3.2 and the header will be shown. To disable this, set the values as below, in which case authentication will only be performed in response to a challenge.

In the file jmeter.properties set httpclient4.auth.preemptive=false

 Note: the above settings only apply to the HttpClient sampler. 

 When looking for a match against a URL, JMeter checks each entry in turn, and stops when it finds the first match. Thus the most specific URLs should appear first in the list, followed by less specific ones. Duplicate URLs will be ignored. If you want to use different usernames/passwords for different threads, you can use variables. These can be set up using a [CSV Data Set Config](https://jmeter.apache.org/usermanual/component_reference.html#CSV_Data_Set_Config) Element (for example). 

[![Image 87: Screenshot for Control-Panel of HTTP Authorization Manager](https://jmeter.apache.org/images/screenshots/http-config/http-auth-manager.png)](https://jmeter.apache.org/images/screenshots/http-config/http-auth-manager.png)

Screenshot of Control-Panel of HTTP Authorization Manager

If there is more than one Authorization Manager in the scope of a Sampler, there is currently no way to specify which one is to be used.

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Authorization_Manager_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree. 

No

Clear auth on each iteration?

Used by Kerberos authentication. If checked, authentication will be done on each iteration of Main Thread Group loop even if it has already been done in a previous one. This is usually useful if each main thread group iteration represents behaviour of one Virtual User. 

Yes

Base URL

 A partial or complete URL that matches one or more HTTP Request URLs. As an example, say you specify a Base URL of "http://localhost/restricted/" with a Username of "jmeter" and a Password of "jmeter". If you send an HTTP request to the URL "http://localhost/restricted/ant/myPage.html", the Authorization Manager sends the login information for the user named, "jmeter". 

Yes

Username

The username to authorize.

Yes

Password

The password for the user. (N.B. this is stored unencrypted in the test plan)

Yes

Domain

The domain to use for NTLM.

No

Realm

The realm to use for NTLM.

No

Mechanism

 Type of authentication to perform. JMeter can perform different types of authentications based on used Http Samplers: Java BASIC HttpClient 4 BASIC, DIGEST and Kerberos

No

 The Realm only applies to the HttpClient sampler. 

**Kerberos Configuration:**
To configure Kerberos you need to setup at least two JVM system properties:

*   -Djava.security.krb5.conf=krb5.conf
*   -Djava.security.auth.login.config=jaas.conf

You can also configure those two properties in the file bin/system.properties. Look at the two sample configuration files (krb5.conf and jaas.conf) located in the JMeter bin folder for references to more documentation, and tweak them to match your Kerberos configuration.

Delegation of credentials is disabled by default for SPNEGO. If you want to enable it, you can do so by setting the property kerberos.spnego.delegate_cred to true.

When generating a SPN for Kerberos SPNEGO authentication IE and Firefox will omit the port number from the URL. Chrome has an option (--enable-auth-negotiate-port) to include the port number if it differs from the standard ones (80 and 443). That behavior can be emulated by setting the following JMeter property as below.

In jmeter.properties or user.properties, set:

*   kerberos.spnego.strip_port=false

**Controls:**
*   Add Button - Add an entry to the authorization table. 
*   Delete Button - Delete the currently selected table entry. 
*   Load Button - Load a previously saved authorization table and add the entries to the existing authorization table entries. 
*   Save As Button - Save the current authorization table to a file. 

When you save the Test Plan, JMeter automatically saves all of the authorization table entries - including any passwords, which are not encrypted.

 Authorization Example[¶](https://jmeter.apache.org/usermanual/component_reference.html#authorization_example "Link to here")

[Download](https://jmeter.apache.org/demos/AuthManagerTestPlan.jmx) this example. In this example, we created a Test Plan on a local server that sends three HTTP requests, two requiring a login and the other is open to everyone. See figure 10 to see the makeup of our Test Plan. On our server, we have a restricted directory named, "secret", which contains two files, "index.html" and "index2.html". We created a login id named, "kevin", which has a password of "spot". So, in our Authorization Manager, we created an entry for the restricted directory and a username and password (see figure 11). The two HTTP requests named "SecretPage1" and "SecretPage2" make requests to "/secret/index.html" and "/secret/index2.html". The other HTTP request, named "NoSecretPage" makes a request to "/index.html".

[![Image 88: Figure 10 - Test Plan](https://jmeter.apache.org/images/screenshots/http-config/auth-manager-example1a.png)](https://jmeter.apache.org/images/screenshots/http-config/auth-manager-example1a.png)

Figure 10 - Test Plan

[![Image 89: Figure 11 - Authorization Manager Control Panel](https://jmeter.apache.org/images/screenshots/http-config/auth-manager-example1b.png)](https://jmeter.apache.org/images/screenshots/http-config/auth-manager-example1b.png)

Figure 11 - Authorization Manager Control Panel

When we run the Test Plan, JMeter looks in the Authorization table for the URL it is requesting. If the Base URL matches the URL, then JMeter passes this information along with the request.

You can download the Test Plan, but since it is built as a test for our local server, you will not be able to run it. However, you can use it as a reference in constructing your own Test Plan.

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

HTTP Cache Manager[¶](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Cache_Manager "Link to here")
----------------------------------------------------------------------------------------------------------------------

The HTTP Cache Manager is used to add caching functionality to HTTP requests within its scope to simulate browser cache feature. Each Virtual User thread has its own Cache. By default, Cache Manager will store up to 5000 items in cache per Virtual User thread, using LRU algorithm. Use property "maxSize" to modify this value. Note that the more you increase this value the more HTTP Cache Manager will consume memory, so be sure to adapt the -Xmx JVM option accordingly.

If a sample is successful (i.e. has response code 2xx) then the Last-Modified and Etag (and Expired if relevant) values are saved for the URL. Before executing the next sample, the sampler checks to see if there is an entry in the cache, and if so, the If-Last-Modified and If-None-Match conditional headers are set for the request.

Additionally, if the "Use Cache-Control/Expires header" option is selected, then the Cache-Control/Expires value is checked against the current time. If the request is a GET request, and the timestamp is in the future, then the sampler returns immediately, without requesting the URL from the remote server. This is intended to emulate browser behaviour. Note that if Cache-Control header is "no-cache", the response will be stored in cache as pre-expired, so will generate a conditional GET request. If Cache-Control has any other value, the "max-age" expiry option is processed to compute entry lifetime, if missing then expire header will be used, if also missing entry will be cached as specified in [RFC 2616 section 13.2.4](https://tools.ietf.org/html/2616#section-13.2.4) using Last-Modified time and response Date.

 If the requested document has not changed since it was cached, then the response body will be empty. Likewise if the Expires date is in the future. This may cause problems for Assertions. 

[![Image 90: Screenshot for Control-Panel of HTTP Cache Manager](https://jmeter.apache.org/images/screenshots/http-config/http-cache-manager.png)](https://jmeter.apache.org/images/screenshots/http-config/http-cache-manager.png)

Screenshot of Control-Panel of HTTP Cache Manager

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Cache_Manager_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree. 

No

Clear cache each iteration

 If selected, then the cache is cleared at the start of the thread. 

Yes

Use Cache Control/Expires header when processing GET requests

See description above.

Yes

Max Number of elements in cache

See description above.

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

HTTP Cookie Manager[¶](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Cookie_Manager "Link to here")
------------------------------------------------------------------------------------------------------------------------

The Cookie Manager element has two functions: 

 First, it stores and sends cookies just like a web browser. If you have an HTTP Request and the response contains a cookie, the Cookie Manager automatically stores that cookie and will use it for all future requests to that particular web site. Each JMeter thread has its own "cookie storage area". So, if you are testing a web site that uses a cookie for storing session information, each JMeter thread will have its own session. Note that such cookies do not appear on the Cookie Manager display, but they can be seen using the [View Results Tree](https://jmeter.apache.org/usermanual/component_reference.html#View_Results_Tree) Listener.

JMeter checks that received cookies are valid for the URL. This means that cross-domain cookies are not stored. If you have bugged behaviour or want Cross-Domain cookies to be used, define the JMeter property "CookieManager.check.cookies=false".

Received Cookies can be stored as JMeter thread variables. To save cookies as variables, define the property "CookieManager.save.cookies=true". Also, cookies names are prefixed with "COOKIE_" before they are stored (this avoids accidental corruption of local variables) To revert to the original behaviour, define the property "CookieManager.name.prefix= " (one or more spaces). If enabled, the value of a cookie with the name TEST can be referred to as ${COOKIE_TEST}.

Second, you can manually add a cookie to the Cookie Manager. However, if you do this, the cookie will be shared by all JMeter threads.

Note that such Cookies are created with an Expiration time far in the future

Cookies with null values are ignored by default. This can be changed by setting the JMeter property: CookieManager.delete_null_cookies=false. Note that this also applies to manually defined cookies - any such cookies will be removed from the display when it is updated. Note also that the cookie name must be unique - if a second cookie is defined with the same name, it will replace the first.

[![Image 91: Screenshot for Control-Panel of HTTP Cookie Manager](https://jmeter.apache.org/images/screenshots/http-config/http-cookie-manager.png)](https://jmeter.apache.org/images/screenshots/http-config/http-cookie-manager.png)

Screenshot of Control-Panel of HTTP Cookie Manager

If there is more than one Cookie Manager in the scope of a Sampler, there is currently no way to specify which one is to be used. Also, a cookie stored in one cookie manager is not available to any other manager, so use multiple Cookie Managers with care.

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Cookie_Manager_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree. 

No

Clear Cookies each Iteration

If selected, all server-defined cookies are cleared each time the main Thread Group loop is executed. Any cookie defined in the GUI are not cleared.

Yes

Cookie Policy

 The cookie policy that will be used to manage the cookies. "standard" is the default since 3.0, and should work in most cases. See [Cookie specifications](https://hc.apache.org/httpcomponents-client-ga/tutorial/html/statemgmt.html#d5e515) and [CookieSpec implementations](http://hc.apache.org/httpcomponents-client-ga/httpclient/apidocs/org/apache/http/cookie/CookieSpec.html) [Note: "ignoreCookies" is equivalent to omitting the CookieManager.] 

Yes

Implementation

HC4CookieHandler (HttpClient 4.5.X API). Default is HC4CookieHandler since 3.0. 

_[Note: If you have a website to test with IPv6 address, choose HC4CookieHandler (IPv6 compliant)]_

Yes

User-Defined Cookies

 This gives you the opportunity to use hardcoded cookies that will be used by all threads during the test execution. 

 The "domain" is the hostname of the server (without http://); the port is currently ignored. 

No (discouraged, unless you know what you're doing)

Add Button

Add an entry to the cookie table.

N/A

Delete Button

Delete the currently selected table entry.

N/A

Load Button

Load a previously saved cookie table and add the entries to the existing cookie table entries.

N/A

Save As Button

 Save the current cookie table to a file (does not save any cookies extracted from HTTP Responses). 

N/A

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

HTTP Request Defaults[¶](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request_Defaults "Link to here")
----------------------------------------------------------------------------------------------------------------------------

This element lets you set default values that your HTTP Request controllers use. For example, if you are creating a Test Plan with 25 HTTP Request controllers and all of the requests are being sent to the same server, you could add a single HTTP Request Defaults element with the "Server Name or IP" field filled in. Then, when you add the 25 HTTP Request controllers, leave the "Server Name or IP" field empty. The controllers will inherit this field value from the HTTP Request Defaults element.

 All port values are treated equally; a sampler that does not specify a port will use the HTTP Request Defaults port, if one is provided. 

[![Image 92: Screenshot for Control-Panel of HTTP Request Defaults](https://jmeter.apache.org/images/screenshots/http-config/http-request-defaults.png)](https://jmeter.apache.org/images/screenshots/http-config/http-request-defaults.png)

Screenshot of Control-Panel of HTTP Request Defaults

[![Image 93: HTTP Request Advanced config fields](https://jmeter.apache.org/images/screenshots/http-config/http-request-defaults-advanced-tab.png)](https://jmeter.apache.org/images/screenshots/http-config/http-request-defaults-advanced-tab.png)

HTTP Request Advanced config fields

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request_Defaults_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Server

 Domain name or IP address of the web server. E.g. www.example.com. [Do not include the http:// prefix. 

No

Port

Port the web server is listening to.

No

Connect Timeout

Connection Timeout. Number of milliseconds to wait for a connection to open.

No

Response Timeout

Response Timeout. Number of milliseconds to wait for a response.

No

Implementation

Java, HttpClient4. If not specified the default depends on the value of the JMeter property jmeter.httpsampler, failing that, the Java implementation is used. 

No

Protocol

HTTP or HTTPS. 

No

Content encoding

The encoding to be used for the request.

No

Path

 The path to resource (for example, /servlets/myServlet). If the resource requires query string parameters, add them below in the "Send Parameters With the Request" section. Note that the path is the default for the full path, not a prefix to be applied to paths specified on the HTTP Request screens. 

No

Send Parameters With the Request

 The query string will be generated from the list of parameters you provide. Each parameter has a _name_ and _value_. The query string will be generated in the correct fashion, depending on the choice of "Method" you made (i.e. if you chose GET, the query string will be appended to the URL, if POST, then it will be sent separately). Also, if you are sending a file using a multipart form, the query string will be created using the multipart form specifications. 

No

Server (proxy)

 Hostname or IP address of a proxy server to perform request. [Do not include the http:// prefix.] 

No

Port

Port the proxy server is listening to.

No, unless proxy hostname is specified

Username

(Optional) username for proxy server.

No

Password

(Optional) password for proxy server. (N.B. this is stored unencrypted in the test plan)

No

Retrieve All Embedded Resources from HTML Files

Tell JMeter to parse the HTML file and send HTTP/HTTPS requests for all images, Java applets, JavaScript files, CSSs, etc. referenced in the file. 

No

Use concurrent pool

Use a pool of concurrent connections to get embedded resources.

No

Size

Pool size for concurrent connections used to get embedded resources.

No

URLs must match:

 If present, this must be a regular expression that is used to match against any embedded URLs found. So if you only want to download embedded resources from http://example.invalid/, use the expression: http://example\.invalid/.*

No

URLs must not match:

 If present, this must be a regular expression that is used to filter out any embedded URLs found. So if you don't want to download PNG or SVG files from any source, use the expression: .*\.(?i:svg|png)

No

 Note: radio buttons only have two states - on or off. This makes it impossible to override settings consistently - does off mean off, or does it mean use the current default? JMeter uses the latter (otherwise defaults would not work at all). So if the button is off, then a later element can set it on, but if the button is on, a later element cannot set it off. 

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

HTTP Header Manager[¶](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Header_Manager "Link to here")
------------------------------------------------------------------------------------------------------------------------

The Header Manager lets you add or override HTTP request headers.

**JMeter now supports multiple Header Managers**. The header entries are merged to form the list for the sampler. If an entry to be merged matches an existing header name, it replaces the previous entry. This allows one to set up a default set of headers, and apply adjustments to particular samplers. Note that an empty value for a header does not remove an existing header, it justs replace its value.

[![Image 94: Screenshot for Control-Panel of HTTP Header Manager](https://jmeter.apache.org/images/screenshots/http-config/http-header-manager.png)](https://jmeter.apache.org/images/screenshots/http-config/http-header-manager.png)

Screenshot of Control-Panel of HTTP Header Manager

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Header_Manager_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree. 

No

Name (Header)

 Name of the request header. Two common request headers you may want to experiment with are "User-Agent" and "Referer". 

No (You should have at least one, however)

Value

Request header value.

No (You should have at least one, however)

Add Button

Add an entry to the header table.

N/A

Delete Button

Delete the currently selected table entry.

N/A

Load Button

Load a previously saved header table and add the entries to the existing header table entries.

N/A

Save As Button

Save the current header table to a file.

N/A

 Header Manager example[¶](https://jmeter.apache.org/usermanual/component_reference.html#header_manager_example "Link to here")

[Download](https://jmeter.apache.org/demos/HeaderManagerTestPlan.jmx) this example. In this example, we created a Test Plan that tells JMeter to override the default "User-Agent" request header and use a particular Internet Explorer agent string instead. (see figures 12 and 13).

[![Image 95: Figure 12 - Test Plan](https://jmeter.apache.org/images/screenshots/http-config/header-manager-example1a.png)](https://jmeter.apache.org/images/screenshots/http-config/header-manager-example1a.png)

Figure 12 - Test Plan

[![Image 96: Figure 13 - Header Manager Control Panel](https://jmeter.apache.org/images/screenshots/http-config/header-manager-example1b.png)](https://jmeter.apache.org/images/screenshots/http-config/header-manager-example1b.png)

Figure 13 - Header Manager Control Panel

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Java Request Defaults[¶](https://jmeter.apache.org/usermanual/component_reference.html#Java_Request_Defaults "Link to here")
----------------------------------------------------------------------------------------------------------------------------

The Java Request Defaults component lets you set default values for Java testing. See the [Java Request](https://jmeter.apache.org/usermanual/component_reference.html#Java_Request).

[![Image 97: Screenshot for Control-Panel of Java Request Defaults](https://jmeter.apache.org/images/screenshots/java_defaults.png)](https://jmeter.apache.org/images/screenshots/java_defaults.png)

Screenshot of Control-Panel of Java Request Defaults

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

JDBC Connection Configuration[¶](https://jmeter.apache.org/usermanual/component_reference.html#JDBC_Connection_Configuration "Link to here")
--------------------------------------------------------------------------------------------------------------------------------------------

 Creates a database connection (used by [JDBC Request](https://jmeter.apache.org/usermanual/component_reference.html#JDBC_Request)Sampler) from the supplied JDBC Connection settings. The connection may be optionally pooled between threads. Otherwise each thread gets its own connection. The connection configuration name is used by the JDBC Sampler to select the appropriate connection. The used pool is DBCP, see [BasicDataSource Configuration Parameters](https://commons.apache.org/proper/commons-dbcp/configuration.html)

[![Image 98: Screenshot for Control-Panel of JDBC Connection Configuration](https://jmeter.apache.org/images/screenshots/jdbc-config/jdbc-conn-config.png)](https://jmeter.apache.org/images/screenshots/jdbc-config/jdbc-conn-config.png)

Screenshot of Control-Panel of JDBC Connection Configuration

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#JDBC_Connection_Configuration_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for the connection configuration that is shown in the tree.

No

Variable Name for created pool

 The name of the variable the connection is tied to. Multiple connections can be used, each tied to a different variable, allowing JDBC Samplers to select the appropriate connection. 

Each name must be different. If there are two configuration elements using the same name, only one will be saved. JMeter logs a message if a duplicate name is detected.

Yes

Max Number of Connections

 Maximum number of connections allowed in the pool. In most cases, **set this to zero (0)**. This means that each thread will get its own pool with a single connection in it, i.e. the connections are not shared between threads. 

 If you really want to use shared pooling (why?), then set the max count to the same as the number of threads to ensure threads don't wait on each other. 

Yes

Max Wait (ms)

 Pool throws an error if the timeout period is exceeded in the process of trying to retrieve a connection, see [BasicDataSource.html#getMaxWaitMillis](https://commons.apache.org/proper/commons-dbcp/api-2.1.1/org/apache/commons/dbcp2/BasicDataSource.html#getMaxWaitMillis--)

Yes

Time Between Eviction Runs (ms)

 The number of milliseconds to sleep between runs of the idle object evictor thread. When non-positive, no idle object evictor thread will be run. (Defaults to "60000", 1 minute). See [BasicDataSource.html#getTimeBetweenEvictionRunsMillis](https://commons.apache.org/proper/commons-dbcp/api-2.1.1/org/apache/commons/dbcp2/BasicDataSource.html#getTimeBetweenEvictionRunsMillis--)

Yes

Auto Commit

Turn auto commit on or off for the connections.

Yes

Transaction isolation

Transaction isolation level

Yes

Pool Prepared Statements

 Max number of Prepared Statements to pool per connection. "-1" disables the pooling and "0" means unlimited number of Prepared Statements to pool. (Defaults to "-1") 

Yes

Preinit Pool

 The connection pool can be initialized instantly. If set to False (default), the JDBC request samplers using this pool might measure higher response times for the first queries – as the connection establishment time for the whole pool is included. 

No

Init SQL statements separated by new line

A Collection of SQL statements that will be used to initialize physical connections when they are first created. These statements are executed only once - when the configured connection factory creates the connection. 

No

Test While Idle

 Test idle connections of the pool, see [BasicDataSource.html#getTestWhileIdle](https://commons.apache.org/proper/commons-dbcp/api-2.1.1/org/apache/commons/dbcp2/BasicDataSource.html#getTestWhileIdle--). Validation Query will be used to test it. 

Yes

Soft Min Evictable Idle Time(ms)

 Minimum amount of time a connection may sit idle in the pool before it is eligible for eviction by the idle object evictor, with the extra condition that at least minIdle connections remain in the pool. See [BasicDataSource.html#getSoftMinEvictableIdleTimeMillis](https://commons.apache.org/proper/commons-dbcp/api-2.1.1/org/apache/commons/dbcp2/BasicDataSource.html#getSoftMinEvictableIdleTimeMillis--). Defaults to 5000 (5 seconds) 

Yes

Validation Query

 A simple query used to determine if the database is still responding. This defaults to the 'isValid()' method of the jdbc driver, which is suitable for many databases. However some may require a different query; for example Oracle something like 'SELECT 1 FROM DUAL' could be used. 
The list of the validation queries can be configured with jdbc.config.check.query property and are by default:

hsqldb select 1 from INFORMATION_SCHEMA.SYSTEM_USERS Oracle select 1 from dual DB2 select 1 from sysibm.sysdummy1 MySQL or MariaDB select 1 Microsoft SQL Server (MS JDBC driver)select 1 PostgreSQL select 1 Ingres select 1 Derby values 1 H2 select 1 Firebird select 1 from rdb$database Exasol select 1

 The list come from [stackoverflow entry on different database validation queries](https://stackoverflow.com/questions/10684244/dbcp-validationquery-for-different-databases) and it can be incorrect 

 Note this validation query is used on pool creation to validate it even if "Test While Idle" suggests query would only be used on idle connections. This is DBCP behaviour. 

No

Database URL

JDBC Connection string for the database.

Yes

JDBC Driver class

 Fully qualified name of driver class. (Must be in JMeter's classpath - easiest to copy .jar file into JMeter's /lib directory). 
The list of the preconfigured jdbc driver classes can be configured with jdbc.config.jdbc.driver.class property and are by default:

hsqldb org.hsqldb.jdbc.JDBCDriver Oracle oracle.jdbc.OracleDriver DB2 com.ibm.db2.jcc.DB2Driver MySQL com.mysql.jdbc.Driver Microsoft SQL Server (MS JDBC driver)com.microsoft.sqlserver.jdbc.SQLServerDriver or com.microsoft.jdbc.sqlserver.SQLServerDriver PostgreSQL org.postgresql.Driver Ingres com.ingres.jdbc.IngresDriver Derby org.apache.derby.jdbc.ClientDriver H2 org.h2.Driver Firebird org.firebirdsql.jdbc.FBDriver Apache Derby org.apache.derby.jdbc.ClientDriver MariaDB org.mariadb.jdbc.Driver SQLite org.sqlite.JDBC Sybase AES net.sourceforge.jtds.jdbc.Driver Exasol com.exasol.jdbc.EXADriver

Yes

Username

Name of user to connect as.

No

Password

Password to connect with. (N.B. this is stored unencrypted in the test plan)

No

Connection Properties

 Connection Properties to set when establishing connection (like internal_logon=sysdba for Oracle for example) 

No

Different databases and JDBC drivers require different JDBC settings. The Database URL and JDBC Driver class are defined by the provider of the JDBC implementation.

Some possible settings are shown below. Please check the exact details in the JDBC driver documentation.

If JMeter reports No suitable driver, then this could mean either:

*    The driver class was not found. In this case, there will be a log message such as DataSourceElement: Could not load driver: {classname} java.lang.ClassNotFoundException: {classname}
*   The driver class was found, but the class does not support the connection string. This could be because of a syntax error in the connection string, or because the wrong classname was used.

If the database server is not running or is not accessible, then JMeter will report a java.net.ConnectException.

Some examples for databases and their parameters are given below.

MySQL Driver class com.mysql.jdbc.Driver Database URL jdbc:mysql://host[:port]/dbname PostgreSQL Driver class org.postgresql.Driver Database URL jdbc:postgresql:{dbname}Oracle Driver class oracle.jdbc.OracleDriver Database URL jdbc:oracle:thin:@//host:port/service OR jdbc:oracle:thin:@(description=(address=(host={mc-name})(protocol=tcp)(port={port-no}))(connect_data=(sid={sid})))Ingress (2006)Driver class ingres.jdbc.IngresDriver Database URL jdbc:ingres://host:port/db[;attr=value]Microsoft SQL Server (MS JDBC driver)Driver class com.microsoft.sqlserver.jdbc.SQLServerDriver Database URL jdbc:sqlserver://host:port;DatabaseName=dbname Apache Derby Driver class org.apache.derby.jdbc.ClientDriver Database URL jdbc:derby://server[:port]/databaseName[;URLAttributes=value[;…]]MariaDB Driver class org.mariadb.jdbc.Driver Database URL jdbc:mariadb://host[:port]/dbname[;URLAttributes=value[;…]] Exasol (see also [JDBC driver documentation](https://docs.exasol.com/connect_exasol/drivers/jdbc.htm)) Driver class com.exasol.jdbc.EXADriver Database URL jdbc:exa:host[:port][;schema=SCHEMA_NAME][;prop_x=value_x]

The above may not be correct - please check the relevant JDBC driver documentation.

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Keystore Configuration[¶](https://jmeter.apache.org/usermanual/component_reference.html#Keystore_Configuration "Link to here")
------------------------------------------------------------------------------------------------------------------------------

The Keystore Config Element lets you configure how Keystore will be loaded and which keys it will use. This component is typically used in HTTPS scenarios where you don't want to take into account keystore initialization into account in response time.

To use this element, you need to setup first a Java Key Store with the client certificates you want to test, to do that:

1.    Create your certificates either with Java keytool utility or through your PKI 
2.   If created by PKI, import your keys in Java Key Store by converting them to a format acceptable by JKS
3.    Then reference the keystore file through the two JVM properties (or add them in system.properties): 
    *   -Djavax.net.ssl.keyStore=path_to_keystore
    *   -Djavax.net.ssl.keyStorePassword=password_of_keystore

To use PKCS11 as the source for the store, you need to set javax.net.ssl.keyStoreType to PKCS11 and javax.net.ssl.keyStore to NONE.

[![Image 99: Screenshot for Control-Panel of Keystore Configuration](https://jmeter.apache.org/images/screenshots/keystore_config.png)](https://jmeter.apache.org/images/screenshots/keystore_config.png)

Screenshot of Control-Panel of Keystore Configuration

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Keystore_Configuration_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree. 

No

Preload

 Whether or not to preload Keystore. Setting it to true is usually the best option. 

Yes

Variable name holding certificate alias

 Variable name that will contain the alias to use for authentication by client certificate. Variable value will be filled from CSV Data Set for example. In the screenshot, "certificat_ssl" will also be a variable in CSV Data Set. Defaults to clientCertAliasVarName

False

Alias Start Index

The index of the first key to use in Keystore, 0-based.

Yes

Alias End Index

 The index of the last key to use in Keystore, 0-based. When using "Variable name holding certificate alias" ensure it is large enough so that all keys are loaded at startup. Default to -1 which means load all. 

Yes

 To make JMeter use more than one certificate you need to ensure that: 
*   https.use.cached.ssl.context=false is set in jmeter.properties or user.properties
*   You use HTTPClient 4 implementation for HTTP Request

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Login Config Element[¶](https://jmeter.apache.org/usermanual/component_reference.html#Login_Config_Element "Link to here")
--------------------------------------------------------------------------------------------------------------------------

The Login Config Element lets you add or override username and password settings in samplers that use username and password as part of their setup.

[![Image 100: Screenshot for Control-Panel of Login Config Element](https://jmeter.apache.org/images/screenshots/login-config.png)](https://jmeter.apache.org/images/screenshots/login-config.png)

Screenshot of Control-Panel of Login Config Element

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Login_Config_Element_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree. 

No

Username

The default username to use.

No

Password

The default password to use. (N.B. this is stored unencrypted in the test plan)

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

LDAP Request Defaults[¶](https://jmeter.apache.org/usermanual/component_reference.html#LDAP_Request_Defaults "Link to here")
----------------------------------------------------------------------------------------------------------------------------

The LDAP Request Defaults component lets you set default values for LDAP testing. See the [LDAP Request](https://jmeter.apache.org/usermanual/component_reference.html#LDAP_Request).

[![Image 101: Screenshot for Control-Panel of LDAP Request Defaults](https://jmeter.apache.org/images/screenshots/ldap_defaults.png)](https://jmeter.apache.org/images/screenshots/ldap_defaults.png)

Screenshot of Control-Panel of LDAP Request Defaults

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

LDAP Extended Request Defaults[¶](https://jmeter.apache.org/usermanual/component_reference.html#LDAP_Extended_Request_Defaults "Link to here")
----------------------------------------------------------------------------------------------------------------------------------------------

The LDAP Extended Request Defaults component lets you set default values for extended LDAP testing. See the [LDAP Extended Request](https://jmeter.apache.org/usermanual/component_reference.html#LDAP_Extended_Request).

[![Image 102: Screenshot for Control-Panel of LDAP Extended Request Defaults](https://jmeter.apache.org/images/screenshots/ldapext_defaults.png)](https://jmeter.apache.org/images/screenshots/ldapext_defaults.png)

Screenshot of Control-Panel of LDAP Extended Request Defaults

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

TCP Sampler Config[¶](https://jmeter.apache.org/usermanual/component_reference.html#TCP_Sampler_Config "Link to here")
----------------------------------------------------------------------------------------------------------------------

The TCP Sampler Config provides default data for the TCP Sampler

[![Image 103: Screenshot for Control-Panel of TCP Sampler Config](https://jmeter.apache.org/images/screenshots/tcpsamplerconfig.png)](https://jmeter.apache.org/images/screenshots/tcpsamplerconfig.png)

Screenshot of Control-Panel of TCP Sampler Config

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#TCP_Sampler_Config_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

TCPClient classname

 Name of the TCPClient class. Defaults to the property tcp.handler, failing that TCPClientImpl. 

No

ServerName or IP

Name or IP of TCP server

Port Number

Port to be used

Re-use connection

If selected, the connection is kept open. Otherwise it is closed when the data has been read.

Yes

Close connection

If selected, the connection will be closed after running the sampler.

Yes

SO_LINGER

 Enable/disable SO_LINGER with the specified linger time in seconds when a socket is created. If you set "SO_LINGER" value as 0, you may prevent large numbers of sockets sitting around with a TIME_WAIT status. 

No

End of line(EOL) byte value

 Byte value for end of line, set this to a value outside the range -128 to +127 to skip EOL checking. You may set this in jmeter.properties file as well with the tcp.eolByte property. If you set this in TCP Sampler Config and in jmeter.properties file at the same time, the setting value in the TCP Sampler Config will be used. 

No

Connect Timeout

Connect Timeout (milliseconds, 0 disables).

No

Response Timeout

Response Timeout (milliseconds, 0 disables).

No

Set Nodelay

Should the nodelay property be set?

Text to Send

Text to be sent

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

User Defined Variables[¶](https://jmeter.apache.org/usermanual/component_reference.html#User_Defined_Variables "Link to here")
------------------------------------------------------------------------------------------------------------------------------

The User Defined Variables element lets you define an **initial set of variables**, just as in the [Test Plan](https://jmeter.apache.org/usermanual/component_reference.html#Test_Plan).

 Note that all the UDV elements in a test plan - no matter where they are - are processed at the start. 

 So you cannot reference variables which are defined as part of a test run, e.g. in a Post-Processor. 
**UDVs should not be used with functions that generate different results each time they are called. Only the result of the first function call will be saved in the variable.** However, UDVs can be used with functions such as [__P()](https://jmeter.apache.org/usermanual/functions.html#__P), for example:

HOST      ${__P(host,localhost)}

which would define the variable "HOST" to have the value of the JMeter property "host", defaulting to "localhost" if not defined.

For defining variables during a test run, see [User Parameters](https://jmeter.apache.org/usermanual/component_reference.html#User_Parameters). UDVs are processed in the order they appear in the Plan, from top to bottom.

For simplicity, it is suggested that UDVs are placed only at the start of a Thread Group (or perhaps under the Test Plan itself).

Once the Test Plan and all UDVs have been processed, the resulting set of variables is copied to each thread to provide the initial set of variables.

If a runtime element such as a User Parameters Pre-Processor or Regular Expression Extractor defines a variable with the same name as one of the UDV variables, then this will replace the initial value, and all other test elements in the thread will see the updated value.

[![Image 104: Screenshot for Control-Panel of User Defined Variables](https://jmeter.apache.org/images/screenshots/user_defined_variables.png)](https://jmeter.apache.org/images/screenshots/user_defined_variables.png)

Screenshot of Control-Panel of User Defined Variables

 If you have more than one Thread Group, make sure you use different names for different values, as UDVs are shared between Thread Groups. Also, the variables are not available for use until after the element has been processed, so you cannot reference variables that are defined in the same element. You can reference variables defined in earlier UDVs or on the Test Plan. 

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#User_Defined_Variables_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

User Defined Variables

 Variable name/value pairs. The string under the "Name" column is what you'll need to place inside the brackets in ${…} constructs to use the variables later on. The whole ${…} will then be replaced by the string in the "Value" column. 

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Random Variable[¶](https://jmeter.apache.org/usermanual/component_reference.html#Random_Variable "Link to here")
----------------------------------------------------------------------------------------------------------------

The Random Variable Config Element is used to generate random numeric strings and store them in variable for use later. It's simpler than using [User Defined Variables](https://jmeter.apache.org/usermanual/component_reference.html#User_Defined_Variables) together with the [__Random()](https://jmeter.apache.org/usermanual/functions.html#__Random) function.

The output variable is constructed by using the random number generator, and then the resulting number is formatted using the format string. The number is calculated using the formula minimum+Random.nextInt(maximum-minimum+1). Random.nextInt() requires a positive integer. This means that maximum-minimum - i.e. the range - must be less than 2147483647, however the minimum and maximum values can be any long values so long as the range is OK.

As the random value is evaluated at the start of each iteration, it is probably not a good idea to use a variable other than a property as a value for the minimum or maximum. It would be zero on the first iteration.

[![Image 105: Screenshot for Control-Panel of Random Variable](https://jmeter.apache.org/images/screenshots/random_variable.png)](https://jmeter.apache.org/images/screenshots/random_variable.png)

Screenshot of Control-Panel of Random Variable

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Random_Variable_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Yes

Variable Name

The name of the variable in which to store the random string.

Yes

Format String

 The java.text.DecimalFormat format string to be used. For example "000" which will generate numbers with at least 3 digits, or "USER_000" which will generate output of the form USER_nnn. If not specified, the default is to generate the number using Long.toString()

No

Minimum Value

 The minimum value (long) of the generated random number. 

Yes

Maximum Value

 The maximum value (long) of the generated random number. 

Yes

Random Seed

 The seed for the random number generator. If you use the same seed value with Per Thread set to true, you will get the same value for each Thread as per [Random](http://docs.oracle.com/javase/8/docs/api/java/util/Random.html) class. If no seed is set, Default constructor of Random will be used. 

No

Per Thread(User)?

 If False, the generator is shared between all threads in the thread group. If True, then each thread has its own random generator. 

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Counter[¶](https://jmeter.apache.org/usermanual/component_reference.html#Counter "Link to here")
------------------------------------------------------------------------------------------------

Allows the user to create a counter that can be referenced anywhere in the Thread Group. The counter config lets the user configure a starting point, a maximum, and the increment. The counter will loop from the start to the max, and then start over with the start, continuing on like that until the test is ended.

The counter uses a long to store the value, so the range is from -2^63 to 2^63-1.

[![Image 106: Screenshot for Control-Panel of Counter](https://jmeter.apache.org/images/screenshots/counter.png)](https://jmeter.apache.org/images/screenshots/counter.png)

Screenshot of Control-Panel of Counter

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Counter_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Starting value

The starting value for the counter. The counter will equal this value during the first iteration (defaults to 0).

No

Increment

How much to increment the counter by after each iteration (defaults to 0, meaning no increment).

Yes

Maximum value

 If the counter exceeds the maximum, then it is reset to the Starting value. Default is Long.MAX_VALUE

No

Format

 Optional format, e.g. 000 will format as 001, 002, etc. This is passed to DecimalFormat, so any valid formats can be used. If there is a problem interpreting the format, then it is ignored. [The default format is generated using Long.toString()] 

No

Exported Variable Name

 This will be the variable name under which the counter value is available. If you name it counterA, you can then access it using ${counterA} as explained in [user-defined values](https://jmeter.apache.org/usermanual/functions.html) (By default, it creates an empty string variable that can be accessed using ${} but this is highly discouraged) 

No

Track Counter Independently for each User

 In other words, is this a global counter, or does each user get their own counter? If unchecked, the counter is global (i.e., user #1 will get value "1", and user #2 will get value "2" on the first iteration). If checked, each user has an independent counter. 

No

Reset counter on each Thread Group Iteration

 This option is only available when counter is tracked per User, if checked, counter will be reset to Start value on each Thread Group iteration. This can be useful when Counter is inside a Loop Controller. 

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Simple Config Element[¶](https://jmeter.apache.org/usermanual/component_reference.html#Simple_Config_Element "Link to here")
----------------------------------------------------------------------------------------------------------------------------

The Simple Config Element lets you add or override arbitrary values in samplers. You can choose the name of the value and the value itself. Although some adventurous users might find a use for this element, it's here primarily for developers as a basic GUI that they can use while developing new JMeter components.

[![Image 107: Screenshot for Control-Panel of Simple Config Element](https://jmeter.apache.org/images/screenshots/simple_config_element.png)](https://jmeter.apache.org/images/screenshots/simple_config_element.png)

Screenshot of Control-Panel of Simple Config Element

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Simple_Config_Element_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree. 

Yes

Parameter Name

The name of each parameter. These values are internal to JMeter's workings and are not generally documented. Only those familiar with the code will know these values.

Yes

Parameter Value

The value to apply to that parameter.

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

MongoDB Source Config (DEPRECATED)[¶](https://jmeter.apache.org/usermanual/component_reference.html#MongoDB_Source_Config_(DEPRECATED) "Link to here")
------------------------------------------------------------------------------------------------------------------------------------------------------

 Creates a MongoDB connection (used by [MongoDB Script](https://jmeter.apache.org/usermanual/component_reference.html#MongoDB_Script)Sampler) from the supplied Connection settings. Each thread gets its own connection. The connection configuration name is used by the JDBC Sampler to select the appropriate connection. 
You can then access com.mongodb.DB object in Beanshell or JSR223 Test Elements through the element [MongoDBHolder](https://jmeter.apache.org/api/org/apache/jmeter/protocol/mongodb/config/MongoDBHolder.html) using this code

import com.mongodb.DB;
import org.apache.jmeter.protocol.mongodb.config.MongoDBHolder;
DB db = MongoDBHolder.getDBFromSource("value of property MongoDB Source",
            "value of property Database Name");
…
    

[![Image 108: Screenshot for Control-Panel of MongoDB Source Config (DEPRECATED)](https://jmeter.apache.org/images/screenshots/mongodb-source-config.png)](https://jmeter.apache.org/images/screenshots/mongodb-source-config.png)

Screenshot of Control-Panel of MongoDB Source Config (DEPRECATED)

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#MongoDB_Source_Config_(DEPRECATED)_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for the connection configuration that is shown in the tree.

No

Server Address List

Mongo DB Servers

Yes

MongoDB Source

 The name of the variable the connection is tied to. 

Each name must be different. If there are two configuration elements using the same name, only one will be saved.

Yes

Keep Trying

 If true, the driver will keep trying to connect to the same server in case that the socket cannot be established. 

 There is maximum amount of time to keep retrying, which is 15s by default. 

 This can be useful to avoid some exceptions being thrown when a server is down temporarily by blocking the operations. 

 It can also be useful to smooth the transition to a new primary node (so that a new primary node is elected within the retry time). 

 Note that when using this flag 
*   for a replica set, the driver will try to connect to the old primary node for that time, instead of failing over to the new one right away 
*   this does not prevent exception from being thrown in read/write operations on the socket, which must be handled by application.

 Even if this flag is false, the driver already has mechanisms to automatically recreate broken connections and retry the read operations. 

 Default is false. 

No

Maximum connections per host

No

Connection timeout

 The connection timeout in milliseconds. 

 It is used solely when establishing a new connection Socket.connect(java.net.SocketAddress, int)

 Default is 0 and means no timeout. 

No

Maximum retry time

 The maximum amount of time in milliseconds to spend retrying to open connection to the same server. 

 Default is 0, which means to use the default 15s if autoConnectRetry is on. 

No

Maximum wait time

 The maximum wait time in milliseconds that a thread may wait for a connection to become available. 

 Default is 120,000. 

No

Socket timeout

 The socket timeout in milliseconds It is used for I/O socket read and write operations Socket.setSoTimeout(int)

 Default is 0 and means no timeout. 

No

Socket keep alive

 This flag controls the socket keep alive feature that keeps a connection alive through firewalls Socket.setKeepAlive(boolean)

 Default is false. 

No

ThreadsAllowedToBlockForConnectionMultiplier

 This multiplier, multiplied with the connectionsPerHost setting, gives the maximum number of threads that may be waiting for a connection to become available from the pool. 

 All further threads will get an exception right away. 

 For example if connectionsPerHost is 10 and threadsAllowedToBlockForConnectionMultiplier is 5, then up to 50 threads can wait for a connection. 

 Default is 5. 

No

Write Concern: Safe

 If true the driver will use a WriteConcern of WriteConcern.SAFE for all operations. 

 If w, wtimeout, fsync or j are specified, this setting is ignored. 

 Default is false. 

No

Write Concern: Fsync

 The fsync value of the global WriteConcern. 

 Default is false. 

No

Write Concern: Wait for Journal

 The j value of the global WriteConcern. 

 Default is false. 

No

Write Concern: Wait for servers

 The w value of the global WriteConcern. 

 Default is 0. 

No

Write Concern: Wait timeout

 The wtimeout value of the global WriteConcern. 

 Default is 0. 

No

Write Concern: Continue on error

 If batch inserts should continue after the first error 

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Bolt Connection Configuration[¶](https://jmeter.apache.org/usermanual/component_reference.html#Bolt_Connection_Configuration "Link to here")
--------------------------------------------------------------------------------------------------------------------------------------------

 Creates a Bolt connection pool (used by [Bolt Request](https://jmeter.apache.org/usermanual/component_reference.html#Bolt_Request) Sampler) from the supplied Connection settings. 

[![Image 109: Screenshot for Control-Panel of Bolt Connection Configuration](https://jmeter.apache.org/images/screenshots/bolt-connection-config.png)](https://jmeter.apache.org/images/screenshots/bolt-connection-config.png)

Screenshot of Control-Panel of Bolt Connection Configuration

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Bolt_Connection_Configuration_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Comments

Free text for additional details.

No

Bolt URI

The database URI.

Yes

Username

User account.

No

Password

User credentials.

No

Connection Pool Max Size

Max size of the Neo4j driver Bolt connection pool. Raise the value if running large number of concurrent threads, so that JMeter threads are not blocked waiting for a connection to be released to the pool.

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

18.5 Assertions[¶](https://jmeter.apache.org/usermanual/component_reference.html#assertions "Link to here")
===========================================================================================================

Assertions are used to perform additional checks on samplers, and are processed after **every sampler** in the same scope. To ensure that an Assertion is applied only to a particular sampler, add it as a child of the sampler.

 Note: Unless documented otherwise, Assertions are not applied to sub-samples (child samples) - only to the parent sample. In the case of JSR223 and BeanShell Assertions, the script can retrieve sub-samples using the method prev.getSubResults() which returns an array of SampleResults. The array will be empty if there are none. 

Assertions can be applied to either the main sample, the sub-samples or both. The default is to apply the assertion to the main sample only. If the Assertion supports this option, then there will be an entry on the GUI which looks like the following:

[![Image 110: Assertion Scope](https://jmeter.apache.org/images/screenshots/assertion/assertionscope.png)](https://jmeter.apache.org/images/screenshots/assertion/assertionscope.png)

Assertion Scope

 or the following [![Image 111: Assertion Scope](https://jmeter.apache.org/images/screenshots/assertion/assertionscopevar.png)](https://jmeter.apache.org/images/screenshots/assertion/assertionscopevar.png)

Assertion Scope

If a sub-sampler fails and the main sample is successful, then the main sample will be set to failed status and an Assertion Result will be added. If the JMeter variable option is used, it is assumed to relate to the main sample, and any failure will be applied to the main sample only.

 The variable JMeterThread.last_sample_ok is updated to "true" or "false" after all assertions for a sampler have been run. 

Response Assertion[¶](https://jmeter.apache.org/usermanual/component_reference.html#Response_Assertion "Link to here")
----------------------------------------------------------------------------------------------------------------------

The response assertion control panel lets you add pattern strings to be compared against various fields of the request or response. The pattern strings are:

*   Contains, Matches: Perl5-style regular expressions 
*   Equals, Substring: plain text, case-sensitive 

A summary of the pattern matching characters can be found at [ORO Perl5 regular expressions.](http://jakarta.apache.org/oro/api/org/apache/oro/text/regex/package-summary.html)

You can also choose whether the strings will be expected to **match** the entire response, or if the response is only expected to **contain** the pattern. You can attach multiple assertions to any controller for additional flexibility.

Note that the pattern string should not include the enclosing delimiters, i.e. use Price: \d+ not /Price: \d+/.

By default, the pattern is in multi-line mode, which means that the "." meta-character does not match newline. In multi-line mode, "^" and "$" match the start or end of any line anywhere within the string - not just the start and end of the entire string. Note that \s does match new-line. Case is also significant. To override these settings, one can use the _extended regular expression_ syntax. For example:

(?i)ignore case(?s) treat target as single line, i.e. "." matches new-line (?is)both the above These can be used anywhere within the expression and remain in effect until overridden. E.g. (?i)apple(?-i) Pie matches "ApPLe Pie", but not "ApPLe pIe" (?s)Apple.+?Pie matches Apple followed by Pie, which may be on a subsequent line. Apple(?s).+?Pie same as above, but it's probably clearer to use the (?s) at the start. 

[![Image 112: Screenshot for Control-Panel of Response Assertion](https://jmeter.apache.org/images/screenshots/assertion/assertion.png)](https://jmeter.apache.org/images/screenshots/assertion/assertion.png)

Screenshot of Control-Panel of Response Assertion

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Response_Assertion_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Apply to:

 This is for use with samplers that can generate sub-samples, e.g. HTTP Sampler with embedded resources, Mail Reader or samples generated by the Transaction Controller. 
*   Main sample only - only applies to the main sample 
*   Sub-samples only - only applies to the sub-samples 
*   Main sample and sub-samples - applies to both. 
*   JMeter Variable Name to use - assertion is to be applied to the contents of the named variable 

Yes

Field to Test

 Instructs JMeter which field of the Request or Response to test. 
*   Text Response - the response text from the server, i.e. the body, excluding any HTTP headers. 
*   Request data - the request text sent to the server, i.e. the body, excluding any HTTP headers. 
*   Response Code - e.g. 200
*   Response Message - e.g. OK
*   Response Headers, including Set-Cookie headers (if any) 
*   Request Headers
*   URL sampled
*   Document (text) - the extract text from various type of documents via Apache Tika (see [View Results Tree](https://jmeter.apache.org/usermanual/component_reference.html#View_Results_Tree) Document view section). 

Yes

Ignore status

 Instructs JMeter to set the status to success initially. 
The overall success of the sample is determined by combining the result of the assertion with the existing Response status. When the Ignore Status checkbox is selected, the Response status is forced to successful before evaluating the Assertion.

 HTTP Responses with statuses in the 4xx and 5xx ranges are normally regarded as unsuccessful. The "Ignore status" checkbox can be used to set the status successful before performing further checks. 

Note that this will have the effect of clearing any previous assertion failures, so make sure that this is only set on the first assertion.

Yes

Pattern Matching Rules

 Indicates how the text being tested is checked against the pattern. 
*   Contains - true if the text contains the regular expression pattern 
*   Matches - true if the whole text matches the regular expression pattern 
*   Equals - true if the whole text equals the pattern string (case-sensitive) 
*   Substring - true if the text contains the pattern string (case-sensitive) 

Equals and Substring patterns are plain strings, not regular expressions. NOT may also be selected to invert the result of the check. OR Apply each assertion in OR combination (if 1 pattern to test matches, Assertion will be ok) instead of AND (All patterns must match so that Assertion is OK). 

Yes

Patterns to Test

 A list of patterns to be tested. Each pattern is tested separately. If a pattern fails, then further patterns are not checked. There is no difference between setting up one Assertion with multiple patterns and setting up multiple Assertions with one pattern each (assuming the other options are the same). 

 However, when the Ignore Status checkbox is selected, this has the effect of cancelling any previous assertion failures - so make sure that the Ignore Status checkbox is only used on the first Assertion. 

Yes

Custom failure message

Lets you define the failure message that will replace the generated one 

No

The pattern is a Perl5-style regular expression, but without the enclosing brackets.

 Assertion Examples[¶](https://jmeter.apache.org/usermanual/component_reference.html#assertion_examples "Link to here")

[![Image 113: Figure 14 - Test Plan](https://jmeter.apache.org/images/screenshots/assertion/example1a.png)](https://jmeter.apache.org/images/screenshots/assertion/example1a.png)

Figure 14 - Test Plan

[![Image 114: Figure 15 - Assertion Control Panel with Pattern](https://jmeter.apache.org/images/screenshots/assertion/example1b.png)](https://jmeter.apache.org/images/screenshots/assertion/example1b.png)

Figure 15 - Assertion Control Panel with Pattern

[![Image 115: Figure 16 - Assertion Listener Results (Pass)](https://jmeter.apache.org/images/screenshots/assertion/example1c-pass.png)](https://jmeter.apache.org/images/screenshots/assertion/example1c-pass.png)

Figure 16 - Assertion Listener Results (Pass)

[![Image 116: Figure 17 - Assertion Listener Results (Fail)](https://jmeter.apache.org/images/screenshots/assertion/example1c-fail.png)](https://jmeter.apache.org/images/screenshots/assertion/example1c-fail.png)

Figure 17 - Assertion Listener Results (Fail)

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Duration Assertion[¶](https://jmeter.apache.org/usermanual/component_reference.html#Duration_Assertion "Link to here")
----------------------------------------------------------------------------------------------------------------------

The Duration Assertion tests that each response was received within a given amount of time. Any response that takes longer than the given number of milliseconds (specified by the user) is marked as a failed response.

[![Image 117: Screenshot for Control-Panel of Duration Assertion](https://jmeter.apache.org/images/screenshots/duration_assertion.png)](https://jmeter.apache.org/images/screenshots/duration_assertion.png)

Screenshot of Control-Panel of Duration Assertion

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Duration_Assertion_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Duration in Milliseconds

The maximum number of milliseconds each response is allowed before being marked as failed.

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Size Assertion[¶](https://jmeter.apache.org/usermanual/component_reference.html#Size_Assertion "Link to here")
--------------------------------------------------------------------------------------------------------------

The Size Assertion tests that each response contains the right number of bytes in it. You can specify that the size be equal to, greater than, less than, or not equal to a given number of bytes.

An empty response is treated as being 0 bytes rather than reported as an error.

[![Image 118: Screenshot for Control-Panel of Size Assertion](https://jmeter.apache.org/images/screenshots/size_assertion.png)](https://jmeter.apache.org/images/screenshots/size_assertion.png)

Screenshot of Control-Panel of Size Assertion

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Size_Assertion_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Apply to:

 This is for use with samplers that can generate sub-samples, e.g. HTTP Sampler with embedded resources, Mail Reader or samples generated by the Transaction Controller. 
*   Main sample only - assertion only applies to the main sample 
*   Sub-samples only - assertion only applies to the sub-samples 
*   Main sample and sub-samples - assertion applies to both. 
*   JMeter Variable Name to use - assertion is to be applied to the contents of the named variable 

Yes

Size in bytes

The number of bytes to use in testing the size of the response (or value of the JMeter variable).

Yes

Type of Comparison

Whether to test that the response is equal to, greater than, less than, or not equal to, the number of bytes specified.

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

XML Assertion[¶](https://jmeter.apache.org/usermanual/component_reference.html#XML_Assertion "Link to here")
------------------------------------------------------------------------------------------------------------

The XML Assertion tests that the response data consists of a formally correct XML document. It does not validate the XML based on a DTD or schema or do any further validation.

[![Image 119: Screenshot for Control-Panel of XML Assertion](https://jmeter.apache.org/images/screenshots/xml_assertion.png)](https://jmeter.apache.org/images/screenshots/xml_assertion.png)

Screenshot of Control-Panel of XML Assertion

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#XML_Assertion_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

BeanShell Assertion[¶](https://jmeter.apache.org/usermanual/component_reference.html#BeanShell_Assertion "Link to here")
------------------------------------------------------------------------------------------------------------------------

The BeanShell Assertion allows the user to perform assertion checking using a BeanShell script.

**For full details on using BeanShell, please see the [BeanShell website.](http://www.beanshell.org/)**

 Migration to [JSR223 Assertion](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_Assertion)+Groovy is highly recommended for performance, support of new Java features and limited maintenance of the BeanShell library. 

Note that a different Interpreter is used for each independent occurrence of the assertion in each thread in a test script, but the same Interpreter is used for subsequent invocations. This means that variables persist across calls to the assertion.

All Assertions are called from the same thread as the sampler.

If the property "beanshell.assertion.init" is defined, it is passed to the Interpreter as the name of a sourced file. This can be used to define common methods and variables. There is a sample init file in the bin directory: BeanShellAssertion.bshrc

The test element supports the ThreadListener and TestListener methods. These should be defined in the initialisation file. See the file BeanShellListeners.bshrc for example definitions.

[![Image 120: Screenshot for Control-Panel of BeanShell Assertion](https://jmeter.apache.org/images/screenshots/beanshell_assertion.png)](https://jmeter.apache.org/images/screenshots/beanshell_assertion.png)

Screenshot of Control-Panel of BeanShell Assertion

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#BeanShell_Assertion_parms1 "Link to here")

Attribute

Description

Required

Name

 Descriptive name for this element that is shown in the tree. The name is stored in the script variable Label

Reset bsh.Interpreter before each call

 If this option is selected, then the interpreter will be recreated for each sample. This may be necessary for some long running scripts. For further information, see [Best Practices - BeanShell scripting](https://jmeter.apache.org/usermanual/best-practices.html#bsh_scripting). 

Yes

Parameters

 Parameters to pass to the BeanShell script. The parameters are stored in the following variables: 
*   Parameters - string containing the parameters as a single variable 
*   bsh.args - String array containing parameters, split on white-space 

No

Script file

 A file containing the BeanShell script to run. This overrides the script. The file name is stored in the script variable FileName

No

Script

The BeanShell script to run. The return value is ignored.

Yes (unless script file is provided)

There's a [sample script](https://jmeter.apache.org/demos/BeanShellAssertion.bsh) you can try.

Before invoking the script, some variables are set up in the BeanShell interpreter. These are strings unless otherwise noted:

*   log - the [Logger](https://www.slf4j.org/api/org/slf4j/Logger.html) Object. (e.g.) log.warn("Message"[,Throwable])
*   SampleResult, prev - the [SampleResult](https://jmeter.apache.org/api/org/apache/jmeter/samplers/SampleResult.html) Object; read-write 
*   Response - the response Object; read-write 
*   Failure - boolean; read-write; used to set the Assertion status 
*   FailureMessage - String; read-write; used to set the Assertion message 
*   ResponseData - the response body (byte []) 
*   ResponseCode - e.g. 200
*   ResponseMessage - e.g. OK
*   ResponseHeaders - contains the HTTP headers 
*   RequestHeaders - contains the HTTP headers sent to the server 
*   SampleLabel
*   SamplerData - data that was sent to the server 
*   ctx - [JMeterContext](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterContext.html)
*   vars - [JMeterVariables](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterVariables.html) - e.g. vars.get("VAR1");
vars.put("VAR2","value");
vars.putObject("OBJ1",new Object());
*   props - JMeterProperties (class [java.util.Properties](https://docs.oracle.com/javase/8/docs/api/java/util/Properties.html)) - e.g. props.get("START.HMS");
props.put("PROP1","1234");

The following methods of the Response object may be useful:

*   setStopThread(boolean)
*   setStopTest(boolean)
*   String getSampleLabel()
*   setSampleLabel(String)

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

MD5Hex Assertion[¶](https://jmeter.apache.org/usermanual/component_reference.html#MD5Hex_Assertion "Link to here")
------------------------------------------------------------------------------------------------------------------

The MD5Hex Assertion allows the user to check the MD5 hash of the response data.

[![Image 121: Screenshot for Control-Panel of MD5Hex Assertion](https://jmeter.apache.org/images/screenshots/assertion/MD5HexAssertion.png)](https://jmeter.apache.org/images/screenshots/assertion/MD5HexAssertion.png)

Screenshot of Control-Panel of MD5Hex Assertion

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#MD5Hex_Assertion_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

MD5 sum

32 hex digits representing the MD5 hash (case not significant)

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

HTML Assertion[¶](https://jmeter.apache.org/usermanual/component_reference.html#HTML_Assertion "Link to here")
--------------------------------------------------------------------------------------------------------------

The HTML Assertion allows the user to check the HTML syntax of the response data using JTidy.

[![Image 122: Screenshot for Control-Panel of HTML Assertion](https://jmeter.apache.org/images/screenshots/assertion/HTMLAssertion.png)](https://jmeter.apache.org/images/screenshots/assertion/HTMLAssertion.png)

Screenshot of Control-Panel of HTML Assertion

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#HTML_Assertion_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

doctype

omit, auto, strict or loose

Yes

Format

HTML, XHTML or XML

Yes

Errors only

Only take note of errors?

Yes

Error threshold

Number of errors allowed before classing the response as failed

Yes

Warning threshold

Number of warnings allowed before classing the response as failed

Yes

Filename

Name of file to which report is written

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

XPath Assertion[¶](https://jmeter.apache.org/usermanual/component_reference.html#XPath_Assertion "Link to here")
----------------------------------------------------------------------------------------------------------------

The XPath Assertion tests a document for well formedness, has the option of validating against a DTD, or putting the document through JTidy and testing for an XPath. If that XPath exists, the Assertion is true. Using "/" will match any well-formed document, and is the default XPath Expression. The assertion also supports boolean expressions, such as "count(//*error)=2". See [http://www.w3.org/TR/xpath](http://www.w3.org/TR/xpath) for more information on XPath.

 Some sample expressions: 
*   //title[text()='Text to match'] - matches <title>Text to match</title> anywhere in the response 
*   /title[text()='Text to match'] - matches <title>Text to match</title> at root level in the response 

[![Image 123: Screenshot for Control-Panel of XPath2 Assertion](https://jmeter.apache.org/images/screenshots/xpath_assertion.png)](https://jmeter.apache.org/images/screenshots/xpath_assertion.png)

Screenshot of Control-Panel of XPath Assertion

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#XPath_Assertion_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Use Tidy (tolerant parser)

Use Tidy, i.e. be tolerant of XML/HTML errors

Yes

Quiet

Sets the Tidy Quiet flag

If Tidy is selected

Report Errors

If a Tidy error occurs, then set the Assertion accordingly

If Tidy is selected

Show warnings

Sets the Tidy showWarnings option

If Tidy is selected

Use Namespaces

Should namespaces be honoured? (see note below on NAMESPACES)

If Tidy is not selected

Validate XML

Check the document against its schema.

If Tidy is not selected

Ignore Whitespace

Ignore Element Whitespace.

If Tidy is not selected

Fetch External DTDs

If selected, external DTDs are fetched.

If Tidy is not selected

XPath Assertion

XPath to match in the document.

Yes

Invert assertion(will fail if above conditions met)

True if a XPath expression is not matched or returns false

No

 The non-tolerant parser can be quite slow, as it may need to download the DTD etc. 

**NAMESPACES**

 As a work-round for namespace limitations of the Xalan XPath parser (implementation on which JMeter is based) you need to: 
*    provide a Properties file (if for example your file is named namespaces.properties) which contains mappings for the namespace prefixes: 
prefix1=http\://foo.apache.org
prefix2=http\://toto.apache.org
…
*    reference this file in user.properties file using the property: xpath.namespace.config=namespaces.properties

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

XPath2 Assertion[¶](https://jmeter.apache.org/usermanual/component_reference.html#XPath2_Assertion "Link to here")
------------------------------------------------------------------------------------------------------------------

The XPath2 Assertion tests a document for well formedness. Using "/" will match any well-formed document, and is the default XPath2 Expression. The assertion also supports boolean expressions, such as "count(//*error)=2".

 Some sample expressions: 
*   //title[text()='Text to match'] - matches <title>Text to match</title> anywhere in the response 
*   /title[text()='Text to match'] - matches <title>Text to match</title> at root level in the response 

[![Image 124: Screenshot for Control-Panel of XPath2 Assertion](https://jmeter.apache.org/images/screenshots/xpath_assertion.png)](https://jmeter.apache.org/images/screenshots/xpath_assertion.png)

Screenshot of Control-Panel of XPath2 Assertion

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#XPath2_Assertion_parms1 "Link to here")

Attribute

Description

Required

Namespaces aliases list

 List of namespaces aliases you want to use to parse the document, one line per declaration. You must specify them as follow: prefix=namespace. This implementation makes it easier to use namespaces than with the old XPathExtractor version. 

No

XPath2 Assertion

XPath to match in the document.

Yes

Invert assertion

Will fail if xpath expression returns true or matches, succeed otherwise

No

Namespace aliases list

List of namespace aliases prefix=full namespace (one per line)

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

XML Schema Assertion[¶](https://jmeter.apache.org/usermanual/component_reference.html#XML_Schema_Assertion "Link to here")
--------------------------------------------------------------------------------------------------------------------------

The XML Schema Assertion allows the user to validate a response against an XML Schema.

[![Image 125: Screenshot for Control-Panel of XML Schema Assertion](https://jmeter.apache.org/images/screenshots/assertion/XMLSchemaAssertion.png)](https://jmeter.apache.org/images/screenshots/assertion/XMLSchemaAssertion.png)

Screenshot of Control-Panel of XML Schema Assertion

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#XML_Schema_Assertion_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

File Name

Specify XML Schema File Name

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

JSR223 Assertion[¶](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_Assertion "Link to here")
------------------------------------------------------------------------------------------------------------------

The JSR223 Assertion allows JSR223 script code to be used to check the status of the previous sample.

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_Assertion_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Language

The JSR223 language to be used

Yes

Parameters

 Parameters to pass to the script. The parameters are stored in the following variables: 
*   Parameters - string containing the parameters as a single variable 
*   args - String array containing parameters, split on white-space 

No

Script file

 A file containing the script to run, if a relative file path is used, then it will be relative to directory referenced by "user.dir" System property 

No

Script compilation caching

 Unique String across Test Plan that JMeter will use to cache result of Script compilation if language used supports [Compilable](https://docs.oracle.com/javase/8/docs/api/javax/script/Compilable.html) interface (Groovy is one of these, java, BeanShell and JavaScript are not) 

See note in JSR223 Sampler Java System property if you're using Groovy without checking this option

No

Script

The script to run.

Yes (unless script file is provided)

The following variables are set up for use by the script:

*   log - ([Logger](https://www.slf4j.org/api/org/slf4j/Logger.html)) - can be used to write to the log file 
*   Label - the String Label 
*   Filename - the script file name (if any) 
*   Parameters - the parameters (as a String) 
*   args - the parameters as a String array (split on whitespace) 
*   ctx - ([JMeterContext](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterContext.html)) - gives access to the context 
*   vars - ([JMeterVariables](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterVariables.html)) - gives read/write access to variables: 
vars.get(key);
vars.put(key,val);
vars.putObject("OBJ1",new Object());
vars.getObject("OBJ2");
*   props - (JMeterProperties - class [java.util.Properties](https://docs.oracle.com/javase/8/docs/api/java/util/Properties.html)) - e.g. 
props.get("START.HMS");
props.put("PROP1","1234");
*   SampleResult, prev - ([SampleResult](https://jmeter.apache.org/api/org/apache/jmeter/samplers/SampleResult.html)) - gives access to the previous SampleResult (if any) 
*   sampler - ([Sampler](https://jmeter.apache.org/api/org/apache/jmeter/samplers/Sampler.html)) - gives access to the current sampler 
*   OUT - System.out - e.g. OUT.println("message")
*   AssertionResult - ([AssertionResult](https://jmeter.apache.org/api/org/apache/jmeter/assertions/AssertionResult.html)) - the assertion result 

The script can check various aspects of the [SampleResult](https://jmeter.apache.org/api/org/apache/jmeter/samplers/SampleResult.html). If an error is detected, the script should use AssertionResult.setFailureMessage("message") and AssertionResult.setFailure(true).

For further details of all the methods available on each of the above variables, please check the Javadoc

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Compare Assertion[¶](https://jmeter.apache.org/usermanual/component_reference.html#Compare_Assertion "Link to here")
--------------------------------------------------------------------------------------------------------------------

 Compare Assertion **must not be used** during load test as it consumes a lot of resources (memory and CPU). Use it only for either functional testing or during Test Plan debugging and Validation. 

 The Compare Assertion can be used to compare sample results within its scope. Either the contents or the elapsed time can be compared, and the contents can be filtered before comparison. The assertion comparisons can be seen in the [Comparison Assertion Visualizer](https://jmeter.apache.org/usermanual/component_reference.html#Comparison_Assertion_Visualizer). 

[![Image 126: Screenshot for Control-Panel of Compare Assertion](https://jmeter.apache.org/images/screenshots/assertion/compare.png)](https://jmeter.apache.org/images/screenshots/assertion/compare.png)

Screenshot of Control-Panel of Compare Assertion

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Compare_Assertion_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Compare Content

Whether or not to compare the content (response data)

Yes

Compare Time

 If the value is ≥0, then check if the response time difference is no greater than the value. I.e. if the value is 0, then the response times must be exactly equal. 

Yes

Comparison Filters

 Filters can be used to remove strings from the content comparison. For example, if the page has a time-stamp, it might be matched with: "Time: \d\d:\d\d:\d\d" and replaced with a dummy fixed time "Time: HH:MM:SS". 

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

SMIME Assertion[¶](https://jmeter.apache.org/usermanual/component_reference.html#SMIME_Assertion "Link to here")
----------------------------------------------------------------------------------------------------------------

 The SMIME Assertion can be used to evaluate the sample results from the Mail Reader Sampler. This assertion verifies if the body of a mime message is signed or not. The signature can also be verified against a specific signer certificate. As this is a functionality that is not necessarily needed by most users, additional jars need to be downloaded and added to JMETER_HOME/lib: 

*   bcmail-xxx.jar (BouncyCastle SMIME/CMS) 
*   bcprov-xxx.jar (BouncyCastle Provider) 

 These need to be [downloaded from BouncyCastle.](http://www.bouncycastle.org/latest_releases.html)
If using the [Mail Reader Sampler](https://jmeter.apache.org/usermanual/component_reference.html#Mail_Reader_Sampler), please ensure that you select "Store the message using MIME (raw)" otherwise the Assertion won't be able to process the message correctly.

[![Image 127: Screenshot for Control-Panel of SMIME Assertion](https://jmeter.apache.org/images/screenshots/assertion/smime.png)](https://jmeter.apache.org/images/screenshots/assertion/smime.png)

Screenshot of Control-Panel of SMIME Assertion

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#SMIME_Assertion_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Verify Signature

 If selected, the assertion will verify if it is a valid signature according to the parameters defined in the Signer Certificate box. 

Yes

Message not signed

Whether or not to expect a signature in the message

Yes

Signer Certificate

 "No Check" means that it will not perform signature verification. "Check values" is used to verify the signature against the inputs provided. And "Certificate file" will perform the verification against a specific certificate file. 

Yes

Message Position

 The Mail sampler can retrieve multiple messages in a single sample. Use this field to specify which message will be checked. Messages are numbered from 0, so 0 means the first message. Negative numbers count from the LAST message; -1 means LAST, -2 means penultimate etc. 

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

JSON Assertion[¶](https://jmeter.apache.org/usermanual/component_reference.html#JSON_Assertion "Link to here")
--------------------------------------------------------------------------------------------------------------

This component allows you to perform validations of JSON documents. First, it will parse the JSON and fail if the data is not JSON. Second, it will search for specified path, using syntax from [Jayway JsonPath 1.2.0](https://github.com/json-path/JsonPath). If the path is not found, it will fail. Third, if JSON path was found in the document, and validation against expected value was requested, it will perform validation. For the null value there is special checkbox in the GUI. Note that if the path will return array object, it will be iterated and if expected value is found, the assertion will succeed. To validate empty array use [] string. Also, if patch will return dictionary object, it will be converted to string before comparison.

 When using [indefinite JSON Paths](https://github.com/json-path/JsonPath#what-is-returned-when) you must assert the value due to the existing JSON library implementation, otherwise the assertion could always return successful. 

 Since JMeter version 5.5 the assertion will fail, if an indefinite path is given, an empty list is extracted and no assertion value is set. 

[![Image 128: Screenshot for Control-Panel of JSON Assertion](https://jmeter.apache.org/images/screenshots/assertion/json_assertion.png)](https://jmeter.apache.org/images/screenshots/assertion/json_assertion.png)

Screenshot of Control-Panel of JSON Assertion

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#JSON_Assertion_parms1 "Link to here")

Attribute

Description

Required

Assert JSON Path exists

Path to JSON element for assert.

Yes

Additionally assert value

Select checkbox if you want make assert with some value

No

Match as regular expression

Select checkbox if you want use regular expression

No

Expected Value

Value for assert or regular expression for match

No

Expect null

Select checkbox if you expect null

No

Invert assertion (will fail if above conditions met)

Invert assertion (will fail if above conditions met)

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

JSON JMESPath Assertion[¶](https://jmeter.apache.org/usermanual/component_reference.html#JSON_JMESPath_Assertion "Link to here")
--------------------------------------------------------------------------------------------------------------------------------

This component allows you to perform assertion on JSON documents content using [JMESPath](http://jmespath.org/). First, it will parse the JSON and fail if the data is not JSON. 

 Second, it will search for specified path, using JMESPath syntax. 

 If the path is not found, it will fail. 

 Third, if JMES path was found in the document, and validation against expected value was requested, it will perform this additional check. If you want to check for nullity, use the Expect null checkbox. 

 Note that the path cannot be null as the expression JMESPath will not be compiled and an error will occur. Even if you expect an empty or null response, you must put a valid JMESPath expression.

[![Image 129: Screenshot for Control-Panel of JSON JMESPath Assertion](https://jmeter.apache.org/images/screenshots/assertion/jmespath_assertion.png)](https://jmeter.apache.org/images/screenshots/assertion/jmespath_assertion.png)

Screenshot of Control-Panel of JSON JMESPath Assertion

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#JSON_JMESPath_Assertion_parms1 "Link to here")

Attribute

Description

Required

Assert JMESPath exists

Check that JMESPath to JSON element exists

Yes

Additionally assert value

Select checkbox if you check the extracted JMESPath against an expected one

No

Match as regular expression

Select checkbox if you want to use a regular expression for matching

No

Expected Value

 Value to use for exact matching or regular expression if Match as regular expression is checked 

No

Expect null

Select checkbox if you expect the value to be null

No

Invert assertion (will fail if above conditions met)

Invert assertion (will fail if above conditions met)

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

18.6 Timers[¶](https://jmeter.apache.org/usermanual/component_reference.html#timers "Link to here")
===================================================================================================

 Since version 3.1, a new feature (in Beta mode as of JMeter 3.1 and subject to changes) has been implemented which provides the following feature. 

 You can apply a multiplication factor on the sleep delays computed by Random timer by setting property timer.factor=float number where float number is a decimal positive number. 

 JMeter will multiply this factor by the computed sleep delay. This feature can be used by: 
*   [Gaussian Random Timer](https://jmeter.apache.org/usermanual/component_reference.html#Gaussian_Random_Timer)
*   [Poisson Random Timer](https://jmeter.apache.org/usermanual/component_reference.html#Poisson_Random_Timer)
*   [Uniform Random Timer](https://jmeter.apache.org/usermanual/component_reference.html#Uniform_Random_Timer)

 Note that timers are processed **before** each sampler in the scope in which they are found; if there are several timers in the same scope, **all** the timers will be processed **before each** sampler. 

 Timers are only processed in conjunction with a sampler. A timer which is not in the same scope as a sampler will not be processed at all. 

 To apply a timer to a single sampler, add the timer as a child element of the sampler. The timer will be applied before the sampler is executed. To apply a timer after a sampler, either add it to the next sampler, or add it as the child of a [Flow Control Action](https://jmeter.apache.org/usermanual/component_reference.html#Flow_Control_Action) Sampler. 

Constant Timer[¶](https://jmeter.apache.org/usermanual/component_reference.html#Constant_Timer "Link to here")
--------------------------------------------------------------------------------------------------------------

If you want to have each thread pause for the same amount of time between requests, use this timer.

[![Image 130: Screenshot for Control-Panel of Constant Timer](https://jmeter.apache.org/images/screenshots/timers/constant_timer.png)](https://jmeter.apache.org/images/screenshots/timers/constant_timer.png)

Screenshot of Control-Panel of Constant Timer

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Constant_Timer_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this timer that is shown in the tree.

No

Thread Delay

Number of milliseconds to pause.

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Gaussian Random Timer[¶](https://jmeter.apache.org/usermanual/component_reference.html#Gaussian_Random_Timer "Link to here")
----------------------------------------------------------------------------------------------------------------------------

This timer pauses each thread request for a random amount of time, with most of the time intervals occurring near a particular value. The total delay is the sum of the Gaussian distributed value (with mean 0.0 and standard deviation 1.0) times the deviation value you specify, and the offset value. Another way to explain it, in Gaussian Random Timer, the variation around constant offset has a Gaussian curve distribution.

[![Image 131: Screenshot for Control-Panel of Gaussian Random Timer](https://jmeter.apache.org/images/screenshots/timers/gauss_random_timer.png)](https://jmeter.apache.org/images/screenshots/timers/gauss_random_timer.png)

Screenshot of Control-Panel of Gaussian Random Timer

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Gaussian_Random_Timer_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this timer that is shown in the tree

No

Deviation

Deviation in milliseconds.

Yes

Constant Delay Offset

Number of milliseconds to pause in addition to the random delay.

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Uniform Random Timer[¶](https://jmeter.apache.org/usermanual/component_reference.html#Uniform_Random_Timer "Link to here")
--------------------------------------------------------------------------------------------------------------------------

This timer pauses each thread request for a random amount of time, with each time interval having the same probability of occurring. The total delay is the sum of the random value and the offset value.

[![Image 132: Screenshot for Control-Panel of Uniform Random Timer](https://jmeter.apache.org/images/screenshots/timers/uniform_random_timer.png)](https://jmeter.apache.org/images/screenshots/timers/uniform_random_timer.png)

Screenshot of Control-Panel of Uniform Random Timer

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Uniform_Random_Timer_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this timer that is shown in the tree. 

No

Random Delay Maximum

Maximum random number of milliseconds to pause.

Yes

Constant Delay Offset

Number of milliseconds to pause in addition to the random delay.

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Constant Throughput Timer[¶](https://jmeter.apache.org/usermanual/component_reference.html#Constant_Throughput_Timer "Link to here")
------------------------------------------------------------------------------------------------------------------------------------

This timer introduces variable pauses, calculated to keep the total throughput (in terms of samples per minute) as close as possible to a given figure. Of course the throughput will be lower if the server is not capable of handling it, or if other timers or time-consuming test elements prevent it.

N.B. although the Timer is called the Constant Throughput timer, the throughput value does not need to be constant. It can be defined in terms of a variable or function call, and the value can be changed during a test. The value can be changed in various ways:

*   using a counter variable
*    using a __jexl3, __groovy function to provide a changing value 
*   using the remote BeanShell server to change a JMeter property

See [Best Practices](https://jmeter.apache.org/usermanual/best-practices.html) for further details.

 Note that the throughput value should not be changed too often during a test - it will take a while for the new value to take effect. 

[![Image 133: Screenshot for Control-Panel of Constant Throughput Timer](https://jmeter.apache.org/images/screenshots/timers/constant_throughput_timer.png)](https://jmeter.apache.org/images/screenshots/timers/constant_throughput_timer.png)

Screenshot of Control-Panel of Constant Throughput Timer

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Constant_Throughput_Timer_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this timer that is shown in the tree. 

No

Target Throughput

Throughput we want the timer to try to generate.

Yes

Calculate Throughput based on

*   this thread only - each thread will try to maintain the target throughput. The overall throughput will be proportional to the number of active threads. 
*   all active threads in current thread group - the target throughput is divided amongst all the active threads in the group. Each thread will delay as needed, based on when it last ran. 
*   all active threads - the target throughput is divided amongst all the active threads in all Thread Groups. Each thread will delay as needed, based on when it last ran. In this case, each other Thread Group will need a Constant Throughput timer with the same settings. 
*   all active threads in current thread group (shared) - as above, but each thread is delayed based on when any thread in the group last ran. 
*   all active threads (shared) - as above; each thread is delayed based on when any thread last ran. 

Yes

The shared and non-shared algorithms both aim to generate the desired throughput, and will produce similar results. 

 The shared algorithm should generate a more accurate overall transaction rate. 

 The non-shared algorithm should generate a more even spread of transactions across threads.

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Precise Throughput Timer[¶](https://jmeter.apache.org/usermanual/component_reference.html#Precise_Throughput_Timer "Link to here")
----------------------------------------------------------------------------------------------------------------------------------

This timer introduces variable pauses, calculated to keep the total throughput (e.g. in terms of samples per minute) as close as possible to a given figure. The timer does not generate threads, so the resulting throughput will be lower if the server is not capable of handling it, or if other timers add too big delays, or if there's not enough threads, or time-consuming test elements prevent it.

Note: in many cases, Open Model Thread Group would be a better choice for generating the desired load profile

Note: if you alter timer configuration on the fly, then it might take time to adapt to the new settings. For instance, if the timer was initially configured for 1 request per hour, then it assigns incoming threads with 3600+sec pauses. Then, if the load configuration is altered to 1 per second, then the threads are not interrupted from their delays, and the threads keep waiting.

Although the Timer is called Precise Throughput Timer, it does not aim to produce precisely the same number of samples over one-second intervals during the test.

The timer works best for rates under 36000 requests/hour, however your mileage might vary (see monitoring section below if your goals are vastly different).

#### Best location of a Precise Throughput Timer in a Test Plan

As you might know, the timers are inherited by all the siblings and their child elements. That is why one of the best places for Precise Throughput Timer is under the first element in a test loop. For instance, you might add a dummy sampler at the beginning, and place the timer under that dummy sampler

#### Produced schedule

Precise Throughput Timer models [Poisson arrivals](https://en.wikipedia.org/wiki/Poisson_point_process) schedule. That schedule often happens in a real-life, so it makes sense to use that for load testing. For instance, it naturally might generate samples that are close together thus it might reveal concurrency issues. Even if you manage to generate Poisson arrivals with [Poisson Random Timer](https://jmeter.apache.org/usermanual/component_reference.html#Poisson_Random_Timer), it would be susceptible to the issues listed below. For instance, true Poisson arrivals might have indefinitely long pause, and that is not practical for load testing. For instance, "regular" Poisson arrivals with 1 per second rate might end up with 50 samples over 60 second long test.

[Constant Throughput Timer](https://jmeter.apache.org/usermanual/component_reference.html#Constant_Throughput_Timer) converges to the specified rate, however it tends to produce samples at even intervals.

#### Ramp-up and startup spike

You might used "ramp-up" or similar approaches to avoid a spike at the test start. For instance, if you configure [Thread Group](https://jmeter.apache.org/usermanual/component_reference.html#Thread_Group) to have 100 threads, and set Ramp-up Period to 0 (or to a small number), then all the threads would start at the same time, and it would produce an unwanted spike of the load. On top of that, if you set Ramp-up Period too high, it might result in "_too few_" threads being available at the very beginning to achieve the required load.

Precise Throughput Timer schedules executions in a random way, so it can be used to generate constant load, and it is recommended to set both Ramp-up Period and Delay to 0.

#### Multiple thread groups starting at the same time

A variation of Ramp-up issue might appear when [Test Plan](https://jmeter.apache.org/usermanual/component_reference.html#Test_Plan) includes multiple [Thread Group](https://jmeter.apache.org/usermanual/component_reference.html#Thread_Group)s. To mitigate that issue one typically adds "random" delay to each [Thread Group](https://jmeter.apache.org/usermanual/component_reference.html#Thread_Group) so threads start at different times.

Precise Throughput Timer avoids that issue since it schedules executions in a random way. You do not need to add extra random delays to mitigate startup spike

#### Number of iterations per hour

One of the basic requirements is to issue N samples per M minutes. Let it be 60 iterations per hour. Business customers would not understand if you report load test results with 57 executions "just because the random was random". In order to generate 60 iterations per hour, you need to configure as follows (other parameters could be left with their default values)

*   Target throughput (samples): 60 
*   Throughput period (seconds): 3600 
*   Test duration (seconds): 3600 

The first two options set the throughput. Even though 60/3600, 30/1800, and 120/7200 represent exactly the same load level, pick the one that represents business requirements better. For instance, if the requirement is to test for "60 sample per hour", then set 60/3600. If the requirement is to test "1 sample per minute", then set 1/60.

Test duration (seconds) is there so the timer ensures exact number of samples for a given test duration. Precise Throughput Timer creates a schedule for the samples at the test startup. For instance, if you wish to perform 5 minutes test with 60 per hour throughput, you would set Test duration (seconds) to 300. This enables to configure throughput in a business-friendly way. Note: Test duration (seconds) does **not** limit test duration. It is just a hint for the timer.

#### Number of threads and think times

One of the common pitfalls is to adjust number of threads and think times in order to end up with the desired throughput. Even though it might work, that approach results in lots of time spent on the test runs. It might require to adjust threads and delays again when new application version arrives.

Precise Throughput Timer enables to set throughput goal and go for it no matter how well application performs. In order to do that, Precise Throughput Timer creates a schedule at the test startup, then it uses that schedule to release threads. The main driver for the think times and number of threads should be business requirements, not the desire to match throughput somehow.

For instance, if you application is used by support engineers in a call center. Suppose there are 2 engineers in the call center, and the target throughput is 1 per minute. Suppose it takes 4 minutes for the engineer to read and review the web page. For that case you should set 2 threads in the group, use 4 minutes for think time delays, and specify 1 per minute in Precise Throughput Timer. Of course it would result in something around 2samples/4minutes=0.5 per minute and the result of such a test means "you need more support engineers in a call center" or "you need to reduce the time it takes an engineer to fulfill a task".

#### Testing low rates and repeatable tests

Testing at low rates (e.g. 60 per hour) requires to know the desired test profile. For instance, if you need to inject load at even intervals (e.g. 60 seconds in between) then you'd better use [Constant Throughput Timer](https://jmeter.apache.org/usermanual/component_reference.html#Constant_Throughput_Timer). However, if you need to have randomized schedule (e.g. to model real users that execute reports), then Precise Throughput Timer is your friend.

When comparing outcomes of multiple load tests, it is useful to be able to repeat exactly the same test profile. For instance, if action X (e.g. "Profit Report") is invoked after 5 minutes of the test start, then it would be nice to replicate that pattern for subsequent test executions. Replicating the same load pattern simplifies analysis of the test results (e.g. CPU% chart).

Random seed (change from 0 to random) enables to control the seed value that is used by Precise Throughput Timer. By default it is initialized with 0 and that means random seed is used for each test execution. If you need to have repeatable load pattern, then change Random seed so some random value. The general advice is to use non-zero seed, and "0 by default" is an implementation limit.

Note: when using multiple thread groups with same throughput rates and same non-zero seed it might result in unwanted firing the samples at the same time.

#### Testing high rates and/or long test durations

Precise Throughput Timer generates the schedule and keeps it in memory. In most cases it should not be a problem, however, remember that you might want to keep the schedule shorter than 1'000'000 samples. It takes ~200ms to generate a schedule for 1'000'000 samples, and the schedule consumes 8 megabytes in the heap. Schedule for 10 million entries takes 1-2 second to build and it consumes 80 megabytes in the heap.

For instance, if you want to perform 2-week long test with 5'000 per hour rate, then you probably want to have exactly 5'000 samples for each hour. You can set Test duration (seconds) property of the timer of the timer to 1 hour. Then the timer would create a schedule of 5'000 samples for an hour, and when the schedule is exhausted, the timer would generate a schedule for the next hour.

At the same time, you can set Test duration (seconds) to 2 weeks, and the timer would generate a schedule with 168'000 samples = 2 weeks * 5'000 samples/hour = 2*7*24*500. The schedule would take ~30ms to generate, and it would consume a little more than 1 megabyte.

#### Bursty load

There might be a case when all the samples should come in pairs, triples, etc. Certain cases might be solved via [Synchronizing Timer](https://jmeter.apache.org/usermanual/component_reference.html#Synchronizing_Timer), however Precise Throughput Timer has native way to issue requests in packs. This behavior is disabled by default, and it is controlled with "Batched departures" settings

*   Number of threads in the batch (threads). Specifies the number of samples in a batch. Note the overall number of samples will still be in line with Target Throughput
*   Delay between threads in the batch (ms). For instance, if set to 42, and the batch size is 3, then threads will depart at x, x+42ms, x+84ms 

#### Variable load rate

Even though property values (e.g. throughput) can be defined via expressions, it is recommended to keep the value more or less the same through the test, as it takes time to recompute the new schedule to adapt new values.

#### Monitoring

As next schedule is generated, Precise Throughput Timer logs a message to jmeter.log: 2018-01-04 17:34:03,635 INFO o.a.j.t.ConstantPoissonProcessGenerator: Generated 21 timings (... 20 required, rate 1.0, duration 20, exact lim 20000, i21) in 0 ms. First 15 events will be fired at: 1.1869653574244292 (+1.1869653574244292), 1.4691340403043207 (+0.2821686828798915), 3.638151706179226 (+2.169017665874905), 3.836357090410566 (+0.19820538423134026), 4.709330071408575 (+0.8729729809980085), 5.61330076999953 (+0.903970698590955), ... This shows that schedule generation took 0ms, and it shows absolute timestamps in seconds. In the case above, the rate was set to be 1 per second, and the actual timestamps became 1.2 sec, 1.5 sec, 3.6 sec, 3.8 sec, 4.7 sec, and so on.

[![Image 134: Screenshot for Control-Panel of Precise Throughput Timer](https://jmeter.apache.org/images/screenshots/timers/precise_throughput_timer.png)](https://jmeter.apache.org/images/screenshots/timers/precise_throughput_timer.png)

Screenshot of Control-Panel of Precise Throughput Timer

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Precise_Throughput_Timer_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this timer that is shown in the tree

No

Target throughput (in samples per 'throughput period')

Maximum number of samples you want to obtain per "throughput period", including all threads in group, from all affected samplers.

Yes

Throughput period (seconds)

Throughput period. For example, if "throughput" is set to 42 and "throughput period" to 21 sec, then you'll get 2 samples per second.

Yes

Test duration (seconds)

This is used to ensure you'll get throughput*duration samples during "test duration" timeframe.

Yes

Number of threads in the batch (threads)

If the value exceeds 1, then multiple threads depart from the timer simultaneously. Average throughput still meets "throughput" value.

Yes

Delay between threads in the batch (ms)

For instance, if set to 42, and the batch size is 3, then threads will depart at x, x+42ms, x+84ms.

Yes

Random seed (change from 0 to random)

Note: different timers should better have different seed values. Constant seed ensures timer generates the same delays each test start. The value of "0" means the timer is truly random (non-repeatable from one execution to another)..

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Synchronizing Timer[¶](https://jmeter.apache.org/usermanual/component_reference.html#Synchronizing_Timer "Link to here")
------------------------------------------------------------------------------------------------------------------------

The purpose of the SyncTimer is to block threads until X number of threads have been blocked, and then they are all released at once. A SyncTimer can thus create large instant loads at various points of the test plan.

[![Image 135: Screenshot for Control-Panel of Synchronizing Timer](https://jmeter.apache.org/images/screenshots/timers/sync_timer.png)](https://jmeter.apache.org/images/screenshots/timers/sync_timer.png)

Screenshot of Control-Panel of Synchronizing Timer

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Synchronizing_Timer_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this timer that is shown in the tree. 

No

Number of Simultaneous Users to Group by

 Number of threads to release at once. Setting it to 0 is equivalent to setting it to Number of threads in Thread Group. 

Yes

Timeout in milliseconds

 If set to 0, Timer will wait for the number of threads to reach the value in "Number of Simultaneous Users to Group". If superior to 0, then timer will wait at max "Timeout in milliseconds" for the number of Threads. If after the timeout interval the number of users waiting is not reached, timer will stop waiting. Defaults to 0

No

 If timeout in milliseconds is set to 0 and number of threads never reaches "Number of Simultaneous Users to Group by" then Test will pause infinitely. Only a forced stop will stop it. Setting Timeout in milliseconds is an option to consider in this case. 

 Synchronizing timer blocks only within one JVM, so if using Distributed testing ensure you never set "Number of Simultaneous Users to Group by" to a value superior to the number of users of its containing Thread group considering 1 injector only. 

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

BeanShell Timer[¶](https://jmeter.apache.org/usermanual/component_reference.html#BeanShell_Timer "Link to here")
----------------------------------------------------------------------------------------------------------------

The BeanShell Timer can be used to generate a delay.

**For full details on using BeanShell, please see the [BeanShell website.](http://www.beanshell.org/)**

 Migration to [JSR223 Timer](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_Timer)+Groovy is highly recommended for performance, support of new Java features and limited maintenance of the BeanShell library. 

The test element supports the ThreadListener and TestListener methods. These should be defined in the initialisation file. See the file BeanShellListeners.bshrc for example definitions.

[![Image 136: Screenshot for Control-Panel of BeanShell Timer](https://jmeter.apache.org/images/screenshots/timers/beanshell_timer.png)](https://jmeter.apache.org/images/screenshots/timers/beanshell_timer.png)

Screenshot of Control-Panel of BeanShell Timer

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#BeanShell_Timer_parms1 "Link to here")

Attribute

Description

Required

Name

 Descriptive name for this element that is shown in the tree. The name is stored in the script variable Label

No

Reset bsh.Interpreter before each call

 If this option is selected, then the interpreter will be recreated for each sample. This may be necessary for some long running scripts. For further information, see [Best Practices - BeanShell scripting](https://jmeter.apache.org/usermanual/best-practices.html#bsh_scripting). 

Yes

Parameters

 Parameters to pass to the BeanShell script. The parameters are stored in the following variables: 
*   Parameters - string containing the parameters as a single variable 
*   bsh.args - String array containing parameters, split on white-space 

No

Script file

 A file containing the BeanShell script to run. The file name is stored in the script variable FileName The return value is used as the number of milliseconds to wait. 

No

Script

 The BeanShell script. The return value is used as the number of milliseconds to wait. 

Yes (unless script file is provided)

Before invoking the script, some variables are set up in the BeanShell interpreter:

*   log - ([Logger](https://www.slf4j.org/api/org/slf4j/Logger.html)) - can be used to write to the log file 
*   ctx - ([JMeterContext](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterContext.html)) - gives access to the context 
*   vars - ([JMeterVariables](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterVariables.html)) - gives read/write access to variables: 
vars.get(key);
vars.put(key,val);
vars.putObject("OBJ1",new Object());
*   props - (JMeterProperties - class java.util.Properties) - e.g. props.get("START.HMS");props.put("PROP1","1234");
*   prev - ([SampleResult](https://jmeter.apache.org/api/org/apache/jmeter/samplers/SampleResult.html)) - gives access to the previous SampleResult (if any) 

For details of all the methods available on each of the above variables, please check the Javadoc

If the property beanshell.timer.init is defined, this is used to load an initialisation file, which can be used to define methods etc. for use in the BeanShell script.

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

JSR223 Timer[¶](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_Timer "Link to here")
----------------------------------------------------------------------------------------------------------

The JSR223 Timer can be used to generate a delay using a JSR223 scripting language,

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_Timer_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

ScriptLanguage

 The scripting language to be used. 

Yes

Parameters

 Parameters to pass to the script. The parameters are stored in the following variables: 
*   Parameters - string containing the parameters as a single variable 
*   args - String array containing parameters, split on white-space 

No

Script file

 A file containing the script to run, if a relative file path is used, then it will be relative to directory referenced by "user.dir" System property The return value is converted to a long integer and used as the number of milliseconds to wait. 

No

Script compilation caching

 Unique String across Test Plan that JMeter will use to cache result of Script compilation if language used supports [Compilable](https://docs.oracle.com/javase/8/docs/api/javax/script/Compilable.html) interface (Groovy is one of these, java, beanshell and javascript are not) 

See note in JSR223 Sampler Java System property if you're using Groovy without checking this option

No

Script

 The script. The return value is used as the number of milliseconds to wait. 

Yes (unless script file is provided)

Before invoking the script, some variables are set up in the script interpreter:

*   log - ([Logger](https://www.slf4j.org/api/org/slf4j/Logger.html)) - can be used to write to the log file 
*   ctx - ([JMeterContext](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterContext.html)) - gives access to the context 
*   vars - ([JMeterVariables](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterVariables.html)) - gives read/write access to variables: vars.get(key);
vars.put(key,val);
vars.putObject("OBJ1",new Object());
*   props - (JMeterProperties - class java.util.Properties) - e.g. props.get("START.HMS");props.put("PROP1","1234");
*   sampler - ([Sampler](https://jmeter.apache.org/api/org/apache/jmeter/samplers/Sampler.html)) - the current Sampler 
*   Label - the name of the Timer 
*   FileName - the file name (if any) 
*   OUT - System.out 

For details of all the methods available on each of the above variables, please check the Javadoc

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Poisson Random Timer[¶](https://jmeter.apache.org/usermanual/component_reference.html#Poisson_Random_Timer "Link to here")
--------------------------------------------------------------------------------------------------------------------------

This timer pauses each thread request for a random amount of time, with most of the time intervals occurring near a particular value. The total delay is the sum of the Poisson distributed value, and the offset value.

Note: if you want to model Poisson arrivals, consider using [Precise Throughput Timer](https://jmeter.apache.org/usermanual/component_reference.html#Precise_Throughput_Timer) instead.

[![Image 137: Screenshot for Control-Panel of Poisson Random Timer](https://jmeter.apache.org/images/screenshots/timers/poisson_random_timer.png)](https://jmeter.apache.org/images/screenshots/timers/poisson_random_timer.png)

Screenshot of Control-Panel of Poisson Random Timer

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Poisson_Random_Timer_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this timer that is shown in the tree

No

Lambda

Lambda value in milliseconds.

Yes

Constant Delay Offset

Number of milliseconds to pause in addition to the random delay.

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

18.7 Pre Processors[¶](https://jmeter.apache.org/usermanual/component_reference.html#preprocessors "Link to here")
==================================================================================================================

 Preprocessors are used to modify the Samplers in their scope. 

HTML Link Parser[¶](https://jmeter.apache.org/usermanual/component_reference.html#HTML_Link_Parser "Link to here")
------------------------------------------------------------------------------------------------------------------

This modifier parses HTML response from the server and extracts links and forms. A URL test sample that passes through this modifier will be examined to see if it "matches" any of the links or forms extracted from the immediately previous response. It would then replace the values in the URL test sample with appropriate values from the matching link or form. Perl-type regular expressions are used to find matches.

[![Image 138: Screenshot for Control-Panel of HTML Link Parser](https://jmeter.apache.org/images/screenshots/html_link_parser.png)](https://jmeter.apache.org/images/screenshots/html_link_parser.png)

Screenshot of Control-Panel of HTML Link Parser

 Matches are performed using protocol, host, path and parameter names. The target sampler cannot contain parameters that are not in the response links. 

 If using distributed testing, ensure you switch mode (see jmeter.properties) so that it's not a stripping one, see [Bug 56376](https://bz.apache.org/bugzilla/show_bug.cgi?id=56376)

 Spidering Example[¶](https://jmeter.apache.org/usermanual/component_reference.html#spider_example "Link to here")

Consider a simple example: let's say you wanted JMeter to "spider" through your site, hitting link after link parsed from the HTML returned from your server (this is not actually the most useful thing to do, but it serves as a good example). You would create a [Simple Controller](https://jmeter.apache.org/usermanual/component_reference.html#Simple_Controller), and add the "HTML Link Parser" to it. Then, create an HTTP Request, and set the domain to ".*", and the path likewise. This will cause your test sample to match with any link found on the returned pages. If you wanted to restrict the spidering to a particular domain, then change the domain value to the one you want. Then, only links to that domain will be followed.

 Poll Example[¶](https://jmeter.apache.org/usermanual/component_reference.html#poll_example "Link to here")

A more useful example: given a web polling application, you might have a page with several poll options as radio buttons for the user to select. Let's say the values of the poll options are very dynamic - maybe user generated. If you wanted JMeter to test the poll, you could either create test samples with hardcoded values chosen, or you could let the HTML Link Parser parse the form, and insert a random poll option into your URL test sample. To do this, follow the above example, except, when configuring your Web Test controller's URL options, be sure to choose "POST" as the method. Put in hard-coded values for the domain, path, and any additional form parameters. Then, for the actual radio button parameter, put in the name (let's say it's called "poll_choice"), and then ".*" for the value of that parameter. When the modifier examines this URL test sample, it will find that it "matches" the poll form (and it shouldn't match any other form, given that you've specified all the other aspects of the URL test sample), and it will replace your form parameters with the matching parameters from the form. Since the regular expression ".*" will match with anything, the modifier will probably have a list of radio buttons to choose from. It will choose at random, and replace the value in your URL test sample. Each time through the test, a new random value will be chosen.

[![Image 139: Figure 18 - Online Poll Example](https://jmeter.apache.org/images/screenshots/modification.png)](https://jmeter.apache.org/images/screenshots/modification.png)

Figure 18 - Online Poll Example

One important thing to remember is that you must create a test sample immediately prior that will return an HTML page with the links and forms that are relevant to your dynamic test sample.

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

HTTP URL Re-writing Modifier[¶](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_URL_Re-writing_Modifier "Link to here")
------------------------------------------------------------------------------------------------------------------------------------------

This modifier works similarly to the HTML Link Parser, except it has a specific purpose for which it is easier to use than the HTML Link Parser, and more efficient. For web applications that use URL Re-writing to store session ids instead of cookies, this element can be attached at the ThreadGroup level, much like the [HTTP Cookie Manager](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Cookie_Manager). Simply give it the name of the session id parameter, and it will find it on the page and add the argument to every request of that ThreadGroup.

Alternatively, this modifier can be attached to select requests and it will modify only them. Clever users will even determine that this modifier can be used to grab values that elude the [HTML Link Parser](https://jmeter.apache.org/usermanual/component_reference.html#HTML_Link_Parser).

[![Image 140: Screenshot for Control-Panel of HTTP URL Re-writing Modifier](https://jmeter.apache.org/images/screenshots/url_rewriter.png)](https://jmeter.apache.org/images/screenshots/url_rewriter.png)

Screenshot of Control-Panel of HTTP URL Re-writing Modifier

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_URL_Re-writing_Modifier_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name given to this element in the test tree.

No

Session Argument Name

The name of the parameter to grab from previous response. This modifier will find the parameter anywhere it exists on the page, and grab the value assigned to it, whether it's in an HREF or a form.

Yes

Path Extension

Some web apps rewrite URLs by appending a semi-colon plus the session id parameter. Check this box if that is so.

No

Do not use equals in path extension

 Some web apps rewrite URLs without using an "=" sign between the parameter name and value (such as Intershop Enfinity). 

No

Do not use questionmark in path extension

Prevents the query string to end up in the path extension (such as Intershop Enfinity).

No

Cache Session Id?

 Should the value of the session Id be saved for later use when the session Id is not present? 

Yes

URL Encode

 URL Encode value when writing parameter 

No

 If using distributed testing, ensure you switch mode (see jmeter.properties) so that it's not a stripping one, see [Bug 56376](https://bz.apache.org/bugzilla/show_bug.cgi?id=56376). 

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

User Parameters[¶](https://jmeter.apache.org/usermanual/component_reference.html#User_Parameters "Link to here")
----------------------------------------------------------------------------------------------------------------

Allows the user to specify values for User Variables specific to individual threads.

User Variables can also be specified in the Test Plan but not specific to individual threads. This panel allows you to specify a series of values for any User Variable. For each thread, the variable will be assigned one of the values from the series in sequence. If there are more threads than values, the values get re-used. For example, this can be used to assign a distinct user id to be used by each thread. User variables can be referenced in any field of any JMeter Component.

The variable is specified by clicking the Add Variable button in the bottom of the panel and filling in the Variable name in the 'Name:' column. To add a new value to the series, click the 'Add User' button and fill in the desired value in the newly added column.

Values can be accessed in any test component in the same thread group, using the [function syntax](https://jmeter.apache.org/usermanual/functions.html): ${variable}.

See also the [CSV Data Set Config](https://jmeter.apache.org/usermanual/component_reference.html#CSV_Data_Set_Config) element, which is more suitable for large numbers of parameters

[![Image 141: Screenshot for Control-Panel of User Parameters](https://jmeter.apache.org/images/screenshots/user_params.png)](https://jmeter.apache.org/images/screenshots/user_params.png)

Screenshot of Control-Panel of User Parameters

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#User_Parameters_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Update Once Per Iteration

 A flag to indicate whether the User Parameters element should update its variables only once per iteration. if you embed functions into the UP, then you may need greater control over how often the values of the variables are updated. Keep this box checked to ensure the values are updated each time through the UP's parent controller. Uncheck the box, and the UP will update the parameters for every sample request made within its [scope](https://jmeter.apache.org/usermanual/test_plan.html#scoping_rules). 

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

BeanShell PreProcessor[¶](https://jmeter.apache.org/usermanual/component_reference.html#BeanShell_PreProcessor "Link to here")
------------------------------------------------------------------------------------------------------------------------------

The BeanShell PreProcessor allows arbitrary code to be applied before taking a sample.

**For full details on using BeanShell, please see the [BeanShell website.](http://www.beanshell.org/)**

 Migration to [JSR223 PreProcessor](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_PreProcessor)+Groovy is highly recommended for performance, support of new Java features and limited maintenance of the BeanShell library. 

The test element supports the ThreadListener and TestListener methods. These should be defined in the initialisation file. See the file BeanShellListeners.bshrc for example definitions.

[![Image 142: Screenshot for Control-Panel of BeanShell PreProcessor](https://jmeter.apache.org/images/screenshots/beanshell_preprocessor.png)](https://jmeter.apache.org/images/screenshots/beanshell_preprocessor.png)

Screenshot of Control-Panel of BeanShell PreProcessor

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#BeanShell_PreProcessor_parms1 "Link to here")

Attribute

Description

Required

Name

 Descriptive name for this element that is shown in the tree. The name is stored in the script variable Label

No

Reset bsh.Interpreter before each call

 If this option is selected, then the interpreter will be recreated for each sample. This may be necessary for some long running scripts. For further information, see [Best Practices - BeanShell scripting](https://jmeter.apache.org/usermanual/best-practices.html#bsh_scripting). 

Yes

Parameters

 Parameters to pass to the BeanShell script. The parameters are stored in the following variables: 
*   Parameters - string containing the parameters as a single variable 
*   bsh.args - String array containing parameters, split on white-space 

No

Script file

 A file containing the BeanShell script to run. The file name is stored in the script variable FileName

No

Script

The BeanShell script. The return value is ignored.

Yes (unless script file is provided)

Before invoking the script, some variables are set up in the BeanShell interpreter:

*   log - ([Logger](https://www.slf4j.org/api/org/slf4j/Logger.html)) - can be used to write to the log file 
*   ctx - ([JMeterContext](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterContext.html)) - gives access to the context 
*   vars - ([JMeterVariables](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterVariables.html)) - gives read/write access to variables: vars.get(key);
vars.put(key,val);
vars.putObject("OBJ1",new Object());
*   props - (JMeterProperties - class java.util.Properties) - e.g. props.get("START.HMS");props.put("PROP1","1234");
*   prev - ([SampleResult](https://jmeter.apache.org/api/org/apache/jmeter/samplers/SampleResult.html)) - gives access to the previous SampleResult (if any) 
*   sampler - ([Sampler](https://jmeter.apache.org/api/org/apache/jmeter/samplers/Sampler.html))- gives access to the current sampler 

For details of all the methods available on each of the above variables, please check the Javadoc

If the property beanshell.preprocessor.init is defined, this is used to load an initialisation file, which can be used to define methods etc. for use in the BeanShell script.

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

JSR223 PreProcessor[¶](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_PreProcessor "Link to here")
------------------------------------------------------------------------------------------------------------------------

The JSR223 PreProcessor allows JSR223 script code to be applied before taking a sample.

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_PreProcessor_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Language

The JSR223 language to be used

Yes

Parameters

 Parameters to pass to the script. The parameters are stored in the following variables: 
*   Parameters - string containing the parameters as a single variable 
*   args - String array containing parameters, split on white-space 

No

Script file

 A file containing the script to run, if a relative file path is used, then it will be relative to directory referenced by "user.dir" System property 

No

Script compilation caching

 Unique String across Test Plan that JMeter will use to cache result of Script compilation if language used supports [Compilable](https://docs.oracle.com/javase/8/docs/api/javax/script/Compilable.html) interface (Groovy is one of these, java, beanshell and javascript are not) 

See note in JSR223 Sampler Java System property if you're using Groovy without checking this option

No

Script

The script to run.

Yes (unless script file is provided)

The following JSR223 variables are set up for use by the script:

*   log - ([Logger](https://www.slf4j.org/api/org/slf4j/Logger.html)) - can be used to write to the log file 
*   Label - the String Label 
*   FileName - the script file name (if any) 
*   Parameters - the parameters (as a String) 
*   args - the parameters as a String array (split on whitespace) 
*   ctx - ([JMeterContext](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterContext.html)) - gives access to the context 
*   vars - ([JMeterVariables](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterVariables.html)) - gives read/write access to variables: vars.get(key);
vars.put(key,val);
vars.putObject("OBJ1",new Object());
vars.getObject("OBJ2");
*   props - (JMeterProperties - class java.util.Properties) - e.g. props.get("START.HMS");props.put("PROP1","1234");
*   sampler - ([Sampler](https://jmeter.apache.org/api/org/apache/jmeter/samplers/Sampler.html))- gives access to the current sampler 
*   OUT - System.out - e.g. OUT.println("message")

For details of all the methods available on each of the above variables, please check the Javadoc

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

JDBC PreProcessor[¶](https://jmeter.apache.org/usermanual/component_reference.html#JDBC_PreProcessor "Link to here")
--------------------------------------------------------------------------------------------------------------------

The JDBC PreProcessor enables you to run some SQL statement just before a sample runs. This can be useful if your JDBC Sample requires some data to be in DataBase and you cannot compute this in a setup Thread group. For details, see [JDBC Request](https://jmeter.apache.org/usermanual/component_reference.html#JDBC_Request).

See the following Test plan:

See also:

*   [Test Plan using JDBC Pre/Post Processor](https://jmeter.apache.org/demos/JDBC-Pre-Post-Processor.jmx)

In the linked test plan, "Create Price Cut-Off" JDBC PreProcessor calls a stored procedure to create a Price Cut-Off in Database, this one will be used by "Calculate Price cut off".

[![Image 143: Create Price Cut-Off Preprocessor](https://jmeter.apache.org/images/screenshots/jdbc-pre-processor.png)](https://jmeter.apache.org/images/screenshots/jdbc-pre-processor.png)

Create Price Cut-Off Preprocessor

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

RegEx User Parameters[¶](https://jmeter.apache.org/usermanual/component_reference.html#RegEx_User_Parameters "Link to here")
----------------------------------------------------------------------------------------------------------------------------

Allows to specify dynamic values for HTTP parameters extracted from another HTTP Request using regular expressions. RegEx User Parameters are specific to individual threads.

This component allows you to specify reference name of a regular expression that extracts names and values of HTTP request parameters. Regular expression group numbers must be specified for parameter's name and also for parameter's value. Replacement will only occur for parameters in the Sampler that uses this RegEx User Parameters which name matches

[![Image 144: Screenshot for Control-Panel of RegEx User Parameters](https://jmeter.apache.org/images/screenshots/regex_user_params.png)](https://jmeter.apache.org/images/screenshots/regex_user_params.png)

Screenshot of Control-Panel of RegEx User Parameters

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#RegEx_User_Parameters_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Regular Expression Reference Name

Name of a reference to a regular expression

Yes

Parameter names regexp group number

Group number of regular expression used to extract parameter names

Yes

Parameter values regex group number

Group number of regular expression used to extract parameter values

Yes

 Regexp Example[¶](https://jmeter.apache.org/usermanual/component_reference.html#regex_user_param_example "Link to here")

Suppose we have a request which returns a form with 3 input parameters and we want to extract the value of 2 of them to inject them in next request

1.    Create Post Processor Regular Expression for first HTTP Request 
    *   refName - set name of a regular expression Expression (listParams) 
    *   regular expression - expression that will extract input names and input values attributes 

 Ex: input name="([^"]+?)" value="([^"]+?)"
    *   template - would be empty 
    *   match nr - -1 (in order to iterate through all the possible matches) 

2.    Create Pre Processor RegEx User Parameters for second HTTP Request 
    *   refName - set the same reference name of a regular expression, would be listParams in our example 
    *   parameter names group number - group number of regular expression for parameter names, would be 1 in our example 
    *   parameter values group number - group number of regular expression for parameter values, would be 2 in our example 

See also the [Regular Expression Extractor](https://jmeter.apache.org/usermanual/component_reference.html#Regular_Expression_Extractor) element, which is used to extract parameters names and values

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

See also:

*   [Test Plan showing how to use RegEx User Parameters](https://jmeter.apache.org/demos/RegEx-User-Parameters.jmx)

Sample Timeout[¶](https://jmeter.apache.org/usermanual/component_reference.html#Sample_Timeout "Link to here")
--------------------------------------------------------------------------------------------------------------

This Pre-Processor schedules a timer task to interrupt a sample if it takes too long to complete. The timeout is ignored if it is zero or negative. For this to work, the sampler must implement Interruptible. The following samplers are known to do so: 

 AJP, BeanShell, FTP, HTTP, Soap, AccessLog, MailReader, JMS Subscriber, TCPSampler, TestAction, JavaSampler

The test element is intended for use where individual timeouts such as Connection Timeout or Response Timeout are insufficient, or where the Sampler does not support timeouts. The timeout should be set sufficiently long so that it is not triggered in normal tests, but short enough that it interrupts samples that are stuck.

[By default, JMeter uses a Callable to interrupt the sampler. This executes in the same thread as the timer, so if the interrupt takes a long while, it may delay the processing of subsequent timeouts. This is not expected to be a problem, but if necessary the property InterruptTimer.useRunnable can be set to true to use a separate Runnable thread instead of the Callable.]

[![Image 145: Screenshot for Control-Panel of Sample Timeout](https://jmeter.apache.org/images/screenshots/sample_timeout.png)](https://jmeter.apache.org/images/screenshots/sample_timeout.png)

Screenshot of Control-Panel of Sample Timeout

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Sample_Timeout_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this timer that is shown in the tree.

No

Sample Timeout

If the sample takes longer to complete, it will be interrupted.

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

18.8 Post-Processors[¶](https://jmeter.apache.org/usermanual/component_reference.html#postprocessors "Link to here")
====================================================================================================================

As the name suggests, Post-Processors are applied after samplers. Note that they are applied to **all** the samplers in the same scope, so to ensure that a post-processor is applied only to a particular sampler, add it as a child of the sampler.

 Note: Unless documented otherwise, Post-Processors are not applied to sub-samples (child samples) - only to the parent sample. In the case of JSR223 and BeanShell post-processors, the script can retrieve sub-samples using the method prev.getSubResults() which returns an array of SampleResults. The array will be empty if there are none. 

Post-Processors are run before Assertions, so they do not have access to any Assertion Results, nor will the sample status reflect the results of any Assertions. If you require access to Assertion Results, try using a Listener instead. Also note that the variable JMeterThread.last_sample_ok is set to "true" or "false" after all Assertions have been run.

Regular Expression Extractor[¶](https://jmeter.apache.org/usermanual/component_reference.html#Regular_Expression_Extractor "Link to here")
------------------------------------------------------------------------------------------------------------------------------------------

Allows the user to extract values from a server response using a Perl-type regular expression. As a post-processor, this element will execute after each Sample request in its scope, applying the regular expression, extracting the requested values, generate the template string, and store the result into the given variable name.

[![Image 146: Screenshot for Control-Panel of Regular Expression Extractor](https://jmeter.apache.org/images/screenshots/regex_extractor.png)](https://jmeter.apache.org/images/screenshots/regex_extractor.png)

Screenshot of Control-Panel of Regular Expression Extractor

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Regular_Expression_Extractor_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Apply to:

 This is for use with samplers that can generate sub-samples, e.g. HTTP Sampler with embedded resources, Mail Reader or samples generated by the Transaction Controller. 
*   Main sample only - only applies to the main sample 
*   Sub-samples only - only applies to the sub-samples 
*   Main sample and sub-samples - applies to both. 
*   JMeter Variable Name to use - extraction is to be applied to the contents of the named variable 

 Matching is applied to all qualifying samples in turn. For example if there is a main sample and 3 sub-samples, each of which contains a single match for the regex, (i.e. 4 matches in total). For match number = 3, Sub-samples only, the extractor will match the 3 rd sub-sample. For match number = 3, Main sample and sub-samples, the extractor will match the 2 nd sub-sample (1 st match is main sample). For match number = 0 or negative, all qualifying samples will be processed. For match number >0, matching will stop as soon as enough matches have been found. 

Yes

Field to check

 The following fields can be checked: 
*   Body - the body of the response, e.g. the content of a web-page (excluding headers) 
*   Body (unescaped) - the body of the response, with all Html escape codes replaced. Note that Html escapes are processed without regard to context, so some incorrect substitutions may be made.  Note that this option highly impacts performances, so use it only when absolutely necessary and be aware of its impacts  
*   Body as a Document - the extract text from various type of documents via Apache Tika (see [View Results Tree](https://jmeter.apache.org/usermanual/component_reference.html#View_Results_Tree) Document view section).  Note that the Body as a Document option can impact performances, so ensure it is OK for your test  
*   Request Headers - may not be present for non-HTTP samples 
*   Response Headers - may not be present for non-HTTP samples 
*   URL
*   Response Code - e.g. 200
*   Response Message - e.g. OK

 Headers can be useful for HTTP samples; it may not be present for other sample types. 

Yes

Name of created variable

 The name of the JMeter variable in which to store the result. Also note that each group is stored as [refname]_g#, where [refname] is the string you entered as the reference name, and # is the group number, where group 0 is the entire match, group 1 is the match from the first set of parentheses, etc. 

Yes

Regular Expression

 The regular expression used to parse the response data. This must contain at least one set of parentheses "()" to capture a portion of the string, unless using the group $0$. Do not enclose the expression in / / - unless of course you want to match these characters as well. 

Yes

Template

 The template used to create a string from the matches found. This is an arbitrary string with special elements to refer to groups within the regular expression. The syntax to refer to a group is: '$1$' to refer to group 1, '$2$' to refer to group 2, etc. $0$ refers to whatever the entire expression matches. 

Yes

Match No. (0 for Random)

 Indicates which match to use. The regular expression may match multiple times. 
*   Use a value of zero to indicate JMeter should choose a match at random.
*    A positive number N means to select the n th match. 
*    Negative numbers are used in conjunction with the [ForEach Controller](https://jmeter.apache.org/usermanual/component_reference.html#ForEach_Controller) - see below. 

Yes

Default Value

 If the regular expression does not match, then the reference variable will be set to the default value. This is particularly useful for debugging tests. If no default is provided, then it is difficult to tell whether the regular expression did not match, or the RE element was not processed or maybe the wrong variable is being used. 
However, if you have several test elements that set the same variable, you may wish to leave the variable unchanged if the expression does not match. In this case, remove the default value once debugging is complete.

No, but recommended

Use empty default value

 If the checkbox is checked and Default Value is empty, then JMeter will set the variable to empty string instead of not setting it. Thus when you will for example use ${var} (if Reference Name is var) in your Test Plan, if the extracted value is not found then ${var} will be equal to empty string instead of containing ${var} which may be useful if extracted value is optional. 

No

If the match number is set to a non-negative number, and a match occurs, the variables are set as follows:

*   refName - the value of the template 
*   refName_g _n_, where n=0,1,2 - the groups for the match 
*   refName_g - the number of groups in the Regex (excluding 0) 

If no match occurs, then the refName variable is set to the default (unless this is absent). Also, the following variables are removed:

*   refName_g0
*   refName_g1
*   refName_g

If the match number is set to a negative number, then all the possible matches in the sampler data are processed. The variables are set as follows:

*   refName_matchNr - the number of matches found; could be 0
*   refName_ _n_, where n = 1, 2, 3 etc. - the strings as generated by the template 
*   refName_ _n_ _g _m_, where m=0, 1, 2 - the groups for match n
*   refName - always set to the default value 
*   refName_g _n_ - not set 

Note that the refName variable is always set to the default value in this case, and the associated group variables are not set.

See also [Response Assertion](https://jmeter.apache.org/usermanual/component_reference.html#Response_Assertion) for some examples of how to specify modifiers, and [for further information on JMeter regular expressions.](https://jmeter.apache.org/usermanual/regular_expressions.html)

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

CSS Selector Extractor[(was: CSS/JQuery Extractor )](https://jmeter.apache.org/usermanual/component_reference.html)[¶](https://jmeter.apache.org/usermanual/component_reference.html#CSS_Selector_Extractor "Link to here")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Allows the user to extract values from a server HTML response using a CSS Selector syntax. As a post-processor, this element will execute after each Sample request in its scope, applying the CSS/JQuery expression, extracting the requested nodes, extracting the node as text or attribute value and store the result into the given variable name.

[![Image 147: CSS Extractor with attribute value set](https://jmeter.apache.org/images/screenshots/css_extractor_attr.png)](https://jmeter.apache.org/images/screenshots/css_extractor_attr.png)

Screenshot of Control-Panel of CSS Selector Extractor

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#CSS_Selector_Extractor_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Apply to:

 This is for use with samplers that can generate sub-samples, e.g. HTTP Sampler with embedded resources, Mail Reader or samples generated by the Transaction Controller. 
*   Main sample only - only applies to the main sample 
*   Sub-samples only - only applies to the sub-samples 
*   Main sample and sub-samples - applies to both. 
*   JMeter Variable Name to use - extraction is to be applied to the contents of the named variable 

 Matching is applied to all qualifying samples in turn. For example if there is a main sample and 3 sub-samples, each of which contains a single match for the regex, (i.e. 4 matches in total). For match number = 3, Sub-samples only, the extractor will match the 3 rd sub-sample. For match number = 3, Main sample and sub-samples, the extractor will match the 2 nd sub-sample (1 st match is main sample). For match number = 0 or negative, all qualifying samples will be processed. For match number >0, matching will stop as soon as enough matches have been found. 

Yes

CSS Selector Implementation

 2 Implementations for CSS/JQuery based syntax are supported: 
*   [JSoup](http://jsoup.org/)
*   [Jodd-Lagarto (CSSelly)](http://jodd.org/doc/lagarto/index.html)

 If selector is set to empty, default implementation(JSoup) will be used. 

False

Name of created variable

The name of the JMeter variable in which to store the result.

Yes

CSS/JQuery expression

 The CSS/JQuery selector used to select nodes from the response data. Selector, selectors combination and pseudo-selectors are supported, examples: 
*   E[foo] - an E element with a "foo" attribute 
*   ancestor child - child elements that descend from ancestor, e.g. .body p finds p elements anywhere under a block with class "body" 
*   :lt(n) - find elements whose sibling index (i.e. its position in the DOM tree relative to its parent) is less than n; e.g. td:lt(3)
*   :contains(text) - find elements that contain the given text. The search is case-insensitive; e.g. p:contains(jsoup)
*   …

 For more details on syntax, see: 
*   [JSoup](http://jsoup.org/cookbook/extracting-data/selector-syntax)
*   [Jodd-Lagarto (CSSelly)](http://jodd.org/doc/csselly/)

Yes

Attribute

 Name of attribute (as per HTML syntax) to extract from nodes that matched the selector. If empty, then the combined text of this element and all its children will be returned. 

 This is the equivalent [Element#attr(name)](http://jsoup.org/apidocs/org/jsoup/nodes/Node.html#attr%28java.lang.String%29) function for JSoup if an attribute is set. 

[![Image 148: CSS Extractor with attribute value set](https://jmeter.apache.org/images/screenshots/css_extractor_attr.png)](https://jmeter.apache.org/images/screenshots/css_extractor_attr.png)

CSS Extractor with attribute value set

 If empty this is the equivalent of [Element#text()](http://jsoup.org/apidocs/org/jsoup/nodes/Element.html#text%28%29) function for JSoup if not value is set for attribute. [![Image 149: CSS Extractor with no attribute set](https://jmeter.apache.org/images/screenshots/css_extractor_noattr.png)](https://jmeter.apache.org/images/screenshots/css_extractor_noattr.png)

CSS Extractor with no attribute set

false

Match No. (0 for Random)

 Indicates which match to use. The CSS/JQuery selector may match multiple times. 
*   Use a value of zero to indicate JMeter should choose a match at random.
*    A positive number N means to select the n th match. 
*    Negative numbers are used in conjunction with the [ForEach Controller](https://jmeter.apache.org/usermanual/component_reference.html#ForEach_Controller) - see below. 

Yes

Default Value

 If the expression does not match, then the reference variable will be set to the default value. This is particularly useful for debugging tests. If no default is provided, then it is difficult to tell whether the expression did not match, or the CSS/JQuery element was not processed or maybe the wrong variable is being used. 
However, if you have several test elements that set the same variable, you may wish to leave the variable unchanged if the expression does not match. In this case, remove the default value once debugging is complete.

No, but recommended

Use empty default value

 If the checkbox is checked and Default Value is empty, then JMeter will set the variable to empty string instead of not setting it. Thus when you will for example use ${var} (if Reference Name is var) in your Test Plan, if the extracted value is not found then ${var} will be equal to empty string instead of containing ${var} which may be useful if extracted value is optional. 

No

If the match number is set to a non-negative number, and a match occurs, the variables are set as follows:

*   refName - the value of the template 

If no match occurs, then the refName variable is set to the default (unless this is absent).

If the match number is set to a negative number, then all the possible matches in the sampler data are processed. The variables are set as follows:

*   refName_matchNr - the number of matches found; could be 0
*   refName_n, where n = 1, 2, 3, etc. - the strings as generated by the template 
*   refName - always set to the default value 

Note that the refName variable is always set to the default value in this case.

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

XPath2 Extractor[¶](https://jmeter.apache.org/usermanual/component_reference.html#XPath2_Extractor "Link to here")
------------------------------------------------------------------------------------------------------------------

This test element allows the user to extract value(s) from structured response - XML or (X)HTML - using XPath2 query language. 

[![Image 150: Screenshot for Control-Panel of XPath2 Extractor](https://jmeter.apache.org/images/screenshots/xpath2_extractor.png)](https://jmeter.apache.org/images/screenshots/xpath2_extractor.png)

Screenshot of Control-Panel of XPath2 Extractor

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#XPath2_Extractor_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Apply to:

 This is for use with samplers that can generate sub-samples, e.g. HTTP Sampler with embedded resources, Mail Reader or samples generated by the Transaction Controller. 
*   Main sample only - only applies to the main sample 
*   Sub-samples only - only applies to the sub-samples 
*   Main sample and sub-samples - applies to both. 
*   JMeter Variable Name to use - extraction is to be applied to the contents of the named variable 

 XPath matching is applied to all qualifying samples in turn, and all the matching results will be returned. 

Yes

Return entire XPath fragment instead of text content?

 If selected, the fragment will be returned rather than the text content. 

 For example //title would return "<title>Apache JMeter</title>" rather than "Apache JMeter". 

 In this case, //title/text() would return "Apache JMeter". 

Yes

Name of created variable

The name of the JMeter variable in which to store the result.

Yes

XPath Query

Element query in XPath 2.0 language. Can return more than one match.

Yes

Match No. (0 for Random)

 If the XPath Path query leads to many results, you can choose which one(s) to extract as Variables: 
*   0: means random (default value) 
*   -1 means extract all results, they will be named as _<variable name>_ _N (where N goes from 1 to Number of results) 
*   X: means extract the X th result. If this X th is greater than number of matches, then nothing is returned. Default value will be used 

No

Default Value

Default value returned when no match found. It is also returned if the node has no value and the fragment option is not selected.

yes

Namespaces aliases list

 List of namespaces aliases you want to use to parse the document, one line per declaration. You must specify them as follow: prefix=namespace. This implementation makes it easier to use namespaces than with the old XPathExtractor version. 

No

To allow for use in a [ForEach Controller](https://jmeter.apache.org/usermanual/component_reference.html#ForEach_Controller), it works exactly the same as the above XPath Extractor

XPath2 Extractor provides some interestings tools such as an improved syntax and much more functions than in its first version.

Here are some exemples:

abs(/book/page[2]) extracts 2 nd absolute value of the page from a book avg(/librarie/book/page)extracts the average number of page from all the books in the libraries compare(/book[1]/page[2],/book[2]/page[2]) return Integer value equal 0 to if the 2 nd page of the first book is equal to the 2 nd page of the 2 nd book, else return -1. 
To see more information about these functions, please check [xPath2 functions](http://saxon.sourceforge.net/saxon7.9.1/functions.html)

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

XPath Extractor[¶](https://jmeter.apache.org/usermanual/component_reference.html#XPath_Extractor "Link to here")
----------------------------------------------------------------------------------------------------------------

 This test element allows the user to extract value(s) from structured response - XML or (X)HTML - using XPath query language. 

 Since JMeter 5.0, you should use [XPath2 Extractor](https://jmeter.apache.org/usermanual/component_reference.html#XPath2_Extractor) as it provides better and easier namespace management, better performances and support for XPath 2.0 

[![Image 151: Screenshot for Control-Panel of XPath Extractor](https://jmeter.apache.org/images/screenshots/xpath_extractor.png)](https://jmeter.apache.org/images/screenshots/xpath_extractor.png)

Screenshot of Control-Panel of XPath Extractor

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#XPath_Extractor_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Apply to:

 This is for use with samplers that can generate sub-samples, e.g. HTTP Sampler with embedded resources, Mail Reader or samples generated by the Transaction Controller. 
*   Main sample only - only applies to the main sample 
*   Sub-samples only - only applies to the sub-samples 
*   Main sample and sub-samples - applies to both. 
*   JMeter Variable Name to use - extraction is to be applied to the contents of the named variable 

 XPath matching is applied to all qualifying samples in turn, and all the matching results will be returned. 

Yes

Use Tidy (tolerant parser)

 If checked use Tidy to parse HTML response into XHTML. 
*    "Use Tidy" should be checked on for HTML response. Such response is converted to valid XHTML (XML compatible HTML) using Tidy 
*    "Use Tidy" should be unchecked for both XHTML or XML response (for example RSS) 

For HTML, CSS Selector Extractor is the correct and performing solution. Don't use XPath for HTML extractions.

Yes

Quiet

Sets the Tidy Quiet flag

If Tidy is selected

Report Errors

If a Tidy error occurs, then set the Assertion accordingly

If Tidy is selected

Show warnings

Sets the Tidy showWarnings option

If Tidy is selected

Use Namespaces

 If checked, then the XML parser will use namespace resolution.(see note below on NAMESPACES) Note that currently only namespaces declared on the root element will be recognised. See below for user-definition of additional workspace names. 

If Tidy is not selected

Validate XML

Check the document against its schema.

If Tidy is not selected

Ignore Whitespace

Ignore Element Whitespace.

If Tidy is not selected

Fetch External DTDs

If selected, external DTDs are fetched.

If Tidy is not selected

Return entire XPath fragment instead of text content?

 If selected, the fragment will be returned rather than the text content. 

 For example //title would return "<title>Apache JMeter</title>" rather than "Apache JMeter". 

 In this case, //title/text() would return "Apache JMeter". 

Yes

Name of created variable

The name of the JMeter variable in which to store the result.

Yes

XPath Query

Element query in XPath language. Can return more than one match.

Yes

Match No. (0 for Random)

 If the XPath Path query leads to many results, you can choose which one(s) to extract as Variables: 
*   0: means random 
*   -1 means extract all results (default value), they will be named as _<variable name>_ _N (where N goes from 1 to Number of results) 
*   X: means extract the X th result. If this X th is greater than number of matches, then nothing is returned. Default value will be used 

No

Default Value

Default value returned when no match found. It is also returned if the node has no value and the fragment option is not selected.

To allow for use in a [ForEach Controller](https://jmeter.apache.org/usermanual/component_reference.html#ForEach_Controller), the following variables are set on return:

*   refName - set to first (or only) match; if no match, then set to default 
*   refName_matchNr - set to number of matches (may be 0) 
*   refName_n - n=1, 2, 3, etc. Set to the 1 st, 2 nd 3 rd match etc. 

 Note: The next refName_n variable is set to null - e.g. if there are 2 matches, then refName_3 is set to null, and if there are no matches, then refName_1 is set to null. 

XPath is query language targeted primarily for XSLT transformations. However it is useful as generic query language for structured data too. See [XPath Reference](http://www.topxml.com/xsl/xpathref.asp) or [XPath specification](http://www.w3.org/TR/xpath) for more information. Here are few examples:

/html/head/title extracts title element from HTML response/book/page[2] extracts 2 nd page from a book /book/page extracts all pages from a book//form[@name='countryForm']//select[@name='country']/option[text()='Czech Republic'])/@value extracts value attribute of option element that match text 'Czech Republic' inside of select element with name attribute 'country' inside of form with name attribute 'countryForm' 

 When "Use Tidy" is checked on - resulting XML document may slightly differ from original HTML response: 
*   All elements and attribute names are converted to lowercase
*    Tidy attempts to correct improperly nested elements. For example - original (incorrect) ul/font/li becomes correct ul/li/font

 See [Tidy homepage](http://jtidy.sf.net/) for more information. 

**NAMESPACES**

 As a work-round for namespace limitations of the Xalan XPath parser (implementation on which JMeter is based) you need to: 
*    provide a Properties file (if for example your file is named namespaces.properties) which contains mappings for the namespace prefixes: 
prefix1=http\://foo.apache.org
prefix2=http\://toto.apache.org
…
*    reference this file in user.properties file using the property: xpath.namespace.config=namespaces.properties

//mynamespace:tagname//*[local-name()='tagname' and namespace-uri()='uri-for-namespace']uri-for-namespace mynamespace

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

JSON JMESPath Extractor[¶](https://jmeter.apache.org/usermanual/component_reference.html#JSON_JMESPath_Extractor "Link to here")
--------------------------------------------------------------------------------------------------------------------------------

This test element allows the user to extract value(s) from JSON response using JMESPath query language. 

[![Image 152: Screenshot for Control-Panel of JSON JMESPath Extractor](https://jmeter.apache.org/images/screenshots/extractor/jmespath_extractor.png)](https://jmeter.apache.org/images/screenshots/extractor/jmespath_extractor.png)

Screenshot of Control-Panel of JSON JMESPath Extractor

In the XPATH Extractor we support to extract multiple xpaths at the same time, but in JMES Extractor only one JMES Expression can be entered at a time. 

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#JSON_JMESPath_Extractor_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Apply to:

 This is for use with samplers that can generate sub-samples, e.g. HTTP Sampler with embedded resources, Mail Reader or samples generated by the Transaction Controller. 
*   Main sample only - only applies to the main sample 
*   Sub-samples only - only applies to the sub-samples 
*   Main sample and sub-samples - applies to both. 
*   JMeter Variable Name to use - extraction is to be applied to the contents of the named variable 

Yes

Name of created variable

The name of the JMeter variable in which to store the result.

Yes

JMESPath expressions

Element query in JMESPath query language. Can return the matched result.

Yes

Match No. (0 for Random)

 If the JMESPath query leads to many results, you can choose which one(s) to extract as Variables: 
*   0: means random 
*   -1 means extract all results (default value), they will be named as _<variable name>_ _N (where N goes from 1 to Number of results) 
*   X: means extract the X th result. If this X th is greater than number of matches, then nothing is returned. Default value will be used 

No

Default Value

Default value returned when no match found. It is also returned if the node has no value and the fragment option is not selected.

JMESPath is a query language for JSON. It is described in an ABNF grammar with a complete specification. This ensures that the language syntax is precisely defined. See [JMESPath Reference](http://jmespath.org/) for more information. Here are also some examples [JMESPath Example](http://jmespath.org/tutorial.html).

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Result Status Action Handler[¶](https://jmeter.apache.org/usermanual/component_reference.html#Result_Status_Action_Handler "Link to here")
------------------------------------------------------------------------------------------------------------------------------------------

This test element allows the user to stop the thread or the whole test if the relevant sampler failed. 

[![Image 153: Screenshot for Control-Panel of Result Status Action Handler](https://jmeter.apache.org/images/screenshots/resultstatusactionhandler.png)](https://jmeter.apache.org/images/screenshots/resultstatusactionhandler.png)

Screenshot of Control-Panel of Result Status Action Handler

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Result_Status_Action_Handler_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Action to be taken after a Sampler error

 Determines what happens if a sampler error occurs, either because the sample itself failed or an assertion failed. The possible choices are: 
*   Continue - ignore the error and continue with the test 
*   Start next thread loop - does not execute samplers following the sampler in error for the current iteration and restarts the loop on next iteration 
*   Stop Thread - current thread exits 
*   Stop Test - the entire test is stopped at the end of any current samples. 
*   Stop Test Now - the entire test is stopped abruptly. Any current samplers are interrupted if possible. 

 No 

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

BeanShell PostProcessor[¶](https://jmeter.apache.org/usermanual/component_reference.html#BeanShell_PostProcessor "Link to here")
--------------------------------------------------------------------------------------------------------------------------------

The BeanShell PreProcessor allows arbitrary code to be applied after taking a sample.

BeanShell Post-Processor no longer ignores samples with zero-length result data

**For full details on using BeanShell, please see the [BeanShell website.](http://www.beanshell.org/)**

 Migration to [JSR223 PostProcessor](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_PostProcessor)+Groovy is highly recommended for performance, support of new Java features and limited maintenance of the BeanShell library. 

The test element supports the ThreadListener and TestListener methods. These should be defined in the initialisation file. See the file BeanShellListeners.bshrc for example definitions.

[![Image 154: Screenshot for Control-Panel of BeanShell PostProcessor](https://jmeter.apache.org/images/screenshots/beanshell_postprocessor.png)](https://jmeter.apache.org/images/screenshots/beanshell_postprocessor.png)

Screenshot of Control-Panel of BeanShell PostProcessor

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#BeanShell_PostProcessor_parms1 "Link to here")

Attribute

Description

Required

Name

 Descriptive name for this element that is shown in the tree. The name is stored in the script variable Label

No

Reset bsh.Interpreter before each call

 If this option is selected, then the interpreter will be recreated for each sample. This may be necessary for some long running scripts. For further information, see [Best Practices - BeanShell scripting](https://jmeter.apache.org/usermanual/best-practices.html#bsh_scripting). 

Yes

Parameters

 Parameters to pass to the BeanShell script. The parameters are stored in the following variables: 
*   Parameters - string containing the parameters as a single variable 
*   bsh.args - String array containing parameters, split on white-space 

No

Script file

 A file containing the BeanShell script to run. The file name is stored in the script variable FileName

No

Script

The BeanShell script. The return value is ignored.

Yes (unless script file is provided)

The following BeanShell variables are set up for use by the script:

*   log - ([Logger](https://www.slf4j.org/api/org/slf4j/Logger.html)) - can be used to write to the log file 
*   ctx - ([JMeterContext](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterContext.html)) - gives access to the context 
*   vars - ([JMeterVariables](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterVariables.html)) - gives read/write access to variables: vars.get(key);
vars.put(key,val);
vars.putObject("OBJ1",new Object());
*   props - (JMeterProperties - class java.util.Properties) - e.g. props.get("START.HMS");props.put("PROP1","1234");
*   prev - ([SampleResult](https://jmeter.apache.org/api/org/apache/jmeter/samplers/SampleResult.html)) - gives access to the previous SampleResult 
*   data - (byte [])- gives access to the current sample data 

For details of all the methods available on each of the above variables, please check the Javadoc

If the property beanshell.postprocessor.init is defined, this is used to load an initialisation file, which can be used to define methods etc. for use in the BeanShell script.

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

JSR223 PostProcessor[¶](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_PostProcessor "Link to here")
--------------------------------------------------------------------------------------------------------------------------

The JSR223 PostProcessor allows JSR223 script code to be applied after taking a sample.

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#JSR223_PostProcessor_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Language

The JSR223 language to be used

Yes

Parameters

 Parameters to pass to the script. The parameters are stored in the following variables: 
*   Parameters - string containing the parameters as a single variable 
*   args - String array containing parameters, split on white-space 

No

Script file

 A file containing the script to run, if a relative file path is used, then it will be relative to directory referenced by "user.dir" System property 

No

Script compilation caching

 Unique String across Test Plan that JMeter will use to cache result of Script compilation if language used supports [Compilable](https://docs.oracle.com/javase/8/docs/api/javax/script/Compilable.html) interface (Groovy is one of these, java, beanshell and javascript are not) 

See note in JSR223 Sampler Java System property if you're using Groovy without checking this option

No

Script

The script to run.

Yes (unless script file is provided)

Before invoking the script, some variables are set up. Note that these are JSR223 variables - i.e. they can be used directly in the script.

*   log - ([Logger](https://www.slf4j.org/api/org/slf4j/Logger.html)) - can be used to write to the log file 
*   Label - the String Label 
*   FileName - the script file name (if any) 
*   Parameters - the parameters (as a String) 
*   args - the parameters as a String array (split on whitespace) 
*   ctx - ([JMeterContext](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterContext.html)) - gives access to the context 
*   vars - ([JMeterVariables](https://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterVariables.html)) - gives read/write access to variables: vars.get(key);
vars.put(key,val);
vars.putObject("OBJ1",new Object());
vars.getObject("OBJ2");
*   props - (JMeterProperties - class java.util.Properties) - e.g. props.get("START.HMS");props.put("PROP1","1234");
*   prev - ([SampleResult](https://jmeter.apache.org/api/org/apache/jmeter/samplers/SampleResult.html)) - gives access to the previous SampleResult (if any) 
*   sampler - ([Sampler](https://jmeter.apache.org/api/org/apache/jmeter/samplers/Sampler.html))- gives access to the current sampler 
*   OUT - System.out - e.g. OUT.println("message")

For details of all the methods available on each of the above variables, please check the Javadoc

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

JDBC PostProcessor[¶](https://jmeter.apache.org/usermanual/component_reference.html#JDBC_PostProcessor "Link to here")
----------------------------------------------------------------------------------------------------------------------

The JDBC PostProcessor enables you to run some SQL statement just after a sample has run. This can be useful if your JDBC Sample changes some data and you want to reset state to what it was before the JDBC sample run.

See also:

*   [Test Plan using JDBC Pre/Post Processor](https://jmeter.apache.org/demos/JDBC-Pre-Post-Processor.jmx)

In the linked test plan, "JDBC PostProcessor" JDBC PostProcessor calls a stored procedure to delete from Database the Price Cut-Off that was created by PreProcessor.

[![Image 155: JDBC PostProcessor](https://jmeter.apache.org/images/screenshots/jdbc-post-processor.png)](https://jmeter.apache.org/images/screenshots/jdbc-post-processor.png)

JDBC PostProcessor

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

JSON Extractor[¶](https://jmeter.apache.org/usermanual/component_reference.html#JSON_Extractor "Link to here")
--------------------------------------------------------------------------------------------------------------

The JSON PostProcessor enables you extract data from JSON responses using JSON-PATH syntax. This post processor is very similar to Regular expression extractor. It must be placed as a child of HTTP Sampler or any other sampler that has responses. It will allow you to extract in a very easy way text content, see [JSON Path syntax](https://github.com/json-path/JsonPath).

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#JSON_Extractor_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Apply to:

 This is for use with samplers that can generate sub-samples, e.g. HTTP Sampler with embedded resources, Mail Reader or samples generated by the Transaction Controller. Main sample only only applies to the main sample Sub-samples only only applies to the sub-samples Main sample and sub-samples applies to both.JMeter Variable Name to use extraction is to be applied to the contents of the named variable

Yes

Names of created variables

Semicolon separated names of variables that will contain the results of JSON-PATH expressions (must match number of JSON-PATH expressions)

Yes

JSON Path Expressions

Semicolon separated JSON-PATH expressions (must match number of variables)

Yes

Default Values

Semicolon separated default values if JSON-PATH expressions do not return any result(must match number of variables)

No

Match Numbers

 For each JSON Path Expression, if the JSON Path query leads to many results, you can choose which one(s) to extract as Variables: 
*   0: means random (Default Value) 
*   -1 means extract all results, they will be named as _<variable name>_ _N (where N goes from 1 to Number of results) 
*   X: means extract the _X_ th result. If this _X_ th is greater than number of matches, then nothing is returned. Default value will be used 

 The numbers have to be given as a Semicolon separated list. The number of elements in that list have to match the number of given JSON Path Expressions. If left empty, the value 0 will be used as default for every expression. 

No

Compute concatenation var

 If many results are found, plugin will concatenate them using ‘,’ separator and store it in a var named _<variable name>_ _ALL

No

[![Image 156: JSON PostProcessor](https://jmeter.apache.org/images/screenshots/json-post-processor.png)](https://jmeter.apache.org/images/screenshots/json-post-processor.png)

JSON PostProcessor

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Boundary Extractor[¶](https://jmeter.apache.org/usermanual/component_reference.html#Boundary_Extractor "Link to here")
----------------------------------------------------------------------------------------------------------------------

Allows the user to extract values from a server response using left and right boundaries. As a post-processor, this element will execute after each Sample request in its scope, testing the boundaries, extracting the requested values, generate the template string, and store the result into the given variable name.

[![Image 157: Screenshot for Control-Panel of Boundary Extractor](https://jmeter.apache.org/images/screenshots/extractor/boundary_extractor.png)](https://jmeter.apache.org/images/screenshots/extractor/boundary_extractor.png)

Screenshot of Control-Panel of Boundary Extractor

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Boundary_Extractor_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Apply to:

 This is for use with samplers that can generate sub-samples, e.g. HTTP Sampler with embedded resources, Mail Reader or samples generated by the Transaction Controller. 
*   Main sample only - only applies to the main sample 
*   Sub-samples only - only applies to the sub-samples 
*   Main sample and sub-samples - applies to both. 
*   JMeter Variable Name to use - assertion is to be applied to the contents of the named variable 

 Matching is applied to all qualifying samples in turn. For example if there is a main sample and 3 sub-samples, each of which contains a single match test, (i.e. 4 matches in total). For match number = 3, Sub-samples only, the extractor will match the 3 rd sub-sample. For match number = 3, Main sample and sub-samples, the extractor will match the 2 nd sub-sample (1 st match is main sample). For match number = 0 or negative, all qualifying samples will be processed. For match number >0, matching will stop as soon as enough matches have been found. 

Yes

Field to check

 The following fields can be checked: 
*   Body - the body of the response, e.g. the content of a web-page (excluding headers) 
*   Body (unescaped) - the body of the response, with all Html escape codes replaced. Note that Html escapes are processed without regard to context, so some incorrect substitutions may be made.  Note that this option highly impacts performances, so use it only when absolutely necessary and be aware of its impacts  
*   Body as a Document - the extract text from various type of documents via Apache Tika (see [View Results Tree](https://jmeter.apache.org/usermanual/component_reference.html#View_Results_Tree) Document view section).  Note that the Body as a Document option can impact performances, so ensure it is OK for your test  
*   Request Headers - may not be present for non-HTTP samples 
*   Response Headers - may not be present for non-HTTP samples 
*   URL
*   Response Code - e.g. 200
*   Response Message - e.g. OK

 Headers can be useful for HTTP samples; it may not be present for other sample types. 

Yes

Name of created variable

 The name of the JMeter variable in which to store the result. Also note that each group is stored as [refname]_g#, where [refname] is the string you entered as the reference name, and # is the group number, where group 0 is the entire match, group 1 is the match from the first set of parentheses, etc. 

Yes

Left Boundary

Left boundary of value to find

No

Right Boundary

Right boundary of value to find

No

Match No. (0 for Random)

 Indicates which match to use. The boundaries may match multiple times. 
*   Use a value of zero to indicate JMeter should choose a match at random.
*    A positive number N means to select the n th match. 
*    Negative numbers are used in conjunction with the [ForEach Controller](https://jmeter.apache.org/usermanual/component_reference.html#ForEach_Controller) - see below. 

Yes

Default Value

 If the boundaries do not match, then the reference variable will be set to the default value. This is particularly useful for debugging tests. If no default is provided, then it is difficult to tell whether the boundaries did not match, or maybe the wrong variable is being used. 
However, if you have several test elements that set the same variable, you may wish to leave the variable unchanged if the expression does not match. In this case, remove the default value once debugging is complete.

No, but recommended

If the match number is set to a non-negative number, and a match occurs, the variables are set as follows:

*   refName - the value of the extraction 

If no match occurs, then the refName variable is set to the default (unless this is absent).

If the match number is set to a negative number, then all the possible matches in the sampler data are processed. The variables are set as follows:

*   refName_matchNr - the number of matches found; could be 0
*   refName_ _n_, where n = 1, 2, 3 etc. - the strings as generated by the template 
*   refName_ _n_ _g _m_, where m=0, 1, 2 - the groups for match n
*   refName - always set to the default value 

Note that the refName variable is always set to the default value in this case, and the associated group variables are not set.

If both left and right boundary are null, the whole data selected in scope is returned

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

18.9 Miscellaneous Features[¶](https://jmeter.apache.org/usermanual/component_reference.html#Miscellaneous_Features "Link to here")
===================================================================================================================================

Test Plan[¶](https://jmeter.apache.org/usermanual/component_reference.html#Test_Plan "Link to here")
----------------------------------------------------------------------------------------------------

The Test Plan is where the overall settings for a test are specified.

Static variables can be defined for values that are repeated throughout a test, such as server names. For example the variable SERVER could be defined as www.example.com, and the rest of the test plan could refer to it as ${SERVER}. This simplifies changing the name later.

If the same variable name is reused on one of more [User Defined Variables](https://jmeter.apache.org/usermanual/component_reference.html#User_Defined_Variables) Configuration elements, the value is set to the last definition in the test plan (reading from top to bottom). Such variables should be used for items that may change between test runs, but which remain the same during a test run.

Note that the Test Plan cannot refer to variables it defines.

 If you need to construct other variables from the Test Plan variables, use a [User Defined Variables](https://jmeter.apache.org/usermanual/component_reference.html#User_Defined_Variables) test element. 
Selecting Functional Testing instructs JMeter to save the additional sample information - Response Data and Sampler Data - to all result files. This increases the resources needed to run a test, and may adversely impact JMeter performance. If more data is required for a particular sampler only, then add a Listener to it, and configure the fields as required.

The option does not affect CSV result files, which cannot currently store such information.

Also, an option exists here to instruct JMeter to run the [Thread Group](https://jmeter.apache.org/usermanual/component_reference.html#Thread_Group) serially rather than in parallel.

Run tearDown Thread Groups after shutdown of main threads: if selected, the tearDown groups (if any) will be run after graceful shutdown of the main threads. The tearDown threads won't be run if the test is forcibly stopped.

Test plan now provides an easy way to add classpath setting to a specific test plan. The feature is additive, meaning that you can add jar files or directories, but removing an entry requires restarting JMeter.

Note that this cannot be used to add JMeter GUI plugins, because they are processed earlier.

 However it can be useful for utility jars such as JDBC drivers. The jars are only added to the search path for the JMeter loader, not for the system class loader. 
JMeter properties also provides an entry for loading additional classpaths. In jmeter.properties, edit "user.classpath" or "plugin_dependency_paths" to include additional libraries. See [JMeter's Classpath](https://jmeter.apache.org/usermanual/get-started.html#classpath) and [Configuring JMeter](https://jmeter.apache.org/usermanual/get-started.html#configuring_jmeter) for details.

[![Image 158: Screenshot for Control-Panel of Test Plan](https://jmeter.apache.org/images/screenshots/testplan.png)](https://jmeter.apache.org/images/screenshots/testplan.png)

Screenshot of Control-Panel of Test Plan

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Open Model Thread Group[¶](https://jmeter.apache.org/usermanual/component_reference.html#Open_Model_Thread_Group "Link to here")
--------------------------------------------------------------------------------------------------------------------------------

This thread group is experimental, and it might change in the future releases. Please provide your feedback on what works and what could be improved.

Open Model Thread Group defines a pool of users that will execute a particular test case against the server. The users are generated according to the schedule.

The load profile consists of a sequence of constant, increasing or decreasing load. The basic configuration is rate(1/sec) random_arrivals(2 min) rate(3/sec) which means the load will increase linearly from one request per second to three requests per second during a period of two-minutes. If you omit rate at the end, then it will be set to the same value as that from the start. For example, rate(1/sec) random_arrivals(2 min) is exactly the same as rate(1/sec) random_arrivals(2 min) rate(1/sec). That is why rate(1/sec) random_arrivals(2 min) random_arrivals(3 min) rate(4/sec) is exactly the same as rate(1/sec) random_arrivals(2 min) rate(1/sec) random_arrivals(3 min) rate(4/sec), so the load is one request per second during the first two minutes, after which it increases linearly from one request per second to four requests per second during three minutes.

Here are examples for using the schedule:

rate(10/sec) random_arrivals(1 min) rate(10/sec)constant load rate of ten requests per second during one minute rate(0) random_arrivals(1 min) rate(10/sec)linearly increase the load from zero requests per second to ten requests per second during one minute rate(0) random_arrivals(1 min) rate(10/sec) random_arrivals(1 min) rate(10/sec) random_arrivals(1 min) rate(0)linearly increase the load from zero requests per second to ten requests per second during one minute, then hold the load during one minute, then linearly decrease the load from ten requests per second to zero during one minute rate(10) random_arrivals(1 min) rate(10/sec) random_arrivals(1 min) rate(10/sec) random_arrivals(1 min) rate(0)linearly increase the load from zero requests per second to ten requests per second during one minute, then hold the load during one minute, then linearly decrease the load from ten requests per second to zero requests per second during one minute rate(10) random_arrivals(1 min) pause(2 sec) random_arrivals(1 min)run with constant load of ten requests per second during one minute, then make two second pause, then resume the load of ten requests per second for one minute
The following commands are available:

rate(<number>/sec) configures target load rate. The following time units are supported: ms, sec, min, hour, day. You can omit time unit in case the rate is 0: rate(0)random_arrivals(<number> sec) configures random arrivals schedule with the given duration. The starting load rate is configured before random_arrivals, and the finish load rate is configured after random_arrivals. For example, 10 minute test from five requests per second at the beginning to fifteen request per second at the end could be configured as rate(5/sec) random_arrivals(10 min) rate(15/sec). 

 The implicit rate at the beginning of the test is 0. If the finish rate is not provided (or if several random_arrivals steps go one after another), then the load is constant. For instance, rate(3/sec) random_arrivals(1 min) random_arrivals(2 min) rate(6/sec) configures constant rate of three requests per second for the first minute, and then the load increases from three requests per second to six requests per second during the next two minutes. The time units are the same as in rate. even_arrivals(<number> sec) configures even arrivals (TODO: not implemented yet). For instance, if the desired load is one request per second, then random_arrivals would lauch samples with exactly one second intervals. pause(<number> sec) configures a pause for the given duration. The rate is restored after the pause, so rate(2/sec) random_arrivals(5 sec) pause(5 sec) random_arrivals(5 sec) generates random arrivals with two requests per second rate, then a pause for five seconds (no new arrivals), then five more seconds with two requests per second rate. 

 Note: pause duration is always honoured, even if all the scenarios are complete, and no new ones will be scheduled. For instance, if you use rate(1/sec) random_arrivals(1 min) pause(1 hour), the thread group would always last for sixty-one minutes no matter how much time do individual scenarios take. /* Comments */can be used to clarify the schedule or temporary disable some steps. Comments cannot be nested. // line comments can be used to clarify the schedule or temporary disable some steps. Line comment lasts till the end of the line. 
The thread groups terminates threads as soon as the schedule ends. In other words, the threads are interrupted after all arrivals and pause intervals. If you want to let the threads complete safely, consider adding pause(5 min) at the end of the schedule. That will add five minutes for the threads to continue.

There are no special functions for generating the load profile in a loop, however, the default JMeter templating functions can be helpful for generating the schedule.

For example, the following pattern would generate a sequence of 10 steps where each step lasts 10 seconds: 10/sec, 20/sec, 30/sec, ... ${__groovy((1..10).collect { "rate(" + it*10 + "/sec) random_arrivals(10 sec) pause(1 sec)" }.join(" "))} You can get variables from properties as follows: rate(${__P(beginRate,40)}) random_arrivals(${__P(testDuration, 10)} sec) rate(${__P(endRate,40)})

Currently, the load profile is evaluated at the beginning of the test only, so if you use dynamic functions, then only the first result will be used.

[![Image 159: Screenshot for Control-Panel of Open Model Thread Group](https://jmeter.apache.org/images/screenshots/open_model_thread_group.png)](https://jmeter.apache.org/images/screenshots/open_model_thread_group.png)

Screenshot of Control-Panel of Open Model Thread Group

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Open_Model_Thread_Group_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this thread group that is shown in the tree

No

Schedule

 The expression that configures schedule. For example: rate(5/sec) random_arrivals(1 min) pause(5 sec)

Yes

Random Seed (change from 0 to random)

Note: different thread groups should better have different seed values. Constant seed ensures thread group generates the same delays each test start. The value of "0" means the schedule is truly random (non-repeatable from one execution to another)..

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Thread Group[¶](https://jmeter.apache.org/usermanual/component_reference.html#Thread_Group "Link to here")
----------------------------------------------------------------------------------------------------------

A Thread Group defines a pool of users that will execute a particular test case against your server. In the Thread Group GUI, you can control the number of users simulated (number of threads), the ramp up time (how long it takes to start all the threads), the number of times to perform the test, and optionally, a start and stop time for the test.

See also [tearDown Thread Group](https://jmeter.apache.org/usermanual/component_reference.html#tearDown_Thread_Group) and [setUp Thread Group](https://jmeter.apache.org/usermanual/component_reference.html#setUp_Thread_Group).

When using the scheduler, JMeter runs the thread group until either the number of loops is reached or the duration/end-time is reached - whichever occurs first. Note that the condition is only checked between samples; when the end condition is reached, that thread will stop. JMeter does not interrupt samplers which are waiting for a response, so the end time may be delayed arbitrarily.

[![Image 160: Screenshot for Control-Panel of Thread Group](https://jmeter.apache.org/images/screenshots/threadgroup.png)](https://jmeter.apache.org/images/screenshots/threadgroup.png)

Screenshot of Control-Panel of Thread Group

Since JMeter 3.0, you can run a selection of Thread Group by selecting them and right clicking. A popup menu will appear:

[![Image 161: Popup menu to start a selection of Thread Groups](https://jmeter.apache.org/images/screenshots/threadgroup-popup-menu.png)](https://jmeter.apache.org/images/screenshots/threadgroup-popup-menu.png)

Popup menu to start a selection of Thread Groups

 Notice you have three options to run the selection of Thread Groups: Start Start the selected thread groups only Start no pauses Start the selected thread groups only but without running the timers Validate Start the selected thread groups only using validation mode. Per default this runs the Thread Group in validation mode (see below)**Validation Mode:**

 This mode enables rapid validation of a Thread Group by running it with one thread, one iteration, no timers and no Startup delay set to 0. Behaviour can be modified with some properties by setting in user.properties: testplan_validation.nb_threads_per_thread_group Number of threads to use to validate a Thread Group, by default 1 testplan_validation.ignore_timers Ignore timers when validating the thread group of plan, by default 1 testplan_validation.number_iterations Number of iterations to use to validate a Thread Group testplan_validation.tpc_force_100_pct Whether to force Throughput Controller in percentage mode to run as if percentage was 100 %. Defaults to false

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Thread_Group_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Action to be taken after a Sampler error

 Determines what happens if a sampler error occurs, either because the sample itself failed or an assertion failed. The possible choices are: 
*   Continue - ignore the error and continue with the test 
*   Start Next Thread Loop - ignore the error, start next loop and continue with the test 
*   Stop Thread - current thread exits 
*   Stop Test - the entire test is stopped at the end of any current samples. 
*   Stop Test Now - the entire test is stopped abruptly. Any current samplers are interrupted if possible. 

 No 

Number of Threads

Number of users to simulate.

Yes

Ramp-up Period

 How long JMeter should take to get all the threads started. If there are 10 threads and a ramp-up time of 100 seconds, then each thread will begin 10 seconds after the previous thread started, for a total time of 100 seconds to get the test fully up to speed. 

 The first thread will always start directly, so if you configured **one** thread, the ramp-up time is effectively **zero**. For the same reason, the tenth thread in the above example will actually be started after 90 seconds and not 100 seconds. 

Yes

Same user on each iteration

 If selected, cookie and cache data from the first sampler response are used in subsequent requests (requires a global Cookie and Cache Manager respectively). 

 If not selected, cookie and cache data from the first sampler response are not used in subsequent requests. 

If not selected, a new connection will be opened between iterations which will result in increased response times and consume more resources (memory and cpu).

Yes

Loop Count

 Number of times to perform the test case. Alternatively, "infinite" can be selected causing the test to run until manually stopped or end of the thread lifetime is reached. 

Yes, unless Infinite is selected

Same user on each iteration

 If selected, cookie and cache data from the first sampler response are used in subsequent requests (requires a global Cookie and Cache Manager respectively). 

 If not selected, cookie and cache data from the first sampler response are not used in subsequent requests. 

If not selected, a new connection will be opened between iterations which will result in increased response times and consume more resources (memory and cpu).

Yes

Delay Thread creation until needed

 If selected, threads are created only when the appropriate proportion of the ramp-up time has elapsed. This is most appropriate for tests with a ramp-up time that is significantly longer than the time to execute a single thread. I.e. where earlier threads finish before later ones start. 

 If not selected, all threads are created when the test starts (they then pause for the appropriate proportion of the ramp-up time). This is the original default, and is appropriate for tests where threads are active throughout most of the test. 

Yes

Specify Thread lifetime

If selected, confines Thread operation time to the given bounds

Yes

Duration (seconds)

 If the scheduler checkbox is selected, one can choose a relative end time. JMeter will use this to calculate the End Time. 

No

Startup delay (seconds)

 If the scheduler checkbox is selected, one can choose a relative startup delay. JMeter will use this to calculate the Start Time. 

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

WorkBench[¶](https://jmeter.apache.org/usermanual/component_reference.html#WorkBench "Link to here")
----------------------------------------------------------------------------------------------------

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

SSL Manager[¶](https://jmeter.apache.org/usermanual/component_reference.html#SSL_Manager "Link to here")
--------------------------------------------------------------------------------------------------------

The SSL Manager is a way to select a client certificate so that you can test applications that use Public Key Infrastructure (PKI). It is only needed if you have not set up the appropriate System properties.

 If you want to test client certificate authentication, see [Keystore Configuration](https://jmeter.apache.org/usermanual/component_reference.html#Keystore_Configuration)

**Choosing a Client Certificate**
You may either use a Java Key Store (JKS) format key store, or a Public Key Certificate Standard #12 (PKCS12) file for your client certificates. There is a feature of the JSSE libraries that require you to have at least a six character password on your key (at least for the keytool utility that comes with your JDK).

To select the client certificate, choose Options→SSL Manager from the menu bar. You will be presented with a file finder that looks for PKCS12 files by default. Your PKCS12 file must have the extension '.p12' for SSL Manager to recognize it as a PKCS12 file. Any other file will be treated like an average JKS key store. If JSSE is correctly installed, you will be prompted for the password. The text box does not hide the characters you type at this point -- so make sure no one is looking over your shoulder. The current implementation assumes that the password for the keystore is also the password for the private key of the client you want to authenticate as.

Or you can set the appropriate System properties - see the system.properties file.

The next time you run your test, the SSL Manager will examine your key store to see if it has at least one key available to it. If there is only one key, SSL Manager will select it for you. If there is more than one key, it currently selects the first key. There is currently no way to select other entries in the keystore, so the desired key must be the first.

**Things to Look Out For**
You must have your Certificate Authority (CA) certificate installed properly if it is not signed by one of the five CA certificates that ships with your JDK. One method to install it is to import your CA certificate into a JKS file, and name the JKS file "jssecacerts". Place the file in your JRE's lib/security folder. This file will be read before the "cacerts" file in the same directory. Keep in mind that as long as the "jssecacerts" file exists, the certificates installed in "cacerts" will not be used. This may cause problems for you. If you don't mind importing your CA certificate into the "cacerts" file, then you can authenticate against all of the CA certificates installed.

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

HTTP(S) Test Script Recorder[(was: HTTP Proxy Server )](https://jmeter.apache.org/usermanual/component_reference.html)[¶](https://jmeter.apache.org/usermanual/component_reference.html#HTTP(S)_Test_Script_Recorder "Link to here")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The HTTP(S) Test Script Recorder allows JMeter to intercept and record your actions while you browse your web application with your normal browser. JMeter will create test sample objects and store them directly into your test plan as you go (so you can view samples interactively while you make them). 

 Ensure you read this [wiki page](https://cwiki.apache.org/confluence/display/JMETER/TestRecording210) to setup correctly JMeter.

To use the recorder, _add_ the HTTP(S) Test Script Recorder element. Right-click on the Test Plan element to get the Add menu: (Add→Non-Test Elements→HTTP(S) Test Script Recorder ).

The recorder is implemented as an HTTP(S) proxy server. You need to set up your browser use the proxy for all HTTP and HTTPS requests.

Do not use JMeter as the proxy for any other request types - FTP, etc. - as JMeter cannot handle them.

Ideally use private browsing mode when recording the session. This should ensure that the browser starts with no stored cookies, and prevents certain changes from being saved. For example, Firefox does not allow certificate overrides to be saved permanently.

#### HTTPS recording and certificates

HTTPS connections use certificates to authenticate the connection between the browser and the web server. When connecting via HTTPS, the server presents the certificate to the browser. To authenticate the certificate, the browser checks that the server certificate is signed by a Certificate Authority (CA) that is linked to one of its in-built root CAs.

Browsers also check that the certificate is for the correct host or domain, and that it is valid and not expired.

 If any of the browser checks fail, it will prompt the user who can then decide whether to allow the connection to proceed. 
JMeter needs to use its own certificate to enable it to intercept the HTTPS connection from the browser. Effectively JMeter has to pretend to be the target server.

JMeter will generate its own certificate(s). These are generated with a validity period defined by the property proxy.cert.validity, default 7 days, and random passwords. If JMeter detects that it is running under Java 8 or later, it will generate certificates for each target server as necessary (dynamic mode) unless the following property is defined: proxy.cert.dynamic_keys=false. When using dynamic mode, the certificate will be for the correct host name, and will be signed by a JMeter-generated CA certificate. By default, this CA certificate won't be trusted by the browser, however it can be installed as a trusted certificate. Once this is done, the generated server certificates will be accepted by the browser. This has the advantage that even embedded HTTPS resources can be intercepted, and there is no need to override the browser checks for each new server.

Browsers don't prompt for embedded resources. So with earlier versions, embedded resources would only be downloaded for servers that were already 'known' to the browser

Unless a keystore is provided (and you define the property proxy.cert.alias), JMeter needs to use the keytool application to create the keystore entries. JMeter includes code to check that keytool is available by looking in various standard places. If JMeter is unable to find the keytool application, it will report an error. If necessary, the system property keytool.directory can be used to tell JMeter where to find keytool. This should be defined in the file system.properties.

The JMeter certificates are generated (if necessary) when the Start button is pressed.

Certificate generation can take some while, during which time the GUI will be unresponsive.

 The cursor is changed to an hour-glass whilst this is happening. When certificate generation is complete, the GUI will display a pop-up dialogue containing the details of the certificate for the root CA. This certificate needs to be installed by the browser in order for it to accept the host certificates generated by JMeter; see [below](https://jmeter.apache.org/usermanual/component_reference.html#install_cert) for details. 
If necessary, you can force JMeter to regenerate the keystore (and the exported certificates - ApacheJMeterTemporaryRootCA[.usr|.crt]) by deleting the keystore file proxyserver.jks from the JMeter directory.

This certificate is not one of the certificates that browsers normally trust, and will not be for the correct host. 

 As a consequence:

*    The browser should display a dialogue asking if you want to accept the certificate or not. For example: 
                                    1) The server's name "www.example.com" does not match the certificate's name
   "_ JMeter Root CA for recording (INSTALL ONLY IF IT S YOURS)". Somebody may be trying to eavesdrop on you.
2) The certificate for "_ JMeter Root CA for recording (INSTALL ONLY IF IT S YOURS)" is signed by the unknown Certificate Authority
   "_ JMeter Root CA for recording (INSTALL ONLY IF IT S YOURS)". It is not possible to verify that this is a valid certificate.

                                 You will need to accept the certificate in order to allow the JMeter Proxy to intercept the SSL traffic in order to record it. However, do not accept this certificate permanently; it should only be accepted temporarily. Browsers only prompt this dialogue for the certificate of the main URL, not for the resources loaded in the page, such as images, CSS or JavaScript files hosted on a secured external CDN. If you have such resources (gmail has for example), you'll have to first browse manually to these other domains in order to accept JMeter's certificate for them. Check in jmeter.log for secure domains that you need to register certificate for. 
*   If the browser has already registered a validated certificate for this domain, the browser will detect JMeter as a security breach and will refuse to load the page. If so, you have to remove the trusted certificate from your browser's keystore. 

Versions of JMeter from 2.10 onwards still support this method, and will continue to do so if you define the following property: proxy.cert.alias The following properties can be used to change the certificate that is used:

*   proxy.cert.directory - the directory in which to find the certificate (default = JMeter bin/) 
*   proxy.cert.file - name of the keystore file (default "proxyserver.jks") 
*   proxy.cert.keystorepass - keystore password (default "password") [Ignored if using JMeter certificate] 
*   proxy.cert.keypassword - certificate key password (default "password") [Ignored if using JMeter certificate] 
*   proxy.cert.type - the certificate type (default "JKS") [Ignored if using JMeter certificate] 
*   proxy.cert.factory - the factory (default "SunX509") [Ignored if using JMeter certificate] 
*   proxy.cert.alias - the alias for the key to be used. If this is defined, JMeter does not attempt to generate its own certificate(s). 
*   proxy.ssl.protocol - the protocol to be used (default "SSLv3") 

 If your browser currently uses a proxy (e.g. a company intranet may route all external requests via a proxy), then you need to [tell JMeter to use that proxy](https://jmeter.apache.org/usermanual/get-started.html#proxy_server) before starting JMeter, using the [command-line options](https://jmeter.apache.org/usermanual/get-started.html#options)-H and -P. This setting will also be needed when running the generated test plan. 

[](https://jmeter.apache.org/usermanual/component_reference.html)
#### Installing the JMeter CA certificate for HTTPS recording

As mentioned above, when run under Java 8, JMeter can generate certificates for each server. For this to work smoothly, the root CA signing certificate used by JMeter needs to be trusted by the browser. The first time that the recorder is started, it will generate the certificates if necessary. The root CA certificate is exported into a file with the name ApacheJMeterTemporaryRootCA in the current launch directory. When the certificates have been set up, JMeter will show a dialog with the current certificate details. At this point, the certificate can be imported into the browser, as per the instructions below.

Note that once the root CA certificate has been installed as a trusted CA, the browser will trust any certificates signed by it. Until such time as the certificate expires or the certificate is removed from the browser, it will not warn the user that the certificate is being relied upon. So anyone that can get hold of the keystore and password can use the certificate to generate certificates which will be accepted by any browsers that trust the JMeter root CA certificate. For this reason, the password for the keystore and private keys are randomly generated and a short validity period used. The passwords are stored in the local preferences area. Please ensure that only trusted users have access to the host with the keystore.

 The popup that displays once you start the Recorder is an informational popup: [![Image 162: Recorder Install Certificate Popup](https://jmeter.apache.org/images/screenshots/recorder_popup_info.png)](https://jmeter.apache.org/images/screenshots/recorder_popup_info.png)

Recorder Install Certificate Popup

 Just click ok and proceed further. 

##### Installing the certificate in Firefox

Choose the following options:

*   Tools / Options
*   Advanced / Certificates
*   View Certificates
*   Authorities
*   Import …
*    Browse to the JMeter launch directory, and click on the file ApacheJMeterTemporaryRootCA.crt, press Open
*    Click View and check that the certificate details agree with the ones displayed by the JMeter Test Script Recorder 
*    If OK, select "Trust this CA to identify web sites", and press OK
*    Close dialogs by pressing OK as necessary 

##### Installing the certificate in Chrome or Internet Explorer

Both Chrome and Internet Explorer use the same trust store for certificates.

*    Browse to the JMeter launch directory, and click on the file ApacheJMeterTemporaryRootCA.crt, and open it 
*    Click on the "Details" tab and check that the certificate details agree with the ones displayed by the JMeter Test Script Recorder 
*    If OK, go back to the "General" tab, and click on "Install Certificate …" and follow the Wizard prompts 

##### Installing the certificate in Opera

*   Tools / Preferences / Advanced / Security
*   Manage Certificates …
*    Select "Intermediate" tab, click "Import …" 
*    Browse to the JMeter launch directory, and click on the file ApacheJMeterTemporaryRootCA.usr, and open it 

[![Image 163: Screenshot for Control-Panel of HTTP(S) Test Script Recorder](https://jmeter.apache.org/images/screenshots/proxy_control.png)](https://jmeter.apache.org/images/screenshots/proxy_control.png)

Screenshot of Control-Panel of HTTP(S) Test Script Recorder

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#HTTP(S)_Test_Script_Recorder_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Port

 The port that the HTTP(S) Test Script Recorder listens to. 8888 is the default, but you can change it. 

Yes

HTTPS Domains

 List of domain (or host) names for HTTPS. Use this to pre-generate certificates for all servers you wish to record. 

 For example, *.example.com,*.subdomain.example.com

 Note that wildcard domains only apply to one level, i.e. abc.subdomain.example.com matches *.subdomain.example.com but not *.example.com

No

Target Controller

The controller where the proxy will store the generated samples. By default, it will look for a Recording Controller and store them there wherever it is.

Yes

Grouping

 Whether to group samplers for requests from a single "click" (requests received without significant time separation), and how to represent that grouping in the recording: 
*   Do not group samplers - store all recorded samplers sequentially, without any grouping. 
*   Add separators between groups - add a controller named "--------------" to create a visual separation between the groups. Otherwise the samplers are all stored sequentially. 
*   Put each group in a new controller - create a new [Simple Controller](https://jmeter.apache.org/usermanual/component_reference.html#Simple_Controller) for each group, and store all samplers for that group in it. 
*   Store 1 st sampler of each group only - only the first request in each group will be recorded. The "Follow Redirects" and "Retrieve All Embedded Resources …" flags will be turned on in those samplers. 
*   Put each group in a new transaction controller - create a new [Transaction Controller](https://jmeter.apache.org/usermanual/component_reference.html#Transaction_Controller) for each group, and store all samplers for that group in it. 

 The property proxy.pause determines the minimum gap that JMeter needs between requests to treat them as separate "clicks". The default is 5000 (milliseconds) i.e. 5 seconds. If you are using grouping, please ensure that you leave the required gap between clicks. 

Yes

Capture HTTP Headers

 Should headers be added to the plan? If specified, a Header Manager will be added to each HTTP Sampler. The Proxy server always removes Cookie and Authorization headers from the generated Header Managers. By default it also removes If-Modified-Since and If-None-Match headers. These are used to determine if the browser cache items are up to date; when recording one normally wants to download all the content. To change which additional headers are removed, define the JMeter property proxy.headers.remove as a comma-separated list of headers. 

Yes

Add Assertions

Add a blank assertion to each sampler?

Yes

Regex Matching

 Use Regex Matching when replacing variables? If checked replacement will use word boundaries, i.e. it will only replace word matching values of variable, not part of a word. A word boundary follows Perl5 definition and is equivalent to \b. More information below in the paragraph about "User Defined Variable replacement". 

Yes

Prefix/Transaction name

Add a prefix to sampler name during recording (Prefix mode). Or replace sampler name by user chosen name (Transaction name)

No

Naming scheme

 Select the naming scheme for sampler names during recording. Default is Transaction name

No

Naming format

 If Use format string is selected as naming scheme, a freestyle format can be given. Placeholders for the transaction name, scheme, host, port, path and counter can be given by #{name}, #{scheme}, #{host}, #{port}, #{path}, #{url} and #{counter}. A simple format could be "#{name}-#{counter}", which would be equivalent to the numbered default naming scheme. For more complex formatting Java formatting for MessageFormat can be used, as in "#{counter,number,000}: #{name}-#{path}", which would print the counter filled with up to three zeroes. Note that scheme is called protocol in the sampler GUI and host is called domain. Default is an empty string. 

No

Counter start value

 Can be used to reset the counter to a given value. Note, that the next sample will first increment and then use the value. If the first sampler should start with 1, reset the counter to 0. 

No

Create new transaction after request (ms)

Inactivity time between two requests needed to consider them in two separate groups.

 No 

Type

Which type of sampler to generate (the HTTPClient default or Java)

Yes

Redirect Automatically

Set Redirect Automatically in the generated samplers?

Yes

Follow Redirects

 Set Follow Redirects in the generated samplers? 

Note: see "Recording and redirects" section below for important information.

Yes

Use Keep-Alive

Set Use Keep-Alive in the generated samplers?

Yes

Retrieve all Embedded Resources

Set Retrieve all Embedded Resources in the generated samplers?

Yes

Content Type filter

 Filter the requests based on the content-type - e.g. "text/html [;charset=utf-8 ]". The fields are regular expressions which are checked to see if they are contained in the content-type. [Does not have to match the entire field]. The include filter is checked first, then the exclude filter. Samples which are filtered out will not be stored. 

Note: this filtering is applied to the content type of the response

No

Patterns to Include

 Regular expressions that are matched against the full URL that is sampled. Allows filtering of requests that are recorded. All requests pass through, but only those that meet the requirements of the Include/Exclude fields are _recorded_. If both Include and Exclude are left empty, then everything is recorded (which can result in dozens of samples recorded for each page, as images, stylesheets, etc. are recorded). 

 If there is at least one entry in the Include field, then only requests that match one or more Include patterns are recorded 

 . 

No

Patterns to Exclude

 Regular expressions that are matched against the URL that is sampled. 

 Any requests that match one or more Exclude pattern are _not_ recorded 

 . 

No

Notify Child Listeners of filtered samplers

 Notify Child Listeners of filtered samplers 

 Any response that match one or more Exclude pattern is _not_ delivered to Child Listeners (View Results Tree) 

 . 

No

Start Button

 Start the proxy server. JMeter writes the following message to the console once the proxy server has started up and is ready to take requests: "Proxy up and running!". 

N/A

Stop Button

Stop the proxy server.

N/A

Restart Button

Stops and restarts the proxy server. This is useful when you change/add/delete an include/exclude filter expression.

N/A

#### Recording and redirects

During recording, the browser will follow a redirect response and generate an additional request. The Proxy will record both the original request and the redirected request (subject to whatever exclusions are configured). The generated samples have "Follow Redirects" selected by default, because that is generally better.

Redirects may depend on the original request, so repeating the originally recorded sample may not always work.

Now if JMeter is set to follow the redirect during replay, it will issue the original request, and then replay the redirect request that was recorded. To avoid this duplicate replay, JMeter tries to detect when a sample is the result of a previous redirect. If the current response is a redirect, JMeter will save the redirect URL. When the next request is received, it is compared with the saved redirect URL and if there is a match, JMeter will disable the generated sample. It also adds comments to the redirect chain. This assumes that all the requests in a redirect chain will follow each other without any intervening requests. To disable the redirect detection, set the property proxy.redirect.disabling=false

#### Includes and Excludes

The **include and exclude patterns** are treated as regular expressions (using Jakarta ORO). They will be matched against the host name, port (actual or implied), path and query (if any) of each browser request. If the URL you are browsing is 

 "http://localhost/jmeter/index.html?username=xxxx", 

 then the regular expression will be tested against the string: 

 "localhost:80/jmeter/index.html?username=xxxx". 

 Thus, if you want to include all .html files, your regular expression might look like: 

 ".*\.html(\?.*)?" - or ".*\.html if you know that there is no query string or you only want html pages without query strings.

If there are any include patterns, then the URL **must match at least one** of the patterns , otherwise it will not be recorded. If there are any exclude patterns, then the URL **must not match any** of the patterns , otherwise it will not be recorded. Using a combination of includes and excludes, you should be able to record what you are interested in and skip what you are not.

 N.B. the string that is matched by the regular expression must be the same as the **whole** host+path string. 

 Thus "\.html" will **not** match localhost:80/index.html

#### Capturing binary POST data

JMeter is able to capture binary POST data. To configure which content-types are treated as binary, update the JMeter property proxy.binary.types. The default settings are as follows:

# These content-types will be handled by saving the request in a file:
proxy.binary.types=application/x-amf,application/x-java-serialized-object
# The files will be saved in this directory:
proxy.binary.directory=user.dir
# The files will be created with this file filesuffix:
proxy.binary.filesuffix=.binary

#### Adding timers

It is also possible to have the proxy add timers to the recorded script. To do this, create a timer directly within the HTTP(S) Test Script Recorder component. The proxy will place a copy of this timer into each sample it records, or into the first sample of each group if you're using grouping. This copy will then be scanned for occurrences of variable ${T} in its properties, and any such occurrences will be replaced by the time gap from the previous sampler recorded (in milliseconds).

When you are ready to begin, hit "start".

You will need to edit the proxy settings of your browser to point at the appropriate server and port, where the server is the machine JMeter is running on, and the port # is from the Proxy Control Panel shown above.

#### Where Do Samples Get Recorded?

JMeter places the recorded samples in the Target Controller you choose. If you choose the default option "Use Recording Controller", they will be stored in the first Recording Controller found in the test object tree (so be sure to add a Recording Controller before you start recording).

If the Proxy does not seem to record any samples, this could be because the browser is not actually using the proxy. To check if this is the case, try stopping the proxy. If the browser still downloads pages, then it was not sending requests via the proxy. Double-check the browser options. If you are trying to record from a server running on the same host, then check that the browser is not set to "Bypass proxy server for local addresses" (this example is from IE7, but there will be similar options for other browsers). If JMeter does not record browser URLs such as http://localhost/ or http://127.0.0.1/, try using the non-loopback hostname or IP address, e.g. http://myhost/ or http://192.168.0.2/.

#### Handling of HTTP Request Defaults

If the HTTP(S) Test Script Recorder finds enabled [HTTP Request Defaults](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request_Defaults) directly within the controller where samples are being stored, or directly within any of its parent controllers, the recorded samples will have empty fields for the default values you specified. You may further control this behaviour by placing an HTTP Request Defaults element directly within the HTTP(S) Test Script Recorder, whose non-blank values will override those in the other HTTP Request Defaults. See [Best Practices with the HTTP(S) Test Script Recorder](https://jmeter.apache.org/usermanual/best-practices.html#proxy_server) for more info.

#### User Defined Variable replacement

Similarly, if the HTTP(S) Test Script Recorder finds [User Defined Variables](https://jmeter.apache.org/usermanual/component_reference.html#User_Defined_Variables) (UDV) directly within the controller where samples are being stored, or directly within any of its parent controllers, the recorded samples will have any occurrences of the values of those variables replaced by the corresponding variable. Again, you can place User Defined Variables directly within the HTTP(S) Test Script Recorder to override the values to be replaced. See [Best Practices with the Test Script Recorder](https://jmeter.apache.org/usermanual/best-practices.html#proxy_server) for more info.

Please note that matching is case-sensitive.

Replacement by Variables: by default, the Proxy server looks for all occurrences of UDV values. If you define the variable WEB with the value www, for example, the string www will be replaced by ${WEB} wherever it is found. To avoid this happening everywhere, set the "Regex Matching" check-box. This tells the proxy server to treat values as Regexes (using the perl5 compatible regex matchers provided by ORO).

If "Regex Matching" is selected every variable will be compiled into a perl compatible regex enclosed in \b( and )\b. That way each match will start and end at a word boundary.

 Note that the boundary characters are not part of the matching group, e.g. n.* to match name out of You can call me 'name'. 

If you don't want your regex to be enclosed with those boundary matchers, you have to enclose your regex within parens, e.g ('.*?') to match 'name' out of You can call me 'name'.

 The variables will be checked in random order. So ensure, that the potential matches don't overlap. Overlapping matchers would be .* (which matches anything) and www (which matches www only). Non-overlapping matchers would be a+ (matches a sequence of a's) and b+ (matches a sequence of b's). 

If you want to match a whole string only, enclose it in (^ and $), e.g. (^thus$). The parens are necessary, since the normally added boundary characters will prevent ^ and $ to match.

If you want to match /images at the start of a string only, use the value (^/images). Jakarta ORO also supports zero-width look-ahead, so one can match /images/… but retain the trailing / in the output by using (^/images(?=/)).

 Note that the current version of Jakarta ORO does not support look-behind - i.e. (?<=…) or (?<!…). 

Look out for overlapping matchers. For example the value .* as a regex in a variable named regex will partly match a previous replaced variable, which will result in something like ${{regex}, which is most probably not the desired result.

If there are any problems interpreting any variables as patterns, these are reported in jmeter.log, so be sure to check this if UDVs are not working as expected.

When you are done recording your test samples, stop the proxy server (hit the "stop" button). Remember to reset your browser's proxy settings. Now, you may want to sort and re-order the test script, add timers, listeners, a cookie manager, etc.

#### How can I record the server's responses too?

Just place a [View Results Tree](https://jmeter.apache.org/usermanual/component_reference.html#View_Results_Tree) listener as a child of the HTTP(S) Test Script Recorder and the responses will be displayed. You can also add a [Save Responses to a file](https://jmeter.apache.org/usermanual/component_reference.html#Save_Responses_to_a_file) Post-Processor which will save the responses to files.

#### Associating requests with responses

If you define the property proxy.number.requests=true JMeter will add a number to each sampler and each response. Note that there may be more responses than samplers if excludes or includes have been used. Responses that have been excluded will have labels enclosed in [ and ], for example [23 /favicon.ico]

#### Cookie Manager

If the server you are testing against uses cookies, remember to add an [HTTP Cookie Manager](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Cookie_Manager) to the test plan when you have finished recording it. During recording, the browser handles any cookies, but JMeter needs a Cookie Manager to do the cookie handling during a test run. The JMeter Proxy server passes on all cookies sent by the browser during recording, but does not save them to the test plan because they are likely to change between runs.

#### Authorization Manager

The HTTP(S) Test Script Recorder grabs "Authentication" header, tries to compute the Auth Policy. If Authorization Manager was added to target controller manually, HTTP(S) Test Script Recorder will find it and add authorization (matching ones will be removed). Otherwise Authorization Manager will be added to target controller with authorization object. You may have to fix automatically computed values after recording.

#### Uploading files

Some browsers (e.g. Firefox and Opera) don't include the full name of a file when uploading files. This can cause the JMeter proxy server to fail. One solution is to ensure that any files to be uploaded are in the JMeter working directory, either by copying the files there or by starting JMeter in the directory containing the files.

#### Recording HTTP Based Non Textual Protocols not natively available in JMeter

You may have to record an HTTP protocol that is not handled by default by JMeter (Custom Binary Protocol, Adobe Flex, Microsoft Silverlight, … ). Although JMeter does not provide a native proxy implementation to record these protocols, you have the ability to record these protocols by implementing a custom SamplerCreator. This Sampler Creator will translate the binary format into a HTTPSamplerBase subclass that can be added to the JMeter Test Case. For more details see "Extending JMeter".

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

HTTP Mirror Server[¶](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Mirror_Server "Link to here")
----------------------------------------------------------------------------------------------------------------------

The HTTP Mirror Server is a very simple HTTP server - it simply mirrors the data sent to it. This is useful for checking the content of HTTP requests.

It uses default port 8081.

[![Image 164: Screenshot for Control-Panel of HTTP Mirror Server](https://jmeter.apache.org/images/screenshots/mirrorserver.png)](https://jmeter.apache.org/images/screenshots/mirrorserver.png)

Screenshot of Control-Panel of HTTP Mirror Server

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Mirror_Server_parms1 "Link to here")

Attribute

Description

Required

Port

 Port on which Mirror server listens, defaults to 8081. 

Yes

Max Number of threads

 If set to a value >0, number of threads serving requests will be limited to the configured number, if set to a value ≤ 0 a new thread will be created to serve each incoming request. Defaults to 0

No

Max Queue size

 Size of queue used for holding tasks before they are executed by Thread Pool, when Thread pool is exceeded, incoming requests will be held in this queue and discarded when this queue is full. This parameter is only used if Max Number of Threads is greater than 0. Defaults to 25

No

 Note that you can get more control over the responses by adding an HTTP Header Manager with the following name/value pairs: 

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Mirror_Server_parms2 "Link to here")

Attribute

Description

Required

X-Sleep

Time to sleep in ms before sending response

No

X-SetCookie

Cookies to be set on response

No

X-ResponseStatus

 Response status, see [HTTP Status responses](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html), example 200 OK, 500 Internal Server Error, …. 

No

X-ResponseLength

Size of response, this trims the response to the requested size if that is less than the total size

No

X-SetHeaders

 Pipe separated list of headers, example: 

headerA: valueA|headerB: valueB would set headerA to valueA and headerB to valueB. 

No

You can also use the following query parameters:

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Mirror_Server_parms3 "Link to here")

Attribute

Description

Required

redirect

 Generates a 302 (Temporary Redirect) with the provided location, e.g. ?redirect=/path

No

status

 Overrides the default status return, e.g. ?status=404 Not Found

No

v

Verbose flag, writes some details to standard output, e.g. first line and redirect location if specified

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Property Display[¶](https://jmeter.apache.org/usermanual/component_reference.html#Property_Display "Link to here")
------------------------------------------------------------------------------------------------------------------

The Property Display shows the values of System or JMeter properties. Values can be changed by entering new text in the Value column.

[![Image 165: Screenshot for Control-Panel of Property Display](https://jmeter.apache.org/images/screenshots/property_display.png)](https://jmeter.apache.org/images/screenshots/property_display.png)

Screenshot of Control-Panel of Property Display

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Property_Display_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Debug Sampler[¶](https://jmeter.apache.org/usermanual/component_reference.html#Debug_Sampler "Link to here")
------------------------------------------------------------------------------------------------------------

The Debug Sampler generates a sample containing the values of all JMeter variables and/or properties.

The values can be seen in the [View Results Tree](https://jmeter.apache.org/usermanual/component_reference.html#View_Results_Tree) Listener Response Data pane.

[![Image 166: Screenshot for Control-Panel of Debug Sampler](https://jmeter.apache.org/images/screenshots/debug_sampler.png)](https://jmeter.apache.org/images/screenshots/debug_sampler.png)

Screenshot of Control-Panel of Debug Sampler

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Debug_Sampler_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

JMeter Properties

Include JMeter properties?

Yes

JMeter Variables

Include JMeter variables?

Yes

System Properties

Include System properties?

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Debug PostProcessor[¶](https://jmeter.apache.org/usermanual/component_reference.html#Debug_PostProcessor "Link to here")
------------------------------------------------------------------------------------------------------------------------

The Debug PostProcessor creates a subSample with the details of the previous Sampler properties, JMeter variables, properties and/or System Properties.

The values can be seen in the [View Results Tree](https://jmeter.apache.org/usermanual/component_reference.html#View_Results_Tree) Listener Response Data pane.

[![Image 167: Screenshot for Control-Panel of Debug PostProcessor](https://jmeter.apache.org/images/screenshots/debug_postprocessor.png)](https://jmeter.apache.org/images/screenshots/debug_postprocessor.png)

Screenshot of Control-Panel of Debug PostProcessor

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Debug_PostProcessor_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

JMeter Properties

 Whether to show JMeter properties (default false). 

Yes

JMeter Variables

 Whether to show JMeter variables (default false). 

Yes

Sampler Properties

 Whether to show Sampler properties (default true). 

Yes

System Properties

 Whether to show System properties (default false). 

Yes

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

Test Fragment[¶](https://jmeter.apache.org/usermanual/component_reference.html#Test_Fragment "Link to here")
------------------------------------------------------------------------------------------------------------

The Test Fragment is used in conjunction with the [Include Controller](https://jmeter.apache.org/usermanual/component_reference.html#Include_Controller) and [Module Controller](https://jmeter.apache.org/usermanual/component_reference.html#Module_Controller).

[![Image 168: Screenshot for Control-Panel of Test Fragment](https://jmeter.apache.org/images/screenshots/test_fragment.png)](https://jmeter.apache.org/images/screenshots/test_fragment.png)

Screenshot of Control-Panel of Test Fragment

### Parameters [¶](https://jmeter.apache.org/usermanual/component_reference.html#Test_Fragment_parms1 "Link to here")

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Yes

 When using Test Fragment with [Module Controller](https://jmeter.apache.org/usermanual/component_reference.html#Module_Controller), ensure you disable the Test Fragment to avoid the execution of Test Fragment itself. This is done by default since JMeter 2.13. 

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

setUp Thread Group[¶](https://jmeter.apache.org/usermanual/component_reference.html#setUp_Thread_Group "Link to here")
----------------------------------------------------------------------------------------------------------------------

A special type of ThreadGroup that can be utilized to perform Pre-Test Actions. The behavior of these threads is exactly like a normal [Thread Group](https://jmeter.apache.org/usermanual/component_reference.html#Thread_Group) element. The difference is that these type of threads execute before the test proceeds to the executing of regular Thread Groups.

[![Image 169: Screenshot for Control-Panel of setUp Thread Group](https://jmeter.apache.org/images/screenshots/setup_thread_group.png)](https://jmeter.apache.org/images/screenshots/setup_thread_group.png)

Screenshot of Control-Panel of setUp Thread Group

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

tearDown Thread Group[¶](https://jmeter.apache.org/usermanual/component_reference.html#tearDown_Thread_Group "Link to here")
----------------------------------------------------------------------------------------------------------------------------

A special type of ThreadGroup that can be utilized to perform Post-Test Actions. The behavior of these threads is exactly like a normal [Thread Group](https://jmeter.apache.org/usermanual/component_reference.html#Thread_Group) element. The difference is that these type of threads execute after the test has finished executing its regular Thread Groups.

[![Image 170: Screenshot for Control-Panel of tearDown Thread Group](https://jmeter.apache.org/images/screenshots/teardown_thread_group.png)](https://jmeter.apache.org/images/screenshots/teardown_thread_group.png)

Screenshot of Control-Panel of tearDown Thread Group

 Note that by default it won't run if Test is gracefully shutdown, if you want to make it run in this case, ensure you check option "Run tearDown Thread Groups after shutdown of main threads" on Test Plan element. If Test Plan is stopped, tearDown will not run even if option is checked. 

[![Image 171: Figure 1 - Run tearDown Thread Groups after shutdown of main threads](https://jmeter.apache.org/images/screenshots/tear_down_on_shutdown.png)](https://jmeter.apache.org/images/screenshots/tear_down_on_shutdown.png)

Figure 1 - Run tearDown Thread Groups after shutdown of main threads

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

[^](https://jmeter.apache.org/usermanual/component_reference.html#)

*   [< Prev](https://jmeter.apache.org/usermanual/boss.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/properties_reference.html)

 Share this page: 
*   [share](https://jmeter.apache.org/usermanual/component_reference.html "Share on facebook")
*   [tweet](https://jmeter.apache.org/usermanual/component_reference.html "Tweet on twitter")

[Go to top](https://jmeter.apache.org/usermanual/component_reference.html#top)

 Copyright © 1999 – 2024 , Apache Software Foundation 

Apache, Apache JMeter, JMeter, the Apache feather, and the Apache JMeter logo are trademarks of the Apache Software Foundation.
