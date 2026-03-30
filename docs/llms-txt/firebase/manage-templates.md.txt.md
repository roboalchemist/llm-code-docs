# Source: https://firebase.google.com/docs/ai-logic/server-prompt-templates/manage-templates.md.txt

> [!WARNING]
> **Preview**: Using server prompt templates is a feature that's in Preview, which means that it isn't subject to any SLA or deprecation policy and could change in backwards-incompatible ways.

<br />

This page describes how to manage templates, including editing, locking,
deleting, and version control.

## Edit and iterate on a template

You can edit any template that's unlocked.

We strongly recommend the following:

- Avoid editing templates that are used in production.  

  Any changes to the template will nearly immediately be used by requests from
  your app, so you need to be cautious about making changes that could break
  your app or cause unexpected changes in behavior.

- Try to use a
  [versioning system](https://firebase.google.com/docs/ai-logic/server-prompt-templates/manage-templates#version-template) for iterating on templates.

Here's how to edit an existing template:

1. In the Firebase console, go to the
   [Firebase AI Logic **Prompt templates** tab](https://console.firebase.google.com/project/_/ailogic/templates).

2. In the list of templates, locate and click on the template you want to
   edit.

3. If the template is locked, unlock it by clicking the
   lock icon in the
   top-right corner of the template.

4. Edit the template, then click **Save**.

5. If the template was locked before, make sure to click the
   lock icon again.

6. Exit the template by clicking **Close**.

## Lock a template

> [!IMPORTANT]
> **Important:** Always lock your template before going to production.

We strongly recommend the following:

- Be aware that locking a template acts as protection against unintentional
  editing, but locking *does **not** entirely block editing*. A project member
  with the appropriate permissions can always unlock a template to edit it.

- Lock templates that are actively being used by code -- especially production
  code.

Here's how to lock a template:

1. In the Firebase console, go to the
   [Firebase AI Logic **Prompt templates** tab](https://console.firebase.google.com/project/_/ailogic/templates).

2. In the list of templates, locate and click on the template you want to
   lock.

3. Lock the template by clicking the
   lock icon in the
   top-right corner of the template.

4. Exit the template by clicking **Close**.

## Delete a template

> [!CAUTION]
> **Caution:** Deleting a template cannot be undone. Also, **if a template is
> deleted, any request from your app that uses that template will fail.**

Note that if a template is deleted, you can create a new template with the same
template ID.

Here's how to delete an existing template:

1. In the Firebase console, go to the
   [Firebase AI Logic **Prompt templates** tab](https://console.firebase.google.com/project/_/ailogic/templates).

2. In the list of templates, locate the template you want to delete.

3. At the end of the template's row, click
   \> **Delete**.

4. Confirm the deletion, then click **Delete**.

## Version a template

We recommend using a versioning system for your server prompt templates. Here
are some general recommendations:

- Create template IDs appended with a version that uses
  [semantic versioning (semver)](https://semver.org/)
  (for example, `my-first-template-v1-0-0`).

- [Use Firebase Remote Config](https://firebase.google.com/docs/ai-logic/server-prompt-templates/versioning-with-remote-config)
  so that you can easily change the template and other values in your request.

- If you want to use a standard versioning infrastructure, you can
  [provide templates as files](https://firebase.google.com/docs/ai-logic/server-prompt-templates/advanced-workflows)
  using the REST API.

You can duplicate an existing template to use as the basis for your next
version:

1. In the Firebase console, go to the
   [Firebase AI Logic **Prompt templates** tab](https://console.firebase.google.com/project/_/ailogic/templates).

2. In the list of templates, locate the template you want to duplicate.

3. At the end of the template's row, click
   \> **Duplicate**.

4. In the new template, increment the template ID to reflect the next version.