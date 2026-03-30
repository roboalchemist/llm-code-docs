# Source: https://docs.verda.com/cpu-and-gpu-instances/set-up-a-gpu-instance.md

# Set up a CPU or GPU instance

Create an account and get a CPU or GPU instance up and running within a few minutes!

## Deploy New Instance

Click the **Deploy Instance** button on the top right of the **Instances** page.

### Choose instance type and contract

On-demand instances are available for **Pay As You Go** pricing (every 10 minutes deducted from your account balance) or long-term rentals. *Long-term rentals are paid fully up-front.*

Spot instances are only available for reduced **Pay As You Go** pricing because they can be evicted by Verda at any point without warning.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-64193ad30fc5751269489b8bf4f12859fd4747b8%2Fcontract%20type.png?alt=media" alt=""><figcaption></figcaption></figure>

***

### Choose GPU or CPU model and size

First choose the model you would like. You can see the available sizes on the bottom of each model card (grey are unavailable). After clicking the desired model, the size section will appear with specifications. Select your desired size or request to be notified when it is available by clicking the **Notify** button.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-dd66770675502c229c7a1b45dd3b338e2d4b0589%2Fmodel%20and%20size.png?alt=media" alt=""><figcaption></figcaption></figure>

***

### Choose location

In most cases, the above choices will automatically select the location for your instance.\
Please note that all storage attached/shared to your compute must be in the same location.

[Learn more about our data center locations](https://docs.verda.com/welcome-to-verda/locations-and-sustainability)

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-3a4dedc7067e491c1e66196b95d7205e0a8b88f1%2Flocation.png?alt=media" alt=""><figcaption></figcaption></figure>

***

### Configure the operating system

You can choose between Ubuntu and JupyterLab with various configurations. Click the menu to select your preferred image configuration.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-28fcba508c835a0df4c5049d705e85941a52b293%2FOS.png?alt=media" alt=""><figcaption></figcaption></figure>

***

### Add storage

Create new storage by clicking the **Add volume** or **Add shared filesystem** buttons, or select existing storage by clicking **Add existing storage**.

Your block volumes must be detached in order to be attached to a new instance. Storage must be in the same location as the instance to be attached/shared.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-d874a28e3f0e4f2d4ad0011d3c821c3e73d25d09%2Fstorage.png?alt=media" alt=""><figcaption></figcaption></figure>

***

### Choose or create SSH key

Add a new SSH key from the **Deploy instance** page or **Keys** page.\
View [Creating an SSH key](https://docs.verda.com/cpu-and-gpu-instances/creating-an-ssh-key).

***

### Load a startup script (optional)

A startup script is a bash script that runs automatically when you deploy your GPU instance for the first time. It's handy for automating tasks without having to SSH into the instance and run the script manually.

***

### Choose hostname and description

The **hostname** is a human-friendly name to help you recognize an instance. The **description** shows various information about what type of instance it is, including OS, GPU model, and location. These are automatically generated, but you can edit them to be anything you want.

{% hint style="info" %}
The hostname cannot be changed after deployment
{% endhint %}

***

### Review and Deploy

Review your order summary and click **Deploy now** or continue through the payment flow to deploy your instance. If you are ordering a long-term instance, you will pay for the full contract up front [view pricing and billing](https://docs.verda.com/welcome-to-verda/pricing-and-billing). For large-scale long-term contracts with monthly invoicing, please contact us via chat or <support@verda.com>.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-0442c595459fbd1cbf260df0bf9b48726c001741%2Forder%20summary.png?alt=media" alt=""><figcaption></figcaption></figure>
