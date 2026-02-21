# Source: https://www.zaproxy.org/docs/authentication/

Title: ZAP – Authentication Decision Tree

URL Source: https://www.zaproxy.org/docs/authentication/

Markdown Content:
### Question: Does your app have a login page?

##### Background

This guide explains how to set up ZAP to handle authentication in your applications. It is in the format of a decision tree - follow the relevant answers and it will lead you to the best solution for your apps.

If your application uses authentication then you will need to configure ZAP to handle it, otherwise ZAP will not be able to access any of the protected functionality.

Unfortunately web app authentication is very complicated and there are many ways in which applications implement it.

ZAP typically needs to handle apps with login pages differently than those without, so this is why we start with this question.
