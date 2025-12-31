# Source: https://docs.warp.dev/knowledge-and-collaboration/session-sharing.md

# Session Sharing

{% hint style="warning" %}
This action sends command information to Warp’s servers and is explicitly opt-in. Read more about privacy for cloud features in the [privacy overview](https://www.warp.dev/privacy/overview).
{% endhint %}

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-49346a9f4cbf5ef87cdada308b4f7708d41fc938%2Fsession_sharing_preview.png?alt=media" alt=""><figcaption><p>Session Sharing allows multiple teammates to edit the input at the same time</p></figcaption></figure>

### Share a session

To start sharing:

1. From the [Command Palette](https://docs.warp.dev/terminal/command-palette), search for and select "Share New Session" or "Share Current Session".
2. From the Pane header overflow menu, select "Start Session sharing"
3. From the `RIGHT-CLICK` context menu, select "Share session..."

#### How to control a starting point for sharing

If you select to share a current session, you will be given the option to share without scrollback or from the start of the session. When you share access from the start of a session (with scrollback), collaborators will be able to view and interact with your entire session history including command outputs from before sharing was initiated.

If you initiate a shared session using Block actions, you will be given the option to start sharing from the selected block onwards. This option gives you the precision to select a specific block of output in your session history as the starting point, excluding all previous scrollback before that block.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-9eff70e46ce75eaed56052c14b2b54226d0e1b61%2FScreenshot%202024-04-24%20at%203.09.05%E2%80%AFPM.png?alt=media&#x26;token=01fb0d6e-4e6f-4aae-8f55-0c927099df62" alt=""><figcaption><p>Start sharing from a selected block onward or an entire session with or without scrollback</p></figcaption></figure>

#### How to allow access to collaborators in your session

After starting a shared session, Warp will copy a link to your clipboard that you can share. Share links open the Warp's native app or the Web.

{% hint style="warning" %}
By default the links are restricted to only emails that have access. It’s critical you only share your session links in private channels with known teammates and approved collaborators. Do not include your session-sharing links in any public forums.
{% endhint %}

You can adjust who has view or edit access to your session and specifically:

* Add emails to grant access
* Allow anyone with the link
* Allow anyone on your team
* Revoke edit access from collaborators
* Remove collaborators from the session

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-cbc2de4884896428461d94ea4930edf5e4e45345%2Fsession-who-has-access.png?alt=media&#x26;token=0d9b3c31-679a-48cc-a932-ab3d43ec8153" alt=""><figcaption><p>Update permissions through the share icon</p></figcaption></figure>

When somebody accesses your shared session, they will be able to:

* View your session in Warp including your command line input and output
* Highlight blocks and text in your session
* Request control to edit and enter commands in the sharer’s session

If granted access, collaborators can edit the input together in real-time and execute commands.

You can also:

* Reference avatars and usernames for every collaborator who has access to your session
* Jump to a collaborator’s selection by clicking on their avatar

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-8bd8c322de21dbc965dc969d693a9b2469c681c9%2Fsession-sharing-native-web-demo.gif?alt=media&#x26;token=527a1780-2914-4636-8a3a-d06658827f42" alt=""><figcaption><p>Session Sharing Native to Web Demo</p></figcaption></figure>

#### How to end a shared session

When you’re ready to end a shared session, click `Share > Stop` sharing to wrap up and close access for all collaborators.

#### Multiple shared sessions

You may share multiple sessions simultaneously. If you have multiple shared sessions, you will find *Other shared sessions* listed in the Share dropdown menu. You may also end multiple shared sessions at the same time with `Share > Stop` sharing all.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-72dc9022fb52487a8704ea93fd558b45ce9c1c57%2Fswitch-stop-session-sharing.png?alt=media&#x26;token=b7f3192b-b29e-40e9-ae60-1007eef1089f" alt=""><figcaption><p>Switch between shared sessions or stop all shared sessions at once</p></figcaption></figure>

### Known limitations

* Even if enabled, [Secret Redaction](https://docs.warp.dev/privacy/secret-redaction) is not applied during session sharing.
* There is a session size limit of 100MB per session, 1GB per user per day, and a maximum of 10 participants per session (excluding the sharer). These limits are subject to change.
* Some of Warp's plans are limited to 5 shared sessions and the session limits do not reset. Upgrade to a [paid plan](https://www.warp.dev/pricing) to get unlimited sessions.

{% hint style="info" %}
If you have any questions, please email <feedback+ss@warp.dev>.
{% endhint %}
