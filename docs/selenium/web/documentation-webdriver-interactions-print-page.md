# Source: https://selenium.dev/documentation/webdriver/interactions/print_page/

Title: Print Page

URL Source: https://selenium.dev/documentation/webdriver/interactions/print_page/

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
Navigation
Alerts
Cookies
Frames
Print Page
Windows
Virtual Authenticator
Actions API
BiDi
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
Configuring
Orientation
Range
Size
Margins
Scale
Background
ShrinkToFit
Printing
Documentation
WebDriver
Interactions
Print Page
v4.0
Print Page

Printing a webpage is a common task, whether for sharing information or maintaining archives. Selenium simplifies this process through its PrintOptions, PrintsPage, and browsingContext classes, which provide a flexible and intuitive interface for automating the printing of web pages. These classes enable you to configure printing preferences, such as page layout, margins, and scaling, ensuring that the output meets your specific requirements.

Configuring
Orientation

Using the getOrientation() and setOrientation() methods, you can get/set the page orientation — either PORTRAIT or LANDSCAPE.

Java
CSharp
Ruby
Python
JavaScript
Kotlin
        driver.get("https://www.selenium.dev/");
        PrintOptions printOptions = new PrintOptions();
        printOptions.setOrientation(PrintOptions.Orientation.LANDSCAPE);
        PrintOptions.Orientation current_orientation = printOptions.getOrientation();
View Complete Code
View on GitHub
Range

Using the getPageRanges() and setPageRanges() methods, you can get/set the range of pages to print — e.g. “2-4”.

Java
CSharp
Ruby
Python
JavaScript
Kotlin
        driver.get("https://www.selenium.dev/");
        PrintOptions printOptions = new PrintOptions();
        printOptions.setPageRanges("1-2");
        String[] current_range = printOptions.getPageRanges();
View Complete Code
View on GitHub
Size

Using the getPageSize() and setPageSize() methods, you can get/set the paper size to print — e.g. “A0”, “A6”, “Legal”, “Tabloid”, etc.

Java
CSharp
Ruby
Python
JavaScript
Kotlin
        driver.get("https://www.selenium.dev/");
        PrintOptions printOptions = new PrintOptions();
        printOptions.setPageSize(new PageSize(27.94, 21.59)); // A4 size in cm
        double currentHeight = printOptions.getPageSize().getHeight(); // use getWidth() to retrieve width
View Complete Code
View on GitHub
Margins

Using the getPageMargin() and setPageMargin() methods, you can set the margin sizes of the page you wish to print — i.e. top, bottom, left, and right margins.

Java
CSharp
Ruby
Python
JavaScript
Kotlin
        driver.get("https://www.selenium.dev/");
        PrintOptions printOptions = new PrintOptions();
        PageMargin margins = new PageMargin(1.0,1.0,1.0,1.0);
        printOptions.setPageMargin(margins);
        double topMargin = margins.getTop();
        double bottomMargin = margins.getBottom();
        double leftMargin = margins.getLeft();
        double rightMargin = margins.getRight();
View Complete Code
View on GitHub
Scale

Using getScale() and setScale() methods, you can get/set the scale of the page you wish to print — e.g. 1.0 is 100% or default, 0.25 is 25%, etc.

Java
CSharp
Ruby
Python
JavaScript
Kotlin
    {
        driver.get("https://www.selenium.dev/");
        PrintOptions printOptions = new PrintOptions();
        printOptions.setScale(.50);
        double current_scale = printOptions.getScale();
View Complete Code
View on GitHub
Background

Using getBackground() and setBackground() methods, you can get/set whether background colors and images appear — boolean true or false.

Java
CSharp
Ruby
Python
JavaScript
Kotlin
        driver.get("https://www.selenium.dev/");
        PrintOptions printOptions = new PrintOptions();
        printOptions.setBackground(true);
        boolean current_background = printOptions.getBackground();
View Complete Code
View on GitHub
ShrinkToFit

Using getShrinkToFit() and setShrinkToFit() methods, you can get/set whether the page will shrink-to-fit content on the page — boolean true or false.

Java
CSharp
Ruby
Python
JavaScript
Kotlin
        driver.get("https://www.selenium.dev/");
        PrintOptions printOptions = new PrintOptions();
        printOptions.setShrinkToFit(true);
        boolean current_shrink_to_fit = printOptions.getShrinkToFit();
View Complete Code
View on GitHub
Printing

Once you’ve configured your PrintOptions, you’re ready to print the page. To do this, you can invoke the print function, which generates a PDF representation of the web page. The resulting PDF can be saved to your local storage for further use or distribution. Using PrintsPage(), the print command will return the PDF data in base64-encoded format, which can be decoded and written to a file in your desired location, and using BrowsingContext() will return a String.

There may currently be multiple implementations depending on your language of choice. For example, with Java you have the ability to print using either BrowingContext() or PrintsPage(). Both take PrintOptions() objects as a parameter.

Note: BrowsingContext() is part of Selenium’s BiDi implementation. To enable BiDi see Enabling Bidi

Java
CSharp
Ruby
Python
JavaScript
Kotlin

PrintsPage()

        PrintsPage printer = (PrintsPage) driver;
        PrintOptions printOptions = new PrintOptions();
        Pdf printedPage = printer.print(printOptions);
        Assertions.assertNotNull(printedPage);
    }
View Complete Code
View on GitHub

BrowsingContext()

        driver.get("https://www.selenium.dev/selenium/web/formPage.html");
        PrintOptions printOptions = new PrintOptions();
        String printPage = browsingContext.print(printOptions);
        Assertions.assertTrue(printPage.length() > 0);
    }
View Complete Code
View on GitHub
Last modified July 29, 2025: Adding trailing / to retrieve code from GitHub (48b97e9bf82)
Development Partners
Selenium Level Sponsors
Support the Selenium Project

Learn more or view the full list of sponsors.

LEARN MORE 
© 2026 Software Freedom Conservancy All Rights Reserved

About Selenium
