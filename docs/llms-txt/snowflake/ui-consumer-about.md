# Source: https://docs.snowflake.com/en/developer-guide/native-apps/ui-consumer-about.md

# Use and manage Snowflake Native Apps as a consumer

Consumers can discover and install apps published to the Snowflake Marketplace or shared
using private listings.

The Native Apps Framework allows consumers to perform the following:

* Use the app by accessing data via Snowflake worksheets.
* View Streamlit apps created by the provider.
* Grant privileges on the app object to users in your organization.
* Associate references that allow access to object required by the app.
* Share event and logging information with the provider.

## Consumer workflow for working with a Snowflake Native App

The following workflow is what consumers typically do when working with apps:

1. [Become a consumer](../../collaboration/consumer-becoming.md).
2. [Install an app from a listing](ui-consumer-installing.md).
3. [Review the access requests from the app](ui-consumer-granting-privs.md).

   This includes granting the privileges and creating references required by the app.
4. (Optional) [Set up an event table](ui-consumer-enable-logging.md) to enable logging and
   event sharing for an app.

## Apps installed from trial listings

When the trial period ends for an app installed from a trial listing, Snowflake
automatically suspends the app unless the consumer converts the app to a full listing.
When the trial period is about to expire, Snowflake sends an email notification before the app is
suspended.

Snowflake recommends that consumers convert the trial listing into a full listing before the
trial period expires. After the app is suspended it may not be possible to resume the app. For example,
if the provider removes the current version of the app or there are unresolved state changes, the
app cannot be resumed.

When an app installed from a trial listing is suspended, all data written inside the app is retained
as long as the consumer does not delete the app.

If the app installed from a trial listing creates objects in the consumer account outside
the application object, consumers can retain these objects after the app is uninstalled. However, they
must transfer ownership of the objects before uninstalling the app. See [Uninstall a Snowflake Native App](ui-consumer-managing-applications.md)
