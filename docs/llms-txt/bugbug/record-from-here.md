# Source: https://docs.bugbug.io/recording-tests-steps/record-from-here.md

# Record from here

You do not need to record from scratch every time! Need that in the middle of an existing test? No problem!  ✨

You can start recording from any step in an existing test. Go to the test details and:

1. Hover on a step you want to record from
2. Click `+` icon
3. Click `Record from here` option
4. The recording window will open, and the test will run until the given step
5. The recording mode will activate, and you can continue recording new steps *from here*

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F66hD3gpAmNOPw3Ct9WQm%2Fimage.png?alt=media&#x26;token=1baa7490-b41d-4e8c-b45a-f8b4bd427084" alt=""><figcaption><p>Click "Record from here" to execute test to a given position and enable recording mode</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FPznSvOTHxbfFbTCOCNbG%2Fimage.png?alt=media&#x26;token=d9ed6909-d478-4738-8518-c6a177ef7235" alt=""><figcaption><p>Recording mode in the webapp UI</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F76vVIgu52DUmOaCYYmO5%2Fimage.png?alt=media&#x26;token=c742700a-4b16-4e50-bb8d-264d5aa57794" alt=""><figcaption><p>Recording mode is activated in the browser window with a test</p></figcaption></figure>

All newly recorded steps will be automatically added to a test without any extra confirmation and will have a `NEW` badge, as shown in the screenshot below.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F18ElPmvagA5KNQh0Bdxo%2Fimage.png?alt=media&#x26;token=58cd147b-19d9-4d99-bef0-c22f4512ba85" alt=""><figcaption><p>Newly recorded steps with the NEW badge</p></figcaption></figure>

### Changing the recording position

BugBug also allows you to **change the current recording position**. To do this, drag & drop the recording position from the web app UI.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F6MFAetDBQQVGX0wkRtuT%2Fimage.png?alt=media&#x26;token=d4604616-b53d-4069-afed-7e02041d48e0" alt=""><figcaption><p>Movable recoding position</p></figcaption></figure>

This feature lets you record new steps in multiple test positions within a single recording session. If you want to pause the recording to set your application state manually and continue recording again, you can do this by clicking `Pause` button, and then you can continue recording by clicking the `Record` button.&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FESPhRQH0JE5RDxLmI24O%2Fimage.png?alt=media&#x26;token=f8f499c5-61eb-4904-8cf5-a773497edc6f" alt=""><figcaption><p>You can pause recording and enable it again by clicking Record button</p></figcaption></figure>

You can also continue recording from the current end of a test case - just click the button `Record from here` at the end of a test. Newly recorded steps will appear in the new group.&#x20;

![Record from here at the end of the test](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FCjPDyELf1ndYx9FEShn5%2Fimage.png?alt=media\&token=94c2f16c-a62b-4a16-9c1f-a0d81052f004)

### Resume execution after recording new steps

BugBug allows you to resume executing the test after recording without starting the test from the beginning. This awesome feature significantly reduces the time spent on fixing the test.

The common scenario looks like this:

* Record new steps inside the test
* Pause recording
* Change playback position before newly recorded steps
* Resume a test

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FPZlWg0dicbXhP8KL0gEy%2Fimage.png?alt=media&#x26;token=1d13dcd2-d57d-4c17-9a3a-1979d763f2a7" alt=""><figcaption><p>Change playback position and click Resume button to execute newly recorded steps</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fyhw7dDH519WMxv5kTJ3T%2Fimage.png?alt=media&#x26;token=abc95091-49d4-41f9-b215-4b9ba1a29890" alt=""><figcaption><p>You can resume execution from BugBug overlay</p></figcaption></figure>

You can repeat the record and replay sequence as many times as you like. Enjoy BugBug's flexibility!

{% hint style="info" %}
We also recommend reading about [edit-and-rewind](https://docs.bugbug.io/workflow-tips/edit-and-rewind "mention") feature that explains more about how to fix broken tests easily.
{% endhint %}
