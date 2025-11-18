# Source: https://docs.windsurf.com/troubleshooting/plugins-enterprise/vscode.md

# Visual Studio Code (VSCode)

VS Code 1.89 or greater are supported!

# Gathering extension logs

Starting in VS Code Extension 1.10.0, the Extension Diagnostics are accessible for download via the Settings page. This download will contain a collection of relevant logs and parameters into a text file.

*For full output logs of VSCode:*

1. Go to the Command Palette (`Ctrl/Cmd + Shift + P` or go to View > Command Palette)

2. Type in "Show logs" and select the option that reads `Developer: Show Logs`

3. From the dropdown, select `Extension Host`

4. You should see something similar to the image below:

<Frame>
  <img src="https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-showlogs.jpg?fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=8a5317496a257a1efffaf5191c7963c9" data-og-width="2244" width="2244" data-og-height="410" height="410" data-path="assets/plugins/troubleshooting-vscode-showlogs.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-showlogs.jpg?w=280&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=4268142b3843c514977b07d8388232a3 280w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-showlogs.jpg?w=560&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=728c2a187b07fa4e33dc32f5a9c7e9fb 560w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-showlogs.jpg?w=840&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=2635e312277210b8124f3676fe9b13ed 840w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-showlogs.jpg?w=1100&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=33cab90539c14a54e1d5b29d7d2a6f1e 1100w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-showlogs.jpg?w=1650&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=a249a33aaa1e4a9c8b6f99e08e08e8bc 1650w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-showlogs.jpg?w=2500&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=271ab0396f1060a9cfda797488f66eda 2500w" />
</Frame>

5. Change the dropdown in the top right that reads "Extension Host" and select "Codeium"

6. Export or copy the logs

# How to reset or change your Enterprise URL

1. Navigate to the Codeium Enterprise extension settings by pressing Ctrl+Shift+X. Choose the Enterprise Updater (purple extension)

<Frame>
  <img src="https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-enterprise-updater.jpg?fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=aa08c3bed861bc4a12a74b28858c2a55" data-og-width="2562" width="2562" data-og-height="970" height="970" data-path="assets/plugins/troubleshooting-vscode-enterprise-updater.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-enterprise-updater.jpg?w=280&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=6dff61250d3afaf74e3c9a9d82d2a7c2 280w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-enterprise-updater.jpg?w=560&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=84d1995dca640571726c2b662e02d082 560w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-enterprise-updater.jpg?w=840&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=29e543f61bfabeb697cf5cb126f5a165 840w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-enterprise-updater.jpg?w=1100&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=94021abd9458a7089a51a7da36b7047f 1100w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-enterprise-updater.jpg?w=1650&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=6101e40ac8cd97629067ec2710c014ed 1650w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-enterprise-updater.jpg?w=2500&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=6ad969ea4a22dd12fff360b4d7caf0a4 2500w" />
</Frame>

2. Click on the gear icon and select `Extension Settings`

<Frame>
  <img src="https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-enterprise-settings.jpg?fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=47b9618b69cdb38b242f6766a72bacf3" data-og-width="1386" width="1386" data-og-height="574" height="574" data-path="assets/plugins/troubleshooting-vscode-enterprise-settings.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-enterprise-settings.jpg?w=280&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=3c8b645ed9b6fddfdc7cf07270e80df6 280w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-enterprise-settings.jpg?w=560&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=4a7fe1acf97e3998c3506bbb9743424f 560w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-enterprise-settings.jpg?w=840&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=0b74e308ec0a7286a552a80fb48d6c13 840w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-enterprise-settings.jpg?w=1100&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=85c6e05c54f1b4720ef1fbcc6df6ce7e 1100w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-enterprise-settings.jpg?w=1650&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=b83d8d8034e0ab304bec47db41704618 1650w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-enterprise-settings.jpg?w=2500&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=24433d5a06f9bb89d77d81d2938ce0c9 2500w" />
</Frame>

3. In the extension settings, click the gear icon and select `Reset Setting` for each box populated with a URL

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/codeium/assets/plugins/troubleshooting-vscode-enterprise-reset-settings.jpg" />
</Frame>

4. Reload VSCode by going to View -> Command Palette. Once the command palette is open type "Reload window" and press enter.

5. Once reloaded, you should be prompted to Set URL. From here, type in the new URL.

