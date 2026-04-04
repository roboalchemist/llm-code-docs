# Source: https://selenium.dev/documentation/webdriver/bidi/w3c/script/

Title: Script

URL Source: https://selenium.dev/documentation/webdriver/bidi/w3c/script/

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
Call function in a browsing context
Call function in a sandbox
Call function in a realm
Evaluate script in a browsing context
Evaluate script in a sandbox
Evaluate script in a realm
Disown handles in a browsing context
Disown handles in a realm
Get all realms
Get realm by type
Get browsing context realms
Get browsing context realms by type
Preload a script
Remove a preloaded script
Events
Message
Realm Created
Realm Destroyed
Documentation
WebDriver
BiDi
W3C
Script
v4.0
Script
Commands

This section contains the APIs related to script commands.

Call function in a browsing context
Java
Ruby
JavaScript
Kotlin

Selenium v4.15

        try (Script script = new Script(id, driver)) {
            List<LocalValue> arguments = new ArrayList<>();
            arguments.add(PrimitiveProtocolValue.numberValue(22));

            Map<Object, LocalValue> value = new HashMap<>();
            value.put("some_property", LocalValue.numberValue(42));
            LocalValue thisParameter = LocalValue.objectValue(value);

            arguments.add(thisParameter);

            EvaluateResult result =
                    script.callFunctionInBrowsingContext(
                            id,
                            "function processWithPromise(argument) {\n"
                                    + "  return new Promise((resolve, reject) => {\n"
                                    + "    setTimeout(() => {\n"
                                    + "      resolve(argument + this.some_property);\n"
                                    + "    }, 1000)\n"
                                    + "  })\n"
                                    + "}",
                            true,
                            Optional.of(arguments),
                            Optional.of(thisParameter),
                            Optional.of(ResultOwnership.ROOT));
View Complete Code
View on GitHub
Call function in a sandbox
Java
Ruby
JavaScript
Kotlin

Selenium v4.15

        try (Script script = new Script(id, driver)) {
            EvaluateResult result =
                    script.callFunctionInBrowsingContext(
                            id,
                            "sandbox",
                            "() => window.foo",
                            true,
                            Optional.empty(),
                            Optional.empty(),
                            Optional.empty());
View Complete Code
View on GitHub
Call function in a realm
Java
Ruby
JavaScript
Kotlin

Selenium v4.15

        try (Script script = new Script(tab, driver)) {
            List<RealmInfo> realms = script.getAllRealms();
            String realmId = realms.get(0).getRealmId();

            EvaluateResult result = script.callFunctionInRealm(
                    realmId,
                    "() => { window.foo = 3; }",
                    true,
                    Optional.empty(),
                    Optional.empty(),
                    Optional.empty());
View Complete Code
View on GitHub
Evaluate script in a browsing context
Java
Ruby
JavaScript
Kotlin

Selenium v4.15

        try (Script script = new Script(id, driver)) {
            EvaluateResult result =
                    script.evaluateFunctionInBrowsingContext(id, "1 + 2", true, Optional.empty());

View Complete Code
View on GitHub
Evaluate script in a sandbox
Java
Ruby
JavaScript
Kotlin

Selenium v4.15

        try (Script script = new Script(id, driver)) {
            EvaluateResult result =
                    script.evaluateFunctionInBrowsingContext(
                            id, "sandbox", "window.foo", true, Optional.empty());
View Complete Code
View on GitHub
Evaluate script in a realm
Java
Ruby
JavaScript
Kotlin

Selenium v4.15

        try (Script script = new Script(tab, driver)) {
            List<RealmInfo> realms = script.getAllRealms();
            String realmId = realms.get(0).getRealmId();

            EvaluateResult result =
                    script.evaluateFunctionInRealm(
                            realmId, "window.foo", true, Optional.empty());
View Complete Code
View on GitHub
Disown handles in a browsing context
Java
Ruby
JavaScript
Kotlin

Selenium v4.15

            script.disownBrowsingContextScript(
View Complete Code
View on GitHub
Disown handles in a realm
Java
Ruby
JavaScript
Kotlin

Selenium v4.15

            script.disownRealmScript(realmId, List.of(boxId));
View Complete Code
View on GitHub
Get all realms
Java
Ruby
JavaScript
Kotlin

Selenium v4.15

        try (Script script = new Script(firstWindow, driver)) {
            List<RealmInfo> realms = script.getAllRealms();
View Complete Code
View on GitHub
Get realm by type
Java
Ruby
JavaScript
Kotlin

Selenium v4.15

        try (Script script = new Script(firstWindow, driver)) {
            List<RealmInfo> realms = script.getRealmsByType(RealmType.WINDOW);
View Complete Code
View on GitHub
Get browsing context realms
Java
Ruby
JavaScript
Kotlin

Selenium v4.15

        try (Script script = new Script(windowId, driver)) {
            List<RealmInfo> realms = script.getRealmsInBrowsingContext(tabId);
View Complete Code
View on GitHub
Get browsing context realms by type
Java
Ruby
JavaScript
Kotlin

Selenium v4.15

            List<RealmInfo> windowRealms =
                    script.getRealmsInBrowsingContextByType(windowId, RealmType.WINDOW);
View Complete Code
View on GitHub
Preload a script
Java
Ruby
JavaScript
Kotlin

Selenium v4.15

            String id = script.addPreloadScript("() => { window.bar=2; }", "sandbox");
View Complete Code
View on GitHub
Remove a preloaded script
Java
Ruby
JavaScript
Kotlin

Selenium v4.15

                script.removePreloadScript(id);
View Complete Code
View on GitHub
Events

This section contains the APIs related to script events.

Message
Java
Ruby
JavaScript
Kotlin

Selenium v4.16

        try (Script script = new Script(driver)) {
            CompletableFuture<Message> future = new CompletableFuture<>();
            script.onMessage(future::complete);

            script.callFunctionInBrowsingContext(
                    driver.getWindowHandle(),
                    "(channel) => channel('foo')",
                    false,
                    Optional.of(List.of(LocalValue.channelValue("channel_name"))),
                    Optional.empty(),
                    Optional.empty());

            Message message = future.get(5, TimeUnit.SECONDS);
            Assertions.assertEquals("channel_name", message.getChannel());
        }
View Complete Code
View on GitHub
Realm Created
Java
Ruby
JavaScript
Kotlin

Selenium v4.16

        try (Script script = new Script(driver)) {
            CompletableFuture<RealmInfo> future = new CompletableFuture<>();
            script.onRealmCreated(future::complete);

            BrowsingContext context = new BrowsingContext(driver, driver.getWindowHandle());

            context.navigate("https://www.selenium.dev/selenium/blankPage");
            RealmInfo realmInfo = future.get(5, TimeUnit.SECONDS);
            Assertions.assertNotNull(realmInfo.getRealmId());
            Assertions.assertEquals(RealmType.WINDOW, realmInfo.getRealmType());
        }
View Complete Code
View on GitHub
Realm Destroyed
Java
Ruby
JavaScript
Kotlin

Selenium v4.16

        try (Script script = new Script(driver)) {
            CompletableFuture<RealmInfo> future = new CompletableFuture<>();
            script.onRealmDestroyed(future::complete);

            BrowsingContext context = new BrowsingContext(driver, driver.getWindowHandle());

            context.close();
            RealmInfo realmInfo = future.get(5, TimeUnit.SECONDS);
            Assertions.assertNotNull(realmInfo.getRealmId());
            Assertions.assertEquals(RealmType.WINDOW, realmInfo.getRealmType());
        }
View Complete Code
View on GitHub
Last modified July 10, 2024: Release 4.22 Updates (#1765) (fa7b1165ed0)
Development Partners
Selenium Level Sponsors
Support the Selenium Project

Learn more or view the full list of sponsors.

LEARN MORE 
© 2026 Software Freedom Conservancy All Rights Reserved

About Selenium
