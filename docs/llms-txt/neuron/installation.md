# Source: https://docs.neuron.world/node-builder-software/installation.md

# Installation

## What You'll Learn

By the end of this guide, you'll have:

* ✅ Neuron NodeBuilder installed and running
* ✅ Your account set up and connected to the network
* ✅ A working development environment ready for tutorials

## Before You Start

Make sure you have:

* A computer running Windows, Mac, or Linux
* An internet connection
* About 30 minutes of time
* An email invitation to the Neuron Beta program

Welcome to the Neuron NodeBuilder Beta! Here you can find out how to install the software and follow our tutorials to learn how to buy and sell services with other users, machines, or AI agents.

{% embed url="<https://www.youtube.com/watch?v=hcfN0JjGVsc>" %}

## Step 1: Get Access to the Beta Program

**Option A: I have an email invitation**

1. Check your email for a Neuron Beta invitation
2. Click the registration link in your email
3. Continue to Step 2 below

**Option B: I don't have an invitation**

1. Contact <tech@neuron.world> to request beta access
2. Sign up to the waiting list: <https://www.neuron.world/builder>
3. Wait for your invitation email, then return to Option A

## Step 2: Create Your Account

1. **Click the registration link** from your email invitation
2. **Create a new account** with your email and a strong password
3. **Verify your email** by clicking the link sent to your inbox
4. **Accept the terms and conditions**

💚 **Important:** You must register a new account, even if you already have an account with Neuron, as this one is specific to the builder.

**Troubleshooting:** If the system does not let you accept the terms, logout, re-login, and try again.

After successful registration and login, you should see this screen:

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FxqyjWmsNa284xsIn3VnJ%2Fimage.png?alt=media&#x26;token=3b5d6dac-7366-4814-8f92-740b7855af20" alt=""><figcaption></figcaption></figure>

## Step 3: Copy Your Credentials

1. **Find your credentials** on the page above
2. **Copy your Hedera account number** - it looks like `0.0.123456`
3. **Copy your private key** - it's a long string of letters and numbers

🔒 **Keep these around!** You'll need them to connect to the network, and you can't recover them if lost.

Note this is a testnet, if you need to get these keys back log back into your account.&#x20;

## Step 4: Install the NodeBuilder Software

You have two options for installation:

### Option A: Easy Installer (Recommended for Beginners)

1. **Download the installer** from the links provided on your account page
2. **Run the installer** by double-clicking the downloaded file
3. **Wait for installation** to complete
4. **Your browser will automatically open** to `http://localhost:1880`

**For Mac users:** Look for the Neuron icon in your menubar (top of screen), not in your dock.

### Option B: Build from Source (Advanced Users)

**Prerequisites:** You need `nodejs` and `git` installed first.

1. **Follow the build instructions** provided on your account page
2. **Monitor the terminal/command prompt** for any error messages
3. **Keep the terminal window open** - it helps with troubleshooting
4. **Wait for the success message** that tells you to visit `http://localhost:1880`

![](https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FoNS4zlzHMeuBqZtq7lVy%2F1.png?alt=media\&token=48314a4f-3e30-4bbe-8202-6177e7e7016b)

## Step 5: Connect to Your NodeBuilder

1. **Open your web browser** (Chrome, Firefox, Safari, or Edge)
2. **Go to:** `http://localhost:1880` or `http://127.0.0.1:1880`
3. **Enter your credentials** when prompted:
   * Hedera account number (the `0.0.123456` you saved earlier)
   * Private key (the long string you saved earlier)

![](https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FnCwycg93j4hJgMxcui6i%2F2.png?alt=media\&token=c35acda3-12a4-47a2-ae1f-982776e4e205)

4. **Click Save Credentials and continue** - the system will connect to the Neuron network
5. **Wait for a coder's canvas to load** - you should see an empty canvas appear

![](https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2Fadk0VpsMextthanPt3zq%2F3.png?alt=media\&token=962842bc-bb49-4f01-9412-e160f44b6f88)

## Step 6: Verify Everything is Working

✅ **You should see:**

* An empty canvas (workspace) in the center
* Various nodes available on the left sidebar
* Your account balance in the upper right corner
* Neuron-specific nodes mixed with generic building blocks

## 🎉 Success! What's Next?

You're now ready to build your first program! Continue to: [your-first-program-hello-world](https://docs.neuron.world/node-builder-software/your-first-program-hello-world "mention")

## Common Problems & Solutions

**Problem:** Browser shows "This site can't be reached"

* **Solution:** Make sure NodeBuilder is running (see Step 6 above)

**Problem:** Can't find my credentials

* **Solution:** Go back to your account page where you registered

**Problem:** "Invalid credentials" error

* **Solution:** Double-check you copied the full account number and private key correctly

**Problem:** NodeBuilder won't start

* **Solution (Installer):**
  * Make sure NodeBuilder is not already running in the background. On Windows, open Task Manager and end any "NodeBuilder" or "node" processes. On Mac, use Activity Monitor to do the same.
* **Solution (Command Line):**
  * Ensure you have all prerequisites installed: `nodejs` and `git`.
  * Check for any running "NodeBuilder" or "node" processes and terminate them (Task Manager on Windows, Activity Monitor or `kill` command on Mac).
  * If you see error messages about missing dependencies, install them as indicated.
