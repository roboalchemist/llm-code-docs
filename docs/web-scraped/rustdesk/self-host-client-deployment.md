# Source: https://rustdesk.com/docs/en/self-host/client-deployment/

# Client Deployment

The simplest way is to use custom client, https://twitter.com/rustdesk/status/1788905463678951787.

You can deploy using a number of methods, some are covered in Client Configuration.

Alternatively you can use mass deployment scripts with your RMM, Intune, etc. The ID and password are output by the script. You should collect this or split it into different scripts to collect the ID and password.

The permanent password can be changed from random to one you prefer using by changing the content inside `()` after `rustdesk_pw` to your preferred password for PowerShell and the corresponding line for any other platform.

## PowerShell

```
$ErrorActionPreference= 'silentlycontinue'

# Assign the value random password to the password variable
$rustdesk_pw=(-join ((65..90) + (97..122) | Get-Random -Count 12 | % {[char]$_}))

# Get your config string from your Web portal and Fill Below
$rustdesk_cfg=&#34;configstring&#34;

################################## Please Do Not Edit Below This Line #########################################

# Run as administrator and stays in the current directory
if (-Not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator))
{
    if ([int](Get-CimInstance -Class Win32_OperatingSystem | Select-Object -ExpandProperty BuildNumber) -ge 6000)
    {
        Start-Process PowerShell -Verb RunAs -ArgumentList &#34;-NoProfile -ExecutionPolicy Bypass -Command `&#34;cd '$pwd'; & '$PSCommandPath';`&#34;&#34;;
        Exit;
    }
}

