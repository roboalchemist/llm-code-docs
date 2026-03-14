# Source: https://docs.enate.net/enate-help/integrations/enate-integrations/blue-prism/setting-up-enate-and-blue-prism-integration.md

# Setting Up Enate & Blue Prism Integration

## Overview

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FU8pmXpKw0UrZtvNujnXB%2Fimage.png?alt=media&#x26;token=dee02af9-31e3-4169-9104-0b40c7336939" alt=""><figcaption></figcaption></figure>

## Creating a Process

The following diagram shows what a basic integration with Enate should look like using the Enate VBO.  It should follow the logic of:

* **Authenticate**\
  Pass credentials to Enate and get a token, this will be used in all future calls to Enate.
* **Get More Work**\
  This action will return a small JSON object with details on what the next piece of work is.
* **Get Action**\
  This will get the full JSON object representing the piece of work assigned to the bot (assuming it’s an action)
* **{process object using BP commands/actions or the Enate JSON Get/Set} -** this is where you are going to manipulate the JSON object before updating this back to Enate.  Change status, add notes, send email etc.
* **Update Action**\
  This action will send the updated JSON object back to Enate for updating.
* **Is Work Available**\
  This last stage is to check if there is any more work for the bot to process, if there is then go back to the start to **Get More Work**

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FbIlftsbnDss5CNMp3Cp0%2Fimage.png?alt=media&#x26;token=2ba24b58-3238-42be-b0e3-0abc99c4a1f9" alt=""><figcaption></figcaption></figure>

\
There are lots of different things you can do with the Enate VBO, this is one example.  You could also have a process which could iterate through an excel document and create a case/ticket in Enate for each row in the document.  This would not use the get more work action and would use a combination of the BP looping along with the Enate Create Ticket action.  The Get more work action is used where you are asking Enate for work and you should then keep checking until there is no more work to do.  The bot can then rest until it’s next scheduled time to run.

## Publishing a Process <a href="#toc9926660" id="toc9926660"></a>

In order for you to be able to schedule the process you need have published it to the control room.

If you double click on the process information box (or right click choose properties)

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F87tDkBEZD8X8LXEWPlED%2Fimage.png?alt=media&#x26;token=5a26b799-d52f-4c64-9e70-49008a37fef3" alt=""><figcaption></figcaption></figure>

Then you will get the process information windows displayed.  At the bottom of this screen there is a checkbox you need to ensure is ticked:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FO5bPlW29ClwFMpSFptq6%2Fimage.png?alt=media&#x26;token=c56b0b42-a933-4abe-bb9b-ac77eb8d3417" alt=""><figcaption></figcaption></figure>

This process will then be available to schedule in the control room.

## Scheduling a process <a href="#toc9926661" id="toc9926661"></a>

Now head to the Control section of Blue prism which looks like this:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FPzcm0FjSEb5gbc95bwmm%2Fimage.png?alt=media&#x26;token=5e854cc9-6771-4ef2-8555-07a0d75fe403" alt=""><figcaption></figcaption></figure>

Right click on schedules and choose new schedule:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FaF1bpCpI0haxtuaeinKO%2Fimage.png?alt=media&#x26;token=0d42e054-942e-4ec2-854d-382cd54a65ae" alt=""><figcaption></figcaption></figure>

Now give it a name and configure how often you want this schedule to run:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FZVx0rQ9EOclPCyjxsS2g%2Fimage.png?alt=media&#x26;token=cde84552-4ba3-4a9e-8dfd-e4f42bd62cd8" alt=""><figcaption></figcaption></figure>

After you have configured this, you’ll notice on the left in the tree there is a new task under the schedule:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FRxqDvCy2ezWhWpXMK4lk%2Fimage.png?alt=media&#x26;token=2e0696d4-6271-4d80-ab15-cd8d6529a522" alt=""><figcaption></figcaption></figure>

Click on this task and then we need to configure the process we are going to run and what resource to run this on:

You need to drag the process onto the relevant resource:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fp1aFLumwaFxHf2Jjju7o%2Fimage.png?alt=media&#x26;token=fa36764b-6cfb-4f66-8c52-907fd9493713" alt=""><figcaption></figcaption></figure>

This will then create an entry at the bottom to show this is a scheduled session:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FMquYiHbwafYXTgvgMJXq%2Fimage.png?alt=media&#x26;token=ec37cbf4-3bd6-415a-8c0d-650bcf34c727" alt=""><figcaption></figcaption></figure>

Click the apply changes button at the bottom left to ensure the schedule is saved:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FQXomSZFv0DblgwUxBUaF%2Fimage.png?alt=media&#x26;token=f3ab3956-5047-4348-91e6-05f437f166a5" alt=""><figcaption></figcaption></figure>

If you click on the timetable in the tree you can see that the task is now scheduled to run:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F71pVyjn6H5Vw5pUNdohO%2Fimage.png?alt=media&#x26;token=e4146be5-a013-4d66-83e2-bac77439cb1f" alt=""><figcaption></figcaption></figure>
