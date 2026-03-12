# Source: https://docs.pentaho.com/rest-api/authenticate-with-the-server-before-making-service-calls.md

# Authenticate with the Server Before Making Service Calls

The Pentaho Server has a configurable authentication system that authenticates clients that make web service calls. Out-of-the-box, there are two options available: Basic Authentication, also known as Basic-Auth and Cookie-Based Authentication.

#### Choosing an Authentication Option

**NOTE:** Since your system administrator might have implemented another authentication option such as a single sign-on option like CAS, contact your administrator to determine the best option for your installation.

**Use Cookie-Based Authentication** if the client making the web service requests supports cookies and will make more than one service call. Once a cookie is obtained it is reused for subsequent calls. This reduces the burden on the Authentication system and makes the server more efficient.

**Use Basic Authentication** if cookie support is not available or you're only making one call. Basic Authentication re-authenticates with every call made.

#### Cookie-Based Authentication

With cookie-based authentication, you set up your client to interact with the server in the same way a web browser does. You first obtain a cookie by calling the login URL. The cookie provided corresponds to a session on the server. Subsequent calls share the original authentication and reuse the same session until it expires.

**NOTE:** The following examples assume the server is deployed with pentaho as the web application name. If yours has been changed, adjust the URLs accordingly.

To obtain an authentication cookie, send a POST request to `/pentaho/j_spring_security_check` with the following request parameters:

* `j_username=[username]`
* `j_password=[password]`

Success is indicated by a 302 response that redirects to `/pentaho/Home`. Failure is indicated by a 302 response that redirects to `/pentaho/Login` with the parameter `login_error=1`.

#### Basic Authentication

The Pentaho Server supports Basic Authentication as defined in RFC 2617. Most HTTP tools and libraries support this natively; refer the documentation for your tool for the most appropriate and easiest usage. When using this authentication method, each call to the server must contain an Authorization HTTP Header with the value Basic and the Base64 encoded username and password separated by a colon (such as admin:password).

**Example Authorization Header:**

```
Authorization: Basic YWRtaW46cGFzc3dvcmQ=
```