# This function will return the latest version and download link as an object
function getLatest()
{
    $Page = Invoke-WebRequest -Uri 'https://github.com/rustdesk/rustdesk/releases/latest' -UseBasicParsing
    $HTML = New-Object -Com &#34;HTMLFile&#34;
    try
    {
        $HTML.IHTMLDocument2_write($Page.Content)
    }
    catch
    {
        $src = [System.Text.Encoding]::Unicode.GetBytes($Page.Content)
        $HTML.write($src)
    }

    # Current example link: https://github.com/rustdesk/rustdesk/releases/download/1.2.6/rustdesk-1.2.6-x86_64.exe
    $Downloadlink = ($HTML.Links | Where {$_.href -match '(.)+\/rustdesk\/rustdesk\/releases\/download\/\d{1}.\d{1,2}.\d{1,2}(.{0,3})\/rustdesk(.)+x86_64.exe'} | select -first 1).href

    # bugfix - sometimes you need to replace &#34;about:&#34;
    $Downloadlink = $Downloadlink.Replace('about:', 'https://github.com')

    $Version = &#34;unknown&#34;
    if ($Downloadlink -match './rustdesk/rustdesk/releases/download/(?<content>.*)/rustdesk-(.)+x86_64.exe')
    {
        $Version = $matches['content']
    }

    if ($Version -eq &#34;unknown&#34; -or $Downloadlink -eq &#34;&#34;)
    {
        Write-Output &#34;ERROR: Version or download link not found.&#34;
        Exit
    }

    # Create object to return
    $params += @{Version = $Version}
    $params += @{Downloadlink = $Downloadlink}
    $Result = New-Object PSObject -Property $params

    return($Result)
}

$RustDeskOnGitHub = getLatest

$rdver = ((Get-ItemProperty  &#34;HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\RustDesk\&#34;).Version)

if ($rdver -eq $RustDeskOnGitHub.Version)
{
    Write-Output &#34;RustDesk $rdver is the newest version.&#34;
    Exit
}

if (!(Test-Path C:\Temp))
{
    New-Item -ItemType Directory -Force -Path C:\Temp | Out-Null
}

cd C:\Temp

Invoke-WebRequest $RustDeskOnGitHub.Downloadlink -Outfile &#34;rustdesk.exe&#34;
Start-Process .\rustdesk.exe --silent-install
Start-Sleep -seconds 20

$ServiceName = 'Rustdesk'
$arrService = Get-Service -Name $ServiceName -ErrorAction SilentlyContinue

if ($arrService -eq $null)
{
    Write-Output &#34;Installing service&#34;
    cd $env:ProgramFiles\RustDesk
    Start-Process .\rustdesk.exe --install-service
    Start-Sleep -seconds 20
    $arrService = Get-Service -Name $ServiceName
}

while ($arrService.Status -ne 'Running')
{
    Start-Service $ServiceName
    Start-Sleep -seconds 5
    $arrService.Refresh()
}

cd $env:ProgramFiles\RustDesk\
.\rustdesk.exe --get-id | Write-Output -OutVariable rustdesk_id

.\rustdesk.exe --config $rustdesk_cfg

.\rustdesk.exe --password $rustdesk_pw

Write-Output &#34;...............................................&#34;
# Show the value of the ID Variable
Write-Output &#34;RustDesk ID: $rustdesk_id&#34;

# Show the value of the Password Variable
Write-Output &#34;Password: $rustdesk_pw&#34;
Write-Output &#34;...............................................&#34;
```

## Windows batch/cmd

```
@echo off

REM Assign the value random password to the password variable
setlocal ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION
set alfanum=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789
set rustdesk_pw=
for /L %%b in (1, 1, 12) do (
    set /A rnd_num=!RANDOM! %% 62
    for %%c in (!rnd_num!) do (
        set rustdesk_pw=!rustdesk_pw!!alfanum:~%%c,1!
    )
)

REM Get your config string from your Web portal and Fill Below
set rustdesk_cfg=&#34;configstring&#34;

REM ############################### Please Do Not Edit Below This Line #########################################

if not exist C:\Temp\ md C:\Temp\
cd C:\Temp\

curl -L &#34;https://github.com/rustdesk/rustdesk/releases/download/1.2.6/rustdesk-1.2.6-x86_64.exe&#34; -o rustdesk.exe

rustdesk.exe --silent-install
timeout /t 20

cd &#34;C:\Program Files\RustDesk\&#34;
rustdesk.exe --install-service
timeout /t 20

for /f &#34;delims=&#34; %%i in ('rustdesk.exe --get-id ^| more') do set rustdesk_id=%%i

rustdesk.exe --config %rustdesk_cfg%

rustdesk.exe --password %rustdesk_pw%

echo ...............................................
REM Show the value of the ID Variable
echo RustDesk ID: %rustdesk_id%

REM Show the value of the Password Variable
echo Password: %rustdesk_pw%
echo ...............................................
```

## MSI

You can also use msi instead of `rustdesk.exe --silent-install`.

https://rustdesk.com/docs/en/client/windows/msi/

## Winget

you can deploy via powershell with winget as well (this installs via microsofts version of apt - part of most recent windows installs)

from a powershell window or via script (for example via GPO)

```
winget install --id=RustDesk.RustDesk  -e
```

## macOS Bash

```
#!/bin/bash

# Assign the value random password to the password variable
rustdesk_pw=$(openssl rand -hex 4)

# Get your config string from your Web portal and Fill Below
rustdesk_cfg=&#34;configstring&#34;

################################## Please Do Not Edit Below This Line #########################################

# Root password request for privilege escalation
[ &#34;$UID&#34; -eq 0 ] || exec sudo bash &#34;$0&#34; &#34;$@&#34;

# Specify the mount point for the DMG (temporary directory)
mount_point=&#34;/Volumes/RustDesk&#34;

# Download the rustdesk.dmg file
echo &#34;Downloading RustDesk Now&#34;

if [[ $(arch) == 'arm64' ]]; then
    rd_link=$(curl -sL https://github.com/rustdesk/rustdesk/releases/latest | grep -Eo &#34;(http|https)://[a-zA-Z0-9./?=_-]*/\d{1}.\d{1,2}.\d{1,2}/rustdesk.\d{1}.\d{1,2}.\d{1,2}.aarch64.dmg&#34;)
    dmg_file=$(echo $rd_link | grep -Eo &#34;rustdesk.\d{1}.\d{1,2}.\d{1,2}.aarch64.dmg&#34;)
    curl -L &#34;$rd_link&#34; --output &#34;$dmg_file&#34;
else
    rd_link=$(curl -sL https://github.com/rustdesk/rustdesk/releases/latest | grep -Eo &#34;(http|https)://[a-zA-Z0-9./?=_-]*/\d{1}.\d{1,2}.\d{1,2}/rustdesk.\d{1}.\d{1,2}.\d{1,2}.x86_64.dmg&#34;)
    dmg_file=$(echo $rd_link | grep -Eo &#34;rustdesk.\d{1}.\d{1,2}.\d{1,2}.x86_64.dmg&#34;)
    curl -L &#34;$rd_link&#34; --output &#34;$dmg_file&#34;
fi

# Mount the DMG file to the specified mount point
hdiutil attach &#34;$dmg_file&#34; -mountpoint &#34;$mount_point&#34; &> /dev/null

# Check if the mounting was successful
if [ $? -eq 0 ]; then
    # Move the contents of the mounted DMG to the /Applications folder
    cp -R &#34;$mount_point/RustDesk.app&#34; &#34;/Applications/&#34; &> /dev/null

    # Unmount the DMG file
    hdiutil detach &#34;$mount_point&#34; &> /dev/null
else
    echo &#34;Failed to mount the RustDesk DMG. Installation aborted.&#34;
    exit 1
fi

# Run the rustdesk command with --get-id and store the output in the rustdesk_id variable
cd /Applications/RustDesk.app/Contents/MacOS/
rustdesk_id=$(./RustDesk --get-id)

# Apply new password to RustDesk
./RustDesk --server &
/Applications/RustDesk.app/Contents/MacOS/RustDesk --password $rustdesk_pw &> /dev/null

/Applications/RustDesk.app/Contents/MacOS/RustDesk --config $rustdesk_cfg

# Kill all processes named RustDesk
rdpid=$(pgrep RustDesk)
kill $rdpid &> /dev/null

echo &#34;...............................................&#34;
# Check if the rustdesk_id is not empty
if [ -n &#34;$rustdesk_id&#34; ]; then
    echo &#34;RustDesk ID: $rustdesk_id&#34;
else
    echo &#34;Failed to get RustDesk ID.&#34;
fi

# Echo the value of the password variable
echo &#34;Password: $rustdesk_pw&#34;
echo &#34;...............................................&#34;

echo &#34;Please complete install on GUI, launching RustDesk now.&#34;
open -n /Applications/RustDesk.app
```

## Linux

```
#!/bin/bash

# Assign a random value to the password variable
rustdesk_pw=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 8 | head -n 1)

# Get your config string from your Web portal and Fill Below
rustdesk_cfg=&#34;configstring&#34;

################################## Please Do Not Edit Below This Line #########################################

# Check if the script is being run as root
if [[ $EUID -ne 0 ]]; then
    echo &#34;This script must be run as root.&#34;
    exit 1
fi

# Identify OS
if [ -f /etc/os-release ]; then
    # freedesktop.org and systemd
    . /etc/os-release
    OS=$NAME
    VER=$VERSION_ID

    UPSTREAM_ID=${ID_LIKE,,}

    # Fallback to ID_LIKE if ID was not 'ubuntu' or 'debian'
    if [ &#34;${UPSTREAM_ID}&#34; != &#34;debian&#34; ] && [ &#34;${UPSTREAM_ID}&#34; != &#34;ubuntu&#34; ]; then
        UPSTREAM_ID=&#34;$(echo ${ID_LIKE,,} | sed s/\&#34;//g | cut -d' ' -f1)&#34;
    fi

elif type lsb_release >/dev/null 2>&1; then
    # linuxbase.org
    OS=$(lsb_release -si)
    VER=$(lsb_release -sr)
elif [ -f /etc/lsb-release ]; then
    # For some versions of Debian/Ubuntu without lsb_release command
    . /etc/lsb-release
    OS=$DISTRIB_ID
    VER=$DISTRIB_RELEASE
elif [ -f /etc/debian_version ]; then
    # Older Debian, Ubuntu, etc.
    OS=Debian
    VER=$(cat /etc/debian_version)
elif [ -f /etc/SuSE-release ]; then
    # Older SuSE etc.
    OS=SuSE
    VER=$(cat /etc/SuSE-release)
elif [ -f /etc/redhat-release ]; then
    # Older Red Hat, CentOS, etc.
    OS=RedHat
    VER=$(cat /etc/redhat-release)
else
    # Fall back to uname, e.g. &#34;Linux <version>&#34;, also works for BSD, etc.
    OS=$(uname -s)
    VER=$(uname -r)
fi

# Install RustDesk

echo &#34;Installing RustDesk&#34;
if [ &#34;${ID}&#34; = &#34;debian&#34; ] || [ &#34;$OS&#34; = &#34;Ubuntu&#34; ] || [ &#34;$OS&#34; = &#34;Debian&#34; ] || [ &#34;${UPSTREAM_ID}&#34; = &#34;ubuntu&#34; ] || [ &#34;${UPSTREAM_ID}&#34; = &#34;debian&#34; ]; then
    wget https://github.com/rustdesk/rustdesk/releases/download/1.2.6/rustdesk-1.2.6-x86_64.deb
    apt-get install -fy ./rustdesk-1.2.6-x86_64.deb > null
elif [ &#34;$OS&#34; = &#34;CentOS&#34; ] || [ &#34;$OS&#34; = &#34;RedHat&#34; ] || [ &#34;$OS&#34; = &#34;Fedora Linux&#34; ] || [ &#34;${UPSTREAM_ID}&#34; = &#34;rhel&#34; ] || [ &#34;$OS&#34; = &#34;Almalinux&#34; ] || [ &#34;$OS&#34; = &#34;Rocky*&#34; ] ; then
    wget https://github.com/rustdesk/rustdesk/releases/download/1.2.6/rustdesk-1.2.6-0.x86_64.rpm
    yum localinstall ./rustdesk-1.2.6-0.x86_64.rpm -y > null
else
    echo &#34;Unsupported OS&#34;
    # here you could ask the user for permission to try and install anyway
    # if they say yes, then do the install
    # if they say no, exit the script
    exit 1
fi

# Run the rustdesk command with --get-id and store the output in the rustdesk_id variable
rustdesk_id=$(rustdesk --get-id)

# Apply new password to RustDesk
rustdesk --password $rustdesk_pw &> /dev/null

rustdesk --config $rustdesk_cfg

systemctl restart rustdesk

echo &#34;...............................................&#34;
# Check if the rustdesk_id is not empty
if [ -n &#34;$rustdesk_id&#34; ]; then
    echo &#34;RustDesk ID: $rustdesk_id&#34;
else
    echo &#34;Failed to get RustDesk ID.&#34;
fi

# Echo the value of the password variable
echo &#34;Password: $rustdesk_pw&#34;
echo &#34;...............................................&#34;
```