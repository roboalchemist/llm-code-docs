# Source: https://docs.curator.interworks.com/site_administration/performance/troubleshooting_load_times.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting Load Times 

> Diagnose and resolve slow loading issues using Curator debug mode for performance optimization.

When determining the root-cause of latency issues on Curator, using the debug mode for Curator is the fastest
way to rule out a number of issues that may be causing slow loading times.  This can come from the location
of your servers and/or networking issues, custom code, internal Curator issues or slow Dashboard load times.
Curator's debug mode provides the Curator team with enough information to know where to start looking when
addressing these issues.  Follow the steps below to view Curator's debug data, and download the debug file
and send it to the Curator support team if you have any concerns.

## Enabling Debug Mode

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click on the "General" tab at the top of the main page content.
4. In the "Debug" section, turn ON *Enable Frontend Debug* and click the "Save" button.

## Using the Debug Mode

1. Append `?debug=1` to the end of any url (unless there is already a `?` in the url, in which case append `&debug=1`)\*
2. Click the arrow on the bottom tray to expand the debug menu, then navigate between the tabs to view the debug output.
   \*NOTE: If you are debugging slow login times, be sure to logout first, and then add the debug parameter to
   your URL (e.g. `http://curatorexample.com/backend`?debug=1)

## Capturing Debugging Results

1. Once you have followed the **Using the debug mode** steps above, you can download the results of your
   debugging session using the export button on the debugging tray:

   <img src="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_administration/performance/download_debugbar.png?fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=cbf803e7b7f062cb46ec3fb460b68603" alt="debug download" data-og-width="432" width="432" data-og-height="169" height="169" data-path="assets/images/site_administration/performance/download_debugbar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_administration/performance/download_debugbar.png?w=280&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=59c527debb32a97c025060e9ec615d05 280w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_administration/performance/download_debugbar.png?w=560&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=3b891790274288cfb4e3793e30e01e43 560w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_administration/performance/download_debugbar.png?w=840&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=f1fe117a9714390175604e8e04fbe133 840w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_administration/performance/download_debugbar.png?w=1100&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=600a37e311f8dca5adea8762e3bc5eab 1100w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_administration/performance/download_debugbar.png?w=1650&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=d59e546210f44b62661fd0aa5c122019 1650w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/site_administration/performance/download_debugbar.png?w=2500&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=5a16119387c9146476895337b4b577ab 2500w" />

2. This will output a `.iw` file which you can send to Curator support for assistance with slow load times.
