# Source: https://developers.webflow.com/browser/data-exports/destinations/sftp.mdx

***

title: SFTP
slug: data-exports/destinations/sftp
description: Configure SFTP as a destination for Data Exports
-------------------------------------------------------------

This guide walks you through configuring SFTP as a destination for your Webflow Analyze and Optimize data export.

## Prerequisites

* By default, SFTP uses keypair authentication for access. You will need a provided `public key` to configure your destination. It will look roughly like this:

```json
ssh-key <ssh_public_key_beginning_with_AAAA> some-comment
```

## Configuration steps

<Steps>
  ### Create a user on the SFTP server

  Log in to the SFTP server and complete the steps below.

  1. Create group `sftpwriter`:

     ```shell
     sudo groupadd sftpwriter
     ```

  2. Create user `sftpwriter`:

     ```shell
     sudo useradd -m -g sftpwriter sftpwriter
     ```

  3. Switch to the `sftpwriter` user:

     ```shell
     sudo su - sftpwriter
     ```

  4. Create the `.ssh` directory:

     ```shell
     mkdir ~/.ssh
     ```

  5. Set permissions:

     ```shell
     chmod 700 ~/.ssh
     ```

  6. Navigate to the `.ssh` directory:

     ```shell
     cd ~/.ssh
     ```

  7. Create the `authorized_keys` file:

     ```shell
     touch authorized_keys
     ```

  8. Set permissions:

     ```shell
     chmod 600 authorized_keys
     ```

  9. Add the public key to the `authorized_keys` file. *The key -- including the "ssh-key" and comment -- should be all on one line in the file, without linebreaks.*

     ```shell
     echo "ssh-key <ssh_public_key_beginning_with_AAAA> sftpwriter-public-key" > authorized_keys
     ```

  ### Add your destination

  Use the following details to complete the connection setup: **host name**, **folder name**, **username**, **port** and preferred **delimiter character**.

  * Instructions for [Analyze / Optimize for Webflow sites](https://help.webflow.com/hc/en-us/articles/49269430371219)
  * Instructions for [Optimize for non-Webflow sites](https://help-optimize.webflow.com/hc/en-us/articles/49271451687699)

  <Note>
    **Write permissions at the SFTP root are required**

    In addition to write access within your configured `<folder>`, this destination writes per-transfer manifest files under a `_manifests/` directory created at the root of the SFTP home/path. Ensure the SFTP user can create and write to `_manifests` at that root (even if your data lands under a subfolder). Manifests allow downstream systems to detect when a transfer is complete. See the FAQ below for how these files are organized.
  </Note>
</Steps>

## FAQ

<Accordion title="How will the data appear in my SFTP server?">
  The data will be loaded with the configured file format (Parquet, CSV, or JSON/JSONL) in a predictable folder structure that can be easily parsed by downstream systems.

  ```
  sftpwriter_home_folder/
  ├─ some_provided_folder/
  │  ├─ some_table_a/
  │  │  ├─ dt=2024-01-01/
  │  │  │  ├─ 0_20240101181004.csv
  │  │  │  ├─ 1_20240101184002.csv
  │  │  ├─ dt=2024-01-02/
  │  │  │  ├─ 0_20240102180123.csv
  │  │  ├─ dt=2024-01-03/
  │  │  │  ├─ 0_20240103182145.csv
  │  ├─ some_table_b/
  │  │  ├─ dt=2024-01-01/
  │  │  │  ├─ 0_20240101186004.csv
  │  │  ├─ dt=2024-01-02/
  │  │  │  ├─ 0_20240102185123.csv
  │  │  ├─ dt=2024-01-03/
  │  │  │  ├─ 0_20240103187145.csv
  ```
</Accordion>

<Accordion title="How is the SFTP connection secured?">
  Use SSH key-based authentication for a dedicated, least-privileged SFTP user. Restrict access to only the required directories (e.g., chroot), and allowlist Webflow's static egress IP at your network perimeter.
</Accordion>

<Accordion title="What file formats are supported?">
  Parquet (default/recommended), CSV, and JSON/JSONL.
</Accordion>

<Accordion title="How do I know when a transfer completed?">
  Each transfer writes a manifest JSON file per model under `_manifests/` at the root. Files follow the pattern: `_manifests/<model_name>/dt=<transfer_date>/manifest_{transfer_id}.json`. Use these manifests to trigger downstream processing.
</Accordion>

<Accordion title="Why do I sometimes see duplicates?">
  File-based destinations are append-oriented. The change-detection process uses a lookback window to prevent missed records, which can create duplicates across adjacent transfers. Downstream pipelines can deduplicate by primary key prioritizing rows in the most recent transfer window.
</Accordion>

<Accordion title="Can I provide my own public key? Where is the private key stored?">
  We do not support providing your own public key for security reasons. The private key is securely generated and stored in our system and is never shared externally.
</Accordion>
