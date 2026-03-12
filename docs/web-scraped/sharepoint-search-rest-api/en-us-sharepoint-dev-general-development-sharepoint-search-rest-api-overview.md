# Source: https://learn.microsoft.com/en-us/sharepoint/dev/general-development/sharepoint-search-rest-api-overview

Title: SharePoint Search REST API overview

URL Source: https://learn.microsoft.com/en-us/sharepoint/dev/general-development/sharepoint-search-rest-api-overview

Markdown Content:
Add search functionality to client and mobile applications using the Search REST service in SharePoint and any technology that supports REST web requests.

When you query in the context of a SharePoint Online user, you get results from:

* Content in SharePoint Online site collections
* Content in Microsoft 365 groups
* Shared OneDrive for Business content (content that's accessible for others than the owner of the OneDrive for Business)
* Content from SharePoint Server that's been indexed via a cloud search Service application. [Learn about cloud hybrid search.](https://learn.microsoft.com/en-us/sharepoint/hybrid/learn-about-cloud-hybrid-search-for-sharepoint)

If the Office 365 Private or Public CDN is enabled to optimize performance for assets then this section applies to you. If your search results contain images that are served from the CDN, then the URL for the image will be the CDN URL that is returned in the results and not the asset library location. For more information on CDN please review [Use the Office 365 Content Delivery Network (CDN) with SharePoint Online](https://aka.ms/spocdn).

Search in SharePoint includes a Search REST service you can use to add search functionality to your client and mobile applications by using any technology that supports REST web requests. You can use the Search REST service to submit Keyword Query Language (KQL) or FAST Query Language (FQL) queries in your SharePoint Add-ins, remote client applications, mobile applications, and other applications. The Search REST service supports both HTTP **POST** and HTTP **GET** requests.

Construct the URI for query **GET** requests to the Search REST service as follows:

```
GET /_api/search/query
```

For **GET** requests, you specify the query parameters in the URL. You can construct the **GET** request URL in two ways:

```
GET http://server/_api/search/query?query_parameter=value&amp;query_parameter=value
GET http://server/_api/search/query(query_parameter=value&amp;query_parameter=<value>)
```

You construct the URI for query **POST** requests to the Search REST service as follows:

```
POST /_api/search/postquery
```

For **POST** requests, you pass the query parameters in the request in JavaScript Object Notation (JSON) format. The HTTP **POST** version of the Search REST service supports all parameters supported by the HTTP **GET** version. However, some of the parameters have different data types, as described in Table 1.

**Table 1. Query parameters with different data types for POST requests**

| Parameter | Data type |
| --- | --- |
| [SelectProperties](https://learn.microsoft.com/en-us/sharepoint/dev/general-development/sharepoint-search-rest-api-overview#selectproperties) | string[] |
| [RefinementFilters](https://learn.microsoft.com/en-us/sharepoint/dev/general-development/sharepoint-search-rest-api-overview#refinementfilters) | string[] |
| [SortList](https://learn.microsoft.com/en-us/sharepoint/dev/general-development/sharepoint-search-rest-api-overview#sortlist) | [Sort](https://msdn.microsoft.com/library/Microsoft.SharePoint.Client.Search.Query.Sort.aspx) |
| [HitHighlightedProperties](https://learn.microsoft.com/en-us/sharepoint/dev/general-development/sharepoint-search-rest-api-overview#hithighlightedproperties) | string[] |
| [Properties](https://learn.microsoft.com/en-us/sharepoint/dev/general-development/sharepoint-search-rest-api-overview#properties) | [Microsoft.SharePoint.Client.Search.Query.KeywordQueryProperties](https://msdn.microsoft.com/library/Microsoft.SharePoint.Client.Search.Query.KeywordQueryProperties.aspx) |

Use **POST** requests in the following scenarios:

* When you'll exceed the URL length restriction with a **GET** request.
* When you can't specify the query parameters in a simple URL. For example, if you have to pass parameter values that contain a complex type array, or comma-separated strings, you have more flexibility when constructing the **POST** request.
* When you use the [ReorderingRules](https://learn.microsoft.com/en-us/sharepoint/dev/general-development/sharepoint-search-rest-api-overview#reorderingrules) parameter because it is supported only with **POST** requests.

By default, results are returned in XML format. To get results in JSON format, add the following header to your request:

```
accept: application/json;odata=verbose
```

If you don't need metadata, you can instead use:

```
accept: application/json;odata=nometadata
```

When you make a call to the Search REST service, you specify query parameters with the request. Search in SharePoint uses these query parameters to construct the search query. With a **GET** request, you specify the query parameters in the URL. For **POST** requests, you pass the query parameters in the body in JavaScript Object Notation (JSON) format. The following sections describe the query parameters you can use to submit search queries with the Search REST service.

A string that contains the text for the search query.

```
GET http://{server}/_api/search/query?querytext='sharepoint'
```

```
{
  'request': {
    'Querytext': 'sharepoint',
    'RowLimit': 20,
    'ClientType': 'ContentSearchRegular'
  }
}
```

A string that contains the text that replaces the query text, as part of a query transform.

```
GET http://server/_api/search/query?querytext='sharepoint'&amp;querytemplate='{searchterms} author:johndoe'
```

```
{
  '__metadata': {
      'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
   },
  'Querytext': 'sharepoint',
  'QueryTemplate': '{searchterms} Author:johndoe'
}
```

A Boolean value that specifies whether the result tables that are returned for the result block are mixed with the result tables that are returned for the original query.

**true** to mix the ResultTables; otherwise, **false**. The default value is **true**.

Change this value only if you want to provide your own interleaving implementation.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;enableinterleaving=true
```

```
{
  '__metadata': {
      'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  '​EnableInterleaving': 'True'
}
```

The result source ID to use for executing the search query.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;sourceid='8413cd39-2156-4e00-b54d-11efd9abdb89'
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'SourceId': '8413cd39-2156-4e00-b54d-11efd9abdb89'
}
```

The ID of the ranking model to use for the query.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;rankingmodelid​= _CustomRankingModelID_
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'RankingModelId': 'CustomRankingModelID '
}
```

The first row that is included in the search results that are returned. You use this parameter when you want to implement paging for search results.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;startrow=10
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'StartRow': '10'
}
```

Note

Please be aware that in order to provide search experience with high performance, we limit the maximum supported value of `StartRow` to be **50,000**. If you need to page through larger result sets, please see [Pagination for large result sets.](https://learn.microsoft.com/en-us/sharepoint/dev/general-development/pagination-for-large-result-sets)

The maximum number of rows overall that are returned in the search results. Compared to _RowsPerPage_, _RowLimit_ is the maximum number of rows returned overall.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;rowlimit=30
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'RowLimit': '30'
}
```

The maximum number of rows to return per page. Compared to _RowLimit_, _RowsPerPage_ refers to the maximum number of rows to return per page, and is used primarily when you want to implement paging for search results.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;rowsperpage=10
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'RowsPerPage': '10'
}
```

The managed properties to return in the search results. To return a managed property, set the property's retrievable flag to **true** in the search schema.

For **GET** requests, you specify the _SelectProperties_ parameter in a string containing a comma-separated list of properties. For **POST** requests, you specify the _SelectProperties_ parameter as a string array.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;selectproperties='Title,Author'
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'SelectProperties': {
    'results': ['Title','Author']
  }
}
```

The locale ID (LCID) for the query (see [Locale IDs Assigned by Microsoft](https://msdn.microsoft.com/goglobal/bb964664.aspx)).

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;culture=1044
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'Culture': '1044'
}
```

The set of refinement filters used when issuing a refinement query. For **GET** requests, the _RefinementFilters_ parameter is specified as an FQL filter. For **POST** requests, the _RefinementFilters_ parameter is specified as an array of FQL filters.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;refinementfilters='fileExtension:equals("docx")'
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'RefinementFilters': {
    'results': ['fileExtension:equals("docx")']
  }
}
```

The set of refiners to return in a search result.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;refiners='author,size'
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'Refiners': 'author,size',
}
```

The additional query terms to append to the query.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;hiddenconstraints='developer'
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'HiddenConstraints': 'developer'
}
```

The list of properties by which the search results are ordered.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;sortlist='rank:descending,modifiedby:ascending'
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'SortList': {
    'results': [
      {
        'Property': 'Created',
        'Direction': '0'
      },
      {
        'Property': 'FileExtension',
        'Direction': '1'
      }
    ]
  }
}
```

A Boolean value that specifies whether stemming is enabled.

**true** if the stemming is enabled; otherwise, **false**. The default value is **true**.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;enablestemming=false
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'EnableStemming : 'False'
}
```

A Boolean value that specifies whether duplicate items are removed from the results.

**true** to remove the duplicate items; otherwise, **false**. The default value is **true**.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;trimduplicates=false
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'TrimDuplicates': 'False'
}
```

The amount of time in milliseconds before the query request times out. The default value is 30000.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;timeout=60000
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'Timeout': '60000'
}
```

A Boolean value that specifies whether the exact terms in the search query are used to find matches, or if nicknames are used also. **true** if nicknames are used; otherwise, **false**. The default value is **false**.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;enablenicknames=true
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'EnableNicknames': 'True'
}
```

A Boolean value that specifies whether the phonetic forms of the query terms are used to find matches.

**true** if phonetic forms are used; otherwise, **false**. The default value is **false**.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;enablephonetic=true
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'EnablePhonetic': 'True'
}
```

A Boolean value that specifies whether the query uses the FAST Query Language (FQL).

**true** if the query is an FQL query; otherwise, **false**. The default value is **false**.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;enablefql=true
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'EnableFQL': 'True'
}
```

The properties to highlight in the search result summary when the property value matches the search terms entered by the user. For **GET** requests, Specify in a string containing a comma-separated list of properties. For **POST** requests, specify as an array of strings.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;hithighlightedproperties='Title'
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'HitHighlightedProperties':  {
    'results': ['Title']
  }
}
```

A Boolean value that specifies whether to perform result type processing for the query.

**false** to perform result type processing; otherwise, **true**. The default value is **true**.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;bypassresulttypes=true
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'BypassResultTypes': 'true'
}
```

A Boolean value that specifies whether to return best bet results for the query.

**true** to return best bets; otherwise, **false**. This parameter is used only when **EnableQueryRules** is set to **true**, otherwise it is ignored. The default value is **false**.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;processbestbets=true&amp;enablequeryrules=true
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'ProcessBestBets': 'true',
  'EnableQueryRules': 'true'
}
```

The type of the client that issued the query.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;clienttype='custom'
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'ClientType': 'custom'
}
```

