# Source: https://rustdesk.com/docs/en/self-host/rustdesk-server-oss/windows/

# Windows & PM2 or NSSM

Note

Windows security policy is tricky, if this tutorial does not work for you, or you encounter unstable connection, please migrate to a Linux server.

Note

The GUI version, `RustDeskServer.setup.exe` has not been maintained any more, not recommended.

## A crossroads

You now either have two choices, you can either use PM2 (easier) or NSSM (a bit harder) to start the RustDesk server
There are some benefits to using NSSM:

- Backwards compatibility with older Windows (Windows Server 2008 R2/Windows 7 and earlier although untested).
- Ideal for Windows Server
- Auto start on boot without login (The user who created the startup entry does not need to log on for it to start).
- Running both binaries as Services.
- Standalone (no dependency on Node.js)

While the benefits of PM2 include:

- Good idea if you run the server on the same computer as your main work computer
- You logon regularly to the user that created the RustDesk startup entry
- More user friendly

## Installing using NSSM

### Installing NSSM

Please download and extract NSSM select the appropriate
architecture to your Windows system (if x86 use the contents of the win32 folder, if x64 use the
contents of win64 folder). It is also best practice to move the binary of NSSM into the
`Program Files\NSSM` (NSSM once started as a service, it cannot be moved from the directory it was placed in.
thus it is best to tuck it away in `Program Files`) directory of your Installation drive (Usually the C: drive).
It is also advisable to add the path (such as `C:\Program Files\NSSM`) to the path variable.

### Checking if NSSM is installed properly

If you&rsquo;ve done everything correctly the folder `C:\Program Files\NSSM` (in this example I use the C:
drive but you can use whatever drive you installed Windows to or whatever path you desire) should
only contain the file `nssm.exe`.

We will be using `C:\Program Files\NSSM` in this example.

Open Command prompt and run `nssm` if you see a help page you are ready to move onto the next step.

### Run hbbr and hbbs

Download the Windows version of RustDesk Server.
Unzip the program to the `C:\Program Files\RustDesk Server` (or anywhere you desire just make sure it
doesn&rsquo;t change after the service is installed). Now get back to Command prompt.

We will be using `C:\Program Files\RustDesk Server` in this example.

```
nssm install &#34;RustDesk hbbs service&#34; &#34;C:\Program Files\RustDesk Server\hbbs.exe&#34;
nssm install &#34;RustDesk hbbr service&#34; &#34;C:\Program Files\RustDesk Server\hbbr.exe&#34;
```

**Note:**

- You can change `RustDesk hbbs service` to whatever you desire to name hbbs the service
- You can change `RustDesk hbbr service` to whatever you desire to name hbbr the service
- You can change `C:\Program Files\RustDesk Server\hbbs.exe` to wherever you placed the RustDesk binaries
- You can change `C:\Program Files\RustDesk Server\hbbr.exe` to wherever you placed the RustDesk binaries

**Command templates:**

The command template in case you just want to copy and paste and edit.

```
nssm install <Desired hbbs servicename> <RustDesk hbbs binary path> <RustDesk hbbs arguments>
nssm install <Desired hbbr servicename> <RustDesk hbbr binary path> <RustDesk hbbr arguments>
```

**Start services**

After successful installation of services, they need to be started.

```
nssm start <Desired hbbs servicename>
nssm start <Desired hbbr servicename>
```

**Done!**

(The method above has been tested on Windows Server Core 2022 Standard).

## or

## Installing using PM2

### Install Node.js

Please download and install Node.js.
Node.js is the runtime environment of PM2, so you need to install Node.js first.

### Install PM2

Enter belows in `cmd.exe`, press the Enter key for each line, and run them line by line.

```
npm install -g pm2
npm install pm2-windows-startup -g
pm2-startup install
```

### Run hbbr and hbbs

Download the Windows version of RustDesk Server. Unzip the program to the C: drive. Run the following four commands:

```
cd C:\rustdesk-server-windows-x64
pm2 start hbbs.exe
pm2 start hbbr.exe
pm2 save
```

### View the log

```
pm2 log hbbr
pm2 log hbbs
```

## Alternative tutorials

[https://pedja.supurovic.net/setting-up-self-hosted-rustdesk-server-on-windows/?lang=lat](https://pedja.supurovic.net/setting-up-self-hosted-rustdesk-server-on-windows/?lang=lat)