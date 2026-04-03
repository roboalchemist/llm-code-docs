# Connecting to an instance -

Source: https://docs.lambda.ai/public-cloud/on-demand/connecting-instance/

---

[on-demand cloud ](../../../tags/#tag:on-demand-cloud)
# Connecting to an instance [# ](#connecting-to-an-instance)

You can connect to your On-Demand Cloud (ODC) instances directly through SSH or by using the preinstalled JupyterLab server. 

## Setting up SSH access [# ](#setting-up-ssh-access)

Before you launch an instance, you must add an SSH key to your Lambda Cloud account. When you go through the process of launching an instance, you'll be prompted to supply this SSH key so you can securely connect to the instance after launching. You can import an existing key if you have one, or you can generate a new one in the Lambda Cloud console. 

### Adding an existing SSH key [# ](#adding-an-existing-ssh-key)

If you have an existing SSH key, you can add it to your Lambda Cloud account and use it to connect to your instances. Lambda Cloud accepts SSH keys in the following formats: 

- OpenSSH, the format `ssh-keygen`uses by default when generating keys. 
- RFC4716, the format PuTTYgen uses when you save a public key. 
- PKCS8 
- PEM View examples of each key type 
OpenSSH keys look like: 

```
`[](#__codelineno-0-1)ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIK5HIO+OQSyFjz0clkvg+48YAihYMo5J7AGKiq+9Alg8 foo@bar
`
```
