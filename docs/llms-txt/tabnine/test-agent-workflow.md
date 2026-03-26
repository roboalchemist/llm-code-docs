# Source: https://docs.tabnine.com/main/getting-started/tabnine-testing/test-agent-workflow.md

# Test Agent Workflow

### Generating Test Suggestions

To generate test suggestions, head to the snippet of code or function in the code that you want to test.

Above the relevant snippet, you will see the code lens menu from Tabnine (This will look different depending on the IDE). In Visual Studio Code, everything in the menu, aside from the word “Tabnine” itself (in JetBrains IDEs, the Tabnine logo itself), is clickable:

Tabnine | **Edit** | **Test** | **Explain** | **Document** | **Ask**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-91e9cf1a1ac117d0cfd358df36fb268db0b64ca0%2FShowing%20Gray%20Tabnine%20Menu%20.png?alt=media" alt=""><figcaption></figcaption></figure>

To open the Tabnine test agent, do one of the following three things:

1. Click **Test** above the code snippet. The test widget will open to the left side of the screen (in Visual Studio).
2. Go to the Test panel next to the Chat panel
3. Write `/test` in the Chat window

As mentioned in our Chat documentation, Tabnine makes use of the full context of your requests. That includes existing testing files and open project files.

You will see a window open asking if you do or do not already have a test file. You will have the option to either locate it or select a location for generating a new one:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d31d77bceb4e6a06ebd2471cf758a224d51dc451%2FGenerate%20Test%20Suggestions%201.gif?alt=media" alt=""><figcaption></figcaption></figure>

#### Updating the Test Plan State / Regenerating Test Suggestions

Once you've loaded the tests you want, update the Test Plan window by hitting the cycling ⟳ symbol in the upper righthand corner of the **Test plan** window:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-e4adbbb0f11d424e9ae2c07f1c4d8efd5a9b9f20%2FRegenerate%20Test%20Suggestions.gif?alt=media" alt=""><figcaption></figcaption></figure>

#### Return to the Test Plan Window

At any time, you can return to the Test plan window by clicking the beaker icon between the chat icon and the Settings cog:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-49c33e3c5e618d4133200812a66d3df029ca1dc4%2FSwitch%20Chat%20to%20Test%20GIF.gif?alt=media" alt=""><figcaption></figcaption></figure>

### Insert Test Code into Test File

You will see multiple options for inserting the suggested testing code into the test file. The three options are:

1. Apply
2. Insert
3. Copy

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-bdeeace7c1b33fcd9659f4c3cdad26c1cd179db8%2FApply%20Insert%20Copy%20Thumbs%20Up%20Thumbs%20Down.png?alt=media" alt=""><figcaption></figcaption></figure>

#### Apply

Hitting "Apply" is the simplest of the options. For the test code, Tabnine will automatically place it at the end as the last segment of code in the file.

#### Insert

Insert is somewhat more like human-in-the-loop (HITL), where you deliberately select the placement of the test code by pre-clicking the location. You will see the text cursor floating / blinking there. In this situation, you have to be sure the correct location is marked.

#### Copy

Copying the code is the most manual process. Some might prefer this when wanting to be extra precise that the code is not errantly put in the wrong place.

Here, copy the code, ***THEN*** navigate to where you want it, and only then finally paste it.

### Modifying Test Cases

In the text bar below the selected test, write in how you want to modify the test. After a few seconds, the regenerated test will be available.

If you had already applied or inserted the previous version of that test into the code, Tabnine will pinpoint what to replace.

Simply press <mark style="color:blue;">**Apply**</mark>, then the new test language will appear highlighted over the previous testing language. Press Alt+A on the keyboard or **✓ Accept the change (Alt+A)** above the highlighted section to implement the new test:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-e27266db357e011fcfff124e2af022cd1216c42d%2FApply%20and%20Accept%20Change.gif?alt=media" alt=""><figcaption></figcaption></figure>

### Adding Custom Test Cases

Below the full list of suggested tests, you can request the generation of another test.

In our example, our word game should also come up with results that uses letters more than once, so we ask Tabnine to create such a test:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-26a3eafde6527ffb17c7eab5f21750b6e605a157%2FTest%20for%20repeated%20letters.gif?alt=media" alt=""><figcaption></figcaption></figure>
