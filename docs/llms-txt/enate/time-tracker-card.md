# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/time-tracker-card.md

# Time Tracking

## Overview

To help you manage activity against your SLAs, Enate allows users to track the time it takes for work items to be completed, both as an overall total and broken out by the various resources who may have worked on it.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTgwNw==>" %}

#### When is time tracked for a Work Item?

The time tracker records the time of each individual browser session that the item is worked on; time is tracked whenever a work item is open on-screen, regardless of whether it is assigned to the user or not and regardless of what state the work item is in. The time tracker runs for one single work item at a time within a browser session and will run for a work item tab when it gets browser tab focus. **It continues to run even if the browser is minimized, if the computer is in lock screen etc.**

#### Switching between tabs

In the scenario where work item A is open (with the timer running) and a further work item B tab gets opened, the timer will stop on item A and switch instead to item B. Flipping between these work item tabs would equally switch which one the time tracker is running for.&#x20;

Time tracking halts when the work item tab is closed and in the event of a browser/machine timing out.

**See here for more details about** [**when time is tracked or not tracked**](#when-is-time-tracked-not-tracked) **in the Time Tracker card.**

#### Work Item Time Tracking when accessing Email View

{% hint style="info" %}
Clicking directly on an email in any of the Email View tabs will start the time tracker running for that work item and would stop a time tracker running for any other work item tab it had been running on immediately prior to this.
{% endhint %}

## Time Tracker Card Information

The card displays the length of time of the current session, a combined total of the length of time of all previous sessions, the expected initial estimated effort time and - for Actions and Tickets - the estimated effort time which the service agent can alter, which is useful for Forecasting.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FAmE4Xc9J36r4b9lY6tiC%2Fimage.png?alt=media&#x26;token=d9558dcf-646f-45c3-ad24-1e5c4de92b6f" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note: You are able to pause and reset the time being recorded for the current session, regardless of whether or not you are the work item's assignee.
{% endhint %}

Additionally you can edit the time of the current *and your* previous recorded sessions, regardless of whether or not you are the work item's assignee. However please note that only Team Leaders are able to edit the time recorded by *other* members of their team, whereas Team Members are only able to edit the time recorded for their own sessions.

## Viewing Previous Recorded Sessions

Expanding the Time Tracker card displays the recorded time for previous sessions, as well as who was working on the work item during that session, how long the session lasted and if the session's recorded time has been edited.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FFCzgQWsEOVRcw70mHmSQ%2Fimage.png?alt=media&#x26;token=c8c5bb9e-6d39-45e2-9172-c547fb91dc26" alt=""><figcaption></figcaption></figure>

Clicking on the information icon lets you see the date and time when the session was recorded and, if the work item is a Ticket, which category it was assigned to during that session.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FPXptA7gjjJ0X6P5kOfHq%2Fimage.png?alt=media\&token=6bc977db-c457-4841-ad0f-42940070af8a)

## Editing Recorded Times <a href="#previously-recorded-times" id="previously-recorded-times"></a>

You can edit the time of the current and previous recorded sessions, regardless of whether or not you are the work item's assignee. However please note that only Team Leaders are able to edit the time recorded by other members of their team, whereas Team Members are only able to edit the time recorded for their own sessions.

Manually editing the current time-on-task will save that edited time **as a new row** in the history.&#x20;

You will be able to see further information including when an edit was made and who by when you open the card in full-screen mode.&#x20;

{% hint style="info" %}
Note that time tracker values for work performed by robots are read-only.&#x20;
{% endhint %}

### Viewing Edited Times

You can click the expand icon to open the card in full-screen mode. Here you can see the length of time of the current session, a combined total of the length of time of all previous sessions, and, for Actions and Tickets, the expected time required to complete the work item. You will also be able to see more detailed information about the individual session, as well as information about edits made to the recorded time:

