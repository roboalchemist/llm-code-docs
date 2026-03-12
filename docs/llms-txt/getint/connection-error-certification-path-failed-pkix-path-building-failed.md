# Source: https://docs.getint.io/support-legal-and-others/troubleshooting-guide-for-getint-users/connection-error-certification-path-failed-pkix-path-building-failed.md

# Connection Error: Certification Path Failed/PKIX Path Building Failed

This error might appear if Getint isn’t able to find a valid certification path to create a connection.

{% hint style="warning" %}
Please note that this issue is outside the scope of Getint support and is not specific to Getint software. It is related to the certificates used in your connections.
{% endhint %}

### Issue: Connectivity Issues between Getint (On-Premise Version) and Other Tools

Connection issues with other tools such as ServiceNow and Azure DevOps arise after replacing an expired SSL certificate. The following error message is displayed: Request failed with status code 500. PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target

The problem occurs when an on-premise server uses a self-signed certificate. As a workaround, add this certificate to the list of trusted certificates in your JVM. You can either:

1. Edit the JAVA\_HOME/jre/lib/security/cacerts file.
2. Run your application with the -Djavax.net.ssl.trustStore parameter.

Make sure to verify which JDK/JRE you are using, as this is often a source of confusion.

### Additional Tips

* **Ensure Proper Certificate Chain**: Ensure that the certificate chain is complete and correctly installed on the server to avoid similar issues in the future.
* **Regularly Update Certificates**: Schedule regular updates and replacements of SSL certificates to prevent disruptions.
* **Consult Documentation**: Refer to your JVM’s and server's documentation for detailed instructions on managing certificates.

Atlassian also provides a guide on resolving this issue, which you can access here: [Unable to Connect to SSL Services Due to PKIX Path Building Failed Error](https://confluence.atlassian.com/kb/unable-to-connect-to-ssl-services-due-to-pkix-path-building-failed-error-779355358.html).

If you have any further questions or need assistance with other issues, feel free to contact our [Support Team](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FHecEC9W2epQwYsz7yXQh%2FGetint%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=2073bde2-3980-46c4-9272-e72c21655b11" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues to build your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>
