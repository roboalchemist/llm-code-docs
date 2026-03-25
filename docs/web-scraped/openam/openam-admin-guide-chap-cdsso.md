# Source: https://doc.openidentityplatform.org/openam/admin-guide/chap-cdsso

Title: Configuring Cross-Domain Single Sign-On :: Open Identity Platform Documentation

URL Source: https://doc.openidentityplatform.org/openam/admin-guide/chap-cdsso

Markdown Content:
This chapter shows you how to configure cross-domain single sign-on (CDSSO). When you have multiple domains in a single organization, CDSSO lets your OpenAM servers in one domain work with policy agents from other domains. _Cross-domain single sign-on_ provides a safe mechanism for managing access across multiple, different domains that you control. CDSSO lets OpenAM authenticate users redirected by policy agents in other DNS domains.

CDSSO is an OpenAM-specific capability. For single sign-on across multiple organizations or when integrating with other access management software, use OpenAM’s federation capabilities. CDSSO requires stateful OpenAM sessions. Be sure that OpenAM is configured for stateful sessions—the default configuration—before attempting to use CDSSO.

Single sign-on depends on cookies to store session information. Yet for security reasons, browsers do not let a web site in one domain to get access to a cookie from another domain. With CDSSO, the policy agents work around this by negotiating with OpenAM to allow access.

The Java EE policy agent allows CDSSO by using a mechanism to write the SSO token from OpenAM authentication to a cookie with the domain the host where the agent runs. The following sequence diagram illustrates this mechanism.

