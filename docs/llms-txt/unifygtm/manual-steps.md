# Source: https://docs.unifygtm.com/reference/sequences/manual-steps.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unifygtm.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Manual Sequence Steps

> Bring human-in-the-loop actions to your Unify Sequences.

export const PhoneCallIcon = ({size = 24}) => <>
    <svg class="block dark:hidden" stroke="var(--icon-pink-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path d="M5 4h4l2 5l-2.5 1.5a11 11 0 0 0 5 5l1.5 -2.5l5 2v4a2 2 0 0 1 -2 2a16 16 0 0 1 -15 -15a2 2 0 0 1 2 -2"></path>
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-pink-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path d="M5 4h4l2 5l-2.5 1.5a11 11 0 0 0 5 5l1.5 -2.5l5 2v4a2 2 0 0 1 -2 2a16 16 0 0 1 -15 -15a2 2 0 0 1 2 -2"></path>
    </svg>
  </>;

export const ManualEmailIcon = ({size = 24}) => <>
    <svg class="block dark:hidden" stroke="var(--icon-blue-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path d="M3 7a2 2 0 0 1 2 -2h14a2 2 0 0 1 2 2v10a2 2 0 0 1 -2 2h-14a2 2 0 0 1 -2 -2v-10z"></path>
      <path d="M3 7l9 6l9 -6"></path>
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-blue-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path d="M3 7a2 2 0 0 1 2 -2h14a2 2 0 0 1 2 2v10a2 2 0 0 1 -2 2h-14a2 2 0 0 1 -2 -2v-10z"></path>
      <path d="M3 7l9 6l9 -6"></path>
    </svg>
  </>;

export const ActionItemIcon = ({size = 24}) => <>
    <svg class="block dark:hidden" stroke="var(--icon-purple-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path d="M9 11l3 3l8 -8"></path>
      <path d="M20 12v6a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2v-12a2 2 0 0 1 2 -2h9"></path>
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-purple-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path d="M9 11l3 3l8 -8"></path>
      <path d="M20 12v6a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2v-12a2 2 0 0 1 2 -2h9"></path>
    </svg>
  </>;

Manual steps allow you to layer manual emails, phone calls, action items, and social touches into your Unify Sequences.

## Adding Manual steps to Sequences

In the Sequence Builder, click the `+` button to add a step and choose from the following options:

<CardGroup cols={2}>
  <Card title="Manual email" icon={<ManualEmailIcon />} href="#manual-email-steps">
    Create an email that must be manually queued to send from Unify
  </Card>

  <Card title="Phone call" icon={<PhoneCallIcon />} href="#phone-call-steps">
    Create a task to call the prospect.
  </Card>

  <Card title="Action item" icon={<ActionItemIcon />} href="#action-item-steps">
    This will create a task to perform some generic action.
  </Card>
</CardGroup>

Each time a prospect runs through the Sequence, a corresponding task will be created in your Task Dashboard for each manual step.

<Frame caption="Adding a manual step in a Sequence.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/add-manual-step.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=bc20d14be82a7ab9cce68ec39d6a296a" data-og-width="3046" width="3046" data-og-height="1586" height="1586" data-path="images/reference/sequences/add-manual-step.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/add-manual-step.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c91e98e3998fc07bc0dd96ca3c3e80f7 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/add-manual-step.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=f306f19922af4d4711b834d2fe000e1d 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/add-manual-step.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=f98534b4ce24ee605903443ae7625285 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/add-manual-step.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=fa364223e514204d5d583ec7fab0de2e 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/add-manual-step.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=e935ac9eed7958354f1da20f6cfd196a 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/add-manual-step.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=56f6e7bb6500f265b10d8f9dcb41f8a4 2500w" />
</Frame>

## Manual email steps

Just like automated emails, manual email steps can be composed using
[template variables](/reference/sequences/template-variables)
or [snippets](/reference/sequences/smart-snippets). You can set the priority of
the task that will be created for the step and who to assign the task to.

<Frame caption="Adding a manual email step in a Sequence.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/manual-email-step.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=89cb51506015c59d8903a921b10df145" data-og-width="3014" width="3014" data-og-height="1862" height="1862" data-path="images/reference/sequences/manual-email-step.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/manual-email-step.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=672b3a2457da807c8d61f734172d4ba7 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/manual-email-step.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=37f4b0b65f5a7c11202f5cdf02d804eb 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/manual-email-step.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=2b163a30c425732d0e9657e21ea61556 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/manual-email-step.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=f89177f359e779bc435688a7d1982e75 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/manual-email-step.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=31b3280b9560fe729c023f876814490e 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/manual-email-step.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=33a52e9f8f9e10c4052e67bc48d08783 2500w" />
</Frame>

## Phone call steps

Phone call steps can include notes that will appear on the call task once created.
[Template variables](/reference/sequences/template-variables) and
[snippets](/reference/sequences/smart-snippets) can be used to customize the notes.

<Frame caption="Adding a phone call step in a Sequence.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/phone-call-step.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a15d26ded98ac73c08678c5e9f863afb" data-og-width="2996" width="2996" data-og-height="1084" height="1084" data-path="images/reference/sequences/phone-call-step.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/phone-call-step.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=4f06cabda9b5b8a2b779e2dfa518da85 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/phone-call-step.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=eb18748781f262406cadf33e953c9d45 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/phone-call-step.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c847993e95d3675b0f12975dd8d39138 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/phone-call-step.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=7bd5de861a77fd159b119c7dd86dde4f 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/phone-call-step.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=99a6f5d537184c1708a65cbb87cbc369 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/phone-call-step.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=36ece6039276d6cb77e52eb7aa4c0936 2500w" />
</Frame>

## Action item steps

Action item steps can include notes that will appear on the task once created. These notes
can be used to generate instructions for the user to complete the task or simply contain information
about the prospect. [Template variables](/reference/sequences/template-variables) and
[snippets](/reference/sequences/smart-snippets) can be used to customize the notes.

<Frame caption="Adding an action item step in a Sequence.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/action-item-step.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=be13af243166e535c23dff387e13d777" data-og-width="3004" width="3004" data-og-height="1048" height="1048" data-path="images/reference/sequences/action-item-step.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/action-item-step.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=69fcf93feddb2d235b4ccbb03e0e900f 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/action-item-step.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=26aa7d8581a8de6a56d943514d9ee86f 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/action-item-step.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=3cbcc9cc0ff876a78b26dee956a73689 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/action-item-step.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=7cfce655f1b2884a1f33cd0d7e59e32f 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/action-item-step.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=f0370cc7512fbec38a8d65389d462d97 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/action-item-step.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=99cfd00d658cb25cf46183ba7a3a70fa 2500w" />
</Frame>
