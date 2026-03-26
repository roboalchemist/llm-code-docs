# Source: https://docs.socket.dev/docs/socket-firewall-enterprise-generating-keys.md

# Generating Keys for Proxy Service

Socket Firewall running in proxy service mode requires a Certificate Authority (CA) to sign certificates for intercepted HTTPS connections. This guide explains how to generate the required CA certificate and private key using OpenSSL.

## Prerequisites

You'll need OpenSSL installed on your system. Most Linux distributions and macOS include it by default. Windows users can install it via [Git for Windows](https://gitforwindows.org/) or download it from [slproweb.com](https://slproweb.com/products/Win32OpenSSL.html).

Verify OpenSSL is installed:

```bash
openssl version
```

## Generating the CA Key Pair

Socket Firewall needs two files in PEM format:

* **CA Certificate** (`ca.crt`) - The public certificate that clients will trust
* **CA Private Key** (`ca.key`) - The private key used to sign certificates

### Step 1: Generate the Private Key

Create a 2048-bit RSA private key:

```bash
openssl genrsa -out ca.key 4096
```

This creates `ca.key` in your current directory. Keep this file secure - anyone with access to it can impersonate your proxy.

### Step 2: Generate the CA Certificate

Create a self-signed certificate valid for 1 year:

```bash
openssl req -new -x509 -key ca.key -out ca.crt -days 365 \
  -subj "/CN=Socket Security CA/O=Socket Security" \
  -extensions v3_ca \
  -config <(cat <<EOF
[req]
distinguished_name = req_distinguished_name
x509_extensions = v3_ca

[req_distinguished_name]

[v3_ca]
basicConstraints = critical,CA:TRUE
keyUsage = critical,keyCertSign
subjectKeyIdentifier = hash
EOF
)
```

This creates `ca.crt` in your current directory. You should modify the certificate's subject such that it lists your company name rather than `Socket Security`. You can also modify the validity period from 365 days to another value of your choosing.

**What this command does:**

* `-new -x509`: Creates a new self-signed certificate
* `-key ca.key`: Uses the private key you just generated
* `-out ca.crt`: Saves the certificate to this file
* `-days 365`: Certificate is valid for 1 year
* `-subj`: Sets the certificate subject (Common Name and Organization)
* `-extensions v3_ca`: Applies CA-specific extensions
* `basicConstraints = critical,CA:TRUE`: Marks this as a CA certificate
* `keyUsage = critical,keyCertSign`: Allows the certificate to sign other certificates
* `subjectKeyIdentifier = hash`: Adds a unique identifier for the certificate

### Step 3: Verify the Certificate

Check that your certificate was created correctly:

```bash
openssl x509 -in ca.crt -text -noout
```

You should see output similar to:

```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: ...
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN=Socket Security CA, O=Socket Security
        Validity
            Not Before: ...
            Not After : ...
        Subject: ...
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (4096 bit)
        X509v3 extensions:
            X509v3 Basic Constraints: critical
                CA:TRUE
            X509v3 Key Usage: critical
                Certificate Sign
            X509v3 Subject Key Identifier:
                ...
```

## Using the Keys with Socket Firewall

Once you've generated `ca.crt` and `ca.key`, you can use them with Socket Firewall in service mode:

```bash
export SFW_CA_CERT_PATH=/path/to/ca.crt
export SFW_CA_KEY_PATH=/path/to/ca.key
sfw --service
```

See [Service Setup](socket-firewall-enterprise-proxy-service-setup) for complete configuration instructions.

## Installing the CA Certificate

After generating the CA certificate, you need to install it on any system that will connect to Socket Firewall. This allows clients to trust the certificates signed by your CA.

See [Client Setup](socket-firewall-enterprise-proxy-client-setup) for detailed installation instructions for different operating systems.

## Security Considerations

* **Keep `ca.key` secure**: Store it with restricted permissions (`chmod 600 ca.key` on Unix systems)
* **Don't commit to version control**: Add `*.key` to your `.gitignore`
* **Rotate regularly**: Generate new keys periodically (e.g., annually)
* **Backup safely**: Store backups in a secure location with encryption
* **Limit distribution**: Only install the CA certificate on systems that need to use the proxy