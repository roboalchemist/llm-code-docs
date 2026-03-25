# Source: https://docs.bugbug.io/editing-tests/local-variables.md

# Local variables

BugBug has the option to set up and insert a variable from the tested source during test recording. Now you can store any text value from the web page you are testing in a variable and use it in feature steps. For example, to find out newly registered unique users in your CRM. Also, you can use built-in variables or custom variables added to the project.&#x20;

A new option for **variables** in the test recording process can be found in the **BugBug Extension overlay**.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FzXt74muO2oZ029AEiahi%2F1_recorder.png?alt=media&#x26;token=6e5c59cf-bf71-45f1-8a51-af54048bc1c8" alt="" width="284"><figcaption><p>Variables button in recorder</p></figcaption></figure>

When you click on the "**Variables**" button there will be two options:

* Save variable for later
* Insert variable

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FFDlqqL5U1IM7gdyr5ioH%2FZrzut%20ekranu%202023-04-03%20120138.png?alt=media&#x26;token=713c1990-5c94-453b-9bc0-deb0cb3c723d" alt=""><figcaption></figcaption></figure>

### Save variable for later&#x20;

This option is used to save the new text value as a variable during the test recording. You can find an element and copy the value directly from the browser. Now there is no need to hardcode values and change them later in a BugBug web app steps edition. You can move forward. <br>

Click on the "**Save variable for later**" button. Saving a variable mode is now active.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FL77P8Hp2JW8vInPErfoi%2F2_saveForLater.png?alt=media&#x26;token=a1ae9b0a-92d2-4157-8199-4f078463791e" alt=""><figcaption><p>Click on a "Save variable for later" button</p></figcaption></figure>

At this time you can click on an element with text value on a tested web app and save it into a variable. For example, you can save the search phrase - *"Bugbug automation tool"*.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FQdEsHgQ75H4HLOS3PDRh%2F3_saveForLater.png?alt=media&#x26;token=f1804c1f-f448-41eb-87cb-9612df3701fd" alt=""><figcaption><p>Click the item with the desired text value</p></figcaption></figure>

When an element is selected and a value is recorded, you will see an input in the BugBug extension menu where you can save the name for the new variable. Later this name will be visible in a list of variables in the BugBug extension menu.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FCsxfMkjlyduJ7KZwsRfr%2F4_saveForLater.png?alt=media&#x26;token=c0535a58-54c3-4245-bc6d-dffcf04cec02" alt=""><figcaption><p>No spaces or other special characters allowed</p></figcaption></figure>

When you save a variable, you will be taken to the main menu of the BugBug extension and can continue recording steps.

{% hint style="info" %}
The saved variable is a cross-domain feature. Now you can use the saved value on different web apps in one test. eg. You can open a new tab and use the stored value there.&#x20;
{% endhint %}

{% hint style="warning" %}
The variable can be overwritten several times during the test recording by using the same name. If you want to avoid this situation, use some unique names each time.
{% endhint %}

{% hint style="warning" %}
Using the same name of the variable as the built-in or custom variable name will override the data. This can cause a problem if your test is based on them and overriding these variables is not intended.
{% endhint %}

### Insert a variable during step recording

Now you can insert a variable during step recording in BugBug. You can use saved variables from previous steps, use custom variables from the project, or use global variables that are predefined by default.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Ffdtbsex1j77lbwFzgZbC%2FInsert%20variable.png?alt=media&#x26;token=fed2a6b6-a490-4da1-8b52-48146cee592a" alt=""><figcaption></figcaption></figure>

