# Source: https://docs.safetycli.com/safety-docs/firewall/using-firewall/firewall-monitoring-and-management.md

# Firewall Monitoring and Management

## Accessing Firewall Monitoring

To access Firewall monitoring features:

1. Log in to Safety Platform at [platform.safetycli.com](https://platform.safetycli.com)
2. Navigate to the "Firewall" section in the main navigation

### Live Firewall Updates

The Live Firewall Updates stream displays real-time events from across your organization, including:

* Package installations
* Installation warnings
* Blocked installations
* Authentication events

This stream is particularly useful for:

* Quick debugging of Firewall activity
* Monitoring recent activity across your organization
* Verifying that events are being properly recorded

{% hint style="info" %}
The live Firewall Updates stream is an excellent way to confirm that Safety Firewall is properly configured and reporting events from your team members' environments.
{% endhint %}

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2Fg57l2CqOiozMGY7HnXAH%2FFirewall%20Dashboard.png?alt=media&#x26;token=b91dc831-c227-49d5-bc81-e47999521d6d" alt=""><figcaption></figcaption></figure>

## Organization Protection Status

The Protection Status section provides an overview of your organization's Safety Firewall implementation, including:

### Users Overview

* Total number of protected users
* List of users with Safety Firewall installed
* Last activity time for each user

### Package Managers

For each user, you can see which package managers are protected:

* pip
* poetry
* UV
* Other package managers (future releases)

This helps you ensure complete coverage across your organization.

### Installed Packages Overview

The Installed Packages section shows all packages installed across your organization:

* Package name and version
* Installation date and time
* User who performed the installation
* Whether any warnings or blocks were triggered

You can search and filter this list to find specific packages or activity.

## Managing Team Members

### Adding Users to Firewall

To add new users to Safety Firewall:

1. Navigate to the "Team" section in Safety Platform
2. Click "Invite Team Member"
3. Enter the user's email address
4. Assign appropriate roles and permissions
5. Send the invitation

New users will receive an email invitation with instructions to set up Safety Firewall.

### Monitoring Installation Status

After inviting team members, you can monitor their Firewall installation status:

1. Navigate to the "Firewall" section
2. Check the "Users" tab to see which team members have installed Firewall
3. Follow up with team members who haven't completed installation

{% hint style="info" %}
Team members must complete both the installation of Safety CLI and the Firewall initialization process to appear as protected in Safety Platform.
{% endhint %}
