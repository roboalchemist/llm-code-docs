# Source: https://help.aikido.dev/virtual-machine-scanning/local-vm-scanning/setting-up-the-local-vm-scanner-linux.md

# Setting Up the Local VM Scanner on Linux

Aikido VM Scanner is a single-package that installs on your system, automatically scanning and identifying dependencies to provide a detailed view into your environment.

### Prerequisites

* Minimum system requirements: at least 1GB RAM.
* Preferred system requirements: at least 2GB RAM and 4 CPUs.
* Ensure you have sudo / admin privileges on your system
* Make sure to use the appropriate commands for your system or cloud provider
* If you need to run with root, place the AIKIDO\_TOKEN env var after sudo, like this:\
  `sudo AIKIDO_TOKEN=REPLACE_ME <install_command>`

### Installation and Upgrade

Make sure you run as sudo and replace `AIKIDO_TOKEN` with [valid token from Local VM scanning page in Aikido](https://app.aikido.dev/settings/integrations/vm-scan-agent). To specify the VM environment (that you will see later in Aikido), you can also set the `VM_TYPE` variable as one of: `production`, `staging` or `development`.

The VM Scanner Agent runs once a day, at a random time between 4:00 AM - 8:00 AM (machine time).&#x20;

After install, **a first scan will start automatically**. If you want to run it on demand, you can manually execute:

```bash
/opt/aikido-vm-scanner-1.4.0/aikido-vm-scanner
```

#### **For Red Hat-based Systems (RHEL, CentOS, Fedora)**

**x86\_64**

```
AIKIDO_TOKEN=REPLACE_ME VM_TYPE=production dnf install -y https://aikido-vm-agent.s3.eu-west-1.amazonaws.com/v1.4.0/aikido-vm-scanner.x86_64.rpm
```

<table><thead><tr><th width="100.1015625">Hash</th><th>aikido-vm-scanner.x86_64.rpm</th></tr></thead><tbody><tr><td>MD5</td><td>9f1b2af00926fd90d8f91150f60ab1e7</td></tr><tr><td>SHA256</td><td>8d1b4d97adcd20f430f3d4272dffd9425346cf2721b6a072b75544f5f97f0572</td></tr></tbody></table>

**aarch64**

```
AIKIDO_TOKEN=REPLACE_ME VM_TYPE=production dnf install -y https://aikido-vm-agent.s3.eu-west-1.amazonaws.com/v1.4.0/aikido-vm-scanner.aarch64.rpm
```

<table><thead><tr><th width="99.953125">Hash</th><th>aikido-vm-scanner.aarch64.rpm</th></tr></thead><tbody><tr><td>MD5</td><td>82adac693c44ea844b5dfe8a5e55eef1</td></tr><tr><td>SHA256</td><td>7bd654999cc7f4dd0b72838a7ec8a6960baf6ebaa70e006e11580ba3a60158f7</td></tr></tbody></table>

#### **For Debian-based Systems (Debian, Ubuntu)**

{% hint style="warning" %}
We support Debian >= 10 and Ubuntu >= 20.04.
{% endhint %}

**x86\_64**

```
curl -L -O https://aikido-vm-agent.s3.eu-west-1.amazonaws.com/v1.4.0/aikido-vm-scanner.amd64.deb
AIKIDO_TOKEN=REPLACE_ME VM_TYPE=production apt-get install -y ./aikido-vm-scanner.amd64.deb
```

<table><thead><tr><th width="100.36328125">Hash</th><th>aikido-vm-scanner.amd64.deb</th></tr></thead><tbody><tr><td>MD5</td><td>a46a60934fa4c8788c1ff8ea7101e37a</td></tr><tr><td>SHA256</td><td>da67a0734ce252ed2752883bb7276dff015111523d72496fa044fb7cc770e36d</td></tr></tbody></table>

**aarch64**

```
curl -L -O https://aikido-vm-agent.s3.eu-west-1.amazonaws.com/v1.4.0/aikido-vm-scanner.arm64.deb
AIKIDO_TOKEN=REPLACE_ME VM_TYPE=production apt-get install -y ./aikido-vm-scanner.arm64.deb
```

<table><thead><tr><th width="100.19921875">Hash</th><th>aikido-vm-scanner.arm64.deb</th></tr></thead><tbody><tr><td>MD5</td><td>5acd8dcde8efa941acc2095de6e5723e</td></tr><tr><td>SHA256</td><td>a4641dfc2d0fe8807af6903ae4484cfc093f63e97d9abfbebc9e4d52516889a9</td></tr></tbody></table>

### Latest version

If you have an automated install process and you always want to be on the latest version as soon as we release it, you can replace the version in the install link with `latest`:

* <https://aikido-vm-agent.s3.eu-west-1.amazonaws.com/latest/aikido-vm-scanner.x86\\_64.rpm>
* <https://aikido-vm-agent.s3.eu-west-1.amazonaws.com/latest/aikido-vm-scanner.aarch64.rpm>
* <https://aikido-vm-agent.s3.eu-west-1.amazonaws.com/latest/aikido-vm-scanner.amd64.deb>
* <https://aikido-vm-agent.s3.eu-west-1.amazonaws.com/latest/aikido-vm-scanner.arm64.deb>

### Additional Configuration

#### Token setup

If for any reason you can't set the AIKIDO\_TOKEN at install time, you can set the token post install in one of two ways:

* Paste the token in `/opt/aikido-vm-scanner-1.4.0/.token`&#x20;
* Change the contents of `/opt/aikido-vm-scanner-1.4.0/config.json` :

```
{
    "api_key": "AIKIDO_TOKEN_HERE",
    "exclude": []
}
```

#### Hostname change

By default, we automatically get the hostname for the scanned machine and submit that to Aikido, in order to be displayed in the Virtual Machines tab.

If you want to change the reported hostname, you can do that using the configuration file:

```
{
    "hostname": "YOUR_HOSTNAME_HERE",
    "exclude": []
}
```

#### Exclude files or paths

In the config.json you can exclude files and paths by adding additional items to the exclude list. You can find some examples below.

* Exclude a single file in a directory:

```
{
    "exclude": [
        ...
        "./home/testing/app/package.json",
    ]
}
```

* Exclude all releases subdirectories:

```
{
    "exclude": [
            ...
            "./home/testing/*/releases",
    ]
}
```

* Exclude all .json files in the out folder and all subdirectories:

```
{
    "exclude": [
        ...
        "./out/**/*.json",
    ]
}
```

* Exclude catalogers from scanning (eg: exclude Golang catalogers):

```
{
    "exclude": [
    ],
    "select_catalogers": "-go"
}
```

#### Output channel

If you want to control the output channel of the VM scanner, when installing you can specify the OUTPUT variable as `stdout`, `stderr` or `none`.

Example for rpm x86\_64:

```
AIKIDO_TOKEN=REPLACE_ME VM_TYPE=production OUTPUT=stderr dnf install -y https://aikido-vm-agent.s3.eu-west-1.amazonaws.com/v1.4.0/aikido-vm-scanner.x86_64.rpm
```

{% hint style="info" %}
This option does not affect the disk logs. These are created no matter what this setting is.
{% endhint %}

#### Disable initial scan

When a rpm/deb package is installed, it automatically triggers an initial scan.\
If you want to disable this feature, you can set the `INITIAL_SCAN` parameter to 0 at install time, like this:

```
AIKIDO_TOKEN=REPLACE_ME INITIAL_SCAN=0 dnf install -y https://aikido-vm-agent.s3.eu-west-1.amazonaws.com/v1.4.0/aikido-vm-scanner.x86_64.rpm
```

#### CLI parameters

If for any reason you need to start the scanning on demand via the command line, you can specify the following CLI parameters to be used for that scan:

```
  --api-key string
        API key for authentication
  --hostname string
        Hostname of the machine
  --select-catalogers string
        Comma-separated list of catalogers to use or remove
  --vm-type string
        Type of the virtual machine
```

These CLI parameters take precedence over those specified in config.json.

{% hint style="warning" %}
We trigger an automatic scan once per day and those scans will still use the configuration file and not the CLI parameters, so it is always preferred to place these in config.json.
{% endhint %}

* Example for setting a custom hostname via CLI:

```
/opt/aikido-vm-scanner-1.4.0/aikido-vm-scanner --hostname "My Custom VM"
```

* Example for excluding Golang catalogers via CLI:

```
/opt/aikido-vm-scanner-1.4.0/aikido-vm-scanner --select-catalogers "-go"
```

### Uninstall

#### Manual uninstall

**For Red Hat-based Systems (RHEL, CentOS, Fedora)**

```
dnf remove -y aikido-vm-scanner
```

**For Debian-based Systems (Debian, Ubuntu)**

```
apt-get remove -y aikido-vm-scanner
```

### Logs

Logs are available here, along with the last generated SBOM: `/var/log/aikido-vm-scanner-1.4.0`
