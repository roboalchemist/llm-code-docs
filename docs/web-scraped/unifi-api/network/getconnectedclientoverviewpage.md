# getconnectedclientoverviewpage

Source: https://developer.ui.com/network/v10.1.68/getconnectedclientoverviewpage

UniFi APIEndpoints combined into Ansible Modules for customized workflows.List Connected ClientsGET/v1/sites/{siteId}/clientsRetrieve a paginated list of all connected clients on a site, including physical devices (computers, smartphones) and active VPN connections.
Filterable properties (click to expand)NameTypeAllowed functionsidUUIDeq ne in notIntypeSTRINGeq ne in notInmacAddressSTRINGisNull isNotNull eq ne in notInipAddressSTRINGisNull isNotNull eq ne in notInconnectedAtTIMESTAMPisNull isNotNull eq ne gt ge lt leaccess.typeSTRINGeq ne in notInaccess.authorizedBOOLEANisNull isNotNull eq nepath ParameterssiteIdrequiredstringquery ParametersoffsetintegerlimitintegerfilterstringResponses200Response Schema: application/jsonoffsetrequiredintegerlimitrequiredintegercountrequiredintegertotalCountrequiredintegerdataExpandrequiredArray of object (Client overview)