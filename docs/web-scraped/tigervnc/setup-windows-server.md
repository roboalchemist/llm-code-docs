# Source: https://github.com/TigerVNC/tigervnc/wiki/Setup-TigerVNC-server-(Windows)

## Recommended version 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#recommended-version)

**DISCLAIMER:** TigerVNC *dropped* official support for the Windows server (WinVNC) [in September 2020](https://github.com/TigerVNC/tigervnc/releases/tag/v1.11.0). However, as of August 2024, [version 1.14.0](https://github.com/TigerVNC/tigervnc/releases/tag/v1.14.0) works reliably.

(Note: WinVNC stores settings in the Windows registry.)

## Private network 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#private-network)

Before installing TigerVNC server, check you are on a private network at home (not a public network). Then check that your computer knows that you are on a private network (steps below).

1.  In the task bar (bottom right), right click on the Network icon and choose **Open Network & Internet settings**
2.  If it says \"Private network\" under your connection, skip to \"Install and setup TigerVNC server.\" If it says \"Public Network\" continue.
3.  Choose **Change connection properties**
4.  Choose **Private**
5.  Close settings.

## Install and setup TigerVNC server 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#install-and-setup-tigervnc-server)

1.  Download and install TigerVNC server using the default settings. Look for the download file with the name \"-winvnc-\" (e.g. \"tigervnc64-winvnc-x.xx.xx.exe\"). That file contains the server. Otherwise you just get the viewer.
2.  Restart your computer.
3.  In the task bar (bottom right), choose the up arrow to show more task icons, then right click on the TigerVNC icon and choose **Options**
4.  Under Authentication choose **Configure** and type a password. Important: VNC only accepts the first eight characters of the password, so make sure you have a good mix of uppercase, lowercase, numbers, and symbols in those eight characters. No extended characters are permitted.
5.  Choose **OK** to close the password window and **OK** to close the Server Properties window.

## Firewall setup 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#firewall-setup)

The following instructions are for Windows built-in firewall. Adapt if you are using a 3rd-party firewall.

1.  From the **Start menu** type and choose **Firewall & network protection**
2.  Choose **Allow an app through firewall**
3.  Choose **Change settings**
4.  Choose **Allow another app**
5.  Choose **Browse\...**
6.  Browse to `C:\Program Files\TigerVNC Server\winvnc4.exe` (older versions saved under `C:\Program Files\TigerVNC\winvnc4.exe`)
7.  Choose **Add**
8.  Choose **OK**

## Connecting 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#connecting)

1.  Open the TigerVNC viewer on another computer (we\'ll call this the \"remote (client) computer\")
2.  Type in the name or IP address of the computer you want to connect to, then choose **Connect**
3.  Type in the password you setup for the server. Then choose **OK**

## Troubleshooting 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#troubleshooting)

If you get a \"Can\'t establish connection\" error. Here are a few steps to try to locate the problem.

1.  Open TigerVNC\'s viewer on the same computer and connect to \"localhost\". This checks the VNC server is working on your computer. If you get the same error, check the following:
    -   Review the \"Install and setup TigerVNC server\" section above.
    -   If you have VNC software besides TigerVNC running, close or uninstall it.
2.  Open TigerVNC\'s viewer on the same computer and connect to your IP address on the network. This checks the firewall on the server computer is not an issue. If you get the same error on this step, review the \"Firewall setup\" section above.
3.  On the remote computer enter the IP address/computer name. Using TigerVNC\'s viewer on the remote computer is recommended. If you use another viewer, here\'s some setting to check:
    -   Protocol: **VNC** (Virtual Network Computing)
    -   Server: (name/IP address of computer on your local network)
    -   Username: (leave blank)
    -   Password: (password you set up on the server, or leave blank if you want it to ask you every time).

## Making the connection secure 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#making-the-connection-secure)

Next, see [Secure your connection](/TigerVNC/tigervnc/wiki/Secure-your-connection).

The wiki is read-only because of malware spam that GitHub refuses to provide protection agains. Contact the maintainers directly with changes you\'d like to make.