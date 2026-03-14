# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/case-conditionality.md

# Case Conditionality

## Overview

Enate offers lots of flexibility when it comes to adding conditionality to your Case flows to specify multiple optional flows of Actions which the Case could choose to execute, depending upon which condition is met.&#x20;

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MjY0OQ==>" %}

## Adding a Condition <a href="#b-configuring-a-condition" id="b-configuring-a-condition"></a>

You add a condition by clicking on the menu on the right-hand side of a step and selecting 'Condition'. This is also how you can edit an already existing condition.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpaP-7H9QReEXdkc06%2F-MWpbwsOUdfsk1H_Cbc6%2Fimage.png?alt=media\&token=a9f4aaa2-962c-49a1-9fe7-0b065ae684a0)

In the following pop-up, add a name to be shown in the flow diagram, then select the field you want to be basing your condition on from the ‘Field’ dropdown.

You have multiple types of field that you can choose from:

* Date and Time fields
* Platform fields
* Work Item fields
* Custom Data fields

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F34eaIjoP4q4XnHWKa7Ao%2Fimage.png?alt=media&#x26;token=1d746a76-ea59-4f75-bb4b-06be71585020" alt=""><figcaption></figcaption></figure>

Once you have selected the desired field to base you condition on, you need to add a Branch Name, a condition and a Value.

* Branch Name - this is the name that will appear in the Case flow for that branch
* Condition - depending on the type of field you have chosen, you have the option of selecting 'Equals', 'Does Not Equal', 'Greater than', 'Less than', 'Greater than or equals to', 'Less than or equals to' and 'Between'.
* Value - the value that the condition will be measured against. This is the value entered by a Work Manager user at runtime.

You can add as many branches to your condition as you need.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F6uBnUYzhoTZB3dRVBPdV%2Fimage.png?alt=media&#x26;token=9b14fa35-d1e8-4220-879e-fd1418427422" alt=""><figcaption></figcaption></figure>

Alternatively, you can choose to add your condition in 'Advanced' mode - [see below](#c-configuring-a-condition-advanced-mode).

Click to 'Validate' your condition and then clock 'OK' to add it to your Case flow.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F6fkt1MHrS61sJNyWiLqA%2Fimage.png?alt=media&#x26;token=8ab1aac6-869c-4343-ba05-4964a51d670a" alt=""><figcaption></figcaption></figure>

In the Case flow your condition will appear as a diamond and the different branches you have configured are listed below it.

You then need to add the Actions you want your Case to follow when one of the branches' conditions are met.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FKlHn89qMzfiy3NixTsoj%2Fimage.png?alt=media&#x26;token=8708e1b0-9e1b-4ddb-9c54-57a5af430b08" alt=""><figcaption></figcaption></figure>

### Advanced Mode  <a href="#c-configuring-a-condition-advanced-mode" id="c-configuring-a-condition-advanced-mode"></a>

When you are building these Conditions, Enate is constructing them in C# scripting in the background. You can always easily define simple Conditions in the way described above, but if you want to expose that underlying scripting code to make some advanced adjustments, you can do this by selecting the ‘Advanced Mode’ icon in the Condition popup screen:&#x20;

Doing so will expose the underlying Expression being created in the Condition and allow you to make adjustments and even write your Expressions from scratch. &#x20;

This allows more advanced users with knowledge of C# to write complex Conditions involving standard C# functions such as Substring on a string or Day, DayOfWeek, DayOfYear on a Date, etc., exposing huge amounts flexibility to model your Conditions against any number of business scenarios.&#x20;

Furthermore, the “value” of a branch can also be defined in C# script. For instance, it is possible to compare two Field values by entering the value as a field such as \[workItemStartDate]. See below for an example.&#x20;

Note: A regularly used Condition which is not currently accessible via the Simple view is: WorkItemHasFileWithTag("file tag name"). It is, however, available on Advanced mode. However, there are a number of important aspects to take into account when writing these expressions in C#, for example case sensitivity and awareness of .Net Datatype for each of the Enate Datatypes. Please see the Appendix for more detailed information.&#x20;

#### Testing Your Expression  <a href="#testing-your-expression" id="testing-your-expression"></a>

Once you have written an expression in Advanced mode, you can validate it using the ‘Validate’ button. This will check your script for syntax errors. For example, an Expression of “\[customerName].ToLowerInvarant()”, which has a typo in the ToLowerInvariant reference, would produce a validation error of:&#x20;

Expression: (1,37): error CS1061: 'string' does not contain a definition for 'ToLowerInvarant' and no accessible extension method 'ToLowerInvarant' accepting a first argument of type 'string' could be found (are you missing a using directive or an assembly reference?)&#x20;

This error will also be accompanied by a link to the Microsoft help page related to your syntax error.

You can also test your Expression on the free dotNetFiddle website (<https://dotnetfiddle.net/>). Simply click the “Open dotNetFiddle demonstration” link on the Condition Popup and press the “copy” button to copy an executable (and commented) version of your expression and branches to the clipboard. Then in dotNetFiddle paste the script.&#x20;

In dotNetFiddle you can change the test values to replicate different scenarios.&#x20;

For example, for the following condition:&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpaP-7H9QReEXdkc06%2F-MWpcNIvxpJRrslynRth%2Fimage.png?alt=media\&token=8aed93a0-e663-47fd-b1cd-b2f07d6d78d3)

The following script is produced to test in .Net Fiddle:&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpaP-7H9QReEXdkc06%2F-MWpcWa8LW6I0B7BKj7Q%2Fimage.png?alt=media\&token=234e7f44-071a-4ef2-a07f-e988849ccd6d)