| Column                        | Detail                                                                  |
| ----------------------------- | ----------------------------------------------------------------------- |
| User                          | Who was working on the work item                                        |
| Time                          | The start and end time and total length of time of the recorded session |
| Date                          | The date when the session was recorded                                  |
| Time Edited By                | Who last edited the session's recorded time                             |
| Time Edited To                | What the session's recorded time has been edited to                     |
| Date Edited                   | The date when the session's recorded time was edited                    |
| Ticket Category (Ticket Only) | The category that the Ticket was in when the time was edited            |

## 'Expected Time'

The expected time required to complete the work item can be configured in Builder for Cases, Actions and Tickets. Note that this information will only display if:

* An Initial Estimated Effort value has been entered for this Case, Action or the selected Ticket Category in Builder.
* The system-wide settings 'Show Time Tracker' and 'Display Expected Time in Time Tracker' are enabled.

***

## Ensuring Accurate Auto-Time Tracking - Recommendations

* If you only have one work item open in Enate and are currently working on a different business application, as long as you return to that tab before your Enate session expires your time will be tracked accurately.
* If you have multiple work items open in Enate and are currently working on a different business application, as long as you return to the most recently accessed tab before your Enate session expires your time will be tracked accurately. The other work items that were open but not accessed mostly recently will not have their times tracked.

### Helpful Hints and Tips (Dos and Don'ts)

In order to keep time tracking of your activities as accurate as possible, here are a few help 'Do's and Don'ts' that will optimise how the system can help while running in a web browser.&#x20;

Remember that you might have one single Enate Work item tab open, or perhaps multiple work items open in tabs in your browser.&#x20;

#### Recommended behaviour (Dos)

1. Always open the work item you want to track time against as the LAST activity in Enate before switching to another business application to work on your task.
2. Make sure to return to the Enate application at the point where you finish your task.&#x20;
3. If your activity is taking an extended period of time to complete, it's a good idea to come back to Enate from time to time, since your session may otherwise time out due to your browser timeout\*.

*\*Session timeout periods for browsers could be typically from 20 mins to several hours. If you're finding that that things are timing out like this, speak with your IT admin about how that settings can be extended to help avoid this.*

### Things that may lead to less accurate tracking (Don'ts)

1. Failing to return to Enate after finishing your work.
2. Returning to Enate too late, i.e. after a session timeout due to inactivity.
3. Logging in on a different device or browser rather than going back to the same tab you left.
4. Just clicking the 'X' on the Enate tab without having reopened it (i.e. without having clicked to display the tab content).
5. Restarting the browser before returning to the Enate tab.
6. Closing the entire browser.
7. Restarting your system.

***

## Details - Time Tracking in various scenarios <a href="#when-is-time-tracked-not-tracked" id="when-is-time-tracked-not-tracked"></a>

Time is tracked whenever a user has the Enate work item tab open either displayed or not displayed on screen. Time will not be tracked when the Time Tracker Card has been paused. \
\
You can find more detailed information about whether time is tracked or not in a particular scenario from the table below.

