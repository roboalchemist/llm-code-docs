# getdnspolicypage

Source: https://developer.ui.com/network/v10.1.68/getdnspolicypage

UniFi APIEndpoints combined into Ansible Modules for customized workflows.List DNS PoliciesGET/v1/sites/{siteId}/dns/policiesRetrieve a paginated list of all DNS policies on a site.
Filterable properties (click to expand)NameTypeAllowed functionstypeSTRINGeq ne in notInidUUIDeq ne in notInenabledBOOLEANeq nedomainSTRINGeq ne in notIn likeipv4AddressSTRINGeq ne in notIn likeipv6AddressSTRINGeq ne in notIn liketargetDomainSTRINGeq ne in notIn likemailServerDomainSTRINGeq ne in notIn liketextSTRINGeq ne in notIn likeserverDomainSTRINGeq ne in notIn likeipAddressSTRINGeq ne in notIn likettlSecondsINTEGEReq ne gt ge lt le in notInpriorityINTEGEReq ne gt ge lt le in notInserviceSTRINGeq ne in notInprotocolSTRINGeq ne in notInportINTEGEReq ne gt ge lt le in notInweightINTEGEReq ne gt ge lt le in notInpath Parametersquery ParametersResponses200Response Schema: application/json