# Source: https://docs.bugbug.io/workflow-tips/mobile-version-testing.md

# Mobile version testing

### What is a mobile version / RWD?

Your website may behave differently when opened on smaller screens, such as a smartphone or a tablet. This behavior is called Responsive Web Design (RWD) or simply a mobile version of your website - your website is designed in a way that adapts to different screen widths.

### When to test more than one screen width?

If your app is very similar on mobile and desktop, there's no need to create separate mobile tests - it will just double your work without much value added. We recommend that you focus on one screen resolution - the one that has the most users. You can still create 5 - 10 additional tests for different resolutions, but focus on the major differences between the mobile and desktop versions - just check if these specific core differences work correctly. &#x20;

If your app has many differences between mobile and desktop, for example very different navigation and user journeys, it makes sense to develop tests for mobile and desktop in parallel, as completely independent projects.

### How to create tests for different screen resolutions?

The easiest way to test the mobile version (responsive web design / RWD) is to have 2 different projects: one for desktop tests and one for mobile tests. Set a different window width per project in its [project settings](https://docs.bugbug.io/preventing-failed-tests/project-settings).&#x20;

We recommend doing this in the following way:

1. Create all the important desktop tests
2. Duplicate the project
3. Rename the new project and add `- Mobile` suffix to the project name
4. Change the screen size to "Mobile" in the project settings
5. Adapt the tests to the mobile version via [re-recording test steps](https://docs.bugbug.io/recording-tests-steps/re-recording-steps).

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FlGZC12L6SOkYpDQF4M8O%2Fimage.png?alt=media&#x26;token=534e92c9-dcdf-410b-8da9-f0a99c98956f" alt=""><figcaption><p>Duplicate the project and change its name</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F9jW3KMcPZnvqm6MOQ1VC%2FZrzut%20ekranu%202023-03-15%20111526.png?alt=media&#x26;token=7337642c-d861-4094-89ed-767d13ead9f1" alt=""><figcaption><p>You can choose a mobile option when creating a new test </p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F4CiUJoL12Py0VzPa5fMN%2FZrzut%20ekranu%202023-03-15%20114211.png?alt=media&#x26;token=86f76954-3bf4-47b0-86bc-8ed87ca64b4d" alt=""><figcaption><p>or change to mobile screen size in test settings. </p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FHmJppQqEBjlfvNAqTqVU%2FZrzut%20ekranu%202023-03-15%20114222.png?alt=media&#x26;token=016fa209-fa63-4bfe-9478-7b1571a975aa" alt=""><figcaption><p>When You copy an existing test </p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FzwWT4J0dfBHPogKfNSd7%2Fimage.png?alt=media&#x26;token=c2358d47-fe19-4b0a-b4a1-69b14dcccc43" alt=""><figcaption><p>Run tests with smaller mobilewindow width</p></figcaption></figure>

{% hint style="info" %}
**Tip!** You can [ask support to move the tests between projects or accounts](https://docs.bugbug.io/organizing-tests/projects#transfer-a-project-to-a-different-organization).&#x20;
{% endhint %}
