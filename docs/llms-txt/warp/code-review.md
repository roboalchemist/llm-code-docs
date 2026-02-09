# Source: https://docs.warp.dev/code/code-review.md

# Code Review

## Overview

When you are working locally in a Git repository with uncommitted changes, the **Code Review panel** lets you inspect, edit, and manage code changes directly inside Warp. It integrates with Git and Warp's Agents, giving you the ability to:

* Review diffs and attach them as context for the Agent
* Apply, edit, or revert changes in real time
* See changes made outside of Warp or by Warp's Agents automatically reflected

Any uncommitted changes appear in the panel (or compare the changes on your branch against `main` or `master` ). Switching branches or saving files updates the panel instantly, so it always reflects the current state of your codebase.

{% embed url="<https://www.loom.com/share/96581523168742eb9b95c3973924728c?sid=a3ee9164-4274-4468-ac32-38ce6807f9a8>" %}
Code Review Demo
{% endembed %}

<figure><img src="https://4009768362-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FPsjNxoJ0NFCXW6rRdHH3%2Fuploads%2Fgit-blob-380b08f2356cdb3390646691e30c929cba0d0025%2Fcode-review-panel-update.png?alt=media" alt=""><figcaption><p>Full view of Code Review panel and terminal pane.</p></figcaption></figure>

