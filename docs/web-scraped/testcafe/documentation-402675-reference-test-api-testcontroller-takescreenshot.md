# Source: https://testcafe.io/documentation/402675/reference/test-api/testcontroller/takescreenshot

Title: .takeScreenshot() | TestController | Test API | API

URL Source: https://testcafe.io/documentation/402675/reference/test-api/testcontroller/takescreenshot

Markdown Content:
.takeScreenshot() | TestController | Test API | API
===============

[](https://testcafe.io/)[](https://testcafe.io/)
*   [Studio](https://www.devexpress.com/products/testcafestudio/)

*   [Guides](https://testcafe.io/documentation/402635/guides/overview/getting-started)
*   [API](https://testcafe.io/documentation/402632/api)
*   [Recipes](https://testcafe.io/documentation/402633/recipes)
*   [Examples](https://testcafe.io/documentation/402637/examples)
*   [FAQ](https://testcafe.io/documentation/402636/faq/general-info)
*   [What's New 2](https://testcafe.io/release-notes)

*   [Support](https://testcafe.io/support)

Search K

[](https://github.com/DevExpress/testcafe)

[Star](https://github.com/DevExpress/testcafe)[9,908](https://github.com/DevExpress/testcafe/stargazers)

API

*   [Command Line Interface](https://testcafe.io/documentation/402639/reference/command-line-interface) 
*   [Configuration File](https://testcafe.io/documentation/402638/reference/configuration-file) 
*   Test API
    *   [Test Object](https://testcafe.io/documentation/403366/reference/test-api/test) 
    *   [ClientFunction Object](https://testcafe.io/documentation/402671/reference/test-api/clientfunction) 
    *   [DOMNodeState Object](https://testcafe.io/documentation/402670/reference/test-api/domnodestate) 
    *   [RequestHook Class](https://testcafe.io/documentation/402669/reference/test-api/requesthook) 
    *   [Fixture Class](https://testcafe.io/documentation/403367/reference/test-api/fixture) 
    *   Global Functions 
    *   [RequestLogger Class](https://testcafe.io/documentation/402668/reference/test-api/requestlogger) 
    *   [RequestMock Class](https://testcafe.io/documentation/402667/reference/test-api/requestmock) 
    *   [Selector Object](https://testcafe.io/documentation/402666/reference/test-api/selector) 
    *   [TestController](https://testcafe.io/documentation/402665/reference/test-api/testcontroller) 
        *   [.addRequestHooks()](https://testcafe.io/documentation/402713/reference/test-api/testcontroller/addrequesthooks)
        *   [.browser](https://testcafe.io/documentation/402712/reference/test-api/testcontroller/browser)
        *   [.clearUpload()](https://testcafe.io/documentation/402711/reference/test-api/testcontroller/clearupload)
        *   [.click()](https://testcafe.io/documentation/402710/reference/test-api/testcontroller/click)
        *   [.closeWindow()](https://testcafe.io/documentation/402709/reference/test-api/testcontroller/closewindow)
        *   [.ctx](https://testcafe.io/documentation/402708/reference/test-api/testcontroller/ctx)
        *   [.debug()](https://testcafe.io/documentation/402707/reference/test-api/testcontroller/debug)
        *   [.deleteCookies()](https://testcafe.io/documentation/403874/reference/test-api/testcontroller/deletecookies)
        *   [.dispatchEvent()](https://testcafe.io/documentation/403091/reference/test-api/testcontroller/dispatchevent)
        *   [.doubleClick()](https://testcafe.io/documentation/402706/reference/test-api/testcontroller/doubleclick)
        *   [.drag()](https://testcafe.io/documentation/402705/reference/test-api/testcontroller/drag)
        *   [.dragToElement()](https://testcafe.io/documentation/402704/reference/test-api/testcontroller/dragtoelement)
        *   [.eval()](https://testcafe.io/documentation/402703/reference/test-api/testcontroller/eval)
        *   [.expect()](https://testcafe.io/documentation/402702/reference/test-api/testcontroller/expect)
        *   [.expect.contains()](https://testcafe.io/documentation/402729/reference/test-api/testcontroller/expect/contains)
        *   [.expect.eql()](https://testcafe.io/documentation/402728/reference/test-api/testcontroller/expect/eql)
        *   [.expect.gt()](https://testcafe.io/documentation/402727/reference/test-api/testcontroller/expect/gt)
        *   [.expect.gte()](https://testcafe.io/documentation/402726/reference/test-api/testcontroller/expect/gte)
        *   [.expect.lt()](https://testcafe.io/documentation/402725/reference/test-api/testcontroller/expect/lt)
        *   [.expect.lte()](https://testcafe.io/documentation/402724/reference/test-api/testcontroller/expect/lte)
        *   [.expect.match()](https://testcafe.io/documentation/402723/reference/test-api/testcontroller/expect/match)
        *   [.expect.notContains()](https://testcafe.io/documentation/402722/reference/test-api/testcontroller/expect/notcontains)
        *   [.expect.notEql()](https://testcafe.io/documentation/402721/reference/test-api/testcontroller/expect/noteql)
        *   [.expect.notMatch()](https://testcafe.io/documentation/402720/reference/test-api/testcontroller/expect/notmatch)
        *   [.expect.notOk()](https://testcafe.io/documentation/402719/reference/test-api/testcontroller/expect/notok)
        *   [.expect.notTypeOf()](https://testcafe.io/documentation/402718/reference/test-api/testcontroller/expect/nottypeof)
        *   [.expect.notWithin()](https://testcafe.io/documentation/402717/reference/test-api/testcontroller/expect/notwithin)
        *   [.expect.ok()](https://testcafe.io/documentation/402716/reference/test-api/testcontroller/expect/ok)
        *   [.expect.typeOf()](https://testcafe.io/documentation/402715/reference/test-api/testcontroller/expect/typeof)
        *   [.expect.within()](https://testcafe.io/documentation/402714/reference/test-api/testcontroller/expect/within)
        *   [.fixture](https://testcafe.io/documentation/404445/reference/test-api/testcontroller/fixture)
        *   [.fixtureCtx](https://testcafe.io/documentation/402701/reference/test-api/testcontroller/fixturectx)
        *   [.getBrowserConsoleMessages()](https://testcafe.io/documentation/402700/reference/test-api/testcontroller/getbrowserconsolemessages)
        *   [.getCookies()](https://testcafe.io/documentation/403873/reference/test-api/testcontroller/getcookies)
        *   [.getCurrentWindow()](https://testcafe.io/documentation/402699/reference/test-api/testcontroller/getcurrentwindow)
        *   [.getCurrentCDPSession()](https://testcafe.io/documentation/404913/reference/test-api/testcontroller/getcurrentcdpsession)
        *   [.getNativeDialogHistory()](https://testcafe.io/documentation/402698/reference/test-api/testcontroller/getnativedialoghistory)
        *   [.hover()](https://testcafe.io/documentation/402697/reference/test-api/testcontroller/hover)
        *   [.maximizeWindow()](https://testcafe.io/documentation/402696/reference/test-api/testcontroller/maximizewindow)
        *   [.navigateTo()](https://testcafe.io/documentation/402695/reference/test-api/testcontroller/navigateto)
        *   [.openWindow()](https://testcafe.io/documentation/402694/reference/test-api/testcontroller/openwindow)
        *   [.pressKey()](https://testcafe.io/documentation/402693/reference/test-api/testcontroller/presskey)
        *   [.removeRequestHooks()](https://testcafe.io/documentation/402692/reference/test-api/testcontroller/removerequesthooks)
        *   [.request()](https://testcafe.io/documentation/403981/reference/test-api/testcontroller/request)
        *   [.resizeWindow()](https://testcafe.io/documentation/402691/reference/test-api/testcontroller/resizewindow)
        *   [.resizeWindowToFitDevice()](https://testcafe.io/documentation/402690/reference/test-api/testcontroller/resizewindowtofitdevice)
        *   [.rightClick()](https://testcafe.io/documentation/402689/reference/test-api/testcontroller/rightclick)
        *   [.scroll()](https://testcafe.io/documentation/403065/reference/test-api/testcontroller/scroll)
        *   [.scrollBy()](https://testcafe.io/documentation/403066/reference/test-api/testcontroller/scrollby)
        *   [.scrollIntoView()](https://testcafe.io/documentation/403067/reference/test-api/testcontroller/scrollintoview)
        *   [.selectEditableContent()](https://testcafe.io/documentation/402688/reference/test-api/testcontroller/selecteditablecontent)
        *   [.selectText()](https://testcafe.io/documentation/402687/reference/test-api/testcontroller/selecttext)
        *   [.selectTextAreaContent()](https://testcafe.io/documentation/402686/reference/test-api/testcontroller/selecttextareacontent)
        *   [.setCookies()](https://testcafe.io/documentation/403872/reference/test-api/testcontroller/setcookies)
        *   [.setFilesToUpload()](https://testcafe.io/documentation/402685/reference/test-api/testcontroller/setfilestoupload)
        *   [.setNativeDialogHandler()](https://testcafe.io/documentation/402684/reference/test-api/testcontroller/setnativedialoghandler)
        *   [.setPageLoadTimeout()](https://testcafe.io/documentation/402683/reference/test-api/testcontroller/setpageloadtimeout)
        *   [.setTestSpeed()](https://testcafe.io/documentation/402682/reference/test-api/testcontroller/settestspeed)
        *   [.skipJsErrors()](https://testcafe.io/documentation/404027/reference/test-api/testcontroller/skipjserrors)
        *   [.switchToIframe()](https://testcafe.io/documentation/402681/reference/test-api/testcontroller/switchtoiframe)
        *   [.switchToMainWindow()](https://testcafe.io/documentation/402680/reference/test-api/testcontroller/switchtomainwindow)
        *   [.switchToParentWindow()](https://testcafe.io/documentation/402679/reference/test-api/testcontroller/switchtoparentwindow)
        *   [.switchToPreviousWindow()](https://testcafe.io/documentation/402678/reference/test-api/testcontroller/switchtopreviouswindow)
        *   [.switchToWindow()](https://testcafe.io/documentation/402677/reference/test-api/testcontroller/switchtowindow)
        *   [.takeElementScreenshot()](https://testcafe.io/documentation/402676/reference/test-api/testcontroller/takeelementscreenshot)
        *   [.takeScreenshot()](https://testcafe.io/documentation/402675/reference/test-api/testcontroller/takescreenshot)
        *   [.test](https://testcafe.io/documentation/404444/reference/test-api/testcontroller/test)
        *   [.typeText()](https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext)
        *   [.useRole()](https://testcafe.io/documentation/402673/reference/test-api/testcontroller/userole)
        *   [.wait()](https://testcafe.io/documentation/402672/reference/test-api/testcontroller/wait)
        *   [.report()](https://testcafe.io/documentation/404350/reference/test-api/testcontroller/report)

*   TestCafe API
    *   [BrowserConnection Object](https://testcafe.io/documentation/402643/reference/testcafe-api/browserconnection) 
    *   [LiveModeRunner Object](https://testcafe.io/documentation/402642/reference/testcafe-api/livemoderunner) 
    *   [Runner Object](https://testcafe.io/documentation/402641/reference/testcafe-api/runner) 
    *   [TestCafe Object](https://testcafe.io/documentation/402640/reference/testcafe-api/testcafe) 
    *   Global 

*   Plugin API
    *   [BrowserProvider Interface](https://testcafe.io/documentation/402791/reference/plugin-api/browserprovider) 
    *   [Reporter Interface](https://testcafe.io/documentation/402790/reference/plugin-api/reporter) 

*   [Version Logger API](https://testcafe.io/documentation/404469/reference/version-logger-api) 

[API](https://testcafe.io/documentation/402632/api)→[TestController](https://testcafe.io/documentation/402665/reference/test-api/testcontroller)→.takeScreenshot()

t.takeScreenshot Method
=======================

Takes screenshot of the entire page. [Chainable](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#action-chaining).

```plaintext
t.takeScreenshot([options]) → this | Promise<any>
deprecated: t.takeScreenshot([path]) → this | Promise<any>
```

The `options` object can include the following properties:

| Parameter | Type | Description | Default Value |
| --- | --- | --- | --- |
| `path`_(optional)_ | String | **Relative** path to the screenshot file. Use the [runner.screenshots](https://testcafe.io/documentation/402654/reference/testcafe-api/runner/screenshots) method or the [-s (--screenshots)](https://testcafe.io/documentation/402639/reference/command-line-interface#-s---screenshots-optionvalueoption2value2) CLI option to set the root directory. Overrides screenshot [path patterns](https://testcafe.io/documentation/402840/guides/intermediate-guides/screenshots-and-videos#screenshot-and-video-storage-configuration). |  |
| `pathPattern`_(optional)_ | String | Defines a custom naming pattern for the screenshot file. See [Screenshot and Video Storage Configuration](https://testcafe.io/documentation/402840/guides/intermediate-guides/screenshots-and-videos#screenshot-and-video-storage-configuration). |  |
| `fullPage`_(optional)_ | Boolean | Enable `fullPage` to capture the entire page, including the area outside the viewport. | `false` |

Important

_t.takeScreenshot_ requires .NET v4.0 or higher on Windows machines and an [ICCCM/EWMH-compliant window manager](https://en.wikipedia.org/wiki/Comparison_of_X_window_managers) on Linux.

The following example shows how to use the `t.takeScreenshot` action.

```js
fixture`TestController.takeScreenshot`
    .page`https://devexpress.github.io/testcafe/example/`;

test('Take a screenshot of a fieldset', async t => {
    await t
        .typeText('#developer-name', 'Peter Parker')
        .click('#submit-button')
        .takeScreenshot({
            path:     'my-fixture/thank-you-page.png',
            fullPage: true,
        });
});
```

To take a screenshot of a specific element, use the [t.takeElementScreenshot](https://testcafe.io/documentation/402676/reference/test-api/testcontroller/takeelementscreenshot) method.

See [Screenshots and Videos](https://testcafe.io/documentation/402840/guides/intermediate-guides/screenshots-and-videos) for more information on taking screenshots.

![Image 1: TestCafe](https://testcafe.io/img/testcafe-logo.svg)
TestCafe is a user-friendly end-to-end testing framework. Free and open source test runner. Powerful desktop app. Enterprise-quality web services.

[Facebook](https://www.facebook.com/dxtestcafe/)[Twitter](https://twitter.com/DXTestCafe)[GitHub](https://github.com/DevExpress/testcafe)[Email](mailto:testcafeteam@devexpress.com)[Youtube](https://www.youtube.com/playlist?list=PL8h4jt35t1wirqPiT68hV0cpX1ppQMVtF)

Footer navigation
-----------------

### Product

*   [Why TestCafe](https://testcafe.io/documentation/402631/guides/overview/why-testcafe)
*   [Getting Started](https://testcafe.io/documentation/402635/guides/overview/getting-started)
*   [TestCafe Studio](https://www.devexpress.com/products/testcafestudio/)
*   [Integrations](https://testcafe.io/documentation/402809/guides/continuous-integration)
*   [What's New](https://testcafe.io/release-notes)
*   [Roadmap](https://testcafe.io/402949/roadmap)

### Features

*   [Cross-browser tests](https://testcafe.io/documentation/402828/guides/concepts/browsers)
*   [API tests](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing)
*   [Multi-window tests](https://testcafe.io/documentation/402841/guides/intermediate-guides/multiple-browser-windows)
*   [Iframe tests](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#work-with-iframes)
*   [Live Mode](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#live-mode)
*   [Unstable test detection](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#quarantine-mode)
*   [Screenshots and Videos](https://testcafe.io/documentation/402840/guides/intermediate-guides/screenshots-and-videos)
*   [Concurrent test runs](https://testcafe.io/documentation/403626/guides/intermediate-guides/run-tests-concurrently)
*   [TypeScript tests](https://testcafe.io/documentation/402824/guides/concepts/typescript-and-coffeescript)

### Resources

*   [Blog](https://testcafe.io/resources/team-blog)
*   [Community Blogs](https://testcafe.io/resources/community-blogs)
*   [Courses](https://testcafe.io/resources/courses)
*   [Books](https://testcafe.io/resources/books)
*   [Case studies](https://testcafe.io/case-studies)

### Learn

*   [Docs](https://testcafe.io/documentation/402635/guides/overview/getting-started)
*   [FAQ](https://testcafe.io/documentation/402636/faq/general-info)
*   [Guides](https://testcafe.io/documentation/402634/guides)
*   [Best Practices](https://testcafe.io/documentation/402836/guides/basic-guides/best-practices)
*   [Examples](https://testcafe.io/documentation/402637/examples)

### Support

*   [Report an Issue](https://github.com/DevExpress/testcafe/issues/new?assignees=&labels=TYPE%3A+bug&template=bug_report.yaml)
*   [Suggest a Feature](https://github.com/DevExpress/testcafe/issues/new?assignees=&labels=TYPE%3A+enhancement&template=feature_request.yaml)
*   [Ask on StackOverflow](https://stackoverflow.com/questions/ask?tags=testcafe)

© 2012–2023 Developer Express Inc. Use of this site constitutes acceptance of our [Privacy Policy.](https://www.devexpress.com/aboutus/privacy-policy.xml)

All trademarks or registered trademarks are property of their respective owners.

Why We Use Cookies

This site uses cookies to make your browsing experience more convenient and personal. Cookies store useful information on your computer to help us improve the efficiency and relevance of our site for you. In some cases, they are essential to making the site work properly. By accessing this site, you consent to the use of cookies. For more information, refer to DevExpress [privacy policy](https://www.devexpress.com/aboutus/privacy-policy.xml) and[cookie policy](https://www.devexpress.com/AboutUs/cookie-policy.xml).

I understand
