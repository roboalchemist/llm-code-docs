# Source: https://jmeter.apache.org/usermanual/curl.html

Title: Apache JMeter
          -
          User's Manual: Curl

URL Source: https://jmeter.apache.org/usermanual/curl.html

Published Time: Sun, 07 Jan 2024 17:19:24 GMT

Markdown Content:
Apache JMeter - User's Manual: Curl
===============
[Main content](https://jmeter.apache.org/usermanual/curl.html#content)

[![Image 1: Logo ASF](https://jmeter.apache.org/images/asf-logo.svg)](https://www.apache.org/)

[![Image 2: Apache JMeter](https://jmeter.apache.org/images/logo.svg)](https://jmeter.apache.org/)

[![Image 3: Current Apache event teaser](https://www.apache.org/events/current-event-234x60.png)](https://www.apache.org/events/current-event.html)

*   About 
    *   [Overview](https://jmeter.apache.org/index.html)
    *   [License](https://www.apache.org/licenses/)

*   Download 
    *   [Download Releases](https://jmeter.apache.org/download_jmeter.cgi)
    *   [Release Notes](https://jmeter.apache.org/changes.html)

*   Documentation 
    *   [Get Started](https://jmeter.apache.org/usermanual/get-started.html)
    *   [User Manual](https://jmeter.apache.org/usermanual/index.html)
    *   [Best Practices](https://jmeter.apache.org/usermanual/best-practices.html)
    *   [Component Reference](https://jmeter.apache.org/usermanual/component_reference.html)
    *   [Functions Reference](https://jmeter.apache.org/usermanual/functions.html)
    *   [Properties Reference](https://jmeter.apache.org/usermanual/properties_reference.html)
    *   [Change History](https://jmeter.apache.org/changes_history.html)
    *   [Javadocs](https://jmeter.apache.org/api/index.html)
    *   [JMeter Wiki](https://cwiki.apache.org/confluence/display/JMETER/Home)
    *   [FAQ (Wiki)](https://cwiki.apache.org/confluence/display/JMETER/JMeterFAQ)

*   Tutorials 
    *   [Distributed Testing](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.html)
    *   [Recording Tests](https://jmeter.apache.org/usermanual/jmeter_proxy_step_by_step.html)
    *   [JUnit Sampler](https://jmeter.apache.org/usermanual/junitsampler_tutorial.html)
    *   [Access Log Sampler](https://jmeter.apache.org/usermanual/jmeter_accesslog_sampler_step_by_step.html)
    *   [Extending JMeter](https://jmeter.apache.org/usermanual/jmeter_tutorial.html)

*   Community 
    *   [Issue Tracking](https://jmeter.apache.org/issues.html)
    *   [Security](https://jmeter.apache.org/security.html)
    *   [Mailing Lists](https://jmeter.apache.org/mail.html)
    *   [Source Repositories](https://jmeter.apache.org/svnindex.html)
    *   [Building and Contributing](https://jmeter.apache.org/building.html)
    *   [Project info at Apache](https://projects.apache.org/project.html?jmeter)
    *   [Contributors](https://cwiki.apache.org/confluence/display/JMETER/JMeterCommitters)

*   Foundation 
    *   [The Apache Software Foundation (ASF)](https://www.apache.org/)
    *   [Get Involved in the ASF](https://www.apache.org/foundation/getinvolved.html)
    *   [Privacy Policy](https://privacy.apache.org/policies/privacy-policy-public.html)
    *   [Sponsorship](https://www.apache.org/foundation/sponsorship.html)
    *   [Thanks](https://www.apache.org/foundation/thanks.html)

*   [Twitter](https://twitter.com/ApacheJMeter "Follow us on Twitter")
*   [github](https://github.com/apache/jmeter "Fork us on github")

*   [< Prev](https://jmeter.apache.org/usermanual/glossary.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/history_future.html)

24. Curl[¶](https://jmeter.apache.org/usermanual/curl.html#hints "Link to here")
================================================================================

This method is to create http requests from curl command. If you want to know more about curl, please click the [Curl document](https://curl.haxx.se/).

24.1 How to enter (a) command(s)[¶](https://jmeter.apache.org/usermanual/curl.html#enter_command "Link to here")
----------------------------------------------------------------------------------------------------------------

Create a Test Plan From a cURL Command

1.    To create an import from a cURL, open the Tools menu and click Import from cURL. [![Image 4: Figure 1 - The menu where curl is located](https://jmeter.apache.org/images/screenshots/curl/choose_curl.png)](https://jmeter.apache.org/images/screenshots/curl/choose_curl.png)

Figure 1 - The menu where curl is located

2.    There are two ways to enter the curl command line. Firstly, we can enter it manually. Secondly, we can import a file containing the curl command line. This tool supports input of multiple curl command lines at the same time. [![Image 5: Figure 2.1 - Enter curl command in text panel](https://jmeter.apache.org/images/screenshots/curl/enter_command.png)](https://jmeter.apache.org/images/screenshots/curl/enter_command.png)

Figure 2.1 - Enter curl command in text panel

[![Image 6: Figure 2.2 - Enter curl command from file](https://jmeter.apache.org/images/screenshots/curl/enter_command_from_file.png)](https://jmeter.apache.org/images/screenshots/curl/enter_command_from_file.png)

Figure 2.2 - Enter curl command from file

3.    Then, click Create Test Plan button and a new HTTP Sample will be added to the Test Plan. [![Image 7: Figure 3 - result of Test Plan](https://jmeter.apache.org/images/screenshots/curl/result.png)](https://jmeter.apache.org/images/screenshots/curl/result.png)

Figure 3 - result of Test Plan

24.2 Curl options supported[¶](https://jmeter.apache.org/usermanual/curl.html#curl_options "Link to here")
----------------------------------------------------------------------------------------------------------

-H, --header <header>Extra header to use when getting a web page.-X, --request <command>Specifies a custom request method to use when communicating with the HTTP server.--compressed Request a compressed response using one of the algorithms curl supports, and return the uncompressed document.-A, --user-agent <agent string>Specify the User-Agent string to send to the HTTP server.-b, --cookie <name=data>Pass the data to the HTTP server as a cookie.-d and friends 
Sending data via POST request

Sends the specified data in a POST request to the HTTP server. If this option is used more than once on the same command line, the data pieces specified will be merged together with a separating '&' character. Thus, using '-d name=daniel -d skill=lousy' would generate a POST chunk that looks like 'name=daniel&skill=lousy'.

-d, --data <data>, --data-ascii <data> use @ to upload a file --data-raw <data>gt; --data-raw <data> This posts data exactly as specified with no extra processing whatsoever. If you start the data with the character @, the rest should be a filename. --data-raw <data>ta> This posts data, similar to the other --data options with the exception that this performs URL-encoding. --data-raw <data> This posts data similarly to --data but without the special interpretation of the @ character. -F and friends 
This lets curl emulate a filled-in form in which a user has pressed the submit button.

-F, --form <name=content> use @ to upload a file --form-string <name=content>-u, --user <user:password >Specify user and password to use for server authentication.--basic, --digest Tells curl to use HTTP authentication.--cacert and friends 
Tells curl to use the specified client certificate file when getting a file with HTTPS

--cacert <CA certificate>--capath <CA certificate directory>--ciphers <list of ciphers>--cert-status--cert-type <type>-G, --get put the post data in the URL and use get to replace post.--no-keepalive Disables the use of keepalive messages on the TCP connection.-e, --referer <URL> Sends the _Referer Page_ information to the HTTP server. -L, --location If the server reports that the requested page has moved to a different location this option will make curl redo the request on the new place.-i, --include Include the HTTP-header in the output.--connect-timeout <seconds>Maximum time in seconds that the connection to the server may take.--keepalive-time <seconds>This option sets the time a connection needs to remain idle before sending keepalive probes and the time between individual keepalive probes.-m, --max-time <seconds>Maximum time in seconds that you allow the whole operation to take.-x, --proxy <[protocol://][user:password@]proxyhost[:port]> Use the specified HTTP proxy. If the port number is not specified, it is assumed at port 1080. -U, --proxy-user <user:password>Specify user and password to use for proxy authentication.-k, --insecure This option explicitly allows curl to perform _insecure_ SSL connections and transfers. --raw When used, it disables all internal HTTP decoding of content or transfer encodings and instead makes them passed on unaltered,raw.-I, --head Fetch the HTTP-header only. HTTP-servers feature the method HEAD which this uses to get nothing but the header of a document. --interface <name>Perform an operation using a specified interface. You can enter interface name, IP address or host name.--proxy-ntlm/--proxy-negotiate Tells curl to use HTTP BASIC/NTLM/Digest authentication when communicating with the given proxy.--dns-servers <addresses>Resolve host name over DOH.--resolve <host:port:address>Provide a custom address for a specific host and port pair.--limit-rate <speed>Specify the maximum transfer rate you want curl to use.--max-redirs <num>Set maximum number of redirections which may be followed.--noproxy <no-proxy-list>Comma-separated list of hosts which do not use a proxy, if one is specified.

24.3 Warning[¶](https://jmeter.apache.org/usermanual/curl.html#warning "Link to here")
--------------------------------------------------------------------------------------

When the command you entered is ignored or contains warning content, we will display warning in the comment section of HTTP Request.

[![Image 8: Figure 1 -Warning](https://jmeter.apache.org/images/screenshots/curl/http_request_warning.png)](https://jmeter.apache.org/images/screenshots/curl/http_request_warning.png)

Figure 1 -Warning

24.4 Examples[¶](https://jmeter.apache.org/usermanual/curl.html#example "Link to here")
---------------------------------------------------------------------------------------

**Use cookie**

curl -X POST  "https://example.invalid" -b 'username=Tom;password=123456'
**Use data**

curl -X POST  "https://example.invalid" --data 'fname=a&lname=b'
**Use form**

curl -X POST  "https://example.invalid" -F 'lname=a'  -F 'fname=b' -F 'c=@C:\Test\test.txt'
**Use proxy**

curl 'https://example.invalid/' -x 'https://aa:bb@proxy.invalid:8042'
**Use authorization**

curl "https://example.invalid" -u 'user:passwd' --basic
**Use DNS**

curl "https://example.invalid" --dns-servers '0.0.0.0,1.1.1.1'

*   [< Prev](https://jmeter.apache.org/usermanual/glossary.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/history_future.html)

 Share this page: 
*   [share](https://jmeter.apache.org/usermanual/curl.html "Share on facebook")
*   [tweet](https://jmeter.apache.org/usermanual/curl.html "Tweet on twitter")

[Go to top](https://jmeter.apache.org/usermanual/curl.html#top)

 Copyright © 1999 – 2024 , Apache Software Foundation 

Apache, Apache JMeter, JMeter, the Apache feather, and the Apache JMeter logo are trademarks of the Apache Software Foundation.
