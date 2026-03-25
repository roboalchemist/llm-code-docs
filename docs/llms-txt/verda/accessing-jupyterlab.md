<!-- Source: https://docs.verda.com/cpu-and-gpu-instances/accessing-jupyterlab.md -->

# Accessing JupyterLab

JupyterLab runs on your instance and listens on port `8888` by default. Keep it private. Use SSH port-forwarding.

## Start an instance

Pick **JupyterLab** as the Operating System.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-33f02f6cb5f77c825930588b1f21f33b2805acd4%2FJupyterLab2.png?alt=media" alt=""><figcaption></figcaption></figure>

### Secure the instance

Do this before you run any public-facing services:

* [Securing Your Instance](https://docs.verda.com/cpu-and-gpu-instances/securing-your-instance)

{% hint style="warning" %}
Do not open port `8888` to the internet. Prefer SSH tunneling.
{% endhint %}

### Connect from your browser (recommended)

#### 1) Create an SSH tunnel

Run this on your laptop/desktop:

```bash
ssh -L 8888:localhost:8888 <user>@IP_OF_YOUR_INSTANCE
```

Keep this SSH session open while you use JupyterLab.

If you use `root`, the command looks like:

```bash
ssh -L 8888:localhost:8888 root@IP_OF_YOUR_INSTANCE
```

If JupyterLab uses a different port, forward that port instead.

#### 2) Open JupyterLab

Open this URL in your browser:

* <http://127.0.0.1:8888/>

#### 3) Get the token

## Option A: From the Verda console (fastest)

Open the **Open JupyterLab** link on the instance card. Copy the `token=...` value from the URL.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-a0b9deafc8e36b9a4bee4daf408feacce6fc426e%2Fjupyterlink.png?alt=media" alt=""><figcaption></figcaption></figure>

## Option B: From the instance (Docker)

If you can SSH into the instance, print the running server list. It includes the full token URL.

```bash
# SSH into the instance
ssh root@IP_OF_YOUR_INSTANCE

# Find the Jupyter container name or ID
# (it is often named "jupyter")
docker ps

# Print the server list (includes the token URL)
docker exec jupyter jupyter server list

# Or use the container ID
# docker exec <container-id> jupyter server list
```

You’re looking for a line like:

* `http://localhost:8888/?token=...`

If Jupyter is running on the host (not in Docker), run this instead:

```bash
jupyter server list
```

### (Optional) Connect from VS Code

VS Code connects to the same forwarded URL. Use the Jupyter extension. Then point the kernel URL at:

* `http://127.0.0.1:8888`

Continue here for the VS Code flow:

* [Connecting to Jupyter notebook with VS Code](https://docs.verda.com/cpu-and-gpu-instances/connecting-to-jupyter-notebook-with-vs-code)
