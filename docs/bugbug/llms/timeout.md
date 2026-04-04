# Source: https://docs.bugbug.io/preventing-failed-tests/timeout.md

# Timeout

BugBug will not immediately fail the test if it can't click an element right away (or do any other interaction or assertion).

By default, it will wait for 30 seconds and reattempt to run the test step and hold until [waiting conditions](https://docs.bugbug.io/preventing-failed-tests/waiting-conditions) are met. If it was not possible to continue the test after such time, the test will be marked as failed.

## Configure global timeout

You configure the timeout waiting time in Project settings.

Increase the timeout if your page is slow or fails in the cloud.

Decrease the default timeout if you don't want to wait 30 seconds for failed tests results.

Increase the timeout for cloud runs if your [local runs are passed but cloud runs fail](https://docs.bugbug.io/troubleshooting/cloud-tests-sometimes-failing).

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FQDkpjcmwuUYOLSSQDQHL%2FScreen%20Shot%202022-11-24%20at%2013.20.21.png?alt=media&#x26;token=2ac1af3f-abcc-423d-9b55-8bb403925d16" alt=""><figcaption></figcaption></figure>

## Change timeout for individual steps

You can override the timeout for each step separately

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FdkUGZF5M3AI7PAIScCTi%2FScreenshot%202022-04-11%20at%2019.22.39.png?alt=media\&token=969ce483-dc8e-4263-ad9d-c5aff531a9ea)
