# Fleet Status | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/fleet_status

[API Reference][Zero Trust][Devices]
# Fleet Status

##### [Get the live status of a latest device]
GET/accounts/{account_id}/dex/devices/{device_id}/fleet-status/live
##### ModelsExpand Collapse
FleetStatusGetResponse  { colo, deviceId, mode, 35 more } colo: string
Cloudflare colo
[]deviceId: string
Device identifier (UUID v4)
[]mode: string
The mode under which the WARP client is run
[]platform: string
Operating system
[]status: string
Network status
[]timestamp: string
Timestamp in ISO format
[]version: string
WARP client version
[]alwaysOn: optional boolean[]batteryCharging: optional boolean[]batteryCycles: optional numberformatint64[]batteryPct: optional numberformatfloat[]connectionType: optional string[]cpuPct: optional numberformatfloat[]cpuPctByApp: optional array of array of  { cpu_pct, name } cpu_pct: optional numberformatfloat[]name: optional string[][]deviceIpv4: optional  { address, asn, aso, 3 more } address: optional string[]asn: optional number[]aso: optional string[]location: optional  { city, country_iso, state_iso, zip } city: optional string[]country_iso: optional string[]state_iso: optional string[]zip: optional string[][]netmask: optional string[]version: optional string[][]deviceIpv6: optional  { address, asn, aso, 3 more } address: optional string[]asn: optional number[]aso: optional string[]location: optional  { city, country_iso, state_iso, zip } city: optional string[]country_iso: optional string[]state_iso: optional string[]zip: optional string[][]netmask: optional string[]version: optional string[][]deviceName: optional string
Device identifier (human readable)
[]diskReadBps: optional numberformatint64[]diskUsagePct: optional numberformatfloat[]diskWriteBps: optional numberformatint64[]dohSubdomain: optional string[]estimatedLossPct: optional numberformatfloat[]firewallEnabled: optional boolean[]gatewayIpv4: optional  { address, asn, aso, 3 more } address: optional string[]asn: optional number[]aso: optional string[]location: optional  { city, country_iso, state_iso, zip } city: optional string[]country_iso: optional string[]state_iso: optional string[]zip: optional string[][]netmask: optional string[]version: optional string[][]gatewayIpv6: optional  { address, asn, aso, 3 more } address: optional string[]asn: optional number[]aso: optional string[]location: optional  { city, country_iso, state_iso, zip } city: optional string[]country_iso: optional string[]state_iso: optional string[]zip: optional string[][]netmask: optional string[]version: optional string[][]handshakeLatencyMs: optional numberformatint64[]ispIpv4: optional  { address, asn, aso, 3 more } address: optional string[]asn: optional number[]aso: optional string[]location: optional  { city, country_iso, state_iso, zip } city: optional string[]country_iso: optional string[]state_iso: optional string[]zip: optional string[][]netmask: optional string[]version: optional string[][]ispIpv6: optional  { address, asn, aso, 3 more } address: optional string[]asn: optional number[]aso: optional string[]location: optional  { city, country_iso, state_iso, zip } city: optional string[]country_iso: optional string[]state_iso: optional string[]zip: optional string[][]netmask: optional string[]version: optional string[][]metal: optional string[]networkRcvdBps: optional numberformatint64[]networkSentBps: optional numberformatint64[]networkSsid: optional string[]personEmail: optional string
User contact email address
[]ramAvailableKb: optional numberformatint64[]ramUsedPct: optional numberformatfloat[]ramUsedPctByApp: optional array of array of  { name, ram_used_pct } name: optional string[]ram_used_pct: optional numberformatfloat[][]switchLocked: optional boolean[]wifiStrengthDbm: optional numberformatint64[][]