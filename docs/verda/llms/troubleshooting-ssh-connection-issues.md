# Source: https://docs.verda.com/cpu-and-gpu-instances/troubleshooting-ssh-connection-issues.md

# Troubleshooting SSH Connection Issues

When you can't SSH into your Verda GPU or CPU instance (VM), the problem could be anywhere from your local machine to the network to the instance itself. Here's how to systematically identify and fix the issue.

### Step 1: Verify Basic Connectivity

Start by confirming the VM is reachable at the network level.

**Ping the VM** to see if it responds at all:

```bash
ping your-vm-ip-address
```

If ping fails, the VM might be down, have firewall rules blocking ICMP, or there's a network routing issue. If it succeeds, at least the VM is alive and reachable.

**Check if the SSH port is open** using telnet:

```bash
telnet your-vm-ip-address 22
```

If this times out or is refused, the SSH service might not be running or firewall rules are blocking port 22.

### Step 2: Check Your SSH Command and Credentials

Make sure you're using the correct connection details:

```bash
ssh -v username@your-vm-ip-address -i /path/to/private-key
```

The `-v` flag enables verbose mode, which shows you exactly where the connection fails. Common issues include wrong username (try `ubuntu`, `admin`, or `root` depending on your OS), incorrect IP address, or wrong SSH key.

**Verify your SSH key has correct permissions:**

```bash
chmod 600 /path/to/private-key
```

If permissions are too open (like 644 or 777), SSH will refuse to use the key for security reasons.

### Step 3: Check VM Status Through the Cloud Console

Log into your web console at [console.verda.com](http://console.verda.com/) and verify from your project page:

* The VM is actually running (not offline or discontinued)
* System health checks are passing

### Step 4: Contact support

If you still can't get in, please contact our support through the Chat at the bottom of the corner or through email.
