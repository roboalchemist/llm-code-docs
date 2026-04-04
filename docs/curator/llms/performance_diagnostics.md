# Source: https://docs.curator.interworks.com/site_administration/performance/performance_diagnostics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Performance Diagnostics

> Guide for collecting system performance data to help the Curator support team diagnose and resolve slow performance issues.

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

When experiencing slow performance with Curator, collecting detailed system information helps the support team identify
the root cause. Follow these steps to gather the necessary diagnostic files.

## Step 1: Collect Server Performance Data

Connect to your Curator server via SSH (Linux) or RDP (Windows), then run the performance script for your operating
system to generate a comprehensive report of your server's configuration, performance metrics, and usage statistics.

<Tabs>
  <Tab title="Linux Servers">
    ```bash  theme={null}
    curl -o /tmp/curator_server_info.sh "https://api.curator.interworks.com/scripts/curator_server_info.sh";
    chmod +x /tmp/curator_server_info.sh && /tmp/curator_server_info.sh
    ```
  </Tab>

  <Tab title="Windows Servers">
    ```powershell  theme={null}
    Invoke-WebRequest -Uri "https://api.curator.interworks.com/scripts/curator_server_info.ps1" -OutFile "$env:TEMP\curator_server_info.ps1";
    PowerShell -ExecutionPolicy Bypass -File "$env:TEMP\curator_server_info.ps1"
    ```
  </Tab>
</Tabs>

<Note>
  The generated file will contain system information including server configuration, performance metrics,
  and usage statistics needed for performance analysis.
</Note>

## Step 2: Access API Keys Settings

<BackendNavPath levelOne="Settings" levelTwo="API Keys" />

<Note>
  You'll use the **REST API Explorer** section on this page to generate diagnostic endpoint URLs.
</Note>

## Step 3: Collect Portal Info Endpoint

1. Under **REST API Explorer**, use the dropdowns to select:
   * **API Section:** Portal
   * **API Method:** Info
2. Click the **REST API Access URL** link to open the endpoint in a new tab.
3. You should see raw JSON data.
4. Right-click on the page and select **Save As** to save the output to a file.
5. Save the file as `info.json` (save as JSON format, **not PDF**).

## Step 4: Collect Portal PHPInfo Endpoint

1. Return to the API Keys page and change the **API Method** dropdown to **PHPInfo** (keep Portal selected).
2. Click the **REST API Access URL** link to open the PHPInfo page.
3. Right-click on the page and select **Save As** to save the output to a file.
4. Save the file as `phpinfo.html` (save as HTML format, **not PDF**).

## Send Files for Analysis

Email the following files to the Curator support team for analysis:

* Server performance data (markdown file from Step 1)
* `info.json` (from Step 3)
* `phpinfo.html` (from Step 4)
* Feel free to include screenshots of any relevant system information.

The support team will analyze these files and provide specific recommendations to improve your system's performance.
