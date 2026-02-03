# Source: https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-split-url-test.md

# How to Set Up a Split URL Test

{% embed url="<https://www.loom.com/share/d106c570d0224bbeaacb317712654dc6>" %}
Video: How to create and set up a Split URL Test with Intelligems
{% endembed %}

## **Step 1: Create a new test**

Navigate to the "A/B Tests" tab in the menu on the left-hand side of the Intelligems app. Once you're there, click 'Create New Test' above the experiments table. Give it a name, and a helpful description. Then select "Content Test" , then "Split URL Test", then "Create Test".

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-14655bd151e01d03cfce92763d4d8299a66cd965%2FStep%201.gif?alt=media" alt=""><figcaption></figcaption></figure>

## **Step 2: Create your test groups**

Create a test group for each redirect variation you want to include in the test. Fill in the Test Name and Test Description for the experiment you are creating. This information is all internal - the more detail you include here the better! Tests can be live for several weeks, and your future self will thank you for including the details here.

You can add new groups to include in the test by clicking on the ‘+’ button. Name the groups for the experiment and use the slider to allocate what percentage of traffic will go to each group. Click ‘Next Step’ when you are done.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-773ff2f961fca4dcfb3be8a16e743d7b5ea6f01b%2FStep%202.gif?alt=media" alt=""><figcaption></figcaption></figure>

## **Step 3:** Set up redirects

There are two types of redirects:

* **Simple Redirects** - this type of redirect is best used when targeting a small quantity of specific URLs
* **Advanced Redirects** - this type of redirect is best used when targeting many URLs that have a similar pattern

### Simple Redirect Setup

Enter the URL you want to *redirect from* in the Origin URL field. Then, for each test group enter the URL you want to *redirect to*.

In the example below, we redirect from <https://deepdish-pizza.myshopify.com/page-a> to <https://deepdish-pizza.myshopify.com/page-b>. When visitors land on <https://deepdish-pizza.myshopify.com/page-a>, those in the Control Group will remain at the original URL, while those in the test group "Redirect Test Group" will be redirected to <https://deepdish-pizza.myshopify.com/page-b>. Create a Redirect for each origin URL you want to redirect from.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-a8a234632ae2176b141198ab138b06a0faec78a3%2FScreenshot%202024-12-06%20at%2012.54.01%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure>

### Advanced Redirect Setup

Advanced redirects allow for more flexibility when defining the criteria for a qualifying page URL.

Start by choosing a matching option and entering a value to match against.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-b93925d6103458f66ea8bf74ca06330693b5d454%2Fstep%203.gif?alt=media" alt=""><figcaption></figcaption></figure>

Here are some examples of different matching options with values:

* **matches exactly** - `https://deepdish-pizza.myshopify.com/en-us/cool-collections/product-a`
* **contains** - `sofa`
* **ends with -** `/products/product-a` Note: this will evaluate the URL Path and ignore query parameters. So `https://example.com/products/product-a?utm_source=abc` DOES meet the conditions here
* matches regex - `^.*\/[a-zA-Z]{2}-[a-zA-Z]{2}\/pages\/abc$` This regex expression checks for a URL in the pattern `example.com/en-US/pages/abc.`

Make sure all matching conditions are case *insensitive.*

{% hint style="warning" %}
**Products Redirects**

For most product redirects, it would be better to use ENDS WITH than CONTAINS.

For example, if you use contains `/products/product-abc` but you also have a `/products/product-abc-plus`, then that would match both products. If you were looking to just target the non-plus version, you should use ENDS WITH.
{% endhint %}

{% hint style="info" %}
Note: "/cool-collections" will be evaluated differently than "cool-collections". A redirect set to look for "cool-collections" (without a leading /) will evaluate to true for pages <https://deepdish-pizza.myshopify.com/en-us/cool-collections> AND <https://deepdish-pizza.myshopify.com/en-us-cool-collections> whereas a redirect set to look for "/cool-collections" will only evaluate to true for <https://deepdish-pizza.myshopify.com/en-us/cool-collections>.
{% endhint %}

After selecting a matching option and entering a condition, select which type of Redirect Type to use:

* Replace Full URL - this option updates the entire URL
* Replace Matching Text - this option will allow you to find specific values in the current page URL and replace them with text of your choosing

If you choose `Replace Full URL`, you'll need to enter a full valid URL for each test group redirect. If you choose `Replace Matching Text`, you'll need to enter valid find and replace values.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-067e3387bd768c44c3f357492c0fb2ef22fc33a2%2Fstep%204.gif?alt=media" alt=""><figcaption></figcaption></figure>

