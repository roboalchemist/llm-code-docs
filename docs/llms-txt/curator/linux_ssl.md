# Source: https://docs.curator.interworks.com/setup/ssl/linux_ssl.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Linux SSL

> Configure SSL certificates and HTTPS encryption for Curator on Linux systems

1. First, find your `curator.conf` file. For Ubuntu installations, this is located in `/etc/apache2/sites-enabled`. For
   all other Linux distributions, this file is located in `/etc/httpd/conf.d/curator.conf`. If you cannot find this file,
   you may have an old Curator installation. If so,
   [download `curator.conf` here](https://api.curator.interworks.com/file/curator_conf).

2. Upload your SSL certificate, key, and (optionally) chain files to the webserver. This can be done with a secure copy
   (SCP) client, such as FileZilla. Place these certificates in */etc/apache2/certs* for Ubuntu, or */etc/httpd/certs*, for
   all other Linux distributions.

3. Replace the references to SSLCertificateChainFile, SSLCertificateFile, and SSLCertificateKeyFile in the `curator.conf`
   to the location you uploaded them to in Step #2.

4. Save the contents of the file and restart apache with the commands below:

   ```bash  theme={null}
   sudo apachectl restart
   ```

5. Navigate to the HTTPS version of the link to your portal in your browser (i.e. `https://curatorexample.com`). You
   should see a lock icon appear in the URL bar after the site loads to indicate that it is successfully encrypted. If you
   don’t see the lock or if you get an error, check your certificate for invalid information, such as incorrect site name
   or missing Subject Alternative Names.

## Debugging SSL

Having issues? It happens! SSL certificates can be uniquely challenging to implement. Here are a few debugging tips:

1. Make sure the certificate and key match. Often these get mismatched. Your server will not start if they do not match.
   If either of these commands errors, you may not have correctly formatted certificates. Make sure you acquired Apache/PEM
   certificates:

   ```bash  theme={null}
   openssl rsa -modulus -noout -in yourKeyFile.key | openssl md5
   openssl x509 -modulus -noout -in myServer.crt | openssl md5
   ```

2. The certificate chain file is important, but can cause issues. If your Curator server won't start, try commenting out
   the SSLCertificateChainFile line in `curator.conf` temporarily to ensure that the issue is not the chain file.

3. Check Apache/HTTPD's error log. This can be found in /var/log/apache2/error\_log (Ubuntu) or /var/log/httpd/error\_log
   (All other distros). Also check `/var/www/curator_error.log`, if it exists. If the error message is not detailed enough,
   try increasing "LogLevel" to "debug" in `curator.conf`. (Note: be sure to set this value back to "warn" after you are done!)

## Notes on obtaining SSL certificates

1. Curator uses "Apache" type certificates. These may be referred to as "OpenSSL" or PEM certificates as well.
2. These certificates may in one big bundle, or separated into key, certificate, and chain files.
3. When installing key certificates, many providers require a key-passphrase.
   Once installed on the Curator server and at rest, you may wish to remove this passphrase.
   If the passphrase remains, it will be required anytime there is a restart of the web server.
   **STORE THE PASSPHRASE IN A SAFE PLACE. IF IT REMAINS ON THE KEY AND IS LOST YOU WILL HAVE TO GENERATE NEW CERTIFICATES.**
   To remove the passphrase, use this command.

   ```bash  theme={null}
   openssl rsa -in [original.key] -out [new.key]
   ```

## SSL Protocols / Ciphers (Optional)

1. You may wish to update your SSL protocols and cipher suites. To do this, you'll need a little more info about your
   web server. Run the command below to get the Apache and OpenSSL versions:

   ```bash  theme={null}
   httpd -V 2>/dev/null | grep version; apache2 -V 2>/dev/null | grep version; openssl version; php -v | grep cli
   ```

2. The expected output will look something like this:

   ```bash  theme={null}
   Server version: Apache/2.4.48 ()
   OpenSSL 1.0.2k-fips  26 Jan 2017
   PHP 7.4.21 (cli) (built: Jul  7 2021 17:35:08) ( NTS )
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
   SSLCipherSuite          ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384
   ```

5. Have a server open to the internet? Qualys has a free tool to test the certificates, protocols/ciphers, and their
   security: [https://www.ssllabs.com/ssltest/analyze.html](https://www.ssllabs.com/ssltest/analyze.html)
