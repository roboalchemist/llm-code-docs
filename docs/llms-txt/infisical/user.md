# Source: https://infisical.com/docs/cli/commands/user.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# infisical user

> Manage logged in users

```bash  theme={"dark"}
infisical user
```

## Description

This command allows you to manage the current logged in users on the CLI

### Sub-commands

<Accordion title="infisical user switch" defaultOpen="true">
  Use this command to switch between profiles that are currently logged into the CLI

  ```bash  theme={"dark"}
  infisical user switch
  ```
</Accordion>

<Accordion title="infisical user update domain">
  With this command, you can modify the backend API that is utilized for all requests associated with a specific profile.
  For instance, you have the option to point the profile to use either the Infisical Cloud or your own self-hosted Infisical instance.

  ```bash  theme={"dark"}
  infisical user update domain
  ```
</Accordion>

<Accordion title="infisical user get token">
  Use this command to get your current Infisical access token and session information. This command requires you to be logged in.

  The command will display:

  * Your session ID
  * Your full JWT access token

  ```bash  theme={"dark"}
  infisical user get token
  ```

  Example output:

  ```bash  theme={"dark"}
  Session ID: abc123-xyz-456
  Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
  ```

  ### Flags

  <Accordion title="--plain">
    Output only the JWT token without formatting (no session ID)

    Default value: `false`

    ```bash  theme={"dark"}
    # Example
    infisical user get token --plain
    ```

    Example output:

    ```bash  theme={"dark"}
    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
    ```
  </Accordion>
</Accordion>
