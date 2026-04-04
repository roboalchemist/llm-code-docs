# Source: https://clickwrap-developer.ironcladapp.com/docs/integrating-clickwrap-without-psjs.md

# Integrating Ironclad Clickwrap without PS.js

The guide will cover a server-side setup for accepting clickwraps.

In order to send acceptance of contracts completely server-side, you can simply set up 2 API calls with Ironclad Clickwrap to:

1. Get the latest published Version IDs for the Group you're going to be loading on the page.
2. Send acceptance of those Contract Versions after a user accepts them as part of a registration or login flow in your app.

### What you need to get started

* You should have familiarity with the [Activity API](https://clickwrap-developer.ironcladapp.com/docs/what-is-the-activity-api)
* A working registration flow including a processing back-end in which to send acceptance of terms as part of a login or registration for your app.
* A published [Group](https://app.pactsafe.com/groups) in Ironclad Clickwrap's dashboard (which will require *public, published* [Contracts](https://app.pactsafe.com/contracts))

<Image title="Image 2018-01-10 at 2.23.11 PM.png" alt={1236} src="https://files.readme.io/2f76af7-Image_2018-01-10_at_2.23.11_PM.png">
  Here's an example flow for how you'll interact with the Ironclad Clickwrap API to process acceptance. This flow includes use of PS.js to actually load the checkbox and links to the agreements being accepted via click-through.
</Image>

> 👍 Details & code samples on the Activity API
>
> More details and code samples for interacting with the Activity API can be found in our [Reference here](https://developer.pactsafe.com/v1.1/reference).

## 1. Get the latest published Version IDs for your Group

After creating your Group in Ironclad Clickwrap, you'll have a group `key` that you can reference when making a call to Ironclad Clickwrap. This call will give you back the Contract IDs and Version IDs associated with the Contracts you need your users to accept when creating an account.

After making your `HTTP GET` to `https://pactsafe.io/published?...` (as specified [here](https://clickwrap-developer.ironcladapp.com/reference/get-the-latest-published-versions-for-a-group-1)), you'll receive the following results:

```json
{
    "282":  "592491db0a8eb8133e7a3c5b",
    "1241": "592494670a8eb8133e7a3c67"
}
```

You can then save those values in your form and pass them to the next page for processing acceptance after your user submits their form. We'd recommend saving contract IDs and version IDs as respective hidden `<input>` fields on your page:

```html
...
<input type="hidden" name="_ps_contracts" value="282,1241" />
<input type="hidden" name="_ps_versions" value="592491db0a8eb8133e7a3c5b,592494670a8eb8133e7a3c67" />
...
```

## 2. Send acceptance of those Contract Versions after a user accepts them

Once your user submits the form, you can then send acceptance of those contracts & versions through the Activity API. By calling an `HTTP GET` (or `POST`) to `https://pactsafe.io/send` (as specified [here](https://clickwrap-developer.ironcladapp.com/reference/send-contracts-signedaccepted-by-signer)). The response to this call will be a 1x1 web beacon, and is handled asynchronously in Ironclad Clickwrap.

### Additional values you can pass

There are some required parameters to pass, but you can also pass additional parameters to reinforce the acceptance record. Below are some additional URL parameters to the `/send` call that you can pass to track things like User Agent and IP Address:

* **IP Address:** addr=192.0.0.1
* **Operating System:** os=MacOS
* **Environment:** env=desktop
* **Screen Color Depth:** scd=24-bit
* **Screen Resolution:** res=1280x800
* **Browser Locale:** bl=en-us
* **Browser Time Zone:** btz=5
* **Browser User Agent:** bua="Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_15\_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15"
* **Page Encoding:** pae=UTF-8
* **Page Path:** pap=/saas/app/register.html
* **Page Domain:** pad=neighborino.co
* **Page URL:** pau=[https://neighborino.co/saas/app/register.html](https://neighborino.co/saas/app/register.html)
* **Page Title:** pat=Angle - Bootstrap Admin Template