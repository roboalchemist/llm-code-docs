# Source: https://docs.curator.interworks.com/setup/ssl/windows_ssl_troubleshooting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Windows Apache SSL Troubleshooting

> Diagnose and resolve common Apache SSL startup failures on Windows servers running Curator.

If Apache fails to start after configuring SSL on a Windows Curator installation, work through the steps below
to identify and resolve the issue.

<Note>
  The examples below use the default installation path `C:\InterWorks\Curator`. If Curator was installed on a
  different drive or directory, adjust the paths accordingly (e.g. `D:\InterWorks\Curator`).
</Note>

## Step 1: Test the Configuration From the Command Line

Open PowerShell as Administrator and run:

```bash  theme={null}
& 'C:\InterWorks\Curator\libs\Apache24\bin\httpd.exe' -t
```

This validates the configuration and outputs a specific error message pointing to the exact file, line number, and
problem. If everything is valid, it outputs `Syntax OK`.

<Note>
  This is the fastest way to identify the issue. If the output points to a clear problem, skip to
  [Common SSL Issues and Fixes](#common-ssl-issues-and-fixes) for the resolution.
</Note>

## Step 2: Check the Apache Error Log

If Step 1 wasn't sufficient, check the Apache error log:

```
C:\InterWorks\Curator\libs\Apache24\logs\error.log
```

Open this in Notepad — the most recent entries at the bottom will show what went wrong during the last startup attempt.

## Step 3: Check the Windows Event Log

1. Attempt to start the **Curator HTTPD Server** service from the Windows Services Manager.
2. After it fails, press **Win + R**, type `eventvwr.msc`, and press **Enter**.
3. Navigate to **Windows Logs** > **Application**.
4. The most recent error entries at the top will be from the failed startup attempt — double-click them and read
   the **Description** field for the actual error message.

## Common SSL Issues and Fixes

<AccordionGroup>
  <Accordion title="Certificate key has a passphrase (most common on Windows)">
    **Error:** `SSLPassPhraseDialog builtin is not supported on Win32` or the service hangs waiting for passphrase input.

    **Fix:** Strip the passphrase from the key:

    ```bash  theme={null}
    & 'C:\InterWorks\Curator\libs\Apache24\bin\openssl.exe' rsa -in C:\InterWorks\Curator\certs\your_key.key -out C:\InterWorks\Curator\certs\your_key_nopass.key
    ```

    Then update `SSLCertificateKeyFile` in `C:\InterWorks\Curator\curator.conf` to point to the new key.

    See also: [Removing Passphrases](/setup/ssl/windows_ssl#removing-passphrases-required-if-applicable) in the
    Windows SSL setup guide.
  </Accordion>

  <Accordion title="Certificate file path is wrong or file missing">
    **Error:** `SSLCertificateFile: file 'C:\...' does not exist or is empty`

    **Fix:** Verify the paths in `C:\InterWorks\Curator\curator.conf` for these directives all point to files that
    actually exist in `C:\InterWorks\Curator\certs\`:

    * `SSLCertificateFile`
    * `SSLCertificateKeyFile`
    * `SSLCertificateChainFile`
  </Accordion>

  <Accordion title="SSL section not fully uncommented in curator.conf">
    **Error:** Syntax errors referencing lines in the SSL block.

    **Fix:** Open `C:\InterWorks\Curator\curator.conf` and ensure the entire `<VirtualHost *:443>` block and the
    `Listen 443` line are fully uncommented (no stray `#` characters).

    See: [Replacing References](/setup/ssl/windows_ssl#replacing-references) in the Windows SSL setup guide.
  </Accordion>

  <Accordion title="Chain/intermediate certificate file missing">
    **Error:** `SSLCertificateChainFile: file does not exist`

    **Fix:** Ensure the CA intermediate/chain certificate is in the certs directory and referenced correctly. If you
    have a single combined cert, comment out the `SSLCertificateChainFile` directive.
  </Accordion>

  <Accordion title="Certificate and key don't match">
    **Error:** `certificate and private key do not match`

    **Fix:** Verify they match by comparing their modulus hashes:

    ```bash  theme={null}
    & 'C:\InterWorks\Curator\libs\Apache24\bin\openssl.exe' x509 -noout -modulus -in C:\InterWorks\Curator\certs\your_cert.crt | & 'C:\InterWorks\Curator\libs\Apache24\bin\openssl.exe' md5
    & 'C:\InterWorks\Curator\libs\Apache24\bin\openssl.exe' rsa -noout -modulus -in C:\InterWorks\Curator\certs\your_key.key | & 'C:\InterWorks\Curator\libs\Apache24\bin\openssl.exe' md5
    ```

    Both commands should output the same hash. If they don't, the wrong key or certificate file is being used.
  </Accordion>

  <Accordion title="Port 443 already in use">
    **Error:** `could not bind to address 0.0.0.0:443`

    **Fix:** Check what's using port 443:

    ```bash  theme={null}
    netstat -ano | findstr :443
    ```

    If IIS or another service is on port 443, stop it or change the Curator port.
  </Accordion>

  <Accordion title="Certificate in wrong format (DER instead of PEM)">
    **Error:** `error reading certificate` or `PEM routines:get_name:no start line`

    **Fix:** Apache requires PEM format (text starting with `-----BEGIN CERTIFICATE-----`). Convert from DER if needed:

    ```bash  theme={null}
    & 'C:\InterWorks\Curator\libs\Apache24\bin\openssl.exe' x509 -inform DER -in your_cert.cer -out your_cert.pem
    ```
  </Accordion>
</AccordionGroup>

## After Fixing

1. Re-run the config test:

   ```bash  theme={null}
   & 'C:\InterWorks\Curator\libs\Apache24\bin\httpd.exe' -t
   ```

2. If it says `Syntax OK`, start the **Curator HTTPD Server** service from Services Manager.
