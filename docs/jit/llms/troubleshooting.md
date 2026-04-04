# Source: https://docs.jit.io/docs/troubleshooting.md

# Troubleshooting

If you encounter issues while onboarding GitLab with Jit, follow these troubleshooting steps.

## Choose Group Step - No groups available

Please check the following:

**Token Has No Permissions**

Ensure the token was created with Maintainer role permissions.

**Token Has No Permission to the Chosen Group**

Verify that the token was created for the chosen group with the correct access level.

**No Ability to Create a New Project in the Chosen Group**

Navigate to Group Settings → General → Roles allowed to create projects.

Ensure that Maintainers is set as an allowed role.

## No Scan Being Triggered

Please check the following:

**Wrong Secret**

Go to Jit Platform → Settings → Secret.

Copy the selected secret and paste it into the webhook\_secret\_token key.

**Missing Event Types Selection**

Ensure you have selected all required event types, including:

* Push
* Project
* Merge Request (MR)

**Incorrect Tenant or Installation ID**

Ensure the installation is for the group you chose to integrate with.

Tenant ID: Contact Jit support to obtain the correct Tenant ID.

**Deleted Secret in Jit Platform**

Navigate to Jit Platform → Settings → Secrets.

Add a new webhook\_secret\_token key and paste the correct secret.

## Scan Failures

Please check the following:

**No Runners Configured for Jit Project**

Navigate to Centralized Project → Settings → CI/CD → Runners.

* If using GitLab SaaS:
  * Ensure there are instance runners.
  * Enable the Instance Runners for This Project toggle.
* If using self-hosted runners:
  * Ensure there are project runners.
  * Check the Run Untagged Jobs checkbox.

**IP Whitelisting/Blacklisting**

Reach out to Jit Support for further assistance.

Check Jit documentation for additional guidance.

**Expired Token**

Navigate to Jit Platform → Settings → Secrets.

Update the gitlab\_jit\_secret\_token key with a valid token.

**Deleted Token from Jit Secrets**

Go to Jit Platform → Settings → Secrets.

Add a new gitlab\_jit\_secret\_token key and paste the valid token.

For further assistance, contact Jit Support.