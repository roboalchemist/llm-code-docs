# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/troubleshooting-overview-cp/security-issues/log-output-security-analysis.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/security-issues/log-output-security-analysis.md

# Log output security analysis

The following examples help to determine the location of security configuration issues in the `pentaho.log`:

* When you request a page that is protected, but you are not yet logged on, you should see an exception in the log which looks like the following text:

  ```
  DEBUG [ExceptionTranslationFilter] Access is denied (user is anonymous);
              redirecting to authentication entry point org.springframework.security.AccessDeniedException:
              Access is denied
  ```
* When the user name and/or password does not match what is stored in the back end, you should see a log message like the following text:

  ```
  WARN [LoggerListener] Authentication event
              AuthenticationFailureBadCredentialsEvent: suzy; details:
              org.springframework.security.ui.WebAuthenticationDetails@fffd148a: RemoteIpAddress: 127.0.0.1;
              SessionId: 976C95033136070E0200D6DA26CB0277; exception: Bad credentials
  ```
* When the user name and password match, you should see a log message that looks like the following example:

  ```
  WARN [LoggerListener] Authentication event InteractiveAuthenticationSuccessEvent:
              suzy; details: org.springframework.security.ui.WebAuthenticationDetails@fffd148a: RemoteIpAddress:
              127.0.0.1; SessionId: 976C95033136070E0200D6DA26CB0277 DEBUG
              [HttpSessionContextIntegrationFilter] SecurityContext stored to HttpSession:
              'org.springframework.security.context.SecurityContextImpl@2b86afeb: Authentication:
              org.springframework.security.providers.UsernamePasswordAuthenticationToken@2b86afeb: Username:
              org.springframework.security.userdetails.ldap.LdapUserDetailsImpl@d7f51e; Password: [PROTECTED];
              Authenticated: true; Details: org.springframework.security.ui.WebAuthenticationDetails@fffd148a:
              RemoteIpAddress: 127.0.0.1; SessionId: 976C95033136070E0200D6DA26CB0277; Granted
              Authorities: ROLE_CTO, ROLE_IS, ROLE_AUTHENTICATED'
  ```

After the `InteractiveAuthenticationSuccessEvent`, one of the filters will show the roles fetched for the authenticated user. Compare these roles to the page-role mapping found in the `filterInvocationInterceptor` bean in `applicationContext-spring-security.xml`.

If you are troubleshooting LDAP problems, look for log output similar to the following text:

```
DEBUG [DirMgrBindAuthenticator] (LoggingInterceptor) Return value: LdapUserInfo:
            org.springframework.security.providers.ldap.LdapUserInfo@1f31c64[dn=uid=suzy,ou=users,ou=system,attributes={mail=mail:
            suzy.pentaho@pentaho.org, uid=uid: suzy, userpassword=userpassword: [B@e17c9c,
            businesscategory=businesscategory: cn=cto,ou=roles,ou=system, cn=is,ou=roles,ou=system,
            objectclass=objectClass: organizationalPerson, person, groupOfUniqueNames,
            inetOrgPerson, top, uniquemember=uniquemember: cn=cto, ou=roles, cn = is , ou = roles,
            sn=sn: Pentaho, cn=cn: suzy}]
```
