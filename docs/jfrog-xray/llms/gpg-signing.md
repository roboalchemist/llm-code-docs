# Source: https://docs.jfrog.com/artifactory/docs/gpg-signing.md

# GPG Signing

<Callout icon="📘" theme="info">
  **Subscription Information**

  This feature is supported with the **Enterprise+** license.
</Callout>

JFrog Distribution secures [Release Bundle](/docs/distribute-release-bundles-v1) delivery using a GPG key pair (private and public). The created Release Bundle that's distributed to an Edge Node is signed with a private GPG key. The Edge Node verifies the Release Bundle signature with a public GPG key.

The process for applying GPG keys is:

1. Generate a GPG key.
2. Upload the GPG key using the REST API to the following locations:

   * Distribution service (private and public)
   * Source Artifactory and Edge nodes (public key only)

## Generate GPG Keys

<Callout icon="📘" theme="info">
  **Signing Release Bundles**

  GPG keys need to be at least 2K.
</Callout>

<Callout icon="📘" theme="info">
  **Note**

  If you are using a Vault, see <Anchor label="Vault" target="_blank" href="https://jfrog-enterprise-group.readme.io/administration/docs/vault">Vault</Anchor> for instructions.
</Callout>

The way to generate private and public GPG keys is platform-dependent.

The following example displays how to generate the keys on Linux requiring GPG version 2.1 and higher.

**Generating GPG keys**

```
# Generate the keys
gpg --full-generate-key 

# Select RSA
Please select what kind of key you want: 
(1) RSA and RSA (default) 
(2) DSA and Elgamal 
(3) DSA (sign only) 
(4) RSA (sign only)  


# Select the size of the key you may use the default value.
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (2048)  


# Select the validation for the key (0 will not expire)
0 = key does not expire  = key expires in n days
w = key expires in n weeks
m = key expires in n months
y = key expires in n years
Key is valid for? (0) <- Accept the default value by clicking Enter 

Key does not expire at all
Is this correct? (y/N) y 

# Enter a user ID and email
Real name:
Email address:
Comment: 

# Export the private key with the specified id to a file
gpg --output {private key file name and path} --armor --export-secret-keys {key-id}  

# Export the public key with the specified id to a file
gpg --output {public key file name and path} --armor --export {key-id}
```

<Callout icon="📘" theme="info">
  **Signing Release Bundles**

  If the GPG key pair is created using a passphrase, please be sure to copy the passphrase for keepsake as it will be required by JFrog Distribution for signing the Release Bundle.
</Callout>

## Upload and Deploy GPG Keys

To create trust between JFrog Distribution, the source Artifactory, and the Edge nodes, you need to run the [Upload and Propagate GPG Signing Keys for Distribution](/reference/uploadandpropagategpgsigningkeysfordistribution) REST API to upload and deploy the GPG keys. As part of the automated deployment process, this API will:

1. Deploy the generated GPG Key pair (public and private) for JFrog Distribution. The pair of keys are stored internally in JFrog Distribution.
2. Deploy the generated GPG public key on the source Artifactory and Edge node. The public key will be stored under **Administration > Security > Keys Management > Public Keys** on the source Artifactory and Edge node.
3. If "`propagate_to_edge_nodes`" is set to `true`, the public key will be automatically propagated to the Edge node just once.

## Multiple GPG Signing Keys

Starting from version 2.8.1, Distribution supports managing multiple pairs of GPG signing keys using a set of REST APIs. This enables you to assign a signing key pair per Release Bundle, which provides the ability to choose which keys to use to sign a particular Release Bundle instead of using the same key pair to sign them all.

#### Post-Upgrade Guidelines

When upgrading from a previous version containing GPG keys to Distribution version 2.8.1, with the new multiple GPG signing keys feature there are a few considerations:

* The existing GPG signing keys will be preserved and named `default-gpg-key`.
* Release Bundles should be assigned with key pairs using the:

  * [Upload and Propagate GPG Signing Keys for Distribution](/reference/uploadandpropagategpgsigningkeysfordistribution) REST API: To upload the multiple keys using the additional parameters `alias` and `default`.
  * [Sign Release Bundle Version](/reference/signreleasebundlev1version): To sign the Release Bundle using the additional parameter `signing_key_alias`.
* For each of the key pairs, you need to provide an Alias (mandatory). If an alias is not provided, the name generated consists of GPG and the timestamp.

## Manually Deploy GPG Keys to Edge Nodes

Run the [Propagate GPG Signing Keys to an Edge Node](/reference/propagatepublicsigningkey) REST API  to manually deploy GPG keys to additional Artifactory Edge nodes that were added after the initial Distribution GPG deployment process.