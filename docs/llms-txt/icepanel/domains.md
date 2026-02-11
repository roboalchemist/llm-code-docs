# Source: https://docs.icepanel.io/core-features/domains.md

# Domains

{% hint style="info" %}
Domains are only available on Growth and Isolation plans.
{% endhint %}

## What is a domain?

A domain is an optional way to split up your model and related diagrams into logical groups, keeping the benefits of a single shared model. Domains are optional parent objects for systems (and the system's child objects), actors and areas.

You can create as many domains within a landscape, each with separate models that can be referenced across diagrams in different domains.

## When to use domains

The power of a landscape comes with the shared model, diagrams that can be created from the model and quickly updated across the whole landscape. Because of this, we recommend staying in 1 landscape as much as possible.

There are, however, a few common reasons this becomes hard to manage:

1. Large and/or complex architecture
2. Many diagrams at all levels

The temptation is to create a new landscape to reduce the clutter of many objects and diagrams, however, this separates the model and means you have maintenance overhead when changes are related to separate landscapes.&#x20;

We recommend using domains to split out the logical groups instead. This allows you to reuse objects in other domains, leveraging the power of modelling with the benefits of cleaner separation.

## How to create a domain

To create a new domain:

1. Go to the home screen
2. Click on the domain dropdown on the top left of the navigation
3. Click the `New domain` button located near the top
4. Click on the `...` menu beside the domain
5. Click on the `Rename domain` button
6. Name your new domain

You'll now be able to create new diagrams in the domain whilst using the same shared model.&#x20;

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2Fm4F8HkcKKXE3vDUFwnAs%2FCreate-domain-2.gif?alt=media&#x26;token=76de0802-32bb-4aad-bd4e-345953ce78c1" alt=""><figcaption><p>Creating a new domain</p></figcaption></figure>

## Adding objects from other domains in a diagram

Model objects in other domains within the same landscape can be added to a diagram. There are 2 ways to do this.

To do this via search in a diagram:

1. Double-click to add an object
2. Search for the object in another domain

To do this via the filtered tab:

1. Click on the `Existing objects` button in a diagram
2. Click on the `Other domains` tab
3. Select the object you want to add

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FBMe6tBi52VcLA89ETRwx%2FOther-Domains.gif?alt=media&#x26;token=d97c9ebc-5792-479c-832f-50a29fa1f60d" alt=""><figcaption><p>Adding an object in another domain</p></figcaption></figure>

The domain name will be displayed on the object when used in another domain, making it clear that it's from another area of the shared model.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FFFFMEO0xszs2QukS06jv%2Fimage.png?alt=media&#x26;token=9c446118-9468-45d1-ab28-39d7f1c5bbb8" alt=""><figcaption><p>Objects from other domains will appear with a label on top</p></figcaption></figure>

## How to move objects to another domain

Model objects including Systems (and their child objects), Actors, and Groups can be moved across domains.

To move an object to another domain:

* Select the object you wish to move
* Navigate to the details panel located on the right
* Click on the `Domain` field
* Select the new domain you wish to move the object to in the dropdown. You'll see a breakdown of objects, connections, and diagrams that the change will impact
* Click on the `Change parent` button

This will automatically update any relevant diagrams and flows to reflect your changes.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F9xRJOhTpEMpVsc6ycNT7%2FChange-Domain.gif?alt=media&#x26;token=1aa28a83-beb7-41db-8f24-c552ba6b33cb" alt=""><figcaption><p>Changing the domain of an object</p></figcaption></figure>

## Adding a description to a domain

You can add a description to any domain. Hit the *Domain* in the top menu and add a description.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FFz86Ih8mkT4OVRIg4JOk%2FClipboard-20251117-213525-351.gif?alt=media&#x26;token=350324e9-4be7-49f0-bf42-46284cff95ca" alt=""><figcaption></figcaption></figure>

This description will be accessible both in the drop-down and via API.

## How to delete a domain

{% hint style="danger" %}
Doing this will delete everything from the domain, including model objects, diagrams and flows. This cannot be undone without a version revert.
{% endhint %}

To delete a domain:

1. Go to the home screen.
2. Click on the domain dropdown.
3. Click on the `...` menu beside the domain you want to delete.
4. Click on the `Delete domain` button
5. You'll be shown a menu that explains what will be removed
6. Click `Delete domain` to confirm.

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FceMnjo448HzWKIthe9UF%2FScreenshot%202024-02-01%20at%204.41.10%E2%80%AFPM.png?alt=media&#x26;token=cfd7cb87-ed5f-4e02-832c-2cee2461c156" alt="" width="563"><figcaption><p>Deleting a domain confirmation screen</p></figcaption></figure>

### Switching between domains

You can switch between domains by selecting the drop-down menu on the left side of the screen.&#x20;

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FrTUcbNRIaPPN2OsiqaVU%2Fimage.png?alt=media&#x26;token=b540ba40-5f29-4552-80dc-3929af3dfe5f" alt=""><figcaption><p>Switch between domains</p></figcaption></figure>
