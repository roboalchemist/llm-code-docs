# Source: https://docs.datadoghq.com/coscreen.md

---
title: CoScreen
description: >-
  Use CoScreen for collaborative meeting and screen sharing. CoScreen is
  designed for engineering use cases like pair programming and incident
  management.
breadcrumbs: Docs > CoScreen
---

# CoScreen

{% video
   url="https://datadog-docs.imgix.net/images/coscreen/collab-v2.mp4" /%}

## Overview{% #overview %}

[CoScreen](https://coscreen.co/) is a collaborative meeting tool that allows multiple participants to simultaneously share and interact with any application window on their desktops. It is specifically designed for engineering use casesâsuch as pair programming, incident management, joint troubleshooting, team standups, and employee onboarding.

## Setup{% #setup %}

#### Requirements{% #requirements %}

{% tab title="Desktop" %}
The CoScreen desktop app is available for Windows 10 and macOS v10.15 Catalina and higher.

[Download CoScreen](https://www.coscreen.co/download).

After installing CoScreen, launch the desktop app. You can sign in with your Datadog account.
{% /tab %}

{% tab title="Web" %}
The [CoScreen web app](https://app.coscreen.co/) is supported in Chrome v87+, Edge v87+, and Safari v16+.

The CoScreen web app has limited functionality. To make full use of CoScreen's features, use the desktop app.
{% /tab %}

## Usage{% #usage %}

### Join a CoScreen{% #join-a-coscreen %}

If you were invited to a CoScreen, click on the link. You can click on **Join from browser** to join the CoScreen through the web app, or you can launch the desktop app. You can also join manually by entering your meeting link or ID.

When you join a CoScreen, it is added to your list of *Recent CoScreens* in the main menu. You can rejoin these at any time.

To enable noise reduction in the desktop app, go to **Settings** > **Audio** and select *Apply noise reduction to my microphone*.

On macOS, you can enable background blurring under **Settings** > **Camera** > **Video Effects**.

### Invite your collaborators{% #invite-your-collaborators %}

Invite collaborators by sharing the link.

You can also add your closest collaborators to the list of *Your Collaborators* in the main menu. After a collaborator accepts your request, you can see if they are online and available and call them with a click.

### Share windows{% #share-windows %}

With the CoScreen desktop app, you can share application windows in multiple ways.

#### Select individual windows to be shared{% #select-individual-windows-to-be-shared %}

{% video
   url="https://datadog-docs.imgix.net/images/coscreen/sharewindow2.mp4" /%}

Once you have joined a CoScreen, you can hover over any window in any of your displays, and a **Share** tab appears. Share and unshare windows by clicking on this tab. You can also use the window sharing dialog to select the application window(s) that you want to share with other members of the CoScreen you've joined.

Multiple users can share multiple windows at the same time. Shared windows have a border around them, in a different color assigned to each CoScreen participant.

#### Use the window sharing dialog to share entire displays or individual windows{% #use-the-window-sharing-dialog-to-share-entire-displays-or-individual-windows %}

Click on the **Share windows** button to open the window sharing dialog.

{% image
   source="https://datadog-docs.imgix.net/images/coscreen/share_windows_button.376a551f29459706f4ae714195e97d35.png?auto=format"
   alt="A panel of buttons from the CoScreen desktop UI. The 'Share windows' button is highlighted." /%}

If you have multiple displays, you can select a display and click **Share the entire display** to share all open windows on that display. While screen sharing is enabled, all windows that you open or drag onto your shared display are also shared.

You can also select any number of windows on any of your displays to share.

Screen sharing is deactivated by default when you join a CoScreen.

### Collaborate in shared windows{% #collaborate-in-shared-windows %}

{% video
   url="https://datadog-docs.imgix.net/images/coscreen/v5-control-tabs.mp4" /%}

You can see the mouse pointers of remote participants whenever they move their pointers over a shared window. When viewing a remote window, two tabs appear: **Control**, which enables you to interact with the window, click on buttons, and type into text fields; and **Draw**, which enables you to draw on the window.

### Collaborate in a shared terminal{% #collaborate-in-a-shared-terminal %}

CoScreen includes a shared, collaborative terminal that enables users to run commands and to write and debug code together.

To start a shared terminal, click on the **Share terminal** button in the meeting menu:

{% image
   source="https://datadog-docs.imgix.net/images/coscreen/share_terminal.15c3092140a251d450b02ab69ba41729.png?auto=format"
   alt="A panel of buttons from the CoScreen desktop UI. The 'Share terminal' button is highlighted." /%}

The shared terminal appears for you and all other participants in the CoScreen session. If you enable remote control in CoScreen, other users can type and click into your terminal.

{% image
   source="https://datadog-docs.imgix.net/images/coscreen/coterm.ab4c896c7fa405c889431204dce358f0.png?auto=format"
   alt="A shared CoScreen terminal window." /%}

To stop sharing, click the **Unshare** tab on the terminal window, or on the button in the meeting menu.

For privacy, CoScreen uses [Sensitive Data Scanner](https://docs.datadoghq.com/security/sensitive_data_scanner/) and entropy filters to detect and obfuscate sensitive data.

### Integrations{% #integrations %}

You can integrate CoScreen with Slack, Google Calendar, VS Code, and other apps. [See all CoScreen integrations.](https://www.coscreen.co/integrations)

#### CoScreen + Slack{% #coscreen--slack %}

To install the CoScreen Slack app, go to [coscreen.co/slack](https://coscreen.co/slack) and click on *Add to Slack*. To enable CoScreen in private channels, type `@coscreen` and hit enter/return, then click on *Invite to Channel*. To enable CoScreen in multi-user DMs, go to *View Member List* -> *Add People* -> *CoScreen*.

#### CoScreen + Google Calendar{% #coscreen--google-calendar %}

To configure this integration, install the [CoScreen Chrome extension](https://chrome.google.com/webstore/detail/coscreen/pahmjnapohdeedmdhmbeddgmhebhegme) and sign in. Open any Google Calendar event and use the **Add CoScreen** button to make the event a CoScreen meeting.

#### CoScreen + Datadog Incident Management{% #coscreen--datadog-incident-management %}

In [Incident Management](https://docs.datadoghq.com/incident_response/incident_management/), use the **Meet on CoScreen** button to start a CoScreen meeting with incident responders. To configure this, go to your [Incident Management Integration Settings](https://app.datadoghq.com/incidents/settings#Integrations) page and toggle on **Enable click-to-join CoScreen meeting buttons**.

## Security and privacy{% #security-and-privacy %}

- **Network security**

CoScreen uses a P2P (peer-to-peer) connection whenever you and another participant can connect directly (for example, when there are no corporate firewalls or proxies between you). None of your audio, video, window, or control input feeds touch CoScreen's servers. Connections are end-to-end encrypted using DTLS-SRTP. If there are three or more users in a session, the connection is over a video bridge.

- **Video infrastructure**

Participants collaborate using an enterprise-grade, HIPAA-compatible video infrastructure with hundreds of servers that run the Jitsi framework. All video data is encrypted using DTLS-SRTP during transmission.

- **Data storage**

CoScreen does not record or store any shared information (for example, shared windows, audio, video or remote control input).

CoScreen captures general usage data, like used app features and session statistics, to learn about bugs and usage patterns. CoScreen never records or accesses shared windows or control input apart from enabling you to exchange window content and controls with your peers. See [CoScreen's Privacy Policy](https://www.datadoghq.com/legal/privacy/) for more details.

For all the details on how CoScreen enables secure collaboration, read the [CoScreen Security Whitepaper](https://www.coscreen.co/security).

## Further reading{% #further-reading %}

- [Leverage collaborative screen sharing with Datadog CoScreen](https://www.datadoghq.com/blog/collaborative-screen-sharing-with-datadog-coscreen/)