<table><thead><tr><th width="194">Tab Situation</th><th width="266">Scenario</th><th width="294">Running Counter Behaviour</th></tr></thead><tbody><tr><td>One Enate work item tab open</td><td><mark style="color:green;">Users performs work away from Enate, then returns to Enate before the session timeout</mark></td><td><mark style="color:green;">Time is tracked on the work item accurately. Most correct user behaviour.</mark></td></tr><tr><td>Multiple work item tabs open</td><td><mark style="color:green;">Users performs work away from Enate, then return to last focused tab before session timeout</mark></td><td><mark style="color:green;">Time is tracked on the most recently focused work item tab. Most correct user behaviour.</mark></td></tr><tr><td>Multiple work item tabs open</td><td><mark style="color:green;">Users performs work away from Enate, then returns to a different tab, not the last focused tab, before session timeout</mark></td><td><mark style="color:green;">Enate records time spent on the business application to the last focused tab, but subsequent time is added to the currently focused tab.</mark></td></tr><tr><td>Multiple work item tabs open</td><td><mark style="color:green;">Users performs work away from Enate, then clicks to switch the display of currently focussed work item tab to instead show Enate Home page</mark></td><td><mark style="color:green;">Enate stops recording time on that work item tab, and does not start automatically recording anything until another work item tab is clicked onto.</mark></td></tr><tr><td>Non-work item tab opened, no work item tabs</td><td><mark style="color:green;">Users performs work away from Enate, then returns to Enate before the session timeout</mark></td><td><mark style="color:green;">Time is not recorded as no work item tab was open. not ideal user behaviour from the time tracker feature pov.</mark></td></tr><tr><td>Non-work item tab opened, one work item tab open</td><td><mark style="color:green;">Users performs work away from Enate, then returns to Enate before the session timeout</mark></td><td><mark style="color:green;">Time is recorded accurately on the work item tab if the user visited/opened it.</mark></td></tr><tr><td>Work item tab open</td><td><mark style="color:red;">Users performs work away from Enate, then Enate Tab gets closed without reopening</mark></td><td><mark style="color:red;">Enate may not record this accurately.</mark></td></tr><tr><td>One or more Enate work item tabs open, browser minimized</td><td><mark style="color:green;">Users performs work away from Enate, then returns to Enate before the session timeout</mark></td><td><mark style="color:green;">Time is tracked on the most recently focused work item tab.</mark></td></tr><tr><td>One or more Enate work item tabs open</td><td><mark style="color:red;">Users performs work away from Enate,</mark><br><mark style="color:red;">User session times out (e.g., due to inactivity, browser closed, login in different device/browser)</mark></td><td><mark style="color:red;">Enate may not record this accurately.</mark></td></tr><tr><td>One or more Enate work item tabs open</td><td><mark style="color:green;">User navigates to Enate website and logs out successfully.</mark></td><td><mark style="color:green;">Enate accurately records time on the last focused tab.</mark></td></tr><tr><td>One or more Enate work item tabs open</td><td><mark style="color:green;">Internet connection lost, but then restored and user returns to Enate before session timeout.</mark></td><td><mark style="color:green;">Enate accurately record time on the last focused tab.</mark></td></tr><tr><td>One or more Enate work item tabs open</td><td><mark style="color:red;">System crash or unexpected shutdown. User restarts the system and returns to Enate</mark></td><td><mark style="color:red;">Time tracking may be incomplete or inaccurate due to the unexpected interruption.</mark></td></tr><tr><td>Work item tab open</td><td><mark style="color:green;">Users presses F5 / reloads the Enate tab</mark></td><td><mark style="color:green;">Time is recorded accurately on the work item tab.</mark></td></tr><tr><td>Work item tab open</td><td><mark style="color:green;">Computer is put to sleep and then resumed within User session timeout values (i.e. user wouldn't be re-asked to sign into Enate).</mark></td><td><mark style="color:green;">Time tracking will include the time the computer was asleep</mark></td></tr><tr><td>Work item tab open</td><td><mark style="color:red;">Computer is put to sleep and then resumed but </mark><em><mark style="color:red;">after</mark></em><mark style="color:red;"> the user session has timed out.</mark></td><td><mark style="color:red;">Enate may not record this accurately.</mark></td></tr></tbody></table>

## Additional Time Tracking Information

* The Enate system will always keep a record of the automatically recorded time (i.e. not manually edited). This is a record of the amount of time which the work item tab was displayed directly on screen. This data is not displayed to you but can be accessed for MI / reporting purposes. **Please note that the time tracker tracks ALL accessing of the work item, even&#x20;*****after*****&#x20;it is completed.**&#x20;
* Manually editing the current time-on-task will save that edited time as a new row in the history. The ‘time on task’ box will subsequently display the auto-running count of the time since you started the manual edit of the previously displayed value.
