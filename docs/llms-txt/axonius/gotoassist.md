# Source: https://docs.axonius.com/docs/gotoassist.md

# RescueAssist (GoToAssist)

RescueAssist (formerly GoToAssist) is a cloud-based toolset for IT and customer support teams including remote support, IT monitoring, and service desk management.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Client ID** and **Client Secret** *(required)* - The credentials for an account that has authorization to the RescueAssist API. Follow [GoTo Assist How to create an OAuth Client](https://developer.goto.com/guides/Get%20Started/02_HOW_createClient/) for details.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets. Refer to [GoTo Assist documentation](https://developer.goto.com/guides/Get%20Started/00_Ref-Get-Started/) for details.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="RescueAssist" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RescueAssist.png" />

## APIs

Axonius uses the [GoToConnect API](https://developer.goto.com/guides/GoToConnect/09_HOW_fetchAccountUsers/)

## Required Permissions

The value supplied in [User Name](#parameters) and [Client ID](#parameters) must have read permissions in order to fetch assets.