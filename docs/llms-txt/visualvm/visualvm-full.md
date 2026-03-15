<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="en-US" xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US">
<head>
<meta name="generator" content="HTML Tidy, see www.w3.org">
<title>Java VisualVM</title>
<meta name="yyy" content="reference">

<script language="javascript1.2" type="text/javascript" src="../../../../../webdesign/other/js/search.js"></script>
<script language="javascript1.2" type="text/javascript" src="../../../../../webdesign/pubs8/js/popUp.js"></script>
<script language="javascript1.2" type="text/javascript" src="../../../../../webdesign/pubs8/js/sniff.js"></script>
<script language="javascript1.2" type="text/javascript" src="../../../../../webdesign/pubs8/js/menucontent.js"></script>
<script language="javascript1.2" type="text/javascript" src="../../../../../webdesign/pubs8/js/menucode.js"></script>
<script language="javascript1.2" type="text/javascript" src="../../../../../webdesign/pubs8/js/developer.js"></script>
<link rel="stylesheet" type="text/css" href="../../../../../webdesign/pubs8/css/default_developer.css">
<meta name="collection" content="reference"> 
<script id="ssot-metadata" type="application/json">{"primary":{"category":{"short_name":"java","element_name":"Java","display_in_url":true},"suite":{"short_name":"not-applicable","element_name":"Not Applicable","display_in_url":false},"product_group":{"short_name":"not-applicable","element_name":"Not Applicable","display_in_url":false},"product":{"short_name":"javase","element_name":"Java SE","display_in_url":true},"release":{"short_name":"8","element_name":"8","display_in_url":true}}}</script>
    <script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","name":"Java VisualVM","datePublished":"2025-10-20 CST","dateModified":"2025-10-20 CST"}</script>
    <script>window.ohcglobal || document.write('<script src="/en/dcommon/js/global.js">\x3C/script>')</script></head>
<body>
<noscript>JavaScript is not supported by your browser. JavaScript
support is required for full functionality of this page.</noscript>
<div class="a0 a0v1" id="a0v1"><!-- BEGIN A1 COMPONENT V.0 -->
<div class="a1 a1r2">
<div class="a1v0"><a href="#skip2content" class="skiplink">Skip to
Content</a></div>
</div>
<!-- END A1 COMPONENT V.0 -->
<!-- BEGIN A2 COMPONENT V.1 -->
<div class="a2w0">
<div class="a2" id="a2v1">
<div class="a2w1">
<div class="a2w2">
<div class="a2w3">
<div class="a2w4">
<div class="a2topiclinks"><a href="http://www.oracle.com" title="Oracle Home Page" id="sunlogo" name="sunlogo"><img src="../../../../../webdesign/pubs8/im/a.gif" alt="Home Page" width="98" height="58" border="0"></a>

<ul id="mtopics">

  <li id="mtopic1">
    <a id="glink1" class="tpclink a2menu" title="Java Software" href="https://www.oracle.com/java/" name="glink1">Java Software</a>
  </li>
  
  <li id="mtopic2">
    <a id="glink2" class="tpclink a2menu" title="Java SE Downloads" href="https://www.oracle.com/java/technologies/javase-downloads.html" name="glink2">Java SE Downloads</a>
  </li>
  
  <li id="mtopic3">
    <a id="glink3" class="tpclink a2menu" title="Java Documentation" href="https://docs.oracle.com/javase/8/" name="glink3">Java SE 8 Documentation</a>
  </li>
  
</ul>
<div class="a2search"><a href="../../../../../search.html" target="_blank">Search</a></div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<!-- END A2 COMPONENT V.1 -->
<!-- BEGIN SEPARATOR -->
<div class="hr">
<hr></div>
<!-- END SEPARATOR -->
<!-- ============ -->
<!-- MAIN CONTENT -->
<!-- ============ -->
<a name="skip2content" id="skip2content"></a>


<div class="smallpagetitle"><h1>Java VisualVM</h1></div>

<p style="background-color: rgb(247, 248, 249); border-width: 1px; padding: 10px; font-style: italic; border-style: solid; border-color: rgb(64, 74, 91);">As of JDK 8u361, Java VisualVM is no longer included as part of Java SE 8. Please visit <a href=" https://visualvm.github.io" target="_blank"> https://visualvm.github.io</a> for more information.</p>


