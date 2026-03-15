# Source: https://docs.jit.io/docs/microsoft-teams-integration.md

# Microsoft Teams Integration

## Overview

Microsoft Teams integration enables you to view security-related notifications in your team's native environment for day-to-day communications. Furthermore, you can assign specific notification types (e.g., whenever a developer ignores a security finding) to different channels in your Teams workspace.

## Steps for integrating with Teams

1. From the [Integrations page](https://docs.jit.io/docs/integrations-page), locate the Teams tile and select **Connect**.
2. You will now be prompted to login with a Microsoft account. The account must have administrator access to the teams and channels you want Jit to interact with.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/51c537312b541960c33bfd53140d58f0bca061a560d71b12ade65525775a39cb-team.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

## Configuring Teams channels

Jit enables you to assign channels in your Teams workspace for specific notification types. Use this option to stay organized and eliminate unnecessary noise.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3fc15f913816765fffbcb038f123a5522c493d26d941f95d44edab1a73edbe17-image_2_copy.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

### Notification types:

* *New high-severity findings*: This channel displays a notification for every high-severity (or greater) finding that is displayed in the Backlog page and was not found in the initial scan.
* *Ignored findings*: This channel displays a notification for each ignored finding.
* *Findings on saved views*: Any new security finding that displays in a custom view defined in the Backlog page displays on this channel. For further information on custom views, visit the Backlog page.
* *New action created*: This channel displays a notification for every Action created in the Actions page.

## Disconnecting from Teams

**To disconnect from Teams—**

1. Navigate to the [Integrations page](https://docs.jit.io/docs/integrations-page), locate the Microsoft Teams tile.
2. Click “Configure” and navigate to the configuration
3. Scroll down and click the “Disconnect” button.