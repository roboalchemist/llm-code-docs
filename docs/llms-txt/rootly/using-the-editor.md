# Source: https://docs.rootly.com/collaborative-retrospectives/using-the-editor.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Retrospective Editor

> Learn how to use the collaborative retrospective editor's formatting tools, slash commands, data blocks, and templates to write effective incident retrospectives.

## How the Editor Works

The new retrospective editor provides a rich text editing experience with real-time collaboration, dynamic data blocks, and template support. This page covers everything you need to know to create and edit retrospectives effectively.

The editor is designed to be intuitive. You can type naturally, use slash commands for quick actions, and let autosave handle the rest.

## Getting Started with the Editor

### Where to Find the Editor

<Steps>
  <Step title="Open the incident">
    Navigate to the incident from the incidents list or a direct link.
  </Step>

  <Step title="Go to the Retrospective tab">
    Click the **Retrospective** tab on the incident page.
  </Step>

  <Step title="Click the document preview">
    Click anywhere in the document preview to start navigate to the editor.
  </Step>

  <Step title="Begin editing">
    The editor opens with your team's default template pre-appended to the document. Start typing or use slash commands to add content.
  </Step>
</Steps>

<Info>
  Retrospective documents automatically populate with your team's default template. You can configure this template in **Retrospectives → Document Templates.**
</Info>

### Quick Start

* Type naturally to add text
* Press **Enter** to create new nodes in the document
* Type `/` to open the slash command menu
* Select text and use the toolbar for formatting
* Drag and reposition nodes of content in your document
* All changes save automatically

***

## Rich Text Formatting

The editor supports standard rich text formatting through the toolbar, keyboard shortcuts, and slash commands.

### Text Formatting

| Format            | Keyboard Shortcut      |
| :---------------- | :--------------------- |
| **Bold**          | `Cmd/Ctrl + B`         |
| *Italic*          | `Cmd/Ctrl + I`         |
| ~~Strikethrough~~ | `Cmd/Ctrl + Shift + X` |
| `Inline Code`     | `Cmd/Ctrl + E`         |

### Headings

| Level     | Keyboard Shortcut | **Slash Command** | Description           |
| :-------- | :---------------- | :---------------- | :-------------------- |
| Heading 1 | `#`               | `/h1`             | Main section headers  |
| Heading 2 | `##`              | `/h2`             | Subsection headers    |
| Heading 3 | `###`             | `/h`3             | Minor section headers |

### Lists

| Type          | Keyboard Shortcut | Description                       |
| :------------ | :---------------- | :-------------------------------- |
| Bullet List   | `-`               | Unordered list with bullet points |
| Numbered List | `1.`              | Ordered list with numbers         |

### Other Blocks

| Block      | Slash Command | Description                              |
| :--------- | :------------ | :--------------------------------------- |
| Blockquote | `/blockquote` | Indented quote block for callouts        |
| Code Block | `/codeblock`  | Multi-line code with syntax highlighting |
| Table      | `/table`      | Insert a 3x3 table (expandable)          |
| Image      | `/image`      | Upload and insert an image               |

## Slash Commands

Slash commands provide quick access to all editor features. Type `/` anywhere in the editor to open the command menu.

### Incident Data Blocks

With incident data blocks, you can insert dynamic content that pulls data from the incident.

| Command             | Description                                                                                       |
| ------------------- | ------------------------------------------------------------------------------------------------- |
| `/timeline`         | Insert the incident timeline block                                                                |
| `/followups`        | Insert the follow-ups (action items) block                                                        |
| `/liquid-variables` | Insert a single liquid variable into the document                                                 |
| `/liquid-block`     | Insert a code block that render outputs from more complex liquid syntax or conditional variables. |

#### Basic Blocks

Basic blocks insert standard document elements.

| Command        | Description          |
| -------------- | -------------------- |
| `/text`        | Insert a paragraph   |
| `/h1`          | Insert Heading 1     |
| `/h2`          | Insert Heading 2     |
| `/h3`          | Insert Heading 3     |
| `/bulletList`  | Insert bullet list   |
| `/orderedList` | Insert numbered list |
| `/blockquote`  | Insert blockquote    |
| `/code`        | Toggle inline code   |
| `/codeBlock`   | Insert code block    |
| `/table`       | Insert 3x3 table     |
| `/bold`        | Toggle bold          |
| `/italic`      | Toggle italic        |
| `/strike`      | Toggle strikethrough |