Click the "**Insert Variable**" button. A variable menu will open. As you can see, we suggest the last saved variable by default. Every variable has a name and length-limited value presented below the name. You can open the drop-down menu to select another variable from the list. [Available variables](#available-variables.) will be discussed in another chapter. Now we will focus on how to insert our saved variable into the designated input.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FAQdlfhKDX7r4BD3Qwfpo%2F5_useVariable.png?alt=media&#x26;token=40533faf-2168-4819-9ed9-f3bdf15c1e45" alt=""><figcaption></figcaption></figure>

When you open the "**Insert variable**" menu the insert variable mode is now active for the selected variable. Now let's move on to the web application we're testing.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FoupFn143LvDibgHKYVbH%2F5_useVariable.png?alt=media&#x26;token=2d6ef13e-28f4-4754-8499-a5655eb98e78" alt=""><figcaption><p>Find an input you want to fill with the variable</p></figcaption></figure>

If you have an input that you want to automatically fill and you have opened the Insert Variable menu with the selected variable, you can simply click on an input to fill it with a value.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FCNAc0moYBvht30EMIhnd%2F6_useVariable.png?alt=media&#x26;token=cc3d22a6-5b5f-42c7-ae9c-70abad3af45b" alt=""><figcaption></figcaption></figure>

The "**Insert variable**" menu closes. The entry is saved with the value, and you can continue recording steps such as clicking Enter to open search results.

### Available variables &#x20;

During recording, you can also insert a variable added by default from BugBug such as: <br>

* Built-in variables&#x20;
* Custom variables&#x20;

All these variables are described in the [Variables](https://docs.bugbug.io/editing-tests/variables) section of BugBug documentation. <br>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FzbsFJ26KV2LXm0bkjeHL%2FVariables.png?alt=media&#x26;token=6a30e561-f0cc-4cc4-a238-ed84337a16ae" alt=""><figcaption><p>Variables added by default to insert list. </p></figcaption></figure>

Using built-in or custom variables is now easy and you do not need to edit steps in the BugBug web application UI. You can find them in the list.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fk4SSziLYXVIIV53dvsoq%2FZrzut%20ekranu%202023-04-04%20104323.png?alt=media&#x26;token=9f9e9f7a-22e2-4fb2-8e66-a2ee8fbe32a6" alt=""><figcaption></figcaption></figure>

### Unavailable variables during step recording &#x20;

#### Built-in variables based on a suit or scheduled run &#x20;

We cannot provide data such as {{suiteRunId}} because when recording, there is no suiteRunId. It's only accessible when the suite is running. You can insert this variable in normal test-edit mode on the BugBug web app UI for a case.&#x20;

{% hint style="info" %}
Some of the built-in variables are now disabled with notification. BugBug cannot import data from these variables. You can use it in step edit on the BugBug web app UI.&#x20;
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fk4SSziLYXVIIV53dvsoq%2FZrzut%20ekranu%202023-04-04%20104323.png?alt=media&#x26;token=9f9e9f7a-22e2-4fb2-8e66-a2ee8fbe32a6" alt=""><figcaption></figcaption></figure>

#### Custom JS variables&#x20;

Currently, there is no way to use a custom js variable during test recording. We are working on providing such a feature, but for now, we can only use variables with values that are accessible before the test starts recording.\
You can use custom JS variables in step edit on BugBug web app as we [suggest](https://docs.bugbug.io/editing-tests/custom-javascript-actions) in our documentation.&#x20;

### Search variables on the list&#x20;

You can search for variables on the BugBug extension list by the variable name.&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fy84RjN8eshJOxU3okem7%2FSearch.png?alt=media&#x26;token=e418d3e1-5be5-48d0-bf68-0b038e786b6c" alt=""><figcaption></figcaption></figure>

### Local variables in web app UI&#x20;

There is a new step form for local variables recorded from the tested source. You can edit this variable freely. The recorded variable can be found in the step list as a "set variable".

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FtSzKRtcGOaBOPau7cVLA%2Fset%20variable.png?alt=media&#x26;token=fe70fe60-180c-466b-971d-4e69301a8974" alt=""><figcaption><p>Recorded step for local variable</p></figcaption></figure>

You can edit values such as the variable name or the correct item selector in the BugBug web application UI after you have finished recording.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FaWlbEurlJk5QlsSa19r1%2Fset%20variable%202.png?alt=media&#x26;token=90a84b37-3c0a-474a-9a39-44a740aab9c2" alt=""><figcaption></figcaption></figure>

**Use a local variable**

You can use local variables by selecting the "Insert variable" option during recording in the BugBug overlay. At the end of the recording session, the step using the local variable will be saved as "Type text" with the variable name used in the "value" field.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FrcZ6iPvtNUWqj0lA6Fdm%2Fput%20variable.png?alt=media&#x26;token=c2ddd315-2e8b-4a9e-931a-da06af0f4b86" alt=""><figcaption></figcaption></figure>

You can also add a local variable from the BugBug web app UI by selecting "add a new step" on the list and filling it all manually.&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FXTLThjLWAc5iIrwxZ3D9%2FZrzut%20ekranu%202023-04-11%20105018.png?alt=media&#x26;token=1c4648a8-8fa9-47e6-ac56-91c5f7259a35" alt=""><figcaption></figcaption></figure>

Select "Set variable" from the modal.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FBomqwpOcrAWB8vyvIknU%2FZrzut%20ekranu%202023-04-11%20105541.png?alt=media&#x26;token=1963733d-3e36-4713-8206-444df33e610b" alt=""><figcaption></figcaption></figure>

And fill in the requested inputs&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FG1dh8mjDTmYQ5VShouen%2FZrzut%20ekranu%202023-04-11%20105752.png?alt=media&#x26;token=4cc37aab-67f4-4ed9-959d-f09034a9cc3b" alt=""><figcaption></figcaption></figure>

Any recorded local variable can be used in the following steps by mentioning the local variable name in double curly brackets e.g. {{savedVariable}} in any text field like an assertion or custom selector. For more info check out [what are variables](https://docs.bugbug.io/editing-tests/variables#what-are-variables).

### Combine local and other variables in one JS custom variable&#x20;

You can create a new variable using two different values in the JS form, which allows you to combine stored variables from the recording process and those that we provide as default global variables.<br>

When you set variable from recording&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F8FCPhPrahqbIM5pAOmQ0%2Fset%20variable.png?alt=media&#x26;token=4c0531c6-e6ea-4746-9879-418e21672523" alt=""><figcaption></figcaption></figure>

You can use its name when creating a [new custom JS variable](https://docs.bugbug.io/variables#javascript-variables). All stored variables are accessible in JS form by using the argument <mark style="color:red;">`variables`</mark> combined with the variable name.&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FSaJLzRgI152agxEc5HbV%2Fvariable%20name.png?alt=media&#x26;token=b766b633-d26d-47b5-bf6c-605fb7f7751c" alt=""><figcaption></figcaption></figure>

When you use a new custom JS variable in step, BugBug will automatically combine the stored value with another variable that you want. These options allow you to combine values from all saved variables. You can call them as many times as you like.

To use a newly created variable, just put a variable name in double braces. After the first test run, you can find the calculated value of your variable from the previous test run in Step Details.\ <br>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fp1eIWL2BdeiQ8GcrtT1h%2Fcomputed%20value.png?alt=media&#x26;token=d4516ffe-b067-46af-bfa9-8e747b4a64b2" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Do not use the local variable and its combination in steps before BugBug captures the wanted value. Otherwise, BugBug will return an <mark style="color:red;">`undefined`</mark> string instead of the desired local value.
{% endhint %}
