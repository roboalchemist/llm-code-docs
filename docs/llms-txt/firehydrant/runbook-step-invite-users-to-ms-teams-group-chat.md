# Source: https://docs.firehydrant.com/docs/runbook-step-invite-users-to-ms-teams-group-chat.md

# Invite Users to MS Teams Group Chat

<Image align="center" width="650px" src="https://files.readme.io/bcd9de777e8aa95bb0e55fe47871db8fda3ad6fc91bda5cf853d5e51d9c4ef60-CleanShot_2025-01-15_at_15.42.57.png" />

This Runbook step allows inviting users directly to an incident Group Chat in Microsoft Teams using emails.

## Prerequisites

* This Runbook step should be used in conjunction with [Create Microsoft Teams Group Chat](https://docs.firehydrant.com/docs/create-microsoft-teams-group-chat).

## Configuration

1. Navigate to any Runbook and click "Add step."
2. Search for this step or look for it under Microsoft Teams dropdown and click on it
3. Modify the Runbook step name as desired and then add users in a comma-delimited list under **Users**.

Once executed, this step will attempt to invite those users via the specified emails to the group chat.