# Source: https://selenium.dev/documentation/webdriver/bidi/w3c/browsing_context/

Title: Browsing Context

URL Source: https://selenium.dev/documentation/webdriver/bidi/w3c/browsing_context/

Markdown Content:
About
Downloads
Documentation
Projects
Support
Blog
English
Search
K
Registrations Open for SeleniumConf 2026 | May 06–08 | Join Us In-Person! Register now!
Documentation
Overview
WebDriver
Getting Started
Drivers
Browsers
Waits
Elements
Interactions
Actions API
BiDi
Logging
Network
Script
CDP
W3C
Browsing Context
Input
Log
Network
Script
Support Features
Troubleshooting
Selenium Manager
Grid
IE Driver Server
IDE
Test Practices
Legacy
About
 Edit this page
 Create documentation issue
 Create project issue
 Print entire section
Commands
Open a new window
Open a new tab
Use existing window handle
Open a window with a reference browsing context
Open a tab with a reference browsing context
Navigate to a URL
Navigate to a URL with readiness state
Get browsing context tree
Get browsing context tree with depth
Get All Top level browsing contexts
Close a tab/window
Activate a browsing context
Reload a browsing context
Handle user prompt
Capture Screenshot
Capture Viewport Screenshot
Capture Element Screenshot
Set Viewport
Print page
Navigate back
Navigate forward
Traverse history
Events
Browsing Context Created Event
Dom Content loaded Event
Browsing Context Loaded Event
Navigated Started Event
Fragment Navigated Event
User Prompt Opened Event
User Prompt Closed Event
Browsing Context Destroyed Event
Documentation
WebDriver
BiDi
W3C
Browsing Context
v4.0
Browsing Context
Commands

This section contains the APIs related to browsing context commands.

Open a new window

Creates a new browsing context in a new window.

Java
Ruby
JavaScript
Kotlin

Selenium v4.8

        Assertions.assertEquals(id, browsingContext.getId());
    }

    @Test
View Complete Code
View on GitHub
Open a new tab

Creates a new browsing context in a new tab.

Java
Ruby
JavaScript
Kotlin

Selenium v4.8


    @Test
    void testNavigateToAUrl() {
        BrowsingContext browsingContext = new BrowsingContext(driver, WindowType.TAB);
View Complete Code
View on GitHub
Use existing window handle

Creates a browsing context for the existing tab/window to run commands.

Java
Ruby
JavaScript
Kotlin

Selenium v4.8

        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    }

    @Test
    void testCreateABrowsingContextForGivenId() {
View Complete Code
View on GitHub
Open a window with a reference browsing context

A reference browsing context is a top-level browsing context. The API allows to pass the reference browsing context, which is used to create a new window. The implementation is operating system specific.

Java
Ruby
JavaScript
Kotlin

Selenium v4.8

        Assertions.assertNotNull(browsingContext.getId());
    }

    @Test
    void testCreateATab() {
        BrowsingContext browsingContext = new BrowsingContext(driver, WindowType.TAB);
View Complete Code
View on GitHub
Open a tab with a reference browsing context

A reference browsing context is a top-level browsing context. The API allows to pass the reference browsing context, which is used to create a new tab. The implementation is operating system specific.

Java
Ruby
JavaScript
Kotlin

Selenium v4.8


        Assertions.assertNotNull(browsingContext.getId());
        Assertions.assertNotNull(info.getNavigationId());
        Assertions.assertTrue(info.getUrl().contains("/bidi/logEntryAdded.html"));
    }

View Complete Code
View on GitHub
Navigate to a URL
Java
Ruby
JavaScript
Kotlin

Selenium v4.8

        BrowsingContext browsingContext = new BrowsingContext(driver, WindowType.TAB);

        NavigationResult info = browsingContext.navigate("https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html",
                ReadinessState.COMPLETE);

        Assertions.assertNotNull(browsingContext.getId());
        Assertions.assertNotNull(info.getNavigationId());
        Assertions.assertTrue(info.getUrl().contains("/bidi/logEntryAdded.html"));
    }
View Complete Code
View on GitHub
Navigate to a URL with readiness state
Java
Ruby
JavaScript
Kotlin

