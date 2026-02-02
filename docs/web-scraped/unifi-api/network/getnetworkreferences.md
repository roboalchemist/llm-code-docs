# getnetworkreferences

Source: https://developer.ui.com/network/v10.1.68/getnetworkreferences

UniFi APIEndpoints combined into Ansible Modules for customized workflows.Get Network ReferencesGET/v1/sites/{siteId}/networks/{networkId}/referencesRetrieve references to a specific network.path ParametersnetworkIdrequiredstringsiteIdrequiredstringResponses200Response Schema: application/jsonreferenceResourcesExpandrequiredArray of object (Network reference resource)List of network reference resources