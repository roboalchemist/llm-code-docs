# Source: https://jmeter.apache.org/usermanual/build-ldap-test-plan.html

Title: User's Manual: Building an LDAP Test Plan

URL Source: https://jmeter.apache.org/usermanual/build-ldap-test-plan.html

Markdown Content:
In this section, you will learn how to create a basic Test Plan to test an LDAP server. You will create four users that send requests for four tests on the LDAP server. Also, you will tell the users to run their tests 4 times. So, the total number of requests is (4 users) x (4 requests) x (repeat 4 times) = 64 LDAP requests. To construct the Test Plan, you will use the following elements: [Thread Group](https://jmeter.apache.org/usermanual/test_plan.html#thread_group), [LDAP Request](https://jmeter.apache.org/usermanual/component_reference.html#LDAP_Request), [LDAP Request Defaults](https://jmeter.apache.org/usermanual/component_reference.html#LDAP_Request_Defaults), and [View Results in Table](https://jmeter.apache.org/usermanual/component_reference.html#View_Results_in_Table) .

This example assumes that the LDAP Server is available at ldap.test.com.

8a.1 Adding Users[¶](https://jmeter.apache.org/usermanual/build-ldap-test-plan.html#adding_users "Link to here")
----------------------------------------------------------------------------------------------------------------

The first step you want to do with every JMeter Test Plan is to add a Thread Group element. The Thread Group tells JMeter the number of users you want to simulate, how often the users should send requests, and the how many requests they should send.

Go ahead and add the ThreadGroup element by first selecting the Test Plan, clicking your right mouse button to get the menu, and then select . You should now see the Thread Group element under Test Plan. If you do not see the element, then "expand" the Test Plan tree by clicking on the Test Plan element.

[![Image 1: Figure 8a.1. Thread Group and final test tree](https://jmeter.apache.org/images/screenshots/ldaptest/threadgroup.png)](https://jmeter.apache.org/images/screenshots/ldaptest/threadgroup.png)

 Figure 8a.1. Thread Group and final test tree

8a.2 Adding Login Config Element[¶](https://jmeter.apache.org/usermanual/build-ldap-test-plan.html#add_login "Link to here")
----------------------------------------------------------------------------------------------------------------------------

Begin by selecting the LDAP Users element. Click your right mouse button to get the Add menu, and then select . Then, select this new element to view its Control Panel.

Like most JMeter elements, the Login Config Element's Control Panel has a name field that you can modify. In this example, leave this field with the default value.

[![Image 2: Figure 8a.2 Login Config Element for our Test Plan](https://jmeter.apache.org/images/screenshots/ldaptest/login-config-element.png)](https://jmeter.apache.org/images/screenshots/ldaptest/login-config-element.png)

 Figure 8a.2 Login Config Element for our Test Plan

Enter Username field to "your LDAP Username", 

 The password field to "your LDAP Password"

These values will be used by the LDAP Requests.

8a.3 Adding LDAP Request Defaults[¶](https://jmeter.apache.org/usermanual/build-ldap-test-plan.html#add_defaults "Link to here")
--------------------------------------------------------------------------------------------------------------------------------

Begin by selecting the LDAP Users element. Click your right mouse button to get the menu, and then select . Then, select this new element to view its Control Panel.

Like most JMeter elements, the LDAP Request Defaults Control Panel has a name field that you can modify. In this example, leave this field with the default value.

[![Image 3: Figure 8a.3 LDAP Defaults for our Test Plan](https://jmeter.apache.org/images/screenshots/ldaptest/requestdefaults.png)](https://jmeter.apache.org/images/screenshots/ldaptest/requestdefaults.png)

 Figure 8a.3 LDAP Defaults for our Test Plan

Enter DN field to "your LDAP Root Distinguished Name". 

 Enter LDAP Server's Servername field to "ldap.test.com". 

 The port to 389. 

 These values are default for the LDAP Requests.

8a.4 Adding LDAP Requests[¶](https://jmeter.apache.org/usermanual/build-ldap-test-plan.html#add_requests "Link to here")
------------------------------------------------------------------------------------------------------------------------

In our Test Plan, we need to make four LDAP requests.

1.   Inbuilt Add Test
2.   Inbuilt Search Test
3.   Inbuilt Modify Test
4.   Inbuilt Delete Test

JMeter sends requests in the order that you add them to the tree. Start by adding the first LDAP Request to the LDAP Users element (). Then, select the LDAP Request element in the tree and edit the following properties

1.    Rename to "Add" this element 
2.    Select the Add Test radio button in Test Configuration group 

[![Image 4: Figure 8a.4.1 LDAP Request for Inbuilt Add test](https://jmeter.apache.org/images/screenshots/ldaptest/add.png)](https://jmeter.apache.org/images/screenshots/ldaptest/add.png)

 Figure 8a.4.1 LDAP Request for Inbuilt Add test

You do not have to set the Servername field, port field, Username, Password and DN because you already specified this value in the Login Config Element and LDAP Request Defaults.

Next, add the second LDAP Request and edit the following properties

1.    Rename to "Search" this element 
2.    Select the Search Test radio button in Test Configuration group 

Next, add the Third LDAP Request and edit the following properties

[![Image 5: Figure 8a.4.2 LDAP Request for Inbuilt Search test](https://jmeter.apache.org/images/screenshots/ldaptest/search.png)](https://jmeter.apache.org/images/screenshots/ldaptest/search.png)

 Figure 8a.4.2 LDAP Request for Inbuilt Search test

1.    Rename to "Modify" this element 
2.    Select the Modify Test radio button in Test Configuration group 

Next, add the fourth LDAP Request and edit the following properties

[![Image 6: Figure 8a.4.3 LDAP Request for Inbuilt Modify test](https://jmeter.apache.org/images/screenshots/ldaptest/modify.png)](https://jmeter.apache.org/images/screenshots/ldaptest/modify.png)

 Figure 8a.4.3 LDAP Request for Inbuilt Modify test

1.    Rename to "Delete" this element 
2.    Select the Delete Test radio button in Test Configuration group 

[![Image 7: Figure 8a.4.4 LDAP Request for Inbuilt Delete test](https://jmeter.apache.org/images/screenshots/ldaptest/delete.png)](https://jmeter.apache.org/images/screenshots/ldaptest/delete.png)

 Figure 8a.4.4 LDAP Request for Inbuilt Delete test

8a.5 Adding a Response Assertion[¶](https://jmeter.apache.org/usermanual/build-ldap-test-plan.html#ResponseAssertion "Link to here")
------------------------------------------------------------------------------------------------------------------------------------

You can add a Response Assertion element. This element will check the received response data by verifying if the response text is "successful". ().

Note: A this position in the tree, the Response Assertion will be executed for each LDAP Request.

1.    Select Text Response Radio button in Response Field to Test group 
2.    Select Substring Radio button in Pattern Matching Rules group 
3.    Click on Add button and add the string "successful" in Pattern to Test field 

[![Image 8: Figure 8a.5 LDAP Response Assertion](https://jmeter.apache.org/images/screenshots/ldaptest/responseassertion.png)](https://jmeter.apache.org/images/screenshots/ldaptest/responseassertion.png)

 Figure 8a.5 LDAP Response Assertion

8a.6 Adding a Listener to View/Store the Test Results[¶](https://jmeter.apache.org/usermanual/build-ldap-test-plan.html#add_listener "Link to here")
----------------------------------------------------------------------------------------------------------------------------------------------------

The final element you need to add to your Test Plan is a Listener. This element is responsible for storing all of the results of your LDAP requests in a file and presenting a visual model of the data. Select the LDAP Users element and add a View Results in Table ()

[![Image 9: Figure 8a.6 View Results in Table Listener](https://jmeter.apache.org/images/screenshots/ldaptest/viewtable.png)](https://jmeter.apache.org/images/screenshots/ldaptest/viewtable.png)

 Figure 8a.6 View Results in Table Listener

[Go to top](https://jmeter.apache.org/usermanual/build-ldap-test-plan.html#top)