Selenium v4.8

    void testGetTreeWithAChild() {
        String referenceContextId = driver.getWindowHandle();
        BrowsingContext parentWindow = new BrowsingContext(driver, referenceContextId);

        parentWindow.navigate("https://www.selenium.dev/selenium/web/iframes.html", ReadinessState.COMPLETE);

        List<BrowsingContextInfo> contextInfoList = parentWindow.getTree();

        Assertions.assertEquals(1, contextInfoList.size());
        BrowsingContextInfo info = contextInfoList.get(0);
View Complete Code
View on GitHub
Get browsing context tree

Provides a tree of all browsing contexts descending from the parent browsing context, including the parent browsing context.

Java
Ruby
JavaScript
Kotlin

Selenium v4.8

        Assertions.assertTrue(info.getChildren().get(0).getUrl().contains("formPage.html"));
    }

    @Test
    void testGetTreeWithDepth() {
        String referenceContextId = driver.getWindowHandle();
        BrowsingContext parentWindow = new BrowsingContext(driver, referenceContextId);

        parentWindow.navigate("https://www.selenium.dev/selenium/web/iframes.html", ReadinessState.COMPLETE);

        List<BrowsingContextInfo> contextInfoList = parentWindow.getTree(0);

        Assertions.assertEquals(1, contextInfoList.size());
        BrowsingContextInfo info = contextInfoList.get(0);
View Complete Code
View on GitHub
Get browsing context tree with depth

Provides a tree of all browsing contexts descending from the parent browsing context, including the parent browsing context upto the depth value passed.

Java
Ruby
JavaScript
Kotlin

Selenium v4.8

    }

    @Test
    void testGetAllTopLevelContexts() {
        BrowsingContext window1 = new BrowsingContext(driver, driver.getWindowHandle());
        BrowsingContext window2 = new BrowsingContext(driver, WindowType.WINDOW);

        List<BrowsingContextInfo> contextInfoList = window1.getTopLevelContexts();

        Assertions.assertEquals(2, contextInfoList.size());
    }

    @Test
View Complete Code
View on GitHub
Get All Top level browsing contexts
Java
Ruby
JavaScript
Kotlin

Selenium v4.8

        BrowsingContext window2 = new BrowsingContext(driver, WindowType.WINDOW);

        window2.close();

        Assertions.assertThrows(BiDiException.class, window2::getTree);
    }

    @Test
View Complete Code
View on GitHub
Close a tab/window
Java
Ruby
JavaScript
Kotlin

Selenium v4.8

        BrowsingContext tab2 = new BrowsingContext(driver, WindowType.TAB);

        tab2.close();

        Assertions.assertThrows(BiDiException.class, tab2::getTree);
    }

    @Test
    void testActivateABrowsingContext() {
        BrowsingContext window1 = new BrowsingContext(driver, driver.getWindowHandle());
        BrowsingContext window2 = new BrowsingContext(driver, WindowType.WINDOW);

        window1.activate();

        boolean isFocused = (boolean) ((JavascriptExecutor) driver).executeScript("return document.hasFocus();");

        Assertions.assertTrue(isFocused);
    }
View Complete Code
View on GitHub
Activate a browsing context
Java
Ruby
JavaScript
Kotlin

Selenium v4.14.1

        BrowsingContext browsingContext = new BrowsingContext(driver, WindowType.TAB);

        browsingContext.navigate("https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html", ReadinessState.COMPLETE);

        NavigationResult reloadInfo = browsingContext.reload(ReadinessState.INTERACTIVE);
View Complete Code
View on GitHub
Reload a browsing context
Java
Ruby
JavaScript
Kotlin

Selenium v4.13.0

        BrowsingContext browsingContext = new BrowsingContext(driver, driver.getWindowHandle());

        driver.get("https://www.selenium.dev/selenium/web/alerts.html");

        driver.findElement(By.id("alert")).click();
View Complete Code
View on GitHub
Handle user prompt
Java
Ruby
JavaScript
Kotlin

