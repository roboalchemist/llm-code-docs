# Source: https://tyk.io/docs/tyk-developer-portal/tyk-enterprise-developer-portal/api-consumer-portal/reset-password.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Forgotten Password

> How to reset your password when using Tyk Developer Portal

If you've forgotten your password, you can easily reset it through the Developer Portal. This process works for both API Owners and API Consumers.

1. Navigate to the Developer Portal and select the **Login** button.

   <img src="https://mintcdn.com/tyk/p6VDuboOnNxaT_QZ/img/dashboard/portal-management/enterprise-portal/login-portal-forgot.png?fit=max&auto=format&n=p6VDuboOnNxaT_QZ&q=85&s=003aa3b13c4d8fde931721d4fc09e456" alt="Portal login screen showing the login form with username and password fields" width="699" height="461" data-path="img/dashboard/portal-management/enterprise-portal/login-portal-forgot.png" />

2. On the login screen, select the **Forgot Password?** link located below the login form.

   <img src="https://mintcdn.com/tyk/p6VDuboOnNxaT_QZ/img/dashboard/portal-management/enterprise-portal/forgot-password.png?fit=max&auto=format&n=p6VDuboOnNxaT_QZ&q=85&s=c773bbdcc7de2c77c45656ff19969859" alt="Password reset form requesting email address" width="667" height="328" data-path="img/dashboard/portal-management/enterprise-portal/forgot-password.png" />

3. Enter the email address associated with your account and select **Reset**.

   <img src="https://mintcdn.com/tyk/p6VDuboOnNxaT_QZ/img/dashboard/portal-management/enterprise-portal/forgot-password-email.png?fit=max&auto=format&n=p6VDuboOnNxaT_QZ&q=85&s=bf2b7d23b345f63472e47daefbf2bfa2" alt="Confirmation screen showing that a password reset email has been sent" width="662" height="313" data-path="img/dashboard/portal-management/enterprise-portal/forgot-password-email.png" />

4. Check your email inbox for a message from the Tyk Developer Portal. The email will contain a password reset link in this format: `https://<your-portal-domain>/auth/reset/code?token=<token-id>`

5. Click the reset link in the email. This will take you to a password reset page in the Developer Portal.

6. Enter your new password in both fields and click **Reset**.

   <img src="https://mintcdn.com/tyk/B97_xetnHOB2KQMe/img/dashboard/portal-management/enterprise-portal/reset-password-request.png?fit=max&auto=format&n=B97_xetnHOB2KQMe&q=85&s=17e4ecdcdaf628eb7184a82370c7adf3" alt="Password reset form with fields to enter and confirm a new password" width="692" height="435" data-path="img/dashboard/portal-management/enterprise-portal/reset-password-request.png" />

7. After successfully resetting your password, click **Login again** to return to the login screen with your new credentials.

   <img src="https://mintcdn.com/tyk/B97_xetnHOB2KQMe/img/dashboard/portal-management/enterprise-portal/reset-done.png?fit=max&auto=format&n=B97_xetnHOB2KQMe&q=85&s=5c33f31116404855dca6b9cb47eb0381" alt="Success screen confirming the password has been reset" width="706" height="388" data-path="img/dashboard/portal-management/enterprise-portal/reset-done.png" />

## Important Notes

* Password reset links are valid for a limited time only
* If your reset link expires, simply restart the process
* Ensure your new password meets the system's security requirements
* For security reasons, you'll be required to log in immediately after resetting your password

Built with [Mintlify](https://mintlify.com).
