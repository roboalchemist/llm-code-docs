# Source: https://docs.apify.com/academy/tools/edit-this-cookie.md

# EditThisCookie

**Learn how to add, delete, and modify different cookies in your browser for testing purposes using the EditThisCookie Chrome extension.**

***

**EditThisCookie** is a Chrome extension to manage your browser's cookies. It can be added through the https://chromewebstore.google.com/detail/editthiscookie-v3/ojfebgpkimhlhcblbalbfjblapadhbol. After adding it to Chrome, you'll see a button with a delicious cookie icon next to any other Chrome extensions you might have installed. Clicking on it will open a pop-up window with a list of all saved cookies associated with the currently opened page domain.

![EditThisCookie popup](/assets/images/edit-this-cookie-popup-25db9f40d6518c224bc602a2a8d23acf.png)

## Functionalities

At the top of the popup, there is a row of buttons. From left to right, here is an explanation for each one:

### Delete all cookies

Clicking this button will remove all cookies associated with the current domain. For example, if you're logged into your Apify account and delete all the cookies, the website will ask you to log in again.

### Reset

A refresh button.

### Add a new cookie

Manually add a new cookie for the current domain.

### Import cookies

Allows you to add cookies in bulk. For example, if you have saved some cookies inside your crawler, or someone provided you with some cookies for the purpose of testing a certain website in your browser, they can be imported and automatically applied with this button.

### Export cookies

Copies an array of cookies associated with the current domain to the clipboard. The cookies can then be later inspected, added to your crawler, or imported by someone else using EditThisCookie.

### Search

Allows you to filter through cookies by name.

### Options

Will open a new browser tab with a bunch of EditThisCookie options. The options page allows you to tweak a few settings such as changing the export format, but you will most likely never need to change anything there.

![EditThisCookie options](/assets/images/edit-this-cookie-options-5d3bf2114475f966187a349bc0af84ec.png)
