# Source: https://docs.pentaho.com/pdia-admin/administer/secure-the-pentaho-system/user-security/advanced-security-providers/server-side-request-forgery-prevention.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/user-security/advanced-security-providers/server-side-request-forgery-prevention.md

# Server-Side Request Forgery prevention

Malicious actors can use Server-Side Request Forgery (SSRF) for URL spoofing to map the internal network of the Pentaho Server and then perform possible network attacks. To prevent SSRF attempts against the Pentaho Server and its plugins, you must enable SSRF protection and create an allowed list of alternate fully qualified server URLs to be recognized by the application. Using this allowed list, the server only accepts HTTP requests from compatible host headers. Unlisted URLs are not acknowledged as valid by the server and the system responds with a 403 Forbidden status code.

## Preventing Server-Side Request Forgery

Perform the following steps to prevent SSRF attempts.

1. Stop the Pentaho Server if it is currently running.
2. Navigate to the `pentaho\server\pentaho-server\pentaho-solutions\system` directory.
3. Open the `system.properties` file with any text editor.
4. Locate the **ssrf-protection-enabled** element, which is set to false by default, and then set its value to true:

   \*\*ssrf-protection-enabled=\*\*true
5. Save and close the `system.properties` file.
6. Open the `server.properties` file using the text editor.
7. Locate the **alternative-fully-qualified-server-urls** element and then enter a comma-separated list of all the alternative fully qualified URLs containing the complete and exact location through which the servers can be reached in your environment:

   **alternative-fully-qualified-server-urls=**\<fully qualified URL>,\<fully qualified URL>,\<fully qualified URL>
8. Save and close the `server.properties` file.
9. Start the Pentaho Server.

The Pentaho Server is now configured to only allow fully qualified and alternate fully qualified server URLs to be recognized.
