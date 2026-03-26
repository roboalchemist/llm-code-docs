# Source: https://docs.infrahub.app/sync/guides/custom-certificates.md

# Support adapters with custom CA certificates

This guide will walk you through the steps to support adapters with custom CA certificates for infrahub-sync.

## Step 1: Create a subdirectory for your custom CA certificates[​](#step-1-create-a-subdirectory-for-your-custom-ca-certificates "Direct link to Step 1: Create a subdirectory for your custom CA certificates")

```
sudo mkdir /usr/local/share/ca-certificates/custom-ca
```

## Step 2: Copy your root CA custom certificate into the folder you just created[​](#step-2-copy-your-root-ca-custom-certificate-into-the-folder-you-just-created "Direct link to Step 2: Copy your root CA custom certificate into the folder you just created")

```
cp customRCA.crt /usr/local/share/ca-certificates/custom-ca/
```

## Step 3: Run the following command to load the certificates on your system trusted root certificate store[​](#step-3-run-the-following-command-to-load-the-certificates-on-your-system-trusted-root-certificate-store "Direct link to Step 3: Run the following command to load the certificates on your system trusted root certificate store")

```
sudo update-ca-certificates
```

## Step 4: Use the following command to set `REQUESTS_CA_BUNDLE` environment variable[​](#step-4-use-the-following-command-to-set-requests_ca_bundle-environment-variable "Direct link to step-4-use-the-following-command-to-set-requests_ca_bundle-environment-variable")

```
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
```
