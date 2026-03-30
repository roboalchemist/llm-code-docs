# Source: https://docs.curator.interworks.com/setup/installation/linux_installation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Linux Installation

> Instructions for installing Curator on Linux.

The automated installer covers the vast majority of setups, but each server is different and may require
commands specific to your IT infrastructure.

## Installation Steps

If you are using one of the following Linux Operating Systems, follow our simple instruction steps to get started:

* Ubuntu
* CentOS
* RHEL

<Steps>
  <Step title="Run the Installation Script">
    SSH into your web server, ensure you're using a user that has full sudo access, and run the command below:

    ```bash  theme={null}
    curl -s -o curator.sh https://api.curator.interworks.com/scripts/linux_install.sh && chmod +x ./curator.sh && ./curator.sh
    ```
  </Step>

  <Step title="Retrieve Your Credentials">
    Locate your license key (sent from InterWorks) and open `/var/www/curator_info.txt` to retrieve your default
    administrator credentials.
  </Step>

  <Step title="Open the Installer">
    Open `http://curatorexample.com/install.php` in a browser - replacing `curatorexample.com` with your site's URL. If
    you're on the server you installed, you may also use `localhost`.

    *This may be an IP address or computer name until your IT team sets up DNS.*
  </Step>

  <Step title="Credentials">
    The installer will generate credentials for use during installation and will store them in a file in the installation
    directory (Default: `/var/www/curator_info.txt` or `C:\InterWorks\Curator\curator_info.txt` in Windows). You will need
    these credentials to complete the installation and to log in to the Curator backend after installation.
  </Step>

  <Step title="License Key">
    Enter your license key when prompted. If you do not have a license key, please contact InterWorks to obtain one.

        <img src="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/installation_enter_key.png?fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=f78214155c914ed84abf7a0cfbed9590" alt="License key prompt page" data-og-width="2880" width="2880" data-og-height="1800" height="1800" data-path="assets/images/snippets/installation_enter_key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/installation_enter_key.png?w=280&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=a038f0b5e19ba7f27f10f087bfc36617 280w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/installation_enter_key.png?w=560&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=a43cc98c58b2938445cecc7286314520 560w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/installation_enter_key.png?w=840&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=06a6e59aa1e66df53033cbd203ff53a7 840w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/installation_enter_key.png?w=1100&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=445020613ecc2bf6f2c0452e7ba404f5 1100w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/installation_enter_key.png?w=1650&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=59279cfeea99e4f57144c016e19a3a6d 1650w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/installation_enter_key.png?w=2500&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=0e63e628c90d7d9167cdb7999546efa4 2500w" />
  </Step>

  <Step title="Database Connection">
    You may be prompted to enter your database connection information if the installer is unable to automatically find the
    database for you.

        <img src="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/enter_database_credentials.png?fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=ac7b79590da93165c51793b36faffba2" alt="Database credentials prompt page" data-og-width="2880" width="2880" data-og-height="1800" height="1800" data-path="assets/images/snippets/enter_database_credentials.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/enter_database_credentials.png?w=280&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=e5e615ae58f9a8b398caade550f2249c 280w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/enter_database_credentials.png?w=560&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=2a0cdc565c6f768ba14caded166aaab5 560w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/enter_database_credentials.png?w=840&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=2b0363b31af1e9af44adb74cd2c316ff 840w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/enter_database_credentials.png?w=1100&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=8b3a7f03bf1e122221ccbe67dc8bae2b 1100w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/enter_database_credentials.png?w=1650&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=1b6a6c2ce5d6e8a520ae3ca999b75c0f 1650w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/enter_database_credentials.png?w=2500&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=be65e316d9c1d27dacd797afed0afaa8 2500w" />
  </Step>

  <Step title="Success">
    If the installation is successful, you will be redirected to your new Curator homepage

        <img src="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/post_install_homepage.png?fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=b4fac79de5100b4aa4b4e76c6c4c88fb" alt="Database credentials prompt page" data-og-width="2880" width="2880" data-og-height="1800" height="1800" data-path="assets/images/snippets/post_install_homepage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/post_install_homepage.png?w=280&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=71b2579f6586cd626ff09b7cb2ce875b 280w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/post_install_homepage.png?w=560&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=ccb029c3a1dc255d357e60aa50de2866 560w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/post_install_homepage.png?w=840&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=63065e8d1999fdbc16b8a32bc6db541d 840w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/post_install_homepage.png?w=1100&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=4b000d0905e26baabd2115e854d72891 1100w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/post_install_homepage.png?w=1650&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=52df8dad071b6be5a3f190316353310d 1650w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/post_install_homepage.png?w=2500&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=198c8d449d6b2b317581f4068a58ead1 2500w" />

    Using the same auto-generated credentials created in the install script above, you can log into the Curator backend which
    can be accessed from `http://curatorexample.com/backend`. If you're on the server you installed, you may also use localhost.
    Keep in mind this may be an IP address or computer name until your IT team sets up DNS.
  </Step>
