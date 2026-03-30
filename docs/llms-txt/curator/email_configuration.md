# Source: https://docs.curator.interworks.com/setup/email/email_configuration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Email Configuration

> Configure SMTP and email settings for Curator features including Report Builder and notification systems.

There are a variety of places that use e-mail settings across Curator.  The largest piece is the
[Report Builder](/embedding_using_analytics/report_builder/overview_and_enabling_report_builder),
but you may want to also set up email to get notified when someone fills out a data-manager form.
Whatever the case, the e-mail setup will reside almost entirely with your e-mail provide or IT group that manages your
mail server.  Once you have confirmed with them that you'll be able to utilize their mail service, use the steps below
to fill out the details for your e-mail configuration on Curator.

## Enabling and Testing Mail Settings

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Mail** > **Mail Configuration** section from the left-hand menu (see "Mail
   Configuration Permissions" below if you do not see this menu item).
3. Fill out the form using the details provided from your mail administrator.
4. Save the form.
5. Ensure the details are accurate by clicking the "Test Saved Settings" and entering your email.
6. Once you click send, wait up to 5 minutes (and double-check your spam inbox) - if you have not received an e-mail
   double-check the settings with your mail administrator to ensure everything is set up properly

## Mail Configuration Permissions

Access to Mail configuration may not be granted by default depending on your installation.  In order to view the mail
configuration, ensure that your
[Backend User](/site_administration/backend_administrators/overview) has access.
