# Source: https://jmeter.apache.org/usermanual/best-practices.html

Title: Apache JMeter
          -
          User's Manual: Best Practices

URL Source: https://jmeter.apache.org/usermanual/best-practices.html

Published Time: Sun, 07 Jan 2024 17:19:24 GMT

Markdown Content:
Apache JMeter - User's Manual: Best Practices
===============
[Main content](https://jmeter.apache.org/usermanual/best-practices.html#content)

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

*   [< Prev](https://jmeter.apache.org/usermanual/realtime-results.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/boss.html)

16. Best Practices[¶](https://jmeter.apache.org/usermanual/best-practices.html#best_practices "Link to here")
=============================================================================================================

16.1 Always use latest version of JMeter[¶](https://jmeter.apache.org/usermanual/best-practices.html#use_latest_version "Link to here")
=======================================================================================================================================

The performance of JMeter is being constantly improved, so users are highly encouraged to use the most up to date version. 

 Ensure you always read [changes list](https://jmeter.apache.org/changes.html) to be aware of new improvements and components. You should absolutely avoid using versions that are older than 3 versions before the last one.

16.2 Use the correct Number of Threads[¶](https://jmeter.apache.org/usermanual/best-practices.html#sizing_threads "Link to here")
=================================================================================================================================

Your hardware capabilities as well as the Test Plan design will both impact the number of threads you can effectively run with JMeter. The number will also depend on how fast your server is (a faster server makes JMeter work harder since it returns a response quicker). As with any Load Testing tool, if you don't correctly size the number of threads, you will face the "Coordinated Omission" problem which can give you wrong or inaccurate results. If you need large-scale load testing, consider running multiple CLI JMeter instances on multiple machines using distributed mode (or not). When using distributed mode the result file is combined on the Controller node, if using multiple autonomous instances, the sample result files can be combined for subsequent analysis. For testing how JMeter performs on a given platform, the JavaTest sampler can be used. It does not require any network access so can give some idea as to the maximum throughput achievable.

JMeter has an option to delay thread creation until the thread starts sampling, i.e. after any thread group delay and the ramp-up time for the thread itself. This allows for a very large total number of threads, provided that not too many are active concurrently.

16.3 Where to Put the Cookie Manager[¶](https://jmeter.apache.org/usermanual/best-practices.html#put_cookie_manager "Link to here")
===================================================================================================================================

See [Building a Web Test](https://jmeter.apache.org/usermanual/build-web-test-plan.html#adding_cookie_support) for information.

16.4 Where to Put the Authorization Manager[¶](https://jmeter.apache.org/usermanual/best-practices.html#put_auth_manager "Link to here")
========================================================================================================================================

See [Building an Advanced Web Test](https://jmeter.apache.org/usermanual/build-adv-web-test-plan.html#header_manager) for information.

16.5 Using the HTTP(S) Test Script Recorder[¶](https://jmeter.apache.org/usermanual/best-practices.html#proxy_server "Link to here")
====================================================================================================================================

Refer to [HTTP(S) Test Script Recorder](https://jmeter.apache.org/usermanual/component_reference.html#HTTP(S)_Test_Script_Recorder) for details on setting up the recorder. The most important thing to do is filter out all requests you aren't interested in. For instance, there's no point in recording image requests (JMeter can be instructed to download all images on a page - see [HTTP Request](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request)). These will just clutter your test plan. Most likely, there is an extension all your files share, such as .jsp, .asp, .php, .html or the like. These you should "include" by entering ".*\.jsp" as an "Include Pattern".

Alternatively, you can exclude images by entering ".*\.gif" as an "Exclude Pattern". Depending on your application, this may or may not be a better way to go. You may also have to exclude stylesheets, javascript files, and other included files. Test out your settings to verify you are recording what you want, and then erase and start fresh.

The HTTP(S) Test Script Recorder expects to find a ThreadGroup element with a Recording Controller under it where it will record HTTP Requests to. This conveniently packages all your samples under one controller, which can be given a name that describes the test case.

Now, go through the steps of a Test Case. If you have no pre-defined test cases, use JMeter to record your actions to define your test cases. Once you have finished a definite series of steps, save the entire test case in an appropriately named file. Then, wipe clean and start a new test case. By doing this, you can quickly record a large number of test case "rough drafts".

One of the most useful features of the HTTP(S) Test Script Recorder is that you can abstract out certain common elements from the recorded samples. By defining some [user-defined variables](https://jmeter.apache.org/usermanual/functions.html) at the Test Plan level or in [User Defined Variables](https://jmeter.apache.org/usermanual/component_reference.html#User_Defined_Variables) elements, you can have JMeter automatically replace values in you recorded samples. For instance, if you are testing an app on server "xxx.example.com", then you can define a variable called "server" with the value of "xxx.example.com", and anyplace that value is found in your recorded samples will be replaced with "${server}".

Please note that matching is case-sensitive.

If JMeter does not record any samples, check that the browser really is using the proxy. If the browser works OK even if JMeter is not running, then the browser cannot be using the proxy. Some browsers ignore proxy settings for localhost or 127.0.0.1; try using the local hostname or IP instead.

The error "unknown_ca" probably means that you are trying to record HTTPS, and the browser has not accepted the JMeter Proxy server certificate.

16.6 User variables[¶](https://jmeter.apache.org/usermanual/best-practices.html#user_variables "Link to here")
==============================================================================================================

Some test plans need to use different values for different users/threads. For example, you might want to test a sequence that requires a unique login for each user. This is easy to achieve with the facilities provided by JMeter.

For example:

*   Create a text file containing the user names and passwords, separated by commas. Put this in the same directory as your test plan. 
*    Add a CSV DataSet configuration element to the test plan. Name the variables USER and PASS. 
*    Replace the login name with ${USER} and the password with ${PASS} on the appropriate samplers 

The CSV Data Set element will read a new line for each thread.

16.7 Reducing resource requirements[¶](https://jmeter.apache.org/usermanual/best-practices.html#lean_mean "Link to here")
=========================================================================================================================

Some suggestions on reducing resource usage.

*    Use CLI mode: jmeter -n -t test.jmx -l test.jtl
*    Use as few Listeners as possible; if using the -l flag as above they can all be deleted or disabled. 
*   Don't use "View Results Tree" or "View Results in Table" listeners during the load test, use them only during scripting phase to debug your scripts.
*   Rather than using lots of similar samplers, use the same sampler in a loop, and use variables (CSV Data Set) to vary the sample. [The Include Controller does not help here, as it adds all the test elements in the file to the test plan.] 
*   Don't use functional mode
*   Use CSV output rather than XML
*   Only save the data that you need
*   Use as few Assertions as possible
*   Use the most performing scripting language (see JSR223 section)

If your test needs large amounts of data - particularly if it needs to be randomised - create the test data in a file that can be read with CSV Dataset. This avoids wasting resources at run-time.

16.8 BeanShell server[¶](https://jmeter.apache.org/usermanual/best-practices.html#beanshell_server "Link to here")
==================================================================================================================

The BeanShell interpreter has a very useful feature - it can act as a server, which is accessible by telnet or http.

 There is no security. Anyone who can connect to the port can issue any BeanShell commands. These can provide unrestricted access to the JMeter application and the host. **Do not enable the server unless the ports are protected against access, e.g. by a firewall.**

If you do wish to use the server, define the following in jmeter.properties:

beanshell.server.port=9000
beanshell.server.file=../extras/startup.bsh

In the above example, the server will be started, and will listen on ports 9000 and 9001. Port 9000 will be used for http access. Port 9001 will be used for telnet access. The startup.bsh file will be processed by the server, and can be used to define various functions and set up variables. The startup file defines methods for setting and printing JMeter and system properties. This is what you should see in the JMeter console:

Startup script running
Startup script completed
Httpd started on port: 9000
Session started on port: 9001

There is a sample script (extras/remote.bsh) you can use to test the server. [Have a look at it to see how it works.] 

 When starting it in the JMeter bin directory (adjust paths as necessary if running from elsewhere) the output should look like:

$ java -jar ../lib/bshclient.jar localhost 9000 ../extras/remote.bsh
Connecting to BSH server on localhost:9000
Reading responses from server …
BeanShell 2.0b5 - by Pat Niemeyer (pat@pat.net)
bsh % remote.bsh starting
user.home = C:\Documents and Settings\User
user.dir = D:\eclipseworkspaces\main\JMeter_trunk\bin
Setting property 'EXAMPLE' to '0'.
Setting property 'EXAMPLE' to '1'.
Setting property 'EXAMPLE' to '2'.
Setting property 'EXAMPLE' to '3'.
Setting property 'EXAMPLE' to '4'.
Setting property 'EXAMPLE' to '5'.
Setting property 'EXAMPLE' to '6'.
Setting property 'EXAMPLE' to '7'.
Setting property 'EXAMPLE' to '8'.
Setting property 'EXAMPLE' to '9'.
EXAMPLE = 9
remote.bsh ended
bsh % … disconnected from server.

As a practical example, assume you have a long-running JMeter test running in CLI mode, and you want to vary the throughput at various times during the test. The test-plan includes a Constant Throughput Timer which is defined in terms of a property, e.g. ${__P(throughput)}. The following BeanShell commands could be used to change the test:

printprop("throughput");
curr = Integer.decode(args[0]);  // Start value
inc  = Integer.decode(args[1]);  // Increment
end  = Integer.decode(args[2]);  // Final value
secs = Integer.decode(args[3]);  // Wait between changes
while(curr <= end) {
  setprop("throughput",curr.toString()); // Needs to be a string here
  Thread.sleep(secs*1000);
  curr += inc;
}
printprop("throughput");

The script can be stored in a file (throughput.bsh, say), and sent to the server using bshclient.jar. For example:

java -jar ../lib/bshclient.jar localhost 9000 throughput.bsh 70 5 100 60

16.9 BeanShell scripting[¶](https://jmeter.apache.org/usermanual/best-practices.html#bsh_scripting "Link to here")
==================================================================================================================

 Since JMeter 3.1, we advise switching from BeanShell to JSR223 Test Elements (see JSR223 section below for more details), and switching from [__Beanshell](https://jmeter.apache.org/usermanual/functions.html#__BeanShell) function to [__groovy](https://jmeter.apache.org/usermanual/functions.html#__groovy) function. 

16.9.1 Overview[¶](https://jmeter.apache.org/usermanual/best-practices.html#bsh_overview "Link to here")
--------------------------------------------------------------------------------------------------------

Each BeanShell test element has its own copy of the interpreter (for each thread). If the test element is repeatedly called, e.g. within a loop, then the interpreter is retained between invocations unless the "Reset bsh.Interpreter before each call" option is selected.

Some long-running tests may cause the interpreter to use lots of memory; if this is the case try using the reset option.

You can test BeanShell scripts outside JMeter by using the command-line interpreter:

$ java -cp bsh-xxx.jar[;other jars as needed] bsh.Interpreter file.bsh [parameters]
 or 
$ java -cp bsh-xxx.jar bsh.Interpreter
bsh% source("file.bsh");
bsh% exit(); // or use EOF key (e.g. ^Z or ^D)

16.9.2 Sharing Variables[¶](https://jmeter.apache.org/usermanual/best-practices.html#bsh_variables "Link to here")
------------------------------------------------------------------------------------------------------------------

Variables can be defined in startup (initialisation) scripts. These will be retained across invocations of the test element, unless the reset option is used.

Scripts can also access JMeter variables using the get() and put() methods of the "vars" variable, for example:

vars.get("HOST");
vars.put("MSG","Successful"); The get() and put() methods only support variables with String values, but there are also getObject() and putObject() methods which can be used for arbitrary objects. JMeter variables are local to a thread, but can be used by all test elements (not just Beanshell). 
If you need to share variables between threads, then JMeter properties can be used:

import org.apache.jmeter.util.JMeterUtils;
String value = JMeterUtils.getPropDefault("name","");
JMeterUtils.setProperty("name", "value");
 The sample .bshrc files contain sample definitions of getprop() and setprop() methods. 
Another possible method of sharing variables is to use the "bsh.shared" shared namespace. For example:

if (bsh.shared.myObj == void){
    // not yet defined, so create it:
    myObj = new AnyObject();
}
bsh.shared.myObj.process();
 Rather than creating the object in the test element, it can be created in the startup file defined by the JMeter property "beanshell.init.file". This is only processed once. 

16.10 Developing script functions in Groovy or Jexl3 etc.[¶](https://jmeter.apache.org/usermanual/best-practices.html#developing_scripts "Link to here")
========================================================================================================================================================

It's quite hard to write and test scripts as functions. However, JMeter has the JSR223 samplers which can be used instead with any language supporting it. We advise using [Apache Groovy](http://www.groovy-lang.org/) or any language that supports the [Compilable](https://docs.oracle.com/javase/8/docs/api/javax/script/Compilable.html) interface of JSR223.

Create a simple Test Plan containing the JSR223 Sampler and Tree View Listener. Code the script in the sampler script pane, and test it by running the test. If there are any errors, these will show up in the Tree View and jmeter.log file. Also the result of running the script will show up as the response.

Once the script is working properly, it can be stored as a variable on the Test Plan. The script variable can then be used to create the function call. For example, suppose a Groovy script is stored in the variable RANDOM_NAME. The function call can then be coded as ${__groovy(${RANDOM_NAME})}. There is no need to escape any commas in the script, because the function call is parsed before the variable's value is interpolated.

16.11 Parameterising tests[¶](https://jmeter.apache.org/usermanual/best-practices.html#parameterising_tests "Link to here")
===========================================================================================================================

Often it is useful to be able to re-run the same test with different settings. For example, changing the number of threads or loops, or changing a hostname.

One way to do this is to define a set of variables on the Test Plan, and then use those variables in the test elements. For example, one could define the variable LOOPS=10, and refer to that in the Thread Group as ${LOOPS}. To run the test with 20 loops, just change the value of the LOOPS variable on the Test Plan.

This quickly becomes tedious if you want to run lots of tests in CLI mode. One solution to this is to define the Test Plan variable in terms of a property, for example LOOPS=${__P(loops,10)}. This uses the value of the property "loops", defaulting to 10 if the property is not found. The "loops" property can then be defined on the JMeter command-line:

jmeter … -Jloops=12 … If there are a lot of properties that need to be changed together, then one way to achieve this is to use a set of property files. The appropriate property file can be passed in to JMeter using the -q command-line option. 

16.12 JSR223 Elements[¶](https://jmeter.apache.org/usermanual/best-practices.html#jsr223 "Link to here")
========================================================================================================

For intensive load testing, the recommended scripting language is one whose ScriptingEngine implements the [Compilable](https://docs.oracle.com/javase/8/docs/api/javax/script/Compilable.html) interface. Groovy scripting engine implements [Compilable](https://docs.oracle.com/javase/8/docs/api/javax/script/Compilable.html). However neither Beanshell nor Javascript do so as of release date of JMeter 3.1, so it is recommended to avoid them for intensive load testing.

 Note: Beanshell implements the [Compilable](https://docs.oracle.com/javase/8/docs/api/javax/script/Compilable.html) interface but it has not been coded - the method just throws an Exception. JMeter has an explicit work-round for this bug. 

 When using JSR 223 elements, it is advised to check Cache compiled script if available property to ensure the script compilation is cached if underlying language supports it. In this case, ensure the script does not use any variable using ${varName} as caching would take only first value of ${varName}. Instead use : 
vars.get("varName")

You can also pass them as Parameters to the script and use them this way.

16.13 Sharing variables between threads and thread groups[¶](https://jmeter.apache.org/usermanual/best-practices.html#sharing_variables "Link to here")
=======================================================================================================================================================

Variables are local to a thread; a variable set in one thread cannot be read in another. This is by design. For variables that can be determined before a test starts, see [Parameterising Tests](https://jmeter.apache.org/usermanual/best-practices.html#parameterising_tests) (above). If the value is not known until the test starts, there are various options:

*   Store the variable as a property - properties are global to the JMeter instance
*   Write variables to a file and re-read them.
*    Use the bsh.shared namespace - see [above](https://jmeter.apache.org/usermanual/best-practices.html#bsh_variables)
*   Write your own Java classes

16.14 Managing properties[¶](https://jmeter.apache.org/usermanual/best-practices.html#properties "Link to here")
================================================================================================================

When you need to modify jmeter properties, ensure you don't modify jmeter.properties file, **instead copy the property from jmeter.properties and modify its value in user.properties file**. 

 Doing so will ease you migration to the next version of JMeter. 

 Note that in the documentation jmeter.properties is frequently mentioned but this should be understood as "Copy from jmeter.properties to user.properties the property you want to modify and do so in the latter file".

user.properties file supersedes the properties defined in jmeter.properties

16.15 Deprecated elements[¶](https://jmeter.apache.org/usermanual/best-practices.html#deprecation "Link to here")
=================================================================================================================

It is advised not to use deprecated elements (marked as such in [changes list](https://jmeter.apache.org/changes.html) and in [component reference](https://jmeter.apache.org/usermanual/component_reference.html)) and to migrate to new advised elements if available or new way of doing the same thing. 

 Deprecated elements are removed from the menu in version N but can be enabled for migration by modifying not_in_menu property in user.properties file and removing the full class name of the element from there.

Please note that deprecated elements in version N will be removed definitely in version N+1, so ensure you stop using them as soon as possible.

*   [< Prev](https://jmeter.apache.org/usermanual/realtime-results.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/boss.html)

 Share this page: 
*   [share](https://jmeter.apache.org/usermanual/best-practices.html "Share on facebook")
*   [tweet](https://jmeter.apache.org/usermanual/best-practices.html "Tweet on twitter")

[Go to top](https://jmeter.apache.org/usermanual/best-practices.html#top)

 Copyright © 1999 – 2024 , Apache Software Foundation 

Apache, Apache JMeter, JMeter, the Apache feather, and the Apache JMeter logo are trademarks of the Apache Software Foundation.
