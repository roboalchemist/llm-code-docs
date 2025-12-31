# Source: https://docs.windsurf.com/troubleshooting/plugins-gathering-logs.md

# Gathering Logs

If you're having issues, the first step in the troubleshooting process is to retrieve the logs from your IDE. Here's how you can get Windsurf logs for each of the major IDEs:

## JetBrains IDEs

<Tabs>
  <Tab title="Local">
    Cascade has now the option to generate a diagnostics file directly from the IDE, there are 2 ways to do so:

    * In the Cascade window, click on the 3 dots in the upper right side, and select Download Diagnostics
    * In the IDE menu, go to Tools > Windsurf > Download Windsurf Diagnostics

    The first option is preferred since it also includes Cascade embedded browser logs.
    This button will automatically collect relevant logs and parameters into a text file.

    In extreme situations, you can always get the IDE full log (idea.log) from Help > Show Log in Explorer/Finder.
  </Tab>

  <Tab title="Remote">
    To gather the Windsurf diagnostics, you can use the following options:

    * In the Cascade window, click on the 3 dots in the upper right side, and select Download Diagnostics
    * In the IDE menu, go to Tools > Windsurf > Download Windsurf Diagnostics

    The first option is preferred since it also includes Cascade embedded browser logs.

    In addition, to collect the full IDE logs:

    * In the IDE menu, go to Tools > Windsurf > Collect Host and Client Logs
  </Tab>
</Tabs>

## VS Code

1. Go to the Command Palette (`Ctrl/Cmd + Shift + P` or go to View > Command Palette)

2. Type in "Show logs" and select the option that reads "Developer: Show Logs"

3. Change the dropdown in the top right that reads "Extension Host" and select "Windsurf"

4. You should see something similar to the image below:

<Frame style={{ border: 'none', background: 'none' }}>
  <img src="https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/extension-diagnostics-log.png?fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=5559a02942eaf0fe736625f13e86bf67" data-og-width="2042" width="2042" data-og-height="272" height="272" data-path="assets/extension-diagnostics-log.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/extension-diagnostics-log.png?w=280&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=2344ea0881b4de4a4433812e6c956e23 280w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/extension-diagnostics-log.png?w=560&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=429e361008386d9abcf033d991477321 560w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/extension-diagnostics-log.png?w=840&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=a0ad762267a2b4c3af14027caf4eb2bf 840w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/extension-diagnostics-log.png?w=1100&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=deb9ce059733784d94a337a19993a5c5 1100w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/extension-diagnostics-log.png?w=1650&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=56faddc7414338ad6e16650acba2d53a 1650w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/extension-diagnostics-log.png?w=2500&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=88e03340e7060bc698560856ffe32fb4 2500w" />
</Frame>

5. Export or copy the logs

## Eclipse

In Eclipse, logs are written to the following paths:

* **Mac/Linux**: \~/.codeium/codeium.log
* **Windows**: C:\Users\<username>.codeium\codeium.log

## Visual Studio

Go to **view > output**, select "Windsurf" in the dropdown, and copy the logs.

## NeoVim

Set `g:codeium_log_file` to a path to a file in their vimrc and then relaunch vim.

Then the logs should be written to that file.