The GUID for the user who submitted the search query.

```
GET http:// _\<server\>_/_api/search/query?querytext='sharepoint'&amp;personalizationdata=' _\<GUID\>_'
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'PersonalizationData': ' <GUID> '
}
```

The URL for the search results page.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;resultsurl='http://server/site/resultspage.aspx'
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint'
  'ResultURL': 'http://server/site/resultspage.aspx'
}
```

Custom tags that identify the query. You can specify multiple query tags, separated by semicolons.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint'
}
```

Additional properties for the query. **GET** requests support only string values. **POST** requests support values of any type.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;properties='termid:guid'
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'Properties': {
    'results': [
      {
        'Name': 'sampleBooleanProperty',
        'Value':
        {
          'BoolVal': 'True',
          'QueryPropertyValueTypeIndex': 3
        }
      },
      {
        'Name': 'sampleIntProperty',
        'Value':
        {
          'IntVal': '1234',
          'QueryPropertyValueTypeIndex': 2
        }
      }
    ]
  }
}
```

A Boolean value that specifies whether to enable query rules for the query.

**true** to enable query rules; otherwise, **false**. The default value is **true**.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;enablequeryrules=false
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'EnableQueryRules': 'false'
}
```

Special rules for reordering search results. These rules can specify that documents matching certain conditions are ranked higher or lower in the results. This property applies only when search results are sorted based on rank. You must use a **POST** request for this property; it does not work in a **GET** request.

