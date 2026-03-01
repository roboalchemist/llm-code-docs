# Source: https://docs.curator.interworks.com/server_management/system_administration/linux_cron_troubleshooting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Linux - Cron Troubleshooting

> Troubleshooting guide for resolving Linux cron job issues in Curator installations, including permission fixes and scheduling problems.

Curator runs regularly scheduled tasks on Linux using the web-server's cron.  This takes care of things like status
checks, scheduled reports, user-syncing along with a host of other very important items.  Rarely this setup can be done
incorrectly on installation, so we've provided some steps for resolving common issues related to the cron.

## Cron Troubleshooting

### Identify Current Cron User

If you're unsure which user is currently running the schedule:run cron job, use these commands:

```bash  theme={null}
# Check all user crontabs for schedule:run
sudo grep -r "schedule:run" /var/spool/cron/

# Check system-wide cron files
sudo grep -r "schedule:run" /etc/cron* /etc/crontab

# Monitor processes when schedule:run executes (run this and wait)
watch -n 1 'ps aux | grep -E "artisan|schedule:run" | grep -v grep'

# Check cron logs for schedule:run execution
sudo grep "schedule:run" /var/log/cron* | tail -20
```

The first two commands will show all cron entries containing "schedule:run" and which user/file they're in. The watch command will show the user in the first column when the process runs. The cron logs should also indicate which user is executing the command.

### Permissions Error

1. Log on to the webserver that is running Curator.
2. In the terminal, login as root user by typing in `su - root`
3. View the cron by typing in `crontab -e`
4. If there is content in the crontab file, check to see if the root user is running anything related to Curator.
   For example, look for "artisan" or "php" commands.
5. If these are found, copy these lines and place them somewhere you can reference later - then delete the lines from
   this and press `esc` then type `:wq` to save the empty file.
6. Find the user running your web-server.  If you are unsure, you can find this on the **Settings** > **Curator** >
   **Status** page on the backend of Curator.
7. Ensuring you're still logged in as root, edit the crontab file associated with your server-run-as user you found in
   the previous step.  For example, if your user was "apache" you would type
   `crontab -e -u apache` and press enter.  This will open the crontab file.  Press `i` to enter "insert mode" and paste in
   the contents from step #5.  Then press `esc` and type `:wq` to save the empty file.

NOTE: If the contents of all your cron files are empty, then revisit step #7 above (ensuring you're still logged in as
root) and paste in the contents below while in insert mode:
`* * * * * php /var/www/html/artisan schedule:run >> /dev/null 2>&1`

### Test Cron

In order to make sure your cron schedule is running properly, you can manually fire the cron task via Curator's API
using the steps below.  If you do not receive a 'success' response then you may need to adjust your environment configuration:

1. Follow instructions in the
   [Auto Generate API Links](/curator_api/getting_started/curator_api_overview)
   section and ensure the dropdowns are set to **Portal** and **cron** respectively.
2. Click the preview link generated
3. Link will open in new tab and should display a "success" message