<Info>
  The slash command menu filters as you type. For example, typing /time will show the timeline command at the top.
</Info>

***

## Incident Data Blocks

Incident Data Blocks are dynamic elements that pull live data from the incident. They update automatically when the underlying data changes.

### Timeline Block

The Timeline block displays all events from the incident timeline, including user actions, system events, and status changes.

#### **To insert a Timeline block:**

1. Type `/timeline` in the editor
2. Press **Enter** or click the command

#### **Timeline block features:**

* Shows event date/time, source, user, and description
* Pagination controls help keep the document compact
* Drag the block to reposition it in the document
* Click the node to select the entire block, then use backspace to delete

<Info>
  The Timeline block pulls live data from the incident. If new events are added to the timeline, the block updates automatically.
</Info>

### Follow-ups Block

The Follow-ups block displays action items associated with the incident.

#### **To insert a Follow-ups block:**

1. Type `/followups` in the editor
2. Press **Enter** or click the command

#### **Follow-ups block features:**

* Shows action item title, priority, status, assignee, and due date
* Sort options: **Due Date**, **Priority**, or **Status**
* Drag the block to reposition it in the document
* Click the node to select the entire block, then use backspace to delete

<Info>
  When follow-ups are added or updated on the incident, the block reflects those changes automatically.
</Info>

## How Data Blocks Render on Export

When you publish or export the retrospective to an external provider, data blocks are rendered as static content at the time of export. This includes:

* Timeline events formatted as a table
* Follow-ups formatted as a list with metadata
* Liquid variables or blocks resolved to their actual values

***

## Using Templates

Templates provide pre-built content structures that ensure consistency across retrospectives.

### Inserting a Template

<Steps>
  <Step title="Open the slash command menu">
    Type `/` in the editor.
  </Step>

  <Step title="Select Template">
    Click **Template** from the dropdown
  </Step>

  <Step title="Choose a template">
    Browse your team's available templates and click to insert.
  </Step>

  <Step title="Customize the content">
    The template content is inserted at your cursor position. Edit as needed.
  </Step>
</Steps>

### What Templates Can Include

* Headings and sections (Summary, Root Cause, Timeline, etc.)
* Placeholder text to guide authors
* Liquid variables (e.g., `{{ incident.title }}`)
* Data blocks (`/timeline`, `/followups`)
* Formatting and structure

<Info>
  Templates are configured by administrators in **Settings → Retrospective Templates**. Contact your admin to create or modify templates.
</Info>

***

## Liquid Variables

Liquid variables are dynamic placeholders that resolve to actual values from the incident.

### Inserting Liquid Variables

1. Type `{{` to start a liquid variable
2. Continue typing to filter available variables
3. Select from the autocomplete dropdown
4. The variable appears as a chip in the editor

#### Common Variables

| Variable                        | Description               |
| ------------------------------- | ------------------------- |
| `{{ incident.title }}`          | Incident title            |
| `{{ incident.severity }}`       | Severity level            |
| `{{ incident.status }}`         | Current status            |
| `{{ incident.started_at }}`     | Start timestamp           |
| `{{ incident.resolved_at }}`    | Resolution timestamp      |
| `{{ incident.duration }}`       | Total incident duration   |
| `{{ incident.commander.name }}` | Incident commander's name |
| `{{ incident.slack_channel }}`  | Slack channel name        |
| `{{ post_mortem.title }}`       | Retrospective title       |

<Info>
  Liquid variables display as visual chips in the editor. On publish or export, they resolve to their actual values.
</Info>

## Liquid Blocks

Liquid Blocks are standalone template blocks that support the full Liquid templating language, including conditionals, loops, and complex logic.

### Liquid Block vs Liquid Variable

| Feature       | Liquid Variable          | Liquid Block                                  |
| ------------- | ------------------------ | --------------------------------------------- |
| **Scope**     | Inline (within text)     | Block-level (standalone)                      |
| **Syntax**    | `{{ variable }}` only    | Full Liquid: `{% if %}`, `{% for %}`, filters |
| **Rendering** | Inline chip              | Edit/Preview panel with live rendering        |
| **Best for**  | Inserting dynamic values | Conditional content, loops, complex logic     |

