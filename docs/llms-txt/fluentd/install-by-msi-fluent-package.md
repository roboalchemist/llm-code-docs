# Source: https://docs.fluentd.org/installation/install-fluent-package/install-by-msi-fluent-package.md

# .msi Installer (Windows)

The recommended way to install Fluentd on Windows is to use MSI installers of `fluent-package`.

## What is `fluent-package`?

`fluent-package` is a packaged distribution of Fluentd which is formerly known as `td-agent`.

* Includes Ruby and other library dependencies (since most Windows machines don't have them installed).
* Includes a set of commonly-used 3rd-party plugins such as `in_windows_eventlog2`.

You can also see [fluent-package-v5-vs-td-agent](https://docs.fluentd.org/quickstart/fluent-package-v5-vs-td-agent).

## How to install `fluent-package`

{% hint style="danger" %}
The following are deprecated (EOL) fluent-package and td-agent information:

* About [Fluent Package (fluent-package) v5 (EOL)](https://www.fluentd.org/blog/schedule-for-fluent-package-5-eol), See [Install by .msi Package v5](https://docs.fluentd.org/installation/obsolete-installation/fluent-package-v5-eol-installation/install-by-msi-fluent-package-v5).
* About deprecated [Treasure Agent (td-agent) v4 (EOL)](https://www.fluentd.org/blog/schedule-for-td-agent-4-eol), see [Install by .msi Installer v4 (Windows)](https://docs.fluentd.org/installation/obsolete-installation/treasure-agent-v4-eol-installation/install-by-msi-td-agent-v4).
* About deprecated [Treasure Agent (td-agent) 3 will not be maintained anymore](https://www.fluentd.org/blog/schedule-for-td-agent-3-eol), see [Install by msi Package v3](https://docs.fluentd.org/installation/obsolete-installation/treasure-agent-v3-eol-installation/install-by-msi-td-agent-v3).
* Do not directly upgrade from v3 to v5. Such a workflow is not supported. It causes a trouble. Upgrade in stages. (v3 to v4, then v4 to v5)
  {% endhint %}

### Step 1: Install `fluent-package`

Download the latest version of MSI installer from [the download page for Long Term Support version](https://fluentd.cdn.cncf.io/lts/6/windows/index.html). Run the installer and follow the wizard. If you want to use the normal release version, use [the download page for normal release version](https://fluentd.cdn.cncf.io/6/windows/index.html).

![fluent-package installation wizard](https://1982584918-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LR7OsqPORtP86IQxs6E-694727794%2Fuploads%2Fgit-blob-849372e355d76b218db84900478246f2653422f0%2Ffluent-package6-wizard.png?alt=media)

### Step 2: Set up `fluentd.conf`

Open `C:/opt/fluent/etc/fluent/fluentd.conf` with a text editor. Replace the configuration with the following content:

```
<source>
  @type windows_eventlog2
  @id windows_eventlog2
  channels application
  read_existing_events false
  tag winevt.raw
  rate_limit 200
  <storage>
    @type local
    persistent true
    path C:\opt\fluent\winlog.json
  </storage>
</source>

<match winevt.raw>
  @type stdout
</match>
```

### Step 3: Launch Fluent Package Command Prompt with Administrator privilege

Open Windows Start menu, and search `Fluent Package Command Prompt`. In most environments, the program will be found right under the "Recently Added" section or "Best match" section.

![Windows start menu and Fluent Package Command Prompt](https://1982584918-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LR7OsqPORtP86IQxs6E-694727794%2Fuploads%2Fgit-blob-cc58f8a4d0e5d896acf81bcc7c00c77ee3459b4c%2Ffluent-package5-menu.png?alt=media\&token=e4da7e1e-f83f-447e-b323-e13ac7c2399f)

`Fluent Package Command Prompt` is basically `cmd.exe`, with a few PATH tweaks for Fluentd programs. Use this program whenever you need to interact with Fluentd.

### Step 4: Run `fluentd`

Type the following command into `Fluent Package Command Prompt` with Administrator privilege:

```
C:\opt\fluent> fluentd
```

Now `fluentd` starts listening to Windows Eventlog, and will print records to stdout as they occur.

![Fluent Package Command Prompt](https://1982584918-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LR7OsqPORtP86IQxs6E-694727794%2Fuploads%2Fgit-blob-6441f9dae6917556193d1dc54dca0e0c80294cf0%2Ffluent-package6-prompt.png?alt=media)

### Step 5: Run `fluentd` as Windows service

Fluentd is registered as a Windows service permanently by the msi installer. Since version 5.0.0, the service does not automatically start after installed. You must manually start it.

Choose one of your preferred way:

* Using GUI
* Using `net.ext`
* Using Powershell Cmdlet

#### Using GUI

Please guide yourself to `Control Panel -> System and Security -> Administrative Tools -> Services`, and you'll see `Fluentd Windows Service` is listed.

Please double click `Fluentd Window Service`, and click `Start` button. Then the process will be executed as Windows Service.

#### Using `net.exe`

```
> net start fluentdwinsvc
The Fluentd Windows Service service is starting..
The Fluentd Windows Service service was started successfully.
```

#### Using Powershell Cmdlet

```
PS> Start-Service fluentdwinsvc
```

Note that using `fluentdwinsvc` is needed to start Fluentd service from the command-line. `fluentdwinsvc` is the service name and it should be passed to `net.exe` or `Start-Service` Cmdlet.

The log file will be located at `C:/opt/fluent/fluentd.log` as we specified in Step 3.

### Step 6: Install Plugins

Open `Fluent Package Command Prompt` and use `fluent-gem` command:

```
C:\opt\fluent> fluent-gem install fluent-plugin-xyz --version=1.2.3
```

## Next Steps

You are now ready to collect real logs with Fluentd. Refer to the following tutorials on how to collect data from various sources:

* Basic Configuration
  * [Config File](https://docs.fluentd.org/configuration/config-file)
* Application Logs
  * [Ruby](https://docs.fluentd.org/language-bindings/ruby)
  * [Java](https://docs.fluentd.org/language-bindings/java)
  * [Python](https://docs.fluentd.org/language-bindings/python)
  * [PHP](https://docs.fluentd.org/language-bindings/php)
  * [Perl](https://docs.fluentd.org/language-bindings/perl)
  * [Node.js](https://docs.fluentd.org/language-bindings/nodejs)
  * [Scala](https://docs.fluentd.org/language-bindings/scala)
* Examples
  * [Store Apache Log into Amazon S3](https://docs.fluentd.org/how-to-guides/apache-to-s3)
  * [Store Apache Log into MongoDB](https://docs.fluentd.org/how-to-guides/apache-to-mongodb)
  * [Data Collection into HDFS](https://docs.fluentd.org/how-to-guides/http-to-hdfs)

{% hint style="info" %}
There are some commercial supports for Fluentd, see [Enterprise Services](https://www.fluentd.org/enterprise_services). If you use Fluentd on production, Let's share your use-case/testimonial on [Testimonials](https://www.fluentd.org/testimonials) page. Please consider to feedback via [GitHub](https://github.com/fluent/fluentd-website/issues/new?template=testimonials.yml).
{% endhint %}

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is an open-source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
