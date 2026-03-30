# Source: https://docs.safetycli.com/safety-docs/safety-cli/scanning-for-vulnerable-and-malicious-packages/scanning-in-production.md

# Scanning in Production

To run Safety in the production environment, you need to set the stage to production. This ensures that the security scans are aligned with the strict requirements of production environments.

#### Option 1: Run Safety in Production

To run the Safety CLI in production, use the `--stage` flag set to production like this: `safety --stage production scan`

Ensure the `$SAFETY_API_KEY` is set as an environment variable before running the command.

#### Option 2: Run as a Cron Job

If you want to automate this process, you can set up a cron job to periodically run Safety CLI within your Python repository. Here's an example cron job configuration:

```bash
# Run Safety every day at midnight
0 0 * * * cd /path/to/repo && \
safety --stage production scan >> \
/var/log/safety.log 2>&1
```

This will scan your production environment every day at midnight, appending the output to `/var/log/safety.log`.
