# Source: https://docs.base44.com/developers/references/sdk/docs/interfaces/auth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# auth

***

## Overview

Authentication module for managing user authentication and authorization. The module automatically stores tokens in local storage when available and manages authorization headers for API requests.

### Features

This module provides comprehensive authentication functionality including:

* Email/password login and registration
* Token management
* User profile access and updates
* Password reset flows
* OTP verification
* User invitations

### Authentication Modes

The auth module is only available in user authentication mode (`base44.auth`).

## Methods

### me()

> **me**(): `Promise`\<`User`>

Gets the current authenticated user's information.

#### Returns

`User`

An authenticated user.

<Accordion title="Properties">
  <ResponseField name="id" type="string" required>
    Unique user identifier.
  </ResponseField>

  <ResponseField name="created_date" type="string" required>
    When the user was created.
  </ResponseField>

  <ResponseField name="updated_date" type="string" required>
    When the user was last updated.
  </ResponseField>

  <ResponseField name="email" type="string" required>
    User's email address.
  </ResponseField>

  <ResponseField name="full_name" type="string | null" required>
    User's full name.
  </ResponseField>

  <ResponseField name="disabled" type="boolean | null" required>
    Whether the user is disabled.
  </ResponseField>

  <ResponseField name="is_verified" type="boolean" required>
    Whether the user's email has been verified.
  </ResponseField>

  <ResponseField name="app_id" type="string" required>
    The app ID this user belongs to.
  </ResponseField>

  <ResponseField name="is_service" type="boolean" required>
    Whether this is a service account.
  </ResponseField>

  <ResponseField name="role" type="string" required>
    User's role in the app. Roles are configured in the app settings and determine the user's permissions and access levels.
  </ResponseField>

  <ResponseField name="[key: string]" type="any">
    Additional custom fields defined in the user schema. Any custom properties added to the user schema in the app will be available here with their configured types and values.
  </ResponseField>
</Accordion>

#### Example

<CodeGroup>
  ```typescript Get current user information theme={null}
  const user = await base44.auth.me();
  console.log(`Logged in as: ${user.email}`);
  console.log(`User ID: ${user.id}`);
  ```
</CodeGroup>

***

### updateMe()

> **updateMe**(`data`): `Promise`\<`User`>

Updates the current authenticated user's information.

Only the fields included in the data object will be updated.
Commonly updated fields include `full_name` and custom profile fields.

#### Parameters

<ParamField body="data" type="Partial<Omit<User, ... | ... | ...>>" required>
  Object containing the fields to update.
</ParamField>

<Accordion title="Properties">
  <ParamField body="id" type="string" required>
    Unique user identifier.
  </ParamField>

  <ParamField body="created_date" type="string" required>
    When the user was created.
  </ParamField>

  <ParamField body="updated_date" type="string" required>
    When the user was last updated.
  </ParamField>

  <ParamField body="email" type="string" required>
    User's email address.
  </ParamField>

  <ParamField body="full_name" type="string | null" required>
    User's full name.
  </ParamField>

  <ParamField body="disabled" type="boolean | null" required>
    Whether the user is disabled.
  </ParamField>

  <ParamField body="is_verified" type="boolean" required>
    Whether the user's email has been verified.
  </ParamField>

  <ParamField body="app_id" type="string" required>
    The app ID this user belongs to.
  </ParamField>

  <ParamField body="is_service" type="boolean" required>
    Whether this is a service account.
  </ParamField>

  <ParamField body="role" type="string" required>
    User's role in the app. Roles are configured in the app settings and determine the user's permissions and access levels.
  </ParamField>
</Accordion>

#### Returns

`User`

An authenticated user.

