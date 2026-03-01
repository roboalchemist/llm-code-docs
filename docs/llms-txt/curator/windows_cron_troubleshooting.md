# Source: https://docs.curator.interworks.com/server_management/system_administration/windows_cron_troubleshooting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Windows - Cron Troubleshooting

> Troubleshooting guide for resolving Windows cron job issues in Curator installations, including scheduled task path fixes and configuration problems.

export const BackendNavPath = ({levelOne, levelTwo, levelThree, tab, section}) => {
  const levels = [levelOne, levelTwo, levelThree].filter(Boolean);
  const lastLevel = levels.length ? levels[levels.length - 1] : '';
  return <span>
      In the <a href="/setup/installation/linux_installation">backend of Curator</a> using the left-hand navigation,
      navigate to the
      {levelOne && <strong>{" " + levelOne}</strong>}
      {levelOne && levelTwo && " > "}
      {levelTwo && <strong>{levelTwo}</strong>}
      {levelTwo && levelThree && " > "}
      {levelThree && <strong>{levelThree}</strong>} page.
      {(tab || section) && <>
          {" "}On the {lastLevel} page
          {tab && <> click the <strong>{tab}</strong> tab</>}
          {tab && section && " and"}
          {section && <> expand the <strong>{section}</strong> section</>}.
        </>}
    </span>;
};

Curator runs regularly scheduled tasks on Windows using Task Scheduler. This takes care of things like status checks,
scheduled reports, user-syncing along with a host of other very important items. Occasionally this setup can have
issues, so we've provided some steps for resolving common problems related to Windows scheduled tasks.

## Scheduled Task Troubleshooting

### Path Issues

The most common issue with Windows scheduled tasks for Curator is an incorrect path to the artisan file. To troubleshoot this:

1. Open Task Scheduler:
   * Press `Windows Key + R`, type `taskschd.msc`, and press Enter
   * Or search for "Task Scheduler" in the Start Menu

2. Find the Curator task:
   * Look for tasks named "Curator Cron", "Curator Central Dispatch", or similar
   * Double-click the task to open its properties

3. Check the action path:
   * Click the "Actions" tab
   * Click "Edit" to view the action details
   * Note the full command in the "Program/script" and "Add arguments" fields
   * Common format: `C:\InterWorks\Curator\libs\PHP\php.exe C:\InterWorks\Curator\htdocs\artisan schedule:run`
   * **Note:** Your installation path may differ (e.g., `D:\Curator`, `E:\InterWorks\Curator`, etc.)

4. Test the command manually:
   * Open Command Prompt as Administrator
   * Copy the full command from the scheduled task (combining program and arguments)
   * Run the command exactly as it appears in the task
   * Observe the output:
     * **Success**: Command runs without errors
     * **"The system cannot find the path specified"**: Path to php.exe or artisan is incorrect
     * **PHP errors**: Path is correct but there are application issues
     * **No output**: May indicate the command is running but not producing visible output

5. Common path corrections:
   * Verify your Curator installation directory (common locations: `C:\InterWorks\Curator`, `D:\Curator`, etc.)
   * Ensure php.exe exists at: `[YourInstallDir]\libs\PHP\php.exe`
   * Confirm artisan file exists at: `[YourInstallDir]\htdocs\artisan`
   * Update the scheduled task with corrected paths if needed
   * **Remember:** Replace `[YourInstallDir]` with your actual installation path

### Determine Correct Scheduled Task User

The scheduled task should run as the same user that your web server (IIS/Apache) is running as. Here's how to determine the correct user:

**Check Web Server User in Curator Backend:**

1. <BackendNavPath levelOne="Settings" levelTwo="Curator" levelThree="Status" />
2. Look for the "User" field in the System Information section
3. This shows which user account your web server is running as (e.g., IIS\_IUSRS, SYSTEM, apache, etc.)
4. Your scheduled task should be configured to run as this same user to avoid permission issues

**Verify Current Task User in Task Scheduler:**

1. In Task Scheduler, find the Curator task

2. View the user account using one of these methods:
   * **Method 1:** In the main panel, look at the "Security options" column
   * **Method 2:** Double-click the task, go to "General" tab
   * Look for "When running the task, use the following user account:"
   * Common accounts: SYSTEM, NT AUTHORITY\SYSTEM, or a service account

3. Additional task details:
   * "Actions" tab shows the exact command being run
   * "History" tab shows recent execution logs and any errors
   * "Triggers" tab shows when the task runs (typically every minute)

**Using PowerShell:**

```powershell  theme={null}
# List all Curator scheduled tasks with their run-as user
Get-ScheduledTask | Where-Object {$_.TaskName -like "*Curator*"} | 
    ForEach-Object {
        [PSCustomObject]@{
            TaskName = $_.TaskName
            State = $_.State
            RunAsUser = $_.Principal.UserId
            Action = $_.Actions.Execute + " " + $_.Actions.Arguments
        }
    }
```

### Test Scheduled Task

To verify the scheduled task is working properly:

1. **Test command directly in Command Prompt:**
   * Open Command Prompt as Administrator
   * Navigate to your Curator directory (adjust path as needed): `cd C:\InterWorks\Curator`
   * Run the exact command from your scheduled task
   * **Important:** Replace the paths below with the actual paths from your Task Scheduler action:
     ```
     C:\InterWorks\Curator\libs\PHP\php.exe C:\InterWorks\Curator\htdocs\artisan schedule:run
     ```
     (Your paths may differ - use `D:\`, `E:\`, or different directory names as shown in Task Scheduler)
   * Check the output:
     * **Success**: Shows "Running scheduled command:" or similar output
     * **Errors**: Note any error messages for troubleshooting

2. **Manual test via Task Scheduler:**
   * Right-click the Curator task in Task Scheduler
   * Select "Run"
   * Check the "Last Run Result" column (should show "0x0" for success)

3. **Check via Curator API:**
   * Follow instructions in the [Auto Generate API Links](/curator_api/getting_started/curator_api_overview) section
   * Set dropdowns to **Portal** and **cron** respectively
   * Click the preview link
   * Should display a "success" message

4. **Verify in logs:**
   * Check Curator logs at: `[InstallDir]\storage\logs\system-[date].log`
   * Look for recent cron execution entries

### Common Issues and Solutions

1. **Task runs but nothing happens:**
   * Check if the user account has permissions to the Curator directory
   * Verify PHP can be executed by the task user
   * Check Windows Event Viewer for errors

2. **Task shows error code:**
   * `0x1`: General error - check the command syntax
   * `0x2`: File not found - verify all paths
   * `0x5`: Access denied - check permissions

3. **Task doesn't run on schedule:**
   * Verify the trigger is set to run every minute
   * Check if "Start the task only if the computer is on AC power" is unchecked
   * Ensure "Run whether user is logged on or not" is selected
