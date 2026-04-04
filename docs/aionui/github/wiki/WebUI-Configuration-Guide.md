# Source: https://github.com/iOfficeAI/AionUi/wiki/WebUI-Configuration-Guide

# 🌐 AionUi WebUI Configuration Guide

This guide covers how to configure and use AionUi in WebUI mode, enabling browser-based access and remote connections to your local AI assistant.

**[English](WebUI-Configuration-Guide)** | [简体中文](WebUI-Configuration-Guide-Chinese)

## 🎯 WebUI Mode Overview

WebUI mode allows you to access AionUi through a browser, supporting any browser, remote access, secure login, and server deployment.

**Configuration Process (4 Steps):**

1. **Start WebUI** → Select platform, run startup command
2. **First Login** → Open `http://localhost:25808` in browser, create account
3. **Remote Access** (optional) → Use `--remote` for same network, Tailscale for cross-network
4. **Server Deployment** (optional) → macOS uses LaunchAgent, Linux uses systemd

**Usage Scenarios:**
- 🏠 **Local Use Only**: Step 1 → Step 2
- 📱 **LAN Access**: Step 1 → Step 2 → Step 3 (same network)
- 🌐 **Cross-Network Access**: Step 1 → Step 2 → Step 3 (Tailscale)
- 🖥️ **Server Deployment**: Step 1 → Step 2 → Step 4

---

<a id="commands"></a>
## 📋 Quick Command Reference

Before starting, here are the common commands for starting WebUI on each platform:

| Platform | Local Access | Network Access (LAN) |
|:---:|:---:|:---:|
| **Windows** | `AionUi.exe --webui` | `AionUi.exe --webui --remote` |
| **macOS** | `/Applications/AionUi.app/Contents/MacOS/AionUi --webui` | `/Applications/AionUi.app/Contents/MacOS/AionUi --webui --remote` |
| **Linux** | `AionUi --webui` | `AionUi --webui --remote` |
| **Android** | `AionUi --no-sandbox --webui` | `AionUi --no-sandbox --webui --remote` |

> **Tip**: If the command is not found, use the full path (see detailed instructions below for each platform). Linux root users and Android need to add the `--no-sandbox` parameter.

---

## 📑 Quick Navigation

