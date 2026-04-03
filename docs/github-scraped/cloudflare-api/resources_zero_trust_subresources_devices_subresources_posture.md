# Posture | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/posture

[API Reference][Zero Trust][Devices]
# Posture

##### [List device posture rules]
GET/accounts/{account_id}/devices/posture
##### [Get device posture rule details]
GET/accounts/{account_id}/devices/posture/{rule_id}
##### [Create a device posture rule]
POST/accounts/{account_id}/devices/posture
##### [Update a device posture rule]
PUT/accounts/{account_id}/devices/posture/{rule_id}
##### [Delete a device posture rule]
DELETE/accounts/{account_id}/devices/posture/{rule_id}
##### ModelsExpand Collapse
CarbonblackInput = string[]ClientCertificateInput  { certificate_id, cn } certificate_id: string
UUID of Cloudflare managed certificate.
maxLength36[]cn: string
Common Name that is protected by the certificate.
[][]CrowdstrikeInput  { connection_id, last_seen, operator, 6 more } connection_id: string
Posture Integration ID.
[]last_seen: optional string
For more details on last seen, please refer to the Crowdstrike documentation.
[]operator: optional "<" or "<=" or ">" or 2 more
Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][]os: optional string
Os Version.
[]overall: optional string
Overall.
[]sensor_config: optional string
SensorConfig.
[]state: optional "online" or "offline" or "unknown"
For more details on state, please refer to the Crowdstrike documentation.
One of the following:"online"[]"offline"[]"unknown"[][]version: optional string
Version.
[]versionOperator: optional "<" or "<=" or ">" or 2 more
Version Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][][]DeviceInput = [FileInput] { operating_system, path, exists, 2 more }  or [UniqueClientIDInput] { id, operating_system }  or [DomainJoinedInput] { operating_system, domain }  or 17 more
The value to be checked against.
One of the following:FileInput  { operating_system, path, exists, 2 more } operating_system: "windows" or "linux" or "mac"
Operating system.
One of the following:"windows"[]"linux"[]"mac"[][]path: string
File path.
[]exists: optional boolean
Whether or not file exists.
[]sha256: optional string
SHA-256.
[]thumbprint: optional string
Signing certificate thumbprint.
[][]UniqueClientIDInput  { id, operating_system } id: string
List ID.
[]operating_system: "android" or "ios" or "chromeos"
Operating System.
One of the following:"android"[]"ios"[]"chromeos"[][][]DomainJoinedInput  { operating_system, domain } operating_system: "windows"
Operating System.
[]domain: optional string
Domain.
[][]OSVersionInput  { operating_system, operator, version, 3 more } operating_system: "windows"
Operating System.
[]operator: "<" or "<=" or ">" or 2 more
Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][]version: string
Version of OS.
[]os_distro_name: optional string
Operating System Distribution Name (linux only).
[]os_distro_revision: optional string
Version of OS Distribution (linux only).
[]os_version_extra: optional string
Additional operating system version details. For Windows, the UBR (Update Build Revision). For Mac or iOS, the Product Version Extra. For Linux, the distribution name and version.
[][]FirewallInput  { enabled, operating_system } enabled: boolean
Enabled.
[]operating_system: "windows" or "mac"
Operating System.
One of the following:"windows"[]"mac"[][][]SentineloneInput  { operating_system, path, sha256, thumbprint } operating_system: "windows" or "linux" or "mac"
Operating system.
One of the following:"windows"[]"linux"[]"mac"[][]path: string
File path.
[]sha256: optional string
SHA-256.
[]thumbprint: optional string
Signing certificate thumbprint.
[][]TeamsDevicesCarbonblackInputRequest  { operating_system, path, sha256, thumbprint } operating_system: "windows" or "linux" or "mac"
Operating system.
One of the following:"windows"[]"linux"[]"mac"[][]path: string
File path.
[]sha256: optional string
SHA-256.
[]thumbprint: optional string
Signing certificate thumbprint.
[][]TeamsDevicesAccessSerialNumberListInputRequest  { id } id: string
UUID of Access List.
maxLength36[][]DiskEncryptionInput  { checkDisks, requireAll } checkDisks: optional array of [CarbonblackInput]
List of volume names to be checked for encryption.
[]requireAll: optional boolean
Whether to check all disks for encryption.
[][]TeamsDevicesApplicationInputRequest  { operating_system, path, sha256, thumbprint } operating_system: "windows" or "linux" or "mac"
Operating system.
One of the following:"windows"[]"linux"[]"mac"[][]path: string
Path for the application.
[]sha256: optional string
SHA-256.
[]thumbprint: optional string
Signing certificate thumbprint.
[][]ClientCertificateInput  { certificate_id, cn } certificate_id: string
UUID of Cloudflare managed certificate.
maxLength36[]cn: string
Common Name that is protected by the certificate.
[][]TeamsDevicesClientCertificateV2InputRequest  { certificate_id, check_private_key, operating_system, 4 more } certificate_id: string
UUID of Cloudflare managed certificate.
maxLength36[]check_private_key: boolean
Confirm the certificate was not imported from another device. We recommend keeping this enabled unless the certificate was deployed without a private key.
[]operating_system: "windows" or "linux" or "mac"
Operating system.
One of the following:"windows"[]"linux"[]"mac"[][]cn: optional string
Certificate Common Name. This may include one or more variables in the ${ } notation. Only ${serial_number} and ${hostname} are valid variables.
[]extended_key_usage: optional array of "clientAuth" or "emailProtection"
List of values indicating purposes for which the certificate public key can be used.
One of the following:"clientAuth"[]"emailProtection"[][]locations: optional  { paths, trust_stores } paths: optional array of string
List of paths to check for client certificate on linux.
[]trust_stores: optional array of "system" or "user"
List of trust stores to check for client certificate.
One of the following:"system"[]"user"[][][]subject_alternative_names: optional array of string
List of certificate Subject Alternative Names.
[][]TeamsDevicesAntivirusInputRequest  { update_window_days } update_window_days: optional number
Number of days that the antivirus should be updated within.
[][]WorkspaceOneInput  { compliance_status, connection_id } compliance_status: "compliant" or "noncompliant" or "unknown"
Compliance Status.
One of the following:"compliant"[]"noncompliant"[]"unknown"[][]connection_id: string
Posture Integration ID.
[][]CrowdstrikeInput  { connection_id, last_seen, operator, 6 more } connection_id: string
Posture Integration ID.
[]last_seen: optional string
For more details on last seen, please refer to the Crowdstrike documentation.
[]operator: optional "<" or "<=" or ">" or 2 more
Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][]os: optional string
Os Version.
[]overall: optional string
Overall.
[]sensor_config: optional string
SensorConfig.
[]state: optional "online" or "offline" or "unknown"
For more details on state, please refer to the Crowdstrike documentation.
One of the following:"online"[]"offline"[]"unknown"[][]version: optional string
Version.
[]versionOperator: optional "<" or "<=" or ">" or 2 more
Version Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][][]IntuneInput  { compliance_status, connection_id } compliance_status: "compliant" or "noncompliant" or "unknown" or 3 more
Compliance Status.
One of the following:"compliant"[]"noncompliant"[]"unknown"[]"notapplicable"[]"ingraceperiod"[]"error"[][]connection_id: string
Posture Integration ID.
[][]KolideInput  { connection_id, countOperator, issue_count } connection_id: string
Posture Integration ID.
[]countOperator: "<" or "<=" or ">" or 2 more
Count Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][]issue_count: string
The Number of Issues.
[][]TaniumInput  { connection_id, eid_last_seen, operator, 3 more } connection_id: string
Posture Integration ID.
[]eid_last_seen: optional string
For more details on eid last seen, refer to the Tanium documentation.
[]operator: optional "<" or "<=" or ">" or 2 more
Operator to evaluate risk_level or eid_last_seen.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][]risk_level: optional "low" or "medium" or "high" or "critical"
For more details on risk level, refer to the Tanium documentation.
One of the following:"low"[]"medium"[]"high"[]"critical"[][]scoreOperator: optional "<" or "<=" or ">" or 2 more
Score Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][]total_score: optional number
For more details on total score, refer to the Tanium documentation.
[][]SentineloneS2sInput  { connection_id, active_threats, infected, 4 more } connection_id: string
Posture Integration ID.
[]active_threats: optional number
The Number of active threats.
[]infected: optional boolean
Whether device is infected.
[]is_active: optional boolean
Whether device is active.
[]network_status: optional "connected" or "disconnected" or "disconnecting" or "connecting"
Network status of device.
One of the following:"connected"[]"disconnected"[]"disconnecting"[]"connecting"[][]operational_state: optional "na" or "partially_disabled" or "auto_fully_disabled" or 4 more
Agent operational state.
One of the following:"na"[]"partially_disabled"[]"auto_fully_disabled"[]"fully_disabled"[]"auto_partially_disabled"[]"disabled_error"[]"db_corruption"[][]operator: optional "<" or "<=" or ">" or 2 more
Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][][]TeamsDevicesCustomS2sInputRequest  { connection_id, operator, score } connection_id: string
Posture Integration ID.
[]operator: "<" or "<=" or ">" or 2 more
Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][]score: number
A value between 0-100 assigned to devices set by the 3rd party posture provider.
[][][]DeviceMatch  { platform } platform: optional "windows" or "mac" or "linux" or 3 moreOne of the following:"windows"[]"mac"[]"linux"[]"android"[]"ios"[]"chromeos"[][][]DevicePostureRule  { id, description, expiration, 5 more } id: optional string
API UUID.
maxLength36[]description: optional string
The description of the device posture rule.
[]expiration: optional string
Sets the expiration time for a posture check result. If empty, the result remains valid until it is overwritten by new data from the WARP client.
[]input: optional [DeviceInput]
The value to be checked against.
[]match: optional array of [DeviceMatch] { platform }
The conditions that the client must match to run the rule.
platform: optional "windows" or "mac" or "linux" or 3 moreOne of the following:"windows"[]"mac"[]"linux"[]"android"[]"ios"[]"chromeos"[][][]name: optional string
The name of the device posture rule.
[]schedule: optional string
Polling frequency for the WARP client posture check. Default: `5m` (poll every five minutes). Minimum: `1m`.
[]type: optional "file" or "application" or "tanium" or 20 more
The type of device posture rule.
One of the following:"file"[]"application"[]"tanium"[]"gateway"[]"warp"[]"disk_encryption"[]"serial_number"[]"sentinelone"[]"carbonblack"[]"firewall"[]"os_version"[]"domain_joined"[]"client_certificate"[]"client_certificate_v2"[]"antivirus"[]"unique_client_id"[]"kolide"[]"tanium_s2s"[]"crowdstrike_s2s"[]"intune"[]"workspace_one"[]"sentinelone_s2s"[]"custom_s2s"[][][]DiskEncryptionInput  { checkDisks, requireAll } checkDisks: optional array of [CarbonblackInput]
List of volume names to be checked for encryption.
[]requireAll: optional boolean
Whether to check all disks for encryption.
[][]DomainJoinedInput  { operating_system, domain } operating_system: "windows"
Operating System.
[]domain: optional string
Domain.
[][]FileInput  { operating_system, path, exists, 2 more } operating_system: "windows" or "linux" or "mac"
Operating system.
One of the following:"windows"[]"linux"[]"mac"[][]path: string
File path.
[]exists: optional boolean
Whether or not file exists.
[]sha256: optional string
SHA-256.
[]thumbprint: optional string
Signing certificate thumbprint.
[][]FirewallInput  { enabled, operating_system } enabled: boolean
Enabled.
[]operating_system: "windows" or "mac"
Operating System.
One of the following:"windows"[]"mac"[][][]IntuneInput  { compliance_status, connection_id } compliance_status: "compliant" or "noncompliant" or "unknown" or 3 more
Compliance Status.
One of the following:"compliant"[]"noncompliant"[]"unknown"[]"notapplicable"[]"ingraceperiod"[]"error"[][]connection_id: string
Posture Integration ID.
[][]KolideInput  { connection_id, countOperator, issue_count } connection_id: string
Posture Integration ID.
[]countOperator: "<" or "<=" or ">" or 2 more
Count Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][]issue_count: string
The Number of Issues.
[][]OSVersionInput  { operating_system, operator, version, 3 more } operating_system: "windows"
Operating System.
[]operator: "<" or "<=" or ">" or 2 more
Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][]version: string
Version of OS.
[]os_distro_name: optional string
Operating System Distribution Name (linux only).
[]os_distro_revision: optional string
Version of OS Distribution (linux only).
[]os_version_extra: optional string
Additional operating system version details. For Windows, the UBR (Update Build Revision). For Mac or iOS, the Product Version Extra. For Linux, the distribution name and version.
[][]SentineloneInput  { operating_system, path, sha256, thumbprint } operating_system: "windows" or "linux" or "mac"
Operating system.
One of the following:"windows"[]"linux"[]"mac"[][]path: string
File path.
[]sha256: optional string
SHA-256.
[]thumbprint: optional string
Signing certificate thumbprint.
[][]SentineloneS2sInput  { connection_id, active_threats, infected, 4 more } connection_id: string
Posture Integration ID.
[]active_threats: optional number
The Number of active threats.
[]infected: optional boolean
Whether device is infected.
[]is_active: optional boolean
Whether device is active.
[]network_status: optional "connected" or "disconnected" or "disconnecting" or "connecting"
Network status of device.
One of the following:"connected"[]"disconnected"[]"disconnecting"[]"connecting"[][]operational_state: optional "na" or "partially_disabled" or "auto_fully_disabled" or 4 more
Agent operational state.
One of the following:"na"[]"partially_disabled"[]"auto_fully_disabled"[]"fully_disabled"[]"auto_partially_disabled"[]"disabled_error"[]"db_corruption"[][]operator: optional "<" or "<=" or ">" or 2 more
Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][][]TaniumInput  { connection_id, eid_last_seen, operator, 3 more } connection_id: string
Posture Integration ID.
[]eid_last_seen: optional string
For more details on eid last seen, refer to the Tanium documentation.
[]operator: optional "<" or "<=" or ">" or 2 more
Operator to evaluate risk_level or eid_last_seen.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][]risk_level: optional "low" or "medium" or "high" or "critical"
For more details on risk level, refer to the Tanium documentation.
One of the following:"low"[]"medium"[]"high"[]"critical"[][]scoreOperator: optional "<" or "<=" or ">" or 2 more
Score Operator.
One of the following:"<"[]"<="[]">"[]">="[]"=="[][]total_score: optional number
For more details on total score, refer to the Tanium documentation.
[][]UniqueClientIDInput  { id, operating_system } id: string
List ID.
[]operating_system: "android" or "ios" or "chromeos"
Operating System.
One of the following:"android"[]"ios"[]"chromeos"[][][]WorkspaceOneInput  { compliance_status, connection_id } compliance_status: "compliant" or "noncompliant" or "unknown"
Compliance Status.
One of the following:"compliant"[]"noncompliant"[]"unknown"[][]connection_id: string
Posture Integration ID.
[][]PostureDeleteResponse  { id } id: optional string
API UUID.
maxLength36[][]
#### PostureIntegrations

