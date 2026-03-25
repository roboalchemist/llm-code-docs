# Source: https://docs.newrelic.com/docs/synthetics/synthetic-monitoring/getting-started/get-started-synthetic-monitoring/

Title: Get started with synthetic monitoring

URL Source: https://docs.newrelic.com/docs/synthetics/synthetic-monitoring/getting-started/get-started-synthetic-monitoring/

Markdown Content:
Have an application that needs to stay live? Synthetic monitoring helps you proactively catch and resolve issues before they affect your customers, all without an installation.

Check page load performance
---------------------------

Our simple browser monitor lets you check the availability and performance of a single page, including a full page load.

### Paste in a URL

Grab the URL of a page you want to test and drop it in the **URL** field. For best results, we recommend:

*   Selecting at least three locations that your monitor deploys from. This helps you avoid false positives on your checks.
*   Using multiple browser types, using a combination of Chrome and Firefox.
*   Adjusting the time period between checks with the **Period** dropdown. How often you test is entirely up to you.

### View your data

[![Image 1: A screenshot of the summary page after a simple browser monitor reports data](https://docs.newrelic.com/images/synthetic_screenshot-full_Results-page-for-simple-browser-monitor.webp)](https://docs.newrelic.com/images/synthetic_screenshot-full_Results-page-for-simple-browser-monitor.webp)

Mimic simple user workflows with codeless monitoring
----------------------------------------------------

You can build codeless step monitors that run through common user workflows. This is a good choice if you want to mimic simple behaviors across your app, like navigating across different pages, testing page elements, or typing and submitting text into text fields.

### Define your steps

Mix and match from a selection of 12 prebuilt steps. Your monitor can be simple, like clicking buttons to hop through different pages, or you can test a journey that looks like:

1.   A customer goes to your web app

2.   They type their email into a page modal

3.   They select from a dropdown and navigate to a different page

4.   They select something on this page, such as an item to purchase

5.   They fill out forms with secure credentials purchase that item, then submits those forms

Whatever you choose to build, remember to click **Validate** before saving your monitor. Validating checks that the steps you've strung together run successfully.

### View your data

[![Image 2: A screenshot of the summary page after a simple browser monitor reports data](https://docs.newrelic.com/images/synthetic_screenshot-crop_Step-monitor-summary-page.webp)](https://docs.newrelic.com/images/synthetic_screenshot-crop_Step-monitor-summary-page.webp)

Test site behavior with scripted monitoring
-------------------------------------------

Scripted browser monitors are a flexible monitor type that let you test website behavior. Scripting lets you deploy monitors that respond to your web apps like a customer might, choosing different paths across your site depending on conditions you've scripted.

You might choose to create a scripted browser monitor instead of a step monitor if:

*   You want to define custom timeout values
*   You want a script to take actions not offered in our step builder
*   You want to set conditions that change the path your monitor takes if those conditions are met

`// Visit `http://telco.nrdemo.com/`$webDriver.get("http://telco.nrdemo.com/");`

`$webdriver.get()` sends your monitor to the domain you want to monitor.

`$webDriver.get("http://telco.nrdemo.com/").then(function(){  // Find a link with display text that matches `About`  return $webDriver.findElement($selenium.By.linkText("About")).click();  // Click the link that matches `About`}).then(function(){    return $webDriver.findElement($selenium.By.partialLinkText("Home")).click();});`

Once your monitor goes to a URL, `$webDriver.findElement()` finds the defined element, then implements an action, in this case `click()`. When the action is complete, the monitor navigates back to the home page using the same logic.

`async function waitForAndFindElement(locator, timeout){  const element = await $webDriver.wait($selenium.until.elementLocated(locator), timeout, 'Timed-out waiting for element to be located using: '+locator);  await $webDriver.wait($selenium.until.elementIsVisible(element), timeout, 'Timed-out waiting for element to be visible using ${element}');  return await $webDriver.findElement(locator);}await $webDriver.get("http://telco.nrdemo.com/")await $webDriver.findElement($selenium.By.id("supportDropDown")).click();// Wait up to 20000 seconds for the FAQ page to appearlet aboutPage = await waitForAndFindElement($selenium.By.id("supportFAQLink"), 20000)await aboutPage.click();`

Scripted browser monitors can wait a specified amount of time before reporting an error. Since some images or dynamic elements take time to generate, you can give parameters to `$webDriver.waitForandFindElement()`. In this snippet, your monitor finds `"supportFAQLink"`, then waits `20000` seconds before reporting an error.

`$webDriver.get("http://example.com/login.jsp").then(function(){  return $webDriver.findElement($selenium.By.name("username")).sendKeys($secure.SECURE_USERNAME);}).then(function(){  // Find the password field by specifying its name, then submits a secured password.  return $webDriver.findElement($selenium.By.name("password")).sendKeys($secure.SECURE_PASSWORD);}).then(function(){  // Find and click the login button.  return $webDriver.findElement($selenium.By.xpath("//inp[@value='Login']")).click();});`

You can test elements that require login info, too. We recommend that you create unique credentials for your script.

Go to **[one.newrelic.com > Synthetic monitoring > Create a monitor](https://one.newrelic.com/synthetics-nerdlets/monitor-create)**, then choose **User flow/functionality** for scripted browser.

What's next?
------------

Now that you've created your first set of monitors, you're ready to explore our other features. We recommend checking out these docs:

*   Set up [alerts for synthetic monitors](https://docs.newrelic.com/docs/synthetics/synthetic-monitoring/using-monitors/alerts-synthetic-monitoring/) so you're notified when a check fails
*   Curious about how it all works? [Get a general overview of synthetic monitors](https://docs.newrelic.com/docs/synthetics/synthetic-monitoring/using-monitors/intro-synthetic-monitoring/)
