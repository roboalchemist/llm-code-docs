# getnetworksoverviewpage

Source: https://developer.ui.com/network/v10.1.68/getnetworksoverviewpage

UniFi APIEndpoints combined into Ansible Modules for customized workflows.List NetworksGET/v1/sites/{siteId}/networksRetrieve a paginated list of all Networks on a site.
Filterable properties (click to expand)NameTypeAllowed functionsmanagementSTRINGeq ne in notInidUUIDeq ne in notInnameSTRINGeq ne in notIn likeenabledBOOLEANeq nevlanIdINTEGEReq ne gt ge lt le in notIndeviceIdUUIDeq ne in notIn isNull isNotNullmetadata.originSTRINGeq ne in notInpath ParameterssiteIdrequiredstringquery ParametersoffsetintegerlimitintegerfilterstringResponses200Response Schema: application/jsonoffsetrequiredintegerlimitrequiredintegercountrequiredintegertotalCountrequiredintegerdataExpandrequiredArray of object (Network overview)