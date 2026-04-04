# Source: https://loops.so/docs/loop-builder/pausing-loops.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Pausing Loops

> Learn how to pause and stop a Loop to control the sending of emails.

## Pausing vs Stopping

Both pausing and stopping a Loop will prevent any emails from sending until you resume the Loop, but there are a few key differences.

<Tip>
  We generally recommend stopping emails based on in-app actions completed (e.g., “user upgraded,” “ticket closed,” “trial converted”) rather than on email replies as a reply (such as an out of office email) doesn't necessarily mean the action you emailed about has been taken.
</Tip>

### Pausing a Loop

When you pause a Loop, you can resume the Loop at any time.

During the pause, all contacts that were scheduled to receive an email will receive it once you resume the Loop. However, this assumes that these contacts still meet the necessary criteria to receive the email (e.g., they are subscribed and match any audience filters or other conditions you've set).

New contacts that match the Trigger conditions while the Loop is paused will enter the Loop but only within the first 24 hours. Contacts that qualify for the Trigger after the 24-hour mark will not enter the Loop.

<Tip>
  We will notify you via email once the 24-hour period has elapsed, reminding
  you that contacts will no longer queue to enter the Loop if you resume it.
</Tip>

The 24-hour limitation prevents contacts from entering a Loop that has been paused for an extended period and receiving irrelevant emails. For instance, if your Loop sends a welcome email to new contacts, you wouldn't want a contact to join the Loop three months after signing up and receive a welcome email.

### Stopping a Loop

Stopping a Loop will not queue any new contacts to enter the Loop. Any contacts that were queued to enter the Loop will not enter the Loop. That's the key difference between pausing and stopping a Loop.
