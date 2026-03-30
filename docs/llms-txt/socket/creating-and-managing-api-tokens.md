# Source: https://docs.socket.dev/reference/creating-and-managing-api-tokens.md

# Creating and Managing API Tokens

## Introduction

Socket provides a powerful API that allows you to interact with your organization's data programmatically. To authenticate API requests, you need to use API tokens. This guide will show you how to generate and manage these tokens within your organization.

## Generating a New API Token

To generate a new API token:

1. **Navigate to Settings**: On the Socket dashboard, go to `Settings` in the left-hand menu.
2. **Access API Tokens**: Click on the `API Tokens` tab within the Settings menu.
3. **Create API Token**: Click the `+ Create API token` button in the upper-right corner.
4. A dialog will appear where you can set the name and choose the scopes for the token.
5. After selecting the appropriate scopes, click **Confirm** to generate the token.

<Image align="center" src="https://files.readme.io/4350e63-Screenshot_2024-08-13_at_5.59.25_PM.png" />

<br />

## Editing and Managing API Tokens

1. To edit an API token, navigate to the **API Tokens** section.
2. Click on the ellipsis (**...**) next to the token you want to manage.
3. You can **Edit name**, **Edit scopes**, **Edit visibility**, **Rotate token**, or **Revoke token** as needed.

<Image align="center" src="https://files.readme.io/ed38f01-Screenshot_2024-08-13_at_5.50.54_PM.png" />

## Best Practices

* **Least Privilege Principle**: Assign only the necessary scopes to each token to minimize potential security risks.
* **Regular Rotation**: Regularly rotate your tokens to reduce the impact of a compromised token.
* **Audit and Review**: Periodically review the tokens and their scopes to ensure they align with current organizational needs and security practices.