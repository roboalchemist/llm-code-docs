# Custom DERP Servers

**Source:** https://tailscale.com/kb/1069/custom-derp

---

Docs›Start›Install Tailscale›Uninstall TailscaleUninstall TailscaleHere's how to uninstall Tailscale from your device, or completely reset
Tailscale for debugging purposes.
WindowsmacOS (App Store)macOS (Standalone)iOStvOSAndroidLinuxSynologyTailscale for Windows can be uninstalled like any Windows app, by using the
Windows Control Panel. Go to Settings > Apps, find Tailscale, and press the
Uninstall button.If you'd like to completely delete Tailscale, destroying any state or local
information, you can also remove the files at the following paths:C:\ProgramData\Tailscale
C:\Users\%USERNAME%\AppData\Local\Tailscale
C:\Windows\System32\config\systemprofile\AppData\Local\Tailscale
The path under System32 was only used in older versions of the Tailscale
client and may not be present on your system.After uninstalling Tailscale, if you install Tailscale on a device again at a later time, it will have a new IP address.
