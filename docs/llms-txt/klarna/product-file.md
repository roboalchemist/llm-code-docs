# Source: https://docs.klarna.com/klarna-search/integrate-klarna-search/product-file.md

# Product file

## Feed URL

Your product feed must be accessible via an HTTPS address or an FTP server so that we can access and use the file containing your information for our comparisons. If you have IP-level access restrictions, please ensure that our IPs can access the file. We will be changing servers later this year, which will result in changes to our IP addresses. To ensure that we can continue to retrieve your product feed during the transition, it is important that you already allow the new IP addresses below in your system. It is also important that you retain the current IP addresses until the change is fully implemented to avoid interruptions during the transition. Old IPs

- 99.81.173.210
- 3.248.75.7
- 34.251.48.227
- 107.20.175.27
- 34.198.248.212
- 107.20.165.77
- 13.48.206.143
- 13.51.87.202
- 13.51.99.152

New IPs

- 63.32.183.131
- 52.51.164.75
- 108.129.33.253
- 3.212.28.164
- 52.71.114.62
- 54.161.108.102

Refrain from using timestamps or other information that will change the URL of the feed as this will cause your products to disappear from the platform.

## Headers

For us to optimize update routines and display your product catalog’s recent version with prices and item availability, we highly encourage the last-modified HTTP response header to be provided and serviced. The header indicates the date and time the product feed was last changed. By servicing this regularly, we can check for updates more frequently.

## Encoding

Use one of the following encodings for the price file:

- UTF-8, UTF-16
- ISO-8859-1
- Windows-1252

## Format

We can handle the majority of formats. The most common are: TEXT/CSV, XML and JSON. Note that the price file can’t be in Excel or any other non-text format. To make our processing and your updates run faster, compress your feed using gzip/zip.

#### CSV

When it comes to a CSV feed, the data have to be structured in rows and columns. Each row must represent a single product and each column should consist of fields with product information.

- Divide each field or column by a particular separator. Recommended separators include a tab, pipe, semicolon or comma.
- Use "field qualifiers" at the start and end of each field. Note that this character might not occur within a field. Recommended “field qualifiers” single ( ‘ ‘ ) or double ( “ ” ) quotation marks.

#### Example feeds

- [CSV feed example, (tab separated)](https://assets.ctfassets.net/31h9ykss8g0q/35BmS9pLqrQT99kChO0DM0/0da717e9253bf3f01121802b2c1e7bb1/productfeed.txt)
- [XML feed example](https://assets.ctfassets.net/31h9ykss8g0q/6IUoK3iNf8VGyKZ2sWCk3V/ea9c6162325ec271056bd6b89898d4a5/productfeed.xml)

## Field specification and order

Below is a list of the columns recommended for a successful listing. The order and title are not important, provided that they are comprehensible.

- By including EAN/GTIN, it will be possible to match your products automatically and upload them quicker.
- Fields should never contain code or tags such as HTML or JavaScript.

## Fields

### Basic product data (minimum requirements)

- SKU/ID
- Name
- Price
- Shipping costs
- Stock status
- Delivery time
- Manufacturer
- EAN/GTIN
- Condition
- Manufacturer SKU/MPN
- URL
- Image URL
- Category
- Description

### Detailed product data

- AdultContent
- AgeGroup
- Bundled
- Color
- EnergyEfficiencyClass
- Gender
- GroupId
- Material
- Multipack
- Pattern
- Size
- SizeSystem