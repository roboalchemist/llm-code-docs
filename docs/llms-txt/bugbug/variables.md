# Source: https://docs.bugbug.io/editing-tests/variables.md

# Variables

## Intro to Variables

### Why use variables?&#x20;

Variables enable you to **run and maintain tests efficiently** in any of the following situations:

* You work with multiple development environments
* You have multiple tests that use the same value in multiple form fields or assertions
* You want to test forms that require users to enter random and unique data, e.g. registration with an email address
* You want to run the same tests with different form inputs, e.g. testing product searching against various search queries or testing different zip codes

### What are variables?

Variables are **dynamic pieces of text that you can use in your tests**. [Use variables in tests](#use-variables-in-tests) by entering their name in curly brackets to place a variable in any text field in the test steps ex. `{{myCustomVariable}}`

Variables are good for storing:

* Fragments of URL addresses like domains, subdomains, hostnames, etc.&#x20;
* Email addresses
* Input values like product names, brands, phone numbers, ZIP codes, etc.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FeYzk3QfYNkJEsGJxTIJM%2F21.03.2023%2012_11_58.png?alt=media&#x26;token=bd1ed665-5f4f-4c9a-bb23-cae5e5660564" alt=""><figcaption><p>Example: variable "hostname" used in an URL</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F23ul12snZCDN1vTPGcd7%2FZrzut%20ekranu%202023-03-21%20123230.png?alt=media&#x26;token=daac65a2-abb5-43fe-9941-790ea4ff1b56" alt=""><figcaption><p>Example: definition of variable "hostname" in the variables tab</p></figcaption></figure>

Variables do not have to be simple text assignments. Some [built-in variables](#use-built-in-variables-for-dynamic-or-random-values) are different each time you run the test for example `{{timestamp}}` or generate random values like `{{testRunId}}`.&#x20;

You can also write your own [javascript variables](#javascript-variables) - functions that return a value that is calculated every time you use the variable.

## Using text variables

### Create custom text variables&#x20;

This is the most basic type of variable. Go to the "Variables" tab and click on the "New variable" button.&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F2KQwTRNtCsfA6rJ2CTwh%2FnewVariable_new.png?alt=media&#x26;token=cca5eb19-b48e-4123-9db2-307aab8e9380" alt=""><figcaption></figcaption></figure>

Add a name and value for your variable.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FxehmJ0ZANjm4Gt0UGXQv%2F1newVar2.png?alt=media&#x26;token=f7f06d24-f181-40b0-9181-678f551ae94e" alt=""><figcaption></figcaption></figure>

Then click on the "Create variable" button to save it.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FXogYdHSLR558bX3EMYSx%2F1newVar3.png?alt=media&#x26;token=1f747217-bf8d-4581-8275-19286183f76a" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important!** You can't use spaces in a variable name. We recommend that you use [camelCase](https://en.wikipedia.org/wiki/Camel_case).&#x20;
{% endhint %}

### Create custom JavaScript variables

Previously, a custom variable containing a text value was added. Now you can go further and use it with a JS variable that can generate a unique value. As a support, you are going to use the built-in variables in BugBug as well.

For starters, once again click on the "Create variable" button to create a new one, yet this time on the modal select the "Custom JavaScript" in the "Type" field.

Also, paste the JS code into the "JavaScript code" field. As an example, a simple function was used here:

```
return variables.testVariable + ' ' + variables.testRunId;
```

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fs8QnU5UugZAWtYSpaakw%2FvariableSettings_new.png?alt=media&#x26;token=7725c7d0-b68d-49ac-9d76-f3877f8a9f2c" alt=""><figcaption><p>Variable settings</p></figcaption></figure>

Next, click on the "Create variable" button, and we're all set.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FFvRouzh1HmMK5yFPwS6w%2F2newJSvar2.png?alt=media&#x26;token=54cced63-21a4-41c5-8418-a5b88f59e77c" alt=""><figcaption><p>List of added custom variables</p></figcaption></figure>

Now you're ready to use the names of our created variables when editing a test. To do this, simply use the names of the existing variables, i.e. place them in the target field(s) on a page that's being tested.

```javascript
{{testVariable}} or {{taskName}}
```

In general, the applied variables in your test might look like this:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FEcanpADx7QBgWeauqdFW%2FvarUsageInTest2.png?alt=media&#x26;token=4bad7f10-99c5-4d74-8c1f-36b579c9c67b" alt=""><figcaption><p>Variables used in a test</p></figcaption></figure>

###

### Use variables in tests&#x20;

Use a variable name in curly brackets to place a variable **in any text field in the test steps**. You can combine variables with normal text, for example `{{hostname}}/v1/index.html`

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FeYzk3QfYNkJEsGJxTIJM%2F21.03.2023%2012_11_58.png?alt=media&#x26;token=bd1ed665-5f4f-4c9a-bb23-cae5e5660564" alt=""><figcaption><p>Example: a variable used in "Go to url" action</p></figcaption></figure>

You can use variables in other types of actions, such as typing text in a form, assertions, and **even CSS selectors.**

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F0rMfCwY1CjysQI3Amlho%2FZrzut%20ekranu%202023-03-24%20125442.png?alt=media&#x26;token=0478e2f3-897c-4cd6-87ac-d5079d217c2f" alt=""><figcaption><p><strong>Use variables in selectors, assertions, etc.</strong></p></figcaption></figure>

**Combining variables with curly brackets**

You can also combine variables with `{{ }}` signs if you need to. To escape curly brackets, use `{% raw %}` and `{% endraw %}` blocks.

Here is an example:

Input:

* *variable: projectName* = `Foo`&#x20;
* *format*: `{{ projectName }}{% raw %} {Put this text in brackets}{% endraw %}`

Output:

* `Foo {Put this text in brackets}`

### Use built-in variables for dynamic or random values

Use BugBug's pre-defined set of variables to handle your complex testing scenarios. Here are some examples of what you can do with built-in variables

<table><thead><tr><th width="218.62315752406113">Built-in variable name</th><th width="92">Type</th><th width="188.744109669127">Description</th><th>Usage example</th></tr></thead><tbody><tr><td><h4>testRunId</h4></td><td>Text</td><td>The current id of the running test (UUID format).</td><td>You want to have a new random unique value for one specific test run, for example you want to <a href="#test-user-registration-and-login-using-variables">test user sign-up and then log in.</a> </td></tr><tr><td><h4>testId</h4><p></p></td><td>Text</td><td>The current id of the test (UUID format).</td><td>You want to test add/edit/remove operations in one test, for example, add a product and then remove the same product with a name <code>Test Product {{testId}}</code></td></tr><tr><td><h4>suiteRunId</h4></td><td>Text</td><td>The current id of the suite (if the test is running from a suite, UUID format).</td><td>You want to have a new, random unique value that is the same across all the test runs in one suite.</td></tr><tr><td><h4>runMode</h4></td><td>Text</td><td>The current run mode for the test ("local" or "server").</td><td>You want to have different input or assertion value when the test is run on server. </td></tr><tr><td><strong>randomNameFixed</strong></td><td>Text</td><td>Random name that remains unchanged during the test run (8 letters).</td><td>You want to have a new, random uniqe name that is the same across all the  test and used multiple time </td></tr><tr><td><h4>scheduleId</h4></td><td>Text</td><td>The current id of the schedule (if the test has been started via a schedule, UUID format).</td><td>You want to have a new, random unique value that is the same across all schedule run.</td></tr><tr><td><h4>timestamp</h4></td><td>Text</td><td>The current Unix Time in milliseconds (int format, e.g.: 1645710937798).</td><td>You want to know when your test runs or use it similar to <strong>randomNumber</strong></td></tr><tr><td><h4>randomNumberFixed</h4></td><td>Text</td><td>Random number that remains unchanged during the test run (10 digits).</td><td>If you want to edit an element, find it later in test steps and use it or remove it.</td></tr><tr><td><h4>profileName</h4></td><td>Text</td><td>The current profile name for the test. Default: "Default".</td><td>If you want to enter a production/test URL depending on the profile, test runs</td></tr><tr><td><h4>suiteName</h4></td><td>Text</td><td>The current suite name for the test (if the test is running from a suite).</td><td>If you want to create an email that inform you about suit name that was run </td></tr><tr><td><h4>testName</h4></td><td>Text</td><td>The current test name.</td><td>You can mix it with timestamp to create a new subscription notification test.</td></tr></tbody></table>

Built-in variables also give you access to generators of random numbers and names that you can use right away in your tests.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FfJfFAIGfICSZDi0ZIOeR%2FZrzut%20ekranu%202023-03-20%20111515.png?alt=media&#x26;token=6af6e495-b35f-4d96-a43f-1345d9408c13" alt=""><figcaption></figcaption></figure>

### Recording and working with variables

Currently, you can use variables during recording.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FiTjofjLxq5nsC3rxjjY2%2FvarBtn.png?alt=media&#x26;token=b850827e-1d13-4c0a-bf70-483cbfb858d4" alt="" width="279"><figcaption></figcaption></figure>

* You can **insert** pre-prepared or built-in **variables** when **recording tests.**
* You can also dynamically **create variables** during recording based on the source being tested.
* You can also record the steps and then edit them manually.&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FlSuvQyItDk84UwsceiR9%2FZrzut%20ekranu%202023-04-03%20120138.png?alt=media&#x26;token=8bdbff18-3807-4a60-8f0a-99baedd17446" alt=""><figcaption><p>Two option for variables action in overlay</p></figcaption></figure>

{% hint style="info" %}
&#x20;For more details, go to the "[Variables During Recording](https://docs.bugbug.io/editing-tests/local-variables)" document.&#x20;
{% endhint %}

## User registration and login using the BugBug Testing Inbox

The [BugBug Testing Inbox](https://bugbug-inbox.com/) solves several problems of testing user registration and login.

> **Test case:** As a user, I go to the home page and click the "Login" button. I enter my email and password. I receive a verification email. I click on the link. I use my previous email and password to log in.

&#x20;You can use inbox to solve several problems, such as:

* How to get a unique random email address
* How to receive the email with the verification link
* How to use previously generated unique email and password in the login form&#x20;

#### **Create your test using BugBug**&#x20;

First, start the test recording with a page that requires registration. Add steps that lead to the registration process. You don't need to set it up any particular way at this point. Record it as normal users perform their actions.

### Use the BugBug Testing Inbox to generate a unique email address&#x20;

When you're ready to enter the email address, look at the BugBug extension overlay menu. There is an option called **"Inbox"**. Click it, but do not stop the recording.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FnEiwj28K9BCm1lA0N9iQ%2Finbox%20menu.png?alt=media&#x26;token=45c7dfb3-2570-4146-8452-12a0f696621d" alt=""><figcaption></figcaption></figure>

When you open it, you will see two options. Focus on the **"Auto-generated random email unique for this test"** option.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FI0zjD3V8Yj4X0QHii60T%2Finbox%20open.png?alt=media&#x26;token=eefe3fef-6cf6-4960-8f1b-e57fb5a5c425" alt=""><figcaption></figcaption></figure>

This option creates a random email address using the variable **{{testRunId}}** and the domain **@bugbug-inbox.com**. \
The {{testRunId}} variable is unique per test run, so the generated email address will be constant during a single test run. If you rerun the test, a new email address will be generated using this variable. On the BugBug web application, in steps, you will see it as **{{testRunId}}@bugbug-inbox.com**.

You can copy it directly from the extension using the copy **icon.**

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fcx2X7nyCfMU3jLuK5QKR%2FCopy%20icon.png?alt=media&#x26;token=5eb1bc55-f756-46d2-932e-f9b7ae3c7818" alt=""><figcaption></figcaption></figure>

And use it directly to register. If the registration process does not require a verification email, you can now go back to the extension menu and continue. If you need to confirm a verification email, go to the verification flow.&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F3nj5NCqhVLwvQlbgM2Cz%2Fgo%20back.png?alt=media&#x26;token=86180729-dffb-44c8-bbfb-0bb9725d766d" alt=""><figcaption></figcaption></figure>

You can find the email address based on a variable in the test step. Now your test is free of duplicate registration email problems every time you run it.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FfNaWVjORrYyt6uLgUjrY%2Fsteps.png?alt=media&#x26;token=a0a008c8-dcbc-4780-9185-d41ac516ebfe" alt=""><figcaption></figcaption></figure>

### Using the BugBug Testing Inbox to activate the registration email

Most of the registration processes require opening the verification email and confirming the address. With the BugBug Testing Inbox, you can open an email, automatically confirm it as a test step, and complete the process without using third-party providers. \
\
When you reach the moment of providing an email in the test steps, just **copy the email address** by an icon. Submit the form and **open our inbox in a different tab** by clicking the "open inbox" button. Do not stop the recording. \
\
Opening a new tab will be recorded and required.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FmkOstuMtUjKkvYZWbaLW%2Fopen%20inbox.png?alt=media&#x26;token=0f8afda4-f776-4d9a-8e3d-31fafd404ea4" alt=""><figcaption></figcaption></figure>

In a new tab, you will see an inbox created specifically for an email address you used in the previous steps. Wait for a confirmation email.&#x20;

\
The inbox refreshes automatically, so there is no need to do it manually.

{% hint style="warning" %}
The BugBug inbox only saves emails for **10 minutes**. After that time, all emails will be removed.
{% endhint %}

Open the registration email by clicking on "subject".

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FNW7uSzFQy4nI1Q18395B%2Fsubject.png?alt=media&#x26;token=41252ac9-5902-4f80-a3e1-116c351d9b67" alt=""><figcaption><p>The BugBug confirmation email is used only as an example of the process.</p></figcaption></figure>

{% hint style="info" %}
**Important! Make sure you click the subject line of the email!** \
BugBug needs to always open the most recent email, so your [selector](https://docs.bugbug.io/preventing-failed-tests/selectors) here needs to click the first email with a specific subject line, for example `//SPAN[normalize-space(text())="`Confirm your e-mail address`"]`
{% endhint %}

Now just click the button with the authorization link and continue recording.&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F9NP3qGDS80IJvNbEWPmi%2Fconfirm%20button.png?alt=media&#x26;token=38dbfa9b-e71c-496c-9542-84c92385a62c" alt=""><figcaption><p>The BugBug confirmation email is used only as an example of the process.</p></figcaption></figure>

<details>

<summary>If your email doesn't have a button but just a verification link </summary>

If your verification link is shown directly as a string, this string will be different every time. BugBug will record a selector that matches exactly this string, for example //A\[normalize-space(text())="`https://`acmecorp`.com/#/activate`?key=60f0ae29-542a-4418-8529-41a01bf22fcc"]

In such case, you may need to manually update your selector after the recording so that it only checks if the text contains the beginning of the verification URL, for example `//*[contains(text(), "https://`acmecorp`.com/#/activate")`

</details>

When your email is confirmed you can return to the test page tab and continue.&#x20;

### Using specific email and virtual inbox features  &#x20;

If you need to use an email address with a specific alias during a test you can also use the BugBug Testing Inbox. The menu provides an option for a custom alias.&#x20;

Just select the **"Specific test email"** option.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F8aiEJBCp2TDmG9uGpoGk%2FmyEmail.png?alt=media&#x26;token=b90ea3be-24fc-4d79-b1ce-ec7b1f7a7dd2" alt=""><figcaption></figcaption></figure>

If this option is selected, you can create your email alias by typing.

{% hint style="info" %}
You create only an Alias for **@bugbug-inbox.com**.&#x20;

Do not put other domains.
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FtzYOJ7Ny15JkGUDwKSOC%2Falias.png?alt=media&#x26;token=d6e11de1-47a9-4278-a1be-a3471fe3924c" alt=""><figcaption></figcaption></figure>

This option also allows you to **open Inbox** with a specific email you set.

{% hint style="warning" %}
If you decide to create an alias, make sure it's unique. We do not limit inboxes per project or test. Make sure that other users will not be able to interrupt your tests with the same email address.
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FyVMlbyPcraF06pWjAESs%2Faliasinbox.png?alt=media&#x26;token=87176eb6-716b-43bc-8151-0761be206176" alt=""><figcaption></figcaption></figure>

### Using variables with BugBug Testing Inbox

By default, inbox uses only the **testRunId** variable, but you can boost it by freely changing it in your recorded steps.&#x20;

You can mix or change variables simply by changing the alias of the email and adding eg. a **timestamp** variable.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FYm07pvUf03GdeOJ6uj5i%2FtypeTextId.png?alt=media&#x26;token=92881833-04fb-420f-a5e3-dd63d2ba6efd" alt=""><figcaption><p>Add any variable as alias </p></figcaption></figure>

{% hint style="info" %}
You can open a virtual inbox by combining **<https://bugbug-inbox.com/>** and any **variable**.&#x20;
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FQLD6M7ixalr454fyE10I%2Ftab.png?alt=media&#x26;token=a430c859-947d-4a2b-a3a9-19b1d8841508" alt=""><figcaption><p>Combined URL </p></figcaption></figure>

## Profiles

### What are profiles?

Profiles are your own **presets for different variable values**. You can run tests or suites with profiles to override your default variables to a specific value. This is especially useful when [working with multiple development environments. ](#work-with-different-development-environments)

{% hint style="info" %}
**Important** To see the profile section in the test, you need to have at least 2 profiles. &#x20;
{% endhint %}

![You can quickly swap the profile in the menu near the "Run" button. This menu will not appear if you only have one default profile.](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FUrAZiXTITShS4lPbEWlI%2Fimage.png?alt=media\&token=03154cf6-a084-4523-bbe1-e2dd25750686)

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FPzxcCgXllhhgMhHkCwHG%2Fnew%20profile.png?alt=media&#x26;token=95e11ba1-031d-4a8e-b31e-60732dc49e2c" alt=""><figcaption><p>To add, remove and edit profiles go to the "Variables" tab</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FyyPRzALolmimuNPJoBLq%2FZrzut%20ekranu%202023-03-21%20152825.png?alt=media&#x26;token=ceb83aea-7c45-4338-8d53-23743af97ae3" alt=""><figcaption><p>Override variables in the profile settings. Leave an empty field to keep the default value.</p></figcaption></figure>

### Run a test with a profile to override variables

First, make sure that you have read about [what profiles](#what-are-profiles)[ are](#what-are-profiles), and then:

1. Create a profile in the "Variables" tab
2. Go to test editing
3. Swap profiles before running the test in the menu near the "Run" button

You can also run tests with a [profile from the command line](#override-variables-and-profiles-from-command-line-cli) in your pipeline

{% hint style="info" %}
**Important!** Profiles selection is not saved in the test. \
If you run the test from the tests list, we will ask you to select a profile.&#x20;
{% endhint %}

{% hint style="info" %}
**Tip!** Your tests should pass on all profiles. Don't create tests that only work in one profile.&#x20;
{% endhint %}

### Run a suite with a profile

You can have multiple suites and each suite can run your tests with a specific profile. For example, you create suites for "Production smoke tests" and "Staging all tests". Each suite will have different sets of tests that will run on different profiles with different variables.

1. Go to "Suites" and select a suite to edit
2. Choose with which profile this suite will run

{% hint style="info" %}
**Important!** This suite will always run with this profile. The profile selection is saved in the suite settings.&#x20;
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FdQGIdHRxuoHKoopfMcml%2Fprofile.png?alt=media&#x26;token=f8343800-6334-4ba6-9ae7-5c4337ff4b8a" alt=""><figcaption></figcaption></figure>

### Work with different development environments

Let's say you have 3 environments: *production, staging, and local*. They are all exactly the same, but they have different URL addresses. You want to run the test sometimes on production and sometimes on staging.

| Environment | URL              |
| ----------- | ---------------- |
| Production  | `acme.com`       |
| Staging     | `stage.acme.com` |
| Local       | `localhost:3000` |

**Prepare the variables and profiles**

1. Create a variable named `hostname` with default value `https://acme.com`
2. Create 2 profiles named `Staging` and `Local`
3. Override the hostname variable in the profile Staging for `https://stage.acme.com`
4. Override the hostname variable in the profile `Local` for `https://localhost:3000`

#### Update the URLs with your variable

1. In the tests, find your steps with `Go to url` action
2. Replace the `acme.com` with `{{hostname}}`.&#x20;

**Tip:** You can also combine the curly brackets with the rest of the URL for example `{{hostname}}/registration` or `app.{{hostname}}`

Now you can [run the tests with different profiles](#run-a-test-with-a-profile-to-override-variables) and quickly swap between your dev environments.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FL9chpQmQrcDRZqlePYfh%2Fimage.png?alt=media\&token=891f04a1-ffdb-4215-b979-25dfaa011e3f)

### Override variables and profiles from the command line (CLI)

Use [BugBug CLI ](https://docs.bugbug.io/integrations/api)to integrate with your build pipelines and run tests with variables that you can adjust to multiple environments.&#x20;

If you run tests or suites from the command line, you can override each variable or profile with parameters, for example,  `--variable val1=value` and `--profile=profileName`. Read more in the [CLI documentation](https://www.npmjs.com/package/@testrevolution/bugbug-cli).

## JavaScript variables

Javascript variables allow you to compute dynamic values every time the variable is used in a test.&#x20;

#### Use JavaScript variables for:

* Getting data from API, for example, SMS codes, authorization magic links
* Mathematical calculations such as adding, subtracting, multiplying, etc.
* Generating unique strings that need to meet specific validation criteria such as social security numbers,  postal codes
* Values that are different depending on conditions, for example, if your app shows a different text during night and daytime

#### **To create a JavaScript variable**&#x20;

1. Go to the "Variables" tab and click "New variable"
2. Change the variable type to "Custom JavaScript"
3. Enter a JavaScript function that will be executed every time this variable is used in the test

{% hint style="info" %}
**Important!** Remember that your function needs to have a `return` statement - it needs to return a specific value.
{% endhint %}

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FJhTTD3ywHYBnZXbGEb71%2FScreenshot%202022-04-05%20at%2011.47.15.png?alt=media\&token=77a74fc9-329a-40db-905a-4040277515e7)

### Example JavaScript variable functions

Return a simple string value:

```
async function(variables) {
    let firstName = "John";
    let lastName = "Smith";
    return firstName + lastName;
}
```

Return a different value when the day of the week is Sunday:

```
async function(variables) {
    const d = new Date();
    let day = d.getDay();
    if (day === '7') {
        return "Delivery in 48 hours"
    } else {
       return "Delivery in 24 hours"
    }
}
```

### Use the "variables" argument in your JavaScript function

Your custom JS variable can also read your other variables. The `variables` argument stores all the built-in variables, your custom variables, and local variables recorded during the test run. <br>

If you run a custom javascript step with a function `console.log(variables)` you will get such an output in the console:&#x20;

```
{
    hostname: "https://marmelab.com/react-admin-demo/"
    profileName: "Default"
    runMode: "local"
    scheduleId: null //only for scheduled runs
    scheduleName: null //only for scheduled runs
    startDemoURL: "https://marmelab.com/react-admin-demo/"
    suiteId: "54bd4384-ad9c-4e83-946f-111392ed0a82"
    suiteName: "All tests"
    suiteRunId: "18e1e3c3-ec2a-45c9-b817-8f48a56a0807"
    testId: "37e64599-31a9-4707-9fed-a64cdec24294"
    testName: "Test"
    testRunId: "6498c9bd-81a5-412f-a275-2c7f1cfc4d45"
    timestamp: 1665667075470
    username: "demo"
}
```

You can use this to operate on the variables, combine them, calculate, etc.&#x20;

```
async function(variables) {
    return variables.firstName + variables.lastName
}
```

```
async function(variables) {
    return variables.userEmail + variables.testRunId
}
```

```
async function(variables) {
    return variables.userHeightInCentimeters + 20;
}
```

{% hint style="info" %}
**Important!** Variables are calculated immediately before a step is executed. If you want to calculate variable only once per test, use `localStorage` to cache the result and then access it with [custom javascript steps](https://docs.bugbug.io/editing-tests/custom-javascript-actions).
{% endhint %}

{% hint style="warning" %}
**Important!** Other Custom JavaScript variables are not available in the `variables` object. This is impossible because you can't specify the order in which the JS variables are calculated or control the dependencies. See the `localStorage` workaround below.
{% endhint %}

{% hint style="info" %}
**Important!** Do not use the local variable and its combination in steps before BugBug captures the wanted value. Otherwise, BugBug will return an <mark style="color:red;">`undefined`</mark> string instead of the desired [local value](https://docs.bugbug.io/editing-tests/local-variables).
{% endhint %}

### Use localStorage to pass on data between variables

If you want to access a variable that was already calculated in a previous step, use `localStorage`.&#x20;

1. At the end of the function in the first variable, store the result in `localStorage`.&#x20;

```
async function(variables) {
    let name = variables.firstName + variables.lastName;
    localStorage.setItem('bugbugUserName', name);
    return name;
}
```

2\. At the beginning of the next variable get the value from `localStorage`.

```
async function(variables) {
    let name = localStorage.getItem('bugbugUserName', name);
    if (name === 'Carl') {
        ...
    }
}
```