{% hint style="info" %}
To review agent-generated diffs, leave inline comments, batch your feedback, and have the agent apply all requested changes, see [Interactive Code Review](https://docs.warp.dev/code/code-review/interactive-code-review).
{% endhint %}

## Opening the Code Review panel

The Code Review panel can be opened in several ways. Each entry point makes it easy to inspect and manage changes without leaving your workflow.

{% hint style="success" %}
You can also open the Code Review panel with `CMD – SHIFT – +` on macOS or `CTRL – SHIFT – +` on Windows and Linux.
{% endhint %}

#### 1. Universal Input: Git diff chip

In the [Universal Input](https://docs.warp.dev/terminal/universal-input) editor, when you're in a Git repository with changes, the chip shows the number of files modified along with lines added and removed. Clicking the chip opens the Code Review panel with the relevant diffs.

<figure><img src="https://4009768362-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FPsjNxoJ0NFCXW6rRdHH3%2Fuploads%2Fgit-blob-7c440f8e587ca77a4b3dbd040902306cecf80a77%2Fwhole%20UDI%20bar.png?alt=media" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4009768362-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FPsjNxoJ0NFCXW6rRdHH3%2Fuploads%2Fgit-blob-cf1d23a5793eb9d59594623b9d682f41fdf74ca1%2Fgit%20chip%20tooltip%201.png?alt=media" alt=""><figcaption></figcaption></figure>

#### 2. Agent Conversation: Review Changes Button

When an Agent makes code edits in an [Agent Conversation](https://docs.warp.dev/agent-platform/agent/using-agents/agent-conversations), a `Review changes` button appears at the bottom of the conversation. Clicking it opens the code review panel.

<figure><img src="https://4009768362-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FPsjNxoJ0NFCXW6rRdHH3%2Fuploads%2Fgit-blob-62fa47f13942e16b39a009c7ac4ed14d3147536d%2FBlocklist%20with%20review%20changes.png?alt=media" alt=""><figcaption><p>Review changes at bottom of Agent Conversation.</p></figcaption></figure>

<figure><img src="https://4009768362-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FPsjNxoJ0NFCXW6rRdHH3%2Fuploads%2Fgit-blob-593ea47a3a2df70aef6409d3cb350be43fcc003c%2Freview%20changes%20in%20footer.png?alt=media" alt=""><figcaption></figcaption></figure>

#### 3. Agent Conversation: Toolbelt (Bottom Right)

During an Agent conversation, you can view all changed files in the toolbelt chips at the persistent bottom right. From there, you can open the Code Review panel directly.

<figure><img src="https://4009768362-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FPsjNxoJ0NFCXW6rRdHH3%2Fuploads%2Fgit-blob-9026ae0da1e5f81fb45160a4dcebf0b81090ad4c%2Fai_control_panel_buttons_larger_view.png?alt=media" alt=""><figcaption></figcaption></figure>

#### 4. Warp Tab Bar

In any Git-tracked repository, you can open the Code Review panel by clicking the plus/minus icon in the top-right corner of Warp, next to your avatar.

<figure><img src="https://4009768362-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FPsjNxoJ0NFCXW6rRdHH3%2Fuploads%2Fgit-blob-11a3ccd59f79cced7f18a9ef03c583efa39594e2%2Fwarp-tab-bar-review-code.png?alt=media" alt=""><figcaption></figcaption></figure>

#### Viewing All Edited Files

Inside the Code Review panel, you can open the file sidebar to browse all changed files in your repository. Clicking on a file will automatically scroll to that file in the panel.

<figure><img src="https://4009768362-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FPsjNxoJ0NFCXW6rRdHH3%2Fuploads%2Fgit-blob-6b0cfb0199c6310f6c6bbc3f7ef5c5567e663375%2Fwhole%20git%20diff%20view%20with%20one%20file%20collapsed.png?alt=media" alt=""><figcaption><p>Viewing all edited files in the code review panel, with the file sidebar open.</p></figcaption></figure>

{% hint style="info" %}
By default, the Code Review panel opens as a pane on the right, but you can drag it to reposition wherever you prefer.
{% endhint %}

## Reviewing diffs

By default, the Code Review panel shows all **uncommitted changes** on your current branch, excluding changes to files ignored by `.gitignore`.

Warp offers two ways to review changes:

1. **Uncommitted changes**: view all edits you've made locally on the current branch.
2. **Changes vs. main**: compare your branch against `main` or `master` to see what would be included in a pull request to that branch, for instance.
   1. Warp automatically detects the target branch and updates the comparison accordingly.
3. **Changes vs. another branch**: compare your work against any arbitrary branch for stacked PRs, feature comparisons, or alternate base branches.

You can manually switch between the two views either in the Code Review panel or via the universal input chip:

<figure><img src="https://4009768362-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FPsjNxoJ0NFCXW6rRdHH3%2Fuploads%2Fgit-blob-067d344b4753797939eb64d41ec32927fb7477af%2Fdiff%20dropdown%20to%20change%20base%20from%20the%20code%20review%20pane.png?alt=media" alt=""><figcaption><p>Changing diff view in the Code Review Panel.</p></figcaption></figure>

<figure><img src="https://4009768362-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FPsjNxoJ0NFCXW6rRdHH3%2Fuploads%2Fgit-blob-1e4414371c81d16b3ea0fe67ce8aea1bef8f6a2e%2Fgit%20diff%20change%20base%20dropdown.png?alt=media" alt=""><figcaption><p>Changing diff view in the Universal input.</p></figcaption></figure>

<div data-full-width="false"><figure><img src="https://4009768362-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FPsjNxoJ0NFCXW6rRdHH3%2Fuploads%2Fgit-blob-c0aacdd7d981e5adaa4bc8ce65f63e70fe7190ff%2Farbitrary-branch-diff.png?alt=media" alt="" width="298"><figcaption><p>Changing diff view against an arbitrary branch.</p></figcaption></figure></div>

Any saved edits made outside of Warp (e.g. in another editor), as well as changes applied by Warp's Agents, appear automatically. The panel updates in real time, ensuring it always reflects the current state of your working file and directory.

#### Attaching diffs as context

The Code Review pane makes it simple to share changes with the Agent. You can attach an entire diff to a prompt so the Agent has full visibility into what was added or removed.

<figure><img src="https://4009768362-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FPsjNxoJ0NFCXW6rRdHH3%2Fuploads%2Fgit-blob-d7bca69edda163d79e0a4954554049ce55fd2c0e%2Fattach-diff-hunk-as-context.png?alt=media" alt="" width="299"><figcaption><p>Attaching a diff as context from the Code Review panel.</p></figcaption></figure>

This ensures responses are grounded in your latest edits, whether you're asking for feedback, explanations, or follow-up changes. For more details, see [Selection as Context](https://docs.warp.dev/agent-platform/agent/using-agents/agent-context/selection-as-context).

#### Reverting diffs

The Code Review panel lets you easily undo changes at different levels. In the gutter next to each diff, you’ll see an option to revert a hunk: roll back a specific set of changes (a “diff hunk”) within a file. This removes the added or modified lines and restores the previous version.

<figure><img src="https://4009768362-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FPsjNxoJ0NFCXW6rRdHH3%2Fuploads%2Fgit-blob-f53f6912cf72da635fec9fc6ff5dd9bafbfc66c2%2Frevert%20diff%20hunk.png?alt=media" alt=""><figcaption></figcaption></figure>

When you revert, the changes are immediately updated in your working directory. The file is restored to match the selected version, so you can continue editing or commit without the reverted code.

### Opening Files from Code Review

In addition to reviewing and editing diffs directly in the Code Review pane, you can open a file directly in Warp's [Code Editor](https://docs.warp.dev/code/code-editor). Each file listed in the Code Review pane includes an expand button in the top-right corner of its diff view.

<figure><img src="https://4009768362-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FPsjNxoJ0NFCXW6rRdHH3%2Fuploads%2Fgit-blob-07c81eaffe1eedb328e4f21d39ebdf613a5b95b6%2Fcode-review-header.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>

* Clicking the **expand button** (right-most button on the header) opens the file in a new editor tab, allowing you to see the full file beyond just the changed lines.
  * This is useful when you need additional context around a diff, want to make broader edits, or prefer working in the full editor rather than inline.
* Once opened, the file behaves like any other editor tab: you can scroll, edit, search, and save.
* Any changes made in the editor automatically sync back into the Code Review pane, so the diff view always stays current.

**Note**: from this code review file header, you can also attach a file diff as context into Warp's agent, or discard all the changes on a single file.

#### Directly editing code diffs

Alternatively, from the Code Review panel, you are able to click and edit the diffs directly:

<figure><img src="https://4009768362-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FPsjNxoJ0NFCXW6rRdHH3%2Fuploads%2Fgit-blob-fa033b4ef71089a7b7682bed39f04fdbd9b15898%2Fdirectly-editing-diffs.gif?alt=media" alt=""><figcaption></figcaption></figure>

#### Discarding all changes

The Code Review panel also lets you discard every uncommitted change on your branch in one action. Clicking Discard all removes all local modifications shown in the panel and restores each file to its state on the base branch. This is useful when you want to reset your working directory, abandon a set of edits, or start a new iteration from a clean slate.

<figure><img src="https://4009768362-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FPsjNxoJ0NFCXW6rRdHH3%2Fuploads%2Fgit-blob-ee4807923d6ff3bf13139f1d787c8288ed1d446b%2Fdiscard-all-changes.png?alt=media" alt="" width="348"><figcaption></figcaption></figure>

Discarding changes will ask you confirm, but still make sure you’ve saved or backed up anything you want to keep before using it.
