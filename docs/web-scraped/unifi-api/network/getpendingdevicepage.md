# getpendingdevicepage

Source: https://developer.ui.com/network/v10.1.68/getpendingdevicepage

UniFi APIEndpoints combined into Ansible Modules for customized workflows.List Devices Pending AdoptionGET/v1/pending-devicesRetrieve a paginated list of devices pending adoption, including basic device information.
Filterable properties (click to expand)NameTypeAllowed functionsmacAddressSTRINGeq ne in notInipAddressSTRINGeq ne in notInmodelSTRINGeq ne in notInstateSTRINGeq ne in notInsupportedBOOLEANeq nefirmwareVersionSTRINGisNull isNotNull eq ne gt ge lt le like in notInfirmwareUpdatableBOOLEANeq nefeaturesSET(STRING)isEmpty contains containsAny containsAll containsExactlyquery ParametersoffsetintegerlimitintegerfilterstringResponses200Response Schema: application/jsonoffsetrequiredintegerlimitrequiredintegercountrequiredintegertotalCountrequiredintegerdataExpandrequiredArray of object (Device pending adoption)