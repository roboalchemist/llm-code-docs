# Source: https://github.com/TigerVNC/tigervnc/wiki/Secure-your-connection

### What is a X.509 certificate? 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#what-is-a-x509-certificate)

\"X.509\" is a standard type of certificate commonly used for websites. However, they are also useful for securing TigerVNC.

Certificates allow two important security functions.

-   Certificates prove the identity of the computer you are viewing (the one with the TigerVNC server).
-   Certificates keep private the contents of the communication between you and the remote computer.

When it comes to obtaining a certificate, you can use an External Certificate Authority if you own a domain name, or create a self-signed certificate.

### Certificate from an External Certificate Authority 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#certificate-from-an-external-certificate-authority)

External Certificate Authorities issue certificates for public domain names but not local network IP addresses. As a result you need to own a domain name (like `example.com`). The basic setup would be something like the following.

1.  If your public website is `example.com`, rename your local network to something like `local.example.com`
2.  Obtain a certificate for `computer1.local.example.com`. Assuming computer1 is not available to the public internet, you need to use a DNS-01 challenge. (If you are using Let\'s Encrypt, see [https://letsencrypt.org/docs/challenge-types/#dns-01-challenge](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge))
3.  When you want to connect to computer1 on your network, type the hostname as `computer1.local.example.com`

Note: External Certificate Authorities have certificate transparency requirements that post the details of every certificate publicly. So don\'t name your computers after any secret company projects.

Once you obtain your certificate, see [Use the certificate with TigerVNC](#use-the-certificate-with-tigervnc)

### Create a self-signed certificate 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#create-a-self-signed-certificate)

If you do not own a domain name, or prefer not to use an external certificate authority, you can create a self-signed certificate.

Creating a certificate differs a little depending on whether you are on Windows or Linux. Jump to the heading that matches your system.

#### Windows 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#windows)

Unfortunately TigerVNC doesn\'t understand [Windows-style certificates](https://docs.microsoft.com/en-us/powershell/module/pkiclient/new-selfsignedcertificate?view=win10-ps) saved in the Windows certificate store or that end with the file extension `.pfx`. However, you can download OpenSSL to do the job.

On the computer with the TigerVNC server:

1.  Find out the local IP address of the computer running the TigerVNC server. See [LifeHacker\'s instructions](https://lifehacker.com/how-to-find-your-local-and-external-ip-address-5833108).
2.  Visit [http://wiki.overbyte.eu/wiki/index.php/ICS_Download#Download_OpenSSL_Binaries\_.28required_for_SSL-enabled_components.29](http://wiki.overbyte.eu/wiki/index.php/ICS_Download#Download_OpenSSL_Binaries_.28required_for_SSL-enabled_components.29) (Of the binaries [suggested by OpenSSL](https://wiki.openssl.org/index.php/Binaries), this is the simplest to run.)
3.  Choose the latest .zip download that matches your computer system (probably the first one labeled \"Win-64\")
4.  Uncompress the zip file.
5.  Go to the uncompress folder and double click **openssl.exe**.
6.  If you have Windows Defender SmartScreen, you may have to choose **More info** \> **Run anyway**.
7.  Type the following (replace both instances of \"192.168.1.5\" with the local IP address you found in step 1 above) `req -x509 -newkey rsa -days 365 -nodes -config openssl.cnf -keyout vnc-server-private.pem -out vnc-server.pem -subj '/CN=192.168.1.5' -addext "subjectAltName=IP:192.168.1.5"`

#### Linux 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#linux)

1.  Find out the local IP address of the computer running the TigerVNC server. See [Stackoverflow instructions](https://stackoverflow.com/questions/13322485/how-to-get-the-primary-ip-address-of-the-local-machine-on-linux-and-os-x#13322549).
2.  Open **Terminal** (if you haven\'t already)
3.  Install OpenSSL
    -   On RedHat/CentOS/Fedora, type: `sudo yum install openssl`
    -   On Debian/Ubuntu, type: `sudo apt-get install openssl`
4.  Create a self-signed certificate. Type the following (replace both instances of \"192.168.1.5\" with the local IP address you found in step 1 above) `openssl req -x509 -newkey rsa -days 365 -nodes -config openssl.cnf -keyout vnc-server-private.pem -out vnc-server.pem -subj '/CN=192.168.1.5' -addext "subjectAltName=IP:192.168.1.5"`

On Ubuntu (and related distros), you may also need to change the path to `openssl.cnf` to `/usr/lib/ssl/openssl.cnf`

### Manage the certificates 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#manage-the-certificates)

The private key should remain private to your computer. If you have syncing services (such as OneDrive, Dropbox, etc.), consider moving \"vnc-server-private.pem\" to a location that isn\'t synced or backed up. If you ever loose the private key, just create a new certificate and private key.

The certificate you created expires in 365 days. A year from now, you will need to go through these steps again and create a new certificate.

### Use the certificate with TigerVNC 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#use-the-certificate-with-tigervnc)

On the computer with TigerVNC server:

1.  Right click the TigerVNC icon in the system tray (bottom right in Windows) and choose **Options**
2.  Under \"Session encryption\" choose **TLS with X.509 certificates**, and uncheck **None** and **Anonymous TLS**.
3.  Choose **Load X.509 Certificate**. Browse to the public key file you saved above (\"vnc-server.pem\").
4.  Choose **Load X.509 Certificate key**. Browse to the private key file you saved above (\"vnc-server-private.pem\").
5.  Choose **Apply**
6.  Copy the public key file (\"vnc-server.pem\") to your remote computer. Save it in the same folder as the TigerVNC viewer. This avoids some problems with the TigerVNC viewer on Windows.

On the remote (client) computer:

1.  Open the TigerVNC viewer
2.  Type in the name or IP address of the computer you want to connect to.
3.  Choose **Options\...**
4.  Choose the **Security** tab
5.  Under **Path to X509 CA certificate** type the name of the your public key file you just copied (e.g. \"vnc-server.pem\"). If you are on Windows, this file needs to be located in the same folder as the viewer. Note: If you really want it in a different folder, you can use Linux-style path names, except the path name can\'t include spaces (and quotes around the path name don\'t work either).
6.  Type the password and choose **OK**. If you get any error messages at this point, read them carefully. If you skip over any error messages, you may bypass all the security guarantees of using certificates.
7.  On the computer with TigerVNC server you may have to choose **Accept** within 10 seconds. You can change this setting if needed.

The wiki is read-only because of malware spam that GitHub refuses to provide protection agains. Contact the maintainers directly with changes you\'d like to make.