# DEX Tests | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/dex_tests

[API Reference][Zero Trust][Devices]
# DEX Tests

##### [List Device DEX tests]
GET/accounts/{account_id}/dex/devices/dex_tests
##### [Get Device DEX test]
GET/accounts/{account_id}/dex/devices/dex_tests/{dex_test_id}
##### [Create Device DEX test]
POST/accounts/{account_id}/dex/devices/dex_tests
##### [Update Device DEX test]
PUT/accounts/{account_id}/dex/devices/dex_tests/{dex_test_id}
##### [Delete Device DEX test]
DELETE/accounts/{account_id}/dex/devices/dex_tests/{dex_test_id}
##### ModelsExpand Collapse
SchemaData  { host, kind, method }
The configuration object which contains the details for the WARP client to conduct the test.
host: optional string
The desired endpoint to test.
[]kind: optional string
The type of test.
[]method: optional string
The HTTP request method type.
[][]SchemaHTTP  { data, enabled, interval, 5 more } data: [SchemaData] { host, kind, method }
The configuration object which contains the details for the WARP client to conduct the test.
[]enabled: boolean
Determines whether or not the test is active.
[]interval: string
How often the test will run.
[]name: string
The name of the DEX test. Must be unique.
[]description: optional string
Additional details about the test.
[]target_policies: optional array of  { id, default, name }
Device settings profiles targeted by this test.
id: optional string
The id of the device settings profile.
[]default: optional boolean
Whether the profile is the account default.
[]name: optional string
The name of the device settings profile.
[][]targeted: optional boolean[]test_id: optional string
The unique identifier for the test.
maxLength32[][]DEXTestListResponse  { data, enabled, interval, 5 more } data:  { host, kind, method }
The configuration object which contains the details for the WARP client to conduct the test.
host: string
The desired endpoint to test.
[]kind: "http" or "traceroute"
The type of test.
One of the following:"http"[]"traceroute"[][]method: optional "GET"
The HTTP request method type.
[][]enabled: boolean
Determines whether or not the test is active.
[]interval: string
How often the test will run.
[]name: string
The name of the DEX test. Must be unique.
[]description: optional string
Additional details about the test.
[]target_policies: optional array of  { id, default, name }
DEX rules targeted by this test
id: string
API Resource UUID tag.
maxLength36[]default: optional boolean
Whether the DEX rule is the account default
[]name: optional string
The name of the DEX rule
[][]targeted: optional boolean[]test_id: optional string
The unique identifier for the test.
maxLength32[][]DEXTestGetResponse  { data, enabled, interval, 5 more } data:  { host, kind, method }
The configuration object which contains the details for the WARP client to conduct the test.
host: string
The desired endpoint to test.
[]kind: "http" or "traceroute"
The type of test.
One of the following:"http"[]"traceroute"[][]method: optional "GET"
The HTTP request method type.
[][]enabled: boolean
Determines whether or not the test is active.
[]interval: string
How often the test will run.
[]name: string
The name of the DEX test. Must be unique.
[]description: optional string
Additional details about the test.
[]target_policies: optional array of  { id, default, name }
DEX rules targeted by this test
id: string
API Resource UUID tag.
maxLength36[]default: optional boolean
Whether the DEX rule is the account default
[]name: optional string
The name of the DEX rule
[][]targeted: optional boolean[]test_id: optional string
The unique identifier for the test.
maxLength32[][]DEXTestCreateResponse  { data, enabled, interval, 5 more } data:  { host, kind, method }
The configuration object which contains the details for the WARP client to conduct the test.
host: string
The desired endpoint to test.
[]kind: "http" or "traceroute"
The type of test.
One of the following:"http"[]"traceroute"[][]method: optional "GET"
The HTTP request method type.
[][]enabled: boolean
Determines whether or not the test is active.
[]interval: string
How often the test will run.
[]name: string
The name of the DEX test. Must be unique.
[]description: optional string
Additional details about the test.
[]target_policies: optional array of  { id, default, name }
DEX rules targeted by this test
id: string
API Resource UUID tag.
maxLength36[]default: optional boolean
Whether the DEX rule is the account default
[]name: optional string
The name of the DEX rule
[][]targeted: optional boolean[]test_id: optional string
The unique identifier for the test.
maxLength32[][]DEXTestUpdateResponse  { data, enabled, interval, 5 more } data:  { host, kind, method }
The configuration object which contains the details for the WARP client to conduct the test.
host: string
The desired endpoint to test.
[]kind: "http" or "traceroute"
The type of test.
One of the following:"http"[]"traceroute"[][]method: optional "GET"
The HTTP request method type.
[][]enabled: boolean
Determines whether or not the test is active.
[]interval: string
How often the test will run.
[]name: string
The name of the DEX test. Must be unique.
[]description: optional string
Additional details about the test.
[]target_policies: optional array of  { id, default, name }
DEX rules targeted by this test
id: string
API Resource UUID tag.
maxLength36[]default: optional boolean
Whether the DEX rule is the account default
[]name: optional string
The name of the DEX rule
[][]targeted: optional boolean[]test_id: optional string
The unique identifier for the test.
maxLength32[][]DEXTestDeleteResponse  { dex_tests } dex_tests: optional array of  { data, enabled, interval, 5 more } data:  { host, kind, method }
The configuration object which contains the details for the WARP client to conduct the test.
host: string
The desired endpoint to test.
[]kind: "http" or "traceroute"
The type of test.
One of the following:"http"[]"traceroute"[][]method: optional "GET"
The HTTP request method type.
[][]enabled: boolean
Determines whether or not the test is active.
[]interval: string
How often the test will run.
[]name: string
The name of the DEX test. Must be unique.
[]description: optional string
Additional details about the test.
[]target_policies: optional array of  { id, default, name }
DEX rules targeted by this test
id: string
API Resource UUID tag.
maxLength36[]default: optional boolean
Whether the DEX rule is the account default
[]name: optional string
The name of the DEX rule
[][]targeted: optional boolean[]test_id: optional string
The unique identifier for the test.
maxLength32[][][]