</Steps>

## Custom Setup

The install script can take optional parameters to specify values for the installation script. This can be helpful in
distributed setups, or scripted installations.

```bash  theme={null}
curl -o curator.sh https://api.curator.interworks.com/scripts/linux_install.sh
chmod +x ./curator.sh
./curator.sh -f -h [database_host] -u [database_username] -p [database_password] -P [database_port] -d [database_name] -l [license_key] -s [persistent_storage_location] -v [curator_version]
```

Arguments:

* `-h` The database hostname *Needed when using an external database host*
* `-u` The database username  *`Default: curator`*
* `-p` The database password *Default: auto-generated password.  Use this when you need to use a connection to a
  database for a user that has already been created with a specific password.*
* `-P` The database port *`Default: 3306`*
* `-d` The database name *`Default: curator`*
* `-l` The License Key for your Curator installation. When performing a full installation, this is required.
* `-s` Path to a persistent storage location *Container-based or distributed installations typically require this.*
* `-v` Sets the version of Curator to install. *Default: most recent version.*

Options:

* `-f` Full Installation, this flag is required in most custom setups to avoid the in-browser installer.

## AWS EC2 Process

AWS provides a helpful outline on [how to connect to an AWS EC2 instance from Windows using Putty](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html).

## Network Whitelist Requirements

For installations in environments with restricted internet access or firewall configurations, the following URLs
should be whitelisted to ensure proper functionality:

### RHEL/CentOS Systems

* InterWorks API
  * `api.curator.interworks.com`
* EPEL Repository
  * `dl.fedoraproject.org`
  * `download.fedoraproject.org` (covers mirrors.fedoraproject.org)
* Remi Repository (PHP packages)
  * `*.remirepo.net` (covers rpms.remirepo.net, repo.remirepo.net, mirrors.remirepo.net)
* Base RHEL/CentOS Repositories
  * `*.centos.org` (covers vault.centos.org, mirror.centos.org)
  * `download.redhat.com`
  * `cdn.redhat.com`
* CDN Networks
  * `*.akamaiedge.net` (covers `*.akamaitechnologies.com` - same Akamai network)

### Ubuntu Systems

* InterWorks API
  * `api.curator.interworks.com`
* Ubuntu Repositories
  * `*.archive.ubuntu.com` (covers archive.ubuntu.com, us.archive.ubuntu.com, gb.archive.ubuntu.com, etc.)
  * `security.ubuntu.com`
  * `ports.ubuntu.com`
  * `changelogs.ubuntu.com`
* Launchpad PPAs (for ondrej/apache2 and ondrej/php)
  * `*.launchpad.net` (covers ppa.launchpad.net, launchpad.net)
  * `ppa.launchpadcontent.net`
  * `keyserver.ubuntu.com`