In the following example, _MatchType_ refers to [ReorderingRuleMatchType](https://learn.microsoft.com/en-us/previous-versions/office/sharepoint-server/jj276975(v=office.15)) . In the following example, `'MatchType': '0'` specifies `ResultContainsKeyword`.

```
{
  '__metadata': {
  'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'ReorderingRules':  {
    'results': [
    {
      'MatchValue': '<someValue>',
      'Boost': '10',
      'MatchType': '0'
    }
    ]
  }
}
```

A Boolean value that specifies whether to return personal favorites with the search results.

**true** to return personal favorites; otherwise **false**.

```
GET http://_server_/_api/search/query?querytext='sharepoint'&amp;processpersonalfavorites=true
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext ': 'sharepoint',
  'ProcessPersonalFavorites': 'false'
}
```

The location of the _queryparametertemplate.xml_ file. This file is used to enable anonymous users to make Search REST queries.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;querytemplatepropertiesurl='spfile://webroot/queryparametertemplate.xml'
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext ': 'sharepoint',
  QueryTemplatePropertiesUrl : 'spfile://webroot/queryparametertemplate.xml'
}
```

The number of properties to show hit highlighting for in the search results.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;hithighlightedmultivaluepropertylimit=2
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext ': 'sharepoint',
  'HitHighlihtedMultivaluePropertyLimit': '2'
}
```

