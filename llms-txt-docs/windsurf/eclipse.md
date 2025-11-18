# Source: https://docs.windsurf.com/troubleshooting/plugins-enterprise/eclipse.md

# Eclipse

# Supported Versions

Version 4.25+ (2022-09+)

# Gathering extension logs

In Eclipse, logs are written to the following paths:

* **Mac/Linux**: \~/.codeium/codeium.log
* **Windows**: C:\Users\<username>.codeium\codeium.log

# How to reset or change your Enterprise URL

1. Open the settings/preferences dialog.

2. Select Codeium.

3. Set the Portal URL to `<NEW_URL>`. Then click the Apply and Close button.

<Frame>
  <img src="https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/plugins/troubleshooting-eclipse-portal-url.jpg?fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=a7a3dc48899d017362dff5b8cac8d7b3" data-og-width="2890" width="2890" data-og-height="2099" height="2099" data-path="assets/plugins/troubleshooting-eclipse-portal-url.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/plugins/troubleshooting-eclipse-portal-url.jpg?w=280&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=f7049748ba25b58625cc311027b5e72d 280w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/plugins/troubleshooting-eclipse-portal-url.jpg?w=560&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=50ea671aea859baee84dd99612e65c7b 560w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/plugins/troubleshooting-eclipse-portal-url.jpg?w=840&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=ae2c7d50a45a09e7aca67f2bb3203a06 840w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/plugins/troubleshooting-eclipse-portal-url.jpg?w=1100&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=4fabb3f06336d578744b7ba05282ab7b 1100w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/plugins/troubleshooting-eclipse-portal-url.jpg?w=1650&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=7096312ee2fbef2921692bbe40abba21 1650w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/plugins/troubleshooting-eclipse-portal-url.jpg?w=2500&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=97be642c613ab57ec808da69b2fbd0a3 2500w" />
</Frame>

# Known IDE issues and solutions

## Codeium isn't starting

If Codeium isn't starting up, use the logs to debug what the cause could be (See above). If you are not able to resolve the issue, file a help request by submitting a ticket at help.codeium.com. Make sure to include the logs referenced above to help our team debug the issue as quickly as possible.

## Codeium Chat shows an empty screen

If you are using Windows 10, it's possible you need to install **WebView2** to switch the Eclipse web renderer from Internet Explorer to Edge.

You can see if this is the case by right-clicking --> `Properties` and seeing if there is an Internet Explorer icon.

## Certificate issue

This issue may be indicated by the following errors in the logs:

```
Failed to fetch extension version at <YourDomainURL>
javax.net.ssl.SSLHandshakeException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
```

Unlike other IDEs, Eclipse does not use the OS certificate store. You will have to load the certificates to the Java keystore.

* SaaS users will have to load the Codeium Github URL
* Self-hosted (On-prem) users will have to load their Codeium Enterprise domain URL as well as the Codeium Github URL

**Note**: This is an example for SaaS users, but the process is the same. *For enterprise users - Your certificate is issued and managed by your local IT or Admin team. Please reach out to them for assistance with installing the necessary certificates on your system.*

1. Export the certificate for [https://exafunction.github.io/](https://exafunction.github.io/) from the browser as `githubio.cer` file

In Chrome: navigate to the website, click the padlock, click `Connection is secure`, click `Certificate is valid`, go to the `Details` tab, press the `Copy to File...` button

2. Import in JDK/JRE keystore: (Need to run from cmd prompt opened with "Administrator" privilege)

```
keytool -import -noprompt -trustcacerts -alias codeiumgithub -file githubio.cer -keystore "%JAVA_HOME%/jre/lib/security/ cacerts" -storepass changeit
```

3. Verify that the certificate is added to the Keystore by executing:

```
keytool -list -keystore "%JAVA_HOME%/jre/lib/security/ cacerts" | findstr codeium
```

Enter the Keystore password.

4. Restart Eclipse and browse the marketplace extension from an internal browser. You should be directed to trust the unsigned content.

5. In some cases you might also need to pass the certificates path in VM arguments by editing your eclipse.ini file and adding the path:

```
-Djavax.net.ssl.trustStore="path-to-your-certificates"
```