<!-- Body text begins here -->
<p>Java VisualVM is a tool that provides a visual interface for
viewing detailed information about Java applications while they are
running on a Java Virtual Machine (JVM), and for troubleshooting
and profiling these applications. Various optional tools, including
Java VisualVM, are provided with the Java
Development Kit (JDK) for retrieving different types of data about
running JVM software instances. For example, most of the previously
standalone tools JConsole, <span class="style1">jstat</span>,
<span class="style1">jinfo</span>, <span class="style1">jstack</span>, and <span class="style1">jmap</span> are
part of Java VisualVM. Java VisualVM federates these tools to
obtain data from the JVM software, then re-organizes and presents
the information graphically, to enable you to view different data
about multiple Java applications uniformly, whether they are
running locally or on remote machines. Furthermore, developers can
extend Java VisualVM to add new functionality by creating and
posting plug-ins to the tool's built-in update center.</p>
<p>Java VisualVM can be used by Java application developers to
troubleshoot applications and to monitor and improve the
applications' performance. Java VisualVM can allow developers to
generate and analyse heap dumps, track down memory leaks, browse
the platform's MBeans and perform operations on those MBeans,
perform and monitor garbage collection, and perform lightweight
memory and CPU profiling.</p>
<p>Java VisualVM was first bundled with the the Java platform,
Standard Edition (Java SE) in JDK version 6, update 7.</p>
<h2>Overview</h2>
<ul>
<li>The following documents provide an introduction to Java
VisualVM.
<ul>
<li><a href="intro.html"><strong>Introduction to Java
VisualVM</strong></a>
<ul>
<li><a href="applications_window.html">Using the Applications
Window</a></li>
<li><a href="applications_local.html">Working with Local
Applications</a>
<ul>
<li><a href="overview_tab.html">Viewing Application
Overview</a></li>
<li><a href="monitor_tab.html">Monitoring an Application</a></li>
<li><a href="threads.html">Monitoring Application Threads</a></li>
<li><a href="profiler.html">Profiling Applications</a></li>
<li><a href="jmx_connections.html">Connecting to JMX Agents
Explicitly</a></li>
</ul>
</li>
<li><a href="applications_remote.html">Working with Remote
Applications</a>
<ul>
<li><a href="overview_tab.html">Viewing Application
Overview</a></li>
<li><a href="monitor_tab.html">Monitoring an Application</a></li>
<li><a href="threads.html">Monitoring Application Threads</a></li>
<li><a href="jmx_connections.html">Connecting to JMX Agents
Explicitly</a></li>
</ul>
</li>
<li><a href="coredumps.html">Working with Coredumps</a></li>
<li><a href="snapshots.html">Working with Snapshots</a></li>
<li><a href="heapdump.html">Browsing a Heap Dump</a></li>
</ul>
</li>
</ul>
</li>
<li>The following pages provide information about optional plug-ins
that are currently available for Java VisualVM. These plug-ins are
evolving outside of the JDK platform's update cycle.
<ul>
<li><a href="https://htmlpreview.github.io/?https://raw.githubusercontent.com/visualvm/visualvm.java.net.backup/master/www/mbeans_tab.html">Working with
MBeans</a></li>
<li><a href="https://htmlpreview.github.io/?https://raw.githubusercontent.com/visualvm/visualvm.java.net.backup/master/www/jconsole_plugin_wrapper_tab.html">JConsole
Plug-In Wrapper Tab</a></li>
</ul>
</li>
</ul>
<h2>Tools</h2>
<ul>
<li><strong><tt>jvisualvm</tt></strong> - the man page for Java VisualVM for <a href="../../tools/unix/jvisualvm.html">Solaris, Linux, or Mac OS X</a> or <a href="../../tools/windows/jvisualvm.html">Windows</a>.</li>
</ul>
<h2>Tutorials and Programmer's Guides</h2>
<ul>
<li><a href="https://htmlpreview.github.io/?https://raw.githubusercontent.com/visualvm/visualvm.java.net.backup/master/www/api-quickstart.html">Getting
Started Extending Java VisualVM</a> - An introduction to the Java
VisualVM APIs, providing details of how to write extensions for
Java VisualVM to create customized monitoring, troubleshooting and
profiling services for your applications.</li>
<li><a href="https://htmlpreview.github.io/?https://raw.githubusercontent.com/visualvm/visualvm.java.net.backup/master/www/api-faq.html">VisualVM API
FAQs</a>.</li>
</ul>
<h2>More Information</h2>
<ul>
<li><a href="https://visualvm.github.io/">Java VisualVM Developers'
Site</a></li>
<li><a href="../management/index.html">Java SE Platform Monitoring
and Management documentation</a></li>
<li><a href="http://www.oracle.com/technetwork/java/javase/index-138283.html">Troubleshooting
the Java SE Platform</a></li>
</ul>

<div id="javasefooter">
<div class="hr">
<hr></div>
<div id="javasecopyright">
<a href="../../../legal/cpyr.html">Copyright &#169;</a> 1993, 2025, Oracle
and/or its affiliates. All rights reserved.
</div>

<div id="javasecontactus">
<a href="http://docs.oracle.com/javase/feedback.html">Contact Us</a>
</div>
</div>
</div>

<!-- Start SiteCatalyst code -->
<script type="application/javascript" src="https://www.oracleimg.com/us/assets/metrics/ora_docs.js"></script>
<!-- End SiteCatalyst code -->

</body>
</html>