A Boolean value that specifies whether the hit highlighted properties can be ordered.

**true** to enable ordering rules; otherwise **false**.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;enableorderinghithighlightedproperty=false
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext ': 'sharepoint',
  'EnableOrderingHitHighlightedProperty': 'false'
}
```

The managed properties that are used to determine how to collapse individual search results. Results are collapsed into one or a specified number of results if they match any of the individual collapse specifications. Within a single collapse specification, results are collapsed if their properties match all individual properties in the collapse specification.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;collapsespecification='Author:1 ContentType:2'
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext ': 'sharepoint',
  'CollapseSpecification': 'Author:1 ContentType:2'
}
```

A Boolean value that specifies whether to sort search results.

**true** to sort search results using _SortList_, or by rank if _SortList_ is empty. **false** to leave results unsorted.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;enablesorting=false
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext ': 'sharepoint',
  'EnableSorting': 'false'
}
```

A Boolean value that specifies whether to return block rank log information in the **BlockRankLog** property of the interleaved result table. A block rank log contains the textual information on the block score and the documents that were de-duplicated.

**true** to return block rank log information; otherwise, **false**.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;generateblockranklog=true
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext ': 'sharepoint',
  'GenerateBlockRankLog': 'true'
}
```

The locale identifier (LCID) of the user interface (see [Locale IDs Assigned by Microsoft](https://msdn.microsoft.com/goglobal/bb964664)).

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;uilanguage=1044
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext ': 'sharepoint',
  'UILanguage': '1044'
}
```

The preferred number of characters to display in the hit-highlighted summary generated for a search result.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;desiredsnippetlength=80
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext ': 'sharepoint',
  'DesiredSnippetLength': '80'
}
```

The maximum number of characters to display in the hit-highlighted summary generated for a search result.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;maxsnippetlength=100
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext ': 'sharepoint',
  'MaxSnippetLength': '100'
}
```

The number of characters to display in the result summary for a search result.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;summarylength=150
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext ': 'sharepoint',
  'Summarylength': '150'
}
```

A Boolean value that specifies whether to include the results from private Microsoft 365 groups.

**true** to include results from private Microsoft 365 groups; otherwise, **false**. The default value is **false**.

```
GET http:// _server_/_api/search/query?querytext='sharepoint'&amp;Properties='EnableDynamicGroups:true'
```

```
{
  '__metadata': {
    'type': 'Microsoft.Office.Server.Search.REST.SearchRequest'
  },
  'Querytext': 'sharepoint',
  'Properties': {
  'results': [ {
    'Name': 'EnableDynamicGroups',
    'Value': { 'BoolVal': true }
  }]
}
```

You can configure search to support Search REST queries from anonymous users. Site administrators can decide what query parameters to expose to anonymous users by using the _queryparametertemplate.xml_ file. This section describes how to configure your site to enable anonymous access, and create the queryparametertemplate.xml file.

