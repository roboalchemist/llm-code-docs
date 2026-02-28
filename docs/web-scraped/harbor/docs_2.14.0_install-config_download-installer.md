# Harbor docs | Download the Harbor Installer

**Source:** https://goharbor.io/docs/2.14.0/install-config/download-installer/

Download the Harbor Installer

[Harbor version 2.14.0](/docs/2.14.0)

[Harbor Installation and Configuration](/docs/2.14.0/install-config/)

* [Test Harbor with the Demo Server](/docs/2.14.0/install-config/demo-server/)
* [Harbor Compatibility List](/docs/2.14.0/install-config/harbor-compatibility-list/)
* [Harbor Installation Prerequisites](/docs/2.14.0/install-config/installation-prereqs/)
* [Download the Harbor Installer](/docs/2.14.0/install-config/download-installer/)
* [Configure HTTPS Access to Harbor](/docs/2.14.0/install-config/configure-https/)
* [Configure Internal TLS communication between Harbor Component](/docs/2.14.0/install-config/configure-internal-tls/)
* [Configure the Harbor YML File](/docs/2.14.0/install-config/configure-yml-file/)
* [Run the Installer Script](/docs/2.14.0/install-config/run-installer-script/)
* [Deploying Harbor with High Availability via Helm](/docs/2.14.0/install-config/harbor-ha-helm/)
* [Troubleshooting Harbor Installation](/docs/2.14.0/install-config/troubleshoot-installation/)
* [Reconfigure Harbor and Manage the Harbor Lifecycle](/docs/2.14.0/install-config/reconfigure-manage-lifecycle/)
* [Customize the Harbor Token Service](/docs/2.14.0/install-config/customize-token-service/)
* [Harbor Configuration](/docs/2.14.0/install-config/configure-system-settings-cli/)

[Harbor Administration](/docs/2.14.0/administration/)

[Working with Projects](/docs/2.14.0/working-with-projects/)

[Building, Customizing, and Contributing to Harbor](/docs/2.14.0/build-customize-contribute/)

You can download the Harbor installers from the
[official releases](https://github.com/goharbor/harbor/releases) page. Download either the online installer or the offline installer.

* **Online installer:** The online installer downloads the Harbor images from Docker hub. For this reason, the installer is very small in size.
* **Offline installer:** Use the offline installer if the host to which are deploying Harbor does not have a connection to the Internet. The offline installer contains pre-built images, so it is larger than the online installer.

The installation processes are almost the same for the online and offline installers.

## Download and Unpack the Installer

1. Go to the
   [Harbor releases page](https://github.com/goharbor/harbor/releases).
2. Download the online or offline installer for the version you want to install.
3. Optionally download the corresponding `*.asc` file to verify that the package is genuine.

   The `*.asc` file is an OpenPGP key file. Perform the following steps to verify that the downloaded bundle is genuine.

   1. Obtain the public key for the `*.asc` file.

      ```
      gpg --keyserver hkps://keyserver.ubuntu.com --receive-keys 644FF454C0B4115C
      ```

      You should see the message  `public key "Harbor-sign (The key for signing Harbor build) <jiangd@vmware.com>" imported`
   2. Verify that the package is genuine by running one of the following commands.

      * Online installer:

        ```
        gpg -v --keyserver hkps://keyserver.ubuntu.com --verify harbor-online-installer-version.tgz.asc
        ```
      * Offline installer:

        ```
        gpg -v --keyserver hkps://keyserver.ubuntu.com --verify harbor-offline-installer-version.tgz.asc
        ```

      The `gpg` command verifies that the bundle’s signature matches that of the `*.asc` key file. You should see confirmation that the signature is correct.

      ```
      gpg: armor header: Version: GnuPG v1
      gpg: assuming signed data in 'harbor-online-installer-v2.0.2.tgz'
      gpg: Signature made Tue Jul 28 09:49:20 2020 UTC
      gpg:                using RSA key 644FF454C0B4115C
      gpg: using pgp trust model
      gpg: Good signature from "Harbor-sign (The key for signing Harbor build) <jiangd@vmware.com>" [unknown]
      gpg: WARNING: This key is not certified with a trusted signature!
      gpg:          There is no indication that the signature belongs to the owner.
      Primary key fingerprint: 7722 D168 DAEC 4578 06C9  6FF9 644F F454 C0B4 115C
      gpg: binary signature, digest algorithm SHA1, key algorithm rsa4096
      ```
4. Use `tar` to extract the installer package:

   * Online installer:

     ```
     bash $ tar xzvf harbor-online-installer-version.tgz
     ```
   * Offline installer:

     ```
     bash $ tar xzvf harbor-offline-installer-version.tgz
     ```

## Next Steps

* To secure the connections to Harbor, see
  [Configure HTTPS Access to Harbor](/docs/2.14.0/install-config/configure-https/).
* To configure your Harbor installation, see
  [Configure the Harbor YML File](/docs/2.14.0/install-config/configure-yml-file/).

On this page

  
  

Contributing

[Page source](https://github.com/goharbor/website/blob/release-2.14.0/docs/install-config/download-installer.md)
[Create issue](https://github.com/goharbor/harbor/issues)