### Additional Features

#### Redirect One Time vs. Redirect Every Time

Selecting `Redirect One Time` ensures that this redirect only fires one time for each visitor. On subsequent visits to the origin URL, visitors will be left on that page and not redirected again. This is the default behavior when creating a redirect.

An example of when you'd want to choose `Redirect One Time`: say you're sending some traffic from a Facebook ad to your homepage, and you want to test to see if using a landing page from the ad would be better. If you didn't select `Redirect One Time` for this, then visitors from the ad who are in the test group would be redirected to the landing page every time they tried to go to the homepage.

An example of when you'd want to select `Redirect Every Time`: say you're testing two versions of a collection page. You would want your visitors in the test group to be redirected every time they went to that collection page so they always see the same version.

You can test different URLs in the Redirect Checker to see where a user in each test group would get redirected.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-559b12e9f1b52e798b3b264f17089e24316dc328%2Fstep%205.gif?alt=media" alt=""><figcaption></figcaption></figure>

#### Query Parameters

You can add or modify query parameters for each redirect. Query parameters will *not* be evaluated when deciding if an origin URL qualifies for a redirect. Only the domain and pathname will be evaluated.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-f4c2b9c0229cff5807a9b2bf7d02c27fca9672a4%2Fstep%206.gif?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note: Query parameters from the origin URL *will be persisted* to the redirect URL even if they are not added in Intelligems. Use Intelligems query parameters to add new values or modify existing values.
{% endhint %}

#### Subdomain Redirects

Intelligems allows you to test redirects between subdomains. All subdomains used in a redirect test must be registered as a subdomain on your primary domain.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-9fb2ca4b0d597652a58b80a455aed49645e2fdee%2Fstep%207.gif?alt=media" alt=""><figcaption></figcaption></figure>

#### Multiple Domain Support

If your brand operates multiple domains under one Shopify account (e.g., dogsuppy.com and dogsuppy.co.uk), you can register all of them in your Intelligems Settings. This allows you to set up Split URL tests for each domain without manually switching your primary domain.

**Example setup for multi-domain brands:**

| Origin URL             | Redirect URL               | Supported? |
| ---------------------- | -------------------------- | ---------- |
| dogsuppy.com/landing   | try.dogsuppy.com/landing   | ✅ Yes      |
| dogsuppy.co.uk/landing | try.dogsuppy.co.uk/landing | ✅ Yes      |
| dogsuppy.com/landing   | dogsuppy.co.uk/landing     | ❌ No       |

**Important:** Cross-domain redirects (redirecting visitors from one top-level domain to a different top-level domain) are not supported. Each domain's redirects must stay within that domain or its subdomains.

To register additional domains, go to **Settings → Domain Settings** in the Intelligems app.

## **Step 4: Set up targeting if needed**

Targeting is an optional step. By default, a visitor will only be included in a split URL test if they visit the origin URL. When a visitor lands on the origin URL, they are randomized into a test group. If they are not in the control group, they are redirected to the specified destination URL.

The targeting tool allows you to apply specific conditions to certain site visitors. There are a few different ways you can do this:

* You can set up currency and country targeting that allows you to limit your test to a single currency and/or a list of specific countries. This feature is defaulted to your store currency for price test.
* You can use UTM parameters to customize your user experience under the Audience option.
* You can filter traffic based on JavaScript Expressions under the Audience option.
* You can filter traffic based on device type (i.e. mobile or desktop) under the Audience option.
* You can filter traffic based off of whether a visitor is new or returning under the Audience option.
* You can prevent users from being targeted by related experiments to reduce undesired interactions under the Mutually Exclusive Tests option.

You can learn more about targeting [here](https://docs.intelligems.io/content-testing/targeting)!

### **Example: Creating a Split URL Test for a Meta Campaign**

{% embed url="<https://www.loom.com/share/2a716fb9605e4c649fab9f88fa6e36b4?sid=e23fe9c9-4c1a-478a-9913-a1a9395e332f>" %}

## **Step 5: Set Your Test Goals**

Finally, select whether analytics should by default consider only orders containing certain products you want to test (for example something related to a particular PDP), or orders containing any products in your shop.\
\
You can always change this later after the test has started by changing the option in your Analytics filters.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-6d8a8153d12df819de248b2eceab169cc920d521%2Fstep%208.gif?alt=media" alt=""><figcaption></figcaption></figure>
