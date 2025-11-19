# Source: https://docs.apify.com/platform/actors/development/quick-start/web-ide.md

# Web IDE

**Create your first Actor using the web IDE in Apify Console.**

***

## What you'll learn

This guide walks you through the full lifecycle of an Actor. You'll start by creating and running it locally with the Apify CLI, then learn to configure its input and data storage. Finally, you will deploy the Actor to the Apify platform, making it ready to run in the cloud.

### Prerequisites

* An Apify account. https://console.apify.com/sign-up on the Apify website.

### Step 1: Create your Actor

Log in to https://console.apify.com, navigate to https://console.apify.com/actors/development/my-actors, then click the **Develop new** button.

![Create Actor](/assets/images/create-actor-69b32bf8ad2b2173628df60685cb9969.png)

You'll see Actor development templates for `JavaScript`, `TypeScript`, and `Python`.

These templates provide boilerplate code and a preconfigured environment. Choose the template that best suits your needs. For the following demo, we'll proceed with **Crawlee + Puppeteer + Chrome**.

Explore Actor templates

Browse the https://apify.com/templates to find the best fit for your Actor.

![Templates](/assets/images/actor-templates-b19999bcbcd98ba04d9c66f73632c38f.png)

After choosing the template, your Actor will be automatically named and you'll be redirected to its page.

### Step 2: Explore the Actor

The provided boilerplate code utilizes the https://docs.apify.com/sdk/js/ combined with https://crawlee.dev/, Apify's popular open-source Node.js web scraping library.

By default, the code crawls the https://apify.com website, but you can change it to any website.

Crawlee

https://crawlee.dev/ is an open-source Node.js library designed for web scraping and browser automation. It helps you build reliable crawlers quickly and efficiently.

### Step 3: Build the Actor

To run your Actor, build it first. Click the **Build** button below the source code.

![Actor source code](/assets/images/actor-source-code-270416bb696b5630433cfb3a5405cef7.png)

Once the build starts, the UI transitions to the **Last build** tab, showing build progress and Docker build logs.

![Actor build](/assets/images/actor-build-b15fc0543e1cdf15b2f97ab8aa983ebb.png)

Actor creation flow

The UI includes four tabs:

* **Code**
* **Last build**
* **Input**
* **Last Run**

This represents the Actor creation flow, where you first build the Actor from the source code. Once the build is successful, you can provide input parameters and initiate an Actor run.

### Step 4: Run the Actor

Once the Actor is built, you can look at its input, which consists of one field - **Start URL**, the URL where the crawling starts. Below the input, you can adjust the **Run options**:

* **Build**
* **Timeout**
* **Memory limit**

![Actor input](/assets/images/actor-input-60fb9eef613c689fd1d9427d6749cb97.png)

To initiate an Actor run, click the **Start** button at the bottom of the page. Once the run is created, you can monitor its progress and view the log in real-time. The **Output** tab will display the results of the Actor's execution, which will be populated as the run progresses. You can abort the run at any time using the **Abort** button.

![Actor run](/assets/images/actor-run-f17d17bfc7366c2a827219ce5be64f53.png)

### Step 5: Pull the Actor

To continue development locally, pull the Actor's source code to your machine.

Prerequisites

Install `apify-cli` :

* macOS/Linux
* Other platforms


```
brew install apify-cli
```



```
npm -g install apify-cli
```


To pull your Actor:

1. Log in to the Apify platform


   ```
   apify login
   ```


2. Pull your Actor:


   ```
   apify pull your-actor-name
   ```


   Or with a specific version:


   ```
   apify pull your-actor-name --version [version_number]
   ```


   As `your-actor-name`, you can use either:

   * The unique name of the Actor (e.g., `apify/hello-world`)
   * The ID of the Actor (e.g., `E2jjCZBezvAZnX8Rb`)

You can find both by clicking on the Actor title at the top of the page, which will open a new window containing the Actor's unique name and ID.

### Step 6: It's time to iterate!

After pulling the Actor's source code to your local machine, you can modify and customize it to match your specific requirements. Leverage your preferred code editor or development environment to make the necessary changes and enhancements.

Once you've made the desired changes, you can push the updated code back to the Apify platform for deployment & execution, leveraging the platform's scalability and reliability.

## Next steps

* Visit the https://docs.apify.com/academy.md to access a comprehensive collection of tutorials, documentation, and learning resources.
* To understand Actors in detail, read the https://whitepaper.actor/.
* Check https://docs.apify.com/platform/actors/development/deployment/continuous-integration.md documentation to automate your Actor development process.
* After you finish building your first Actor, you can https://docs.apify.com/platform/actors/publishing.md.
