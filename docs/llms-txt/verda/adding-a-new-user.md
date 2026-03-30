<!-- Source: https://docs.verda.com/cpu-and-gpu-instances/adding-a-new-user.md -->

# Adding a New User

It is not recommended only to have a `root` user on your server, thus we will set up a new user account.

The process is fairly straightforward:

```bash
adduser username
```

Provide a secure password, and your new user account is created.

We will want occasional higher privileges:

```bash
usermod -aG sudo username
```

And you are done! Read the [Securing Your Instance guide](https://docs.verda.com/cpu-and-gpu-instances/securing-your-instance) for increased security.

## SSH login with a new username

Next, we will allow the newly created. Go to the new User's folder and create `.ssh` folder and `authorized_keys` file, and change its file permissions:

```bash
cd /home/<username>
mkdir .ssh
chmod 700 .ssh
touch .ssh/authorized_keys
chmod 600 .ssh/authorized_keys
chown -R <username>:<username> .ssh
```

To authenticate the new user, you will need to copy the [public key](https://docs.verda.com/cpu-and-gpu-instances/creating-an-ssh-key) corresponding to the user:

```bash
echo "<PUBLIC_KEY_LINE" >> .ssh/authorized_keys
```

You can now login from your workstation:

```bash
ssh <username>@<server_ip>
```

Alternatively, you can copy the entire `authorized_keys` file from the `root` user:

```bash
cp /root/.ssh/authorized_keys /home/<username>/.ssh/
```

Make sure to give an ownership of `.ssh` folder to `<username>`:

```bash
chown -R <username>:<username> .ssh
```
