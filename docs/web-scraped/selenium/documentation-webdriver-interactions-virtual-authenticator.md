# Source: https://selenium.dev/documentation/webdriver/interactions/virtual_authenticator/

Title: Virtual Authenticator

URL Source: https://selenium.dev/documentation/webdriver/interactions/virtual_authenticator/

Markdown Content:
About
Downloads
Documentation
Projects
Support
Blog
English
Search
K
Registrations Open for SeleniumConf 2026 | May 06–08 | Join Us In-Person! Register now!
Documentation
Overview
WebDriver
Getting Started
Drivers
Browsers
Waits
Elements
Interactions
Navigation
Alerts
Cookies
Frames
Print Page
Windows
Virtual Authenticator
Actions API
BiDi
Support Features
Troubleshooting
Selenium Manager
Grid
IE Driver Server
IDE
Test Practices
Legacy
About
 Edit this page
 Create documentation issue
 Create project issue
 Print entire section
Virtual Authenticator Options
Add Virtual Authenticator
Remove Virtual Authenticator
Create Resident Credential
Create Non-Resident Credential
Add Credential
Get Credential
Remove Credential
Remove All Credentials
Set User Verified
Documentation
WebDriver
Interactions
Virtual Authenticator
v4.0
Virtual Authenticator
A representation of the Web Authenticator model.

Web applications can enable a public key-based authentication mechanism known as Web Authentication to authenticate users in a passwordless manner. Web Authentication defines APIs that allows a user to create a public-key credential and register it with an authenticator. An authenticator can be a hardware device or a software entity that stores user’s public-key credentials and retrieves them on request.

As the name suggests, Virtual Authenticator emulates such authenticators for testing.

Virtual Authenticator Options

A Virtual Authenticatior has a set of properties. These properties are mapped as VirtualAuthenticatorOptions in the Selenium bindings.

Java
CSharp
Ruby
Python
JavaScript
Kotlin
  public void testVirtualOptions() {
    VirtualAuthenticatorOptions options = new VirtualAuthenticatorOptions()
      .setIsUserVerified(true)
      .setHasUserVerification(true)
      .setIsUserConsenting(true)
      .setTransport(VirtualAuthenticatorOptions.Transport.USB)
      .setProtocol(VirtualAuthenticatorOptions.Protocol.U2F)
View Complete Code
View on GitHub
Add Virtual Authenticator

It creates a new virtual authenticator with the provided properties.

Java
CSharp
Ruby
Python
JavaScript
Kotlin
  public void testCreateAuthenticator() {
    VirtualAuthenticatorOptions options = new VirtualAuthenticatorOptions()
      .setProtocol(VirtualAuthenticatorOptions.Protocol.U2F)
      .setHasResidentKey(false);

    VirtualAuthenticator authenticator =
View Complete Code
View on GitHub
Remove Virtual Authenticator

Removes the previously added virtual authenticator.

Java
CSharp
Ruby
Python
JavaScript
Kotlin
View Complete Code
View on GitHub
Create Resident Credential

Creates a resident (stateful) credential with the given required credential parameters.

Java
CSharp
Ruby
Python
JavaScript
Kotlin

    byte[] credentialId = {1, 2, 3, 4};
    byte[] userHandle = {1};
    Credential residentCredential = Credential.createResidentCredential(
View Complete Code
View on GitHub
Create Non-Resident Credential

Creates a resident (stateless) credential with the given required credential parameters.

Java
CSharp
Ruby
Python
JavaScript
Kotlin

    byte[] credentialId = {1, 2, 3, 4};
    Credential nonResidentCredential = Credential.createNonResidentCredential(
View Complete Code
View on GitHub
Add Credential

Registers the credential with the authenticator.

Java
CSharp
Ruby
Python
JavaScript
Kotlin
  public void testCreateAndAddNonResidentialKey() {
    VirtualAuthenticatorOptions options = new VirtualAuthenticatorOptions()
      .setProtocol(VirtualAuthenticatorOptions.Protocol.U2F)
      .setHasResidentKey(false);

    VirtualAuthenticator authenticator = ((HasVirtualAuthenticator) driver).addVirtualAuthenticator(options);

    byte[] credentialId = {1, 2, 3, 4};
    Credential nonResidentCredential = Credential.createNonResidentCredential(
      credentialId, "localhost", ec256PrivateKey, /*signCount=*/0);
View Complete Code
View on GitHub
Get Credential

Returns the list of credentials owned by the authenticator.

Java
CSharp
Ruby
Python
JavaScript
Kotlin
  public void testGetCredential() {
    VirtualAuthenticatorOptions options = new VirtualAuthenticatorOptions()
      .setProtocol(VirtualAuthenticatorOptions.Protocol.CTAP2)
      .setHasResidentKey(true)
      .setHasUserVerification(true)
      .setIsUserVerified(true);
    VirtualAuthenticator authenticator = ((HasVirtualAuthenticator) driver).addVirtualAuthenticator(options);

    byte[] credentialId = {1, 2, 3, 4};
    byte[] userHandle = {1};
    Credential residentCredential = Credential.createResidentCredential(
      credentialId, "localhost", rsaPrivateKey, userHandle, /*signCount=*/0);

    authenticator.addCredential(residentCredential);

View Complete Code
View on GitHub
Remove Credential

Removes a credential from the authenticator based on the passed credential id.

Java
CSharp
Ruby
Python
JavaScript
Kotlin
  public void testRemoveCredential() {
    VirtualAuthenticator authenticator =
      ((HasVirtualAuthenticator) driver).addVirtualAuthenticator(new VirtualAuthenticatorOptions());

    byte[] credentialId = {1, 2, 3, 4};
    Credential credential = Credential.createNonResidentCredential(
      credentialId, "localhost", rsaPrivateKey, 0);

    authenticator.addCredential(credential);

View Complete Code
View on GitHub
Remove All Credentials

Removes all the credentials from the authenticator.

Java
CSharp
Ruby
Python
JavaScript
Kotlin
  public void testRemoveAllCredentials() {
    VirtualAuthenticator authenticator =
      ((HasVirtualAuthenticator) driver).addVirtualAuthenticator(new VirtualAuthenticatorOptions());

    byte[] credentialId = {1, 2, 3, 4};
    Credential residentCredential = Credential.createNonResidentCredential(
      credentialId, "localhost", rsaPrivateKey, /*signCount=*/0);

    authenticator.addCredential(residentCredential);

View Complete Code
View on GitHub
Set User Verified

Sets whether the authenticator will simulate success or fail on user verification.

Java
CSharp
Ruby
Python
JavaScript
Kotlin
  public void testSetUserVerified() {
    VirtualAuthenticatorOptions options = new VirtualAuthenticatorOptions()
View Complete Code
View on GitHub
Last modified July 29, 2025: Adding trailing / to retrieve code from GitHub (48b97e9bf82)
Development Partners
Selenium Level Sponsors
Support the Selenium Project

Learn more or view the full list of sponsors.

LEARN MORE 
© 2026 Software Freedom Conservancy All Rights Reserved

About Selenium
