# Source: https://jmeter.apache.org/usermanual/build-jms-point-to-point-test-plan.html

Title: User's Manual: Building a JMS (Java Messaging Service) Point-to-Point Test Plan

URL Source: https://jmeter.apache.org/usermanual/build-jms-point-to-point-test-plan.html

Markdown Content:
Make sure the required jar files are in JMeter's lib directory. If they are not, shutdown JMeter, copy the jar files over and restart JMeter. See [Getting Started](https://jmeter.apache.org/usermanual/get-started.html#libraries_activemq) for details.

In this section, you will learn how to create a [Test Plan](https://jmeter.apache.org/usermanual/build-test-plan.html) to test a JMS Point-to-Point messaging solution. The setup of the test is 1 threadgroup with 5 threads sending 4 messages each through a request queue. A fixed reply queue will be used for monitoring the reply messages. To construct the Test Plan, you will use the following elements: [Thread Group](https://jmeter.apache.org/usermanual/test_plan.html#thread_group), [JMS Point-to-Point](https://jmeter.apache.org/usermanual/component_reference.html#JMS_Point-to-Point), and [Graph Results](https://jmeter.apache.org/usermanual/component_reference.html#Graph_Results).

General notes on JMS: There are currently two JMS samplers. One uses JMS topics and the other uses queues. Topic messages are commonly known as pub/sub messaging. Topic messaging is generally used in cases where a message is published by a producer and consumed by multiple subscribers. A JMS sampler needs the JMS implementation jar files; for example, from Apache ActiveMQ. See [here](https://jmeter.apache.org/usermanual/get-started.html#libraries_activemq) for the list of jars provided by ActiveMQ.

10.1 Adding a Thread Group[¶](https://jmeter.apache.org/usermanual/build-jms-point-to-point-test-plan.html#adding_threadgroup "Link to here")
---------------------------------------------------------------------------------------------------------------------------------------------

The first step you want to do with every JMeter Test Plan is to add a [Thread Group](https://jmeter.apache.org/usermanual/test_plan.html#thread_group) element. The Thread Group tells JMeter the number of users you want to simulate, how often the users should send requests, and the how many requests they should send.

Go ahead and add the ThreadGroup element by first selecting the Test Plan, clicking your right mouse button to get the menu, and then select .

You should now see the Thread Group element under Test Plan. If you do not see the element, then "expand" the Test Plan tree by clicking on the Test Plan element.

Next, you need to modify the default properties. Select the Thread Group element in the tree, if you have not already selected it. You should now see the Thread Group Control Panel in the right section of the JMeter window (see Figure 10.1 below)

[![Image 1: Figure 10.1. Thread Group with Default Values](https://jmeter.apache.org/images/screenshots/webtest/threadgroup.png)](https://jmeter.apache.org/images/screenshots/webtest/threadgroup.png)

 Figure 10.1. Thread Group with Default Values

Start by providing a more descriptive name for our Thread Group. In the name field, enter Point-to-Point.

Next, increase the number of users (called threads) to 5.

In the next field, the Ramp-Up Period, leave set the value to 0 seconds. This property tells JMeter how long to delay between starting each user. For example, if you enter a Ramp-Up Period of 5 seconds, JMeter will finish starting all of your users by the end of the 5 seconds. So, if we have 5 users and a 5 second Ramp-Up Period, then the delay between starting users would be 1 second (5 users / 5 seconds = 1 user per second). If you set the value to 0, then JMeter will immediately start all of your users.

Clear the checkbox labeled "Forever", and enter a value of 4 in the Loop Count field. This property tells JMeter how many times to repeat your test. If you enter a loop count value of 0, then JMeter will run your test only once. To have JMeter repeatedly run your Test Plan, select the Forever checkbox.

In most applications, you have to manually accept changes you make in a Control Panel. However, in JMeter, the Control Panel automatically accepts your changes as you make them. If you change the name of an element, the tree will be updated with the new text after you leave the Control Panel (for example, when selecting another tree element).

10.2 Adding JMS Point-to-Point Sampler[¶](https://jmeter.apache.org/usermanual/build-jms-point-to-point-test-plan.html#adding_point_to_point_sampler "Link to here")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Start by adding the sampler [JMS Point-to-Point](https://jmeter.apache.org/usermanual/component_reference.html#JMS_Point-to-Point) to the Point-to-Point element (). Then, select the JMS Point-to-Point sampler element in the tree. In building the example a configuration will be provided that works with ActiveMQ 3.0.

| Name | Value | Description |
| --- | --- | --- |
| JMS Resources |
| QueueConnectionFactory | ConnectionFactory | This is the default JNDI entry for the connection factory within ActiveMQ. |
| JNDI Name Request Queue | Q.REQ | This is equal to the JNDI name defined in the JNDI properties. |
| JNDI Name Reply Queue | Q.RPL | This is equal to the JNDI name defined in the JNDI properties. |
| Message Properties |
| Communication Style | Request Response | This means that you need at least a service running outside of JMeter and that will respond to the requests. This service must listen to the Request Queue and send messages to the queue referenced by the message.getJMSReplyTo() |
| Content | test | This is just the content of the message. |
| JMS Properties |  | Nothing needed for ActiveMQ. |
| JNDI Properties |
| InitialContextFactory | org.apache.activemq.jndi.ActiveMQInitialContextFactory | The standard InitialContextFactory for ActiveMQ |
| Properties |
| queue.Q.REQ | example.A | This defines a JNDI name Q.REQ for the request queue that points to the queue example.A |
| queue.Q.RPL | example.B | This defines a JNDI name Q.RPL for the reply queue that points to the queue example.B |
| Provider URL |
| Provider URL | tcp://localhost:61616 | This defines the URL of the ActiveMQ messaging system. |

10.3 Adding a Listener to View Store the Test Results[¶](https://jmeter.apache.org/usermanual/build-jms-point-to-point-test-plan.html#adding_listener "Link to here")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

The final element you need to add to your Test Plan is a [Listener](https://jmeter.apache.org/usermanual/component_reference.html#listeners). This element is responsible for storing all of the results of your JMS requests in a file and presenting a visual model of the data.

Select the Thread Group element and add a [Graph Results](https://jmeter.apache.org/usermanual/component_reference.html#Graph_Results) listener (). Next, you need to specify a directory and filename of the output file. You can either type it into the filename field, or select the Browse button and browse to a directory and then enter a filename.

[![Image 2: Figure 10.2. Graph Results Listener](https://jmeter.apache.org/images/screenshots/graph_results.png)](https://jmeter.apache.org/images/screenshots/graph_results.png)

 Figure 10.2. Graph Results Listener

[Go to top](https://jmeter.apache.org/usermanual/build-jms-point-to-point-test-plan.html#top)
