# Source: https://docs.socket.dev/docs/create-socket-api-key-for-cicd.md

# Create Socket API Key for CI/CD

## Create your Socket API token

You can either create your API token yourself if you have permissions in your socket.dev account or you can have your Admin create it for you with the Reports scope.

1. Log into the socket.dev dashboard
2. Go to Settings
3. Go to the API Tokens tab
4. Select Create API Token
5. Give the token a name like **CI/CD API Token**
6. Select the following scopes

   1. **repo**

      1. repo:list
      2. repo:create
      3. repo:update
   2. **security-policy**
      1. security-policy:read
   3. **Triage**

      1. list

      2. update
   4. **full-scans**

      1. full-scans:list
      2. full-scans:create
   5. **packages**

      1. packages:list
7. Click Confirm
8. Click on **Show key**
9. Click on the API Token to copy