<Frame>
  <img src="https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-enterprise-url.jpg?fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=23248d22ccac6991079450a59dda8188" data-og-width="1984" width="1984" data-og-height="630" height="630" data-path="assets/plugins/troubleshooting-vscode-enterprise-url.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-enterprise-url.jpg?w=280&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=0aa1514fb4fa89dafb9f8487f9cc8661 280w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-enterprise-url.jpg?w=560&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=dfe25827e12131e74664a26e959a6688 560w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-enterprise-url.jpg?w=840&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=f81f0a8da8ee4edb651169f6ceb61771 840w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-enterprise-url.jpg?w=1100&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=bc2b0ecbc0e62c8ce33f5fc5e88c5794 1100w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-enterprise-url.jpg?w=1650&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=f9606b889995bb79aa865e36a9a931be 1650w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/plugins/troubleshooting-vscode-enterprise-url.jpg?w=2500&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=de21165ac09d862697403d6e1332a2c1 2500w" />
</Frame>

6. Close out of the Setting tab.

7. Reload VSCode by going to View -> Command Palette. Once the command palette is open type 'Reload window' and press enter.

8. After reloading, you should see a pop-up in the bottom right prompting you to sign in to Codeium. If not, go to the bottom left Accounts tab and click Sign in with Auth to use Codeium. Either method will redirect you to your Codeium Enterprise portal.

# Known IDE issues and solutions

## e.split is not defined

You are using an unsupported VS Code version, please update to a supported version and try again. You can find a list of supported versions [here](/plugins/compatibility).

## Using the wrong API Server

If a user changes their API Server/Portal URL in their **workspace** settings, this will override their user settings and may result in an error where the extension is communicating with the wrong API server.

Make sure that your API Server/Portal URL is set correctly and not overridden accidentally by the workspace settings.

## Not seeing Codeium Chat responses

If you are trying to send messages to Codeium chat but not seeing responses, check if you can cancel the response. If you are unable to cancel the response, this means that the response was completed but not displayed. This can happen if the Chat Web Server loses connection to the extension. Reloading VS Code and opening the Codeium Chat panel again should show the responses.

## Unable to read file .../package.json

```
Unable to read file .../.vscode/extensions/codeium.codeium-<version>/package.json 
```

If the above error shows up in the Codeium logs, try deleting the extension folder (.../.vscode/extensions/codeium.codeium-\<version>) and reinstall the extension.

## VS Code Enterprise Updater Loop

"Codeium Enterprise Updated" every time you open VSCode, try restarting all extensions

1. Open the command palette ( CTRL + SHIFT + P )
2. Run 'Disable All Installed Extensions'
3. Run 'Enable all Extensions'
4. Restart VS Code

Make sure all extensions are enabled again.

## Enterprise updater doesn't install Codeium extension

The Enterprise updater is installed, but no extension is being downloaded or installed in VSCode. No extension logs option is available in VSCode output window drop down. The only available log you can see is:

```
[info] ExtensionService#_doActivateExtension Codeium.codeium-enterprise-updater, startup: false, activationEvent: 'onStartupFinished'
```

If you have previously disabled the Codeium extension and later uninstalled it, VSCode will not clear the disabled flag.

In order to do so manually:

1. Open the command palette ( CTRL + SHIFT + P )
2. Run 'Codeium Enterprise: Reset'
3. Select "Help" from the popup
4. Select "Show Disabled Extensions"
5. Re-enable your Codeium Extension

## Proxy / Network Issues

Unchecking `Detect Proxy` in Codeium settings in VSCode can sometimes resolve issues where the extension is incorrectly attempting to use a proxy.

## Certificate Issues

If you encounter the following errors:

```
ConnectError: [internal] unable to get issuer certificate
```

```
[ERROR]: [internal] unable to verify the first certificate
```

```
tls: failed to verify certificate: x509: "<yourdomainurl>" certificate is not standards compliant
```

This suggests that the Codeium extension is unable to trust the TLS connection to your enterprise portal / API server because it does not trust the certificate being presented. This either means that the certificate presented by the Codeium deployment is untrusted or a certificate presented by a corporate proxy intercepting the request is untrusted.

In either case, the most preferable solution is to ensure that the root certificate that signed this certificate is properly installed on end-user machines in the appropriate location. VS Code and most other IDEs load certificates from the operating system's default location.

Your certificate is issued and managed by your local IT or Admin team. Please reach out to them for assistance with installing the necessary certificates on your system.

It is important that the full certificate chain is being presented from wherever TLS is being terminated. Oftentimes, if only the leaf certificate is presented, VS Code and other IDEs are unable to verify its authenticity because they are not aware of the intermediate certificate which validates the leaf certificate and is validated by the root certificate. Browsers are often able to work around this issue as users will likely have encountered a different website that does present the full certificate chain, so the intermediate cert is seen and cached, but applications like VS Code don't have this advantage.

The Network Proxy Text VS Code extension is useful for debugging certificate issues.
