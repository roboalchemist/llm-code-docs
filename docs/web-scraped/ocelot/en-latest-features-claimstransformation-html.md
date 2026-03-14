# Source: https://ocelot.readthedocs.io/en/latest/features/claimstransformation.html

Title: Claims Transformation — Ocelot Gateway 24.1 "Globality" documentation

URL Source: https://ocelot.readthedocs.io/en/latest/features/claimstransformation.html

Markdown Content:
Ocelot allows the user to access claims and transform them into headers, query string parameters, other claims and change downstream paths. This is only available once a user has been authenticated.

After the user is authenticated, we run the claims to claims transformation middleware (see the [ClaimsToClaimsMiddleware](https://github.com/search?q=repo%3AThreeMammals%2FOcelot%20ClaimsToClaimsMiddleware&type=code) class). This allows the user to transform claims before the authorization middleware is called. After the user is authorized, we call the claims to headers middleware (see the [ClaimsToHeadersMiddleware](https://github.com/search?q=repo%3AThreeMammals%2FOcelot+ClaimsToHeadersMiddleware&type=code) class), then the claims to query string parameters middleware (see the [ClaimsToQueryStringMiddleware](https://github.com/search?q=repo%3AThreeMammals%2FOcelot+ClaimsToQueryStringMiddleware&type=code) class), and finally the claims to downstream path middleware (see the [ClaimsToDownstreamPathMiddleware](https://github.com/search?q=repo%3AThreeMammals%2FOcelot+ClaimsToDownstreamPathMiddleware&type=code) class).

The syntax for performing the transforms is the same for each process. In the route configuration, a JSON dictionary is added with a specific name either `AddClaimsToRequest`, `AddHeadersToRequest`, `AddQueriesToRequest`, or `ChangeDownstreamPathTemplate`.

> **Note**: This syntax is not ideal. So any suggestions are welcome…

Within this dictionary the entries specify how Ocelot should transform things! The key to the dictionary is going to become the key of either a claim, header or query parameter. In the case of `ChangeDownstreamPathTemplate`, the key must be also specified in the `DownstreamPathTemplate`, in order to do the transformation.

The value of the entry is parsed to logic that will perform the transform. First of all, a dictionary accessor is specified e.g. `Claims[CustomerId]`. This means we want to access the claims and get the `CustomerId` claim type. Next is a “greater than” `>` symbol which is just used to split the string. The next entry is either value or value with an indexer. If value is specified, Ocelot will just take the value and add it to the transform. If the value has an indexer, Ocelot will look for a delimiter which is provided after another “greater than” `>` symbol. Ocelot will then split the value on the delimiter and add whatever was at the index requested to the transform.

Claims to Claims[¶](https://ocelot.readthedocs.io/en/latest/features/claimstransformation.html#claims-to-claims "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------

Below is an example configuration that will transform claims to claims

"AddClaimsToRequest": {
 "UserType": "Claims[sub] > value[0] > |",
 "UserId": "Claims[sub] > value[1] > |"
}

This shows a transforms where Ocelot looks at the users `sub` claim and transforms it into `UserType` and `UserId` claims. Assuming the `sub` looks like this `usertypevalue|useridvalue`.

Claims to Query String Parameters[¶](https://ocelot.readthedocs.io/en/latest/features/claimstransformation.html#claims-to-query-string-parameters "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Below is an example configuration that will transform claims to query string parameters

"AddQueriesToRequest": {
 "LocationId": "Claims[LocationId] > value",
}

This shows a transform where Ocelot looks at the users `LocationId` claim and add it as a query string parameter to be forwarded onto the downstream service.

Claims to Downstream Path[¶](https://ocelot.readthedocs.io/en/latest/features/claimstransformation.html#claims-to-downstream-path "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------

Below is an example configuration that will transform claims to downstream path custom placeholders:

"UpstreamPathTemplate": "/api/users/me/{everything}",
"DownstreamPathTemplate": "/api/users/{userId}/{everything}",
"ChangeDownstreamPathTemplate": {
 "userId": "Claims[sub] > value[1] > |",
}

This shows a transform where Ocelot looks at the users `userId` claim and substitutes the value to the `{userId}` placeholder specified in the `DownstreamPathTemplate`. Take into account that the key specified in the `ChangeDownstreamPathTemplate` must be the same than the placeholder specified in the `DownstreamPathTemplate`.

> **Note**: If a key specified in the `ChangeDownstreamPathTemplate` does not exist as a placeholder in `DownstreamPathTemplate`, it will fail at runtime returning an error in the response.
