# Source: https://docs.curator.interworks.com/setup/ssl/windows_ssl.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Windows SSL

> Configure SSL/HTTPS for Curator installations on Windows servers with IIS.

## Finding relevant files

1. Find the **`curator.conf`** file (default location is `C:\InterWorks\Curator\curator.conf`).
2. Find the relevant keys. These will either be in a bundle, or separated into key, certificate, and chain files.
3. Put your keys into the correct directory (default location is `C:\InterWorks\Curator\certs\`).

## Removing Passphrases (Required, if applicable)

If your certificate utilizes a passphrase, you'll need to remove it in order to use the certificate with Curator since
passphrases are not supported by Apache on Microsoft Windows servers.

1. Curator uses "Apache" type certificates. These may be referred to as "OpenSSL" or PEM certificates as well.
2. Windows is unique in that it cannot use certificates with embedded passphrases,
   so these have to be removed if they are present.
   These passphrases would normally be required before a restart of your web server on other operating systems,
   but are not able to be used here.
3. To remove the passphrases, you can use this command in the same directory as the certificates using Powershell.

   ```bash  theme={null}
   & 'C:\InterWorks\Curator\libs\Apache24\bin\openssl.exe' rsa -in [original.key] -out [new.key]
   ```

## Replacing References

1. Locate the references in the file (listed below) and replace your new .crt, .pem, and .key files where they are
   referenced in the `curator.conf` file.

2. Un-comment the lines (by deleting the `#` at the front of the line) starting at `Listen 443` and ending at
   `</IfModule>`.  See example below:

   ```conf  theme={null}
   #Uncomment the lines below for SSL
   Listen 443
   <IfModule mod_ssl.c>
       <VirtualHost _default_:443>
           SSLEngine on
           ServerName www.example.com
           DocumentRoot "C:\InterWorks\Curator\htdocs"
           RewriteEngine on

           SSLCertificateChainFile C:\InterWorks\Curator\certs\chain.crt
           SSLCertificateFile C:\InterWorks\Curator\certs\cert.pem
           SSLCertificateKeyFile C:\InterWorks\Curator\certs\cert.key

           SSLProtocol                 [protocol]
           SSLCipherSuite              [ciphersuite]
           SSLHonorCipherOrder         on
           SSLCompression              off

           <Directory "C:\InterWorks\Curator\htdocs">
               AllowOverride All
               Options Indexes FollowSymLinks
               Require all granted
           </Directory>
   </VirtualHost>
   </IfModule>
   ```

3. After the configuration file has been edited and saved, restart Curator.

## SSL Protocols / Ciphers (Optional)

1. You may wish to update your SSL protocols and cipher suites. To do this, you'll need a little more info about your
   environment. Run the command below to get your Apache and OpenSSL versions, assuming default install locations for both:

   ```bash  theme={null}
   & 'C:\InterWorks\Curator\libs\Apache24\bin\httpd.exe' -v; & 'C:\InterWorks\Curator\libs\Apache24\bin\openssl.exe' version
   ```

2. The expected output will look something like this:

   ```bash  theme={null}
   Server version: Apache/2.4.59 (Win 64)
   OpenSSL 3.3.1 4 Jun 2024 (Library: OpenSSL 3.3.1 4 Jun 2024)
   ```

3. Take the information retrieved in the previous step and use it to fill out the form on this
   [SSL Certificate Generator site](https://ssl-config.mozilla.org/#server=apache).

   * Select **Apache** for "Server Software"
   * Select **Intermediate** for "Mozilla Configuration".
   * Enter your Apache version
   * Enter your OpenSSL version

4. Replace the appropriate areas in the `curator.conf` file with the SSLProtocol and SSLCipherSuite that was generated
   on the SSL Certificate Generator site.

   For example:

   ```conf  theme={null}
   SSLProtocol             all -SSLv3 -TLSv1 -TLSv1.1
   SSLCipherSuite          ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:
   ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:
   DHE-RSA-AES256-GCM-SHA384:DHE-RSA-CHACHA20-POLY1305
   ```

5. Have a server open to the internet? Qualys has a free tool to test the certificates, protocols/ciphers, and their
   security: [https://www.ssllabs.com/ssltest/analyze.html](https://www.ssllabs.com/ssltest/analyze.html)

## Troubleshooting

If Apache fails to start after configuring SSL, see the
[Windows Apache SSL Troubleshooting](/setup/ssl/windows_ssl_troubleshooting) guide for step-by-step diagnostics
and fixes for common issues.
