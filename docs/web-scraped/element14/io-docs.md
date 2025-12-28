# Source: https://partner.element14.com/io-docs

element14, Farnell, Newark API

<div>

</div>

-   [Sign In](https://partner.element14.com/login/login?r=https%3A%2F%2Fpartner.element14.com%2Fio-docs&h=af91ee78cbdeab4deb06090002d317ce)
-   [Register](https://partner.element14.com/member/register)

# Interactive API Playground

Choose the API you want to interact with from the drop-down menu.

[]

-   Select an Interactive Documentation
-   Order API Sandbox
-   Product Search API (REST)

[] Select an Interactive Documentation Order API Sandbox Product Search API (REST)

No description set

element14 Product Search API (REST)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgc3R5bGU9ImhlaWdodDoxZW07d2lkdGg6MWVtOyIgdmlld2JveD0iMCAwIDkyIDkyIiBhcmlhLWxhYmVsbGVkYnk9ImRvd25sb2FkLXNwZWMtdGl0bGUiPjx0aXRsZSBpZD0iZG93bmxvYWQtc3BlYy10aXRsZSI+RG93bmxvYWQgU3BlY2lmaWNhdGlvbjwvdGl0bGU+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNODkgNTguOFY4NmMwIDIuOC0yLjIgNS01IDVIOGMtMi44IDAtNS0yLjItNS01VjU4LjhjMC0yLjggMi4yLTUgNS01czUgMi4yIDUgNVY4MWg2NlY1OC44YzAtMi44IDIuMi01IDUtNXM1IDIuMiA1IDV6TTQyLjQgNjVjLjkgMSAyLjIgMS41IDMuNiAxLjVzMi42LS41IDMuNi0xLjVsMTkuOS0yMC40YzEuOS0yIDEuOS01LjEtLjEtNy4xLTItMS45LTUuMS0xLjktNy4xLjFMNTEgNDkuM1Y2YzAtMi44LTIuMi01LTUtNXMtNSAyLjItNSA1djQzLjNMMjkuNiAzNy43Yy0xLjktMi01LjEtMi03LjEtLjFzLTIgNS4xLS4xIDcuMWwyMCAyMC4zeiI+PC9wYXRoPjwvc3ZnPg==)

OAuth 2.0 Flow: Select OAuth 2.0 Flow

Existing Client Credentials: Manual Input

API Key:

App/Key: Select Application Key [Manually provide key information](#)

Shared Secret:

<div>

Client ID:

</div>

<div>

Client Secret:

Authorize

</div>

<div>

Client ID:

Get Access Token

</div>

<div>

Client ID:

</div>

<div>

Client Secret:

</div>

------------------------------------------------------------------------

<div>

Username:

</div>

<div>

Password:

Get Access Token

</div>

<div>

Client ID:

</div>

<div>

Client Secret:

Get Access Token

</div>

Authorization Code:

Get Access Token

Access Token:

<div>

Username:

</div>

<div>

Password:

</div>

<div>

Username:

</div>

<div>

Binary Security Token:

</div>

<div>

Username:

</div>

<div>

Password:

</div>

-   [Toggle All Endpoints](#)
-   [Toggle All Methods](#)

```
<!-- -->
```
-   ### [ Product Search ] 

    -   [List Methods](#)
    -   [Expand Methods](#)

    ```
    <!-- -->
    ```
    -   ::: title
        [ GET ] [ Search by Keyword ] [ /catalog/products ]
        :::

        [ ]

        Returns Product information based on a search by keyword

          Parameter                             Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              Type     Description
          ------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
          versionNumber                         1.4 1.3 1.2 1.1 1.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                string   field:versionNumber
          term                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     string   field:term (e.g. any:fuse). Note: These examples are specific to the uk.farnell.com store.
          storeInfo.id                          au.element14.com cn.element14.com hk.element14.com in.element14.com kr.element14.com my.element14.com nz.element14.com ph.element14.com sg.element14.com th.element14.com tw.element14.com vn.element14.com at.farnell.com be.farnell.com bg.farnell.com ch.farnell.com cpc.farnell.com cpcireland.farnell.com cz.farnell.com de.farnell.com dk.farnell.com ee.farnell.com es.farnell.com export.farnell.com fi.farnell.com fr.farnell.com hu.farnell.com ie.farnell.com il.farnell.com it.farnell.com lt.farnell.com lv.farnell.com nl.farnell.com no.farnell.com onecall.farnell.com pl.farnell.com pt.farnell.com ro.farnell.com ru.farnell.com se.farnell.com si.farnell.com sk.farnell.com tr.farnell.com uk.farnell.com canada.newark.com mexico.newark.com www.newark.com   string   Store identifier
          resultsSettings.offset                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   string   Start index of for the query. Note: For any given search paging is possible for first 100 items. After that user encounters un-predictable results. Please refine your search term for optimal results.
          resultsSettings.numberOfResults                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          string   Number of results to be returned. Note: For any given search paging is possible for first 100 items. After that user encounters un-predictable results. Please refine your search term for optimal results.
          resultsSettings.refinements.filters   inStock rohsCompliant rohsCompliant,inStock                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        string   In Stock, if selected will only bring back products that are in stock. ROHS Compliant, if selected will bring back products which comply with ROHS specification.
          resultsSettings.responseGroup         small medium large none prices inventory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           string   Filter output. See documentation for greater detail.
          callInfo.omitXmlSchema                false true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         string   Strip XML Namespace. XML data format only
          callInfo.callback                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        string   JSONP Callback wrapper name. Not recommended for use with XML output.
          callInfo.responseDataFormat           json xml                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           string   Output format as JSON or XML

    -   ::: title
        [ GET ] [ Search by element14 / Newark element14 / Farnell element14 Order Code ] [ /catalog/products ]
        :::

        [ ]

        Returns Product information based on a search of the element14 / Newark element14 / Farnell element14 order code

          Parameter                             Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              Type     Description
          ------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
          versionNumber                         1.4 1.3 1.2 1.1 1.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                string   field:versionNumber
          term                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     string   field:term (e.g. id:1278613) Note: These examples are specific to the uk.farnell.com store.
          storeInfo.id                          au.element14.com cn.element14.com hk.element14.com in.element14.com kr.element14.com my.element14.com nz.element14.com ph.element14.com sg.element14.com th.element14.com tw.element14.com vn.element14.com at.farnell.com be.farnell.com bg.farnell.com ch.farnell.com cpc.farnell.com cpcireland.farnell.com cz.farnell.com de.farnell.com dk.farnell.com ee.farnell.com es.farnell.com export.farnell.com fi.farnell.com fr.farnell.com hu.farnell.com ie.farnell.com il.farnell.com it.farnell.com lt.farnell.com lv.farnell.com nl.farnell.com no.farnell.com onecall.farnell.com pl.farnell.com pt.farnell.com ro.farnell.com ru.farnell.com se.farnell.com si.farnell.com sk.farnell.com tr.farnell.com uk.farnell.com canada.newark.com mexico.newark.com www.newark.com   string   Store identifier
          resultsSettings.offset                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   string   Start index of for the query. Note: For any given search paging is possible for first 100 items. After that user encounters un-predictable results. Please refine your search term for optimal results.
          resultsSettings.numberOfResults                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          string   Number of results to be returned. Note: For any given search paging is possible for first 100 items. After that user encounters un-predictable results. Please refine your search term for optimal results.
          resultsSettings.refinements.filters   inStock rohsCompliant rohsCompliant,inStock                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        string   In Stock, if true will only bring back products that are in stock. ROHS Compliant, if true will bring back products which comply with ROHS specification.
          resultsSettings.responseGroup         small medium large none prices inventory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           string   Filter output. See documentation for greater detail.
          callInfo.omitXmlSchema                false true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         string   Strip XML Namespace. XML data format only
          callInfo.callback                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        string   JSONP Callback wrapper name. Not recommended for use with XML output.
          callInfo.responseDataFormat           json xml                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           string   Output format as JSON or XML

    -   ::: title
        [ GET ] [ Search by Manufacturer Part Number ] [ /catalog/products ]
        :::

        [ ]

        Returns Product information based on a search of the manufacturer part number

          Parameter                             Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              Type     Description
          ------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
          versionNumber                         1.4 1.3 1.2 1.1 1.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                string   field:versionNumber
          term                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     string   field:term (e.g. manuPartNum:LM339ADT) Note: These examples are specific to the uk.farnell.com store.
          storeInfo.id                          au.element14.com cn.element14.com hk.element14.com in.element14.com kr.element14.com my.element14.com nz.element14.com ph.element14.com sg.element14.com th.element14.com tw.element14.com vn.element14.com at.farnell.com be.farnell.com bg.farnell.com ch.farnell.com cpc.farnell.com cpcireland.farnell.com cz.farnell.com de.farnell.com dk.farnell.com ee.farnell.com es.farnell.com export.farnell.com fi.farnell.com fr.farnell.com hu.farnell.com ie.farnell.com il.farnell.com it.farnell.com lt.farnell.com lv.farnell.com nl.farnell.com no.farnell.com onecall.farnell.com pl.farnell.com pt.farnell.com ro.farnell.com ru.farnell.com se.farnell.com si.farnell.com sk.farnell.com tr.farnell.com uk.farnell.com canada.newark.com mexico.newark.com www.newark.com   string   Store identifier
          resultsSettings.offset                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   string   Start index of for the query. Note: For any given search paging is possible for first 100 items. After that user encounters un-predictable results. Please refine your search term for optimal results. Mandatory for Keyword Search
          resultsSettings.numberOfResults                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          string   Number of results to be returned. Note: For any given search paging is possible for first 100 items. After that user encounters un-predictable results. Please refine your search term for optimal results. Mandatory for Keyword Search
          resultsSettings.refinements.filters   inStock rohsCompliant rohsCompliant,inStock                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        string   In Stock, if true will only bring back products that are in stock. ROHS Compliant, if true will bring back products which comply with ROHS specification.
          resultsSettings.responseGroup         small medium large none prices inventory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           string   Filter output. See documentation for greater detail.
          callInfo.omitXmlSchema                false true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         string   Strip XML Namespace. XML data format only
          callInfo.callback                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        string   JSONP Callback wrapper name. Not recommended for use with XML output.
          callInfo.responseDataFormat           json xml                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           string   Output format as JSON or XML

-   [Home](https://partner.element14.com/page)
-   [API Gallery](https://partner.element14.com/api_gallery)
-   [Product Search API](https://partner.element14.com/docs)
-   [Order API](https://partner.element14.com/order)
-   [element14 Community](https://community.element14.com)

-   [Privacy Statement](https://partner.element14.com/privacy)
-   [Data Protection Policy](https://partner.element14.com/Data_Protection_Policy)
-   [Terms of Use](https://partner.element14.com/terms)
-   [Contact Us](https://partner.element14.com/contact)
-   [Cookies](https://partner.element14.com/aboutcookies)
-   [Support Notice](https://partner.element14.com/Support_Notice)

Copyright 2011-2025 Premier Farnell Ltd

[](http://www.farnell.com)

[](http://www.newark.com)

[](http://www.farnell.com)