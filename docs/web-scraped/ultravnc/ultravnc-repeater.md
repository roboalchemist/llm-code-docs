# Source: https://uvnc.com/docs/ultravnc-repeater.html

## [UltraVNC Repeater]

[We are online, our links, join us on social networks and share our announcements:\
- Website: <https://uvnc.com/>\
- Forum: <https://forum.uvnc.com/>\
- GitHub: <https://github.com/ultravnc>\
- Mastodon: <https://mastodon.social/@ultravnc>\
- Bluesky/AT Protocol: <https://bsky.app/profile/ultravnc.bsky.social>\
- Facebook: <https://www.facebook.com/ultravnc1>\
- X/Twitter: <https://x.com/ultravnc1>\
- Reddit community: <https://www.reddit.com/r/ultravnc>\
- OpenHub: <https://openhub.net/p/ultravnc>]

 

[UltraVNC Repeater has two unique functions:\
Mode 1: Allows for connection to multiple servers (in listen mode), using only one port. All connection data flows through the repeater, allowing connection to multiple servers through a single port forward or tunnel.\
Mode 2: Allows both a Viewer and Server to connect together using the repeater as a PROXY. All connection data flows through the repeater, allowing both the server and viewer to be behind firewalls or routers.\
]

# UltraVNC Repeater Usage

Start UltraVNC Repeater

Access http://localhost:81 (or whichever address is specified in the pop-up)

user: admin                 password: adminadmi2

\* Use Firefox or Internet Explorer, Google Chrome seems to have problems.

 

Here you will be able to see the Viewers and Servers that are connected to the UltraVNC Repeater. The Connections section will show Servers/Viewers that have established connection to one another. Whereas the Waiting Servers/Waiting Viewers show Servers/Viewers that are ready to be connected to.

 

## Setting up UltraVNC Server for UltraVNC Repeater:

These instructions assume that UltraVNC Server has been installed and set up as a service.

1\. Go to [C:\\Program Files\\uvnc bvba\\UltraVNC and open up ]ultravnc.ini

2\.  Under the section \[admin\] add the following setting: 

**service_commandline = -autoreconnect ID:123456789 -connect repeater_ip_address:5500**

Replace 123456789 with your own custom ID  max 9 digits

3\. Restart the service

 

If you don\'t have the permissions to edit this file you may need to move this file to the desktop first before you edit, and then move back to the original directory.

After saving the changes to ultravnc.ini, stop any exisiting UltraVNC Server services, and start it back up so it will load the new ini settings. You should be able to verify that it\'s working by viewing the UltraVNC Repeater Status page and looking at the Waiting Servers section.

 

UltraVNC Viewer

 

 

## LICENSE

\
[THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS AS IS AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE].

 

  --
  --

[](# "Menu")

[](#)

-   [Home](https://uvnc.com/)
-   [Products[]](https://uvnc.com/products/ultravnc.html)
    -   [UltraVNC](https://uvnc.com/products/ultravnc.html)
    -   [UltraVNC Repeater](https://uvnc.com/products/ultravnc-repeater.html)
    -   [UltraVNC Single Click (SC)](https://uvnc.com/products/ultravnc-sc.html)
    -   [UltraVNC Mirror Driver](https://uvnc.com/products/mirror-driver.html)
    -   [PcHelpWare](https://uvnc.com/products/pchelpware.html)
    -   [PcHelpWareV2](https://uvnc.com/products/pchelpwarev2.html)
-   [Downloads[]](https://uvnc.com/downloads/ultravnc.html)
    -   [UltraVNC](https://uvnc.com/downloads/ultravnc.html)
    -   [UltraVNC Repeater](https://uvnc.com/downloads/ultravnc-repeater.html)
    -   [UltraVNC Single Click (SC)](https://uvnc.com/downloads/ultravnc-sc.html)
    -   [UltraVNC VNC Secure](https://uvnc.com/downloads/encryption.html)
    -   [UltraVNC Mirror Driver](https://uvnc.com/downloads/mirror-driver.html)
    -   [PcHelpWare](https://uvnc.com/downloads/pchelpware.html)
    -   [UltraVNC ScreenRecorder](https://uvnc.com/downloads/ultravnc-screenrecorder.html)
-   [Documentation[]](https://uvnc.com/docs/ultravnc-server.html)
    -   [UltraVNC Server](https://uvnc.com/docs/ultravnc-server.html)
    -   [UltraVNC Viewer](https://uvnc.com/docs/ultravnc-viewer.html)
    -   [UltraVNC Repeater](https://uvnc.com/docs/ultravnc-repeater.html)
    -   [UltraVNC Single Click (SC)](https://uvnc.com/docs/ultravnc-sc.html)
    -   [Documentation 1.3.x +](https://uvnc.com/docs/documentation.html)
    -   [General Knowledge](https://uvnc.com/docs/general-knowledge.html)
    -   [PcHelpWare](https://uvnc.com/docs/pchelpware.html)
-   [Forum](https://forum.uvnc.com)
-   [Git](https://github.com/ultravnc/ultravnc)
-   [Bluesky](https://bsky.app/profile/ultravnc.bsky.social)
-   [OpenHub](https://openhub.net/p/ultravnc)

-   [[]](https://www.facebook.com/UltraVNC1)
-   [[]](https://twitter.com/ultravnc1)
-   [[]](https://www.reddit.com/r/ultravnc/)
-   [[]](https://mastodon.social/@ultravnc)
-   [[]](https://github.com/ultravnc)

[[]](#)

**JavaScript is currently disabled.**Please enable it for a better experience of [Jumi](http://2glux.com/projects/jumi).