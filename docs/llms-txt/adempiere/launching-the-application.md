# Source: https://adempiere.gitbook.io/docs/v3.9.1/introduction/getting-started/launching-the-application.md

# Source: https://adempiere.gitbook.io/docs/introduction/getting-started/launching-the-application.md

# Launching the Application

There are two ways of accessing the ADempiere application: through a java software client that runs on the user's computer or through a web user interface (webui) which can be accessed through a browser. Both these applications communicate with the ADempiere Application Server. Which you use will be determined by your system implementation. In general, the two methods are similar and provide the same functionality. The User Guide will focus on the java client and will discuss the web version where it differs.

## Launching the ADempiere JAVA Client using Web Start

To launch the application, you will need the ADempiere Application Server URL. It may be provided as a link on your company's intranet or you can ask the System Administrator. It may look like

```
http://mycompany.com:8088/admin
```

Open the Application Server URL. It will look something like the following image.

![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LKYc5kZmAN3DUIAq3t5%2F-LKYc6_5l1Uf7JaZlH7P%2Fimage_appserver_admin%20\(1\).png?generation=1534974787327720\&alt=media)

The WebStart option automatically makes sure that the your computer will use the latest version of the ADempiere JAVA Client.

From the Application Server web page, click on the blue WebStart button and you will see the WebStart Dialog:

![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-LJxc0hBdvotIr8-V10n%2F-LJxc1XrF1LNZtbIBpDd%2FWebstart_download_progress.jpg?generation=1534337236613053\&alt=media)

{% hint style="info" %}
If the application Java Client does not start immediately after this, you may need to ask your System Administrator to ensure the Java JNLP file is associated with the Java Web Starter application (javaws).
{% endhint %}

If a security window appears, click on "Always trust content from this publisher".

The very first time the application starts, you will see a license dialog. Accept the license terms.

The application client should start at this point and present a log in dialog. See [Logging In](https://adempiere.gitbook.io/docs/introduction/getting-started/logging-in) for more information.

## Accessing the Web Application

To log in to the Web Application, click the link for the **ADempiere ZK Webui** in the administration page above. You may also have been given the address directly. It will look something line this:

```
http://mycompany.com:8088/webui
```

The web page shown will be the login page to the Web Application running on the server. See [Logging In](https://adempiere.gitbook.io/docs/introduction/getting-started/logging-in) for more information.
