# Source: https://flatfile.com/docs/core-concepts/documents.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Documents

> Standalone webpages within Flatfile Spaces for guidance and dynamic content

Documents are standalone webpages for your Flatfile [Spaces](/core-concepts/spaces). They can be rendered from [Markdown syntax](https://www.markdownguide.org/basic-syntax/).

Often used for getting started guides, Documents become extremely powerful with dynamically generated content that stays updated as Events occur.

Flatfile also allows you to use HTML tags in your Markdown-formatted text. This is helpful if you prefer certain HTML tags rather than Markdown syntax. Links in documents (both Markdown and HTML) automatically open in a new tab to ensure users don't navigate away from the Flatfile interface.

<Frame caption="An example Welcome Document with steps for data import">
  <img src="https://mintcdn.com/flatfileinc/1Ya11_XgeUaQ5e1v/static/images/document.png?fit=max&auto=format&n=1Ya11_XgeUaQ5e1v&q=85&s=03550278ec929bc8fd9490d998168533" width="610" data-og-width="3028" data-og-height="1778" data-path="static/images/document.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/flatfileinc/1Ya11_XgeUaQ5e1v/static/images/document.png?w=280&fit=max&auto=format&n=1Ya11_XgeUaQ5e1v&q=85&s=cbb7f200f917b3aff17af71d312d4bc9 280w, https://mintcdn.com/flatfileinc/1Ya11_XgeUaQ5e1v/static/images/document.png?w=560&fit=max&auto=format&n=1Ya11_XgeUaQ5e1v&q=85&s=1f55dbe0fb8259dbf00fe7325f350de6 560w, https://mintcdn.com/flatfileinc/1Ya11_XgeUaQ5e1v/static/images/document.png?w=840&fit=max&auto=format&n=1Ya11_XgeUaQ5e1v&q=85&s=5af18a338f94c4eee3371c5d78949a94 840w, https://mintcdn.com/flatfileinc/1Ya11_XgeUaQ5e1v/static/images/document.png?w=1100&fit=max&auto=format&n=1Ya11_XgeUaQ5e1v&q=85&s=2c36335f92bf1eec1c48b942b026f040 1100w, https://mintcdn.com/flatfileinc/1Ya11_XgeUaQ5e1v/static/images/document.png?w=1650&fit=max&auto=format&n=1Ya11_XgeUaQ5e1v&q=85&s=b39c37ee5bcd6f995c1d4d903dc8351d 1650w, https://mintcdn.com/flatfileinc/1Ya11_XgeUaQ5e1v/static/images/document.png?w=2500&fit=max&auto=format&n=1Ya11_XgeUaQ5e1v&q=85&s=80cda307d30ebbeca050b9d3fb551ae3 2500w" />
</Frame>

## Key Features

<Note>
  **A note on Documents:** While Documents themselves can be created and updated [dynamically](/core-concepts/documents#dynamic-content), the content inside of a document should be considered to be *static* - that is, you cannot use documents to host interactive elements or single-page webforms. For that sort of functionality, we recommend using [Actions](/core-concepts/actions) to trigger a [Listener](/core-concepts/listeners) to perform the desired functionality.
</Note>

### Markdown-Based Content

Documents support GitHub-flavored Markdown, allowing you to create rich, formatted content with headers, lists, code blocks, and more. You can also use HTML tags within your Markdown for additional formatting flexibility.

### Dynamic Content

Documents can be created and updated programmatically in response to Events, enabling dynamic content that reflects the current state of your Space or data processing workflow.

### Document Actions

Add interactive buttons to your Documents that trigger custom operations. [Actions](/core-concepts/actions) appear in the top right corner and can be configured with different modes, confirmations, and tooltips.

### Embedded Blocks

Documents support embedding interactive data blocks (Workbooks, Sheets, and Diffs) directly within the content. See the [Adding Blocks to Documents](#adding-blocks-to-documents) section for detailed implementation.

## Create a Document

You can create Documents upon Space creation using the [Space Configure Plugin](/plugins/space-configure), or dynamically in a [Listener](/core-concepts/listeners) using the API:

```javascript  theme={null}
import api from "@flatfile/api";

export default function flatfileEventListener(listener) {
  listener.on("file:created", async ({ context: { spaceId, fileId } }) => {
    const fileName = (await api.files.get(fileId)).data.name;
    const bodyText =
      "# Welcome\n" +
      "### Say hello to your first customer Space in the new Flatfile!\n" +
      "Let's begin by first getting acquainted with what you're seeing in your Space initially.\n" +
      "---\n" +
      "Your uploaded file, ${fileName}, is located in the Files area.";

    const doc = await api.documents.create(spaceId, {
      title: "Getting Started",
      body: bodyText,
    });
  });
}
```

This Document will now appear in the sidebar of your Space. Learn how to [customize the guest sidebar](/guides/customize-guest-sidebar) for different user types.

In this example, we create a Document when a file is uploaded, but you can also create Documents in response to any other Event. [Read more](/reference/events) about the different Events you can respond to.

## Document Actions

Actions are optional and allow you to run custom operations in response to a user-triggered event from within a Document.

Define Actions on a Document using the `actions` parameter when a document is created:

```javascript  theme={null}
import api from "@flatfile/api";

export default function flatfileEventListener(listener) {
  listener.on("file:created", async ({ context: { spaceId, fileId } }) => {
    const fileName = (await api.files.get(fileId)).data.name;
    const bodyText =
      "# Welcome\n" +
      "### Say hello to your first customer Space in the new Flatfile!\n" +
      "Let's begin by first getting acquainted with what you're seeing in your Space initially.\n" +
      "---\n" +
      "Your uploaded file, ${fileName}, is located in the Files area.";

    const doc = await api.documents.create(spaceId, {
      title: "Getting Started",
      body: bodyText,
      actions: [
        {
          label: "Submit",
          operation: "contacts:submit",
          description: "Would you like to submit the contact data?",
          tooltip: "Submit the contact data",
          mode: "foreground",
          primary: true,
          confirm: true,
        },
      ],
    });
  });
}
```

Then configure your listener to handle this Action, and define what should happen in response. Read more about Actions and how to handle them in our [Using Actions guide](/guides/using-actions).

Actions appear as buttons in the top right corner of your Document.

## Document treatments

Documents have an optional `treatments` parameter which takes an array of treatments for your Document. Treatments can be used to categorize your Document. Certain treatments will cause your Document to look or behave differently.

### Ephemeral documents

Giving your Document a treatment of `"ephemeral"` will cause the Document to appear as a full-screen takeover, and it will not appear in the sidebar of your Space like other Documents. You can use ephemeral Documents to create a more focused experience for your end users.

```javascript  theme={null}
const ephemeralDoc = await api.documents.create(spaceId, {
  title: "Getting started",
  body: "# Welcome ...",
  treatments: ["ephemeral"],
});
```

Currently, `"ephemeral"` is the only treatment that will change the behavior of your Document.

## Adding Blocks to Documents

Blocks are dynamic, embedded entities that you can use to display data inside a Document. You can add a Block to a Document using the `<embed>` HTML entity in your markdown and specifying which Block type you want to show using the `type` attribute on the entity. Three Block types are currently supported: Embedded Workbook, Embedded Sheet, and Embedded Diff.

### Embedded Workbook

Use this Block to render an entire Workbook with all its Sheets inside a Document, providing users with tabbed navigation between sheets. You can embed a Workbook by passing a workbook ID and optional name. You can also control whether the embedded Workbook is expanded when the document loads and whether to show the header.

```javascript  theme={null}
const doc = await api.documents.create(spaceId, {
  title: "Getting started",
  body:
    "# Welcome\n" +
    "\n" +
    "Here is an embedded Workbook:\n" +
    "\n" +
    "<embed type='embedded-workbook' name='Customer Data' defaultExpanded='true' showHeader='true' workbookId='your_workbook_id'>\n" +
    "\n" +
    "Here is another embedded Workbook without header:\n" +
    "\n" +
    "<embed type='embedded-workbook' showHeader='false' workbookId='us_wb_8e0z52gI'>",
});
```

**Properties:**

* `workbookId` (required): The ID of the workbook to embed
* `name` (optional): Display name for the embedded workbook
* `defaultExpanded` (optional): Whether the workbook is expanded when the document loads (defaults to false)
* `showHeader` (optional): Whether to show the workbook header (defaults to true). When false, the workbook is automatically expanded

### Embedded Sheet

Use this Block to render a Sheet along with all its data inside of a Document. You can embed a Sheet into your Document by passing a sheet ID, workbook ID, and name. You can also specify whether the embedded Sheet is expanded or collapsed when the document is loaded, and whether to show the header.

You can include as many embedded Sheets in your Document as you like, but end users will only be able to expand a maximum of 10 embedded Sheets at once.

```javascript  theme={null}
const doc = await api.documents.create(spaceId, {
  title: "Getting started",
  body:
    "# Welcome\n" +
    "\n" +
    "Here is an embedded Sheet:\n" +
    "\n" +
    "<embed type='embedded-sheet' name='Contacts' defaultExpanded='true' showHeader='true' sheetId='your_sheet_id' workbookId='your_workbook_id'>\n" +
    "\n" +
    "Here is another embedded Sheet without header:\n" +
    "\n" +
    "<embed type='embedded-sheet' name='Countries' showHeader='false' sheetId='us_sh_TVW95224' workbookId='us_wb_8e0z52gI'>",
});
```

**Properties:**

* `sheetId` (required): The ID of the sheet to embed
* `workbookId` (required): The ID of the workbook containing the sheet
* `name` (optional): Display name for the embedded sheet
* `defaultExpanded` (optional): Whether the sheet is expanded when the document loads (defaults to false)
* `showHeader` (optional): Whether to show the sheet header (defaults to true). When false, the sheet is automatically expanded

### Embedded Diff

Use this Block to show a side-by-side comparison of the data in a Sheet now versus at a previous point in time as captured by a Snapshot. Pass a Sheet ID, Workbook ID, and Snapshot ID. You can optionally pass a `direction` attribute which specified whether the changes are displayed with the Snapshot as the end state (`sheet_to_snapshot`) or the Sheet as the end state (`snapshot_to_sheet`). The default value for direction is `sheet_to_snapshot`.

Use `direction="sheet_to_snapshot"` if you want to show changes that have been made since the time the Snapshot was taken, i.e. to review past changes. Use `direction="snapshot_to_sheet"` if to preview the changes that would occur if you were to revert your Sheet back to the state it was in when the Snapshot was taken.

```javascript  theme={null}
const doc = await api.documents.create(spaceId, {
  title: 'Getting started',
  body:
    "# Welcome\n" +
    "\n" +
    "Here is an embedded Diff:\n" +
    "\n" +
    "<embed type='embedded-diff' sheetId='your_sheet_id' workbookId='your_workbook_id' snapshot_id='your_snapshot_id" direction="snapshot_to_sheet">"
  ,
})
```

## Markdown reference

Documents support Github-flavored Markdown. Check out [this guide](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for a full reference on the entities you can use.
