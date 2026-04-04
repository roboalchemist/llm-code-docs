# Source: https://docs.curator.interworks.com/curator_api/custom_integration/scripts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scripts

> Set up and manage custom scripts for scheduled or ad-hoc execution

You can set up custom scripts to run by the site. This requires the "Integration" setting to be enabled. To
create a custom script to be run on a schedule or ad hoc:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on the "Integration" link at the top.
4. Click on "Manage Scripts" in the left navigation.
5. Click on the "New Script" button at the top of the main page content.
6. Enter the name, description, and schedule of execution of the script, and select the appropriate script language.
7. Enter the script details as appropriate
   * For EDT, the full path to the EDT console runner must be specified and the EDT plan must be uploaded.
   * For powershell and python, the script code must be typed or copy and pasted in.
   * If additional arguments need to be passed to the command which runs the script (i.e. powershell.exe,
     etc.), enter those in the arguments field.
8. Click on the "Create" button.
