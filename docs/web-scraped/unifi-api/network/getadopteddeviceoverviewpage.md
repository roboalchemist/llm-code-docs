# getadopteddeviceoverviewpage

Source: https://developer.ui.com/network/v10.1.68/getadopteddeviceoverviewpage

UniFi APIEndpoints combined into Ansible Modules for customized workflows.List Adopted DevicesGET/v1/sites/{siteId}/devicesRetrieve a paginated list of all adopted devices on a site, including basic device information.
Filterable properties (click to expand)NameTypeAllowed functionsidUUIDeq ne in notInmacAddressSTRINGeq ne in notInipAddressSTRINGeq ne in notInnameSTRINGeq ne in notIn likemodelSTRINGeq ne in notInstateSTRINGeq ne in notInsupportedBOOLEANeq nefirmwareVersionSTRINGisNull isNotNull eq ne gt ge lt le like in notInfirmwareUpdatableBOOLEANeq nefeaturesSET(STRING)isEmpty contains containsAny containsAll containsExactlyinterfacesSET(STRING)isEmpty contains containsAny containsAll containsExactlypath Parametersquery ParametersResponses200Response Schema: application/json