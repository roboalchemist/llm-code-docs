# Source: https://clickhouse.ferndocs.com/cloud/manage/postman.md

---
slug: /cloud/manage/postman
sidebar_label: Programmatic API access with Postman
title: Programmatic API access with Postman
description: This guide will help you test the ClickHouse Cloud API using Postman
doc_type: guide
keywords:

- api
- postman
- rest api
- cloud management
- integration

---

This guide will help you test the ClickHouse Cloud API using [Postman](https://www.postman.com/product/what-is-postman/).
The Postman Application is available for use within a web browser or can be downloaded to a desktop.

### Create an account [#create-an-account]

- Free accounts are available at [https://www.postman.com](https://www.postman.com).

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/89fcfc1b047dbefec9e464f234dedd887a9dd2a7e4e3fcc602be41003c347db2/images/cloud/manage/postman/postman1.png" alt="Postman site"/>

### Create a workspace [#create-a-workspace]

- Name your workspace and set the visibility level.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/846a3c9528c0b1a7cd2402e1f4e3a15162eefd7bdf752018a1c4f2821fa0b0f2/images/cloud/manage/postman/postman2.png" alt="Create workspace"/>

### Create a collection [#create-a-collection]

- Below "Explore" on the top left Menu click "Import":

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/c8af9fb0dc75ecbf393756cf19614a37c93e484b07ac405e5c7c58715bdb2345/images/cloud/manage/postman/postman3.png"/> Import" border/>

- A modal will appear:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/493b3de707a757e5572d954fb2eabc24c1000780bdb56558298bfa62f6d8c9bb/images/cloud/manage/postman/postman4.png" alt="API URL entry"/>

- Enter the API address: "https://api.clickhouse.cloud/v1" and press 'Enter':

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/3eaccdec52e27e9e6859ec55c56a88136051c6707bfb5fbdb345d95a5d1f7906/images/cloud/manage/postman/postman5.png" alt="Import"/>

- Select "Postman Collection" by clicking on the "Import" button:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9d013268339b967e8658d83900579dce33cf7889d0a18ab4119ade48ec0837a8/images/cloud/manage/postman/postman6.png"/> Import" border/>

### Interface with the ClickHouse Cloud API spec [#interface-with-the-clickhouse-cloud-api-spec]
- The "API spec for ClickHouse Cloud" will now appear within "Collections" (Left Navigation).

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/f1b2cf8816ff16503044620879c66dd1fc082504d5a50e04bc85e99c8762c24a/images/cloud/manage/postman/postman7.png" alt="Import your API"/>

- Click on "API spec for ClickHouse Cloud." From the middle pain select the 'Authorization' tab:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/c04ceb05ce30e4705e45f9ecda6b704eb52250ddee884189bf1f24938f8b9a2b/images/cloud/manage/postman/postman8.png" alt="Import complete"/>

### Set authorization [#set-authorization]
- Toggle the dropdown menu to select "Basic Auth":

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/09876538b0b7daa438ef2399561fc40c7e852516252fa75608e52f9946df233e/images/cloud/manage/postman/postman9.png" alt="Basic auth"/>

- Enter the Username and Password received when you set up your ClickHouse Cloud API keys:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/ba1fa8d4c65250259cc0c2e167eff5a30e9c7c4c6fb4575b1b7a3e066a8025ad/images/cloud/manage/postman/postman10.png" alt="credentials"/>

### Enable variables [#enable-variables]

- [Variables](https://learning.postman.com/docs/sending-requests/variables/) enable the storage and reuse of values in Postman allowing for easier API testing.

#### Set the organization ID and Service ID [#set-the-organization-id-and-service-id]

- Within the "Collection", click the "Variable" tab in the middle pane (The Base URL will have been set by the earlier API import):
- Below `baseURL` click the open field "Add new value", and Substitute your organization ID and service ID:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/625101ba6627f43e15bc1430f2aa9f67938f0120ffaa5b66b04c2cb1c41b51ba/images/cloud/manage/postman/postman11.png" alt="Organization ID and Service ID"/>

## Test the ClickHouse Cloud API functionalities [#test-the-clickhouse-cloud-api-functionalities]

### Test "GET list of available organizations" [#test-get-list-of-available-organizations]

- Under the "OpenAPI spec for ClickHouse Cloud", expand the folder > V1 > organizations
- Click "GET list of available organizations" and press the blue "Send" button on the right:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/0d3d1cf8fb00447e9e01e4c8415525a6c1c013053c541dd4d129fb34e30411fd/images/cloud/manage/postman/postman12.png" alt="Test retrieval of organizations"/>

- The returned results should deliver your organization details with "status": 200. (If you receive a "status" 400 with no organization information your configuration is not correct).

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/eb18e4a70d5564f615fcd50d2804ec1b58dd1addbfe348ce2f65936c0b655c62/images/cloud/manage/postman/postman13.png" alt="Status"/>

### Test "GET organizational details" [#test-get-organizational-details]

- Under the `organizationid` folder, navigate to "GET organizational details":
- In the middle frame menu under Params an `organizationid` is required.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9c7b366003801501c2847841ea6061d69d365fc57bb19148fdcb178459730b22/images/cloud/manage/postman/postman14.png" alt="Test retrieval of organization details"/>

- Edit this value with `orgid` in curly braces `{{orgid}}` (From setting this value earlier a menu will appear with the value):

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/06c9319eb90d40c8adb5ed5db0222284ed4b791c692bd032362794fef5874446/images/cloud/manage/postman/postman15.png" alt="Submit test"/>

- After pressing the "Save" button, press the blue "Send" button at the top right of the screen.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/29fe96fa24b3fd4d7b83ca129b6f7fadea9d11f07a0a883d8e55fad483fef3a6/images/cloud/manage/postman/postman16.png" alt="Return value"/>

- The returned results should deliver your organization details with "status": 200. (If you receive a "status" 400 with no organization information your configuration is not correct).

### Test "GET service details" [#test-get-service-details]

- Click "GET service details"
- Edit the Values for `organizationid` and `serviceid` with `{{orgid}}` and `{{serviceid}}` respectively.
- Press "Save" and then the blue "Send" button on the right.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/e78ebc10053b3e2578179f55b66982d9fb5c2acca04debd5f5153227993b79ea/images/cloud/manage/postman/postman17.png" alt="List of services"/>

- The returned results should deliver a list of your services and their details with "status": 200. (If you receive a "status" 400 with no service(s) information your configuration is not correct).
