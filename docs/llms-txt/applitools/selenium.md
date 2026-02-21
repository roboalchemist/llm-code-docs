# Source: https://applitools.gitbook.io/docs/quickstart/selenium.md

# Selenium

This quickstart has 6 parts with lot of gifs and pictures to help you quickly get upto speed and know how powerful Applitools' AI really is. Not that it will take about 20 minutes after you install the code.&#x20;

{% hint style="info" %}
The tutorial may like a long one but it's mainly because of all the gifs and pictures.&#x20;
{% endhint %}

* Part 1 - 🚀Setup Applitools and create a baseline
* Part 2 - 🐞Find UI bugs and analyze differences using AI
* Part 3 - 🤖Understand why Applitools AI is superior to pixel-by-pixel comparison
* Part 4 -  ✅Accepting 100s of changes by clicking a button instead of updating numerous tests
* Part 5 -  👁Use advanced AI tools to work with real-world scenarios
* Part 6 - 🔥Code highlights
* Part 7 - 👏Congratulations!

### Part 1 - 🚀Setup environment and create a baseline

#### Test Overview:

In this part you will set up the environment to run the test locally and then store a baseline images of just the login page. We will use the app page later on.

![Login page](https://1948935680-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LKyn5-TPBSSSy8ZqPvE%2F-LLBwhVY7ulYV8T4KOU9%2F-LLBx9i4J9PUk9T0LemL%2FScreen%20Shot%202018-08-30%20at%203.28.58%20PM.png?alt=media\&token=76d459ac-3d20-4196-bc35-81e813692a28)

![Main app page](https://1948935680-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LKyn5-TPBSSSy8ZqPvE%2F-LLY7njW9tNe3T49AzcS%2F-LLY9joeVQlmo-FiGye0%2FScreen%20Shot%202018-09-03%20at%2010.59.35%20PM.png?alt=media\&token=5d3afff6-0aec-4727-bd7e-8ea0fe2070b4)

#### Step 1.1: Setup the environment

Please select a language or framework to get started

{% tabs %}
{% tab title="JavaScript" %}

### Prerequisites:&#x20;

* Create Applitools account [create it now](https://applitools.com/sign-up) to obtain your API key
* Please set the `APPLITOOLS_API_KEY` environment variable
  * On Mac: `export APPLITOOLS_API_KEY='YOUR_API_KEY'`
  * On windows: `set APPLITOOLS_API_KEY='YOUR_API_KEY`
* Install `node.js` from <https://nodejs.org>
* Install `git` from[ https://git-scm.com](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* Install Google Chrome browser from [here](https://www.google.com/chrome/)
* Install Chromedriver for node.js `npm install chromedriver`
  {% endtab %}

{% tab title="Java" %}

{% endtab %}

{% tab title="PHP" %}

{% endtab %}

{% tab title="Python" %}

{% endtab %}

{% tab title="C#" %}

{% endtab %}
{% endtabs %}

#### Step 1.2: Download and run the example test

{% tabs %}
{% tab title="JavaScript" %}

1. Clone the following Github repo: `git clone https://github.com/rajaraodv/Applitools-Selenium-JS-Quickstart`
2. Go to *Applitools-Selenium-JS-Quickstart* folder
3. Run `npm install`
4. Run `npm test part1`
5. You should see the test run in a Chrome browser window

{% hint style="info" %}
If you have any issues, please contact us on [Slack](https://slack.com/applitools?ref=quickstart). \<TODO - Where should people go if >
{% endhint %}
{% endtab %}

{% tab title="Java" %}

{% endtab %}

{% tab title="PHP" %}

{% endtab %}

{% tab title="Python" %}

{% endtab %}

{% tab title="C#" %}

{% endtab %}
{% endtabs %}

#### Step 1.3: Check the baseline

Login to [applitools.com](https://eyes.applitools.com/?utm_source=sel_js_part1) and see the results. Applitools app should show the results like below.

![Applitools dashboard (Click to Zoom)](https://1948935680-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LKyn5-TPBSSSy8ZqPvE%2F-LLFkz_XV6guFi4b7Hqj%2F-LLGMo09bPyL8dFmiLoJ%2Ftutorial1part1.png?alt=media\&token=ad8e000a-bcd1-4cfb-bb19-513888e15c59)

{% hint style="info" %}
Note:

1. Click on the "Refresh" icon if you don't see anything
2. &#x20;The "Thumbs up" icon is used to accept the image as a baseline
3. The "save" button is used to save a new baseline image&#x20;

The initial run is automatically accepted as a baseline.
{% endhint %}

Now you have created a baseline image!&#x20;

### &#x20;Part 2 - 🐞Find UI bugs and analyze differences using AI

In this part you'll run the tests again but the test will use a different url to simulate a broken UI.

#### **Step 2.1: Run the test again**

Go to your command line and type the following command. It will test the login page (version 2) again and store the result in Applitools.

`npm test part2`

####

#### **Step 2.2 Analyze the result**

Please switch to Applitools dashboard in your browser.&#x20;

{% hint style="info" %}
Remember to click on the "Refresh" icon in the left panel to see the new test result
{% endhint %}

You will see a new test run with an "unresolved" status. This means Applitools is asking you to check if the differences are valid. If so, accept it and this result will become a new baseline. If not, reject it and your result will be marked as "Failed" and your previous baseline remains as is.

!["Unresolved" test result (Click to Zoom)](https://1948935680-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LKyn5-TPBSSSy8ZqPvE%2F-LLFkz_XV6guFi4b7Hqj%2F-LLGTVM9dIAPUdviHIrd%2FScreen%20Shot%202018-08-31%20at%2012.33.10%20PM.png?alt=media\&token=df5804b4-96aa-448c-9f98-e22e26e163ac)

**Step 2.3: Click on the result image**

![](https://1948935680-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LKyn5-TPBSSSy8ZqPvE%2F-LLPk3Ho6ImkBWukJkCQ%2F-LLRdtmn9kYO4qjFVA8N%2Fclick-on-the-image.gif?alt=media\&token=093bd617-7a4a-4e61-85d3-627367d6fc39)

**Step 2.4 Click on the "Toggle" button to see differences between the baseline and current checkpoint**

![](https://1948935680-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LKyn5-TPBSSSy8ZqPvE%2F-LLPk3Ho6ImkBWukJkCQ%2F-LLRgtUnQKOZcB0EEMFE%2Ftoggle.gif?alt=media\&token=3d56ee60-830f-4b17-89dc-583c5fe05936)

**Step 2.5 Click on the Radar button to highlight differences at once**

This is very handy when your app is complex and has lot of data.

![](https://1948935680-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LKyn5-TPBSSSy8ZqPvE%2F-LLPk3Ho6ImkBWukJkCQ%2F-LLR_zTMDY-Qmz9WR-Q7%2Fradar-button.gif?alt=media\&token=66c8a486-f4c7-4a89-a2b8-0a5f7431c746)

**Step 2.6 Zoom in and see each difference closely**

![](https://1948935680-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LKyn5-TPBSSSy8ZqPvE%2F-LLRjlmTtvj7JuRG6tfp%2F-LLRk6z89AiVu4v-LxVs%2Fzoom-differences.gif?alt=media\&token=b67b8898-dadd-4cbc-8306-ad2c5d1d4e7d)

### **Part 3 - 🤖Understand why Applitools AI eyes is superior to pixel-by-pixel comparison**

In this part you will see how differences between 4 "modes" of comparisons.&#x20;

![Applitools AI provides 4 modes](https://1948935680-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LKyn5-TPBSSSy8ZqPvE%2F-LLRjlmTtvj7JuRG6tfp%2F-LLRkFiS5oGjo9aOInnM%2FScreen_Shot_2018-09-02_at_4_28_31_PM.png?alt=media\&token=77d489ec-ab50-400b-8119-7c0c22797bbe)

#### **Step 3.1 Check out the "Strict" mode by selecting the option in the menu**

This mode uses AI to simulate the differences that are commonly found by the human eye. It ignores some of the minor differences like "off-by-a-pixel" type errors. This help eliminate common false-positives of pixel-by-pixel comparison tools.

![Click to Zoom](https://1948935680-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LKyn5-TPBSSSy8ZqPvE%2F-LLRjlmTtvj7JuRG6tfp%2F-LLRthi9Z7tbXdPGRfCP%2Fstrict-mode.gif?alt=media\&token=6cfa90dc-f174-4c71-9511-78f6f6a8f7a9)

{% hint style="info" %}
This is the default mode. You can set whichever mode you want in code.
{% endhint %}

#### **Step 3.2 Check out the "Exact" mode by selecting the option in the left-menu**

This mode does pixel-by-pixel comparison. This will cause lot of false-positives! This is one of the big reasons why we use AI.

Notice that a lot of things in the background image is also considered as real bugs!👎

![Click to Zoom](https://1948935680-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LKyn5-TPBSSSy8ZqPvE%2F-LLRjlmTtvj7JuRG6tfp%2F-LLRtlYqFzKlaN2kc4cz%2Fexact-mode.gif?alt=media\&token=baf5ccf3-9bf1-4b64-898f-b33c5ad3b65f)

{% hint style="danger" %}
Do not use this mode unless really necessary as it does pixel-by-pixel comparison and may lead to false positives.
{% endhint %}

#### **Step 3.3 Check out "Content" mode by selecting the option in the menu**

In this mode the AI only compares difference in the content or text such as button text.

![Click to Zoom](https://1948935680-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LKyn5-TPBSSSy8ZqPvE%2F-LLRjlmTtvj7JuRG6tfp%2F-LLRtu_FXMu_XSyTdHkl%2Fcontent-mode.gif?alt=media\&token=d4d3d3b9-d7db-4ff1-863f-005fe500169d)

{% hint style="info" %}
Note: If only content has changed, then content mode will be very similar to strict mode.
{% endhint %}

#### **Step 3.4 Check out the "Layout" mode by selecting the option in the left-menu**

This mode shows any major differences in the layouts like a major section is removed.&#x20;

In our example there are no major layout changes so if you were using the layout mode in your code, it would succeed!

![](https://1948935680-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LKyn5-TPBSSSy8ZqPvE%2F-LLRjlmTtvj7JuRG6tfp%2F-LLRwWJe_xD08ua4PjqD%2Flayout-mode.gif?alt=media\&token=2e6e169b-ef7f-49e8-9da8-292c4067f60c)

{% hint style="info" %}
For most scenarios, we recommend using either the "Strict" mode or the "Layout" mode. Use "Content" and "Exact" modes for special cases.
{% endhint %}

### Part 4 - ✅Accepting 100s of changes by clicking a button instead of updating numerous tests

Now let's imagine that you did your analysis and it turns out all those differences are because of just a new version of the app. Typically this mean you'd need to throw out or rewrite 100s of tests! In "Visual testing" you don't have because you didn't really write any tests😊!&#x20;

{% hint style="info" %}
We'll go over the few lines of code you will add to import Applitools and generate images but that's about all the code you'll write. And once you wrote it, it won't change!
{% endhint %}

To accept 100s of changes, simply click on the "Thumbs up" icon.&#x20;

![](https://1948935680-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LKyn5-TPBSSSy8ZqPvE%2F-LLS8Nq0GvGWYY8-ivy9%2F-LLSEWahh_LFcyCQV8SZ%2FScreen%20Shot%202018-09-02%20at%207.22.28%20PM.png?alt=media\&token=930819e5-aca3-47df-a35e-55162ff70703)

There are three options:

1. **"Accept the differences and the checkpoint image of this test step":** This option allows us to accept all the changes for this specific step and not other steps in the same test (if there are multiple steps).
2. &#x20;**"Accept the differences and checkpoint images of all test steps with similar differences":** This option allows us to accept similar differences in all the steps.&#x20;
3. **"Accept the differences and checkpoint images of all test steps":** This accepts all test steps irrespective of similar differences or not. Essentially, you get a new baseline for all test steps.

**Step 4.1 : Select "Accept the differences and the checkpoint image of this test step" option**

**Step 4.2: Press Save**

![](https://1948935680-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LKyn5-TPBSSSy8ZqPvE%2F-LLS8Nq0GvGWYY8-ivy9%2F-LLSS2wk2XDxVAbiFa9T%2FScreen%20Shot%202018-09-02%20at%208.22.16%20PM.png?alt=media\&token=c2bc70cc-8961-4ee3-9b85-ca1b6bb0a5c6)

&#x20;**Step 4.3: Re-run the test**

Switch to the command prompt and run:

`$ npm test part2`

**Step 4.4: Check the result in the Dashboard**

Switch to Applitools dashboard in the browser. Press the "Refresh" button and then you should see "Passed".

![](https://1948935680-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LKyn5-TPBSSSy8ZqPvE%2F-LLS8Nq0GvGWYY8-ivy9%2F-LLSTigHAbTV1a-47Fpk%2FScreen_Shot_2018-09-02_at_8_24_55_PM.png?alt=media\&token=30b47c40-e821-4ac5-a037-f98bfa42ccd3)

### Part 5 -  👁Use advanced AI tools to work with real-world scenarios

In this part you will run tests on the main app page and learn about how to deal with dynamic contents and floating contents.

![](https://1948935680-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LKyn5-TPBSSSy8ZqPvE%2F-LLY7njW9tNe3T49AzcS%2F-LLY9joeVQlmo-FiGye0%2FScreen%20Shot%202018-09-03%20at%2010.59.35%20PM.png?alt=media\&token=5d3afff6-0aec-4727-bd7e-8ea0fe2070b4)

**Step 5.1 Run the test on the main app**

The following command opens the main app and generates screenshot and closes it.

`$ npm test part_5_1`

{% hint style="info" %}
Note that the main app is long goes below the fold. **So the Applitools scrolls down the page twice.** First time to load everything below the scroller and then it goes back up to the top of the page and then it scrolls down the second time to take the screenshot.

This is because we have **eyes.setForceFullPageScreenshot(true); //force scrolling**
{% endhint %}

**Step 5.2 Run the test on the main app (version 2)**

Now run the following command to open up the second version of the app so we can see differences.

`$ npm test part_5_2`

**Step 5.3 See the differences**

![Click to Zoom](https://1948935680-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LKyn5-TPBSSSy8ZqPvE%2F-LLY7njW9tNe3T49AzcS%2F-LLYAENozGLd0XGjmndy%2Fpart4-part4-diffs.gif?alt=media\&token=d548eb4b-4053-4b21-8e8d-b586e65169ed)

**Step 5.4 Dealing with Dynamic contents**

Dynamic contents are contents that constantly change, for example a clock. If you use pixel-by-pixel comparison, your test will fail every time. Thankfully, Applitools provide a simple way to ignore a region so you can continue to visual test the rest of the page.&#x20;

**Step 5.4.1 Click on the "Ignore region" option**&#x20;

**Step 5.4.2 Select the region around the time**

![](https://1948935680-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LKyn5-TPBSSSy8ZqPvE%2F-LLY7njW9tNe3T49AzcS%2F-LLYB0m8Bgg4N6oPDrhh%2Fignore-region.gif?alt=media\&token=a8867ecb-f320-490b-a292-6f3adc5b65b0)

**Step 5.4 Dealing with floating contents**

Sometimes the data remains the same but they move or float around a bit. For example if you center-align some data then if the data changes, the browser will move it a bit to keep it center. But this causes problems for visual test. Again, you can use Applitools' "Floating region" option to manually add some wiggle room.

In our app, the **"Current time is:"** text moves sideways because it is center aligned. Let's add some wiggle room.

**Step 5.4.1 Select "Floating region" option from the menu**

**Step 5.4.2 Select the area around the** **"Current time is:" to add**

![](https://1948935680-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LKyn5-TPBSSSy8ZqPvE%2F-LLY7njW9tNe3T49AzcS%2F-LLYDMFLybfHPWIURnj3%2Ffloating-region.gif?alt=media\&token=1a7ee63a-02be-4475-8f19-48996b668b65)

**Step 5.4.4 Press "Thumbs up"**

**Step 5.4.5 Press "Save"**

### Part 6 - 🔥Code highlights

Here are all the code you need (in addition to your regular test code) and most of it is just one time deal.

5.1 Import the SDK

{% code title="start.js" %}

```javascript
//import the "eyes" SDK
var SeleniumSDK = require("eyes.selenium");
var Eyes = SeleniumSDK.Eyes;
```

{% endcode %}

5.2 Initialize the SDK and set API key

{% code title="start.js" %}

```javascript
// Initialize the eyes SDK and set your private API key.
var eyes = new Eyes();

//⚠️️️Set the APPLITOOLS_API_KEY environment variable
eyes.setApiKey(process.env.APPLITOOLS_API_KEY);

//scroll the entire page (optional)
eyes.setForceFullPageScreenshot(true);
```

{% endcode %}

5.3 Set the application (AUT) name, the test name and set browser's viewport size

{% code title="start.js" %}

```javascript
  eyes.open(driver, testSelector.appName, testSelector.testName, {
    width: testSelector.viewportWidth,
    height: testSelector.viewportHeight
  });
```

{% endcode %}

5.4 Generate screenshot.&#x20;

This line uploads the image data to Applitools for the AI to compare differences, generate baseline and so on.

{% code title="start.js" %}

```javascript
 // Visual checkpoint #1.
  eyes.checkWindow(testSelector.windowName);
```

{% endcode %}

5.5 Close Applitools

{% code title="start.js" %}

```javascript
// If the test was aborted before eyes.close was called ends the test as aborted.
  eyes.close();

```

{% endcode %}

{% hint style="info" %}
Note that because this example has only one test, the code you include to add Applitools may look like a lot but that's most of the code you'll write even if you write 1000 tests! Only thing you'll add for the rest of the test is "eyes.checkWindow()", "eyes.checkRegion()" etc lines
{% endhint %}

Here is all the code from the test [script.js](https://github.com/rajaraodv/script.js) **\<TODO change the link>**

```javascript
require("chromedriver");

var webdriver = require("selenium-webdriver");
var Capabilities = webdriver.Capabilities;
var Builder = webdriver.Builder;
var By = webdriver.By;

var SeleniumSDK = require("eyes.selenium");
var Eyes = SeleniumSDK.Eyes;
var ConsoleLogHandler = SeleniumSDK.ConsoleLogHandler;

//Runs different tests based on CLI input such as "part1", "part2" and so on.
var testSelector = require("./testSelector.js");
console.log(testSelector);

// Open a Chrome browser.
var driver = new Builder().withCapabilities(Capabilities.chrome()).build();

// Initialize the eyes SDK and set your private API key.
var eyes = new Eyes();

//⚠️️️  Please set the APPLITOOLS_API_KEY environment variable
//on Mac: export APPLITOOLS_API_KEY='YOUR_API_KEY'
//on windows: set APPLITOOLS_API_KEY='YOUR_API_KEY'
//Note: You can get your API key by logging into Applitools | Click on the person icon (top-right corner) | Click on the "My API key" menu
eyes.setApiKey(process.env.APPLITOOLS_API_KEY);

//scroll the entire page
eyes.setForceFullPageScreenshot(true);

if (!process.env.APPLITOOLS_API_KEY) {
  console.log(`
     ⚠️️️  Please set the APPLITOOLS_API_KEY environment variable

        * On Mac: export APPLITOOLS_API_KEY='YOUR_API_KEY'
        
        * On windows: set APPLITOOLS_API_KEY='YOUR_API_KEY'
        
        * Please Note: You can get your API key by logging into applitools.com | Click on the person icon (top-right corner) | Click on the "My API key" menu
    `);
  process.exit(0);
}

//eyes.setLogHandler(new ConsoleLogHandler(false));

try {
  // Set the application (AUT) name, the test name and set browser's viewport size
  eyes.open(driver, testSelector.appName, testSelector.testName, {
    width: testSelector.viewportWidth,
    height: testSelector.viewportHeight
  });

  // Navigate the browser to the "hello world!" web-site.
  driver.get(testSelector.url);

  // Visual checkpoint #1.
  eyes.checkWindow(testSelector.windowName);

  //Only go to the main app page if the test/tutorial needs it
  if (testSelector.goto2ndPage) {
    // Click the "Click me!" button.
    driver.findElement(By.id("log-in")).click();

    // Visual checkpoint #2.
    eyes.checkWindow("Click!");
  }

  // End the test.
  eyes.close(false);
} finally {
  // Close the browser.
  driver.quit();

  // If the test was aborted before eyes.close was called ends the test as aborted.
  eyes.abortIfNotClosed();
}

```

### Part 7 - 👏Congratulations!

Congratulations on completing the quick start. Here are the links for you to learn more:

\<Links to Docs>
