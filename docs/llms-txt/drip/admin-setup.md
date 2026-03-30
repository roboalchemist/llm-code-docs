# Source: https://docs.drip.re/burn-ghosts-activity/admin-setup.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Admin Setup

> Essential Discord slash commands for server administrators to configure Burn Ghosts Activity

## Overview

Server administrators must run two essential slash commands to enable full functionality of the Burn Ghosts Activity. These are **one-time setup commands** that connect your server to the DRIP Rewards system and configure tournament management permissions.

<Warning>
  Both commands require **Administrator** Discord permissions to execute.
</Warning>

## Discord Slash Commands

### `/authorize` (Admin Only)

Connects your Discord server to the DRIP Rewards system for token reward distribution.

<Card title="Purpose" icon="link">
  Links your Discord server to DRIP Rewards so tournament prizes can be distributed as tokens
</Card>

**What it does:**

* Generates a DRIP authorization link for your server
* Provides DRIP bot install button if not already installed
* Links server to a DRIP realm for automatic reward distribution
* Enables token balance viewing and transactions

**When to use:**

* **Required first** before hosting tournaments with token rewards
* Must be run once during initial setup
* Re-run if you need to re-authorize or change DRIP realm connection

<Steps>
  <Step title="Run the command">
    Type `/authorize` in any channel where you have permissions
  </Step>

  <Step title="Click authorization link">
    Follow the generated link to connect to DRIP
  </Step>

  <Step title="Install DRIP bot (if needed)">
    If prompted, install the DRIP bot to your server
  </Step>

  <Step title="Complete authorization">
    Confirm the connection in the DRIP interface
  </Step>
</Steps>

### `/set_master_role` (Admin Only)

Configures which Discord role can access tournament management features in the activity.

<Card title="Purpose" icon="user-shield">
  Determines who can create and manage tournaments in the admin panel
</Card>

**What it does:**

* Takes a Discord role as a parameter
* Grants admin panel access to members with the specified role
* Allows tournament creation, editing, and management
* Controls access to game configuration

**When to use:**

* After running `/authorize` command
* When setting up tournament organizers
* When changing which role manages tournaments

<Steps>
  <Step title="Create a role (if needed)">
    Create a Discord role for tournament managers (e.g., "Tournament Admin")
  </Step>

  <Step title="Run the command">
    Type `/set_master_role` in any channel
  </Step>

  <Step title="Select the role">
    Choose the role from the dropdown parameter
  </Step>

  <Step title="Confirm">
    Members with this role now have admin access in the activity
  </Step>
</Steps>

## Setup Checklist

<AccordionGroup>
  <Accordion title="Step 1: Initial Authorization">
    * Run `/authorize` command
    * Complete DRIP authorization flow
    * Verify DRIP bot is installed
    * Confirm server is linked to DRIP realm
  </Accordion>

  <Accordion title="Step 2: Configure Admin Access">
    * Create or identify the admin role
    * Run `/set_master_role` with chosen role
    * Assign role to tournament managers
    * Verify admin panel access in activity
  </Accordion>

  <Accordion title="Step 3: Test Configuration">
    * Launch Burn Ghosts Activity
    * Check admin panel visibility (admins only)
    * Verify token balances are visible
    * Test creating a sample tournament
  </Accordion>
</AccordionGroup>

## Important Notes

<Info>
  **Setup Order Matters**: Always run `/authorize` before `/set_master_role` to ensure proper functionality.
</Info>

<Warning>
  **Regular Users Don't Need These Commands**: These are server setup commands for administrators only. Regular players can start playing immediately after setup is complete.
</Warning>

### Who Needs What?

| User Type          | Needs /authorize | Needs /set\_master\_role | Can Play |
| ------------------ | ---------------- | ------------------------ | -------- |
| Server Admin       | ✅ Must run       | ✅ Must run               | ✅ Yes    |
| Tournament Manager | ❌ No             | ❌ No (assigned role)     | ✅ Yes    |
| Regular Player     | ❌ No             | ❌ No                     | ✅ Yes    |

## Troubleshooting Commands

### Re-authorizing

If token rewards stop working:

1. Run `/authorize` again
2. Complete the authorization flow
3. Verify connection in DRIP dashboard

### Changing Master Role

To change who can manage tournaments:

1. Run `/set_master_role` with new role
2. Previous role loses admin access
3. New role members gain admin access immediately

### Verification

To verify setup is complete:

* ✅ DRIP bot is present in server
* ✅ `/authorize` completed successfully
* ✅ `/set_master_role` configured with appropriate role
* ✅ Admin panel visible to role members
* ✅ Token balances displaying correctly

<Tip>
  Test your setup with a free tournament first to ensure everything works before creating tournaments with entry fees!
</Tip>

*Keywords: admin setup, slash commands, authorize, set master role, configuration, server setup, discord commands*

Built with [Mintlify](https://mintlify.com).