<Info>
  Use **Liquid Variables** for simple value substitution inline within your text. Use **Liquid Blocks** when you need conditionals, loops, or multi-line template logic.
</Info>

### Inserting a Liquid Block

1. Type `/liquid` to open the slash command menu
2. Select **Liquid Block** from the options
3. Write your Liquid template in the editor panel
4. Click **Preview** to see the rendered output with real incident data
5. Toggle back to **Edit** to make changes

#### Example Use Cases

**Conditional severity messaging:**

```
{% if incident.severity == "critical" %}
  🚨 CRITICAL INCIDENT - Immediate escalation required
{% elsif incident.severity == "high" %}
  ⚠️ High priority incident - Review within 1 hour
{% else %}
  📋 Standard incident - Follow normal procedures
{% endif %}
```

Loop through action items:

```
{% for item in incident.action_items %}
  - [{{ item.status }}] {{ item.summary }} (Owner: {{ item.owner.name }})
{% endfor %}
```

**Conditional content with filters:**

```
{% if incident.resolved_at %}
  Resolved on {{ incident.resolved_at | date: "%B %d, %Y at %I:%M %p" }}
  Duration: {{ incident.duration }}
{% else %}
  ⏳ Incident is still ongoing
{% endif %}
```

<Tip>
  Click **Preview** at any time to see how your template renders with actual incident data. Syntax errors will be displayed with helpful error messages.  When to Use Each
</Tip>

Use Liquid Variables when:

Inserting a single dynamic value into a sentence You need a simple inline placeholder Example: "The incident commander is `{{ incident.commander.name }}`"

Use Liquid Blocks when:

You need conditional logic (`{% if %}...{% endif %}`) You need to loop over collections (`{% for %}...{% endfor %}`) You have multi-line template content You need complex formatting with multiple variables Example: Showing different content based on incident severity

## Collaboration

Multiple users can edit the retrospective simultaneously.

### What You'll See

* **Presence indicators:** Avatars/initials of users currently viewing the document
* **Collaborative cursors:** Coloured cursors showing where each user is working
* **Real-time updates:** Changes from other users appear instantly

### Comments

Select text and click the **comment** button to start a discussion:

1. Select the text you want to comment on
2. Click the **comment** button in the toolbar
3. Type your comment and submit
4. Others can reply, creating a threaded conversation
5. Mark comments as **resolved** when addressed

<Info>
  Comments are visible to all collaborators and sync in real-time. Use them for async review and feedback.
</Info>

***

### Best Practices

* **Use slash commands for speed:** Typing `/` is faster than reaching for the toolbar, especially for common actions.
* **Insert data blocks instead of copying:** Timeline and Follow-ups blocks stay in sync with the incident. Manual copy-paste becomes stale.
* **Use templates for consistency:** Starting from a template ensures all retrospectives follow the same structure.
* **Add comments for review feedback:** Instead of sending feedback in Slack, add comments directly in the document for better context.
* **Use headings to structure content:** Clear section headers (Summary, Timeline, Root Cause, Action Items) make retrospectives easier to scan.

***

### Troubleshooting

<AccordionGroup>
  <Accordion title="The slash command menu doesn't appear when I type /">
    Make sure your cursor is in an editable area of the document, not inside a data block or at an invalid position. Try clicking in a paragraph and typing `/` again.
  </Accordion>

  <Accordion title="A data block shows 'Loading...' indefinitely">
    This usually means the block couldn't fetch data from the incident. Check your network connection and refresh the page. If the problem persists, the incident may not have any data for that block type (e.g., no timeline events or follow-ups).
  </Accordion>

  <Accordion title="Template insertion failed">
    Ensure you have permission to access retrospective templates. If templates aren't appearing, contact your administrator to verify templates are configured for your team.
  </Accordion>

  <Accordion title="I accidentally deleted content. Can I undo?">
    Use `Cmd/Ctrl + Z` to undo recent changes. You can also access version history to restore a previous version of the retrospective.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).