<!-- Source: https://docs.verda.com/cpu-and-gpu-instances/connecting-to-jupyter-notebook-with-vs-code.md -->

# Connecting to Jupyter notebook with VS Code

Use VS Code when you want editor features like linting and AI copilots. You’ll connect VS Code to the Jupyter server running on your instance.

## Before you start

Follow this first:

* [Accessing JupyterLab](https://docs.verda.com/cpu-and-gpu-instances/accessing-jupyterlab)

That flow covers:

* Securing your instance ([Securing Your Instance](https://docs.verda.com/cpu-and-gpu-instances/securing-your-instance))
* Creating the SSH tunnel to `127.0.0.1:8888`
* Getting the `token=...` value

{% hint style="info" %}
Keep the SSH tunnel terminal open while you use VS Code.
{% endhint %}

## Connect VS Code to the remote kernel

Make sure the VS Code **Jupyter** extension is installed. Then connect to the forwarded URL (`http://127.0.0.1:8888`).

{% stepper %}
{% step %}

### Select an existing Jupyter server

Open any local `*.ipynb`. Select **Existing Jupyter Server**.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2F2Of3Zow0PQMRFOlx5yvt%2Fimage.png?alt=media&#x26;token=f3239229-3994-424d-b854-906dd70e06f5" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Enter the local forwarded URL

Use:

* `http://127.0.0.1:8888`

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2FyBo8vOdxOavjeo5IrVbR%2Fimage.png?alt=media&#x26;token=c22e61b7-70c3-477a-948c-d5cd552de91b" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Authenticate with the token

When prompted for a password, paste the Jupyter `token` value.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fi9nPDI7sPFXtKMuYg0zw%2Fimage.png?alt=media&#x26;token=6706bcf3-0809-49af-8092-6fd226845040" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Name the server

Pick any display name.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2FVUwly2jCHwm30tiCIY3G%2Fimage.png?alt=media&#x26;token=1bd2a8a3-e114-4c8a-91ff-24ba9c090f4d" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Select a kernel

Choose a kernel. These are typically available on the image:

* Julia
* Python (Conda)
* R

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2FuJGvDmMWEGsMwzWoHMeu%2Fimage.png?alt=media&#x26;token=ff96652b-45c3-4248-a505-7e353269858d" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

You should now be able to run code on your remote machine through VS Code.
