# Source: https://docs.sinch.com/permission/system-user-role.md

# System User Role

## What is this new feature?

Before we explain about the feature, we need to **understand the problem that we are solving**. When you have to create a chatbot integrated to MM2, you must create an account on MM2 to link this to a chatbot, on Chatlayer. If this person who has created this bot **leaves the company**, this chatbot usually is <mark style="color:red;">**desactivate**</mark> due to this event.

So, thinking in **avoid this bad experience** happen always that someone leaves the company (and to guarantee more security in our process), we have decided to **create the** <mark style="color:red;">**System User Role**</mark>. This new feature intend to prevent this issue from happening, become able to <mark style="color:red;">**create safe users to use on your chatbots.**</mark>

## Activating the System User Role

Go to Settings > My Account > Account Settings

<mark style="color:red;">**2.1**</mark> - You can see the new tab called System User.&#x20;

{% hint style="danger" %}
Only the customer **Admin** and the **Developer role** can be able to set up this new configuration.
{% endhint %}

<mark style="color:red;">**2.2**</mark> - Button to "**Create System User**".

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FcohEwmlI9r0mqrFcqeUm%2Fimage.png?alt=media&#x26;token=87e565e2-44ef-425e-b962-d00cbc0f3d5b" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">**2.3**</mark> - Once you click on the button to create a new system user, it will open a pop up where you can select the subaccount + username.

<mark style="color:red;">**2.4**</mark> - It is important to know that you can only create a system user for each subaccount.

{% hint style="info" %}
The **Username** can be whatever you want.
{% endhint %}

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FTVuZEz6rrWTTzZTk0hbo%2Fimage.png?alt=media&#x26;token=3c23813e-f82f-4ee4-961d-5c09e4118600" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">**2.5 -**</mark> After you define the subaccount and the username, you will click on <mark style="color:red;">**Generate Token**</mark>.&#x20;

It will appear this pop up, so pay attention to take note of this token because it will not be displayed again. In case you forget to take a note, you will have to generate a new token.

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FxCogAnABtlH3H0XHtRWm%2Fimage.png?alt=media&#x26;token=d35f5df7-d0fa-4871-9842-bae499896260" alt=""><figcaption></figcaption></figure>

In this screen, you can see all the system users you have created.

<mark style="color:red;">**2.6 -**</mark> You can see who user has created.

<mark style="color:red;">**2.7 -**</mark> All the informations that belongs to the system user.

<mark style="color:red;">**2.8 -**</mark> You will be able to see just the end of the token.

<mark style="color:red;">**2.9 -**</mark> The date and the time of this creation.

<mark style="color:red;">**2.9.1 -**</mark> If it is active or inactive.

<mark style="color:red;">**2.9.2 -**</mark> More Actions (Deactive or Generate a new Token)

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FQC8wc9JrnAL034oS2zIO%2Fimage.png?alt=media&#x26;token=2df34f0e-38c0-4744-a008-b2477720642a" alt=""><figcaption></figcaption></figure>

## Deactivating the System User Role

Go to Actions > Click on … > Deactivate.

<mark style="color:red;">**3.1**</mark> Once you click on Actions and choose to deactivate the System User, it will open a pop up to confirm your choice.&#x20;

<mark style="color:red;">**3.2**</mark> After doing this, you will see the Status column updated. In case you want to activate it again, just go to Actions.

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2F55rhC0MVRPr5sbaXaUMU%2Fimage.png?alt=media&#x26;token=7f798f7a-0d49-4f90-a77f-cb42143bd6bc" alt=""><figcaption></figcaption></figure>

## Generate a new token

Go to Actions > Click on … > Generate a new token.

<mark style="color:red;">**4.1 -**</mark> Once you click on Actions and choose to Generate a new token, it will open a pop up to ensure your understanding about the risk of doing this (just in case you have configured in an API).

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FoUG56raTaSVKZhWdi59y%2Fimage.png?alt=media&#x26;token=dae3e3c8-7934-4872-ab88-b274d58657c0" alt=""><figcaption></figcaption></figure>

## Webhook Configuration: prepare to Chatlayer integration

Go to Settings > Webhook.

5.1 This configuration is the same of usual.

The only exception is that if your chatbot is not so active into sending messages and not expecting to receive organic MO (mainly after so much time without any interaction), you will have to configure another Answer (MO) to accept **Subaccount Null**.

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FCAL7C454ai4orMqo6WmT%2Fimage.png?alt=media&#x26;token=760ae06d-90a4-4325-9d7b-ed9934a15860" alt=""><figcaption></figcaption></figure>

## Update Chatlayer with System User

Go to Chatlayer > Configure Wavy WhatsApp Channel

<mark style="color:red;">**6.1**</mark> This configuration is the same of usual.

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FXfU0W5LjksBHr6vUwti3%2Fimage.png?alt=media&#x26;token=320565f8-e443-4e88-9ee8-549fa917ea15" alt=""><figcaption></figcaption></figure>
