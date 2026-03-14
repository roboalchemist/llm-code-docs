# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/siem-integrations/syslog-integration.md

# Syslog Integration

This document will provide the details of Syslog integration to send Audit Logs data from the platform to the Syslog server for log/alert management. The Syslog CEF format allows you to send data and application events to a Syslog server over UDP and TCP protocols.

The steps and guidance provided below will ensure a successful integration.

## Integration Steps

From the left menu go to **Company Settings > SIEM Integrations** and click the **+ NEW** button and provide the information requested.

<table><thead><tr><th width="146"></th><th></th></tr></thead><tbody><tr><td>Integration Name</td><td>Enter a SIEM configuration name</td></tr><tr><td>History Logs</td><td><p>Select this option to ensure that all data in the audit log will be transferred to your SIEM solution<br></p><p>If this feature is inactive, only the audit log data recorded after defining the SIEM integration will be transferred to your SIEM solution</p></td></tr><tr><td>Integration Type</td><td>Select the integration type as Syslog</td></tr><tr><td>URL</td><td>Enter the server address of your Syslog application</td></tr><tr><td>Test Connection</td><td>Test the connection to be sure it works correctly</td></tr></tbody></table>

{% hint style="warning" %}
If you selected UDP as protocol, you need to confirm the connection test by viewing the test log on your Syslog solution.
{% endhint %}

## CEF Format Details

The Common Event Format (CEF) standard format, developed by ArcSight, enables vendors and their customers to quickly integrate their product information into ArcSight ESM.

The following example illustrates a general CEF message using syslog transport:

**Base CEF** **Format:** CEF:Version|Platform Name|ModuleName|ProductVersion|Operation|OperationType|Severity|EventId

**Sample CEF Log Entry:** CEF:0|Keepnet Labs|Incident Responder|1.0|Update|Update|Low| eventId=4722914

### CEF Format Fields Description

This section provides detailed information about how the CEF fields have been mapped from the platform event fields in the sample log described above.

<table><thead><tr><th width="200">CEF Extension Field</th><th width="171">Name</th><th>Description</th></tr></thead><tbody><tr><td>src</td><td>Source IP Address</td><td>Platform IP Address</td></tr><tr><td>cs1</td><td>EntityName</td><td>Shows affected asset names in the platform</td></tr><tr><td>cs2</td><td>OldValue</td><td>Shows data before change happens</td></tr><tr><td>cs3</td><td>NewValue</td><td>Show data after the change happens</td></tr><tr><td>cs1Label</td><td>EntityName</td><td>Shows the label name of cs1</td></tr><tr><td>cs2Label</td><td>Old Value</td><td>Shows the label name of cs2</td></tr><tr><td>cs3Label</td><td>New Value</td><td>Shows the label name of cs3</td></tr></tbody></table>

### Explanation of CEF Extension Fields

The example of the data contained in the fields specified in the above table is listed below.

* **Field src**
  * src=10.20.12.85
* **Field cs1**
  * SystemUser
* **Field cs2**
  * {"PropertyName":"Email","OldValue":"<test@domain.com>","NewValue":"<test2@domain.com>"},{"PropertyName":"FirstName","OldValue":"Andrei","NewValue":"Andrei"},{"PropertyName":"LastName","OldValue":"Kruchev","NewValue":"Kruchev"},{"PropertyName":"NormalizedEmail","OldValue":"<test@domain.com>","NewValue":"<test@domain.com>"},{"PropertyName":"NormalizedUserName","OldValue":"<test@domain.com>","NewValue":"<test@domain.com>"},{"PropertyName":"PhoneNumber","OldValue":"","NewValue":""},{"PropertyName":"UserName","OldValue":"","NewValue":""}]
* **Field cs3**
  * {"ResourceId":"lveGT1ZwCkmn","FirstName":"Andrei","LastName":"Kruchev","CompanyId":1,"CreateTime":"2022-01-29T13:31:23.959869","UpdateTime":"2022-01-29T13:40:45.2323091Z","DeleteTime":null,"CreatedBy":1,"UpdatedBy":0,"DeletedBy":null,"IsDeleted":false,"StatusId":1,"TypeId":1,"Id":1945,"UserName":"<test@domain.com>","NormalizedUserName":"<test@domain.com>","Email":"<test@domain.com>","NormalizedEmail":"<test@domain.com>","EmailConfirmed":true,"PasswordHash":"***","SecurityStamp":"***","ConcurrencyStamp":"\*\*\*\*\*","PhoneNumber":"","PhoneNumberConfirmed":false,"TwoFactorEnabled":false,"LockoutEnd":null,"LockoutEnabled":false,"AccessFailedCount":0}

## Control Phase

In order to make sure that the integration works and logs are being transferred from the platform to the Syslog solution properly, a test is advised.

* After performing the integration, click the **Start Searching** button on the Syslog administration panel or use the **grep** function on Linux distributions.
* When you click the **Test Connection** button on the platform, you can see this request or other platform logs in the Search field on the Syslog administration panel.
* Filter logs with the parameter **Device Vendor = Keepnet Labs** to find the test connection log easily.
