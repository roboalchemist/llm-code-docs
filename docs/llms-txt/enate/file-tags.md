# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/file-tags.md

# File Tags

Tagging files is an important feature for processes which involve automation technology. Example: if a downstream automated Action needs to know that the file you’ve attached to your Case is the ‘Invoice Confirmation’ file, you can tag the relevant files as such and, no matter what the file name, the automation technology would know to select that file based on its tag.

File tag configuration can be accessed from the menu in [System Settings](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings).&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpv3TCDYg2A_ocQW_M%2F-MWpvA1We0bkJk0yeF1z%2Fimage.png?alt=media\&token=d55920f9-b6da-49c9-ac87-234cf02be273)

Here you can view a list of your existing File Tags and you can create, edit and delete File Tags.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpv3TCDYg2A_ocQW_M%2F-MWpvCc44lL7yIIsPhGI%2Fimage.png?alt=media\&token=e8f2fec7-0ed7-4c89-915e-161bdca6babd)

You can edit an existing File Tag by clicking on it and editing the information in the resulting popup.

You can create a new File Tag by clicking on the '+' icon and defining its Name and Description in the resulting popup.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpv3TCDYg2A_ocQW_M%2F-MWpvGRgIC7ar15T3xJx%2Fimage.png?alt=media\&token=75bdb299-7ac8-4805-9949-3f8585b50b8b)

If a File Tag is marked as ‘Hidden’ it will not be accessible by users in Work Manager (but is still available for use in background activities e.g. when external RPA resources set / make decisions based on file tag values.

{% hint style="warning" %}
Please note:&#x20;

* File Tag names should be unique.
* Deleting a File Tag will instantly remove it from all running Work Items.
  {% endhint %}

Once you've added tags to your system, they will display in the Files Card on work items in Work Manager, and they'll be available to configure for auto-adding tagged documents into emails with matching tags.
