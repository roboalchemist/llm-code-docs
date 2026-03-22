# Source: https://docs.bugbug.io/workflow-tips/edit-and-rewind.md

# Edit & Rewind

BugBug supports unique functionality that allows you to easily record and execute steps in a very flexible way. Let's dive into the typical maintenance problem in end-to-end tests.

### A long test breaks down, and you have to fix it

This is a very common scenario when dealing with end-to-end testing.&#x20;

Imagine that you have a test that executes in 5 minutes. Of course, the recommendation for e2e tests is to have as short tests as possible, but the reality is very often different.<br>

This scenario is typically resolved as follows:

* Run a test and wait 5 minutes.
* The test fails.
* Fix broken steps or record new steps.
* Re-run the test from the beginning and wait another 5 minutes to reach the problematic part.
* If it passes, it's excellent. If not, you need to fix it again, run it, wait another 5 minutes, and loop it until it succeeds. This takes time - **a lot** of time.

Keeping this in mind, we've implemented a feature that allows you to run a test, pause it, record a new step, rewind the playback position, and continue test execution from the given position. You can run and record a test in any combination.

How to fix a test using BugBug’s Edit & Rewind freature:

* Run a test and wait until the end of execution.
* The test failed.
* Fix broken steps or record new steps.
* Rewind the playback position. **You don't have to start execution from the beggining!**
* Continue test execution from the given position.
* If it passes, excellent. If not, you have to fix it again and rewind the playback position bypassing the need to wait for earlier steps to complete. Simply verify only fixed steps.
* Profit.

#### **What does that mean for you?**

With Edit & Rewind, you can <mark style="background-color:green;">tremendously reduce the time spent on the maintenance</mark> of the tests.

Sounds awesome? Let's see it in action!

{% embed url="<https://vimeo.com/1017561827>" %}
Edit & Rewind in action
{% endembed %}

#### When else will Edit & Rewind be helpful

There are many more scenarios in which you can use this functionality.

1. **If you want to record new steps in multiple places in the test**

Pause and enable the recording multiple times, changing the recording position in the web UI where needed.

2. **If you want to record new steps somewhere in a test but don't want to wait for the whole execution process to reach this position**

Run the test and pause it. Change the playback position. In the window with a test set the right app state and start recording.

3. **If you want to debug the test step-by-step**

Pause the test execution and use the `Run next step` button. You can rewind and replay as many times as you like.

Do you feel it? Life is better now. You can rest.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fqig01LcU1N7eqK9eWvkq%2Fimage.png?alt=media&#x26;token=d8759564-e7a9-4023-b12b-06eea513e487" alt=""><figcaption><p>You after using Edit &#x26; Rewind functionality. Source <a href="https://www.reddit.com/r/wholesomememes/comments/evgnfp/resting_is_important_to_your_wellbeing/">https://www.reddit.com/r/wholesomememes/comments/evgnfp/resting_is_important_to_your_wellbeing/</a></p></figcaption></figure>
