# Source: https://tomcat.apache.org/tools.html

Title: Apache Tomcat® - Developer Tools

URL Source: https://tomcat.apache.org/tools.html

Markdown Content:
### Table of Contents

*   [Overview](https://tomcat.apache.org/tools.html#Overview)
*   [Apache Tools](https://tomcat.apache.org/tools.html#Apache_Tools)
*   [Open Source Tools](https://tomcat.apache.org/tools.html#Open_Source_Tools)
*   [Commercial Tools](https://tomcat.apache.org/tools.html#Commercial_Tools)

### Overview

This page lists the various tools that the Apache Tomcat® project uses. Not all developers use every tool. There are almost certainly some tools that are missing. If you are a committer, you know how to fix this. If you are not a committer, send a short note to the [developer mailing list](https://tomcat.apache.org/lists.html#tomcat-dev) (you'll need to subscribe if you are not already subscribed) and a committer should be able to fix it for you.

### Apache Tools

[![Image 1: Apache Ant](http://ant.apache.org/images/ant_logo_medium.gif)](http://ant.apache.org/)Apache Tomcat is built using Apache Ant.

### Open Source Tools

[![Image 2: Eclipse](https://tomcat.apache.org/res/images/eclipse.gif)](https://www.eclipse.org/)A variety of IDEs are used by the Tomcat developers. One of them is the Eclipse IDE.
[![Image 3: UCDetector](https://tomcat.apache.org/res/images/ucdetector32.png)](https://www.ucdetector.org/)The Unnecessary Code Detector is used by the Tomcat developers to identify code to be removed from future versions of Tomcat.
[![Image 4: SpotBugs](https://tomcat.apache.org/res/images/spotbugs_icon_only_zoom_256px.png)](https://spotbugs.github.io/)SpotBugs is used by the Tomcat developers to identify potential coding errors.
[![Image 5: Checkstyle](https://tomcat.apache.org/res/images/header-checkstyle-logo.png)](https://checkstyle.sourceforge.io/)Checkstyle is used by the Tomcat developers to maintain the Tomcat coding standard.
[🌱 PlantUML](https://plantuml.com/en/)PlantUML is used to create diagrams for Tomcat documentation.
[![Image 6: Far Manager](https://tomcat.apache.org/res/images/far-icon.png)](https://www.farmanager.com/index.php?l=en)Far Manager is a two-panel file manager application for Microsoft Windows. It works in console mode and is very useful to run command-line tools and make small edits that do not require an IDE. It is free software since version 1.75 build 2629 and open source since version 2.0.

### Commercial Tools

[![Image 7: YourKit](https://tomcat.apache.org/res/images/yjp.gif)](http://www.yourkit.com/)YourKit, LLC kindly provide free licenses for the YourKit Java Profiler to open source projects. YourKit Java Profiler is primarily used to investigate performance and memory leak issues reported in Apache Tomcat. It was particularly useful when working on the memory leak detection and prevention code.
[![Image 8: MSDN](https://tomcat.apache.org/res/images/msdn.png)](http://msdn.microsoft.com/)Microsoft kindly provide free MSDN licenses to Apache committers that have a requirement for them. MSDN is primarily used to provide build and test environments for the ISAPI redirector and the Windows APR/native connector but it is also used to provide test platforms for Windows specific Tomcat issues such as those related to the Windows Installer.
[![Image 9: Structure 101](https://tomcat.apache.org/res/images/s101.png)](http://www.structure101.com/)Headway software kindly provide free licenses for Structure 101 to open source projects. Structure 101 is primarily being used in Tomcat trunk to analyze the current package dependencies and identify areas where they may be simplified.
[![Image 10: Simian](https://tomcat.apache.org/res/images/simian.jpg)](http://www.harukizaemon.com/simian/index.html)Simon Harris kindly provides free licenses for Simian (Similarity Analyzer) to open source projects. Simian is primarily being used in Tomcat trunk to reduce code duplication.
[![Image 11: POEditor](https://tomcat.apache.org/res/images/poeditor.svg)](https://poeditor.com/)Code Whale Inc. kindly offer a free unlimited localization project to open source projects that use an OSI approved license. Apache Tomcat is using POEditor primarily in Tomcat trunk to manage translations. The Tomcat project has seen a significant increase in localization contributions since starting to use POEditor.
