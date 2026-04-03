# Invite Sources

**Orpheus Development Papers #5 - Invite Sources**
Version 1 | From: Spine | Date: 2021-06-19

## Overview

This feature helps keep track of how people were invited via interviews
and recruitments from other trackers. Most people who buy invites from the
Bonus Shop for personal friends are not concerned by this. But for people
who interview or recruit, it is helpful to keep the source origins distinguished,
as it is for staff.

## Configuration Steps

### Step 1: Configure Permissions

Grant `admin_manage_invite_source` to moderators and above. This will allow these
people to configure invite sources. It can also be done on a per-user basis
via custom permissions.

Run the seeder:

```bash
phinx seed:run -s InviteSource
```

Then navigate to `/tools.php?action=permission`.

### Step 2: Add Invite Sources

Add the invite sources: mnemonic names of trackers that everyone
understands. Consider adding an Interview source as well if you do
interviews, for interviewers and personal invites. These are stored in the
`invite_source` table.

Navigate to `/tools.php?action=invite_source_config`.

Once added and referred to (by a member who has been granted its use, a
member who has been sourced from it), a source may no longer be removed.
You will need to tidy up the database directly.

### Step 3: Grant Sources to Members

Search for users who have the R or IN secondary classes. On their profile page,
a new "Invite Sources" section will appear. Check the sources that are
appropriate for this user. These grants are stored in the `inviter_has_invite_source`
table.

Navigate to `/tools.php?action=invite_source`.

### Step 4: Inform Members

When they invite people, they will see an additional select box showing the
options that have been configured for them. They can then set the source when
the invitation is issued. The source is tied to the invite key via the
`invite_source_pending` table, so that when the invitee creates their account,
the source is attached to their profile (in the `user_has_invite_source` table).

They can also go to the list of their invitees and backfill the existing
invitees.

Navigate to `/user.php?action=invite&edit=source`.

### Step 5: View on Profile

On the profile page, the "Invite:" information will now say "by `<user>`
from `<source>`".

### Step 6: Removing Sources

If a source is removed from a recruiter, all their invitees that were
tagged as coming from that source will remain.
