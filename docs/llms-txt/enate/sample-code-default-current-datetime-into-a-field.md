# Source: https://docs.enate.net/enate-help/integrations/enate-integrations/sample-code-default-current-datetime-into-a-field.md

# Default Current Date & Time into a Field with Enate's Advanced Custom Cards

The following code can be added to a custom card to set the default value of a date/time field to the current date/time. In order to do this we need to use a third party object called 'moment' which lives in your browser, and will return the current datetime if we include it as a variable at the beginning of our code. This sample will assume the following:

* You have a custom card open
* It is set to 'Customised' in order to show the additional code tabs
* You have added a DateTime Field to your card - **here we will give it a name of 'CurrentDate' - you will have to adjust this name of the field referenced in your code in step 2 in order to match with your own specific field's name.**

When you set your card to 'Customised', all the previously auto-generated for the standard form layout remains for your use, so there are only two small lines of code to add, in two places. Follow the steps below:

**1. Declare 'moment' as a vairable**\
In the Typescript tab, add the following line of code **immediately after line 8**, to declare this 'moment' as a variable for subsequent use:

```
declare var moment; // Include moment in TypeScript
```

It should look like this in your code..

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MejOpiobTcaI_3ctZ1O%2F-MejQv5_BXRDNr24ndsl%2Fimage.png?alt=media\&token=30e21cb7-c044-4af5-a2f9-d44b12ed3f59)

**2. Add your custom code in the dedicated section to set your field value to the 'moment' value.**\
Further down in the Typescript code, add the following line **immediately after the  '//YOUR CUSTOM CODE BEGINS'** line:

```
this.Packet.DataFields['CurrentDate'] = moment().format("YYYY-MM-DD")+'T00:00:00';
```

It should look like this in your code..

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MejOpiobTcaI_3ctZ1O%2F-MejS0rMDpsePIfYXXC8%2Fimage.png?alt=media\&token=4016c20a-3b5d-470e-ae4f-1ae4363d68f1)

Note that you can adjust the date format to fit your needs.

**Save your card, and you're finished.**

Check out our Advanced Custom Cards section for more information about what they are and how to use them:

{% content-ref url="custom-card-content" %}
[custom-card-content](https://docs.enate.net/enate-help/integrations/enate-integrations/custom-card-content)
{% endcontent-ref %}
