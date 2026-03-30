# Source: https://docs.pentaho.com/pdia-admin/administer/secure-the-pentaho-system/user-security/advanced-security-providers/ldap-security.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/secure-the-pentaho-system/user-security/advanced-security-providers/ldap-security.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/user-security/advanced-security-providers/ldap-security.md

# LDAP security

To use Lightweight Directory Access Protocol (LDAP) for user security, you must switch from the default Pentaho security to LDAP, then you must configure LDAP.

## Switch to LDAP

To connect to your LDAP server, you must import the certificate into the JRE's truststore/keystore used by the Pentaho Server (`java/lib/security/cacerts`).

1. From the User Console **Home** menu, click **Administration**, then select **Authentication** from the left.

   The **Authentication** interface appears. **Local - Use basic Pentaho Authentication** is selected by default.
2. Select the **External - Use LDAP / Active Directory server** option.

   ![User console authentication set to external](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-b3f42c7848155e09726e6db54a39cc6f88e20208%2FPUC_Admin_UserSecurity_LDAP_ssLDAPoptions.png?alt=media)

   The **LDAP Server Connection** fields populate with a default URL, user name, and password.
3. Change the **Server URL**, **User Name**, and **Password** as needed.
4. Click **Test Server Connection** to verify the connection to your LDAP server and to complete the set up.
5. Click the node to select the **Pentaho System Administrator** user and role to match your LDAP configuration, then click **OK**.

   **Note:** The Admin user is required for all system-related operations, including the creation of user folders. The Administrator Role is required for mapping a third-party admin role to the Pentaho admin role (Administrator).
