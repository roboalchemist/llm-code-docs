# Source: https://docs.bugbug.io/running-tests/schedules.md

# Schedules

## Run automated tests in the cloud regularly

### Why use schedules?

When you've already prepared automated tests, you should run them on a regular basis to monitor if your web app works properly.&#x20;

Fortunately, you don't need to log in to BugBug and click "Run" every week :smile:. BugBug can [run the tests in the cloud](https://docs.bugbug.io/running-tests/in-cloud-on-server) automatically and notify you about failed tests with [email notifications](#get-email-notifications-with-reports-for-scheduled-results).&#x20;

{% hint style="info" %}
To use schedule and cloud runs you need to have a paid subscription - [see pricing](https://bugbug.io/pricing/)
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F9bl4qLUOtQmgKqx1Y4sb%2F3_meptyScreen.png?alt=media&#x26;token=ffc7e243-f929-4b1d-bf2a-ef47aaa110a1" alt=""><figcaption><p>Empty screen for Schedules</p></figcaption></figure>

## Run all tests every hour

{% hint style="info" %}
Creating an hourly schedule is not the only option you can choose. You can also select and create from other available schedules, such as: \
\&#xNAN;***Every 5 minutes / Hourly / Daily / Weekly / Monthly***.
{% endhint %}

Scheduling cloud monitoring with automated tests doesn't require any engineering knowledge or additional infrastructure. Here's how to do it:

1. Make sure your selected test suite passes when you [run them in the cloud](https://docs.bugbug.io/running-tests/in-cloud-on-server)
2. Go to "Schedules"
3. Click on the "New schedule" button
4. Select "Hourly" and fill out all of the required fields
5. Select "All suites" **or** any other specific suite
6. Make sure "Schedule enabled" is turned on
7. Click on the "Create schedule" button

That's it! Based on this example, BugBug will now run your tests every hour. You will receive email notifications when all tests have been completed.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FTLvb3quBjWTjMcA85mnJ%2Fnew_schedule_options_list.png?alt=media&#x26;token=5a2deab2-f204-43ea-b4f9-8cb6bc90277e" alt=""><figcaption><p>Add new schedule modal</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FSYdSVwwJBKluXdQY2MgW%2F2_scheduleModal.png?alt=media&#x26;token=ef66d8db-f2c4-4d35-92b8-348167c190ab" alt=""><figcaption><p>Filled form for with a new schedule</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FE2nWogwLwjdmE8a7Bn7K%2F1_schedule.png?alt=media&#x26;token=6b6b42fd-ca0c-48f8-8320-36c0287fbe0e" alt=""><figcaption><p>Enabled schedule with all tests running every hour</p></figcaption></figure>

## Get email notifications with reports for scheduled results

You will receive notifications with scheduled test results directly in your inbox. You can [configure who gets notifications in project settings](https://docs.bugbug.io/collaboration/alerts).

Emails notifying about failed schedules are marked with a :x: symbol.

{% hint style="info" %}
**Important!** By default all suites use the [auto-retry failed tests](https://docs.bugbug.io/organizing-tests/suites#auto-retry-failed-cloud-tests-to-prevent-flaky-tests-notifications) setting to avoid sending you false-alarm notifications from unstable, flaky tests.&#x20;
{% endhint %}

{% hint style="info" %}
**Tip!** Add a filter in your email to avoid inbox clutter. Or [disable notifications for passed runs](https://docs.bugbug.io/collaboration/alerts#choose-when-people-get-email-notifications).
{% endhint %}

![Email notifications with various statuses](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F1pmN01MLwPRnDKYTltqc%2Femail%20notifications.png?alt=media\&token=fe628ce9-946f-482d-83f5-136aa89758e2)

The email contains details about the results and direct links to the tests that failed. After clicking the link you will see a read-only report of this run from the [run history](https://docs.bugbug.io/debugging-tests/runs-history).

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F90llpevS86SoUvQU2LDC%2Femail_schedule1.png?alt=media&#x26;token=f0accff2-f972-46a0-808e-90637275a699" alt=""><figcaption><p>Email notification for a failed schedule</p></figcaption></figure>

{% hint style="info" %}
**Did you know?** You can also [integrate BugBug notifications with your Slack](https://docs.bugbug.io/integrations/slack)
{% endhint %}

## Customize schedule

If you work on a large project, you may want to have more than one schedule. For example, you can run production tests every hour but monitor your [test environment](https://docs.bugbug.io/editing-tests/variables#work-with-different-development-environments) just once a day at night.&#x20;

Create more schedules to have control over which suites are run and when.

{% hint style="info" %}
**Important!** Only suites can be scheduled - you can't schedule running individual tests.
{% endhint %}

1. Create separate test suites
2. Go to "Schedules"
3. Click the "New schedule" button
4. Fill out the name field
5. In the "Time" section, select the type of run from ***Every 5 minutes/Hourly/Daily/Weekly/Monthly*** (for this example, we'll select Daily).
6. Select the suites you want to run and set the scheduled time range
7. Make sure "Enabled" is turned on
8. Click on the "Create schedule" button

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FlXUPr4AcsqzXRC8sHQVR%2F4_newscheduleDaily.png?alt=media&#x26;token=276c47fb-9792-45d2-bf63-e48cd4185361" alt=""><figcaption><p>Test suites selected for the daily schedule</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FXVaeVrx3fFHT9NKL5fcN%2F5_schedulespageOverview.png?alt=media&#x26;token=2b2e1af7-681b-41b8-ab1f-4efb46de38dc" alt=""><figcaption><p>List of all created schedules</p></figcaption></figure>
