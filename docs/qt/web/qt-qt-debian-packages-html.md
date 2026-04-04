# Source: https://doc.qt.io/qt/qt-debian-packages.html

Title: Enterprise Qt Debian Packages | Qt 6.10

URL Source: https://doc.qt.io/qt/qt-debian-packages.html

Markdown Content:
To use Enterprise Debian packages with Qt, add your enterprise repositories to Advanced Packaging Tool (APT). For details, see [Debian Repository Configuration Format](https://doc.qt.io/qt-6/qt-debian-packages.html#debian-repository-configuration-format).

To use the enterprise repositories, you need to:

* [Install a public GPG key](https://doc.qt.io/qt-6/qt-debian-packages.html#installing-a-public-gpg-key) for enterprise repositories
* [Configure Qt Account based authentication](https://doc.qt.io/qt-6/qt-debian-packages.html#configuring-authentication) for enterprise repository access
* [Configure repositories](https://doc.qt.io/qt-6/qt-debian-packages.html#full-configuration-example)

Debian Repository Configuration Format[](https://doc.qt.io/qt/qt-debian-packages.html#debian-repository-configuration-format "Direct link to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------

To add extra repositories for APT, insert repositories into a file with an extension of _.list_ under the _/etc/apt/sources.list.d_ directory. For each repository, add a new entry in the file. The generic format is as follows:

deb [arch=<arch> signed-by=<path>] <REPO_URL> <DIST> <COMPONENT(s)>

An example of an enterprise repository entry:

$ sudo nano /etc/apt/sources.list.d/tqtc.list

    deb [arch=arm64 signed-by=/etc/apt/keyrings/tqtc/qt-company-debian-repo.gpg] https://debian-packages.qt.io/debian/enterprise/qt-6.10.2-arm64 tqtc-jammy main

See [Repository information for Qt Releases](https://doc.qt.io/qt-6/qt-debian-packages.html#repository-information-for-qt-releases) for detailed information on how you can configure repositories per Qt release and architecture.

Debian Source Packages[](https://doc.qt.io/qt/qt-debian-packages.html#debian-source-packages "Direct link to this headline")
----------------------------------------------------------------------------------------------------------------------------

To add the Debian source packages for APT, you need to add a _deb-src_ entry for the corresponding _deb_ entry:

$ sudo nano /etc/apt/sources.list.d/tqtc.list

    deb [arch=arm64 signed-by=/etc/apt/keyrings/tqtc/qt-company-debian-repo.gpg] https://debian-packages.qt.io/debian/enterprise/qt-6.10.2-arm64 tqtc-jammy main
    deb-src [signed-by=/etc/apt/keyrings/tqtc/qt-company-debian-repo.gpg] https://debian-packages.qt.io/debian/enterprise/qt-6.10.2-arm64 tqtc-jammy main

To download source packages (for example, for _wayland_) to the current directory, use the `apt source` command:

$ sudo apt source qt-6.10.2-wayland-src

Installing a Public GPG Key[](https://doc.qt.io/qt/qt-debian-packages.html#installing-a-public-gpg-key "Direct link to this headline")
--------------------------------------------------------------------------------------------------------------------------------------

Install a public GPG (GNU Privacy Guard) key for Enterprise Qt Debian repositories as follows:

$ sudo mkdir -p /etc/apt/keyrings/tqtc  # Create the directory with appropriate permissions
$ cd /etc/apt/keyrings/tqtc
$ sudo wget https://cdn.qt.io/debian/keys/qt-company-debian-repo.gpg

Configuring Authentication[](https://doc.qt.io/qt/qt-debian-packages.html#configuring-authentication "Direct link to this headline")
------------------------------------------------------------------------------------------------------------------------------------

To access the listed repositories, you need an enterprise Qt Account or an evaluation Qt Account.

**Note:**If your password contains special characters, you may need to escape those by using **'\'** or **'%40'**.

Configure the Qt Account credentials for your APT package manager as follows:

$ sudo nano /etc/apt/auth.conf

      machine https://debian-packages.qt.io
      login <Qt Account login name (email)>
      password <Qt Account password>

**Warning:**This file may contain sensitive information. To prevent other users on the system from reading the password, make sure the file has strict permissions:

$ sudo chmod 600 /etc/apt/auth.conf

Updating Local Package Cache[](https://doc.qt.io/qt/qt-debian-packages.html#updating-local-package-cache "Direct link to this headline")
----------------------------------------------------------------------------------------------------------------------------------------

Update the local package cache as follows:

$ sudo apt-get update

No errors should originate from the added repository in the output.

Debian Alias Packages[](https://doc.qt.io/qt/qt-debian-packages.html#debian-alias-packages "Direct link to this headline")
--------------------------------------------------------------------------------------------------------------------------

You can install the content more easily with alias packages, which are just meta-packages pointing to the actual Debian packages.

The contents of the Debian alias packages are listed in the table below.

**Note:**Qt 6.10.2 release is used in the alias package examples listed below. Always remember to use the packages that match the Qt release you are working on. For more information, see [Repository information for Qt Releases](https://doc.qt.io/qt-6/qt-debian-packages.html#repository-information-for-qt-releases).

| Alias package name | Package content |
| --- | --- |
| qt6.10.2-essentials | *[essential module libraries](https://doc.qt.io/qt-6/qtmodules.html#qt-essentials)* essential module runtime tools |
| qt6.10.2-essentials-dev | *[essential module libraries](https://doc.qt.io/qt-6/qtmodules.html#qt-essentials)* essential module headers *essential module private headers* essential module runtime tools * essential module development tools |
| qt6.10.2-full | *[essential module libraries](https://doc.qt.io/qt-6/qtmodules.html#qt-essentials)* essential module runtime tools *[add-on module libraries](https://doc.qt.io/qt-6/qtmodules.html#qt-add-ons)* add-on module runtime tools |
| qt6.10.2-full-dev | *all module libraries* all module headers *all module private headers* all module runtime tools * all module development tools |
| qt6.10.2-full-dbg | *all module debug libraries* [essential module libraries](https://doc.qt.io/qt-6/qtmodules.html#qt-essentials) * [add-on module libraries](https://doc.qt.io/qt-6/qtmodules.html#qt-add-ons) |

**Debian Installation Command Example**

$ sudo apt install qt6.10.2-full-dev

Full Configuration Example[](https://doc.qt.io/qt/qt-debian-packages.html#full-configuration-example "Direct link to this headline")
------------------------------------------------------------------------------------------------------------------------------------

The following code snippet demonstrates the whole work flow with Enterprise Qt Debian packages:

# install repository key

 $ sudo mkdir -p /etc/apt/keyrings/tqtc
 $ cd /etc/apt/keyrings/tqtc
 $ sudo wget https://cdn.qt.io/debian/keys/qt-company-debian-repo.gpg

# configure Qt Account based authentication to Qt Debian repositories

 $ sudo nano /etc/apt/auth.conf
   machine https://debian-packages.qt.io
   login <your Qt Account email>
   password <your Qt Account password>

# add repositories

 $ sudo nano /etc/apt/sources.list.d/tqtc.list
     deb [arch=arm64 signed-by=/etc/apt/keyrings/tqtc/qt-company-debian-repo.gpg] https://debian-packages.qt.io/debian/enterprise/qt6.10.2-arm64 tqtc-jammy main

# add source packages

 $ sudo nano /etc/apt/sources.list.d/tqtc.list
     deb-src [signed-by=/etc/apt/keyrings/tqtc/qt-company-debian-repo.gpg] https://debian-packages.qt.io/debian/enterprise/qt-6.10.2-arm64 tqtc-jammy main

# update local package cache

 $ sudo apt-get update

# search and install packages

 $ apt-cache search qt6.10.2-full-dev
 ....
 ....

# files are installed under /opt/qt-6.10.2

$ sudo apt install qt6.10.2-full-dev

See [Repository information for Qt Releases](https://doc.qt.io/qt-6/qt-debian-packages.html#repository-information-for-qt-releases) to pick the needed repositories into your _/etc/apt/sources.list.d/tqtc.list_ file.

Troubleshooting[](https://doc.qt.io/qt/qt-debian-packages.html#troubleshooting "Direct link to this headline")
--------------------------------------------------------------------------------------------------------------

### Difficulties in authentication[](https://doc.qt.io/qt/qt-debian-packages.html#difficulties-in-authentication "Direct link to this headline")

The server may response with the following HTTP error codes:

Wrong credentials. User email and password must be provided in correct format.

Also, try storing the credentials directly into the repository config:

deb [...] https://<Qt Account email>:<Qt Account passwd>@https://debian-packages.qt.io/.....

If your password contains special characters, you may need to escape those for APT. Use '' or '%40' for escaping those characters or try changing your Qt Account password.

#### 403 Forbidden[](https://doc.qt.io/qt/qt-debian-packages.html#403-forbidden "Direct link to this headline")

Missing credentials.

#### 429 Too Many Requests[](https://doc.qt.io/qt/qt-debian-packages.html#429-too-many-requests "Direct link to this headline")

User has sent too much **failed** requests (3 requests per minute).

#### 500 Internal Server Error[](https://doc.qt.io/qt/qt-debian-packages.html#500-internal-server-error "Direct link to this headline")

Contact [Qt support](https://www.qt.io/contact-us).

### Difficulties with repository GPG key usage[](https://doc.qt.io/qt/qt-debian-packages.html#difficulties-with-repository-gpg-key-usage "Direct link to this headline")

An alternative to the `signed-by` usage attribute in the repository config is to install the key in the following way, although this is not recommended as it's a deprecated way to install it:

$ sudo apt-key add qt-company-debian-repo.gpg

Repository information for Qt Releases[](https://doc.qt.io/qt/qt-debian-packages.html#repository-information-for-qt-releases "Direct link to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------

Below you can find the Qt releases that the Enterprise Qt Debian packages supports. Pick the needed repositories and add them to your _/etc/apt/sources.list.d/tqtc.list_ as instructed above.

Also, the following tables list the installation directories on your system and the Linux distribution compatible with the packages.

**Note:**To access the listed repositories, you need an evaluation Qt Account or a commercial Qt Account with a Qt for Device Creation license.

**Note:**The packages may work on other distributions as well but there is no guarantee on that.

### Qt Creator[](https://doc.qt.io/qt/qt-debian-packages.html#qt-creator "Direct link to this headline")

| Architecture | Distribution | Installation directory | Package resource list entries for APT |
| --- | --- | --- | --- |
| amd64 | jammy-jellyfish (Ubuntu 22.04) | /opt/qt-creator/ | deb [arch=amd64 signed-by=<path>] https://debian-packages.qt.io/debian/enterprise/qtcreator-amd64 tqtc-jammy main |
| arm64 | jammy-jellyfish (Ubuntu 22.04) | /opt/qt-creator/ | deb [arch=arm64 signed-by=<path>] https://debian-packages.qt.io/debian/enterprise/qtcreator-arm64 tqtc-jammy main |

### Qt 6.10.2[](https://doc.qt.io/qt/qt-debian-packages.html#qt-6-10-3 "Direct link to this headline")

| Architecture | Distribution | Installation directory | Package resource list entries for APT |
| --- | --- | --- | --- |
| amd64 | jammy-jellyfish (Ubuntu 22.04) | /opt/qt-6.10.2/x86_64-linux-gnu/ | deb [arch=amd64 signed-by=<path>] https://debian-packages.qt.io/debian/enterprise/qt-6.10.2-amd64 tqtc-jammy main |
| arm64 | jammy-jellyfish (Ubuntu 22.04) | /opt/qt-6.10.2/aarch64-linux-gnu/ | deb [arch=arm64 signed-by=<path>] https://debian-packages.qt.io/debian/enterprise/qt-6.10.2-arm64 tqtc-jammy main |
| arm64 | bookworm (Debian 12, GLES) | /opt/qt-6.10.2/aarch64-linux-gnu/ | deb [arch=arm64 signed-by=<path>] https://debian-packages.qt.io/debian/enterprise/qt-6.10.2-arm64-gles tqtc-bookworm main |
