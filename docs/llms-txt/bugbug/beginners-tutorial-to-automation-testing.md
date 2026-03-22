# Source: https://docs.bugbug.io/in-depth-guides/beginners-tutorial-to-automation-testing.md

# Beginners tutorial to automation testing

Automation testing (whether e2e or unit testing) is **the process of using software tools to execute test script on an application,** comparing the actual results to the expected outcomes. It helps save time and effort by automating repetitive tasks and allows for quicker feedback on the application's quality.&#x20;

Testing process can be done in test automation tool like [**BugBug**](https://bugbug.io/) or **Selenium**. The choice of automation testing tool depends on various factors like the type of application being tested, the programming language used, test data, testing framework, the team's expertise, and the testing requirements.

## How to use BugBug?

This **tutorial will guide you through the best practices of creating test automation** with the BugBug testing tool, even if you're not a manual tester with technical knowledge. You're going to:

* Learn the basics of software testing concepts and terminology
* Follow the step-by-step screenshots
* Understand what to automate

This is not an ultimate guide with all there is to be known about test automation. We're going to explain everything **assuming you have zero technical background** but **you're good with computers**, unlike this guy:

{% embed url="<https://www.youtube.com/watch?v=o_XaJdDqQA0>" %}

## Manual testing vs. automated testing

When software developers make changes in the code, they can break something in the app that has already been working. To make sure that nothing is broken, you need to test everything...

{% hint style="success" %}
[Read how to prepare your app for automated testing and avoid common pitfalls.](https://docs.bugbug.io/best-practices#how-to-prepare-your-app-for-testing)
{% endhint %}

### **Manual testing**

You just click everything in the app with your own computer and make sure there are no bugs. This is super boring and can take multiple days to complete!

It makes you feel like this:

![regression testing meme](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fh18ttQLdT3gMIAYkoMpW%2Fregression-testing-again%20\(1\).jpg?alt=media\&token=b98c8be0-1567-4b8c-9ef2-bfc6f016defb)

### **Automated testing**

You create step-by-step instructions for the computer to click everything for you automatically. You don't click on your own, but let the computer do the tedious work.

When you use this method you can feel like this:

![automsted tests meme](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FXqrJyLAc1oZlEKIK9ISF%2FScreen%20Shot%202022-10-27%20at%2011.53.03.png?alt=media\&token=3380ba12-8b24-4a28-ba7c-d3c49e942c6f)

You click "Run" and BugBug is clicking according to your instructions called **test steps**. Here's an example of an automated test where BugBug checks if the login works.

{% embed url="<https://youtu.be/Cbk8i0A27no>" %}

If BugBug is able to finish all the test step&#x73;**,** the test is marked as successfully finished & <mark style="color:green;">**passed**</mark>. It means that everything works as it should.

If BugBug is not able to finish, the test is <mark style="color:red;">**failed**</mark><mark style="color:red;">.</mark> It means that something doesn't work right or your test steps are incorrect.

Keep reading to learn how to create such an automated test 💪&#x20;

## Create your first test via "recording"

Create your first automated test that checks if the login works. You will create a set of step-by-step instructions for BugBug that will tell it what exactly should be clicked or entered in the text fields.

{% hint style="warning" %}
Before you continue make sure you've set up your BugBug account and have access to a [project](https://docs.bugbug.io/organizing-tests/projects) and [installed the BugBug Chrome extension](https://docs.bugbug.io/quick-start/install-chrome-extension).&#x20;
{% endhint %}

{% hint style="info" %}
Throughout this guide, we use [this open-source demo app](https://marmelab.com/react-admin-demo/) called React Admin Posters Galore.&#x20;

You can learn by creating a new blank project and following each step together with us.
{% endhint %}

The next steps would guide us to test execution:&#x20;

1. **Create a new project**

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FEpGOVhr6kNmbRsB9q6jb%2Fnew%20project.png?alt=media&#x26;token=ca0527da-cb36-4f76-8137-a43d13f5a0e5" alt="Create a new project - BugBug test automation tool"><figcaption></figcaption></figure>

**2. Name it "Posters Galore" and enter a URL that will be the starting point of your app**

In our example use [https://marmelab.com/react-admin-demo/](https://marmelab.com/react-admin-demo/#/)

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FVci5VCxJMtyMqb3T0IMz%2Fcreate%20proj.png?alt=media&#x26;token=8a177509-7501-4680-aada-472174474642" alt="Create a new project - BugBug test automation tool"><figcaption></figcaption></figure>

**3. Create a new test**

We're going to create a test that checks if login to our app works, so we will name it simply "Login". In this case we are using functional testing - a type of software testing where the application under test is checked against its functional requirements.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FIeX2jCZMO7WQcjXg8OdU%2Fcreate%20test.png?alt=media&#x26;token=f6e2ffbf-e5f7-4f29-b744-e861c6b16b54" alt="Create a new test - BugBug test automation tool"><figcaption></figcaption></figure>

**4. Start the recording**

Your test is empty for now. That means that it has no instructions - no test steps. The URL you entered before is already pre-filled, so you can click "start recording".

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FO1gXFIu3OMqxCSCaEMKR%2Frecord.png?alt=media&#x26;token=bb436e83-d06f-44c5-8927-049e652ae79d" alt="Start test recording - BugBug test automation tool"><figcaption></figcaption></figure>

**5. Wait 5-10 seconds until BugBug loads your page in an incognito window**

{% hint style="info" %}
**Why incognito?** Testing needs to always start from a clean state. There should be no cookies or browser cache for your page before starting the test.
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FVbAOUMF5EHnbmgaHsSbU%2FZrzut%20ekranu%202023-05-25%20144141.png?alt=media&#x26;token=e7cf0ebd-944d-4949-abe7-859b5302cc79" alt="Test recording - BugBug test automation tool"><figcaption></figcaption></figure>

On the right side of the page, you can see a BugBug panel with actions dedicated to recording. We call it "recording overlay". By default, BugBug records every click and keyboard typing, but using this panel you can also record additional special actions. BugBug is providing automation scripts as you click and navigate on the website.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fo6cAaiBy5cjUPHJk0Who%2Frecording%20overlay.png?alt=media&#x26;token=2b53319b-d1ea-4752-8e2d-e6abbb2299ab" alt="Test recording overlay - BugBug test automation tool"><figcaption></figcaption></figure>

**6. Carefully enter login credentials using "demo" for login and password fields**

{% hint style="info" %}
**Why carefully?** BugBug records every click, so it's better to be slow while recording and think about every click. You don't want to accidentally click in the empty background!
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FBiM7PUdUHyC9h3XVcgSe%2Fusername.png?alt=media&#x26;token=b4a6058c-ec62-494b-8627-fd89122a462b" alt="Test recording - BugBug test automation tool"><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FqDn07Hxhh5YWFTWrhbFP%2Fhaslo.png?alt=media&#x26;token=afa4e60f-7b82-4eac-b21e-96dcf2eb0b69" alt="Test recording - BugBug test automation tool"><figcaption></figcaption></figure>

BugBug shows "Saved" after each click or keyboard typing. Each of these recorded actions will become a "test step".

**7. Click "Sign in"**&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FUbxSFlSGjuSJQtU2Cbnf%2Fsign%20in.png?alt=media&#x26;token=531a70d0-a2ac-4a53-8210-90e0598be53e" alt="Test recording - BugBug test automation tool"><figcaption></figcaption></figure>

You should now see the "Posters Galore" admin panel.&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FInSBbORn2UoCkBvSt6Yw%2FZrzut%20ekranu%202023-05-25%20145328.png?alt=media&#x26;token=3dde5b56-f9a4-42ea-bd61-a3f620686fd3" alt="Test recording - BugBug test automation tool"><figcaption></figcaption></figure>

**8. Add an assertion**

We've successfully logged in, now we need to create an instruction for BugBug that will check if the page actually has logged in. What should appear on the page that clearly tells us that the login worked? What should we *assert*?

{% hint style="info" %}
**Assertion** = a test step that checks if something specific appears on the page, or if the page matches some specific expectations.
{% endhint %}

The simplest way of checking if the login has been successful is to **check if the page shows some specific text**. In our case we can assert if the text "Welcome to the react admin e-commerce demo" is visible. If it is visible everything is fine, if not, the test will fail.

Click "Assert" in the recording overlay

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FVDAFCXHlCt77GHfBn8Jt%2Fassert.png?alt=media&#x26;token=5fc444f9-9f86-407c-8b1f-a9fa2904a6de" alt="Adding assertion - BugBug test automation tool"><figcaption></figcaption></figure>

&#x20;Click the text on the page that you want to check every time BugBug runs this test.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FA7SLXmgpSLKd8pgTqcgS%2Fass.png?alt=media&#x26;token=cfa01568-35db-456b-8fb9-3c0dbc544a47" alt="Test assertion - BugBug test automation tool"><figcaption></figcaption></figure>

**9. Finish recording the test**

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FAUGlwxmFIiL3RQ7SyUOz%2Ffinish.png?alt=media&#x26;token=ec1efdc0-8f66-4f2a-8528-241780981e83" alt="Finish test recording - BugBug test automation tool"><figcaption></figcaption></figure>

See that everything you clicked is now recorded as "test steps".

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FVVFRjy7twnQ526vyMG5i%2FZrzut%20ekranu%202023-05-25%20145749.png?alt=media&#x26;token=d5801c46-2338-427a-8962-79ae6e54f47d" alt="Test steps - BugBug test automation tool"><figcaption></figcaption></figure>

**10. Run the test to see if it works**&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FeV5zN8yUAfHzWrFvJ9Qb%2Fru.png?alt=media&#x26;token=41f5a7d3-760a-4e7f-b2dc-fad17575e3d6" alt="Test Run - BugBug test automation tool"><figcaption></figcaption></figure>

Observe how BugBug is repeating your actions.&#x20;

{% hint style="info" %}
**When running the test:**

* Don't move your mouse cursor over the running test window.
* Don't minimize the window, as Chrome may stop executing the test if it's not visible.
  {% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FPQnMyEEsluPbEXkWAlWv%2FZrzut%20ekranu%202023-05-25%20152005.png?alt=media&#x26;token=d905669c-c80c-448a-90e2-aa47cdeb4115" alt="Test Run - BugBug test automation tool"><figcaption></figcaption></figure>

**11. Check if the test has passed**

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F9I1oR0JfhF6X3FiEgBXY%2Fpass.png?alt=media&#x26;token=46c770f3-bb2c-49bf-9f73-0c02e23eb81d" alt="Test Run - BugBug test automation tool"><figcaption></figcaption></figure>

If your test has not passed and it's failed, it can be caused be several common problems which we will cover later.

**12. Close the finished test**

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FrgUHQ8b2TYuN3B5hghSI%2Fclo.png?alt=media&#x26;token=29c03399-694b-4473-b643-8ee9c8704eaf" alt="Test Finish - BugBug test automation tool"><figcaption></figcaption></figure>

All your test steps are green! The login works as it should.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FKbbgK1aSmm6MCCnVBmUu%2FZrzut%20ekranu%202023-05-25%20152551.png?alt=media&#x26;token=8208a578-2b19-4eb6-b625-d2df2104b1ab" alt="Test Result - BugBug test automation tool"><figcaption></figcaption></figure>

**13. Achievement unlocked!**

🎉 You have successfully automated your first test. Now to check if login works, you don't need to click on your own, you can just click "Run test" and BugBug will do it for you.

## Does the test fail? Fix it with "Record from here"

Sometimes after you finished the initial recording, your test may still not pass. There might be several reasons for that:

* You forgot to record the mouse "hover"
* You clicked an incorrect element during the recording
* Your page has dynamic content, for example, you wanted to check if your homepage shows recommended products, but these products change every time you load the page
* Your page HTML is not built with automation testing in mind and uses unusual development patterns and solutions that are not industry-standard (see more advanced info on [data-testid](https://docs.bugbug.io/preventing-failed-tests/selectors#use-custom-attributes-for-selectors))

​We're going to walk you through an example, where we record a test, but it doesn't work because we forgot to record mouse "hover". Then we're going to fix the test using the "record from here" action and add the missing hover step.

{% hint style="info" %}
For this example, we're using our [Playground page](https://playground.bugbug.io/pl/others/nested-element-dynamically-added-to-dom-on-hover), which is dedicated to testing.

You can learn by creating a new blank project and following each step together with us.&#x20;
{% endhint %}

**1. Create a new project** with our playground example page `https://playground.bugbug.io/pl/others/nested-element-dynamically-added-to-dom-on-hover`

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F5NpN7zJFgGiKhWYtwPnN%2Fimage.png?alt=media&#x26;token=7ed5c7fb-3a98-4fbc-a65a-19d4be8bc769" alt=""><figcaption></figcaption></figure>

**2. Create a new test and start recording** (use the example app URL provided above).

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FrrNRaoRGvoSV6t2qGG7q%2Fimage.png?alt=media&#x26;token=03c6244e-241a-4c14-afb4-f57c56447ff8" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FUMrcIXUlDDU2GRTf4Hz5%2Fimage.png?alt=media&#x26;token=1c704209-2ecb-4f28-ab44-d44484a6a2ac" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FNdflawAHz4VgcZ6DyYa3%2Fimage.png?alt=media&#x26;token=5c084e55-a17c-40f0-aef6-7db8f5c8ba2f" alt=""><figcaption></figcaption></figure>

**3. Hover over a dropdown menu "Trigger" and click the "Item 1" element.**

Attention! This element only appears when you hover your mouse over the dropdown menu. We deliberately skip recording this hover to demonstrate the consequences.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FvkWvDHmSAdtOTyTlE35u%2Fimage.png?alt=media&#x26;token=c08f7723-7ebc-44c4-b71a-c2ccbe04dbac" alt=""><figcaption></figcaption></figure>

**4. Finish your recording.**

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FxzBIjwsuh7iFqwTtnjMJ%2Fimage.png?alt=media&#x26;token=173e8342-105e-46c2-845c-3aef1253c6ce" alt=""><figcaption></figcaption></figure>

**5. Run the test to see if it works...** But it fails because we forgot to record the "hover".

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FIZmsCbBuotTzGNn7N5IG%2Fimage.png?alt=media&#x26;token=7008c029-89bd-4907-a9ec-b9fa7a31a42f" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FIeENGna5vojDYXa0UXqw%2Fimage.png?alt=media&#x26;token=1ae01293-ae00-4946-bd26-03fae3866323" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FQQ9FDtMExCa0o9inSRzP%2Fimage.png?alt=media&#x26;token=61c336a4-ca30-45a9-9ddb-e60789aee8f2" alt=""><figcaption></figcaption></figure>

Now, it's time to fix the test by recording the missing "hover" step.

**6. In the existing window within the test, click the "Edit and rewind" button.**

This option will switch you to [Edit and Rewind mode](https://docs.bugbug.io/workflow-tips/edit-and-rewind), in which you can record new steps to fix our test.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F8d36s4I4b2ti5HKximNS%2Fimage.png?alt=media&#x26;token=4e983e90-07a2-4ff0-a5b7-dec916ffafa9" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Ffm0oOI79YZyOwSM4adBg%2Fimage.png?alt=media&#x26;token=463609ba-5ed5-498f-8f4d-4bcfd261a8ce" alt=""><figcaption></figcaption></figure>

**7. Click "Record from here".**

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FK6ORPT5ZAhetoM8ZUXZG%2Fimage.png?alt=media&#x26;token=80d1b79b-1669-49c5-83e2-50d46f232316" alt=""><figcaption></figcaption></figure>

**8. Click the "Add hover" button in the recording overlay.**

You can see that the test is ready for recording when the BugBug overlay shows the "REC" icon.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F7R8sxx75K9HZqx89pBgV%2Fimage.png?alt=media&#x26;token=a47ab1f6-56a7-41aa-a3ac-a3643e2bbea7" alt=""><figcaption></figcaption></figure>

**9. Click the dropdown menu.**

This tells BugBug that the mouse should be moved to this element before attempting to click the "Item 1" element.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FCwb8PGMSEn92pAYnMbiz%2Fimage.png?alt=media&#x26;token=7924d433-ecee-4605-ba18-888961998f92" alt=""><figcaption></figcaption></figure>

**10. Finish your recording and confirm the recorded steps.**

You can see that we only added one step, "Hover."

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FadCkeNvbmscBvayjK0bi%2Fimage.png?alt=media&#x26;token=f143814b-814f-40d0-8df3-11c3a76d0de8" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FS5BeVk1lMCkWENIQVh0Y%2Fimage.png?alt=media&#x26;token=8d449923-b27b-4617-a44a-3834c371bf40" alt=""><figcaption></figcaption></figure>

**11. Run the test to check if it works now.**

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F27Oh7TbFNSCadwDWFxt4%2Fimage.png?alt=media&#x26;token=1f230059-1e7b-4dc2-b80f-f0f38cff3607" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FHTHQ95boy4ktDOP6ica1%2Fimage.png?alt=media&#x26;token=601a0ea0-e3c5-4d4e-b1c8-8cb83cab8504" alt=""><figcaption></figcaption></figure>

**12. Achievement unlocked!**

🎉 It worked! You've fixed a test with "Record from here". You can use this technique for more advanced problems. Conclusion: if you see that your test fails, try to "Record from here" and replace the failed steps with a new recording. It's the simplest way of fixing tests!

{% hint style="info" %}
If you want to know more about fixing and debugging your tests, read more about [edit-and-rewind](https://docs.bugbug.io/workflow-tips/edit-and-rewind "mention") and [breakpoint-run-step-by-step](https://docs.bugbug.io/debugging-tests/breakpoint-run-step-by-step "mention")&#x20;
{% endhint %}

## What to test?

You might think now: "Hold on, how can I test everything? Is it possible?"&#x20;

In short: no, you will never be 100% sure if everything works as it should. But your goal is to **lower the risk of app users encountering a bug**. You should focus on testing features that are critical for your business.

{% hint style="info" %}
Checking if there are no new bugs is called [**regression testing**](https://bugbug.io/blog/software-testing/everything-you-need-to-know-about-regression-testing/)**.** If you notice a bug in something that has been working before, it's called **a regression.**
{% endhint %}

Examples of features and consequences of their bugs:

| Feature                                              | What if it breaks:                                | Is it critical? |
| ---------------------------------------------------- | ------------------------------------------------- | --------------- |
| Login                                                | Users can't use your app                          | Yes             |
| Homepage / Landing page                              | New clients can't register                        | Yes             |
| Registration                                         | New clients can't register                        | Yes             |
| Creating new items                                   | Users can't achieve their basic goal              | Yes             |
| Password reset                                       | Only users who forgot their password can't access | No              |
| Some checkbox in an obscure feature that nobody uses | Probably no-one will notice                       | Hell no         |

{% hint style="info" %}
A list of things that you want to test is called a list of [**test cases**](https://bugbug.io/blog/software-testing/how-to-write-automation-test-cases/)**.** An individual **test case** should focus on just one process in your app.
{% endhint %}

## How many tests should you create?

If you're just starting with test automation, your first goal is to create about 5 to 15 tests that check your core website functionality.

Later on, you can even have hundreds of tests, checking all the conditions and less critical features, but it's better to **first focus on a small number of useful tests**.

Here's an example list of tests that covers the most critical paths in a web app Software-as-a-Service product.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FgWkyYEJaLDGKuAz7M3IP%2FScreen%20Shot%202022-11-02%20at%2014.09%201.png?alt=media&#x26;token=1d9a475c-d7bf-4d74-a94a-cb52f0c8aef1" alt="List of tests - BugBug Test Automation Tool"><figcaption></figcaption></figure>

## How many steps should a test have?

Shorter tests are better. Write automated tests that are short, avoiding long test cases.&#x20;

Why? Because shorter tests are easier to maintain and fix.&#x20;

Imagine a very long test that takes 10 minutes to run. But it fails at the end. Every time you want to fix it, you would need to wait these 10 minutes until the test goes through the previous steps. Test automation is supposed to make your work faster, so avoid such long tests.

## **How to make shorter tests?**

**Use multiple test accounts**

Don't use your own personal login and password in automated tests. Create a dedicated test user for that. Each user can have a different configuration. For example, one of your test users can be a business user, and one can be a personal user. You create separate tests for each type of login.&#x20;

Make a list of your test accounts and their params and store it somewhere in a spreadsheet, for example like this:

<table><thead><tr><th>Email</th><th width="160">Password</th><th width="143">Type</th><th>Parameters</th></tr></thead><tbody><tr><td>test-automation-standard@xyz.com</td><td>qwe123qwe</td><td>Business</td><td>User with default configuration for business accounts</td></tr><tr><td>test-automation-trial@xyz.com</td><td>asd4rftha</td><td>Personal</td><td>Trial account</td></tr><tr><td>test-automation-subscribed@xyz.com</td><td>46dghbn90</td><td>Business</td><td>Paying user, with a subscription active</td></tr></tbody></table>

**Split user paths to independent tests**

Here's an example of a too long:

| Test name    | Steps                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Landing page | <p>go to landing page URL</p><p>click "features" </p><p>assert all the features</p><p>click "contact"</p><p>assert contact information </p> |

Split it to 2 independent tests:

| Test name             | Steps                                                                                 |
| --------------------- | ------------------------------------------------------------------------------------- |
| Landing page features | <p>go to landing page URL</p><p>click "features" </p><p>assert all the features</p>   |
| Landing page contact  | <p>go to landing page URL</p><p>click "contact"</p><p>assert contact information </p> |

**Remember that tests need to be independent!**&#x20;

Tests should be independent of each other. You should not create 2 tests and then run them in a specific order. Every test needs to be self-contained. Learn more about it in our tips on [atomic test cases](https://docs.bugbug.io/creating-tests/independent-tests).

## What not to test?

A test automation framework is a set of guidelines, best practices, tools, and libraries that provide a structured approach to designing, organizing, and executing automated tests. It aims to standardize the testing process, increase test efficiency, and improve test maintenance.&#x20;

That's why some features are known for being **more difficult to automate.** We recommend that you automate them later after you are done with the easier test cases.

* **Registration**: it's difficult to automate because you can't register the same email twice, so you need to [generate a random email and verify it afterward](https://docs.bugbug.io/editing-tests/variables#test-user-registration-and-login-using-variables).
* **Collaboration**: one user is adding something, and the second user sees the changes. You need one long test where you log in with the first user, then log out and log in again with the second user.
* **Dynamic lists** such as search results, product listings, exchange rates, and lists that change all the time. Automation requires a good understanding of how to make the list more predictable.
* **Downloading files** and checking their contents.
* **Multi-language**: you can have lots of tests for different languages, but it's hard to maintain unless your app supports [selectors](https://docs.bugbug.io/preventing-failed-tests/selectors) based on [data-testid attributes](https://docs.bugbug.io/preventing-failed-tests/selectors#use-custom-attributes-for-selectors).&#x20;
* **Dates and calendars**: the current date changes every day, so it's not easy to record and repeat.

## Suites: when do you need them?

Test [suites](https://docs.bugbug.io/organizing-tests/suites) are groups of individual tests. They allow you to run several tests at once with one click.&#x20;

By default, BugBug creates an "All tests" suite for you. All new tests will be automatically added to this suite. If you're a beginner, you don't need to set up anything else for now, this one suite should cover the basic needs.

{% hint style="info" %}
You will need more suites later on, once you have more advanced tests that cover [different testing environments](https://docs.bugbug.io/editing-tests/variables#work-with-different-development-environments).&#x20;
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FVmFEDRFbANThePLExnG1%2FZrzut%20ekranu%202023-05-26%20164755.png?alt=media&#x26;token=52587bba-9f91-45ce-93ca-2f2af55b0c8a" alt="Test suites - BugBug Test Automation Tool"><figcaption></figcaption></figure>

## Run tests in the cloud

You might think that if you created your 5 essential automated tests, now to run them you need to open up your computer and click "Run" and block your computer for several minutes. Good news - there's no need for that! You can run tests **in the cloud** and even **schedule** them to run automatically, even when you're asleep. :magic\_wand:

{% hint style="info" %}
**Run in cloud** = run on some other machine in a data center, not on your own computer

**Run locally** = run on your own computer in your own browser&#x20;
{% endhint %}

Check if your tests are passed when you run them in the cloud.&#x20;

1. Go to "Suites"&#x20;
2. Find "All tests"
3. Click "Run in cloud"
4. Wait until the suite is finished and passed

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fkm2APHq3T12iB2pzJZrX%2Fcloud.png?alt=media&#x26;token=ff038a64-297f-4253-b879-cbaab5b4bbf2" alt="Test run in cloud - BugBug Test Automation Tool"><figcaption></figcaption></figure>

If the tests are passed locally but fail in the cloud, please [contact our support](https://bugbug.io/contact/). Usually, that should never happen.&#x20;

## Schedule automated tests

You can monitor your web app and run automated tests every hour and get notifications when your test fails. Learn more in our [separate article about scheduling tests](https://docs.bugbug.io/running-tests/schedules).

## Take automation to a next level

This guide only covered the very beginning of what you can achieve with BugBug test coverage. Keep exploring and challenging yourself with more and more difficult test cases! Once you're comfortable with the basics, read our other in-depth guides, where we cover advanced techniques and a more strategic approach to automation testing in a startup.&#x20;

If you have questions or comments on this guide, please [contact us](https://bugbug.io/contact/), our support team is very responsive and interested in your feedback.&#x20;

Happy (automated) testing! :beers:
