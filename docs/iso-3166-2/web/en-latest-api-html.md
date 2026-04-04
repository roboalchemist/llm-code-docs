# Source: https://iso3166-2.readthedocs.io/en/latest/api.html

Title: API — iso3166-2 1.5.2 documentation

URL Source: https://iso3166-2.readthedocs.io/en/latest/api.html

Markdown Content:
The main API endpoint displays the API documentation and homepage and forms the base URL for the 6 other endpoints: [https://iso3166-2-api.vercel.app/api](https://iso3166-2-api.vercel.app/api)

The other endpoints available in the API are:

*   [https://iso3166-2-api.vercel.app/api/all](https://iso3166-2-api.vercel.app/api/all)

*   [https://iso3166-2-api.vercel.app/api/alpha](https://iso3166-2-api.vercel.app/api/alpha)/<input_alpha>

*   [https://iso3166-2-api.vercel.app/api/subdivision](https://iso3166-2-api.vercel.app/api/subdivision)/<input_subdivision>

*   [https://iso3166-2-api.vercel.app/api/country_name](https://iso3166-2-api.vercel.app/api/country_name)/<input_country_name>

*   [https://iso3166-2-api.vercel.app/api/search](https://iso3166-2-api.vercel.app/api/search)/<input_search>

*   [https://iso3166-2-api.vercel.app/api/search_geo](https://iso3166-2-api.vercel.app/api/search_geo)/<input_search>

*   [https://iso3166-2-api.vercel.app/api/list_subdivisions](https://iso3166-2-api.vercel.app/api/list_subdivisions)/<input_alpha>

Query String Parameters[](https://iso3166-2.readthedocs.io/en/latest/api.html#query-string-parameters "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------

There are 3 main query string parameters available throughout the API that can be appended to your GET request:

*   **likeness** - this is a parameter between 1 and 100 that increases or reduces the % of similarity/likeness that the inputted search terms have to match to the subdivision name/local other names. This can be used with the /api/search and /api/country_name endpoints. Having a higher value should return more exact and less matches and having a lower value will return less exact but more matches, e.g /api/search/Paris?likeness=50, /api/search/Louisianna?likeness=90 (**default=100**).

*   **filterAttributes** - this parameter allows you to only include a subset of desired attributes per subdivision in the output. This can be used in any of the API endpoints, e.g /api/alpha/AL,BA,CD?filterAttributes=name,type,parentCode, /api/subdivision/LV-112?filterAttributes=localOtherName,flag,history etc.

*   **excludeMatchScore** - this parameter allows you to exclude the _matchScore_ attribute from the search results when using the /api/search endpoint. The match score is the % of a match each returned subdivision data data object is to the search terms, with 100% being an exact match. By default the match score is returned for each object, but setting this parameter to True will exclude the attribute and sort the results by country code, e.g /api/search/Bernardo O’higgins?excludeMatchScore=1, /api/search/New York?excludeMatchScore=1 (**default=0**).

*   **limit** - this parameter allows you to limit the total number of countries returned from the API call. This is only available in the /api/all endpoint. By default, when calling the /api/all endpoint, all of the available data is called so this param allows you to get a faster small subset of the data. The endpoint accepts an integer value representing the total number of countries to return, e.g /api/all?limit=10, /api/all?limit=50 etc. (**default=None**).

Get subdivision data for ALL countries[](https://iso3166-2.readthedocs.io/en/latest/api.html#get-subdivision-data-for-all-countries "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------

Return all available subdivision data for all countries via the /api/all endpoint.

Python Requests:

import requests

base_url = "https://iso3166-2-api.vercel.app/api/"
all_data = requests.get(f'{base_url}all').json()

all_data["AD"] #subdivision data for Andorra
all_data["IE"] #subdivision data for Ireland
all_data["PW"] #subdivision data for Palau
all_data["ZA"] #subdivision data for South Africa

curl:

$ curl -i https://iso3166-2-api.vercel.app/api/all

Get subdivision data per country, using its ISO 3166-1 alpha code (alpha-2, alpha-3, numeric)[](https://iso3166-2.readthedocs.io/en/latest/api.html#get-subdivision-data-per-country-using-its-iso-3166-1-alpha-code-alpha-2-alpha-3-numeric "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For example, accessing all subdivision data for France (FR,FRA,250), Germany (DE,DEU,276) or Gambia (GM,GMB,270), via their **alpha-2 country code**:

Python Requests:

import requests

base_url = "https://iso3166-2-api.vercel.app/api/"
input_alpha = "FR" #DE, GM
all_data = requests.get(f'{base_url}/alpha/{input_alpha}').json()

all_data["FR"] #subdivision data for France
#all_data["DE"] #subdivision data for Germany
#all_data["GM"] #subdivision data for Gambia

curl:

$ curl -i https://iso3166-2-api.vercel.app/api/alpha/FR
$ curl -i https://iso3166-2-api.vercel.app/api/alpha/DE
$ curl -i https://iso3166-2-api.vercel.app/api/alpha/GM

For example, accessing all subdivision data for Greece (GR,GRC,300), Mexico (MX,MEX,484) or Montenegro (ME,MNE,499), via their **alpha-3 country code**:

Python Requests:

import requests

base_url = "https://iso3166-2-api.vercel.app/api/"
input_alpha = "GRC" #MEX, MNE
all_data = requests.get(f'{base_url}/alpha/{input_alpha}').json()

all_data["GR"] #subdivision data for Greece
#all_data["MX"] #subdivision data for Mexico
#all_data["ME"] #subdivision data for Montenegro

curl:

$ curl -i https://iso3166-2-api.vercel.app/api/alpha/GRC
$ curl -i https://iso3166-2-api.vercel.app/api/alpha/MEX
$ curl -i https://iso3166-2-api.vercel.app/api/alpha/MNE

For example, accessing all subdivision data for Nicaragua (NI,NIC,558), Papa New Guinea (PG,PNG,598) or Qatar (QA,QAT,634) via their **alpha numeric country code**:

Python Requests:

import requests

base_url = "https://iso3166-2-api.vercel.app/api/"
input_alpha = "558" #598, 634 (NI, PG, QA)
all_data = requests.get(f'{base_url}/alpha/{input_alpha}').json()

all_data["NI"] #subdivision data for Nicaragua
#all_data["PG"] #subdivision data for Papua New Guinea
#all_data["QA"] #subdivision data for Qatar

curl:

$ curl -i https://iso3166-2-api.vercel.app/api/alpha/558
$ curl -i https://iso3166-2-api.vercel.app/api/alpha/598
$ curl -i https://iso3166-2-api.vercel.app/api/alpha/634

Get all subdivision data for a specific subdivision, using its subdivision code[](https://iso3166-2.readthedocs.io/en/latest/api.html#get-all-subdivision-data-for-a-specific-subdivision-using-its-subdivision-code "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Get all subdivision data for a single or subset of subdivisions using their official ISO 3166-2 subdivision code. For example, accessing all subdivision data for LV-007 (Alūksnes novads), PA-3 (Colón) and ZA-NC (Northern Cape):

Python Requests:

import requests

base_url = "https://iso3166-2-api.vercel.app/api/"
input_subdivision = "LV-007" #PA-3, ZA-NC
all_data = requests.get(f'{base_url}/subdivision/{input_subdivision}').json()

all_data["LV-007"] #data for LV-007 subdivision
#all_data["PA-3"] #data for PA-3 subdivision
#all_data["ZA-NC"] #data for ZA-NC subdivision

curl:

$ curl -i https://iso3166-2-api.vercel.app/api/subdivision/LV-007
$ curl -i https://iso3166-2-api.vercel.app/api/subdivision/PA-3
$ curl -i https://iso3166-2-api.vercel.app/api/subdivision/ZA-NC

Get all subdivision data for a specific country, using its name[](https://iso3166-2.readthedocs.io/en/latest/api.html#get-all-subdivision-data-for-a-specific-country-using-its-name "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Get all subdivision data using the officially recognized country name, as it is commonly known in English. For example, accessing all subdivision data for Tajikistan (TJ), Seychelles (SC) and Uganda (UG):

Python Requests:

import requests

base_url = "https://iso3166-2-api.vercel.app/api/"
input_country_name = "Tajikistan" #Seychelles, Uganda
all_data = requests.get(f'{base_url}/country_name/{input_country_name}').json()

all_data["TJ"] #subdivision data for Tajikistan
#all_data["SC"] #subdivision data for Seychelles
#all_data["UG"] #subdivision data for Uganda

curl:

$ curl -i https://iso3166-2-api.vercel.app/api/country_name/Tajikistan
$ curl -i https://iso3166-2-api.vercel.app/api/country_name/Seychelles
$ curl -i https://iso3166-2-api.vercel.app/api/country_name/Uganda

Search for a specific subdivision, using its subdivision name or local/other names[](https://iso3166-2.readthedocs.io/en/latest/api.html#search-for-a-specific-subdivision-using-its-subdivision-name-or-local-other-names "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For this endpoint, there is an optional query parameter called _likeness_. This can be set between 1 - 100, representing a % of likeness to the input search term that the subdivisions name or local/other name should be, e.g: a _likeness_ score of 90 will return fewer potential matches whose name only match to a high degree compared to a score of 10 which will create a larger search space, thus returning more potential subdivision matches. A default likeness of 100 (exact match) is used, if no matching subdivision is found then this is reduced to 90. If an invalid subdivision name that doesn’t match any is input then an error will be raised.

The output will be sorted by an attributes called _matchScore_ which is the % likeness that the subdivision name is to the input search terms. This attribute can be excluded via the _excludeMatchScore_ query string parameter, which will cause the output to be sorted alphabetically as like the other endpoints.

For example, accessing all subdivision data for Saarland (DE-SL), Brokopondo (SR-BR) and Delaware (US-DE):

Python Requests:

import requests

base_url = "https://iso3166-2-api.vercel.app/api/"
input_search = "Saarland, Brokopondo, Delaware" #DE-SL, SR-BR, US-DE
all_data = requests.get(f'{base_url}/search/{input_search}').json()

all_data["DE-SL"] #subdivision data for Saarland
all_data["SR-BR"] #subdivision data for Brokopondo
all_data["US-DE"] #subdivision data for Delaware

curl:

$ curl -i https://iso3166-2-api.vercel.app/api/search/Saarland
$ curl -i https://iso3166-2-api.vercel.app/api/search/Brokopondo
$ curl -i https://iso3166-2-api.vercel.app/api/search/Delaware
$ curl -i https://iso3166-2-api.vercel.app/api/search/Saarland,Brokopondo,Delaware

Accessing all subdivision’s that have “Northern” or “Southern” in them using the _?likeness_ query string parameter:

Python Requests:

import requests

base_url = "https://iso3166-2-api.vercel.app/api/"
input_search = "Northern" #Southern
all_data = requests.get(f'{base_url}/search/{input_search}', params={"likeness": 80).json()

curl:

$ curl -i https://iso3166-2-api.vercel.app/api/search/Northern?likeness=80
$ curl -i https://iso3166-2-api.vercel.app/api/search/Southern?likeness=80

Accessing all subdivision’s that have “Saint George” in them, excluding the _Match Score_ attribute:

Python Requests:

import requests

base_url = "https://iso3166-2-api.vercel.app/api/"
input_search = "Saint George"
all_data = requests.get(f'{base_url}/search/{input_search}', params={"excludeMatchScore": 1).json()

curl:

$ curl -i https://iso3166-2-api.vercel.app/api/search/Northern?likeness=80

Search for subdivision geography[](https://iso3166-2.readthedocs.io/en/latest/api.html#search-for-subdivision-geography "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------

This endpoint allows you to search for a specific ISO 3166-2 subdivision and return only geographic attributes (latLng, boundingBox, geojson, neighbours, perimeter). Input can be a comma separated list of subdivision names or ISO 3166-2 subdivision codes. The search is approximate based on the likeness score.

Python Requests:

import requests

base_url = "https://iso3166-2-api.vercel.app/api/"
input_search = "Saarland,US-CA"
data = requests.get(f'{base_url}/search_geo/{input_search}').json()

data["DE-SL"]  # Saarland
data["US-CA"]  # California

curl:

$ curl -i https://iso3166-2-api.vercel.app/api/search_geo/Saarland,US-CA

Get list of all subdivision codes per country[](https://iso3166-2.readthedocs.io/en/latest/api.html#get-list-of-all-subdivision-codes-per-country "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Return a list of all ISO 3166-2 subdivision codes for each country. You can get the list of subdivisions per country by appending its ISO 3166-1 country code.

Python Requests:

import requests

base_url = "https://iso3166-2-api.vercel.app/api/list_subdivisions"
all_data = requests.get(base_url)

all_data["DE"] #subdivision codes for Germany
all_data["OM"] #subdivision data for Oman
all_data["US"] #subdivision data for US

#get specific subdivision list via country code
base_url = "https://iso3166-2-api.vercel.app/api/list_subdivisions/DE"
all_data = requests.get(base_url)

base_url = "https://iso3166-2-api.vercel.app/api/list_subdivisions/OM"
all_data = requests.get(base_url)

base_url = "https://iso3166-2-api.vercel.app/api/list_subdivisions/US"
all_data = requests.get(base_url)

curl:

$ curl -i https://iso3166-2-api.vercel.app/api/list_subdivisions
$ curl -i https://iso3166-2-api.vercel.app/api/list_subdivisions/DE
$ curl -i https://iso3166-2-api.vercel.app/api/list_subdivisions/OM
$ curl -i https://iso3166-2-api.vercel.app/api/list_subdivisions/US

Note

A demo of the software and API is available [here](https://colab.research.google.com/drive/1btfEx23bgWdkUPiwdwlDqKkmUp1S-_7U?usp=sharing).

[Back to top ↑](https://iso3166-2.readthedocs.io/en/latest/api.html#api)
