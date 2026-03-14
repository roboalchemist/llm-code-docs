# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/test-mode.md

# Test Mode

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2ODI0MA==>" %}

## Switching to Test mode <a href="#switching-to-test-mode" id="switching-to-test-mode"></a>

If your user account is set to allow you to access test data, you can switch your Work Manager environment over to ‘Test Mode’. This link is available in the user dropdown on the right of the header bar.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FDnJO5KvN4VBsavId2HlW%2F16-Switching-to-Test-Mode.gif?alt=media\&token=e1d891de-d4b1-4a4c-826f-8aea573d4576)

## Test Mode Explanation <a href="#test-mode-explanation" id="test-mode-explanation"></a>

Once you are running in test mode you will only see test data; allowing you to create and run test work items through test versions of processes to verify them before setting live, all without affecting live production data.

As a visual reminder, the header bar is set to red when you are in Test mode.

## Defining Different Managers and Members of Queues in Test Mode <a href="#defining-different-managers-and-members-of-queues-in-test-mode" id="defining-different-managers-and-members-of-queues-in-test-mode"></a>

Test mode functionality allows you to set a different manager for a Queue when running in Test mode vs. Live mode.

Example: Consider **Manager 1** who has access to live mode and is responsible for managing two Queues, **Funding** and **Master** **Case** Queue.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWs9IbXLiOIO_4AlezW%2F-MWs9gm1OMy6tLbgy9Dy%2Fimage.png?alt=media\&token=bf28b64a-3e8e-4c3d-b9a8-66472c51830b)

In Test Mode, the same two Queues can be managed by another user who has Team Lead and Test Mode permission – see below example where **Manager 2** has been set to be in charge of the Queues in Testing Mode.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWs9IbXLiOIO_4AlezW%2F-MWs9kGgY1W_t3ul-aLF%2Fimage.png?alt=media\&token=7ec9b6f7-c3c3-4bc3-8eb7-3513f2308dea)

## Switch Robots between Live and Test <a href="#switch-robots-between-live-and-test" id="switch-robots-between-live-and-test"></a>

It is possible to switch a robot so that it can run in test mode or live mode. Specifically, two new activities have been added to the activity libraries for UiPath, Automation Anywhere and BluePrism (and the standard APIs adjusted so this can be called generically) as follows

* Set Live Mode
* Set Test Mode

These Actions allow you to flip a robot between test and live states. Once a robot has been flipped into Test mode, subsequent activity calls which the robot might make, e.g. ‘Get more work’ and ‘Create Ticket/Case etc.’ take place within that context of Test mode, getting and creating only test work items. The robot should be switched back to Live mode once the process is set to live, so ensure it is then creating live work items.

## Test Contacts - Separate test contacts in the system <a href="#test-contacts-separate-test-contacts-in-the-system" id="test-contacts-separate-test-contacts-in-the-system"></a>

Enate supports the creation of separate Contact records in Test Mode, i.e. any contact records you create in Test mode will be accessible only to Test Mode users (and contacts created in live mode will be accessible only to Live mode users).  This helps to ensure that emails from test work items are not accidentally sent to production users, and vice versa.

### Warning - Do Not Use Production Email Addresses when creating Test Contacts

{% hint style="warning" %}
**IMPORTANT:** Do NOT create Test Contact records using information (specifically email address) for people you will be using in normal production. \
**If you create a Contact record while you are in Test mode this will be created as a Test Contact, and ALL emails arriving into the system from that email address will create a Case/Ticket in Test Mode.** This would result in incoming production emails creating work test work items which would not be visible by production users.\
\
If you have created a production Contact record as a Test Contract record in error, you should edit the Test contact by changing the email address, then switch back to normal production mode to create the desired normal Contact record.<br>
{% endhint %}
