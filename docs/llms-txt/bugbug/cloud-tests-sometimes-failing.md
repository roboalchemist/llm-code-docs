# Source: https://docs.bugbug.io/troubleshooting/cloud-tests-sometimes-failing.md

# Cloud tests sometimes failing

By default, BugBug will attempt to run a test step for 30 seconds locally and 60 seconds in the cloud. If BugBug is not able able to perform a test step in this amount of time, it will mark the step as failed - this is called a *timeout*.

If your local tests are stable, but only cloud tests are sometimes failing randomly, most likely it is caused by the fact, that BugBug cloud virtual machines are not as fast as your own computer. It may take longer for the page to process in the cloud.&#x20;

To prevent this you can **increase the timeout of cloud runs**:

1. Go to project settings
2. Change the "Cloud runs timeout" to a higher value
3. Save settings

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F8o1CvbgZhB7OzJUGoVSF%2Fcloud%20run%20timeout.png?alt=media\&token=f5736c8c-4d53-45b2-a2d6-7c64696de9ee)

Now BugBug will give your website more time in the cloud to load and operate.
