## HTTP boot

The network install feature uses HTTP over Ethernet to boot the Raspberry Pi into embedded xref:getting-started.adoc#raspberry-pi-imager[Raspberry Pi Imager].

In addition to network install, you can explicitly boot your device with files downloaded via HTTP with xref:raspberry-pi.adoc#BOOT*ORDER[boot-mode] `7`. You can still use this even if xref:raspberry-pi.adoc#NET*INSTALL*ENABLED[network install on boot is disabled].

You could, for example, add this to your `BOOT*ORDER` as a fall-back boot method, or put it behind a GPIO conditional to initiate HTTP boot from your own server when a GPIO pin is pulled low.

For example, if you added the following to your EEPROM config and GPIO 8 (which has a default state of 1 or HIGH) were to be pulled low, the files `\http://downloads.raspberrypi.org:80/net*install/boot.img` and `\http://downloads.raspberrypi.org:80/net*install/boot.sig` would be downloaded. If network install on boot were enabled, it would use the same URL. If GPIO 8 were not pulled low the behaviour would be unchanged.

```ini
[gpio8=0]
BOOT*ORDER=0xf7
HTTP*HOST=downloads.raspberrypi.org
NET*INSTALL*ENABLED=0
```

`boot.img` and the `boot.sig` signature file is a ram disk containing a boot file system. For more details, see xref:config*txt.adoc#boot*ramdisk[boot*ramdisk].

HTTP in the `BOOT*ORDER` will be ignored if secure boot is enabled and xref:raspberry-pi.adoc#HTTP*HOST[HTTP*HOST] is not set.

### Requirements

To use HTTP boot, xref:raspberry-pi.adoc#bootloader*update*stable[update] to a bootloader released 10th March 2022 or later. HTTP boot requires a wired Ethernet connection.

To use custom CA certificates, xref:raspberry-pi.adoc#bootloader*update*stable[update] to a bootloader released 5th April 2024 or later. Only devices running the BCM2712 CPU support custom CA certificates.

### Keys

All HTTP downloads must be signed. The bootloader includes a public key for the files on the default host `fw-download-alias1.raspberrypi.com`. This key will be used to verify the network install image, *unless* you set xref:raspberry-pi.adoc#HTTP*HOST[HTTP*HOST] *and* include a public key in the EEPROM. This allows you to host the Raspberry Pi network install images on your own server.

WARNING: Using your own network install image will require you to sign the image and add your public key to the EEPROM. If you then apply a public EEPROM update, your key will be lost and will need to be re-added.

https://github.com/raspberrypi/usbboot/blob/master/Readme.md[`USBBOOT`] has all the tools needed to program public keys. 

Use the following command to add your public key to the EEPROM. `boot.conf` contains your modifications:

```console
$ rpi-eeprom-config -c boot.conf -p mypubkey.pem -o pieeprom.upd pieeprom.original.bin
```

Use the following command to generate a signature for your EEPROM:

```console
$ rpi-eeprom-digest -i pieeprom.upd -o pieeprom.sig
```

Then, use the following command to sign the network install image with your private key:

```console
$ rpi-eeprom-digest -i boot.img -o boot.sig -k myprivkey.pem
```

Finally, put `boot.img` and `boot.sig` on your web server to use your own signed network install image.

### Certificates

For security, Network Install uses HTTPS to download OS images from the Raspberry Pi website. This feature uses our own CA root included in the bootloader to verify the host.

You can add your own custom CA certificate to your device EEPROM to securely download images from your own website. Use the `--cacertder` option of the `rpi-eeprom-config` tool to add the DER-encoded certificate. You must place a hash of the certificate in the EEPROM config settings to ensure that the certificate is not modified.

Run the following command to generate a DER-encoded certificate:

```console
$ openssl x509 -in your*ca*root*cert.pem -out cert.der -outform DER
```

Then, run the following command to generate a SHA-256 hash of the certificate:

```console
$ sha256sum cert.der
```

You should see output similar to the following:

```
701bd97f67b0f5483a9734e6e5cf72f9a123407b346088638f597878563193fc  cert.der
```

Next, update `boot.conf` to include the hash of the certificate:

```console
$ sudo rpi-eeprom-config --edit
```

Configure the following settings in the `[gpio8=0]` section, replacing:

** `<your*website>` with xref:raspberry-pi.adoc#HTTP*HOST[your website], e.g. `yourserver.org`
** `<path*to*files>` with the xref:raspberry-pi.adoc#HTTP*PATH[path to your OS image] hosted on your website, e.g. `path/to/files`
- `<hash>` with the hash value you generated above, e.g. `701bd97f67b0f5483a9734e6e5cf72f9a123407b346088638f597878563193fc`

```ini
[all]
BOOT*UART=1
POWER*OFF*ON*HALT=0
BOOT*ORDER=0xf461

[gpio8=0]
BOOT*ORDER=0xf7
NET*INSTALL*ENABLED=0
HTTP*HOST=<your*website>
HTTP*PATH=<path*to*files>
HTTP*CACERT*HASH=<hash>
```

When you specify a `HTTP*CACERT*HASH`, Network Install downloads the image using HTTPS over port 443. Without a hash, Network install downloads the image using HTTP over port 80.

Finally, use the following commands to load everything into EEPROM:

```console
$ rpi-eeprom-config -c boot.conf -p mypubkey.pem -o pieeprom.bin --cacertder cert.der pieeprom.original.bin
$ rpi-eeprom-digest -k myprivkey.pem -i pieeprom.bin -o pieeprom.sig
```

During network boot, your Raspberry Pi should use HTTPS instead of HTTP. To see the full HTTPS URL resolved by Network Install for the download, check the boot output:

```
Loading boot.img ...
HTTP: GET request for https://yourserver.org:443/path/to/files/boot.sig
HTTP: GET request for https://yourserver.org:443/path/to/files/boot.img
```

### Secure boot

If secure boot is enabled, then the Raspberry Pi can only run code signed by the customer's private key. So if you want to use network install or HTTP boot mode with secure boot, you must sign `boot.img` and generate `boot.sig` with your own key and host these files somewhere for download. The public key in the EEPROM will be used to verify the image.

If secure boot is enabled and xref:raspberry-pi.adoc#HTTP*HOST[HTTP_HOST] is not set, then network install and HTTP boot will be disabled.

For more information about secure boot see https://github.com/raspberrypi/usbboot/blob/master/secure-boot-recovery/README.md[`USBBOOT`].