Selenium v4.13.0

    @Test
    void testDismissUserPromptWithText() {
        BrowsingContext browsingContext = new BrowsingContext(driver, driver.getWindowHandle());

        driver.get("https://www.selenium.dev/selenium/web/alerts.html");

        driver.findElement(By.id("prompt-with-default")).click();

        String userText = "Selenium automates browsers";
View Complete Code
View on GitHub
Capture Screenshot
Java
Ruby
JavaScript
Kotlin

Selenium v4.13.0


        driver.get("https://www.selenium.dev/selenium/web/coordinates_tests/simple_page.html");

        WebElement element = driver.findElement(By.id("box"));
        Rectangle elementRectangle = element.getRect();
View Complete Code
View on GitHub
Capture Viewport Screenshot
Java
Ruby
JavaScript
Kotlin

Selenium v4.14.0

    }

    @Test
    void textCaptureElementScreenshot() {
        BrowsingContext browsingContext = new BrowsingContext(driver, driver.getWindowHandle());

        driver.get("https://www.selenium.dev/selenium/web/formPage.html");
        WebElement element = driver.findElement(By.id("checky"));

        String screenshot = browsingContext.captureElementScreenshot(((RemoteWebElement) element).getId());
View Complete Code
View on GitHub
Capture Element Screenshot
Java
Ruby
JavaScript
Kotlin

Selenium v4.14.0

        BrowsingContext browsingContext = new BrowsingContext(driver, driver.getWindowHandle());
        driver.get("https://www.selenium.dev/selenium/web/formPage.html");

        browsingContext.setViewport(250, 300);

        List<Long> newViewportSize =
View Complete Code
View on GitHub
Set Viewport
Java
Ruby
JavaScript
Kotlin

Selenium v4.14.1

        BrowsingContext browsingContext = new BrowsingContext(driver, driver.getWindowHandle());

        driver.get("https://www.selenium.dev/selenium/web/formPage.html");
        PrintOptions printOptions = new PrintOptions();
View Complete Code
View on GitHub
Print page
Java
Ruby
JavaScript
Kotlin

Selenium v4.14.1

        browsingContext.navigate("https://www.selenium.dev/selenium/web/formPage.html", ReadinessState.COMPLETE);

        wait.until(visibilityOfElementLocated(By.id("imageButton"))).submit();
        wait.until(titleIs("We Arrive Here"));

        browsingContext.back();
View Complete Code
View on GitHub
Navigate back
Java
Ruby
JavaScript
Kotlin

Selenium v4.16.0


        wait.until(visibilityOfElementLocated(By.id("imageButton"))).submit();
        wait.until(titleIs("We Arrive Here"));

        browsingContext.back();
        Assertions.assertTrue(driver.getPageSource().contains("We Leave From Here"));

View Complete Code
View on GitHub
Navigate forward
Java
Ruby
JavaScript
Kotlin

Selenium v4.16.0

    void canTraverseBrowserHistory() {
        BrowsingContext browsingContext = new BrowsingContext(driver, driver.getWindowHandle());
        browsingContext.navigate("https://www.selenium.dev/selenium/web/formPage.html", ReadinessState.COMPLETE);

        wait.until(visibilityOfElementLocated(By.id("imageButton"))).submit();
        wait.until(titleIs("We Arrive Here"));

        browsingContext.traverseHistory(-1);
        Assertions.assertTrue(driver.getPageSource().contains("We Leave From Here"));
    }
}
View Complete Code
View on GitHub
Traverse history
Java
Ruby
JavaScript
Kotlin

Selenium v4.16.0

View Complete Code
View on GitHub
Events

This section contains the APIs related to browsing context events.

Browsing Context Created Event
Java
Ruby
JavaScript
Kotlin

Selenium v4.10

    try (BrowsingContextInspector inspector = new BrowsingContextInspector(driver)) {
        CompletableFuture<BrowsingContextInfo> future = new CompletableFuture<>();

        inspector.onBrowsingContextCreated(future::complete);

        String windowHandle = driver.switchTo().newWindow(WindowType.WINDOW).getWindowHandle();

        BrowsingContextInfo browsingContextInfo = future.get(5, TimeUnit.SECONDS);
View Complete Code
View on GitHub
Dom Content loaded Event
Java
Ruby
JavaScript
Kotlin

Selenium v4.10

            String windowHandle = driver.switchTo().newWindow(WindowType.TAB).getWindowHandle();

            BrowsingContextInfo browsingContextInfo = future.get(5, TimeUnit.SECONDS);

            Assertions.assertEquals(windowHandle, browsingContextInfo.getId());
        }
    }

    @Test
    void canListenToDomContentLoadedEvent()
View Complete Code
View on GitHub
Browsing Context Loaded Event
Java
Ruby
JavaScript
Kotlin

