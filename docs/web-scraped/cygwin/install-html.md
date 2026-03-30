# Source: https://cygwin.com/install.html

Title: Cygwin Installation

URL Source: https://cygwin.com/install.html

Markdown Content:
Get that [Linux](https://www.linuxfoundation.org/) feeling - on Windows

Installing and Updating Cygwin Packages
---------------------------------------

Installing and Updating Cygwin for 64-bit versions of Windows
-------------------------------------------------------------

Run [setup-x86_64.exe](https://cygwin.com/setup-x86_64.exe) any time you want to update or install a Cygwin package for 64-bit windows.

The gpg [signature](https://cygwin.com/setup-x86_64.exe.sig) for [setup-x86_64.exe](https://cygwin.com/setup-x86_64.exe) can be used to verify the validity of this binary using the public key [here](https://cygwin.com/key/pubring.asc).

General installation notes
--------------------------

When installing packages for the first time, the setup program _does not install every package_. Only the **minimal base packages** from the Cygwin distribution are installed by default, which takes up about 100 MB.

Clicking on categories and packages in the setup program package installation screen allows you to select what is installed or updated.

Individual packages like _bash_, _gcc_, _less_, etc. are released independently of the Cygwin DLL, so the Cygwin DLL version is not useful as a general Cygwin release number. The setup program tracks the versions of all installed components and provides the mechanism for **installing** or **updating** everything available from this site for Cygwin.

Once you've installed your desired subset of the Cygwin distribution, the setup program will remember what you selected, so re-running it will update your system with any new package releases.

The setup program will check by default if it runs with administrative privileges and, if not, will try to elevate the process. If you want to avoid this behaviour and install under an unprivileged account just for your own usage, run setup with the `--no-admin` option.

Q: How do I add a package to my existing Cygwin installation?
-------------------------------------------------------------

A: Run the setup program and select the package you want to add.

**Tip:** If you don't want to also upgrade existing packages, select 'Keep' at the top-right of the package chooser page.

Q: Is there a command-line installer?
-------------------------------------

A: Yes and no. The setup program understands [command-line arguments](https://cygwin.com/faq/faq.html#faq.setup.cli) which allow you to control its behavior and choose individual packages to install. While this provides some functionality similar to such tools as `apt-get` or `yum` it is not as full-featured as those package managers.

**Tip:** Performing an automated installation can be done using the `-q` and `-P package1,package2,...` options.

Q: Why not use `apt`, `yum`, my favourite package manager, etc.?
----------------------------------------------------------------

A: The basic reason for not using a more full-featured package manager is that such a program would need full access to all of Cygwin's POSIX functionality. That is, however, difficult to provide in a Cygwin-free environment, such as exists on first installation. Additionally, Windows does not easily allow overwriting of in-use executables so installing a new version of the Cygwin DLL while a package manager is using the DLL is problematic.

Q: How do I install everything?
-------------------------------

A: You do not want to do this! This will install an enormous number of packages that you will never use, including debuginfo and source for every package.

If you really _must_ do this, clicking on the "Default" label next to the "All" category to change it to "Install" will mark every Cygwin package for installation. Be advised that this will download and install tens of gigabytes of files to your computer.

Q: What packages are available?
-------------------------------

A: To find available packages, and view what package contains _X_ see the [package search](https://cygwin.com/packages/) page.

**Tip:** Perform a search from the command-line using [`cygcheck`](https://cygwin.com/cygwin-ug-net/cygcheck.html) using `-p package` or `-e package1 package2 ...` options.

Q: How do I verify the signature of setup?
------------------------------------------

A: e.g.

$ gpg --recv-key 56405CF6FCC81574682A5D561A698DE9E2E56300
gpg: key 1A698DE9E2E56300: "Cygwin <cygwin@cygwin.com>" imported
gpg: Total number processed: 1
gpg:               imported: 1

$ gpg --keyid-format=long --with-fingerprint --verify setup-x86_64.exe.sig setup-x86_64.exe
gpg: Signature made 22 May 2025 15:49:21 BST
gpg:                using RSA key 56405CF6FCC81574682A5D561A698DE9E2E56300
gpg: Good signature from "Cygwin <cygwin@cygwin.com>"
Primary key fingerprint: 5640 5CF6 FCC8 1574 682A  5D56 1A69 8DE9 E2E5 6300

Q: What's the hash of setup?
----------------------------

A: See [here](https://cygwin.com/sha512.sum)

Q: How can I do an offline install?
-----------------------------------

A1: Install without access to the internet, using a local package repository

*    Create a local copy of the package repository e.g. by using [`rsync` on one of the mirrors](https://cygwin.com/package-server.html#local-mirror). 
*    Move that copy to an accessible location, or copy it to removable media. 
*    Run setup, and enter the URL, path or UNC path of that repository when prompted to "Choose A Download Site". 

A2: Install without access to the internet, using setup's separate download and install actions.

*    Run setup in "Download without installing" mode somewhere it can access a mirror, with the desired packages selected. 
*    Run setup again in "Install from local directory" mode, with the same "Local package directory", and set of packages selected. 

Q: How can I install the last Cygwin version for an old, unsupported Windows version?
-------------------------------------------------------------------------------------

A: Run setup with the options 
```
--allow-unsupported-windows
  --site circa_URL
```
:

| Windows version | Setup version | Cygwin DLL version | circa URL |
| --- | --- | --- | --- |
| Windows 7 Windows Server 2008 R2 (NT 6.1) Windows 8 Windows Server 2012 (NT 6.2) | current | 3.4.10 | 64-bit: http://ctm.crouchingtigerhiddenfruitbat.org/pub/cygwin/circa/64bit/2024/01/30/231215 Also use `--no-verify` with this URL. |
| Windows Vista Windows Server 2008 (NT 6.0) [All 32-bit Windows](https://cygwin.com/pipermail/cygwin-announce/2022-November/010810.html) | current | 3.3.6 | 32-bit: http://ctm.crouchingtigerhiddenfruitbat.org/pub/cygwin/circa/2022/11/23/063457 or the URL for any [sourceware mirror](https://sourceware.org/mirrors.html), followed by cygwin-archive/20221123 64-bit: http://ctm.crouchingtigerhiddenfruitbat.org/pub/cygwin/circa/64bit/2022/11/23/063529 |
| [Windows XP SP3 Windows Server 2003 (NT 5.1)](https://cygwin.com/ml/cygwin/2016-11/msg00071.html) | 2.932 ([32-bit](https://cygwin.com/setup/setup-2.932.x86_64.exe), [64-bit](https://cygwin.com/setup/setup-2.932.x86.exe)) | 2.5.2 | 32-bit: http://ctm.crouchingtigerhiddenfruitbat.org/pub/cygwin/circa/2016/08/30/104223 64-bit: http://ctm.crouchingtigerhiddenfruitbat.org/pub/cygwin/circa/64bit/2016/08/30/104235 Also use `--no-verify` with these URLs. |
| Windows 2000 (NT 5.0) Windows XP SP2 | [2.774](http://ctm.crouchingtigerhiddenfruitbat.org/pub/cygwin/setup/snapshots/setup-2.774.exe) | 1.7.18 | 32-bit: http://ctm.crouchingtigerhiddenfruitbat.org/pub/cygwin/circa/2013/06/04/121035 Also use `--no-verify` with these URLs. Use `--only-site` rather than `--allow-unsupported-windows` with this setup version. |

Thanks to the [Cygwin Time Machine](http://www.crouchingtigerhiddenfruitbat.org/Cygwin/timemachine.html) for providing this archive.

#### A note about 32-bit Cygwin

The limited address space of 32-bit Windows means that [random failures in the fork(2) system call](https://cygwin.com/faq.html#faq.using.fixing-fork-failures) are more likely. Therefore, we recommend using 32-bit Cygwin only in limited scenarios, with only a minimum of necessary packages installed, and only if there's no way to run 64-bit Cygwin instead.

**You have been warned.** If you're still sure you really need a 32-bit Cygwin, and there's absolutely no way around it, you may use the [setup-x86.exe](https://cygwin.com/setup-x86.exe) installer, following the instructions above. The gpg [signature](https://cygwin.com/setup-x86.exe.sig) can be used to verify the validity of this binary.

Q: How do I help improve setup?
-------------------------------

A: See the [setup](https://sourceware.org/cygwin-apps/setup.html) project page for more information.

GUI translations can be made and updated at [weblate](https://hosted.weblate.org/projects/cygwin-setup/cygwin-setup/).
