# Source: https://docs.unifygtm.com/reference/sequences/send-schedules/using-send-schedules.md

# Using a Custom Send Schedule

> Learn how to view and apply Custom Send Schedules for Sequences.

Custom Send Schedules define when automated emails in a Sequence are allowed to send. Once you’ve configured your Custom Send Schedule, you can assign them to individual Sequences.

***

## Accessing Sequence Settings

To view or edit the Custom Send Schedule assigned to a Sequence:

1. Open any Sequence from your **Sequences** list.
2. Click the **⚙️ cog icon** in the top-right corner to open **Sequence Settings**.
3. In the settings drawer, you’ll see a section labeled **Send schedule**, displaying the currently linked schedule and its details.

<Frame caption="Viewing the Custom Send Schedule assigned to a Sequence">
  <img src="https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-drawer.png?fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=0c30a36eb5743a13db3f5ec7b4c4c534" data-og-width="3244" width="3244" data-og-height="1596" height="1596" data-path="images/reference/sequences/send-schedules/sequences-settings-drawer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-drawer.png?w=280&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=9e10928567fffe479c95aefd55ce7f08 280w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-drawer.png?w=560&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=741953681084074239e9c61b738b476b 560w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-drawer.png?w=840&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=705aec18869b5660e24f772109b1a94c 840w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-drawer.png?w=1100&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=223dead02da49e3a9b29e21100d2a4ac 1100w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-drawer.png?w=1650&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=58cbb5d6acdbe55c238c57e5c2ca5185 1650w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-drawer.png?w=2500&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=b29217addbc60ddcbb89e0474649d6d7 2500w" />
</Frame>

***

## Selecting a Custom Send Schedule

To change which Custom Send Schedule a Sequence uses:

1. Click **Edit** in the top-right corner of the Sequence Settings drawer.
2. Open the **Send schedule** dropdown.
3. Choose the desired schedule from the list. You’ll see details including:
   * Schedule name
   * Timezone
   * Days enabled for sending
   * Sending windows per day
   * Skip dates

<Frame caption="Selecting a Custom Send Schedule for a Sequence">
  <img src="https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-edit.png?fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=c61f6d584db97b89080526066fc95bdb" data-og-width="2284" width="2284" data-og-height="1612" height="1612" data-path="images/reference/sequences/send-schedules/sequences-settings-edit.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-edit.png?w=280&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=d1e5dd6ef49283994e156f0484190436 280w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-edit.png?w=560&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=b82b702f769a52cbe3765d535a2e63e2 560w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-edit.png?w=840&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=9e56b629e3b17ec3ab1ef2ccbc914827 840w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-edit.png?w=1100&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=b57805a426feb48ab58e57f926b7f244 1100w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-edit.png?w=1650&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=979a284875616b8c2e3099641ec57fae 1650w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-edit.png?w=2500&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=5575ea4dc41066a8ad2e9e7876997e2f 2500w" />
</Frame>

After you’ve selected a schedule, click **Save** to apply it.

***

## Important Notes

<Note>
  When linking a new Custom Send Schedule to an active Sequence, **Unify will
  immediately reschedule all pending emails for that Sequence** according to the
  new Custom Send Schedule configurations.
</Note>

> 💡 **Tip:** If you’re running outreach across multiple regions, use different Custom Send Schedules for each region’s Sequences to optimize timing and engagement.

***
