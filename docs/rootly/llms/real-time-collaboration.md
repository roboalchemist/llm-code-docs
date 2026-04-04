# Source: https://docs.rootly.com/collaborative-retrospectives/real-time-collaboration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Real-Time Collaboration

> Work together on retrospectives with real-time editing, collaborative cursors, presence indicators, and inline comments.

## How Real-Time Collaboration Works

The retrospective editor supports simultaneous editing by multiple team members. Changes sync instantly across all connected users, eliminating version conflicts and enabling true collaborative writing.

Collaboration features include:

* **Real-time editing:** See changes as others make them
* **Collaborative cursors:** See where each person is working
* **Usage analytics:** Know who recently viewed or edited the document
* **Inline comments:** Discuss specific sections without leaving the editor
* **Version history:** See how your document evolved based on edits made by your team

<Info>
  Real-time collaboration uses conflict-free replicated data types (CRDTs) to merge changes automatically. No manual conflict resolution is required.
</Info>

***

## Collaborative Editing

When multiple users open the same retrospective, all changes sync automatically in real-time.

### What You'll Experience

* **Instant updates** — Text typed by others appears immediately
* **No conflicts** — Edits from all users merge seamlessly
* **Shared state** — Everyone sees the same document at all times

<Info>
  Even if two users edit the same paragraph simultaneously, changes merge correctly without overwriting each other's work.
</Info>

### Presence Indicators

Shows who's viewing or editing the retrospective with user avatars, colored indicators, and real-time updates.

### Collaborative Cursors

See exactly where other users are working in the document with real-time feedback for typing, text selection and navigation.

## Comments

Add inline comments to discuss specific parts of the retrospective with your team.

### Creating a Comment

<Steps>
  <Step title="Select text">
    Highlight the text you want to comment on.
  </Step>

  <Step title="Open comment dialog">
    Click the **comment** button in the toolbar, or use the keyboard shortcut.
  </Step>

  <Step title="Write your comment">
    Type your comment in the dialog that appears.
  </Step>

  <Step title="Submit">
    Press Enter or click Submit to create the comment thread.
  </Step>
</Steps>

### Viewing Comments

Comments appear in three ways:

* **Node indicators:** Comments appear inline, attached to the relevant node in the editor.
* **Highlighted text:** Commented text is highlighted in the document. On narrower screens, click the highlight to view the comment.
* **Comments side panel:** View all open and resolved comment threads via the comments panel triggered from the actions dropdown in the header.

<Info>
  Access resolved threads anytime by clicking **More actions →** **View all comment threads** in the editor controls
</Info>

### Comment Actions

| Action        | Description                                                                   |
| ------------- | ----------------------------------------------------------------------------- |
| **Reply**     | Add a response to an existing thread                                          |
| **Resolve**   | Mark the comment as addressed (hides from active view)                        |
| **Unresolve** | Mark the comment as unaddressed (visible in the All Comments side panel view) |
| **Delete**    | Remove the comment entirely                                                   |
| **Edit**      | Modify your own comment text                                                  |

### Comments Panel

On wider screens, comments display in a dedicated panel alongside the editor.

* **All threads:** See all active comment threads in one place
* **Click to navigate:** Click a thread to jump to that location in the document
* **Reply inline:** Respond to comments directly in the panel
* **Filter options:** View open/resolved comments

#### What Happens When Someone Comments

* The comment appears immediately for all users viewing the document
* The comments panel updates with the new thread
* The commented text becomes highlighted

#### What Happens When Someone Replies

* The reply appears in the thread for all users
* Users viewing the thread see the new reply instantly

<Info>
  Comments are stored with the document and persist across sessions. Team members who open the document later will see all existing comments.
</Info>

***

### Collaboration Best Practices

#### For Effective Teamwork

* **Communicate your focus area** If working with others simultaneously, let them know which section you're editing to avoid stepping on each other's work.
* **Use comments for async feedback** Comments are ideal for review cycles where not everyone is online at the same time.
* **Resolve comments when addressed** Keep the comments panel clean by resolving threads once feedback is incorporated.
* **Check presence before major edits** Glance at who's online before restructuring or deleting large sections.

#### For Comments

* **Be specific** Select the exact text you're commenting on rather than commenting on a general area.
* **Use threads for discussions** Reply to existing comments rather than creating new threads for the same topic.
* **Resolve, don't delete** Resolving preserves the history of feedback; deleting removes it permanently.
* **Tag specific questions** Make it clear if you need a response by phrasing comments as questions.

***

## Visibility and Permissions

### User Permissions

* All users with **edit access** to the incident can collaborate on its retrospective
* Users with **view-only access** can read but not edit or comment
* **Private incidents** restrict access to assigned users

### Comment Visibility

* Comments are visible to all users who can access the retrospective
* There are no private comments. All threads are shared

<Info>
  Collaboration access is determined by incident permissions. Check with your administrator if you need access to a specific incident's retrospective.
</Info>

### Troubleshooting

<AccordionGroup>
  <Accordion title="Presence indicators show someone who left">
    There may be a brief delay (a few seconds) before a user's presence indicator disappears after they close the document. This is normal behavior.
  </Accordion>

  <Accordion title="Can I mention someone in a comment?">
    Currently, comments don't support @mentions, however this functionality is planned for the next release. In the meantime, you can @mention other users in the actual document.
  </Accordion>

  <Accordion title="Why can't I delete someone else's comment?">
    Users can only edit or delete their own comments. To remove someone else's comment, ask them to delete it or contact an administrator.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).