<Accordion title="Properties">
  <ResponseField name="id" type="string" required>
    Unique user identifier.
  </ResponseField>

  <ResponseField name="created_date" type="string" required>
    When the user was created.
  </ResponseField>

  <ResponseField name="updated_date" type="string" required>
    When the user was last updated.
  </ResponseField>

  <ResponseField name="email" type="string" required>
    User's email address.
  </ResponseField>

  <ResponseField name="full_name" type="string | null" required>
    User's full name.
  </ResponseField>

  <ResponseField name="disabled" type="boolean | null" required>
    Whether the user is disabled.
  </ResponseField>

  <ResponseField name="is_verified" type="boolean" required>
    Whether the user's email has been verified.
  </ResponseField>

  <ResponseField name="app_id" type="string" required>
    The app ID this user belongs to.
  </ResponseField>

  <ResponseField name="is_service" type="boolean" required>
    Whether this is a service account.
  </ResponseField>

  <ResponseField name="role" type="string" required>
    User's role in the app. Roles are configured in the app settings and determine the user's permissions and access levels.
  </ResponseField>

  <ResponseField name="[key: string]" type="any">
    Additional custom fields defined in the user schema. Any custom properties added to the user schema in the app will be available here with their configured types and values.
  </ResponseField>
</Accordion>

#### Examples

<CodeGroup>
  ```typescript Update specific fields theme={null}
  const updatedUser = await base44.auth.updateMe({
    full_name: 'John Doe'
  });
  console.log(`Updated user: ${updatedUser.full_name}`);
  ```

  ```typescript Update custom fields defined in your User entity theme={null}
  await base44.auth.updateMe({
    bio: 'Software developer',
    phone: '+1234567890',
    preferences: { theme: 'dark' }
  });
  ```
</CodeGroup>

***

### redirectToLogin()

> **redirectToLogin**(`nextUrl`): `void`

Redirects the user to the app's login page.

Redirects with a callback URL to return to after successful authentication. Requires a browser environment and can't be used in the backend.

#### Parameters

<ParamField body="nextUrl" type="string" required>
  URL to redirect to after successful login.
</ParamField>

#### Returns

`void`

#### Throws

When not in a browser environment.

#### Examples

<CodeGroup>
  ```typescript Redirect to login and come back to current page theme={null}
  base44.auth.redirectToLogin(window.location.href);
  ```

  ```typescript Redirect to login and then go to the dashboard page theme={null}
  base44.auth.redirectToLogin('/dashboard');
  ```
</CodeGroup>

***

### loginWithProvider()

> **loginWithProvider**(`provider`, `fromUrl?`): `void`

Redirects the user to a third-party authentication provider's login page.

Initiates an OAuth login flow with one of the built-in providers. Requires a browser environment and can't be used in the backend.

Supported providers:

