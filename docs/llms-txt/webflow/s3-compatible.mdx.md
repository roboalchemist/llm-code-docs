# Source: https://developers.webflow.com/browser/data-exports/destinations/s3-compatible.mdx

***

title: S3-compatible storage
slug: data-exports/destinations/s3-compatible
description: Configure S3-compatible storage as a destination for Data Exports
------------------------------------------------------------------------------

This guide walks you through configuring S3-compatible storage platforms as a destination for your Webflow Analyze and Optimize data export.

## Prerequisites

* Many object storage platforms offer "S3 compatibility" enabling writing to and reading from the object storage using the S3 protocol. The S3 protocol uses an HMAC key comprised of an access ID and a secret to authenticate and write data.

## Configuration steps

<Steps>
  ### Create an HMAC access ID and secret

  Consult your object storage platform's documentation to learn how to generate an HMAC Access ID and Secret.

  ### Add your destination

  Use the following details to complete the connection setup: **bucket host**, **bucket name**, chosen **folder name**, **HMAC access ID**, and **HMAC secret**.

  * Instructions for [Analyze / Optimize for Webflow sites](https://help.webflow.com/hc/en-us/articles/49269197499667)
  * Instructions for [Optimize for non-Webflow sites](https://help-optimize.webflow.com/hc/en-us/articles/49271408921875)
</Steps>
