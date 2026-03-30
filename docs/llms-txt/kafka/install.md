# Source: https://docs.confluent.io/confluent-cli/current/install.md

<a id="cli-install"></a>

# Install Confluent CLI

This topic describes how to install the Confluent CLI on macOS, Linux, and
Windows. It also includes [other installation methods](#other-cli-install-methods) you can use to install the CLI. Before you install,
verify you [meet all requirements](overview.md#cli-requirements).

### Homebrew

macOS and Linux users can install the latest version of Confluent CLI using
the following [Homebrew](https://brew.sh/) command:

```text
brew install confluentinc/tap/cli
```

### APT

If you are a Debian or Ubuntu user, you can install the latest version of
Confluent CLI using the APT package manager:

1. Install `curl` and `gpg` (if you have not already installed them).
   ```shell
   sudo apt install curl gnupg
   ```
2. Install the Confluent CLI APT public key:
   ```shell
   sudo mkdir -p /etc/apt/keyrings
   curl https://packages.confluent.io/confluent-cli/deb/archive.key | sudo gpg --dearmor -o /etc/apt/keyrings/confluent-cli.gpg
   sudo chmod go+r /etc/apt/keyrings/confluent-cli.gpg
   ```

   You should see output similar to the following:
   ```text
   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                       Dload  Upload   Total   Spent    Left  Speed
   100  3106  100  3106    0     0  16062      0 --:--:-- --:--:-- --:--:-- 16010
   ```
3. Add the Confluent CLI repository to your APT configuration:
   ```shell
   echo "deb [signed-by=/etc/apt/keyrings/confluent-cli.gpg] https://packages.confluent.io/confluent-cli/deb stable main" | sudo tee /etc/apt/sources.list.d/confluent-cli.list >/dev/null
   ```
4. Update `apt`:
   ```bash
   sudo apt update
   ```
5. Install the Confluent CLI:
   ```bash
   sudo apt install confluent-cli
   ```

   You should see output similar to:
   ```text
   ...
   The following NEW packages will be installed:
   confluent-cli
   0 upgraded, 1 newly installed, 0 to remove and 41 not upgraded.
   Need to get 19.3 MB of archives.
   After this operation, 56.2 MB of additional disk space will be used.
   Get:1 https://packages.confluent.io/confluent-cli/deb stable/main amd64 confluent-cli amd64 3.48.0 [19.3 MB]
   ...
   Unpacking confluent-cli (3.48.0) ...
   Setting up confluent-cli (3.48.0) ...
   ```

**Confluent Platform**

If you installed Confluent Platform using APT, you should already have a version of the
Confluent CLI. In most cases, Confluent Platform users should use the version of
Confluent CLI provided with Confluent Platform. However, you can still install the latest
version of the Confluent CLI from the CLI repository by using the following
steps:

1. Install `curl` and `gpg` (if you have not already installed them).
   ```shell
   sudo apt install curl gnupg
   ```
2. Install the Confluent CLI APT public key:
   ```shell
   sudo mkdir -p /etc/apt/keyrings
   curl https://packages.confluent.io/confluent-cli/deb/archive.key | sudo gpg --dearmor -o /etc/apt/keyrings/confluent-cli.gpg
   sudo chmod go+r /etc/apt/keyrings/confluent-cli.gpg
   ```

   You should see output similar to the following:
   ```text
    % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                        Dload  Upload   Total   Spent    Left  Speed
    100  3106  100  3106    0     0  16062      0 --:--:-- --:--:-- --:--:-- 16010
   ```
3. Add the Confluent CLI repository to your APT configuration:
   ```shell
   echo "deb [signed-by=/etc/apt/keyrings/confluent-cli.gpg] https://packages.confluent.io/confluent-cli/deb stable main" | sudo tee /etc/apt/sources.list.d/confluent-cli.list >/dev/null
   ```
4. Update `apt`:
   ```bash
   sudo apt update
   ```
5. Install the latest version of the Confluent CLI. A specific version must be
   provided; if not, APT will install the CLI provided by Confluent Platform that uses the Confluent Platform
   version number (which is not considered to be latest CLI version by APT).
   ```bash
   sudo apt install confluent-cli=3.48.0
   ```

   To find the current latest version, you can run the following commands:
   `sudo apt update` and `sudo apt list -a confluent-cli` and look for
   the highest version number earlier than `7.x` or refer to the [Confluent CLI Release
   Notes](https://docs.confluent.io/confluent-cli/current/release-notes.html).

#### NOTE
Updating the CLI through APT, or installing Confluent Platform through APT will cause this
version of the CLI to be replaced with the version provided by Confluent Platform.

### YUM

RHEL and CentOS users can install the latest version of Confluent CLI using
the YUM package manager.

1. Install the Confluent CLI YUM public key:
   ```bash
   sudo rpm --import https://packages.confluent.io/confluent-cli/rpm/archive.key
   ```
2. Install `yum-config-manager` (included in the `yum-utils` package) if it
   is not already installed:
   ```bash
   sudo yum install yum-utils
   ```
3. Add the Confluent CLI repository to your YUM configuration:
   ```bash
   yum-config-manager --add-repo https://packages.confluent.io/confluent-cli/rpm/confluent-cli.repo
   ```

   You should see output similar to:
   ```text
   Loaded plugins: fastestmirror, ovl
   adding repo from: https://packages.confluent.io/confluent-cli/rpm/confluent-cli.repo
   grabbing file https://packages.confluent.io/confluent-cli/rpm/confluent-cli.repo to /etc/yum.repos.d/confluent-cli.repo
   repo saved to /etc/yum.repos.d/confluent-cli.repo
   ```
4. Clear the YUM caches:
   ```bash
   sudo yum clean all
   ```

   You should see output similar to:
   ```text
   Loaded plugins: fastestmirror, ovl
   Cleaning repos: Confluent-CLI base endpoint extras updates
   Cleaning up list of fastest mirrors
   ```
5. Install the Confluent CLI:
   ```bash
   sudo yum install confluent-cli
   ```

   You should see output similar to:
   ```text
   Loaded plugins: fastestmirror, ovl
   Determining fastest mirrors
   * base: centos-distro.1gservers.com
   * extras: mirror.keystealth.org
   * updates: mirrors.unifiedlayer.com
   Confluent-CLI
   base
   endpoint
   extras
   updates
   (1/6): base/7/x86_64/group_gz
   (2/6): extras/7/x86_64/primary_db
   (3/6): Confluent-CLI/primary_db
   (4/6): endpoint/7/x86_64/primary_db
   (5/6): base/7/x86_64/primary_db
   (6/6): updates/7/x86_64/primary_db
   Resolving Dependencies
   --> Running transaction check
   ---> Package confluent-cli.x86_64 0:3.48.0-1 will be installed
   --> Finished Dependency Resolution

   Dependencies Resolved

   ========================================================================================================================================================================================================================
   Package                                                      Arch                           Version                            Repository                                               Size
   ========================================================================================================================================================================================================================
   Installing:
   confluent-cli                                                x86_64                         3.48.0-1                           Confluent-CLI                                            19 M

   Transaction Summary
   ========================================================================================================================================================================================================================
   Install  1 Package

   Total download size: 19 M
   Installed size: 54 M
   Is this ok [y/d/N]: y
   Downloading packages:
   confluent-cli-3.48.0-1.x86_64.rpm
   Running transaction check
   Running transaction test
   Transaction test succeeded
   Running transaction
   Verifying  : confluent-cli-3.48.0-1.x86_64

   Installed:
   confluent-cli.x86_64 0:3.48.0-1

   Complete!
   ```

**Confluent Platform**

If you installed Confluent Platform using YUM, you should already have a version of the
Confluent CLI. In most cases, Confluent Platform users should use the version of
Confluent CLI provided with Confluent Platform. However, if you want to install the latest
version of the Confluent CLI from the CLI repository, you can use the
following steps:

1. Install the Confluent CLI YUM public key:
   ```text
   sudo rpm --import https://packages.confluent.io/confluent-cli/rpm/archive.key
   ```
2. Add the Confluent CLI repository to your YUM configuration:
   ```text
   yum-config-manager --add-repo https://packages.confluent.io/confluent-cli/rpm/confluent-cli.repo
   ```
3. Uninstall the existing version of the Confluent CLI. This will also
   uninstall `confluent-platform`, but not the individual packages included
   with Confluent Platform:
   ```bash
   sudo yum remove confluent-cli
   ```

   You should see output similar to:
   ```text
   Loaded plugins: fastestmirror, ovl
   Resolving Dependencies
   --> Running transaction check
   ---> Package confluent-cli.x86_64 0:7.5.3-1 will be erased
   --> Processing Dependency: confluent-cli = 7.5.3 for package: confluent-platform-7.5.3-1.noarch
   --> Running transaction check
   ---> Package confluent-platform.noarch 0:7.5.3-1 will be erased
   --> Finished Dependency Resolution

   Dependencies Resolved

   =============================================================================================================================================================================================================
   Package                                                        Arch                          Version                                 Repository                                Size
   =============================================================================================================================================================================================================
   Removing:
   confluent-cli                                                  x86_64                        7.5.3-1                                 @Confluent                                208 M
   Removing for dependencies:
   confluent-platform                                             noarch                        7.5.3-1                                 @Confluent                                0.0

   Transaction Summary
   =============================================================================================================================================================================================================
   Remove  1 Package (+1 Dependent package)

   Installed size: 208 M
   Is this ok [y/N]: y
   Downloading packages:
   Running transaction check
   Running transaction test
   Transaction test succeeded
   Running transaction
   Erasing    : confluent-platform-7.5.3-1.noarch
   Erasing    : confluent-cli-7.5.3-1.x86_64
   Verifying  : confluent-platform-7.5.3-1.noarch
   Verifying  : confluent-cli-7.5.3-1.x86_64

   Removed:
   confluent-cli.x86_64 0:7.5.3-1

   Dependency Removed:
   confluent-platform.noarch 0:7.5.3-1

   Complete!
   ```
4. Clear the YUM caches:
   ```text
   sudo yum clean all
   ```

   You should see output similar to:
   ```text
   Loaded plugins: fastestmirror, ovl
   Cleaning repos: Confluent-CLI base endpoint extras updates
   Cleaning up list of fastest mirrors
   ...
   ```
5. Temporarily disable the Confluent Platform repository:
   ```text
   sudo yum --disablerepo=Confluent install confluent-cli
   ```

   This command assumes that users have added the Confluent Platform repository using the
   `confluent.repo` file provided in [Install Confluent Platform using Systemd
   on RHEL and CentOS](https://docs.confluent.io/platform/current/installation/installing_cp/rhel-centos.html#install-cp-using-systemd-on-rhel-and-centos).
   If you who have modified the repository ID, you must provide the ID as the
   argument to `--disablerepo` in place of `Confluent` in the previous step.
   You can view repository IDs and names using `yum repolist all`.

#### NOTE
Updating the CLI through YUM, or installing Confluent Platform through YUM will cause this
version of the CLI to be replaced with the version provided by Confluent Platform.

### Windows

To install the Confluent CLI on Windows, complete the following
steps:

1. Download the latest Windows ZIP file from
   `https://github.com/confluentinc/cli/releases/latest`.
2. Unzip the following file:
   ```bash
   confluent_X.X.X_windows_amd64.zip
   ```
3. Run `confluent.exe`.

<a id="other-cli-install-methods"></a>

## Other installation methods

This section includes other methods you can use to install the Confluent CLI.

### Docker

To install the Confluent CLI on Docker Desktop, run the following command to
pull the latest CLI version:

```bash
docker pull confluentinc/confluent-cli:latest
```

You can also install a specific version:

```bash
docker pull confluentinc/confluent-cli:<version>
```

<a id="confluent-cli-install-with-cp"></a>

### Confluent Platform installation package

Confluent Platform installation packages include the Confluent CLI binaries for each of the
operating system and architecture types that the Confluent CLI supports.

Confluent Community software users must download the Confluent CLI
separately and configure it manually.

To use the Confluent CLI in the Confluent Platform package:

1. Set the Confluent Platform home environment variable:
   ```bash
   export CONFLUENT_HOME=<The directory where Confluent is installed>
   ```
2. Add the location of the CLI to the `PATH`:
   ```bash
   export PATH=$CONFLUENT_HOME/bin:$PATH
   ```

<a id="confluent-cli-version-install"></a>

#### Install alternative version in Confluent Platform package

The version of the Confluent CLI used by Confluent Platform can be changed by downloading a
specific Confluent CLI binary and using it to replace the current binary.

When you download and install the Confluent CLI outside of the Confluent Platform package,
ensure you install a Confluent CLI version that is compatible with the version
of Confluent Platform you are running. For reference, see the [Confluent CLI to Confluent Platform compatibility table](/platform/current/installation/versions-interoperability.html#confluent-cli-cp-compatibility).

1. Download the appropriate version of the Confluent CLI.
2. Use the downloaded binary to replace the existing Confluent CLI binary
   located in subdirectories of `$CONFLUENT_HOME/libexec/cli/`.

   For example, on macOS, which is the `darwin` operating system type and
   `amd64` architecture type:
   ```bash
   cp <cli binaries> $CONFLUENT_HOME/libexec/cli/darwin_amd64/
   ```

<a id="confluent-cli-bundle-install"></a>

### Tarball or ZIP installation

1. Download and install the most recently released CLI binaries for your
   platform:
   - [macOS with 64-bit Intel chips (Darwin AMD64)](https://packages.confluent.io/confluent-cli/archives/latest/confluent_darwin_amd64.tar.gz)
   - [macOS with Apple chips (Darwin ARM64)](https://packages.confluent.io/confluent-cli/archives/latest/confluent_darwin_arm64.tar.gz)
   - [Windows with 64-bit Intel or AMD chips (Windows AMD64)](https://packages.confluent.io/confluent-cli/archives/latest/confluent_windows_amd64.zip)
   - [Linux with 64-bit Intel or AMD chips (Linux AMD64) (glibc)](https://packages.confluent.io/confluent-cli/archives/latest/confluent_linux_amd64.tar.gz)
   - [Linux with 64-bit ARM chips (Linux ARM64) (glibc)](https://packages.confluent.io/confluent-cli/archives/latest/confluent_linux_arm64.tar.gz)
   - [Alpine with 64-bit Intel or AMD chips (Alpine AMD64) (musl)](https://packages.confluent.io/confluent-cli/archives/latest/confluent_alpine_amd64.tar.gz)
   - [Alpine with 64-bit ARM chips (Alpine ARM64) (musl)](https://packages.confluent.io/confluent-cli/archives/latest/confluent_alpine_arm64.tar.gz)
   - [Checksums (operating system agnostic)](https://packages.confluent.io/confluent-cli/archives/latest/confluent_checksums.txt)
2. Set the `PATH` environment to include the directory that you downloaded the
   CLI binaries in the previous step:
   ```bash
   export PATH=<path-to-cli>:$PATH
   ```
3. Optionally, if you do not have enough space in the default directory that
   CLI stores logs and data, set the `CONFLUENT_CURRENT` environment variable
   to use a different directory:
   ```bash
   export CONFLUENT_CURRENT=<path-to-confluent-local-data>
   ```

## Verify

You can confirm the version and the operating system (OS) type of the CLI with the following
command:

```text
confluent version
```

The output of this command will vary depending on your version and OS type. For example, on macOS, the output will resemble the following:

```text
confluent - Confluent CLI

Version:     v4.43.0
Git Ref:     14b42e02
Build Date:  2025-10-24T21:09:49Z
Go Version:  go1.24.6 (darwin/arm64)
Development: false
```

<a id="cli-upgrade-instructions"></a>

## Upgrade

Use the `confluent update` command to upgrade from an earlier version of the
Confluent CLI to a newer version. For the full syntax, see [confluent update](command-reference/confluent_update.md#confluent-update).

To ensure compatibility, updates using the `confluent update` command are
disabled for the CLI packaged with Confluent Platform. If you need to upgrade to a later
version of the CLI, see [Install alternative version in Confluent Platform package](#confluent-cli-version-install).

## Uninstall

Methods for uninstalling the Confluent CLI vary depending on your operating system and installation method
(package manager or a direct binary download).

### macOS

If you used Homebrew on macOS to install the CLI, you can remove it using the standard uninstall command:

```bash
brew uninstall confluentinc/tap/cli
```

### APT or YUM

If installed with a Linux (APT/YUM) package manager, the uninstall process will vary depending on the OS and package manager you used.
For installations done through the Confluent repository, use your systemâs package manager.

- Ubuntu/Debian (APT):
  ```bash
  sudo apt-get remove confluent-cli
  # To remove unused dependencies as well:
  sudo apt-get autoremove
  ```
- RHEL/CentOS/Fedora (YUM/DNF):
  ```bash
  sudo yum remove confluent-cli
  ```

  Or (for Fedora)
  ```bash
  sudo dnf remove confluent-cli
  ```

### Script or Binary (Manual install)

If you installed the CLI using the curl script or by downloading the binary manually, you simply need to delete the binary and its configuration directory.

1. Locate and remove the binary: Find where the binary is located (usually `/usr/local/bin` or a local bin folder) and delete it.
   ```bash
   which confluent
   # This will show you the path, e.g., /usr/local/bin/confluent
   rm /usr/local/bin/confluent
   ```
2. Remove the configuration directory:
   ```bash
   rm -rf ~/.confluent/
   ```

If you installed the CLI as part of Confluent Platform, you should uninstall the platform package itself:

- Ubuntu:
  ```bash
  sudo apt-get remove confluent-platform
  ```
- RHEL:
  ```bash
  sudo yum remove confluent-platform
  ```
- Fedora:
  ```bash
  sudo dnf remove confluent-platform
  ```

### Windows

If you installed the CLI using the Windows native installer, do the following to uninstall it:

1. Delete the executable.

   Since you manually unzipped the file, simply locate the `confluent.exe` file and delete it.
   Check your Downloads folder or wherever you extracted the ZIP.
   If you moved `confluent.exe` to a permanent folder (like `C:\tools` or `C:\bin`), delete it from there.
2. Remove the CLI Configuration (required).

   The CLI creates a hidden folder to store your login sessions, environments, and cluster metadata. Even if you delete the `confluent.exe`, these files stay on your hard drive.
   1. Open File Explorer.
   2. In the address bar, paste: `%USERPROFILE%` and hit Enter.
   3. Find the folder named `.confluent`, and delete it.
3. Clean up the System Path.

   If you followed common practices, you likely added the folder containing `confluent.exe` to your Windows `Path` so you could run it from any terminal.
   You should remove this to keep your system clean.
   1. Press the Windows Key and type `env`.
   2. Select Edit the system environment variables.
   3. Click the **Environment Variables** button at the bottom right.
   4. In the User variables section (top half), find the variable named **Path** and click **Edit**.
   5. Look for the folder path where you unzipped the Confluent CLI.
   6. Select that line and click **Delete**.
   7. Click **OK** on all windows to save.
4. Verify itâs uninstalled.

   Open a new command prompt or PowerShell window (the changes wonât show in an already open window) and type:
   ```bash
   confluent version
   ```

   If the CLI is uninstalled correctly, you should see an error message similar to:
   ```text
   'confluent' is not recognized as an internal or external command...
   ```

## Confluent Platform properties files

The following list includes the default Confluent Platform services configuration properties
files, where `$CONFLUENT_HOME` is the directory where you installed Confluent Platform. You
reference or modify the appropriate file when you work with a Confluent Platform service.

- Connect: `$CONFLUENT_HOME/etc/schema-registry/connect-avro-distributed.properties`
- Control Center:  `$C3_HOME/etc/confluent-control-center/control-center-dev.properties` <sup>[1](#f1)</sup>
- KRaft Controller: `$CONFLUENT_HOME/etc/kafka/controller.properties`
- Kafka (KRaft mode): `$CONFLUENT_HOME/etc/kafka/broker.properties`
- Kafka (ZooKeeper mode, Legacy): `$CONFLUENT_HOME/etc/kafka/server.properties`
- REST Proxy: `$CONFLUENT_HOME/etc/kafka-rest/kafka-rest.properties`
- ksqlDB: `$CONFLUENT_HOME/etc/ksqldb/ksql-server.properties`
- Schema Registry: `$CONFLUENT_HOME/etc/schema-registry/schema-registry.properties`
- ZooKeeper: `$CONFLUENT_HOME/etc/kafka/zookeeper.properties`

* <a id='f1'>**[1]**</a> Starting with Confluent Platform 8.0, Control Center is provided in an independent release, as described in [Control Center single-node manual installation](/control-center/current/installation/overview.html#single-node-manual-installation), and the Control Center examples in this tutorial: [Getting Started with a multi-broker cluster](/platform/current/get-started/tutorial-multi-broker.html#optional-install-and-configure-c3). In previous versions of Confluent Platform, this path was `$CONFLUENT_HOME/etc/confluent-control-center/control-center-dev.properties`.
