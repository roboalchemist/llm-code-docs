# Source: https://developers.google.com/chart/interactive/faq

Title: Frequently Asked Questions

URL Source: https://developers.google.com/chart/interactive/faq

Markdown Content:
[Skip to main content](https://developers.google.com/chart/interactive/faq#main-content)

* [Home](https://developers.google.com/chart)
* [Guides](https://developers.google.com/chart/interactive/docs)
* [Reference](https://developers.google.com/chart/glossary)
* [Support](https://developers.google.com/chart/interactive/support)

* [Overview](https://developers.google.com/chart/interactive/support)
* [Forum](https://groups.google.com/group/google-visualization-api)
* [Release Notes](https://developers.google.com/chart/interactive/docs/release_notes)
* [Issues & Requests](https://github.com/google/google-visualization-issues/issues)
* [FAQ](https://developers.google.com/chart/interactive/faq)
* [Hall of Fame](https://developers.google.com/chart/interactive/docs/user_gallery)

Frequently Asked Questions Stay organized with collections  Save and categorize content based on your preferences
------------------------------------------------------------------------------------------------------------------

* On this page
* [Getting Started](https://developers.google.com/chart/interactive/faq#getting-started)
* [Using the API](https://developers.google.com/chart/interactive/faq#using-the-api)
* [Troubleshooting](https://developers.google.com/chart/interactive/faq#troubleshooting)
* [Google Visualization Program Policy](https://developers.google.com/chart/interactive/faq#policy)
* [Becoming Active in the Community](https://developers.google.com/chart/interactive/faq#becoming-active-in-the-community)

* The Google Visualization API helps you create charts and reporting applications over structured data and integrate them into your website.

* You can access structured data, implement your own data source, and visualize data with the Google Visualization API.

* The Google Visualization API uses a JavaScript API and its gallery of charts is open to third parties.

* To use charts offline or host the code locally, you must use https://www.gstatic.com/charts/loader.js and our terms of service do not allow you to download the code.

* If you have questions or problems, post them in the Google Visualization API discussion group for community and team support.

* **Getting Started**
  * [What is the Google Visualization API?](https://developers.google.com/chart/interactive/faq#whatis)
  * [What can I do with the Visualization API?](https://developers.google.com/chart/interactive/faq#whatcan)
  * [Where can I find documentation for the Visualization API?](https://developers.google.com/chart/interactive/faq#wherecan)
  * [How do I create a new Chart?](https://developers.google.com/chart/interactive/faq#createvisualization)
  * [What is a Data Source URL?](https://developers.google.com/chart/interactive/faq#datasourceurl)
  * [Where can I find example code of Chart apps using the Visualization API?](https://developers.google.com/chart/interactive/faq#samplecode)
  * [Can a Flash application access the Visualization API?](https://developers.google.com/chart/interactive/faq#flash)
  * [Can I access a chart from a Java application?](https://developers.google.com/chart/interactive/faq#Java)
  * [Can I access a chart from an application written with the Google Web Toolkit (GWT) compiler?](https://developers.google.com/chart/interactive/faq#GWT)
  * [I have a different question/problem, who do I contact to get more information?](https://developers.google.com/chart/interactive/faq#contact)

* **Using the API**
  * [What is the difference between the Google Chart API and the Google Visualization API?](https://developers.google.com/chart/interactive/faq#chartapi)
  * [What data sources can I access using the Visualization API?](https://developers.google.com/chart/interactive/faq#datasources)
  * [My application expects the data it receives to be in a specific format. How do I handle exceptions?](https://developers.google.com/chart/interactive/faq#handleexception)
  * [Is it safe to embed a chart in my web site?](https://developers.google.com/chart/interactive/faq#isitsafe)
  * [Can I use charts offline?](https://developers.google.com/chart/interactive/faq#offline)
  * [Can I download and host the chart code locally, or on an intranet?](https://developers.google.com/chart/interactive/faq#localdownload)

* **Troubleshooting**
  * [My chart is not showing up on the page. What is the problem?](https://developers.google.com/chart/interactive/faq#notshowing)
  * [Why are my months and days off by one?](https://developers.google.com/chart/interactive/faq#funnydates)
  * [Why do my charts fail in Internet Explorer 8 and older versions?](https://developers.google.com/chart/interactive/faq#ie8commas)
  * [Why does my Flash-based chart not work during development?](https://developers.google.com/chart/interactive/faq#flashdevelopment)

* **Google Visualization API Policy**
  * [What is the Google Visualization Program Policy?](https://developers.google.com/chart/interactive/faq#policy)
  * [Is the Google Visualization API available for commercial use?](https://developers.google.com/chart/interactive/faq#commercialuse)
  * [Can I use the Google Visualization API to create client-side software?](https://developers.google.com/chart/interactive/faq#creatingaclient)
  * [Is Google logging all my chart data?](https://developers.google.com/chart/interactive/faq#logging)
  * [Violations of the program policies](https://developers.google.com/chart/interactive/faq#violatingpolicies)

* **Becoming Active in the Community**
  * [How can I share my Chart application with others?](https://developers.google.com/chart/interactive/faq#share)
  * [What is the Chart Gallery?](https://developers.google.com/chart/interactive/faq#gallery)
  * [How do I implement a data source?](https://developers.google.com/chart/interactive/faq#getting_started_how_implement_data_source)

Getting Started
---------------

What is the Google Visualization API? The Google Visualization API allows you to create charts and reporting applications over structured data and helps integrate these directly into your website.What can I do with the Visualization API? With the Google Visualization API, you can access structured data--created locally in your browser or retrieved from supported data sources in a simple tabular format. You can also implement your own data source as Visualization API data source and enable any Visualization-compliant visualization and/or application to access your data. The format is amenable to use by reporting, analysis or chart applications. You can thus visualize the data and/or add new functionality to applications, such as Google Spreadsheets.Where can I find documentation for the Visualization API? You can find the developer guide and all other related documentation at [https://developers.google.com/chart/interactive/docs](https://developers.google.com/chart/interactive/docs).How do I create a new Chart? The best way to get started is to read the [Introduction](https://developers.google.com/chart/interactive/docs), and the [Quickstart](https://developers.google.com/chart/interactive/docs/quick_start) section.What is a Data Source URL? A Data Source URL is the unique URL identifier of a Visualization API data source. A data source URL may also include Chart [Query Language](https://developers.google.com/chart/interactive/docs/querylanguage#Setting_the_Query_in_the_Data_Source_URL) parameters. In this case a query (such as sorting, grouping, etc) is performed on the data source prior to fetching the data.Where can I find example code of Chart apps using the Visualization API? You can find example code at the Visualization API [example code](https://developers.google.com/chart/interactive/docs/examples) documentation.Can a Flash application access the Visualization API? Absolutely. The Visualization API uses a JavaScript API, but there are libraries that enable Flash apps to connect with Javascript code. One such library you may find useful can be found at [http://code.google.com/p/swfobject](http://code.google.com/p/swfobject). See [below](https://developers.google.com/chart/interactive/faq#flashdevelopment) for some development issues affecting Flash.How do I implement a data source?Read the section on [using and creating](https://developers.google.com/chart/interactive/docs/quick_start) a chart, to learn how charts work, then read [Implementing a Data Source](https://developers.google.com/chart/interactive/docs/dev/implementing_data_source) to learn how to create a data source. You can also use the [Google Chart Data Source Java library](https://developers.google.com/chart/interactive/docs/dev/dsl_about) to get started quickly if you use Java.Can I access a chart from a Java application? Yes. The [Google Visualization Library](http://code.google.com/docreader/#p=gwt-google-apis&s=gwt-google-apis&t=Visualization) for the Google Web Toolkit (GWT) allows you to access the API compliant visualizations from Java code compiled with the GWT compiler and to write Visualization API compliant visualizations in Java using the GWT complier. The release candidate library also supports the Visualization API event model. Can I access a chart from an application written with the Google Web Toolkit (GWT) compiler? Yes. The [Google Visualization Library](http://code.google.com/docreader/#p=gwt-google-apis&s=gwt-google-apis&t=Visualization) for the Google Web Toolkit (GWT) allows you to access the API compliant visualizations from Java code compiled with the GWT compiler and to write Visualization API compliant visualizations in Java using the GWT complier. The release candidate library also supports the Visualization API event model. I have a different question/problem, who do I contact to get more information? Please post your question in the [Google Visualization API discussion group](http://groups.google.com/group/google-visualization-api) to get help from the Visualization developer community. The Google Visualization team also participates in this group to answer questions.
Using the API
-------------

What is the difference between the Google Chart API and the Google Visualization API?
The [Chart API](https://developers.google.com/chart) provides a simple way to create image charts of various kinds by sending a formatted URL that includes both the data and chart configuration options to a Google server. The Chart API includes a closed set of charts with various options. The Chart API datasets are limited to the size of a URL (roughly 2K).

The Visualization API provides a way to connect charts and data sources over the web and to publish them:

* The Visualization API provides a Javascript API to access charts.
* Its gallery of charts includes Google-created charts, but is also open to any third party to create their own Visualization API-compliant visualizations.
* Visualization API charts and charts can be anything that can be rendered by a browser. This includes images, Javascript, vector-graphics, Flash, etc.
* A considerable number of Chart API charts are accessible through the Visualization API, although some of their configuration options may not be available.
* The API also provides a documented wire protocol and a way for anyone to expose their data sources to any of the APIs visualizations.
* The API has a defined event model that allows charts to throw and receive events and thus communicate with their host page and/or other charts on the page.

What data sources can I access using the Visualization API? With the Visualization API you can access data locally from your browser by creating the API's standard DataTable format, or access any data source that supports the API. Well-known applications that already support the API are Google Spreadsheets and [Salesforce.com](http://www.salesforce.com/) on their [Force.com](http://www.salesforce.com/platform/) developer platform. You may also implement your own data as a Chart data source.My application expects the data it receives to be in a specific format. How do I handle exceptions? You can use the `getNumberOfColumns()` and `getColumnType()` methods of class [`google.visualization.DataTable`](https://developers.google.com/chart/interactive/docs/reference#DataTable) to test that the data you get matches what you expect, and issue an error message for mismatches.Is it safe to embed a chart in my web site? Running third party code directly on your web site poses inherent risks. Google makes no promises or representations about application performance, quality, security, or content. Chart applications that do not comply with the Google Visualization API [Terms of Service](https://developers.google.com/chart/terms) may be removed from the galleries.Can I use charts offline?Your users' computers must have access to https://www.gstatic.com/charts/loader.js in order to use the interactive features of Google Charts. This is because the visualization libraries that your page requires are loaded dynamically before you use them. The code for loading the appropriate library is part of the included script, and is called when you invoke the `google.charts.load()` method. Our [terms of service](https://developers.google.com/chart/terms) do not allow you to download the `google.charts.load` or `google.visualization` code to use offline.Can I download and host the chart code locally, or on an intranet?Sorry; our [terms of service](https://developers.google.com/chart/terms) do not allow you to download and save or host the `google.charts.load` or `google.visualization` code. However, if you don't need the interactivity of Google Charts, you can screenshot the charts and use them as you wish.
Troubleshooting
---------------

Why doesn't my chart appear?
First, check your JavaScript console. On Chrome, you can access the JavaScript console via Chrome->View->Developer->JavaScript Console, or Chrome->Tools->JavaScript Console. All modern browsers have a JavaScript console; you may need to poke around menus with names like "Advanced" or "Developer Tools" to find it.

Hopefully, the console leads you immediately to the problem. Sometimes, however, it'll be hard to translate the console message to the underlying cause. Here are some common pitfalls:

* You may be using the [Google Loader](https://developers.google.com/loader) incorrectly.

  * Only load the charts/loader.js **once**. No matter how many charts you have on your web page, you should have one and only one call like this: <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script> // Do this ONCE. This can be in the head or the body of your web page, depending on when you want the load to occur.
  * Ideally, call `google.charts.load` only once, with all the packages you'll need for your web page. <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>

<script>
 **google.charts.load("current", {packages: ["corechart", "timeline"]});**

 google.charts.setOnLoadCallback(drawBarChart1);
 function drawBarChart1() {
 ...
 var barChart1 = new google.visualization.BarChart(document.getElementById('chart1'));
 ...
 }

 google.charts.setOnLoadCallback(drawBarChart2);
 function drawBarChart2() {
 ...
 var barChart2 = new google.visualization.BarChart(document.getElementById('chart2'));
 ...
 }

 google.charts.setOnLoadCallback(drawTimeline);
 function drawTimeline() {
 ...
 var timeline = new google.visualization.Timeline(document.getElementById('chart3'));
 ...
 }

</script>
<div id="chart1"></div>
...
<div id="chart2"></div>
...
<div id="chart3"></div>

* Every chart should have a unique element id (e.g., `chart1`, `chart2` in the above example).
* Look for typos. Remember that JavaScript is a case-sensitive language.

If you're still stumped, search the Google Visualization API [discussion group](http://groups.google.com/group/google-visualization-api) to see if anyone had encountered a similar problem. If you can't find a post that answers your question, post your question to the group along with a link to a web page that demonstrates the problem. If possible, include a [jsfiddle](http://jsfiddle.net/).

Why are my months and days off by one? Google Charts uses JavaScript, which uses zero-based indexing. The first day of the month is 0, and the months range from 0 (January) to 11 (December). If your code assumes one-based indexing, subtract one before putting the your data into a JavaScript date object.Why do my charts work in some browsers but not all?We recommend [caniuse.com](http://caniuse.com/) for a trove of information about browser incompatibilities. With Google Charts, there are sometimes problems in Internet Explorer 8 and earlier, for two reasons: *   IE8 doesn't support SVG, so Charts fails over into VML, which is more limited.

* IE8's JavaScript doesn't allow trailing commas in lists.
Why does my Flash-based chart not show up when I'm testing it? Because of Flash security settings, Flash-based charts might not work correctly when accessed from a file location in the browser (e.g., file:///c:/webhost/myhost/myviz.html) rather than from a web server URL (e.g., http://www.myhost.com/myviz.html). This is typically a testing issue only; the issue is not a problem when you access the chart from an http:// address. You can overcome this issue as described on the [Macromedia web site](http://www.macromedia.com/support/documentation/en/flashplayer/help/settings_manager02.html). In general we recommend avoiding Flash development when possible.
Google Visualization Program Policy

-----------------------------------

What is the Google Visualization Program Policy? As described in the [Terms of Service](https://developers.google.com/chart/terms), we may decline to include and display content that violates our program policy by displaying or linking to:

* Illegal content.
* Invasions of personal privacy.
* Pornography or obscenity.
* Content, such as malicious code, that interferes with or is harmful to a user's computer or the functioning of the host web page.
* Promotions of hate or incitement of violence.
* Violations of copyright. Please see our [DMCA policy](http://www.google.com/igoogle_dmca.html) for more information.
* Violations of trademark.
* Impersonations of third parties.

Developers that create charts that collect data, agree to maintain and link to a legally adequate privacy policy. Additionally, we require developers to ensure that their chart is secure, and to maintain their application as long as it resides in the chart directory.

These policies may be revised from time to time without notice.

Is the Google Visualization API available for commercial use? Yes. For the fine print please refer to the Google Visualization API [Terms of Service](https://developers.google.com/chart/terms).Can I use the Google Visualization API to create client-side software?Currently we do not allow developers to use the Visualization API to create client-side software. You may only use the Visualization API through the interface provided. For the fine print please refer to the [Google Visualization API Terms of Service](https://developers.google.com/chart/terms).Is Google logging all my chart data?The chart data included in the HTTP request is saved in temporary logs for no longer than two weeks for internal testing and debugging purposes. Of course you should understand that if your chart appears in an image tag on a public webpage, it could be crawled.Violations of the program policies.Violations of these Program Policies can result in the disabling or removal of your chart, being blacklisted from uploading future charts, termination of your Google accounts and/or deletion of all your charts. Start by placing your chart on the [Chart Gallery](https://developers.google.com/chart/interactive/docs/gallery). You can link back to your site and provide your source code if you wish. Get involved in our [discussion group](http://groups.google.com/group/google-visualization-api) to get the community's feedback.What is the Chart Gallery? The [Chart Gallery](https://developers.google.com/chart/interactive/docs/gallery) is a listing of applications that use the Visualization API. It provides a central location for the Visualization developer community to share Chart applications. To submit your chart application to the gallery, [apply online](https://developers.google.com/chart/interactive/docs/submit).How can I promote my Chart data source?Post your implementation on the Visualization Group. If we like it, we might even mention it ourselves.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-07-10 UTC.
