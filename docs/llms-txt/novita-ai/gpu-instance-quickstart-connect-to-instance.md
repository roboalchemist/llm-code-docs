# Source: https://novita.ai/docs/guides/gpu-instance-quickstart-connect-to-instance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect to Instance

## Connect via SSH with an SSH Key (Recommended)

### Linux/MacOS

1. On Ubuntu or Mac, use the following command to generate an RSA SSH public/private key pair:

```bash  theme={"system"}
ssh-keygen -t rsa
```

2. Force the agent to load the new private key and verify that it's loaded:

```bash  theme={"system"}
ssh-add; ssh-add -l
```

3. Retrieve the content of your SSH public key:

```bash  theme={"system"}
cat ~/.ssh/id_rsa.pub
```

1. Paste the content into the "SSH Public Keys" section in the <a href="https://novita.ai/gpu-instance/console/settings">Console - Settings</a>.

Here is an example of an SSH public key:

```txt  theme={"system"}
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDopiaR1Q6Na6dW1QTK7hMuHVi+gXqutY5pUvrWCgeyjcBtBLHejxDQjdNt+qWQRORK/fZzrmyA8/ghani0rZlGPN3bYw1RXFHitt+bD1jVgtJzOmjMQdpMVALnZASQMoQQcCqVJ8PG5Xc08TciACS7S/Ltz3VdZfIq1tih969GCzCe3sctSFBuTwqUDnyrQ6iqSBhPSfQS7nCC/CwzMi3rDg0JzW2NHzIBsbvy0gdXy1ZtC4kkCr7/lUWAgZLk52v3s2CTXCg6QXnhWx+Q/dHOJVAEEucY4o8bo4rF4Bj+ifgEHFtUEfoK9+yj3OLbWfpIxyzhHK+nNXz3UaOMSC8D ultra@novita.ai
```

### Windows

Generating SSH keys on Windows requires additional command-line tools like Cmder, with operations similar to those on Linux.

Since most machine learning and AI programming is performed on Linux, we strongly recommend installing a Linux subsystem on your Windows machine, such as WSL.

### Common Issues

If you encounter a "Permission denied (publickey)" error, it might be due to:

* Attempting to run SSH/SCP from within an instance;
* Incorrect key setup or using the wrong/unmatched key;
* The SSH key format used is incorrect or unsupported;
* The private key wasn't correctly loaded with `ssh-add`; you may need to use the `-i` parameter;
* New or updated keys not taking effect for already created resources;
* Incorrect SSH key permission settings.

Use the `ssh -vv` command for detailed information.

## Connect via SSH with a Password

Go to <a href="https://novita.ai/gpu-instance/console/instances">Console - Instances</a>, select the instance you want to connect to, click "Connect", and copy the "Basic SSH Terminal" command to your terminal. Log in using the password provided in the pop-up window.


Built with [Mintlify](https://mintlify.com).