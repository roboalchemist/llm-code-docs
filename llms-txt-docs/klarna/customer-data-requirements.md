# Source: https://docs.klarna.com/payments/web-payments/before-you-start/data-requirements/customer-data-requirements.md

# Customer data requirements for authorize()

## This section describes the customer data we require to place an order, depending on the purchase country.

## Why do we care?

As we offer credit to your customers, we need to have enough data to do a proper risk and fraud assessment. This is only possible if we have high-quality customer data in a standardized format. Klarna’s services may not be used by businesses registered or operating in some jurisdictions. Additionally, Klarna’s services may not be used to process payments for the sale of goods or services shipping from, or for the purchase of goods that would be shipped to consumers with a billing or shipping address in the specific regions.  <em>See full list of <span>[Prohibited Jurisdictions and Regions](https://docs.klarna.com)</span> here</em>Finally, but not less important, we also need to manage customer data to ensure the best customer experience in the order management process. Ensure customer information is not sent before confirming the intention to pay with Klarna to remain GDPR compliant. This confirmation typically occurs at the time of [authorization](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/step-2-checkout/).

## Adding billing and shipping address

Klarna payments API can handle both billing and shipping addresses separately. If you don't provide a shipping address, we duplicate the billing address and use it as the shipping address in our customer data.

### Risk assessment

During our assessment, the fraud risk might be higher if:

- The billing and shipping addresses are different.
- The customer of the billing and shipping addresses is different.

## Adding customer data throughout the session

The customer data you send us in later calls after `authorize()` is merged with the data you entered previously.

## Data per country

Depending on the data standards of each country, we require different information per country market. To ensure a friendly customer experience, you need to properly provide the customer details in the mandatory fields. `street_address2` is only to add extra details to the address, such as the floor and the apartment number. Send the main address information in the regular `street_address` field. **The following Unicode blocks are supported for all markets except Greek** [BASIC_LATIN](https://en.wikipedia.org/wiki/Basic_Latin_(Unicode_block)) [LATIN_1_SUPPLEMENT](https://en.wikipedia.org/wiki/Latin-1_Supplement) [LATIN_EXTENDED_A](https://en.wikipedia.org/wiki/Latin_Extended-A) [PHONETIC_EXTENSIONS](https://en.wikipedia.org/wiki/Phonetic_Extensions) **The following Unicode blocks are supported for the Greek market** [BASIC_LATIN](https://en.wikipedia.org/wiki/Basic_Latin_(Unicode_block)) [GREEK](https://en.wikipedia.org/wiki/Greek_and_Coptic) [GREEK_EXTENDED](https://en.wikipedia.org/wiki/Greek_Extended) **Additionally, characters are also matched against the following Unicode categories** [Li](https://www.compart.com/en/unicode/category/Ll) (Lower case characters) [Lu](https://www.compart.com/en/unicode/category/Lu) (Upper case characters) [Nd](https://www.compart.com/en/unicode/category/Nd) (Decimal digit number characters) Note that any characters that don't belong to the categories above are considered special characters. The characters allowed in each field are listed in the market overview tables below.

### Europe

<em>Sweden,Finland,Norway,Denmark</em>

### Sweden, Norway, Finland, and Denmark

<table>
<thead>
<tr>
<th><p>Customer details</p></th>
<th><p>Requierement level</p></th>
<th><p>Comment</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>email</p></td>
<td><p>Optional for <code>authorize()</code> operation</p></td>
<td><p>Must include @ and domain. Pattern: ''(?<local>^[a-zA-Z0-9!#$%&'+/=?^_`{|}</local></p>
<p>~-]+(?:\.[a-zA-Z0-9!#$%&'+/=?^_`{|}</p>
<p>~-]+)*)@(?<domain>(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+(?<tld>[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$))''</tld></domain></p></td>
</tr>
<tr>
<td><p>postal_code</p></td>
<td><p>Optional for <code>authorize()</code> operation</p></td>
<td><p>Validation according to Universal Postal Union addressing systems.</p></td>
</tr>
<tr>
<td><p>national_identification_number</p></td>
<td><p>Depending on the payment method. If not added, Klarna will collect the details in the purchase flow.</p></td>
<td><p>Necessary for all credit payment methods and Pay Now.</p></td>
</tr>
<tr>
<td><p>given_name</p></td>
<td><p>Optional for <code>authorize()</code> operation</p></td>
<td><p>Customers given name in UTF-8 encoding. Cannot be only numbers, must be more than 1 character. Allowed special characters: -'’.°ºᵃª</p></td>
</tr>
<tr>
<td><p>family_name</p></td>
<td><p>Optional for <code>authorize()</code> operation</p></td>
<td><p>Customers family name in UTF-8 encoding. Cannot be only numbers, must be more than 1 character. Allowed special characters: -'’.°ºᵃª</p></td>
</tr>
<tr>
<td><p>street_address</p></td>
<td><p>Optional for <code>authorize()</code> operation</p></td>
<td><p>Street name and number following <a href="http://www.upu.int/en/activities/addressing/postal-addressing-systems-in-member-countries.html">Universal Postal Union addressing systems</a> Allowed special characters: -'´`",.:;#&/()+@ °ºᵃª_ \</p></td>
</tr>
<tr>
<td><p>care_of</p></td>
<td><p>Optional for <code>authorize()</code> operation</p></td>
<td><p>To address the order to another recipient. B2C purchases only.</p></td>
</tr>
<tr>
<td><p>city</p></td>
<td><p>Optional for <code>authorize()</code> operation</p></td>
<td><p>City field according to the market.</p></td>
</tr>
<tr>
<td><p>phone</p></td>
<td><p>Optional for <code>authorize()</code> operation</p></td>
<td><p>Follow the standards defined in <a href="https://github.com/googlei18n/libphonenumber"><span>https://github.com/googlei18n/libphonenumber</span></a></p></td>
</tr>
<tr>
<td><p>gender</p></td>
<td><p>Derived</p></td>
<td><p>Derived from PNO</p></td>
</tr>
<tr>
<td><p>date_of_birth</p></td>
<td><p>Derived</p></td>
<td><p>Derived from PNO</p></td>
</tr>
</tbody>
</table>
<em>United Kingdom</em>

### United Kingdom

<table>
<thead>
<tr>
<th><p>Customer details</p></th>
<th><p>Requierement level</p></th>
<th><p>Comment</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>- email</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Must include @ and domain. Pattern: ''(?<local>^[a-zA-Z0-9!#$%&'+/=?^_`{|}</local></p>
<p>~-]+(?:\.[a-zA-Z0-9!#$%&'+/=?^_`{|}</p>
<p>~-]+)*)@(?<domain>(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+(?<tld>[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$))''</tld></domain></p></td>
</tr>
<tr>
<td><p>- postal_code</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Validation according to Universal Postal Union addressing systems.</p></td>
</tr>
<tr>
<td><p>- title</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Mr, Ms</p></td>
</tr>
<tr>
<td><p>date_of_birth</p></td>
<td><p>|Depending on the payment method. If not added, Klarna will collect the details in the purchase flow.</p></td>
<td><p>Necessary for all credit payment methods and Pay Now.</p></td>
</tr>
<tr>
<td><p>given_name</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Customers given name in UTF-8 encoding. Cannot be only numbers, must be more than 1 character. Allowed special characters: -'’.°ºᵃª</p></td>
</tr>
<tr>
<td><p>family_name</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Customers family name in UTF-8 encoding. Cannot be only numbers, must be more than 1 character. Allowed special characters: -'’.°ºᵃª</p></td>
</tr>
<tr>
<td><p>street_address</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Street name and number following <a href="http://www.upu.int/en/activities/addressing/postal-addressing-systems-in-member-countries.html">Universal Postal Union addressing systems</a> Allowed special characters: -'´`",.:;#&/()+@ °ºᵃª_ \</p></td>
</tr>
<tr>
<td><p>street_address2</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Second address line. Allowed special characters: -'´`",.:;#&/()+@ °ºᵃª_ \</p></td>
</tr>
<tr>
<td><p>city</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>City field according to the market.</p></td>
</tr>
<tr>
<td><p>phone</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Follow the standards defined in <a href="https://github.com/googlei18n/libphonenumber"><span>https://github.com/googlei18n/libphonenumber</span></a></p></td>
</tr>
<tr>
<td><p>gender</p></td>
<td><p>|Derived</p></td>
<td><p>Derived from title</p></td>
</tr>
</tbody>
</table>
<em>Ireland</em>

### Ireland

<table>
<thead>
<tr>
<th><p>Customer details</p></th>
<th><p>Requierement level</p></th>
<th><p>Comment</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>email</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Must include @ and domain. Pattern: ''(?<local>^[a-zA-Z0-9!#$%&'+/=?^_`{|}</local></p>
<p>~-]+(?:\.[a-zA-Z0-9!#$%&'+/=?^_`{|}</p>
<p>~-]+)*)@(?<domain>(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+(?<tld>[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$))''</tld></domain></p></td>
</tr>
<tr>
<td><p>postal_code (eircode)</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Validation according to Universal Postal Union addressing systems</p></td>
</tr>
<tr>
<td><p>date_of_birth</p></td>
<td><p>|Depending on the payment method. If not added, Klarna will collect the details in the purchase flow.</p></td>
<td><p>Necessary for all credit payment methods and Pay Now.</p></td>
</tr>
<tr>
<td><p>given_name</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Customers given name in UTF-8 encoding. Cannot be only numbers, must be more than 1 character. Allowed special characters: -'’.°ºᵃª</p></td>
</tr>
<tr>
<td><p>family_name</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Customers family name in UTF-8 encoding. Cannot be only numbers, must be more than 1 character. Allowed special characters: -'’.°ºᵃª</p></td>
</tr>
<tr>
<td><p>street_address</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Street name and number following <a href="http://www.upu.int/en/activities/addressing/postal-addressing-systems-in-member-countries.html">Universal Postal Union addressing systems</a> Allowed special characters: -'´`",.:;#&/()+@ °ºᵃª_ \</p></td>
</tr>
<tr>
<td><p>street_address2</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Second address line. Allowed special characters: -'´`",.:;#&/()+@ °ºᵃª_ \</p></td>
</tr>
<tr>
<td><p>city</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>City field according to the market.</p></td>
</tr>
<tr>
<td><p>region</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>County, E.G "Antrim".</p></td>
</tr>
<tr>
<td><p>phone</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Follow the standards defined in <a href="https://github.com/googlei18n/libphonenumber"><span>https://github.com/googlei18n/libphonenumber</span></a></p></td>
</tr>
</tbody>
</table>
<em>Germany,Austria,Switzerland,Netherlands,Belgium</em>

### Germany, Austria, Switzerland, Netherlands and Belgium

<table>
<thead>
<tr>
<th><p>Customer details</p></th>
<th><p>Requierement level</p></th>
<th><p>Comment</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>email</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Must include @ and domain. Pattern: ''(?<local>^[a-zA-Z0-9!#$%&'+/=?^_`{|}</local></p>
<p>~-]+(?:\.[a-zA-Z0-9!#$%&'+/=?^_`{|}</p>
<p>~-]+)*)@(?<domain>(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+(?<tld>[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$))''</tld></domain></p></td>
</tr>
<tr>
<td><p>postal_code</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Validation according to Universal Postal Union addressing systems.</p></td>
</tr>
<tr>
<td><p>date_of_birth</p></td>
<td><p>|Depending on the payment method. If not added, Klarna will collect the details in the purchase flow.</p></td>
<td><p>Necessary for all credit payment methods.</p></td>
</tr>
<tr>
<td><p>title</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>de:“Herr”, “Frau”; de_CH: “Herr, “Frau”; it_CH: “Sig.", “Sig.ra”; fr_CH: “M", “Mme”; nl: “Dhr.", “Mevr.”; nl_BE: “Dhr”, “Mevr”; fr_BE: “M", “Mme”</p></td>
</tr>
<tr>
<td><p>given_name</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Customers given name in UTF-8 encoding. Cannot be only numbers, must be more than 1 character. Allowed special characters: -'’.°ºᵃª</p></td>
</tr>
<tr>
<td><p>family_name</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Customers family name in UTF-8 encoding. Cannot be only numbers, must be more than 1 character. Allowed special characters: -'’.°ºᵃª</p></td>
</tr>
<tr>
<td><p>street_address</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Street name and number following <a href="http://www.upu.int/en/activities/addressing/postal-addressing-systems-in-member-countries.html">Universal Postal Union addressing systems</a> Allowed special characters: -'´`",.:;#&/()+@ °ºᵃª_ \</p></td>
</tr>
<tr>
<td><p>care_of</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>To address the order to another recipient. B2C purchases only.</p></td>
</tr>
<tr>
<td><p>city</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>City field according to the market.</p></td>
</tr>
<tr>
<td><p>phone</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Follow the standards defined in <a href="https://github.com/googlei18n/libphonenumber"><span>https://github.com/googlei18n/libphonenumber</span></a></p></td>
</tr>
<tr>
<td><p>> gender</p></td>
<td><p>|</p></td>
<td><p>| Derived from title.</p></td>
</tr>
</tbody>
</table>
<em>France,Spain,Portugal,Poland</em>

### France, Spain, Portugal and Poland

<table>
<thead>
<tr>
<th><p>Customer details</p></th>
<th><p>Requierement level</p></th>
<th><p>Comment</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>email</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Must include @ and domain. Pattern: ''(?<local>^[a-zA-Z0-9!#$%&'+/=?^_`{|}</local></p>
<p>~-]+(?:\.[a-zA-Z0-9!#$%&'+/=?^_`{|}</p>
<p>~-]+)*)@(?<domain>(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+(?<tld>[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$))''</tld></domain></p></td>
</tr>
<tr>
<td><p>postal_code</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Validation according to Universal Postal Union addressing systems.</p></td>
</tr>
<tr>
<td><p>date_of_birth</p></td>
<td><p>|Depending on the payment method. If not added, Klarna will collect the details in the purchase flow.</p></td>
<td><p>Necessary for all credit payment methods.</p></td>
</tr>
<tr>
<td><p>place_of_birth</p></td>
<td><p>|Depending on the payment method. If not added, Klarna will collect the details in the purchase flow.</p></td>
<td><p>Necessary for all credit payment methods.</p></td>
</tr>
<tr>
<td><p>given_name</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Customers given name in UTF-8 encoding. Cannot be only numbers, must be more than 1 character. Allowed special characters: -'’.°ºᵃª</p></td>
</tr>
<tr>
<td><p>family_name</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Customers family name in UTF-8 encoding. Cannot be only numbers, must be more than 1 character. Allowed special characters: -'’.°ºᵃª</p></td>
</tr>
<tr>
<td><p>street_address</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Street name and number following <a href="http://www.upu.int/en/activities/addressing/postal-addressing-systems-in-member-countries.html">Universal Postal Union addressing systems</a> Allowed special characters: -'´`",.:;#&/()+@ °ºᵃª_ \</p></td>
</tr>
<tr>
<td><p>street_address2</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Second address line. Allowed special characters: -'´`",.:;#&/()+@ °ºᵃª_ \</p></td>
</tr>
<tr>
<td><p>city</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>City field according to the market.</p></td>
</tr>
<tr>
<td><p>phone</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Follow the standards defined in <a href="https://github.com/googlei18n/libphonenumber"><span>https://github.com/googlei18n/libphonenumber</span></a></p></td>
</tr>
</tbody>
</table>
<em>Italy</em>

### Italy

<table>
<thead>
<tr>
<th><p>Customer details</p></th>
<th><p>Requierement level</p></th>
<th><p>Comment</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>email</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Must include @ and domain. Pattern: ''(?<local>^[a-zA-Z0-9!#$%&'+/=?^_`{|}</local></p>
<p>~-]+(?:\.[a-zA-Z0-9!#$%&'+/=?^_`{|}</p>
<p>~-]+)*)@(?<domain>(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+(?<tld>[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$))''</tld></domain></p></td>
</tr>
<tr>
<td><p>postal_code</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Validation according to Universal Postal Union addressing systems.</p></td>
</tr>
<tr>
<td><p>date_of_birth</p></td>
<td><p>|Depending on the payment method. If not added, Klarna will collect the details in the purchase flow.</p></td>
<td><p>Necessary for all credit payment methods.</p></td>
</tr>
<tr>
<td><p>place_of_birth</p></td>
<td><p>|Depending on the payment method. If not added, Klarna will collect the details in the purchase flow.</p></td>
<td><p>Necessary for all credit payment methods.</p></td>
</tr>
<tr>
<td><p>given_name</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Customers given name in UTF-8 encoding. Cannot be only numbers, must be more than 1 character. Allowed special characters: -'’.°ºᵃª</p></td>
</tr>
<tr>
<td><p>family_name</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Customers family name in UTF-8 encoding. Cannot be only numbers, must be more than 1 character. Allowed special characters: -'’.°ºᵃª</p></td>
</tr>
<tr>
<td><p>street_address</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Street name and number following <a href="http://www.upu.int/en/activities/addressing/postal-addressing-systems-in-member-countries.html">Universal Postal Union addressing systems</a> Allowed special characters: -'´`",.:;#&/()+@ °ºᵃª_ \</p></td>
</tr>
<tr>
<td><p>street_address2</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Second address line. Allowed special characters: -'´`",.:;#&/()+@ °ºᵃª_ \</p></td>
</tr>
<tr>
<td><p>city</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>City field according to the market.</p></td>
</tr>
<tr>
<td><p>region</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Province in 2 letter format e.g "AG".</p></td>
</tr>
<tr>
<td><p>phone</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Follow the standards defined in <a href="https://github.com/googlei18n/libphonenumber"><span>https://github.com/googlei18n/libphonenumber</span></a></p></td>
</tr>
</tbody>
</table>
<em>Greece,Czech Republic,Hungary,Slovakia</em>

### Greece, Czech Republic, Hungary and Slovakia

<table>
<thead>
<tr>
<th><p><strong>Customer Details</strong></p></th>
<th><p>Requierement level</p></th>
<th><p><strong>Comment</strong></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>email</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Must include @ and domain. Pattern: ''(?<local>^[a-zA-Z0-9!#$%&'+/=?^_`{|}</local></p>
<p>~-]+(?:\.[a-zA-Z0-9!#$%&'+/=?^_`{|}</p>
<p>~-]+)*)@(?<domain>(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+(?<tld>[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$))''</tld></domain></p></td>
</tr>
<tr>
<td><p>postal_code</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Validation according to Universal Postal Union addressing systems.</p></td>
</tr>
<tr>
<td><p>date_of_birth</p></td>
<td><p>|Depending on the payment method. If not added, Klarna will collect the details in the purchase flow.</p></td>
<td><p>Necessary for all credit payment methods.</p></td>
</tr>
<tr>
<td><p>given_name</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Customers given name in UTF-8 encoding. Cannot be only numbers, must be more than 1 character. Allowed special characters: -'’.°ºᵃª</p></td>
</tr>
<tr>
<td><p>family_name</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Customers family name in UTF-8 encoding. Cannot be only numbers, must be more than 1 character. Allowed special characters: -'’.°ºᵃª</p></td>
</tr>
<tr>
<td><p>street_address</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Street name and number following <a href="http://www.upu.int/en/activities/addressing/postal-addressing-systems-in-member-countries.html">Universal Postal Union addressing systems</a> Allowed special characters: -'´`",.:;#&/()+@ °ºᵃª_ \</p></td>
</tr>
<tr>
<td><p>street_address2</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Second address line. Allowed special characters: -'´`",.:;#&/()+@ °ºᵃª_ \</p></td>
</tr>
<tr>
<td><p>city</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>City field according to the market.</p></td>
</tr>
<tr>
<td><p>phone</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Follow the standards defined in <a href="https://github.com/googlei18n/libphonenumber"><span>https://github.com/googlei18n/libphonenumber</span></a></p></td>
</tr>
</tbody>
</table>
<em>Romania</em>

### Romania

<table>
<thead>
<tr>
<th><p>Customer Details</p></th>
<th><p>Requierement level</p></th>
<th><p>Comment</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>email</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Must include @ and domain. Pattern: (?<local>^[a-zA-Z0-9!#$%&'+/=?^_`{|}</local></p>
<p>~-]+(?:\.[a-zA-Z0-9!#$%&'+/=?^_`{|}</p>
<p>~-]+)*)@(?<domain>(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+(?<tld>[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$))</tld></domain></p></td>
</tr>
<tr>
<td><p>postal_code</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Validation according to Universal Postal Union addressing systems.</p></td>
</tr>
<tr>
<td><p>date_of_birth</p></td>
<td><p>|Depending on the payment method. If not added, Klarna will collect the details in the purchase flow.</p></td>
<td><p>Necessary for all credit payment methods.</p></td>
</tr>
<tr>
<td><p>given_name</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Customers given name in UTF-8 encoding. Cannot be only numbers, must be more than 1 character. Allowed special characters: -'’.°ºᵃª Letters with diacritics are allowed.</p></td>
</tr>
<tr>
<td><p>family_name</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Customers given name in UTF-8 encoding. Cannot be only numbers, must be more than 1 character. Allowed special characters: -'’.°ºᵃª Letters with diacritics are allowed.</p></td>
</tr>
<tr>
<td><p>street_address</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Street name and number following <a href="http://www.upu.int/en/activities/addressing/postal-addressing-systems-in-member-countries.html">Universal Postal Union addressing systems</a> Allowed special characters: -'´`",.:;#&/()+@ °ºᵃª_ \ Letters with diacritics are allowed.</p></td>
</tr>
<tr>
<td><p>street_address2</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Street name and number. Allowed special characters: -'´`",.:;#&/()+@ °ºᵃª_ \ Letters with diacritics are allowed.</p></td>
</tr>
<tr>
<td><p>city</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>City field according to the market. Letters with diacritics are allowed.</p></td>
</tr>
<tr>
<td><p>region</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Postal address region (or sector for addresses in Bucharest). For example <em>Cluj</em> (region) or <em>Sector 6</em> (sector). Letters with diacritics are allowed.</p></td>
</tr>
<tr>
<td><p>phone</p></td>
<td><p>Optional for <code>authorize()</code> operation</p></td>
<td><p>Follow the standards defined in <a href="https://github.com/googlei18n/libphonenumber"><span>https://github.com/googlei18n/libphonenumber</span></a></p></td>
</tr>
</tbody>
</table>

## Americas

<em>United States of America,Canada,Mexico</em>

### United States, Canada and Mexico

<table>
<thead>
<tr>
<th><p>Customer details</p></th>
<th><p>Requierement level</p></th>
<th><p>Comment</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>email</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Must include @ and domain. Pattern: ''(?<local>^[a-zA-Z0-9!#$%&'+/=?^_`{|}</local></p>
<p>~-]+(?:\.[a-zA-Z0-9!#$%&'+/=?^_`{|}</p>
<p>~-]+)*)@(?<domain>(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+(?<tld>[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$))''</tld></domain></p></td>
</tr>
<tr>
<td><p>postal_code</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Validation according to Universal Postal Union addressing systems.</p></td>
</tr>
<tr>
<td><p>date_of_birth</p></td>
<td><p>|Depending on the payment method. If not added, Klarna will collect the details in the purchase flow.</p></td>
<td><p>Necessary for all credit payment methods.</p></td>
</tr>
<tr>
<td><p>given_name</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Customers given name in UTF-8 encoding. Cannot be only numbers, must be more than 1 character. Allowed special characters: -'’.°ºᵃª</p></td>
</tr>
<tr>
<td><p>family_name</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Customers family name in UTF-8 encoding. Cannot be only numbers, must be more than 1 character. Allowed special characters: -'’.°ºᵃª</p></td>
</tr>
<tr>
<td><p>street_address</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Street name and number following <a href="http://www.upu.int/en/activities/addressing/postal-addressing-systems-in-member-countries.html">Universal Postal Union addressing systems</a> Allowed special characters: -'´`",.:;#&/()+@ °ºᵃª_ \</p></td>
</tr>
<tr>
<td><p>street_address2</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Address line 2, apartment, suite, for example, apt 2. Allowed special characters: -'´`",.:;#&/()+@ °ºᵃª_ \</p></td>
</tr>
<tr>
<td><p>region</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>For US: Two-letter state code in ISO 3166-1 alpha-2 format. For example, “CA” for California For Canada: Two-letter province code , for example, "ON" for Ontario. For Mexico: Two/three-letter format (ISO 3166-1 alpha-2) for the state. For example, “CDMX” for Ciudad de Mexico, "JAL" for Jalisco, "NL" for Nuevo León.</p></td>
</tr>
<tr>
<td><p>city</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>City field according to the market.</p></td>
</tr>
<tr>
<td><p>phone</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Follow the standards defined in<a href="https://github.com/googlei18n/libphonenumber"><span>https://github.com/googlei18n/libphonenumber</span></a></p></td>
</tr>
</tbody>
</table>

## Asia and Oceania

<em>Australia,New Zealand</em>

### Australia and New Zealand

<table>
<thead>
<tr>
<th><p>Customer details</p></th>
<th><p>Requierement level</p></th>
<th><p>Comment</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>email</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Must include @ and domain. Pattern: ''(?<local>^[a-zA-Z0-9!#$%&'+/=?^_`{|}</local></p>
<p>~-]+(?:\.[a-zA-Z0-9!#$%&'+/=?^_`{|}</p>
<p>~-]+)*)@(?<domain>(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+(?<tld>[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$))''</tld></domain></p></td>
</tr>
<tr>
<td><p>postal_code</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Validation according to Universal Postal Union addressing systems.</p></td>
</tr>
<tr>
<td><p>date_of_birth</p></td>
<td><p>|Depending on the payment method. If not added, Klarna will collect the details in the purchase flow.</p></td>
<td><p>Necessary for all credit payment methods.</p></td>
</tr>
<tr>
<td><p>given_name</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Customers given name in UTF-8 encoding. Cannot be only numbers, must be more than 1 character. Allowed special characters: -'’.°ºᵃª</p></td>
</tr>
<tr>
<td><p>family_name</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Customers family name in UTF-8 encoding. Cannot be only numbers, must be more than 1 character. Allowed special characters: -'’.°ºᵃª</p></td>
</tr>
<tr>
<td><p>street_address</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Street name and number following <a href="http://www.upu.int/en/activities/addressing/postal-addressing-systems-in-member-countries.html">Universal Postal Union addressing systems</a> Allowed special characters: -'´`",.:;#&/()+@ °ºᵃª_ \</p></td>
</tr>
<tr>
<td><p>street_address2</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Second address line. Allowed special characters: -'´`",.:;#&/()+@ °ºᵃª_ \</p></td>
</tr>
<tr>
<td><p>region</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>For AU: State code in <a href="https://www.iso.org/obp/ui/#iso:code:3166:AU">ISO 3166-2</a> format, for example, “QLD” for Queensland, “WA” for “Western Australia”. For NZ: Suburb e.g ​​"Avondale"</p></td>
</tr>
<tr>
<td><p>city</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>City field according to the market.</p></td>
</tr>
<tr>
<td><p>phone</p></td>
<td><p>|Optional for <code>authorize()</code> operation</p></td>
<td><p>Follow the standards defined in <a href="https://github.com/googlei18n/libphonenumber"><span>https://github.com/googlei18n/libphonenumber</span></a></p></td>
</tr>
</tbody>
</table>