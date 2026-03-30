# Source: https://docs.base44.com/developers/references/sdk/docs/interfaces/app-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# app-logs

***

## Overview

App Logs module for tracking and analyzing app usage.

This module provides a method to log user activity. The logs are reflected in the Analytics page in the app dashboard.

### Authentication Modes

This module is available to use with a client in all authentication modes.

## Methods

### logUserInApp()

> **logUserInApp**(`pageName`): `Promise`\<`void`>

Log user activity in the app.

Records when a user visits a specific page or section of the app. Useful for tracking user navigation patterns and popular features. The logs are reflected in the Analytics page in the app dashboard.

The specified page name doesn't have to be the name of an actual page in the app, it can be any string you want to use to track the activity.

#### Parameters

<ParamField body="pageName" type="string" required>
  Name of the page or section being visited.
</ParamField>

#### Returns

`Promise<void>`

Promise that resolves when the log is recorded.

#### Example

<CodeGroup>
  ```typescript Log page visit or feature usage theme={null}
  await base44.appLogs.logUserInApp('home');
  await base44.appLogs.logUserInApp('features-section');
  await base44.appLogs.logUserInApp('button-click');
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).