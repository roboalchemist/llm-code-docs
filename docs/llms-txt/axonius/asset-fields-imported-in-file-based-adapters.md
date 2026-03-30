# Source: https://docs.axonius.com/docs/asset-fields-imported-in-file-based-adapters.md

# Asset Fields Imported in File-Based Adapters

The following sections detail which fields are imported as common data fields for each asset file (Devices, Users, etc.). Any other data in the CSV/JSON/XML is exclusively adapter-specific data.

**General guidelines**

* These fields apply to the general [CSV](https://docs.axonius.com/axonius-help-docs/docs/csv), [JSON](https://docs.axonius.com/axonius-help-docs/docs/json-1), and [Custom Files](https://docs.axonius.com/axonius-help-docs/docs/custom-files) adapters, according to the asset types fetched by each adapter. Any other asset-specific requirements are listed under the specific file type.

  <Callout icon="📘" theme="info">
    **Note**

    In addition for the general CSV adapter, Axonius has [CSV Asset-Specific Adapters](https://docs.axonius.com/axonius-help-docs/docs/csv-specific-adapters).
  </Callout>
* For all values under **Accepted CSV Field Name(s)**, spaces, hyphens and underscores are ignored, and the field name is always lowercase. For example, `First_Name` --> \`firstname'.
* Fields marked as \***KEY** indicate that you need to include **at least one** of these fields as part of the imported CSV file.  More \***KEY** fields available in the CSV file help provide stronger correlation.

## Fields Imported with a Devices File

<Callout icon="❗️" theme="error">
  **Attention**

  The fields imported with a Devices File differ between the CSV and Custom Files adapters.
</Callout>

### CSV

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        UI Field Name
      </th>

      <th>
        Accepted CSV Field Name(s)
      </th>

      <th>
        Notes
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Architecture
      </td>

      <td>
        architecture
      </td>

      <td />
    </tr>

    <tr>
      <td>
        Asset Name
      </td>

      <td>
        name, vmname, displayname, assetname, machinename, instancename, samaccountname, endpointname, machine
      </td>

      <td>
        If no hostname is configured, the Asset Name value is used for the Host Name.
      </td>
    </tr>

    <tr>
      <td>
        Device Manufacturer Serial
      </td>

      <td>
        serial, serialnumber, sn, hostserialnumber, deviceserialnumber, serial#, endpointserialnumber, allserialnumbers
      </td>

      <td>
        \***KEY**
      </td>
    </tr>

    <tr>
      <td>
        Device Manufacturer
      </td>

      <td>
        manufacturer, devicemanufacturer
      </td>

      <td />
    </tr>

    <tr>
      <td>
        Device Model
      </td>

      <td>
        model, modelid, endpointmodel
      </td>

      <td />
    </tr>

    <tr>
      <td>
        Domain
      </td>

      <td>
        domain, domainname, endpointdomain
      </td>

      <td>
        If this value is not specified AND the device is specified in DOMAIN\Name format, Axonius replaces the Domain value with the parsed out DOMAIN.
      </td>
    </tr>

    <tr>
      <td>
        Host Name
      </td>

      <td>
        hostname, host, fqdn, fullyqualifieddomainname, compname, computername, servername, dnsname, hosthostname, endpointfqdn
      </td>

      <td>
        \***KEY** -  If the device is specified in DOMAIN\Name, Axonius parses the DOMAIN value out.

        <br />

        If the CSV field is set to "unknown", Axonius sets the Host Name to blank.
      </td>
    </tr>

    <tr>
      <td>
        ID
      </td>

      <td>
        id, identifier, serialnumber, assetid, resourceid
      </td>

      <td>
        \***KEY** - The ID field is a combination of the "CSV File Name" value and the specified field names.
      </td>
    </tr>

    <tr>
      <td>
        IPs
      </td>

      <td>
        ipaddresstext, ip, ipaddress, ipaddresses, ips, primaryip, endpointipaddress, registerip, sourceip, managementip, privateip, allips, lastip, address, ipaddresslist, ipaddri, ipaddrs, ipaddr, localip, privateipaddresses, ipfirst
      </td>

      <td>
        This field accepts a comma separated set of IP addresses.
      </td>
    </tr>

    <tr>
      <td>
        Last Seen
      </td>

      <td>
        lastmessagetime, lastdiscoveredtime, lastseen, lastcheckin
      </td>

      <td>
        If this value is not specified, enter the time that the CSV was last imported.
      </td>
    </tr>

    <tr>
      <td>
        Last Used Users
      </td>

      <td>
        username
      </td>

      <td>
        This appends to the existing Last Used Users list if the device already exists.
      </td>
    </tr>

    <tr>
      <td>
        MAC
      </td>

      <td>
        mac, macaddress, macaddresses, macs
      </td>

      <td>
        \***KEY** - This field accepts a comma separated set of MAC addresses.
      </td>
    </tr>

    <tr>
      <td>
        Machine
      </td>

      <td>
        name
      </td>

      <td />
    </tr>

    <tr>
      <td>
        Network Interfaces
      </td>

      <td>
        networkinterfaces
      </td>

      <td>
        Axonius attempts to parse IP address(es), MAC address(es), and network interface cards from this field.
      </td>
    </tr>

    <tr>
      <td>
        OS (see Notes)
      </td>

      <td>
        os, osname, osversion, operatingsystem, osmode, uname, endpointos
      </td>

      <td>
        This field is parsed out into multiple properties within the OS field. Not all OSes are parsed properly. Please reach out to Axonius if an OS is not parsing as expected.
      </td>
    </tr>

    <tr>
      <td>
        OS: Kernel Version
      </td>

      <td>
        kernel, kernelversion
      </td>

      <td />
    </tr>

    <tr>
      <td>
        Software Name
      </td>

      <td>
        packages
      </td>

      <td>
        This is delimited by spaces.
      </td>
    </tr>

    <tr>
      <td>
        Cloud ID
      </td>

      <td>
        cloudid, linodeid
      </td>

      <td />
    </tr>

    <tr>
      <td>
        Cloud Provider
      </td>

      <td>
        cloudprovider, cloudprovidor
      </td>

      <td />
    </tr>
  </tbody>
</Table>

### Custom Files

| UI Field Name              | Accepted CSV/JSON Field Name(s)                                                                                 | Notes                                                     |
| :------------------------- | :-------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------- |
| Architecture               | architecture                                                                                                    |                                                           |
| Asset Name                 | name, vmname, displayname, assetname, machinename, instancename, samaccountname, endpointname, machine          | If no hostname is configured, this is used for Host Name. |
| Device Manufacturer Serial | serial, serialnumber, sn, hostserialnumber, deviceserialnumber, serial#, endpointserialnumber, allserialnumbers | \***KEY**                                                 |
| Host Name                  | hostname, host, fqdn, fullyqualifieddomainname, compname, computername, servername, dnsname, endpointfqdn       | \***KEY**                                                 |
| IPs                        | ipaddress, ips, primaryip, endpointipaddress                                                                    | Accepts comma-separated values.                           |
| Asset Tag                  | assettag, tags, tag, labels, label                                                                              | Accepts multiple formats - see examples below             |
| Tag Name                   | tagname, tagkey, labelname, labelkey                                                                            |                                                           |
| Tag Value                  | tagvalue, labelvalue                                                                                            |                                                           |

#### Acceptable Formats for the Asset Tag Field

| Format                         | Example                                              |
| :----------------------------- | :--------------------------------------------------- |
| Comma-separated string         | `"Production,Critical,Web"` → 3 tags                 |
| List of string                 | `["Production", "Critical"]` → 2 tags                |
| List of key-value dictionaries | `[{"key": "env", "value": "prod"}]` → 1 tag with key |
| Single dictionary              | `{"key": "env", "value": "prod"}` → 1 tag with key   |

## Fields Imported with a Users File

| UI Field Name | Accepted CSV Field Name(s)                                                                    | Notes                                                                                                 |
| :------------ | :-------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------- |
| Domain        | domain, domainname, endpointdomain                                                            |                                                                                                       |
| First Name    | firstname, givenname                                                                          |                                                                                                       |
| ID            | id, identifier, serialnumber, assetid, resourceid, userid                                     | \***KEY** - The ID field is a combination of the "CSV File Name" value and the specified field names. |
| Last Name     | lastname, surname, sn                                                                         |                                                                                                       |
| Mail          | mail, email, usermail, mailaddress, email address, emailprimarywork, companyemail             | \***KEY**                                                                                             |
| Name          | name, vmname, displayname, assetname, machinename, instancename, samaccountname, endpointname | \***KEY**                                                                                             |
| User Name     | username                                                                                      | \***KEY**                                                                                             |

## Fields Imported with a Software Applications File

The minimum requirements to parse Vulnerabilities from the CSV adapter are as follows:

* The **File contains installed software** parameter is checked.
* The file has at least the following headers:
  * Hostname (or any of the headers supported as hostname)
  * Software Name (header must be present, though may be empty on a row)
  * CVE ID

The other headers (or data in a row for those headers) are optional for the purposes of parsing Vulnerabilities.

| UI Field Name    | Accepted CSV Field Name(s)                                                                                              | Notes                                                                                                                                                                                                                                                                                       |
| :--------------- | :---------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Host Name        | hostname, host, fqdn, fullyqualifieddomainname, compname, computername, servername, dnsname, hosthostname, endpointfqdn | \***KEY** - This field is required as the software list is imported to each individual device.                                                                                                                                                                                              |
| Software Name    | softwarename, swname                                                                                                    | \***KEY** this field is required in order to parse installed software.  This field may be left empty on a row with CVE ID.                                                                                                                                                                  |
| Software Path    | softwarepath, swpath                                                                                                    |                                                                                                                                                                                                                                                                                             |
| Software Vendor  | softwarevendor, swvendor                                                                                                |                                                                                                                                                                                                                                                                                             |
| Software Version | softwareversion, swversion                                                                                              |                                                                                                                                                                                                                                                                                             |
| CVE ID           | cve, cveid, cvelist, grypecve                                                                                           | If present, a row featuring a CVE ID is parsed as vulnerable software in addition to installed software.                                                                                                                                                                                    |
| CVE Description  | cvedescription                                                                                                          | This field will be ignored if CVE ID is empty or not present.                                                                                                                                                                                                                               |
| CVE Severity     | cveseverity                                                                                                             | CVE Severity needs to be one of the values listed here. An invalid CVE Severity value is ignored.   This field will be ignored if CVE ID is empty or not present. 'NONE', 'LOW', 'MEDIUM', 'MODERATE', 'SEVERE', 'SERIOUS', 'HIGH', 'CRITICAL', 'URGENT', 'INFO', 'UNTRIAGED', 'NEGLIGIBLE' |
| CVE Status       | cvestatus                                                                                                               | CVE Status needs to be one of the values listed here. An invalid CVE Status value is ignored.   This field will be ignored if CVE ID is empty or not present. 'open', 'closed', 'reopen', 'expired', 'done', 'valid', 'obsolete', 'pending'                                                 |

## Fields Imported with a Databases File

<Callout icon="❗️" theme="error">
  **Attention**

  The fields imported with a Databases File differ between the CSV and Custom Files adapters.
</Callout>

### CSV

| UI Field Name | Accepted CSV Field Name(s)                                                           | Notes                                              |
| :------------ | :----------------------------------------------------------------------------------- | :------------------------------------------------- |
| ID            | id, identifier, serialnumber, assetid, recid, deviceid, objectid, hostid, databaseid | \***KEY** - This field is required (database ID)   |
| Name          | name, diaplayname, assetname, instancename, databasename                             | \***KEY** - This field is required (database name) |
| Instance Type | instance, instancetype                                                               |                                                    |
| Status        | status, assetstatus                                                                  |                                                    |
| Creation Date | creationdatetime, datecreation                                                       |                                                    |
| Port          | port                                                                                 |                                                    |
| IP            | ip, ipaddress, ipaddresses, ips, sourceip, ipaddresstext                             |                                                    |

### Custom Files

| UI Field Name | Accepted CSV/JSON Field Name(s)                                                                                                                                                                                                                | Notes     |
| :------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| Name          | name, databasename, datname, database, schemaname                                                                                                                                                                                              | \***KEY** |
| Creation Time | createddatetime, datecreation, creationtime                                                                                                                                                                                                    |           |
| IP            | paddresstext, ip, ipaddress, ipaddresses, ips, primaryip, endpointipaddress, registerip, sourceip, managementip, privateip, allips, ipfirst, lastip, address, ipaddresslist, ipaddri, ipaddrs, ipaddr, localip, privateipaddresses, databaseip |           |
| Port          | port                                                                                                                                                                                                                                           |           |
| Asset Status  | status, databasestatus, state]                                                                                                                                                                                                                 |           |
| Instance      | instance, instancetype                                                                                                                                                                                                                         |           |

## Fields Imported with an Accounts File

| UI Field Name | Accepted CSV Field Name(s)                                                           | Notes                                             |
| :------------ | :----------------------------------------------------------------------------------- | :------------------------------------------------ |
| ID            | id, identifier, serialnumber, assetid, recid, deviceid, objectid, hostid, accounteid | \***KEY** - This field is required (account ID)   |
| Name          | name, diaplayname, assetname, instancename, accountename                             | \***KEY** - This field is required (account name) |
| Creation Time | creationdatetime, datecreation                                                       |                                                   |

## Fields Imported with a Business Applications File

| UI Field Name           | Accepted CSV Field Name(s)                                   | Notes                              |
| :---------------------- | :----------------------------------------------------------- | :--------------------------------- |
| ID                      | id, application number, applicationnumber                    | \***KEY** - This field is required |
| Name                    | name, application name, applicationname                      | \***KEY** - This field is required |
| Application Type        | application type, applicationtype                            |                                    |
| Application Description | description, application description, applicationdescription |                                    |
| Managed By              | managed by, managedby                                        |                                    |
| Business Criticality    | business critically, businesscritically                      |                                    |
| Operational Status      | operational status, operationalstatus                        |                                    |

## Fields Imported with an Alerts/Incidents File

| UI Field Name | Accepted CSV/JSON Field Name(s)                               | Notes                              |
| :------------ | :------------------------------------------------------------ | :--------------------------------- |
| ID            | id, incidentid, cloudid, uniqueid                             | \***KEY** - This field is required |
| Name          | name, incidentname, dusplayname                               |                                    |
| Description   | created, createdtime, creationtime, creteddatetime, createdat |                                    |
| Status        | status, incidentstatus, state                                 |                                    |
| Created At    | starttime, start                                              |                                    |
| Start Time    | status, incidentstatus, state                                 |                                    |
| End Time      | endtime, end                                                  |                                    |

## Fields Imported with a Network Services File

| UI Field Name  | Accepted CSV/JSON Field Name(s)                                                                                                                                                                                                     | Notes                                                     |
| :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------- |
| ID             | id, identifier, uniqueid                                                                                                                                                                                                            | \***KEY**                                                 |
| Name           | name, displayname                                                                                                                                                                                                                   | \***KEY**                                                 |
| Cloud ID       | cloudid, linodeid                                                                                                                                                                                                                   | \***KEY**                                                 |
| Cloud Provider | cloudprovider, cloudprovidor                                                                                                                                                                                                        |                                                           |
| Vendor         | vendor, provider, vendorname                                                                                                                                                                                                        |                                                           |
| Asset Type     | instance, instancetype                                                                                                                                                                                                              |                                                           |
| Description    | assettype, txtassettype, type                                                                                                                                                                                                       |                                                           |
| Status         | status, incidentstatus, state                                                                                                                                                                                                       |                                                           |
| Created        | created, creationdate, datecreation                                                                                                                                                                                                 |                                                           |
| Last Seen      | lastmessagetime, lastdiscoveredtime, lastseen, lastcheckin                                                                                                                                                                          |                                                           |
| IPs            | ipaddresstext, ip, ipaddress, ipaddresses, ips, primaryip, endpointipaddress, registerip, sourceip, managementip, privateip, allips, lastip, address, ipaddresslist, ipaddri, ipaddrs, ipaddr, localip, privateipaddresses, ipfirst | This field accepts a comma separated set of IP addresses. |

## Fields Imported with a Certificates File

| UI Field Name             | Accepted CSV/JSON Field Name(s)                                                                                                                                                                                                     | Notes                                                                                                                                                                                                                                                                   |
| :------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID                        | id, identifier, uniqueid, certificateid, certificateremoteid                                                                                                                                                                        | **Key**                                                                                                                                                                                                                                                                 |
| Name                      | name, displayname, certificatename, commonname                                                                                                                                                                                      | **Key**                                                                                                                                                                                                                                                                 |
| Cloud ID                  | cloudid, linodeid                                                                                                                                                                                                                   | **Key**                                                                                                                                                                                                                                                                 |
| Asset Type                | assettype, certificatetype, type                                                                                                                                                                                                    | One of: AWS Certificate, GoDaddy Certificate, Keyfactor Certificate, Webscan Certificate, Network Discovery Certificate, Cloudflare Certificate, CertificateFromKeyVault, ADCS Certificate, CSC DomainManager Certificate, Wiz Certificate, F5-IControl SSL Certificate |
| Create Time               | createtime, created, createdtime, creationtime, createdatetime                                                                                                                                                                      |                                                                                                                                                                                                                                                                         |
| Issuer                    | issuer, issuedby, certificateissuer                                                                                                                                                                                                 | Must be in DN (Distinguished Name) format                                                                                                                                                                                                                               |
| Version                   | version, certificateversion                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                         |
| Serial Number             | serialnumber, serial, certificateserialnumber                                                                                                                                                                                       | **Key**                                                                                                                                                                                                                                                                 |
| Subject                   | subject, issuedto, certificatesubject                                                                                                                                                                                               | Must be in DN (Distinguished Name) format                                                                                                                                                                                                                               |
| Begins On                 | beginson, validfrom, notbefore, startdate                                                                                                                                                                                           |                                                                                                                                                                                                                                                                         |
| Expires On                | expireson, validto, notafter, expirationdate, expiration, expirationtime                                                                                                                                                            |                                                                                                                                                                                                                                                                         |
| Bit Size                  | bitsize, keysize, keylength                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                         |
| Issued Distinguished Name | issueddistinguishedname, distinguishedname, dn                                                                                                                                                                                      |                                                                                                                                                                                                                                                                         |
| Status                    | status, certificatestatus, state                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                         |
| Key Algorithm             | keyalgorithm, keyalg, publickeyalgorithm                                                                                                                                                                                            |                                                                                                                                                                                                                                                                         |
| Signature Algorithm       | signaturealgorithm, signaturealg, sigalgorithm                                                                                                                                                                                      |                                                                                                                                                                                                                                                                         |
| Not Before                | notbefore, validfrom, beginson                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                         |
| Imported At               | importedat, importtime, importedtime                                                                                                                                                                                                |                                                                                                                                                                                                                                                                         |
| Cloud Provider            | cloudprovider, cloudprovidor                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                         |
| Assigned IP Address       | ipaddresstext, ip, ipaddress, ipaddresses, ips, primaryip, endpointipaddress, registerip, sourceip, managementip, privateip, allips, ipfirst, lastip, address, ipaddresslist, ipaddri, ipaddrs, ipaddr, localip, privateipaddresses |                                                                                                                                                                                                                                                                         |