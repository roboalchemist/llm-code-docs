# Source: https://docs.logrocket.com/docs/updating-snowflake-to-key-pair-auth.md

# Updating Snowflake to key/pair auth

## Overview

Snowflake is deprecating its use of password-based authentication in **Spring 2026**.

We encourage our customers to upgrade as soon as possible to prevent any issues closer to the deadline.

<Callout icon="📘" theme="info">
  These instructions are ONLY for customers who have previously set up Snowflake with password-based authentication!

  You may have already set up key/pair based authentication (the "Alternative Authentication Method" listed on the [Snowflake Prerequisites](https://docs.logrocket.com/docs/snowflake-prerequisites#/) page).

  To check, you can run `DESCRIBE USER <username>`in Snowflake.  If the key is set and `TYPE` is `service`, you can disregard the rest of the steps.
</Callout>

<br />

## Upgrade steps

The LogRocket Streaming Data Export UI has been updated to accommodate the new key/pair authentication flow.

### Step 1:  Follow steps in LogRocket

Visit the [Streaming Data Export Settings Page](https://app.logrocket.com/r/settings/streaming-data-export) and follow the updated UI in-app for Snowflake.  The relevant fields should be autofilled with your organization's details.

<Image align="center" border={false} src="https://files.readme.io/bd555346a633700e4835cc244913cd4caac7dd8590a333961eeafa32d5eef4f5-Screenshot_2025-10-01_at_12.34.26_PM.png" />

Please note the **SSH Public Key** provided here.

### Step 2:  Add public key to Snowflake

In Snowflake, run the following with the SSH public key copied from the LogRocket UI:

```
ALTER USER <username> SET RSA_PUBLIC_KEY=<new_SSH_public_key>
```

<br />

Then, run the following to update the user tpye:

```text
ALTER USER <username> SET TYPE = SERVICE;
```

Finally, you can verify the update by running:

```
DESCRIBE USER <username>;
```

You may also wish to unset the pre-existing password (this is optional):

```
ALTER USER <username> UNSET PASSWORD;
```

You should not experience any disruptions in data streaming service.

Please contact us if you have any questions or experience any issues.

<br />

<br />