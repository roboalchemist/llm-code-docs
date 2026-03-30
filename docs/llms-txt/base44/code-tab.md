# Source: https://docs.base44.com/developers/app-code/editor/code-tab.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Code Tab

> Edit your app's source code directly in Base44's Code tab with live preview and full developer control.

The Code tab lets you view and edit your app's source code directly, giving you control over your app's functionality, design, and behavior while seeing changes immediately.

<Note>
  The Code tab is for developers who want more control. For simpler changes, use
  Base44's visual editor and AI tools.
</Note>

<Frame caption="The Code tab interface showing your app's source code">
    <img src="https://mintcdn.com/base44/HSXlsKQvBkYN-DXR/codeer.png?fit=max&auto=format&n=HSXlsKQvBkYN-DXR&q=85&s=845561c033d8e1acadf501429ed5efbb" alt="The Code tab interface showing your app's source code" width="1915" height="958" data-path="codeer.png" />
</Frame>

## Access the Code tab

**To open the Code tab:**

1. Go to your app's dashboard.
2. Click the **Code** tab.

The Code tab displays your [project files](../overview/project-structure) in a file explorer on the left, with the code editor taking up the main space.

<Frame caption="Accessing the Code tab from your app dashboard">
    <img src="https://mintcdn.com/base44/hrVkAqsRzoi9NYCy/images/codepanel.png?fit=max&auto=format&n=hrVkAqsRzoi9NYCy&q=85&s=26096b47df03c978b9a81a823cd179fd" alt="Accessing the Code tab from your app dashboard" width="1912" height="955" data-path="images/codepanel.png" />
</Frame>

## Navigate your codebase

Use the **Files used in this page** feature to see which files power the page you're previewing. This shows you exactly which code files are running, so you know where to go when you want to edit the page or investigate an issue.

Each entry in the list shows the file name and its folder path, grouped by location in your project such as pages or components.

**To view files used on a page:**

1. Go to your app editor.
2. Click the **More Actions** icon at the top right.
3. Click **Files used in this page**.

<Frame caption="Viewing files used on a page of your app">
    <img src="https://mintcdn.com/base44/ml9BQnGdt1cp4mqU/images/seeallfiles.png?fit=max&auto=format&n=ml9BQnGdt1cp4mqU&q=85&s=2017f1a72e6b880c7405b9c6c1d8784c" alt="Viewing files used on a page of your app" width="2532" height="1208" data-path="images/seeallfiles.png" />
</Frame>

<Tip>
  If you want to move from this focused view into the full file structure, click
  **See all files**. This takes you to the complete code files view so you can
  keep exploring from there.
</Tip>

## Edit with live preview

The Code tab offers a split-screen view that shows your code on one side and a live preview of your app on the other. This lets you see changes instantly without switching contexts.

<Frame caption="Split screen view showing code and live preview">
    <img src="https://mintcdn.com/base44/Kb6mZTf4mNXOF_gr/images/split.png?fit=max&auto=format&n=Kb6mZTf4mNXOF_gr&q=85&s=3b0556cac2c3cac886d1332d10521dc4" alt="Split screen view showing code and live preview" width="1908" height="390" data-path="images/split.png" />
</Frame>

**To edit with live preview:**

1. Open a file in the Code tab.
2. Click the split-screen toggle in the top right corner.
3. Edit your code on the left and see your changes on the right.

**Every time you make changes to the code:**

* Click **Save** at the bottom of the screen to apply your changes and refresh the preview with the latest code.
* Click **Discard** at the bottom of the screen if you want to drop all unsaved edits and return to the last saved version of the file.

<Warning>
  **Important:** If you make changes to your app's code, make sure to click
  **Publish** for them to go live on your app.
</Warning>

When you are ready to leave the split screen, click **Exit split**.

For local development with your own IDE, see [GitHub Integration](../local-development/github).

## FAQs

<AccordionGroup>
  <Accordion title="Can I edit every part of my app's code?">
    Yes. You can open and edit any code file that appears in the Code files
    panel, including pages, components, layouts, and entity helpers. If a part
    of the app is generated for you, it still appears as regular code that you
    can modify.
  </Accordion>

  <Accordion title="Do I need to use split screen to edit code?">
    No. You can work in the full width code editor if you prefer more space.
    Split screen is helpful when you want to see the preview next to your code,
    but you can turn it off at any time and reopen it later.
  </Accordion>

  <Accordion title="What happens if I click Discard?">
    Discard removes all unsaved changes in the active file and restores the last
    saved version. This is useful if you try something that does not work and
    want to go back quickly. Once you click Discard, you cannot recover the
    unsaved code from that session.
  </Accordion>

  <Accordion title="Do I need to be an experienced developer to edit the code?">
    You don't need to be an expert, but basic familiarity with React and JSX
    helps. You can start with small changes such as updating text, swapping
    components, or changing simple styles, then move on to more advanced logic
    as you gain confidence
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).