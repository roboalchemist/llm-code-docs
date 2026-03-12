# Source: https://docs.snowflake.com/en/user-guide/data-exchange.md

# About Data Exchange

Data Exchange provides a data hub for securely collaborating around data with a selected group of members that you invite. It lets you,
as a provider, publish data which can then be discovered by the consumers participating in your exchange.

With a Data Exchange, you can easily provide data to a specific group of consistent business partners taking part in the Data Exchange,
such as internal departments in your company or vendors, suppliers, and partners external to your company.
If you want to share data with a variety of consumers inside and outside your
organization, you can also use listings offered to specific consumers or publicly on the Snowflake Marketplace.

You can manage membership, access to data, and audit data usage, as well as apply security controls to the data shared in the Data Exchange.
see [Manage data listings](data-exchange-managing-data-listings.md).

To set up a data exchange, see [Request a new Data Exchange](data-exchange-requesting.md).

* To access a data exchange, see [Access a Data Exchange](data-exchange-accessing.md).
* To create and manage data exchange provider profiles, see [Manage provider profiles](data-exchange-becoming-a-provider.md).
* If you’re a consumer of a data exchange, see [Configure and use a Data Exchange](data-exchange-using.md).

## Data Exchange Admin responsibilities

The Snowflake account that hosts the Data Exchange is the Data Exchange Admin. The Data Exchange Admin is responsible for configuring the Data Exchange and managing members (data providers and data consumers).

A user with the ACCOUNTADMIN role in the account designated as the Data Exchange Admin can:

* Add or remove members
* Designate members as providers, or consumers, or both

A Data Exchange Admin can delegate these privileges to other roles. For more information, see [Granting administrator privileges in a Data Exchange](data-exchange-marketplace-privileges.md).

## Data Exchange membership

Members are Snowflake accounts that are added by the Data Exchange Admin and designated as providers, consumers, or both.

After joining the Data Exchange, providers can:

* Create a listing.
* Define listing access personalized or [free](../collaboration/collaboration-listings-about.md).
* Publish the listing.
* Grant access to personalized listings or datasets that reside in a different region from the consumer.

After joining the Data Exchange, consumers can:

* Discover by browsing the exchange listings.
* Switch between the Snowflake Marketplace and the Data Exchange.
* Consume datasets (instantly or by request).