| [📋 Command Reference](#commands) | [🚀 Quick Start](#quick-start) | [🔐 Authentication](#auth) | [🔐 Tailscale](#tailscale) | [🌍 Remote Access](#remote) |
|:---:|:---:|:---:|:---:|:---:|
| [🖥️ Server Deployment](#server) | [🔑 Password Management](#password) | [🛠️ Troubleshooting](#troubleshooting) | [📝 CLI Options](#cli) | [💡 Best Practices](#best-practices) |

---

<a id="quick-start"></a>
## 🚀 Quick Start

### Step 1: Start WebUI Mode

---

### 🪟 Windows

**Open Command Prompt or PowerShell, and run:**

Method 1: Using full path

```cmd
"C:\Program Files\AionUi\AionUi.exe" --webui
```

Method 2: If AionUi is in your PATH

```cmd
AionUi.exe --webui
```

---

### 🍎 macOS

**Open Terminal, and run:**

```bash
/Applications/AionUi.app/Contents/MacOS/AionUi --webui
```

---

### 🐧 Linux

**Open Terminal, and select the command based on your user type:**

Desktop Environment (Non-root User):

Local Access:

```bash
AionUi --webui
```

Network Access (LAN):

```bash
AionUi --webui --remote
```

Alternative Methods:

Using system path:

```bash
AionUi --webui
```

Or using full path:

```bash
/usr/bin/AionUi --webui
```

For AppImage:

```bash
./AionUi-*.AppImage --webui
```

---

**Root User:**

If using root user, you need to add `--no-sandbox` flag.

Local Access:

```bash
sudo AionUi --webui --no-sandbox
```

Network Access (LAN):

```bash
sudo AionUi --webui --remote --no-sandbox
```

---

<details>
<summary><strong>📱 Android (Termux)</strong></summary>

> **Community Contribution**: Special thanks to [@Manamama](https://github.com/Manamama) for creating this guide!  
> **Original Tutorial**: [Running AionUi WebUI on Android via Termux + Proot Ubuntu](https://gist.github.com/Manamama/b4f903c279b5e73bdad4c2c0a58d5ddd)  
> **Related Issues**: [#217 - Android Support Discussion](https://github.com/iOfficeAI/AionUi/issues/217)

> ⚠️ **Important**: 
> - Electron desktop mode is **NOT supported** on Android, only WebUI mode works
> - Install Termux from [F-Droid](https://f-droid.org/en/packages/com.termux/) (Google Play version is outdated)
> - Requirements: ~5 GB free storage, Internet connection, Android 7.0+

**Step 1: Install Termux and Proot**

Open Termux and execute:

```bash
pkg update -y
pkg install proot-distro -y
proot-distro install ubuntu
proot-distro login ubuntu
```

**Step 2: Install System Dependencies**

```bash
apt update
apt install -y wget libgtk-3-0 libnss3 libasound2 libgbm1 libxshmfence1 ca-certificates
```

**Step 3: Download and Install AionUi**

```bash
wget https://github.com/iOfficeAI/AionUi/releases/download/v1.5.2/AionUi_1.5.2_arm64.deb
apt install -y ./AionUi_*.deb
which AionUi
```

**Step 4: Launch AionUi**

- **Local Access**: `AionUi --no-sandbox --webui`
- **Network Access**: `AionUi --no-sandbox --webui --remote`

> 💡 **Quick Start** (from Termux main shell):
> ```bash
> proot-distro login ubuntu -- bash -c "AionUi --no-sandbox --webui --remote"
> ```

**Step 5: Access WebUI**

Open `http://localhost:25808` in your browser

<details>
<summary><strong>📋 Additional Information</strong></summary>

**Expected Warnings (Safe to Ignore):**

```
[WARNING] Could not connect to session bus...
[ERROR] Failed to connect to the bus...
[WARNING] Multiple instances of the app detected...
```

These errors are related to D-Bus and X server, which are not needed for WebUI mode.

**Performance Tips:**

- Use lightweight browsers (Chrome or Firefox Focus)
- Close background apps to free RAM
- Use WiFi instead of mobile data
- Keep device charged

**Troubleshooting:**

- **Port in use**: Add `--port 8080` flag
- **Permission denied**: Run `chmod +x /opt/AionUi/aionui`
- **Out of memory**: Close other apps
- **Cannot access**: Check if AionUi is running, clear browser cache

**Need Help?**  
Check the [full detailed tutorial](https://gist.github.com/Manamama/b4f903c279b5e73bdad4c2c0a58d5ddd) or report issues at [GitHub Issue #217](https://github.com/iOfficeAI/AionUi/issues/217)

</details>

</details>

---

### Step 2: Access the Web Interface

After starting with the `--webui` flag, you'll see output like:

```
🚀 WebUI started / WebUI 已启动: http://localhost:25808
```

Simply open this URL in your browser. The application will automatically open your default browser when started.

---

### Step 3: First Login

On first launch, you'll see your initial credentials:

<img src="assets/Images/webui-account.png" alt="First login credentials display" width="600" />

```
========================================
  ✅ Default admin user created!
========================================
  
  Username: admin
  Password: [random-password]
  
  🌐 Access URL: http://localhost:25808
  
========================================
```

**Important**: Copy the password immediately - you'll need it to log in!

---

<a id="auth"></a>
## 🔐 Authentication Setup

### Default Credentials

When AionUi starts in WebUI mode for the first time, a default admin user is automatically created:

- **Username**: `admin`
- **Password**: Randomly generated 12-character password (displayed in console)

### Security Features

- **Rate Limiting**: Login attempts are rate-limited (5 attempts per 15 minutes)
- **Password Hashing**: Passwords are hashed using bcrypt
- **Session Tokens**: JWT tokens for secure session management
- **Cookie Protection**: HttpOnly and SameSite cookies for CSRF protection

### Adding Multiple Users

You can add more users through the WebUI:

1. Log in as admin
2. Navigate to User Settings
3. Add new users with custom credentials

---

<a id="tailscale"></a>
## 🔐 Using Tailscale for Cross-Network Access (Recommended)

> **Use Case**: Access from different networks (e.g., office computer accessing home server, or mobile data access)

Using Tailscale allows cross-network access without router configuration or public IP:

1. Install Tailscale on both server and client devices
2. Log in with the same Tailscale account
3. Access using Tailscale's virtual IP (typically `100.x.x.x:25808`)

---

<a id="remote"></a>
## 🌍 Remote Access Configuration

> **Use Case**: Access from devices on the same WiFi/LAN (e.g., phone and computer on the same WiFi)

### Step 1: Enable Remote Access

Add the `--remote` flag to your startup command:

- **Windows**: `AionUi.exe --webui --remote`
- **macOS**: `/Applications/AionUi.app/Contents/MacOS/AionUi --webui --remote`
- **Linux**: `AionUi --webui --remote` (root users need to add `--no-sandbox`)
- **Android**: `AionUi --no-sandbox --webui --remote`

### Step 2: Get Access Address

After starting, AionUi will display the network access address:

```
🚀 Network access / 网络访问: http://192.168.1.100:25808
```

> 💡 **Tip**: If not displayed, Windows users run `ipconfig`, macOS/Linux users run `ifconfig` to check IP address.

### Step 3: Access from Other Devices

Open the displayed address in a browser on other devices (phone, tablet, etc.) and log in with your credentials.

⚠️ **Note**: Only use remote mode on trusted networks.

---

<a id="server"></a>
## 🖥️ Server Deployment

> **Use Case**: Run 24/7 on servers with remote access and auto-restart support

### 🍎 macOS - LaunchAgent Background Running

**Step 1: Create Configuration File**

Create `~/Library/LaunchAgents/com.aionui.webui.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.aionui.webui</string>
  <key>ProgramArguments</key>
  <array>
    <string>/Applications/AionUi.app/Contents/MacOS/AionUi</string>
    <string>--webui</string>
    <string>--remote</string>
  </array>
  <key>RunAtLoad</key>
  <true/>
  <key>KeepAlive</key>
  <true/>
</dict>
</plist>
```

**Step 2: Start Service**

```bash
launchctl load ~/Library/LaunchAgents/com.aionui.webui.plist
launchctl start com.aionui.webui
```

### 🐧 Linux - systemd (Recommended)

**Step 1: Create Service File**

```bash
sudo nano /etc/systemd/system/aionui-webui.service
```

**Step 2: Add Configuration**

```ini
[Unit]
Description=AionUi WebUI Service
After=network.target

[Service]
Type=simple
User=YOUR_USERNAME
WorkingDirectory=/home/YOUR_USERNAME
ExecStart=/usr/bin/AionUi --webui --remote
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
```

> 💡 **Tip**: Replace `YOUR_USERNAME` and `/usr/bin/AionUi` with actual values.

**Step 3: Enable and Start**

```bash
sudo systemctl daemon-reload
sudo systemctl enable aionui-webui.service
sudo systemctl start aionui-webui.service
sudo systemctl status aionui-webui.service
```

**Common Management Commands:**

- View logs: `sudo journalctl -u aionui-webui.service -f`
- Restart service: `sudo systemctl restart aionui-webui.service`
- Stop service: `sudo systemctl stop aionui-webui.service`

**Step 4: Get Access Address**

Check the access address in logs, or run:

```bash
sudo journalctl -u aionui-webui.service | grep "WebUI"
```

> 💡 **Custom Port**: Add `Environment="AIONUI_PORT=8080"` in `[Service]`, then restart the service.

---

<a id="password"></a>
## 🔑 Password Management

### Reset Admin Password

> 💡 **Tip**: Currently, WebUI does not support custom password changes in the interface. To change your password, use the `--resetpass` command to reset it to a new random password.

If you forget your admin password or need to change it, run the `--resetpass` command in terminal:

#### Windows

Open **Command Prompt** or **PowerShell**, and run:

**Reset admin password:**

```cmd
"C:\Program Files\AionUi\AionUi.exe" --resetpass
```

**Or for a specific user:**

```cmd
"C:\Program Files\AionUi\AionUi.exe" --resetpass username
```

#### macOS

Open **Terminal**, and run:

**Reset admin password:**

```bash
/Applications/AionUi.app/Contents/MacOS/AionUi --resetpass
```

**Or for a specific user:**

```bash
/Applications/AionUi.app/Contents/MacOS/AionUi --resetpass username
```

#### Linux

Open **Terminal**, and run:

**Reset admin password:**

```bash
AionUi --resetpass
```

**Or for a specific user:**

```bash
AionUi --resetpass username
```

**What happens when you run `--resetpass`:**

1. Connects to the database
2. Finds the specified user (default: `admin`)
3. Generates a new random 12-character password
4. Updates the password hash in the database
5. Rotates the JWT secret (invalidating all previous tokens)
6. Displays the new password in the terminal

**After running `--resetpass`:**

1. Copy the new password from the terminal
2. Refresh your browser (Cmd+R or Ctrl+R)
3. You'll be redirected to the login page
4. Log in with the new password shown in the terminal

---

<a id="troubleshooting"></a>
## 🛠️ Troubleshooting

### Port Already in Use

If port 25808 is already in use, AionUi will automatically try the next available port. Check the console output for the actual port number.

### Cannot Access from Browser

1. **Check if the application started successfully**
   - Look for "Server started on port XXXX" message in the console

2. **Try a different browser**
   - Chrome, Firefox, Safari, or Edge

3. **Clear browser cache**
   - Press `Ctrl+Shift+Delete` (Windows/Linux) or `Cmd+Shift+Delete` (macOS)

### Firewall Blocking Access

**Windows:**

```cmd
# Allow through Windows Firewall
netsh advfirewall firewall add rule name="AionUi WebUI" dir=in action=allow protocol=TCP localport=3000
```

**Linux (UFW):**

```bash
sudo ufw allow 3000/tcp
```

**macOS:**
- Go to **System Preferences** → **Security & Privacy** → **Firewall** → **Firewall Options** → Add AionUi

### Application Not Found

**Find application location:**

**Windows:**

```cmd
where AionUi.exe
```

**macOS:**

```bash
mdfind -name "AionUi.app"
```

**Linux:**

```bash
which AionUi
# or
find /usr/bin -name "AionUi" 2>/dev/null
```

### View Logs

**Windows (PowerShell):**

```powershell
& "C:\Program Files\AionUi\AionUi.exe" --webui 2>&1 | Tee-Object -FilePath aionui.log
```

**macOS/Linux:**

```bash
AionUi --webui 2>&1 | tee aionui.log
```

---

<a id="cli"></a>
## 📝 Command Line Options Summary

| Option             | Description                           |
| ------------------ | ------------------------------------- |
| `--webui`          | Start in WebUI mode                  |
| `--remote`         | Allow remote network access           |
| `--webui --remote` | Combine both flags                    |
| `--resetpass`      | Reset admin password (usage above)    |

---

<a id="best-practices"></a>
## 💡 Best Practices

### For Development

- Use `--webui` flag for quick testing
- Enable remote access only on local network
- Keep default admin password secure

### For Production

- Use systemd/LaunchAgent for automatic startup
- Set up firewall rules to restrict access
- Use VPN for external access
- Regularly update your password
- Keep AionUi updated to the latest version

### For Local Network Access

- Ensure all devices are on the same network
- Check your router settings if access doesn't work
- Use your computer's IP address for access

---

## 🔗 Related Resources

- [📖 Getting Started Guide](Getting-Started) - Initial setup and configuration
- [⚙️ LLM Configuration](LLM-Configuration) - Configure AI models
- [🤖 Multi-Agent Setup](ACP-Setup) - Integrate terminal AI agents
- [🔌 MCP Configuration](MCP-Configuration-Guide) - Model Context Protocol setup
- [❓ FAQ](FAQ) - Common issues and solutions

---

## 🌟 Features

### Security

- **HTTPS Ready**: Can be deployed behind a reverse proxy with SSL
- **Session Management**: Automatic session timeout after 24 hours
- **Rate Limiting**: Protection against brute force attacks
- **CSRF Protection**: Built-in cross-site request forgery protection

### Data Storage

- **Local SQLite Database**: All data stored locally
- **No Cloud Storage**: Your conversations never leave your computer
- **Privacy First**: Full control over your data

### Performance

- **Low Resource Usage**: Runs efficiently on most systems
- **WebSocket Real-time**: Real-time updates via WebSocket
- **Efficient Streaming**: Optimized response streaming

---

**Happy using AionUi in WebUI mode!** 🚀

