# Source: https://docs.bugbug.io/running-tests/running-tests.md

# Running the tests

## Different ways of running the tests

### How to initiate test runs?

* simply [by clicking "Run"](#how-to-run-a-test-manually)
* automatically with Schedules
* via API using [BugBug CLI](https://docs.bugbug.io/integrations/api)

### Running locally or in the cloud

* [locally](https://docs.bugbug.io/running-tests/test-in-your-browser) - the test will run on your computer in Chrome browser in incognito mode
* [cloud](https://docs.bugbug.io/running-tests/in-cloud-on-server) - the test will run on BugBug servers on a virtual machine

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FRMj9J6I566CtDGFmBRZ4%2Fimage.png?alt=media\&token=2c6285a1-20d6-43bc-9cde-c5fb628e3703)

## The simplest way to run a test

1. Go to a project and click the test that you want to run
2. Click `Run` button
3. See the incognito Chrome browser opening and the test running

{% hint style="info" %}
**Make sure you don't have any unsaved work in other incognito windows.** If you have other incognito windows open, BugBug will need to close them before running the tests. When you click "Close all windows", then all the incognito Chrome windows will be closed.&#x20;
{% endhint %}

After you run the test, check the result - [learn more about test statuses](https://docs.bugbug.io/running-tests/statuses).
