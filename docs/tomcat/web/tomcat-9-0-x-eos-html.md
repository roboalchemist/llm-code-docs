# Source: https://tomcat.apache.org/tomcat-9.0.x-eos.html

Title: End of support for Apache Tomcat 9.0.x

URL Source: https://tomcat.apache.org/tomcat-9.0.x-eos.html

Markdown Content:
The Apache Tomcat® team announces that support for Apache Tomcat 9.0.x will end on 31 March 2027.

This means that after 31 March 2027:

*   releases from the 9.0.x branch are highly unlikely
*   bugs affecting only the 9.0.x branch will not be addressed
*   security vulnerability reports will not be checked against the 9.0.x branch

Three months later (i.e. after 30 June 2027)

*   the 9.0.x download links will be removed
*   the latest 9.0.x release will be removed from the mirror system
*   the links to the 9.0.x documentation will be removed from tomcat.apache.org

Note that all 9.0.x releases will always be available from the archive.

It is anticipated that the final 9.0.x release will be made shortly before 31 March 2027.

Shortly before 9.0.x support ends, releases from a new 9.1.x branch will be made available. Releases from the 9.1.x branch will continue until 31 December 2030.

The differences between 9.0.x and 9.1.x will be minimal and users can start making the necessary transition now. Those changes are:

*   the APR/native connectors for HTTP, HTTPS and AJP will not be available
*   Support for Tomcat Native 2.0.x will continue but Tomcat Native 1.3.x will not be supported (see the separate EOS announcement for Tomcat Native 1.3.x)

Users of the APR/native AJP connector are strongly encouraged to migrate to the NIO AJP connector and discontinue using Tomcat Native.

Users of the APR/native HTTP connector are strongly encouraged to migrate to the NIO HTTP connector and discontinue using Tomcat Native.

Users of the APR/native HTTPS connector are strongly encouraged to migrate to either the the HTTPS NIO+JSSE connector or the HTTPS NIO+OpenSSL connector. Those migrating to the HTTP NIO+OpenSSL connector should then upgrade Tomcat Native to 2.0.x.

For users that are not using Tomcat Native or are using Tomcat Native 2.0.x, the transition from 9.0.x to 9.1.x will be no different to a normal Tomcat point release upgrade.

Rather than continuing on 9.1.x, Tomcat 9 users are strongly encouraged to consider upgrading to a more recent Tomcat version making use of tools like the Tomcat Migration Tool for Jakarta EE.
