# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/performance-tuning/pentaho-server-performance-tips/test-pentaho-server-scalability.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/pentaho-server-performance-tips/test-pentaho-server-scalability.md

# Test Pentaho Server scalability

Improper scalability testing can give you the wrong idea about changes you have made to your Pentaho Server instance. Before testing, ensure that you are reusing sessions, instead of creating successive new sessions. Creating multiple unnecessary sessions causes the Pentaho Server to run out of memory unless the session timeout in `web.xml` is set extremely low (1 per minute, for instance). The default is 30 minutes.

Logging into the Pentaho Server is resource-intensive. You must authenticate the user, create a bunch of session data, and run all startup action sequences, which usually store data in the user's session. So, if during testing, you simply string together a bunch of URLs and ignore the established session, you will create a series of 30-minute sessions and almost certainly run out of memory.

The correct way to test the server is to mimic a user's actions from a browser.

## Sessions and URLs

Most stress test tools (Loadrunner, JMeter, etc.) have session/cookie management options to ensure that they behave like a human user. However, if you're creating your own test scripts, you should follow this process:

1. Log into the server.
2. Execute a URL that contains the **userid** and **password** parameters.

   `&userid=administrator&password=password`
3. Using the same session, submit other URLs without the userid/password.

Use this process for as many users as you need to test with.

To log out of a session, you can use the [**http://localhost:8080/pentaho/Logout**](http://localhost:8080/pentaho/Logout) URL. This will invalidate the session if you append the **userid** and **password** values of the logged-in user. Without passing those parameters (or, alternatively, specifying the session ID or cookie) on the Logout URL, you will create another new session instead of closing an old one.

This means that two back-to-back `wget` commands in Linux will create two different HTTP sessions on the server unless one of the following conditions is met:

* Session 1: -cookies=on is specified for both `wget` commands
* Session 2: -save-cookies is used on the first `wget` command to save the cookies to a file, and -load-cookies is used on the second `wget` command to load the session state

## Memory and sessions

Out of memory errors can happen because of what your test script is doing, not necessarily because of any weakness in the Pentaho platform. You can see just how robust the the Pentaho platform is by taking a look at a production server's natural (human user) load. The following URL will show you what each day's maximum and present number of HTTP sessions are: [**http://testserver.example.com/pentah...ic/UserService**](http://testserver.example.com/pentaho/public/UserService)

You can see the Java virtual machine memory settings by examining the options passed to the Tomcat start scripts, or by looking at the *CATALINA\_OPTS* system variable, if there is one. The Xms and Xmx options define the minimum and maximum amount of memory assigned to the application server. The default settings are not particularly high, and even if you have adjusted them, take note of the number of sessions it takes to use up all of the memory. Also take note of the fact that closing sessions after an out of memory error will return the memory to the available pool, proving that there are no memory leaks or zombie sessions inherent in the Pentaho platform.