* `'google'`: [Google OAuth](https://developers.google.com/identity/protocols/oauth2). Enabled by default.
* `'microsoft'`: [Microsoft OAuth](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow). Enable Microsoft in your app's authentication settings before specifying this provider.
* `'facebook'`: [Facebook Login](https://developers.facebook.com/docs/facebook-login). Enable Facebook in your app's authentication settings before using.
* `'apple'`: [Sign in with Apple](https://developer.apple.com/sign-in-with-apple/). Enable Apple in your app's authentication settings before using this provider.
* `'sso'`: Enterprise SSO. [Set up an SSO provider](https://docs.base44.com/Setting-up-your-app/Setting-up-SSO) in your app's authentication settings before using this provider.

#### Parameters

<Accordion title="Properties">
  <ParamField body="provider" type="string" required>
    The authentication provider to use: `'google'`, `'microsoft'`, `'facebook'`, `'apple'`, or `'sso'`.
  </ParamField>

  <ParamField body="fromUrl" type="string">
    URL to redirect to after successful authentication. Defaults to `'/'`.
  </ParamField>
</Accordion>

#### Returns

`void`

#### Examples

<CodeGroup>
  ```typescript Google theme={null}
  base44.auth.loginWithProvider('google', window.location.pathname);
  ```

  ```typescript Microsoft theme={null}
  base44.auth.loginWithProvider('microsoft', '/dashboard');
  ```

  ```typescript Apple theme={null}
  base44.auth.loginWithProvider('apple', '/dashboard');
  ```

  ```typescript SSO theme={null}
  base44.auth.loginWithProvider('sso', '/dashboard');
  ```
</CodeGroup>

***

### logout()

> **logout**(`redirectUrl?`): `void`

Logs out the current user.

Removes the authentication token from local storage and Axios headers, then optionally redirects to a URL or reloads the page. Requires a browser environment and can't be used in the backend.

#### Parameters

<ParamField body="redirectUrl" type="string">
  Optional URL to redirect to after logout. Reloads the page if not provided.
</ParamField>

#### Returns

`void`

#### Examples

<CodeGroup>
  ```typescript Logout and reload page theme={null}
  base44.auth.logout();
  ```

  ```typescript Logout and redirect to login page theme={null}
  base44.auth.logout('/login');
  ```

  ```typescript Logout and redirect to home theme={null}
  base44.auth.logout('/');
  ```
</CodeGroup>

***

### setToken()

> **setToken**(`token`, `saveToStorage?`): `void`

Sets the authentication token.

Updates the authorization header for API requests and optionally saves the token to local storage for persistence. Saving to local storage requires a browser environment and is automatically skipped in backend environments.

#### Parameters

<Accordion title="Properties">
  <ParamField body="token" type="string" required>
    JWT authentication token.
  </ParamField>

  <ParamField body="saveToStorage" type="boolean">
    Whether to save the token to local storage. Defaults to true.
  </ParamField>
</Accordion>

#### Returns

`void`

#### Examples

<CodeGroup>
  ```typescript Set token and save to local storage theme={null}
  base44.auth.setToken('eyJhbGciOiJIUzI1NiIs...');
  ```

  ```typescript Set token without saving to local storage theme={null}
  base44.auth.setToken('eyJhbGciOiJIUzI1NiIs...', false);
  ```
</CodeGroup>

***

### loginViaEmailPassword()

> **loginViaEmailPassword**(\
> `email`,\
> `password`,\
> `turnstileToken?`\
> ): `Promise`\<`LoginResponse`>

Logs in a registered user using email and password.

Authenticates a user with email and password credentials. The user must already have a registered account. For new users, use [`register()`](#register) first to create an account. On successful login, automatically sets the token for subsequent requests.

#### Parameters

<Accordion title="Properties">
  <ParamField body="email" type="string" required>
    User's email address.
  </ParamField>

  <ParamField body="password" type="string" required>
    User's password.
  </ParamField>

  <ParamField body="turnstileToken" type="string">
    Optional [Cloudflare Turnstile CAPTCHA token](https://developers.cloudflare.com/turnstile/) for bot protection.
  </ParamField>
</Accordion>

#### Returns

`LoginResponse`

Response from login endpoints containing user information and access token.

<Accordion title="Properties">
  <ResponseField name="access_token" type="string" required>
    JWT access token for authentication.
  </ResponseField>

  <ResponseField name="user" type="User" required>
    User information.

    <Accordion title="Properties">
      <ResponseField name="id" type="string" required>
        Unique user identifier.
      </ResponseField>

      <ResponseField name="created_date" type="string" required>
        When the user was created.
      </ResponseField>

      <ResponseField name="updated_date" type="string" required>
        When the user was last updated.
      </ResponseField>

      <ResponseField name="email" type="string" required>
        User's email address.
      </ResponseField>

      <ResponseField name="full_name" type="string | null" required>
        User's full name.
      </ResponseField>

      <ResponseField name="disabled" type="boolean | null" required>
        Whether the user is disabled.
      </ResponseField>

      <ResponseField name="is_verified" type="boolean" required>
        Whether the user's email has been verified.
      </ResponseField>

      <ResponseField name="app_id" type="string" required>
        The app ID this user belongs to.
      </ResponseField>

      <ResponseField name="is_service" type="boolean" required>
        Whether this is a service account.
      </ResponseField>

      <ResponseField name="role" type="string" required>
        User's role in the app. Roles are configured in the app settings and determine the user's permissions and access levels.
      </ResponseField>
    </Accordion>
  </ResponseField>
</Accordion>

#### Examples

<CodeGroup>
  ```typescript Login with email and password theme={null}
  try {
    const { access_token, user } = await base44.auth.loginViaEmailPassword(
      'user@example.com',
      'securePassword123'
    );
    console.log('Login successful!', user);
  } catch (error) {
    console.error('Login failed:', error);
  }
  ```

  ```typescript With captcha token theme={null}
  const response = await base44.auth.loginViaEmailPassword(
    'user@example.com',
    'securePassword123',
    'captcha-token-here'
  );
  ```
</CodeGroup>

***

### isAuthenticated()

> **isAuthenticated**(): `Promise`\<`boolean`>

Checks if the current user is authenticated.

#### Returns

`Promise<boolean>`

Promise resolving to true if authenticated, false otherwise.

#### Example

<CodeGroup>
  ```typescript Check authentication status theme={null}
  const isAuthenticated = await base44.auth.isAuthenticated();
  if (isAuthenticated) {
    console.log('User is logged in');
  } else {
    // Redirect to login page
    base44.auth.redirectToLogin(window.location.href);
  }
  ```
</CodeGroup>

***

### inviteUser()

> **inviteUser**(`userEmail`, `role`): `Promise`\<`any`>

Invites a user to the app.

Sends an invitation email to a potential user with a specific role.
Roles are configured in the app settings and determine
the user's permissions and access levels.

#### Parameters

<Accordion title="Properties">
  <ParamField body="userEmail" type="string" required>
    Email address of the user to invite.
  </ParamField>

  <ParamField body="role" type="string" required>
    Role to assign to the invited user. Must match a role defined in the app. For example, `'admin'` or `'user'`.
  </ParamField>
</Accordion>

#### Returns

`Promise<any>`

Promise that resolves when the invitation is sent successfully. Throws an error if the invitation fails.

#### Example

<CodeGroup>
  ```typescript try { theme={null}
    await base44.auth.inviteUser('newuser@example.com', 'user');
    console.log('Invitation sent successfully!');
  } catch (error) {
    console.error('Failed to send invitation:', error);
  }
  ```
</CodeGroup>

***

### register()

> **register**(`params`): `Promise`\<`any`>

Registers a new user account.

Creates a new user account with email and password. After successful registration,
use [`loginViaEmailPassword()`](#loginviaemailpassword) to log in the user.

#### Parameters

<ParamField body="params" type="RegisterParams" required>
  Registration details including email, password, and optional fields.
</ParamField>

<Accordion title="Properties">
  <ParamField body="email" type="string" required>
    User's email address.
  </ParamField>

  <ParamField body="password" type="string" required>
    User's password.
  </ParamField>

  <ParamField body="turnstile_token" type="string | null">
    Optional Cloudflare Turnstile CAPTCHA token for bot protection.
  </ParamField>

  <ParamField body="referral_code" type="string | null">
    Optional referral code from an existing user.
  </ParamField>
</Accordion>

#### Returns

`Promise<any>`

Promise resolving to the registration response.

#### Example

<CodeGroup>
  ```typescript Register a new user theme={null}
  await base44.auth.register({
    email: 'newuser@example.com',
    password: 'securePassword123',
    referral_code: 'FRIEND2024'
  });

  // Login after registration
  const { access_token, user } = await base44.auth.loginViaEmailPassword(
    'newuser@example.com',
    'securePassword123'
  );
  ```
</CodeGroup>

***

### verifyOtp()

> **verifyOtp**(`params`): `Promise`\<`any`>

Verifies an OTP (One-time password) code.

Validates an OTP code sent to the user's email during registration
or authentication.

#### Parameters

<ParamField body="params" type="VerifyOtpParams" required>
  Object containing email and OTP code.
</ParamField>

<Accordion title="Properties">
  <ParamField body="email" type="string" required>
    User's email address.
  </ParamField>

  <ParamField body="otpCode" type="string" required>
    One-time password code received by email.
  </ParamField>
</Accordion>

#### Returns

`Promise<any>`

Promise resolving to the verification response if valid.

#### Throws

Error if the OTP code is invalid, expired, or verification fails.

#### Example

<CodeGroup>
  ```typescript try { theme={null}
    await base44.auth.verifyOtp({
      email: 'user@example.com',
      otpCode: '123456'
    });
    console.log('Email verified successfully!');
  } catch (error) {
    console.error('Invalid or expired OTP code');
  }
  ```
</CodeGroup>

***

### resendOtp()

> **resendOtp**(`email`): `Promise`\<`any`>

Resends an OTP code to the user's email address.

Requests a new OTP code to be sent to the specified email address.

#### Parameters

<ParamField body="email" type="string" required>
  Email address to send the OTP to.
</ParamField>

#### Returns

`Promise<any>`

Promise resolving when the OTP is sent successfully.

#### Throws

Error if the email is invalid or the request fails.

#### Example

<CodeGroup>
  ```typescript try { theme={null}
    await base44.auth.resendOtp('user@example.com');
    console.log('OTP resent! Please check your email.');
  } catch (error) {
    console.error('Failed to resend OTP:', error);
  }
  ```
</CodeGroup>

***

### resetPasswordRequest()

> **resetPasswordRequest**(`email`): `Promise`\<`any`>

Requests a password reset.

Sends a password reset email to the specified email address.

#### Parameters

<ParamField body="email" type="string" required>
  Email address for the account to reset.
</ParamField>

#### Returns

`Promise<any>`

Promise resolving when the password reset email is sent successfully.

#### Throws

Error if the email is invalid or the request fails.

#### Example

<CodeGroup>
  ```typescript try { theme={null}
    await base44.auth.resetPasswordRequest('user@example.com');
    console.log('Password reset email sent!');
  } catch (error) {
    console.error('Failed to send password reset email:', error);
  }
  ```
</CodeGroup>

***

### resetPassword()

> **resetPassword**(`params`): `Promise`\<`any`>

Resets password using a reset token.

Completes the password reset flow by setting a new password
using the token received by email.

#### Parameters

<ParamField body="params" type="ResetPasswordParams" required>
  Object containing the reset token and new password.
</ParamField>

<Accordion title="Properties">
  <ParamField body="resetToken" type="string" required>
    Reset token received by email.
  </ParamField>

  <ParamField body="newPassword" type="string" required>
    New password to set.
  </ParamField>
</Accordion>

#### Returns

`Promise<any>`

Promise resolving when the password is reset successfully.

#### Throws

Error if the reset token is invalid, expired, or the request fails.

#### Example

<CodeGroup>
  ```typescript try { theme={null}
    await base44.auth.resetPassword({
      resetToken: 'token-from-email',
      newPassword: 'newSecurePassword456'
    });
    console.log('Password reset successful!');
  } catch (error) {
    console.error('Failed to reset password:', error);
  }
  ```
</CodeGroup>

***

### changePassword()

> **changePassword**(`params`): `Promise`\<`any`>

Changes the user's password.

Updates the password for an authenticated user by verifying
the current password and setting a new one.

#### Parameters

<ParamField body="params" type="ChangePasswordParams" required>
  Object containing user ID, current password, and new password.
</ParamField>

<Accordion title="Properties">
  <ParamField body="userId" type="string" required>
    User ID.
  </ParamField>

  <ParamField body="currentPassword" type="string" required>
    Current password for verification.
  </ParamField>

  <ParamField body="newPassword" type="string" required>
    New password to set.
  </ParamField>
</Accordion>

#### Returns

`Promise<any>`

Promise resolving when the password is changed successfully.

#### Throws

Error if the current password is incorrect or the request fails.

#### Example

<CodeGroup>
  ```typescript try { theme={null}
    await base44.auth.changePassword({
      userId: 'user-123',
      currentPassword: 'oldPassword123',
      newPassword: 'newSecurePassword456'
    });
    console.log('Password changed successfully!');
  } catch (error) {
    console.error('Failed to change password:', error);
  }
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).