# Source: https://docs.brightdata.com/scraping-automation/scraping-browser/features/playground.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Browser API Playground

> Experiment with Browser API using the Playground. Run or edit scripts, view real-time logs, and browser interactions. Currently supports Puppeteer and JavaScript.

The Playground is a code editor for experimenting with the Browser API. With this tool you can run ready-made example scripts or edit the scripts and run your own for testing purposes.
Playground Supported Libraries, Languages and Features

While Browser API supports all common libraries and languages, the current version of the playground can be used with Puppeteer and JavaScript. We promise to add the rest soon enough!

Please note that any features that involve a connection with the user side infrastructure will be supported in production but not in the playground, for example saving files to the user’s file system or using pre-installed libraries like Cheerio. To test Browser API with it’s full capabilities use your usual coding environment.

### Playground Features

* Code editor:
  * By default the code editor will be hosting an example scraper script
  * Script examples can be edited freely or including completely removing them and building any custom script from scratch to run with the Browser API
  * A reset button to revert back to the original example script
* Console logs view
* Web interaction and results view: presents the raw HTML going through the browser or visualizes the browser interactions.

<Frame>
    <img src="https://mintcdn.com/brightdata/YUhP5HZ1PAScLcu8/images/scraping-automation/scraping-browser/features/playground/playground-features.png?fit=max&auto=format&n=YUhP5HZ1PAScLcu8&q=85&s=f2e1f56912d8cac2417ab9c50017642d" alt="playground-features.png" width="1303" height="636" data-path="images/scraping-automation/scraping-browser/features/playground/playground-features.png" />
</Frame>

### Ready Made Example

Run existing example scripts to instantly see the product at work. The example scripts demo the scraping of real target sites. You will be able to see the full script, console logs and a visualization of the browser interaction with the target site.

### Code Editing

Use the code editor to edit the default example scripts or replace them altogether with your own and run any custom scripts to view results or debug your code.
If needed you can always click the reset button and revert back to the original example script.