Selenium v4.10

        try (BrowsingContextInspector inspector = new BrowsingContextInspector(driver)) {
            CompletableFuture<NavigationInfo> future = new CompletableFuture<>();
            inspector.onBrowsingContextLoaded(future::complete);

            BrowsingContext context = new BrowsingContext(driver, driver.getWindowHandle());
            context.navigate("https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html", ReadinessState.COMPLETE);

            NavigationInfo navigationInfo = future.get(5, TimeUnit.SECONDS);
View Complete Code
View on GitHub
Navigated Started Event
Java
Ruby
JavaScript
Kotlin

Selenium v4.15

        try (BrowsingContextInspector inspector = new BrowsingContextInspector(driver)) {
            CompletableFuture<NavigationInfo> future = new CompletableFuture<>();
            inspector.onNavigationStarted(future::complete);

            BrowsingContext context = new BrowsingContext(driver, driver.getWindowHandle());
            context.navigate("https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html", ReadinessState.COMPLETE);

            NavigationInfo navigationInfo = future.get(5, TimeUnit.SECONDS);
View Complete Code
View on GitHub
Fragment Navigated Event
Java
Ruby
JavaScript
Kotlin

Selenium v4.15

        try (BrowsingContextInspector inspector = new BrowsingContextInspector(driver)) {
            CompletableFuture<NavigationInfo> future = new CompletableFuture<>();

            BrowsingContext context = new BrowsingContext(driver, driver.getWindowHandle());
            context.navigate("https://www.selenium.dev/selenium/web/linked_image.html", ReadinessState.COMPLETE);

            inspector.onFragmentNavigated(future::complete);

            context.navigate("https://www.selenium.dev/selenium/web/linked_image.html#linkToAnchorOnThisPage", ReadinessState.COMPLETE);

            NavigationInfo navigationInfo = future.get(5, TimeUnit.SECONDS);
View Complete Code
View on GitHub
User Prompt Opened Event
Java
Ruby
JavaScript
Kotlin

Selenium v4.15

        try (BrowsingContextInspector inspector = new BrowsingContextInspector(driver)) {
            CompletableFuture<NavigationInfo> future = new CompletableFuture<>();

            BrowsingContext context = new BrowsingContext(driver, driver.getWindowHandle());
            context.navigate("https://www.selenium.dev/selenium/web/linked_image.html", ReadinessState.COMPLETE);

            inspector.onFragmentNavigated(future::complete);

            context.navigate("https://www.selenium.dev/selenium/web/linked_image.html#linkToAnchorOnThisPage", ReadinessState.COMPLETE);

            NavigationInfo navigationInfo = future.get(5, TimeUnit.SECONDS);
View Complete Code
View on GitHub
User Prompt Closed Event
Java
Ruby
JavaScript
Kotlin

Selenium v4.15

        try (BrowsingContextInspector inspector = new BrowsingContextInspector(driver)) {
            CompletableFuture<UserPromptClosed> future = new CompletableFuture<>();

            BrowsingContext context = new BrowsingContext(driver, driver.getWindowHandle());
            inspector.onUserPromptClosed(future::complete);

            driver.get("https://www.selenium.dev/selenium/web/alerts.html");

            driver.findElement(By.id("prompt")).click();

            context.handleUserPrompt(true, "selenium");

            UserPromptClosed userPromptClosed = future.get(5, TimeUnit.SECONDS);
            Assertions.assertEquals(context.getId(), userPromptClosed.getBrowsingContextId());
View Complete Code
View on GitHub
Browsing Context Destroyed Event
Java
Ruby
JavaScript
Kotlin

Selenium v4.18

        try (BrowsingContextInspector inspector = new BrowsingContextInspector(driver)) {
            CompletableFuture<BrowsingContextInfo> future = new CompletableFuture<>();

            inspector.onBrowsingContextDestroyed(future::complete);

            String windowHandle = driver.switchTo().newWindow(WindowType.WINDOW).getWindowHandle();

            driver.close();

            BrowsingContextInfo browsingContextInfo = future.get(5, TimeUnit.SECONDS);

            Assertions.assertEquals(windowHandle, browsingContextInfo.getId());
View Complete Code
View on GitHub
Last modified August 4, 2024: refactor(js): update code samples to use mocha and fix line numbers (d4adebb67ba)
Development Partners
Selenium Level Sponsors
Support the Selenium Project

Learn more or view the full list of sponsors.

LEARN MORE 
© 2026 Software Freedom Conservancy All Rights Reserved

About Selenium
