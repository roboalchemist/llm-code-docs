# Source: https://nmap.org/download.html

Title: Download the Free Nmap Security Scanner for Linux/Mac/Windows

URL Source: https://nmap.org/download.html

Markdown Content:
[Download](https://nmap.org/download.html)[Reference Guide](https://nmap.org/book/man.html)[Book](https://nmap.org/book/)[Docs](https://nmap.org/docs.html)[Zenmap GUI](https://nmap.org/zenmap/)[In the Movies](https://nmap.org/movies/)

Get the latest Nmap for your system:

*   [Windows](https://nmap.org/download.html#windows)
*   [macOS](https://nmap.org/download.html#macosx)
*   [Linux (RPM)](https://nmap.org/download.html#linux-rpm)
*   [Any other OS (source code)](https://nmap.org/download.html#source)

Older versions (and sometimes newer test releases) are available from the [Nmap release archive](https://nmap.org/dist/) (and really old ones are in [dist-old](https://nmap.org/dist-old/)). For the more security-paranoid (smart) users, GPG detached signatures and SHA-1 hashes for each release are available in the [sigs directory](https://nmap.org/dist/sigs/) ([verification instructions](https://nmap.org/book/install.html#inst-integrity)). Before downloading, be sure to read the relevant sections for your platform from the [Nmap Install Guide](https://nmap.org/book/install.html). The most important changes (features, bugfixes, etc) in each Nmap version are described in the [Changelog](https://nmap.org/changelog.html). Using Nmap is covered in the [Reference Guide](https://nmap.org/book/man.html), and don't forget to read the other [available documentation](https://nmap.org/docs.html), particularly the official book [Nmap Network Scanning](https://nmap.org/book/)!

Nmap users are encouraged to subscribe to the _Nmap-hackers_ mailing list. It is a low volume (7 posts in 2015), moderated list for the most important announcements about Nmap, Insecure.org, and related projects. You can join the 128,953 current subscribers (as of September 2017) by submitting your email address here:

You can also get updates by liking [Nmap on Facebook](https://facebook.com/nmap) or following us [@nmap on Twitter](https://twitter.com/nmap).

Nmap is distributed with source code under [custom license terms](https://nmap.org/npsl/) similar to (and derived from) the GNU General Public License, as noted in the [copyright page](https://nmap.org/book/man-legal.html).

[![Image 1: Zenmap 7.91 on Windows 11](https://nmap.org/zenmap/images/zenmap-7.91-win-th-204x207.png)](https://nmap.org/zenmap/images/zenmap-7.91-win-730x850.png) Please read the [Windows section](https://nmap.org/book/inst-windows.html) of the Install Guide for limitations and installation instructions for the Windows version of Nmap. It's provided as an executable self-installer which includes Nmap's dependencies and the Zenmap GUI. We support Nmap on Windows 7 and newer, as well as Windows Server 2008 R2 and newer. We also maintain a [guide for users who must run Nmap on earlier Windows releases.](https://secwiki.org/w/Nmap/Old_Windows_Releases).

**Note:** The version of Npcap included in our installers may not always be the latest version. If you experience problems or just want the latest and greatest version, download and install [the latest Npcap release.](https://npcap.com/#download)

**Latest stable release self-installer: [nmap-7.98-setup.exe](https://nmap.org/dist/nmap-7.98-setup.exe)**

**Latest Npcap release self-installer: [npcap-1.87.exe](https://npcap.com/dist/npcap-1.87.exe)**

We have written [post-install usage instructions](https://nmap.org/book/inst-windows.html#inst-win-exec). Please [notify us](https://nmap.org/book/man-bugs.html) if you encounter any problems or have suggestions for the installer.

Many popular Linux distributions (Redhat, Mandrake, Suse, etc) use the [RPM](http://www.rpm.org/) package management system for quick and easy binary package installation. We have written a detailed [guide to installing our RPM packages](https://nmap.org/book/inst-linux.html#inst-rpm), though these simple commands usually do the trick:

rpm -vhU https://nmap.org/dist/nmap-7.98-1.x86_64.rpm
rpm -vhU https://nmap.org/dist/zenmap-7.98-1.noarch.rpm
rpm -vhU https://nmap.org/dist/ncat-7.98-1.x86_64.rpm
rpm -vhU https://nmap.org/dist/nping-7.98-1.x86_64.rpm
 You can also download and install the RPMs yourself:

**Latest stable release:**

**x86-64 (64-bit Linux)**[Nmap](https://nmap.org/) RPM: [nmap-7.98-1.x86_64.rpm](https://nmap.org/dist/nmap-7.98-1.x86_64.rpm)

**x86-64 (64-bit Linux)**[Ncat](https://nmap.org/ncat/) RPM: [ncat-7.98-1.x86_64.rpm](https://nmap.org/dist/ncat-7.98-1.x86_64.rpm)

**x86-64 (64-bit Linux)**[Nping](https://nmap.org/nping/) RPM: [nping-7.98-1.x86_64.rpm](https://nmap.org/dist/nping-7.98-1.x86_64.rpm)

 Optional [Zenmap GUI](https://nmap.org/zenmap/) (all platforms): [zenmap-7.98-1.noarch.rpm](https://nmap.org/dist/zenmap-7.98-1.noarch.rpm)

 Source RPM (includes Nmap, Zenmap, Ncat, and Nping): [nmap-7.98-1.src.rpm](https://nmap.org/dist/nmap-7.98-1.src.rpm)

Nmap binaries for Apple macOS (x86-64) are distributed as a disk image file containing an installer. The installer allows installing Nmap, Zenmap, Ncat, and Ndiff. The programs have been tested on Mac OS X 10.9 and later. See the [Mac OS X Nmap install page](https://nmap.org/book/inst-macosx.html) for more details. Users of PowerPC (PPC) Mac machines, which Apple ceased selling in 2006, should see [this page instead](https://secwiki.org/w/Nmap/Mac_OSX_PPC) for support information.

**Latest stable release installer: [nmap-7.98.dmg](https://nmap.org/dist/nmap-7.98.dmg)**

This is the traditional compile-it-yourself format. The Nmap tarball compiles under Linux, Mac OS X, Windows, and many UNIX platforms (Solaris, Free/Net/OpenBSD, etc.) It includes Zenmap, the GUI frontend.

Detailed Linux/BSD/Solaris compilation instructions and options are [provided here](https://nmap.org/book/inst-source.html), though this usually does the trick:

bzip2 -cd nmap-7.98.tar.bz2 | tar xvf -
cd nmap-7.98
./configure
make
su root
make install

Most Windows users install with our [Windows executable installer](https://nmap.org/download.html#windows), but we also provide [Windows source code compilation instructions](https://nmap.org/book/inst-windows.html#inst-win-source).

Most Mac OS X users install with our [Mac installer](https://nmap.org/download.html#macosx), but we also provide [Mac OS X source code compilation instructions](https://nmap.org/book/inst-macosx.html#inst-macosx-source).

If you are compiling Nmap anyway, you might prefer to get the very latest code from [our SVN source code repository](https://nmap.org/book/install.html#inst-svn) or the [Nmap GitHub mirror](https://github.com/nmap/nmap) rather than downloading a tarball here.

**Latest stable Nmap release tarball: [nmap-7.98.tar.bz2](https://nmap.org/dist/nmap-7.98.tar.bz2)** (or [gzip compressed](https://nmap.org/dist/nmap-7.98.tgz))
