# Source: https://selenium.dev/documentation/webdriver/bidi/w3c/network/

Title: Network

URL Source: https://selenium.dev/documentation/webdriver/bidi/w3c/network/

Markdown Content:
About
Downloads
Documentation
Projects
Support
Blog
English
Search
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
Add network intercept
Remove network intercept
Continue request blocked at authRequired phase with credentials
Continue request blocked at authRequired phase without credentials
Cancel request blocked at authRequired phase
Fail request
Events
Before Request Sent
Response Started
Response Completed
Auth Required
Documentation
WebDriver
BiDi
W3C
Network
v4.0
Network
Commands

This section contains the APIs related to network commands.

Add network intercept
Java
Ruby
JavaScript
Kotlin

Selenium v4.18

            String intercept =
                    network.addIntercept(new AddInterceptParameters(InterceptPhase.BEFORE_REQUEST_SENT));
            Assertions.assertNotNull(intercept);
View Complete Code
View on GitHub
Remove network intercept
Java
Ruby
JavaScript
Kotlin

Selenium v4.18

                    network.addIntercept(new AddInterceptParameters(InterceptPhase.BEFORE_REQUEST_SENT));
            Assertions.assertNotNull(intercept);
            network.removeIntercept(intercept);
        }
    }
View Complete Code
View on GitHub
Continue request blocked at authRequired phase with credentials
Java
Ruby
JavaScript
Kotlin

Selenium v4.18

                    responseDetails ->
                            network.continueWithAuth(
                                    responseDetails.getRequest().getRequestId(),
                                    new UsernameAndPassword("admin", "admin")));
            driver.get("https://the-internet.herokuapp.com/basic_auth");
            String successMessage = "Congratulations! You must have the proper credentials.";
            WebElement elementMessage = driver.findElement(By.tagName("p"));
            Assertions.assertEquals(successMessage, elementMessage.getText());
View Complete Code
View on GitHub
Continue request blocked at authRequired phase without credentials
Java
Ruby
JavaScript
Kotlin

Selenium v4.18

                            // Does not handle the alert
                            network.continueWithAuthNoCredentials(responseDetails.getRequest().getRequestId()));
            driver.get("https://the-internet.herokuapp.com/basic_auth");
            Alert alert = wait.until(ExpectedConditions.alertIsPresent());
            alert.dismiss();
            Assertions.assertTrue(driver.getPageSource().contains("Not authorized"));
        }
View Complete Code
View on GitHub
Cancel request blocked at authRequired phase
Java
Ruby
JavaScript
Kotlin

Selenium v4.18

                            network.cancelAuth(responseDetails.getRequest().getRequestId()));
            driver.get("https://the-internet.herokuapp.com/basic_auth");
            Assertions.assertTrue(driver.getPageSource().contains("Not authorized"));
        }
    }

    @Test
View Complete Code
View on GitHub
Fail request
Java
Ruby
JavaScript
Kotlin

Selenium v4.18

            }
    }
}

View Complete Code
View on GitHub
Events

This section contains the APIs related to network events.

Before Request Sent
Java
Ruby
JavaScript
Kotlin

Selenium v4.15

        try (Network network = new Network(driver)) {
            CompletableFuture<BeforeRequestSent> future = new CompletableFuture<>();
            network.onBeforeRequestSent(future::complete);
            driver.get("https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html");

            BeforeRequestSent requestSent = future.get(5, TimeUnit.SECONDS);
View Complete Code
View on GitHub
Response Started
Java
Ruby
JavaScript
Kotlin

Selenium v4.15

        try (Network network = new Network(driver)) {
            CompletableFuture<ResponseDetails> future = new CompletableFuture<>();
            network.onResponseStarted(future::complete);
            driver.get("https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html");

            ResponseDetails response = future.get(5, TimeUnit.SECONDS);
            String windowHandle = driver.getWindowHandle();
View Complete Code
View on GitHub
Response Completed
Java
Ruby
JavaScript
Kotlin

Selenium v4.15

        try (Network network = new Network(driver)) {
            CompletableFuture<ResponseDetails> future = new CompletableFuture<>();
            network.onResponseCompleted(future::complete);
            driver.get("https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html");

            ResponseDetails response = future.get(5, TimeUnit.SECONDS);
            String windowHandle = driver.getWindowHandle();
View Complete Code
View on GitHub
Auth Required
Java
Ruby
JavaScript
Kotlin

Selenium v4.17

        try (Network network = new Network(driver)) {
            CompletableFuture<ResponseDetails> future = new CompletableFuture<>();
            network.onAuthRequired(future::complete);
            driver.get("https://the-internet.herokuapp.com/basic_auth");

            ResponseDetails response = future.get(5, TimeUnit.SECONDS);
View Complete Code
View on GitHub
Last modified May 27, 2025: Update dependency selenium-webdriver to v4.33.0 (#2316) (5f5285aba17)
Development Partners
Selenium Level Sponsors
Support the Selenium Project

Learn more or view the full list of sponsors.

LEARN MORE 
© 2026 Software Freedom Conservancy All Rights Reserved

About Selenium