6. Select your **LDAP Provider** from the drop-down menu.
7. Configure the LDAP connection as explained in [LDAP properties](#ldap-properties).
8. Stop the Pentaho Server.

   See the **Install Pentaho Data Integration and Analytics** document for instructions on starting and stopping the Pentaho Server.
9. Delete the `server/pentaho-server/pentaho-solutions/system/karaf/caches` folder.
10. Restart the Pentaho Server and test the LDAP functionality.

    See the **Install Pentaho Data Integration and Analytics** document for instructions on starting and stopping the Pentaho Server.

The Pentaho Server is now configured to authenticate users against your LDAP directory server.

## Manual configuration

You must have a working LDAP server with an established configuration before continuing. Follow the instructions below to manually switch from Pentaho default security to LDAP security.

1. Stop the Pentaho Server.
2. Edit the `security.properties` file located in the `server/pentaho-server/pentaho-solutions/system` folder.
   1. Change **provider=jackrabbit** to **provider=ldap**
   2. Save and close the file.
3. Edit the `server/pentaho-server/pentaho-solutions/system/applicationContext-security-ldap.properties` file.
   1. Modify the settings to match your LDAP configuration.

      ```

      userSearch.searchBase=OU\=YourDomainCustomerCareUsers,DC\=YourDomainCustomerCare,DC\=com
      allAuthoritiesSearch.roleAttribute=cn
      allAuthoritiesSearch.searchBase=OU\=YourDomainCustomerCareGroups,DC\=YourDomainCustomerCare,DC\=com
      userSearch.searchFilter=(sAMAccountName\={0})
      allUsernamesSearch.searchFilter=objectClass\=Person
      allAuthoritiesSearch.searchFilter= (objectClass\=group)
      providerType=ldapCustomConfiguration
      contextSource.userDn=youradminUser@YourDomaincustomercare.com
      populator.rolePrefix=
      allUsernamesSearch.searchBase=OU\=YourDomainCustomerCareUsers,DC\=YourDomainCustomerCare,DC\=com
      adminUser=CN\=YourAdminUserDN,OU\=OrlandoFL,OU\=NAMER,OU\=Support,OU\=YourDomainCustomerCareUsers,DC\=YourDomainCustomerCare,DC\=com
      adminRole=CN\=YourAdminRole,OU\=YourDomainCustomerCareGroups,DC\=YourDomainCustomerCare,DC\=com
      populator.groupSearchBase=OU\=YourDomainCustomerCareGroups,DC\=YourDomainCustomerCare,DC\=com
      populator.convertToUpperCase=false
      populator.searchSubtree=false
      allUsernamesSearch.usernameAttribute=sAMAccountName
      populator.groupRoleAttribute=cn
      contextSource.providerUrl=ldap\://10.100.7.17\:389
      contextSource.password=********
      populator.groupSearchFilter=(member\={0})

      ```
   2. Save and close the file.
4. Edit the `server/pentaho-server/pentaho-solutions/system/repository.spring.properties` file.
   1. Replace *admin* in the following line: `singleTenanatAdminUserName=admin` with the value of the **adminUser’s***sAMAccountName* as defined in the `applicationContext-security-ldap.properties` file.
   2. Save and close the file.
5. Delete the following directory: `server/pentaho-server/pentaho-solutions/system/jackrabbit/repository`

   **CAUTION:**

   Do not delete the `repository.xml` file, which is also located in the following directory: `server/pentaho-server/pentaho-solutions/system/jackrabbit`
6. Delete the `server/pentaho-server/pentaho-solutions/system/karaf/caches` folder.
7. Restart the Pentaho Server and test the LDAP functionality.

The Pentaho Server is now configured to authenticate users against your directory server. The [LDAP properties](#ldap-properties) reference article contains supplemental information for LDAP values.

## Configure LDAP security caching

If you are using Lightweight Directory Access Protocol (LDAP) security for your Pentaho environment, the Pentaho Data Integration and Analytics products actively communicate with your LDAP server. Configuring Pentaho to cache access to your LDAP server could improve access speed for this active communication.

To configure Pentaho to cache LDAP security communication, you must update Pentaho spring security to initialize caching, associate the spring security caching with LDAP, then configure the properties of the cache. Perform the following steps to configure Pentaho for LDAP security caching.

1. Open the `pentaho-server/pentaho-solutions/system/applicationContext-spring-security-ldap.xml` file with a text editor.
2. Change `authenticator` to `cachingAuthenticator` and `populator` to `cachingPopulator` in the `ldapAuthenticationProvider` bean entry to initialize caching, as shown in the following example:

   ```xml
   <bean id="ldapAuthenticationProvider" class="org.pentaho.platform.plugin.services.security.userrole.ldap.DefaultLdapAuthenticationProvider">
     <constructor-arg>
       <ref bean="cachingAuthenticator" />
     </constructor-arg>
     <constructor-arg>
       <ref bean="cachingPopulator" />
     </constructor-arg>
     <constructor-arg>
       <ref bean="ldapRoleMapper" />
     </constructor-arg>
   </bean>

   ```
3. Verify the following `constructor` entries are commented out in the `applicationContext-spring-security-ldap.xml` file:

   ```xml
   <bean id="cachingAuthenticator" class="org.pentaho.platform.plugin.services.security.userrole.ldap.PentahoCachingLdapAuthenticator">
   	<constructor-arg ref="authenticator" />
   	<property name="cacheRegionName" value="ldapAuthenticatorCache" />
   	<property name="passwordHashMethod" value="SHA-256" />
   </bean>

   <bean id="cachingPopulator" class="org.pentaho.platform.plugin.services.security.userrole.ldap.PentahoCachingLdapAuthoritiesPopulator">
   	<constructor-arg ref="populator" />
   	<property name="cacheRegionName" value="ldapPopulatorCache" />
   </bean>

   ```
4. Uncomment the `constructor` entries or add them if they do not appear in the `applicationContext-spring-security-ldap.xml` file to associate the spring security caching with LDAP.
5. Save and close the `applicationContext-spring-security-ldap.xml` file.
6. Open the `pentaho-server/tomcat/webapp/WEB-INF/classes/ehcache.xml` file with a text editor.
7. Verify the following `cache` entries are commented out in the `pentaho-server/tomcat/webapp/WEB-INF/classes/ehcache.xml` file:

   ```xml
   <cache 
   name="ldapPopulatorCache" 
   maxEntriesLocalHeap="2000" 
   eternal="false" 
   overflowToDisk="false" 
   timeToIdleSeconds="300" 
   timeToLiveSeconds="600" 
   diskPersistent="false"/>

   <cache 
   name="ldapAuthenticatorCache" 
   maxEntriesLocalHeap="2000" 
   eternal="false" 
   overflowToDisk="false" 
   timeToIdleSeconds="300" 
   timeToLiveSeconds="600" 
   diskPersistent="false"/>

   ```
8. Uncomment the `cache` entries or add them if they do not appear in the `pentaho-server/tomcat/webapp/WEB-INF/classes/ehcache.xml` file to configure the properties of the cache.
9. Save and close the `applicationContext-spring-security-ldap.xml` file.

Your LDAP server connection to Pentaho Data Integration and Analytics is now cached.

## Chain LDAP servers

You can chain multiple LDAP servers together for authentication and authorization of your users. You may want to implement chained servers if you::

* Have one or more LDAP Servers for your organization
* Need a failover LDAP server
* Have multiple domains within an LDAP Server

To chain your LDAP servers, you must configure your setup by editing existing files, creating configuration files, and then finalize the process. This process requires the following steps:

* [Step 1: Configure the authentication manager](#step-1-configure-the-authentication-manager)
* [Step 2: Configure the your users and roles](#step-2-configure-users-and-roles)
* [Step 3: Create a spring security application context file](#step-3-create-a-spring-security-application-context-file)
* [Step 4: Create Pentaho security application context file](#step-4-create-pentaho-security-application-context-file)
* [Step 5: Create a properties file for the ldapProvider](#step-5-create-a-properties-file-for-the-ldapprovider)
* [Step 6: Apply your new files](#step-6-apply-your-new-files)
* [Step 7: Complete the configuration process](#step-7-complete-the-configuration-process)

Before you begin, you must stop the server if it is running before proceeding. You must also use the same `providerName` in all the configuration files below.

### Step 1: Configure the authentication manager

Perform the following steps to configure the authentication manager:

1. Navigate to the `server/pentaho-server/pentaho-solutions/system/` directory.
2. Open the `applicationContext-spring-security.xml` file in any text editor.
3. Locate the `authenticationManager` bean tags and add the following AuthenticationProvider code in the list tag, replacing `ldapProviderName` with your `providerName`:

   ```xml
   <pen:bean class="org.springframework.security.authentication.AuthenticationProvider">
   	<pen:attributes>
   		<pen:attr key="providerName" value="<ldapProviderName>"/>
   	</pen:attributes>
   </pen:bean>

   ```

   After adding the above bean, your authentication manager code will look like the following example code where `ldapProviderName` is replaced with with your `providerName`:

   ```xml
   <bean id="authenticationManager" class="org.springframework.security.authentication.ProviderManager">
   	<constructor-arg>
   		<util:list>
   			<pen:bean class="org.springframework.security.authentication.AuthenticationProvider"/>
   			<ref bean="anonymousAuthenticationProvider"/>
   			<pen:bean class="org.springframework.security.authentication.AuthenticationProvider">
   				<pen:attributes>
   					<pen:attr key="providerName" value="<ldapProviderName>"/>
   				</pen:attributes>
   			</pen:bean>
   		</util:list>
   	</constructor-arg>
   	<property name="authenticationEventPublisher" ref="defaultAuthenticationEventPublisher"/>
   </bean>

   ```
4. Save and close the file.

### Step 2: Configure users and roles

Perform the following steps to configure the your users and roles.

1. Navigate to the `server/pentaho-server/pentaho-solutions/system` directory.
2. Open the `pentahoObjects.spring.xml` file in any text editor.
3. Locate the `activeUserRoleListService` definition beans tag and add the following`UserRoleListService` beans beneath the `activeUserRoleListService` ending tag, replacing `ldapProviderName` with your `providerName` as shown in the following example:

   ```xml
   <pen:bean id="<ldapProviderName>_activeUserRoleListService" class="org.pentaho.platform.api.engine.IUserRoleListService">
   	<pen:attributes>
   		<pen:attr key="providerName" value="<ldapProviderName>"/>
   		</pen:attributes>
   </pen:bean>

   ```
4. Locate the `IUserRoleListService` definition beans tag and add the newly added bean ID after the list tag with ref bean attribute.
5. Add the following property after the constructor tag:

   ```xml
   <property name="strategy">
   	<value type="org.pentaho.platform.plugin.services.security.userrole.CompositeUserRoleListService.STRATEGY">ADDITIVE</value>
   </property>

   ```

   After adding the above reference bean and property, your `IUserRoleListService` code will look like the following example code where `ldapProviderName` is replaced with with your `providerName`:

   ```xml
   <!-- A composite bean composed of the activeUserRoleListService and systemUserRoleListService -->
   <bean id="IUserRoleListService" class="org.pentaho.platform.plugin.services.security.userrole.CompositeUserRoleListService">
   	<constructor-arg>
   		<list>
   			<ref bean="<ldapProviderName>_activeUserRoleListService"/>
   			<ref bean="activeUserRoleListService"/>
   			<ref bean="systemUserRoleListService"/>
   		</list>
   	</constructor-arg>
   	<property name="strategy">
   		<value type="org.pentaho.platform.plugin.services.security.userrole.CompositeUserRoleListService.STRATEGY">ADDITIVE</value>
   	</property>
   	<pen:publish as-type="INTERFACES">
   		<pen:attributes>
   			<pen:attr key="priority" value="50"/>
   		</pen:attributes>
   	</pen:publish>
   </bean>

   ```
6. Locate the `activeUserDetailsServic`e bean tags and add the following `ldapProviderName_activeUserDetailsService` after the `activeUserDetailsService`end tag, replacing `ldapProviderName` with your `providerName`:

   ```xml
   <pen:bean id="<ldapProviderName>_activeUserDetailsService" class="org.springframework.security.core.userdetails.UserDetailsService">
                 <pen:attributes>
                          <pen:attr key="providerName" value="<ldapProviderName>"/>
                  </pen:attributes>
   </pen:bean>

   ```
7. Locate the `UserDetailsService` definition beans tag and add the newly added bean ID after the list tag with reference bean attribute

   After adding the above reference bean, your `UserDetailsService` code will look like the following example code where `ldapProviderName` is replaced with with your `providerName`

   ```xml
   <!-- A composite bean composed of the activeUserDetailsService and systemUserDetailsService -->
   <bean id="UserDetailsService" class="org.pentaho.platform.plugin.services.security.userrole.ChainedUserDetailsService">
   	<constructor-arg>
   		<list>
   			<ref bean="<ldapProviderName>_activeUserDetailsService"/>
   			<ref bean="activeUserDetailsService"/>
   			<ref bean="systemUserDetailsService"/>
   		</list>
   	</constructor-arg>
   </bean>

   ```
8. Save and close the file.

### Step 3: Create a spring security application context file

Perform the following steps to create a spring security application context file:

1. Create a LDAP Spring security `applicationContext` file using the following example code, replacing all occurrences of `ldapProviderName` with your `providerName`:

   ```xml
   <beans xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:pen="http://www.pentaho.com/schema/pentaho-system" xmlns:util="http://www.springframework.org/schema/util" xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-4.3.xsd
   	http://www.pentaho.com/schema/pentaho-system http://www.pentaho.com/schema/pentaho-system.xsd
   	http://www.springframework.org/schema/util http://www.springframework.org/schema/util/spring-util-4.3.xsd" default-lazy-init="true">
   	<bean id="<ldapProviderName>_ldapAuthenticationProvider" class="org.pentaho.platform.plugin.services.security.userrole.ldap.DefaultLdapAuthenticationProvider">
   		<constructor-arg>
   			<ref bean="<ldapProviderName>_authenticator"/>
   		</constructor-arg>
   		<constructor-arg>
   			<ref bean="<ldapProviderName>_populator"/>
   		</constructor-arg>
   		<constructor-arg>
   			<ref bean="<ldapProviderName>_ldapRoleMapper"/>
   		</constructor-arg>
   	</bean>
   	<!-- Interceptor which changes the thread context classloader to the class' current classloader.-->
   	<bean id="<ldapProviderName>_classloaderSwitcherInterceptor" class="org.pentaho.platform.plugin.services.security.userrole.ClassloaderSwitcherInterceptor">
    </bean>
   	<bean id="<ldapProviderName>_ldapAuthenticationProviderProxy" class="org.springframework.aop.framework.ProxyFactoryBean">
   		<property name="proxyInterfaces" value="org.springframework.security.authentication.AuthenticationProvider"/>
   		<property name="target" ref="<ldapProviderName>_ldapAuthenticationProvider"/>
   		<property name="interceptorNames">
   			<list>
   				<value><ldapProviderName>_classloaderSwitcherInterceptor</value>
   				</list>
   			</property>
   			<pen:publish as-type="org.springframework.security.authentication.AuthenticationProvider">
   				<pen:attributes>
   					<pen:attr key="providerName" value="<ldapProviderName>"/>
   				</pen:attributes>
   			</pen:publish>
   		</bean>
   	<bean id="<ldapProviderName>_authenticator" class="org.springframework.security.ldap.authentication.BindAuthenticator">
   		<constructor-arg>
   			<ref bean="<ldapProviderName>_contextSource"/>
   		</constructor-arg>
   		<property name="userSearch">
   			<ref bean="<ldapProviderName>_userSearch"/>
   		</property>
   	</bean>
   <!-- Uncomment below and update ldapAuthenticationProvider to enable local caching of LDAP credentials; reduces LDAP traffic when running numerous spoon/pan/kitchen jobs against a repository. -->
   <!--
   <bean id="cachingAuthenticator"
    class="org.pentaho.platform.plugin.services.security.userrole.ldap.PentahoCachingLdapAuthenticator">
    <constructor-arg ref="authenticator" />
    <property name="cacheRegionName" value="ldapAuthenticatorCache" />
    <property name="passwordHashMethod" value="SHA-256" />
   </bean>
   -->
   	<bean id="<ldapProviderName>_contextSource" class="org.springframework.security.ldap.DefaultSpringSecurityContextSource">
   		<constructor-arg value="${<ldapProviderName>.contextSource.providerUrl}"/>
   		<property name="userDn" value="${<ldapProviderName>.contextSource.userDn}"/>
   		<property name="password" value="${<ldapProviderName>.contextSource.password}"/>
   	</bean>
   	<!-- be sure to escape ampersands -->
   	<bean id="<ldapProviderName>_userSearch" class="org.springframework.security.ldap.search.FilterBasedLdapUserSearch">
   		<constructor-arg index="0" value="${<ldapProviderName>.userSearch.searchBase}"/>
   		<constructor-arg index="1" value="${<ldapProviderName>.userSearch.searchFilter}"/>
   		<constructor-arg index="2">
   			<ref bean="<ldapProviderName>_contextSource"/>
   		</constructor-arg>
   	</bean>
   	<!-- be sure to escape ampersands -->
   	<bean id="<ldapProviderName>_populator" class="org.springframework.security.ldap.userdetails.DefaultLdapAuthoritiesPopulator">
   		<constructor-arg index="0">
   			<ref bean="<ldapProviderName>_contextSource"/>
   		</constructor-arg>
   		<constructor-arg index="1" value="${<ldapProviderName>.populator.groupSearchBase}"/>
   		<property name="groupRoleAttribute" value="${<ldapProviderName>.populator.groupRoleAttribute}"/>
   		<!-- {0} will be replaced with user DN; {1} will be replaced with username -->
   		<property name="groupSearchFilter" value="${<ldapProviderName>.populator.groupSearchFilter}"/>
   		<property name="rolePrefix" value="${<ldapProviderName>.populator.rolePrefix}"/>
   		<property name="convertToUpperCase" value="${<ldapProviderName>.populator.convertToUpperCase}"/>
   		<property name="searchSubtree" value="${<ldapProviderName>.populator.searchSubtree}"/>
   		<property name="defaultRole" ref="defaultRole"/>
   	</bean>
   <!-- Uncomment below and update ldapAuthenticationProvider to enable local caching of LDAP credentials; reduces LDAP
   traffic when running numerous spoon/pan/kitchen jobs against a repository. -->
   <!--
    <bean id="cachingPopulator"
    class="org.pentaho.platform.plugin.services.security.userrole.ldap.PentahoCachingLdapAuthoritiesPopulator">
    <constructor-arg ref="populator" />
    <property name="cacheRegionName" value="ldapPopulatorCache" />
    </bean> -->
   	<bean id="<ldapProviderName>_ldapUserDetailsService0" class="org.pentaho.platform.plugin.services.security.userrole.ldap.DefaultLdapUserDetailsService">
   		<constructor-arg>
   			<ref bean="<ldapProviderName>_userSearch"/>
   		</constructor-arg>
   		<constructor-arg>
   			<ref bean="<ldapProviderName>_populator"/>
   		</constructor-arg>
   		<constructor-arg ref="tenantedUserNameUtils"/>
   	</bean>
   	<bean id="<ldapProviderName>_ldapUserDetailsServiceProxy" class="org.springframework.aop.framework.ProxyFactoryBean">
   		<property name="proxyInterfaces" value="org.springframework.security.core.userdetails.UserDetailsService"/>
   		<property name="target" ref="<ldapProviderName>_ldapUserDetailsService0"/>
   		<property name="interceptorNames">
   			<list>
   				<value><ldapProviderName>_classloaderSwitcherInterceptor</value>
   			</list>
   			</property>
   	</bean>
   		<!-- map LDAP role to pentaho security role -->
   		<util:map id="<ldapProviderName>_ldapRoleMap">
   			<entry key="${<ldapProviderName>.adminRole}" value="Administrator"/>
   		</util:map>
   	<bean id="<ldapProviderName>_ldapRoleMapper" class="org.pentaho.platform.engine.security.DefaultLdapRoleMapper">
   		<constructor-arg>
   			<ref bean="<ldapProviderName>_ldapRoleMap"/>
   		</constructor-arg>
   		<constructor-arg value="${<ldapProviderName>.allAuthoritiesSearch.roleAttribute}"/>
   	</bean>
   	<bean id="<ldapProviderName>_ldapUserDetailsService" class="org.pentaho.platform.engine.security.DefaultRoleUserDetailsServiceDecorator">
   		<property name="userDetailsService" ref="<ldapProviderName>_ldapUserDetailsServiceProxy"/>
   		<property name="defaultRole" ref="defaultRole"/>
   		<property name="roleMapper" ref="<ldapProviderName>_ldapRoleMapper"/>
   		<pen:publish as-type="INTERFACES">
   			<pen:attributes>
   				<pen:attr key="providerName" value="<ldapProviderName>"/>
   			</pen:attributes>
   		</pen:publish>
   	</bean>
   	<bean class="org.pentaho.platform.config.SolutionPropertiesFileConfiguration">
   		<constructor-arg value="<ldapProviderName>"/>
   		<constructor-arg value="applicationContext-security-<ldapProviderName>.properties"/>
   		<pen:publish as-type="INTERFACES"/>
   	</bean>
   </beans>

   ```
2. Save the filename as `applicationContext-spring-security-<ldapProviderName>.xml` where `ldapProviderName` is your `providerName` in the `/pentaho-solutions/system` directory.

### Step 4: Create Pentaho security application context file

Perform the following steps to create a Pentaho security application context file:

1. Copy the following example code into a file, replacing all the occurrences of `ldapProviderName` with your `providerName:`

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!--+
   	| Application context containing LDAP UserRoleListService
   	| implementation.
   	+-->
   <beans xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

          xmlns:pen="http://www.pentaho.com/schema/pentaho-system"
          xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-4.3.xsd http://www.pentaho.com/schema/pentaho-system http://www.pentaho.com/schema/pentaho-system.xsd" default-lazy-init="true">

     <!-- be sure to escape ampersands -->
     <bean id="ldapProviderName_allUsernamesSearch"
           class="org.pentaho.platform.plugin.services.security.userrole.ldap.search.GenericLdapSearch">
       <constructor-arg index="0" ref="ldapProviderName_contextSource" />
       <constructor-arg index="1">
         <bean
             class="org.pentaho.platform.plugin.services.security.userrole.ldap.search.LdapSearchParamsFactoryImpl">
           <constructor-arg index="0" value="${ldapProviderName.allUsernamesSearch.searchBase}" />
           <constructor-arg index="1" value="${ldapProviderName.allUsernamesSearch.searchFilter}" />
         </bean>
       </constructor-arg>
       <constructor-arg index="2">
         <bean
             class="org.pentaho.platform.plugin.services.security.userrole.ldap.transform.SearchResultToAttrValueList">
           <constructor-arg index="0" value="${ldapProviderName.allUsernamesSearch.usernameAttribute}" />
         </bean>
       </constructor-arg>
     </bean>

     <!-- be sure to escape ampersands -->
     <bean id="ldapProviderName_allAuthoritiesSearch"
           class="org.pentaho.platform.plugin.services.security.userrole.ldap.search.GenericLdapSearch">
       <constructor-arg index="0" ref="ldapProviderName_contextSource" />
       <constructor-arg index="1">
         <bean
             class="org.pentaho.platform.plugin.services.security.userrole.ldap.search.LdapSearchParamsFactoryImpl">
           <constructor-arg index="0" value="${ldapProviderName.allAuthoritiesSearch.searchBase}" />
           <constructor-arg index="1"
                            value="${ldapProviderName.allAuthoritiesSearch.searchFilter}" />
         </bean>
       </constructor-arg>
       <constructor-arg index="2">
         <bean
             class="org.apache.commons.collections.functors.ChainedTransformer">
           <constructor-arg index="0">
             <list>
               <bean
                   class="org.pentaho.platform.plugin.services.security.userrole.ldap.transform.SearchResultToAttrValueList">
                 <constructor-arg index="0" value="${ldapProviderName.allAuthoritiesSearch.roleAttribute}" />
               </bean>
               <bean
                   class="org.pentaho.platform.plugin.services.security.userrole.ldap.transform.StringToGrantedAuthority">
                 <property name="rolePrefix" value="${ldapProviderName.populator.rolePrefix}" />
                 <property name="convertToUpperCase" value="${ldapProviderName.populator.convertToUpperCase}" />
               </bean>
             </list>
           </constructor-arg>
         </bean>
       </constructor-arg>
     </bean>

     <!-- not currently used -->
     <bean id="ldapProviderName_usernamesInRoleSearch"
           class="org.pentaho.platform.plugin.services.security.userrole.ldap.search.NoOpLdapSearch">
     </bean>

     <bean id="ldapProviderName_ldapUserRoleListService"
           class="org.pentaho.platform.plugin.services.security.userrole.ldap.DefaultLdapUserRoleListService">
       <constructor-arg index="0" >
         <bean class="org.pentaho.platform.engine.security.DefaultUsernameComparator" />
       </constructor-arg>
       <constructor-arg index="1" >
         <bean class="org.pentaho.platform.engine.security.DefaultRoleComparator" />
       </constructor-arg>
       <constructor-arg index="2">
         <ref bean="ldapProviderName_ldapRoleMapper" />
       </constructor-arg>
       <property name="allAuthoritiesSearch">
         <ref bean="ldapProviderName_allAuthoritiesSearch" />
       </property>
       <property name="allUsernamesSearch">
         <ref bean="ldapProviderName_allUsernamesSearch" />
       </property>
       <property name="userDetailsService">
       	<pen:bean class="org.springframework.security.core.userdetails.UserDetailsService"/>
       </property>
       <property name="usernamesInRoleSearch">
         <ref bean="ldapProviderName_usernamesInRoleSearch" />
       </property>
       <property name="roleNameUtils" >
         <ref bean="tenantedRoleNameUtils" />
       </property>
       <property name="userNameUtils">
         <ref bean="tenantedUserNameUtils" />
       </property>
       <property name="systemRoles" >
         <ref bean="singleTenantSystemAuthorities" />
       </property>
       <property name="extraRoles" ref="extraRoles" />
       <pen:publish as-type="INTERFACES">
         <pen:attributes>
           <pen:attr key="providerName" value="ldapProviderName"/>
         </pen:attributes>
       </pen:publish>    
     </bean>
   </beans>

   ```
2. Save the file as `applicationContext-pentaho-security-<ldapProviderName>.xml` in the `pentaho-solutions/system` directory where `ldapProviderName` is your `providerName`.

### Step 5: Create a properties file for the ldapProvider

Perform the following steps to create an `ldapProvider` properties file:

1. Copy the following example code into any text editor and save it in the `server/pentaho-server/pentaho-solutions/system` directory as the `applicationContext-security-<ldapProviderName>.properties` file where `ldapProviderName` is your `providerName`.

   ```
   userSearch.searchBase=OU\=YourDomainCustomerCareUsers,DC\=YourDomainCustomerCare,DC\=com
   allAuthoritiesSearch.roleAttribute=cn
   allAuthoritiesSearch.searchBase=OU\=YourDomainCustomerCareGroups,DC\=YourDomainCustomerCare,DC\=com
   userSearch.searchFilter=(sAMAccountName\={0})
   allUsernamesSearch.searchFilter=objectClass\=Person
   allAuthoritiesSearch.searchFilter= (objectClass\=group)
   providerType=ldapCustomConfiguration
   contextSource.userDn=youradminUser@YourDomaincustomercare.com
   populator.rolePrefix=
   allUsernamesSearch.searchBase=OU\=YourDomainCustomerCareUsers,DC\=YourDomainCustomerCare,DC\=com
   adminUser=CN\=YourAdminUserDN,OU\=OrlandoFL,OU\=NAMER,OU\=Support,OU\=YourDomainCustomerCareUsers,DC\=YourDomainCustomerCare,DC\=com
   adminRole=CN\=YourAdminRole,OU\=YourDomainCustomerCareGroups,DC\=YourDomainCustomerCare,DC\=com
   populator.groupSearchBase=OU\=YourDomainCustomerCareGroups,DC\=YourDomainCustomerCare,DC\=com
   populator.convertToUpperCase=false
   populator.searchSubtree=false
   allUsernamesSearch.usernameAttribute=sAMAccountName
   populator.groupRoleAttribute=cn
   contextSource.providerUrl=ldap\://10.100.7.17\:389
   contextSource.password=********
   populator.groupSearchFilter=(member\={0})

   ```
2. Modify any variables that pertain to your environment.
3. Save and close the file.

### Step 6: Apply your new files

Perform the following steps to apply the newly created files:

1. Navigate to the `server/pentaho-server/pentaho-solutions/system` directory.
2. Open the `pentaho-spring-beans.xml` file with any text editor.
3. Search for the `<import resource="applicationContext-pentaho-security-ldap.xml" />` element and add the following lines after it:

   ```xml
   <import resource="applicationContext-spring-security-ldapProviderName.xml" />  
   <import resource="applicationContext-pentaho-security-<ldapProviderName>.xml" />

   ```
4. Save and close the file.

### Step 7: Complete the configuration process

Perform the following step to complete the configuration process:

1. Delete the `server/pentaho-server/pentaho-solutions/system/jackrabbit/repository` directory.
2. Delete the `server/pentaho-server/pentaho-solutions/system/karaf/caches` directory.
3. Restart the server.

   **CAUTION:**

   Do not delete the `repository.xml` file in the `server/pentaho-server/pentaho-solutions/system/jackrabbit` directory.

If you want to configure another LDAP configuration, repeat all the steps using a different `providerName`.

## Use nested roles

It is possible to nest user roles such that one role includes all of the users of another role. Doing this external to the core LDAP structure prevents recursive directory queries to find all parents of a given child role. Follow the directions below to modify the Pentaho Server to support nested roles for LDAP and MSAD authentication types.

1. Stop the Pentaho Server or service.

   ```
   sh /usr/local/pentaho/server/pentaho-server/stop-pentaho.sh
   ```
2. Open the `/pentaho/server/pentaho-server/pentaho-solutions/system/applicationContext-spring-security-ldap.xml` file with a text editor.
3. In the `populator` bean definition, replace **DefaultLdapAuthoritiesPopulator** with: **NestedLdapAuthoritiesPopulator**

   ```xml
   <bean id="populator" class="org.pentaho.platform.plugin.services.security.userrole.ldap.NestedLdapAuthoritiesPopulator">
   ```
4. Save the file, then edit `/pentaho/server/pentaho-server/pentaho-solutions/system/applicationContext-pentaho-security-ldap.xml`.

   This and the next step are only necessary if the roles that serve as "parents" to nested roles cannot be returned by a traditional all authorities search.
5. Add an `extraRoles` bean to the list of transformers in the `ChainedTransformers` bean, and set properties for each parent role (represented by **example\_role** below).

   ```xml
   <bean id="allAuthoritiesSearch" class="org.pentaho.platform.plugin.services​.security.userrole.ldap.search.GenericLdapSearch">
       <!-- omitted -->
       <constructor-arg index="2">
           <bean class="org.apache.commons.collections.functors.ChainedTransformer">
               <constructor-arg index="0">
                   <list>
                       <bean class="org.pentaho.platform.plugin.services.security.​userrole.ldap.transform.SearchResultToAttrValueList">
                           <!-- omitted -->
                       </bean>
                       <bean class="org.pentaho.platform.plugin.services.security.userrole.​ldap.transform.ExtraRoles">
                           <property name="extraRoles">
                               <set>
                                   <value>example_role</value>
                               </set>
                           </property>
                       </bean>
                       <bean class="org.pentaho.platform.plugin.services.security.​userrole.ldap.transform.StringToGrantedAuthority">
                           <!-- omitted -->
                       </bean>
                   </list>
               </constructor-arg>
           </bean>
       </constructor-arg>
   </bean>
   ```
6. Save the file, close your text editor, and start the Pentaho Server.

   ```
   sh /usr/local/pentaho/server/pentaho-server/start-pentaho.sh
   ```

The Pentaho Server can now handle nested roles with LDAP or Active Directory authentication.

## LDAP properties

You can configure LDAP values by editing the `/pentaho-solutions/system/applicationContext-security-ldap.properties` file in your Pentaho Server folder.

### Connection information (context)

These entries define connections involving LDAP users (typically administrators) that can execute folder searches.

| LDAP Property                  | Purpose                                                    | Example                                                                |
| ------------------------------ | ---------------------------------------------------------- | ---------------------------------------------------------------------- |
| **context.Source.providerUrl** | LDAP connection URL                                        | `contextSource.providerUrl=ldap://holly:389/DC=Valyant,DC=local`       |
| **contextSource.userDn**       | Distinguished name of a user with read access to directory | `contextSource.userDn=CN= Administrator, CN=Users,DC=Valyant,DC=local` |
| **contextSource.password**     | Password for the specified user                            | `contextSource.password=secret`                                        |

### Users

These options control how the LDAP server is searched for user names that are entered in the Pentaho login dialog box.

**Note:** The `{0}` token will be replaced by the user name from the login dialog box.

**Note:** The example above defines `DC=Valyant,DC=local` in **contextSource.providerURL**. Given that definition, you would not need to repeat that in **userSearch.searchBase** below because it will be appended automatically to the defined value here.

| LDAP Property               | Purpose                                                                                                                                                                                                                                                             | Example                                        |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **userSearch.searchBase**   | Base (by user name) for user searches                                                                                                                                                                                                                               | `userSearch.searchBase=CN=Users`               |
| **userSearch.searchFilter** | Filter (by user name) for user searches. The attribute you specify here must contain the value that you want your users to log into Pentaho with. Active Directory user names are represented by **sAMAccountName**; full names are represented by **displayName**. | `userSearch.searchFilter=(sAMAccountName={0})` |

### Populator

The populator matches fully distinguished user names from **userSearch** to distinguished role names for roles those users belong to.

**Note:** The `{0}` token will be replaced with the user DN found during a user search; the `{1}` token is replaced with the user name entered in the login screen.

| LDAP Property                    | Purpose                                                                                                                                                   | Example                                                                   |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **populator.convertToUpperCase** | Indicates whether or not retrieved role names are converted to uppercase                                                                                  | `populator.convertToUpperCase=false`                                      |
| **populator.groupRoleAttribute** | The attribute to get role names from                                                                                                                      | `populator.groupRoleAttribute=cn`                                         |
| **populator.groupSearchBase**    | Base (by user DN or user name) for role searches.                                                                                                         | `populator.groupSearchBase=ou= Pentaho`                                   |
| **populator.groupSearchFilter**  | The special nested group filter for Active Directory is shown in the example; this will not work with non-MSAD directory servers.                         | `populator.groupSearchFilter= (memberof:1.2.840.113556.1.4.1941: =({0}))` |
| **populator.rolePrefix**         | A prefix to add to the beginning of the role name found in the group role attribute; the value can be an empty string.                                    | `populator.rolePrefix=`                                                   |
| **populator.searchSubtree**      | Indicates whether or not the search must include the current object and all children. If set to `false`, the search must include the current object only. | `populator.searchSubtree=true`                                            |

### All authorities search

These entries populate the Pentaho Server Access Control List (ACL) roles. These should be similar or identical to the populator entries.

| LDAP Property                          | Purpose                                                                                                   | Example                                                  |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **allAuthoritiesSearch.roleAttribute** | The attribute used for role values                                                                        | `allAuthoritiesSearch.roleAttribute=cn`                  |
| **allAuthoritiesSearch.searchBase**    | Base for "all roles" searches                                                                             | `allAuthoritiesSearch.searchBase=ou= Pentaho`            |
| **allAuthoritiesSearch.searchFilter**  | Filter for "all roles" searches. Active Directory requires that the**objectClass** value be set to group. | `allAuthoritiesSearch.searchFilter= (objectClass=group)` |

### All user name search

These entries populate the Pentaho Server ACL users.

| LDAP Property                             | Purpose                            | Example                                                 |
| ----------------------------------------- | ---------------------------------- | ------------------------------------------------------- |
| **allUsernamesSearch.username Attribute** | The attribute used for user values | `allUsernamesSearch.username Attribute= sAMAccountName` |
| **allUsernamesSearch.searchBase**         | Base for "all users" searches      | `allUsernamesSearch.searchBase= CN=users`               |
| **allUsernamesSearch.searchFilter**       | Filter for "all users" searches    | `allUsernamesSearch.searchFilter= objectClass=person`   |
