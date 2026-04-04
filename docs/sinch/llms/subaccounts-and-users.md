# Source: https://docs.sinch.com/permission/subaccounts-and-users.md

# Subaccounts & Users

## What is a Subaccount?

Within Wavy, we have an architecture where our customer can use the same number to serve multiple purposes.

Within an Account, you can have multiple Subaccounts with customized “departments” and settings, where you can trigger multiple different things, such as service, CRM, Request status, among others

![Sinch Structure: Account and Subaccount](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGar7zO0jt7HSPWe7y%2F-MlGb9wIBDCgL4DPdczn%2F0.png?generation=1633456795944564\&alt=media)

Each subaccount can have its own users and webhook; this enables the optimization of a customer number.

{% hint style="warning" %}
**Only users with an Administrator profile can create subaccounts**
{% endhint %}

## Subaccounts Menu

{% hint style="info" %}
**Subaccounts Menu**

Within our platform, access the “Subaccounts & Users” menu. In this session you can:

* See all existing subaccounts in your main account
* See users belonging to subaccounts
* Create a new subaccount or user: Creating Subaccounts and Users depends on your user profile. Only the **Administrator** profile can create and manage subaccounts and users

**See** [**user profiles**](https://docs.wavy.global/permissoes/subcontas-e-usuarios#perfis-de-usuario) **to understand the permissions of this and other sessions**
{% endhint %}

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2Ftm5exBo3GvkUUmylzCtR%2Fimage.png?alt=media\&token=a0ed7465-da85-48a1-9173-81933bf406c5)

### Subaccount Settings

{% hint style="info" %}
**Within a Subaccount**

When you select a subaccount, having an Administrator profile, you can:

* Edit the Subaccount’s name and reference;
* See the list of users linked to this subaccount;
* Edit users of the subaccount;
* Set LAs;
  {% endhint %}

### ​Creating a Subaccount

Creating a new subaccount for your users is simple: after accessing the settings menu > Subaccounts & users, just click on **Create Subaccount:**

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FBoXtMrch6v0n8NYO1OCv%2Fimage.png?alt=media\&token=b0b256e6-1520-4630-b6e3-a383f98063d9)

The platform requests that you add some information:

* Name;
* Reference name (It is the name used in our databank)

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FPE5iNRQJtMjYDxeanL3F%2Fimage.png?alt=media\&token=8e9c0469-c370-414e-9d61-2936f84d3533)

### Adding Users

{% hint style="warning" %}
**Only users with an Administrator profile can create new users**
{% endhint %}

Access the settings menu > Subaccounts & users:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FZYjhTGPOZr6xdz6qZCMm%2Fimage.png?alt=media\&token=189feed3-a394-4657-8901-fb1b6f9aeba5)

Switch the subaccounts menu to **Users:**

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FaVjqprX2F5iyaHiVoBdM%2Fimage.png?alt=media\&token=e9bfdde7-051c-4844-aa68-e81a1828fb82)

On this screen, you can see all users already registered on the platform. If you need to make any changes, such as email address, subaccount to which a user reports, name, or surname, just click the pencil that is under the actions tab:

![pencil](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FgZ56Z30xZB7p4B1cHfqo%2Fimage.png?alt=media\&token=b3e75884-daef-4543-95b7-cdb0d1bb221d)

To create new users on the platform, use the button: **Create user.**

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FQxeZOLWGZwNsxolSnwJT%2Fimage.png?alt=media\&token=f7119eb0-f16b-4764-89df-482525d17e0a)

{% hint style="info" %}
**Adding a User**

By clicking on **add user,** you will enter the registration screen for your new user; fill it out with:

* Name (required);
* Surname (required);
* Username
* Email (Must be a valid email, and you can only use corporate email addresses, you cannot use @gmail.com, for instance);
* Country code;
* Phone number;
* Set the subaccount to which it belongs (required);
* ​[User profile](https://docs.wavy.global/permissoes/subcontas-e-usuarios#perfis-de-usuario): IMPORTANT – each profile grants different permissions
  {% endhint %}

### User Profiles

{% hint style="info" %}

### **Resale Administrator**

#### **Resale administrator:** Has access to all resale customer features (reports, deliveries, and visibility of subaccount and user settings)

{% endhint %}

{% hint style="info" %}

### **Data Analyst**

**Data analyst:** Can extract reports from the entire account, but cannot have access to any other features or trigger any messages.
{% endhint %}

{% hint style="info" %}

### **Manager**

**Manager:** This profile has access to all data that is in the subaccounts of its account, i.e., it is a more macro profile that has information on everything, but does not yet have permission to edit and create new subaccounts and users.
{% endhint %}

{% hint style="info" %}

### **Administrator**

**Administrator**: The administrator profile, in addition to having all data available on everything within its account, such as reports, templates, groups, and contacts, among others, it can also create and edit new subaccounts and users.
{% endhint %}

{% hint style="info" %}

### **User**

**User:** Can send messages and access the report of messages it has sent. Can view some other information that is shared within the subaccount to which it belongs, such as templates, groups, and contacts.
{% endhint %}

{% hint style="info" %}

### **Analyst**

**Analyst**: Has access to everything that has been triggered from its subaccount, such as messages, reports, templates, groups, and contacts.
{% endhint %}