![Image 1: cdsso jee sequence](https://doc.openidentityplatform.org/openam/_images/cdsso-jee-sequence.svg)

Whereas the Java EE policy agent has an endpoint specifically to handle the cookie domain translation, the web policy agent handles the request directly as shown in the following sequence diagram.

![Image 2: cdsso web sequence](https://doc.openidentityplatform.org/openam/_images/cdsso-web-sequence.svg)

This chapter includes the following procedures:

*   ["To Enable CDSSO For a Java EE Policy Agent"](https://doc.openidentityplatform.org/openam/admin-guide/chap-cdsso#enable-cdsso-jee-agent)

*   ["To Enable CDSSO For a Web Policy Agent"](https://doc.openidentityplatform.org/openam/admin-guide/chap-cdsso#enable-cdsso-web-agent)

*   ["To Indicate Progress During CDSSO Login"](https://doc.openidentityplatform.org/openam/admin-guide/chap-cdsso#show-cdsso-login-progress)

*   ["To Protect Against Cookie Hijacking"](https://doc.openidentityplatform.org/openam/admin-guide/chap-cdsso#enable-cdsso-cookie-hijacking-protection)

The federation mechanism associated with SAML v2.0 can be used as an alternative to CDSSO for both Web and Java EE policy agents. While using SAML v2.0 adds complexity, it supports attribute mapping, which may be useful when the two domains are associated with data stores that use different attribute names. For details, see ["Using Policy Agents With Standalone Mode"](https://doc.openidentityplatform.org/openam/admin-guide/chap-federation#using-saml2-with-policy-agents).

To Enable CDSSO For a Java EE Policy Agent

1.   In the OpenAM console, browse to Realms >_Realm Name_> Agents > J2EE >_Agent Name_> SSO.

2.   Scroll down and enable Cross Domain SSO.

3.   Check that the CDSSO Redirect URI is set.

Depending on where you deployed your Java EE agent application, the default is something like `/agentapp/sunwCDSSORedirectURI`.

4.   Set the list of URLs for CDSSO Servlet URL to the Cross Domain Controller Servlet URLs of the servers the agent accesses, such as `http://openam.example.com:8080/openam/cdcservlet`.

If the agent accesses OpenAM through a load balancer, use the load balancer URLs, such as `http://load-balancer.example.com:8080/openam/cdcservlet`.

5.   Leave the CDSSO Clock Skew set to 0.

Make sure instead that the clocks on the servers where you run OpenAM and policy agents are synchronized.

6.   Set the list of URLs for CDSSO Trusted ID Provider to the Cross Domain Controller Servlet URLs of the OpenAM servers the agent accesses, such `http://openam.example.com:8080/openam/cdcservlet`.

This list should include one CDC Servlet URL for every OpenAM server the agent might access. You do not need to include site or load balancer URLs.

7.   (Optional) To protect the SSO token from network snooping, you can select CDSSO Secure Enable to mark the SSO token cookie as secure.

If you select this, then the SSO token cookie can only be sent over a secure connection (HTTPS).

8.   Add the domains involved in CDSSO in the CDSSO Domain List.

9.   If necessary, update the Agent Root URL for CDSSO list on the Global tab page.

If the policy agent is on a server with virtual host names, add the virtual host URLs to the list.

If the policy agent is behind a load balancer, add the load balancer URL to the list.

10.   Save your work.

To Enable CDSSO For a Web Policy Agent

1.   In the OpenAM console, browse to Realms >_Realm Name_> Agents > Web >_Agent Name_> SSO.

2.   Enable Cross Domain SSO.

3.   Set the list of URLs for CDSSO Servlet URL to the Cross Domain Controller Servlet URLs of the servers the agent accesses, such as `http://openam.example.com:8080/openam/cdcservlet`.

If the agent accesses OpenAM through a load balancer, use the load balancer URLs, such as `http://load-balancer.example.com:8080/openam/cdcservlet`.

4.   Add the domains involved in CDSSO in the Cookies Domain List.

5.   If necessary, update the Agent Root URL for CDSSO list on the Global tab page.

If the policy agent is on a server with virtual host names, add the virtual host URLs to the list.

If the policy agent is behind a load balancer, add the load balancer URL to the list.

6.   Save your work.

To Indicate Progress During CDSSO Login

The default self-submitting form page that OpenAM presents to users contains hidden fields, but is otherwise blank. If you want to show users that the operation is in progress, then customize the necessary JSP.

1.   Edit a copy of the file `config/federation/default/cdclogin.jsp` to add a clue that SSO is in progress, such as an image.

You can find this file where you deployed OpenAM, such as `/path/to/tomcat/webapps/openam/config/federation/default/cdclogin.jsp`.

When you add an image or other presentation element, make sure that you retain the form and JavaScript as is.

2.   Unpack OpenAM-16.0.5.war, and replace the file with your modified version.

Also include any images you reference in the page.

3.   Pack up your custom version of OpenAM, and then deploy it in your web container.

To Access the CDSSO Authentication Login

When a client makes an access request to some protected resource in a cross domain single sign-on deployment, the policy agent redirects the client to the Cross Domain Controller Servlet (CDCServlet) URL. The CDCServlet determines that the client needs to be authenticated and proxies the request through to an authentication interface, which typically is at `/UI/Login`:

`http://openam.example.com:8080/openam/UI/Login`

If your application requires access to a specific URL, you can use the `loginURI` parameter to do so.

1.   For example, you can access the previous authentication UI URL as follows:

`http://openam.example.com:8080/openam/cdcservlet?loginURI=/UI/Login` 
2.   If you have another authentication UI deployed at `/openam/customLoginURI`, you can access this URL at:

`http://openam.example.com:8080/openam/cdcservlet?loginURI=/customLoginURI` 
In this case, you must also add the custom login URI to the whitelist that is specified by using the `org.forgerock.openam.cdc.validLoginURIs` property.

    1.   In the OpenAM console, navigate to Configure > Server Defaults > Advanced.

    2.   Set the value of the `org.forgerock.openam.cdc.validLoginURIs` property to `/UI/Login,/customLoginURI`.

    3.   Save your work.

For more information about this property, see ["Advanced"](https://doc.openidentityplatform.org/openam/reference/chap-config-ref#servers-advanced-configuration) in the _Reference_.

To Protect Against Cookie Hijacking

When cookies are set for an entire domain, such as `.example.com`, an attacker who steals a cookie can use it from any host in the domain, such as `untrusted.example.com`. Cookie hijacking protection restricts cookies to the fully-qualified domain name (FQDN) of the host where they are issued, such as `openam-server.example.com` and `server-with-agent.example.com`, using CDSSO to handle authentication and authorization.

For CDSSO with cookie hijacking protection, when a client successfully authenticates OpenAM issues the master SSO token cookie for its FQDN. OpenAM issues _restricted token_ cookies for the other FQDNs where the policy agents reside. The client ends up with cookies having different session identifiers for different FQDNs, and the OpenAM server stores the correlation between the master SSO token and restricted tokens, such that the client only has one master session internally in OpenAM.

To protect against cookie hijacking, you restrict the OpenAM server domain to the server where OpenAM runs. This sets the domain of the SSO token cookie to the host running the OpenAM server that issued the token. You also enable use of a unique SSO token cookie. For your Java EE policy agents, you enable use of the unique SSO token cookie in the agent configuration.

1.   In the OpenAM console, navigate to Configuration > Global Services > System, and then select Platform.

    1.   Remove all domains from the Cookies Domains list.

    2.   Save your work.

2.   Navigate to Configure > Server Defaults > Advanced.

    1.   Change the value of the `com.sun.identity.enableUniqueSSOTokenCookie` property to `true`, from the default `false`.

    2.   Make sure that the property `com.sun.identity.authentication.uniqueCookieName` is set to the name of the cookie that will hold the URL to the OpenAM server that authenticated the user.

The default name is `sunIdentityServerAuthNServer`.

    3.   Save your work.

3.   Navigate to Deployment > Servers >_Server Name_> Advanced, and add the property `com.sun.identity.authentication.uniqueCookieDomain`, setting the value to the FQDN of the current OpenAM server, such as `openam.example.com`.

Save your work.

4.   (Optional) For each Java EE policy agent, navigate to Realms >_Realm Name_> Agents > J2EE >_Agent Name_> Advanced > Custom Properties, and add the `com.sun.identity.enableUniqueSSOTokenCookie=true` property to the list.

Save your work.

5.   Restart OpenAM or the container in which it runs for the configuration changes to take effect.