1. Enable anonymous access on the web application and publishing site. For more information about how to do this, see [Manage permission policies for a web application in SharePoint](https://technet.microsoft.com/library/ff608071.aspx) and [Plan for user authentication methods in SharePoint](https://technet.microsoft.com/library/cc262350.aspx) on [TechNet](https://technet.microsoft.com/).

2. Add a new document library named QueryPropertiesTemplate to the publishing site.

3. Create an XML file named queryparametertemplate.xml, and copy the following XML to the file.

```
<QueryPropertiesTemplate xmlns="https://www.microsoft.com/sharepoint/search/KnownTypes/2008/08" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
  <QueryProperties i:type="KeywordQueryProperties">
    <EnableStemming>true</EnableStemming>
    <FarmId>FarmID</FarmId>
    <IgnoreAllNoiseQuery>true</IgnoreAllNoiseQuery>
    <KeywordInclusion>AllKeywords</KeywordInclusion>
    <SiteId>SiteID</SiteId>
    <SummaryLength>180</SummaryLength>
    <TrimDuplicates>true</TrimDuplicates>
    <WcfTimeout>120000</WcfTimeout>
    <WebId>WebID</WebId>
    <Properties xmlns:a="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
      <a:KeyValueOfstringanyType>
        <a:Key>_IsEntSearchLicensed</a:Key>
        <a:Value i:type="b:boolean" xmlns:b="http://www.w3.org/2001/XMLSchema">true</a:Value>
      </a:KeyValueOfstringanyType>
      <a:KeyValueOfstringanyType>
        <a:Key>EnableSorting</a:Key>
        <a:Value i:type="b:boolean" xmlns:b="http://www.w3.org/2001/XMLSchema">true</a:Value>
      </a:KeyValueOfstringanyType>
      <a:KeyValueOfstringanyType>
        <a:Key>MaxKeywordQueryTextLength</a:Key>
        <a:Value i:type="b:int" xmlns:b="http://www.w3.org/2001/XMLSchema">4096</a:Value>
      </a:KeyValueOfstringanyType>
      <a:KeyValueOfstringanyType>
        <a:Key>TryCache</a:Key>
        <a:Value i:type="b:boolean" xmlns:b="http://www.w3.org/2001/XMLSchema">true</a:Value>
      </a:KeyValueOfstringanyType>
    </Properties>
    <PropertiesContractVersion>15.0.0.0</PropertiesContractVersion>
    <EnableFQL>false</EnableFQL>
    <EnableSpellcheck>Suggest</EnableSpellcheck>
    <EnableUrlSmashing>true</EnableUrlSmashing>
    <IsCachable>false</IsCachable>
    <MaxShallowRefinementHits>100</MaxShallowRefinementHits>
    <MaxSummaryLength>185</MaxSummaryLength>
    <MaxUrlLength>2048</MaxUrlLength>
    <SimilarType>None</SimilarType>
    <SortSimilar>true</SortSimilar>
    <TrimDuplicatesIncludeId>0</TrimDuplicatesIncludeId>
    <TrimDuplicatesKeepCount>1</TrimDuplicatesKeepCount>
  </QueryProperties>
  <WhiteList xmlns:a="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
    <a:string>RowLimit</a:string>
    <a:string>SortList</a:string>
    <a:string>StartRow</a:string>
    <a:string>RefinementFilters</a:string>
    <a:string>Culture</a:string>
    <a:string>RankingModelId</a:string>
    <a:string>TrimDuplicatesIncludeId</a:string>
    <a:string>ReorderingRules</a:string>
    <a:string>EnableQueryRules</a:string>
    <a:string>HiddenConstraints</a:string>
    <a:string>QueryText</a:string>
    <a:string>QueryTemplate</a:string>
  </WhiteList>
</QueryPropertiesTemplate>
```
1. Update the `SiteId`, `FarmId`, and `WebId` elements with the values for your farm, website and publishing site collection.

2. Save _queryparametertemplate.xml_ to the **QueryPropertiesTemplate** document library.

3. Add the `QueryTemplatePropertiesUrl` parameter to your Search REST call, specifying `spfile://webroot/queryparametertemplate.xml` as the value.

The primary elements in the _queryparametertemplate.xml_ file are:

* **QueryProperties** element

Contains a serialized [QueryProperties](https://msdn.microsoft.com/library/Microsoft.Office.Server.Search.Query.QueryProperties.aspx) object.

* **WhiteList** element

Contains the list of query properties that the anonymous user is allowed to set.

When an anonymous Search REST query is submitted, the query object is constructed using what's specified in the **QueryProperties** element. Then, all the properties that are listed in the whitelist are copied from the incoming query to the newly constructed query object.

* [Retrieving query suggestions using the Search REST service](https://learn.microsoft.com/en-us/sharepoint/dev/general-development/retrieving-query-suggestions-using-the-search-rest-service)

* [Search in SharePoint](https://learn.microsoft.com/en-us/sharepoint/dev/general-development/search-in-sharepoint)
* [Using the SharePoint search Query APIs](https://learn.microsoft.com/en-us/sharepoint/dev/general-development/using-the-sharepoint-search-query-apis)
* [What's new in SharePoint search for developers](https://learn.microsoft.com/en-us/sharepoint/dev/general-development/what-s-new-in-sharepoint-search-for-developers)
* [Use OData query operations in SharePoint REST requests](https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/use-odata-query-operations-in-sharepoint-rest-requests)