When running the script you can see the output branch is “default” because the default test value for “customerName” is “This would be the Customer Name” which is not one of the outputs. You can change the test value in the variables block near the top of the script:&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpaP-7H9QReEXdkc06%2F-MWpcZqsW7Sf5ijvQOI_%2Fimage.png?alt=media\&token=d7362225-96b5-434a-a2a7-af8f62d0940b)

If we change the test value to “my first customer” then the script result is “Customer 1”, indicating that if used at runtime Enate would run the Actions under the Customer 1 branch.&#x20;

#### Sample Expressions  <a href="#sample-expressions" id="sample-expressions"></a>

Writing C# is beyond the scope of Enate Training, however some sample functions which may inspire you are:&#x20;

#### Case-Insensitive Customer Name:  <a href="#case-insensitive-customer-name" id="case-insensitive-customer-name"></a>

Expression: \[customerName].ToLowerInvariant()&#x20;

Branch Values:“my first customer”&#x20;

“my second customer”&#x20;

Etc&#x20;

{% hint style="info" %}
Note: The value for the branches must also be in lower case. The use of the ToLowerInvariant() method is preferred over ToLower() as a C# best practice.&#x20;
{% endhint %}

#### Case Started on Particular Day of Week:  <a href="#case-started-on-particular-day-of-week" id="case-started-on-particular-day-of-week"></a>

Expression: \[customerName].DayOfWeek()&#x20;

Branch Values:DayOfWeek.Monday&#x20;

DayOfWeek.Tuesday&#x20;

DayOfWeek.Wednesday&#x20;

etc&#x20;

{% hint style="info" %}
Note: As per the documentation for the DayOfWeek property (<https://docs.microsoft.com/en-us/dotnet/api/system.datetime.dayofweek>) the result is value of type System.DayOfWeek (<https://docs.microsoft.com/en-us/dotnet/api/system.dayofweek>).&#x20;
{% endhint %}

#### Last Action Completed within 3 days of the Case Starting:  <a href="#last-action-completed-within-3-days-of-the-case-starting" id="last-action-completed-within-3-days-of-the-case-starting"></a>

Expression: \[workItemStartDate].AddDays(3)&#x20;

Branch Values:\[lastActionEndDate]&#x20;

{% hint style="info" %}
Note: The Condition of the branch should be set to “Less than”.&#x20;
{% endhint %}

#### Last Action Completed on the same days as Case Starting:  <a href="#last-action-completed-on-the-same-days-as-case-starting" id="last-action-completed-on-the-same-days-as-case-starting"></a>

Expression: \[workItemStartDate] .Date()&#x20;

Branch Values:\[lastActionEndDate].Date()&#x20;

{% hint style="info" %}
Note: The use of “.Date()” removes the Time component of the value; comparing only the date.&#x20;
{% endhint %}