##### [List your device posture integrations]
GET/accounts/{account_id}/devices/posture/integration
##### [Get device posture integration details]
GET/accounts/{account_id}/devices/posture/integration/{integration_id}
##### [Create a device posture integration]
POST/accounts/{account_id}/devices/posture/integration
##### [Update a device posture integration]
PATCH/accounts/{account_id}/devices/posture/integration/{integration_id}
##### [Delete a device posture integration]
DELETE/accounts/{account_id}/devices/posture/integration/{integration_id}
##### ModelsExpand Collapse
Integration  { id, config, interval, 2 more } id: optional string
API UUID.
maxLength36[]config: optional  { api_url, auth_url, client_id }
The configuration object containing third-party integration information.
api_url: string
The Workspace One API URL provided in the Workspace One Admin Dashboard.
[]auth_url: string
The Workspace One Authorization URL depending on your region.
[]client_id: string
The Workspace One client ID provided in the Workspace One Admin Dashboard.
[][]interval: optional string
The interval between each posture check with the third-party API. Use `m` for minutes (e.g. `5m`) and `h` for hours (e.g. `12h`).
[]name: optional string
The name of the device posture integration.
[]type: optional "workspace_one" or "crowdstrike_s2s" or "uptycs" or 5 more
The type of device posture integration.
One of the following:"workspace_one"[]"crowdstrike_s2s"[]"uptycs"[]"intune"[]"kolide"[]"tanium_s2s"[]"sentinelone_s2s"[]"custom_s2s"[][][]IntegrationDeleteResponse = unknown or stringOne of the following:unknown[]string[][]