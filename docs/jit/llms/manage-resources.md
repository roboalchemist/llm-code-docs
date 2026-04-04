# Source: https://docs.jit.io/docs/manage-resources.md

# Manage Resources

Jit lets you control which resources are protected - code repositories, SCM organizations, and cloud accounts (AWS, Azure, GCP).

***

## Code repositories (SCM)

1. Go to **Settings → Manage Resources**.
2. Select the relevant SCM tab (e.g., GitHub).
3. Check or uncheck repositories as needed.
4. Select **Done** to save.

Unchecked repositories will not be scanned or protected by Jit.

### Archived repositories

Jit automatically handles archived repositories - no manual action needed.

When a repository is archived in GitHub, Jit immediately removes it from coverage and resolves all associated findings. If the repository is restored, Jit re-adds it to coverage and triggers a full scan.

***

## Cloud accounts (AWS, Azure, GCP)

1. Go to **Settings → Manage Resources**.
2. Select the relevant cloud tab (AWS, Azure, or GCP).
3. Check or uncheck accounts as needed.
4. Select **Done** to save.

Unchecked accounts will not be protected by Jit.