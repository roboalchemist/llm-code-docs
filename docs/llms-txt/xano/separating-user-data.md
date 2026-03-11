# Source: https://docs.xano.com/building-backend-features/user-authentication-and-user-data/separating-user-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Separating User Data

Separating and restricting access to data are two common features of building a backend. Separating data is crucial for multi-tenant systems. It means that even though all your users have data in the same table, they are only able to see and access the data that belongs to them.

[Restricting Access](/building-backend-features/user-authentication-and-user-data/restricting-access-rbac) (Role-Based Access Control) takes this to another level if, for example, there are special roles assigned to users like an admin who may have permission to access more data than a standard user. You can read more on restricting access or RBAC by clicking the link at the beginning of this paragraph.

<Frame>
  <iframe width="609" height="342" src="https://www.youtube.com/embed/ohL2vR5wp3o" title="Separating Data" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

### Separating Data Example 1

For this example, we have three users in our user table: Steph, Klay, and Jordan.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/941f0967-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=067bb769dfcec3cdf049a3db52dfe99d" width="1046" height="373" data-path="images/941f0967-image.jpeg" />
</Frame>

There is also an items table. Each item belongs to a user.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/WBQXG-4Ngk82eYAW/images/fa3f359e-image.jpeg?fit=max&auto=format&n=WBQXG-4Ngk82eYAW&q=85&s=565d2c47a5f69f07b4c2091b019e6c20" width="914" height="505" data-path="images/fa3f359e-image.jpeg" />
</Frame>

#### How to enforce a user only sees the items that belongs to them

Here we have an API endpoint, which gets all the items from the items table. The first step is to require user [authentication](/building-backend-features/user-authentication-and-user-data) on the endpoint.

<Frame
  caption="Require authentication for the API endpoint.
"
>
  <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/22ad99a3-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=4257f4f6032678358b151c464da937a0" width="1773" height="782" data-path="images/22ad99a3-image.jpeg" />
</Frame>

Now that authentication is required, the next step is to open the [Query All Records](/the-function-stack/functions/database-requests/query-all-records) function and add an expression to the by custom query section.

```python  theme={null}
WHERE
db: items.user_id = auth id
```

<Frame caption="Add an expression to the Query All Records function for items.">
  <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/c3498fb2-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=66a00bc88cf759b21295679695b76f5c" width="1785" height="797" data-path="images/c3498fb2-image.jpeg" />
</Frame>

<Frame caption="Filter the record where the user_id must be equal to the auth id.">
  <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/be91a3a6-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=9d1811f95c9c494d9ccbae287653c140" width="1321" height="463" data-path="images/be91a3a6-image.jpeg" />
</Frame>

When we go to run the API endpoint in Run\&Debug, an auth token is required to run the API. In Xano, we can easily search for a user to use a auth token for testing. In your application, the user will need to [authenticate](/building-backend-features/user-authentication-and-user-data) first by logging in or signing up.

Let's select user 2, Klay and run the API endpoint:

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/0f6b2ac9-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=b4f035847527d34d4d4a07f78ff38459" width="599" height="894" data-path="images/0f6b2ac9-image.jpeg" />
</Frame>

The result is all the items associated with user id = 2:

<Frame caption="Items only belonging to user 2 are returned.">
  <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/b7b9f62c-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=4e3f5ea9b141795453b7d2e7523d46b7" width="598" height="685" data-path="images/b7b9f62c-image.jpeg" />
</Frame>

#### Added layer of security with precondition

We can add an additional layer of security with the use of preconditions.

First, use a Get Record on the user table with a field value of the auth id.

<Frame caption="Get the user record with the auth id.">
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/36d1f1a9-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=c00ab49be42782f566c2390890da1b68" width="1786" height="734" data-path="images/36d1f1a9-image.jpeg" />
</Frame>

Then use a precondition to enforce the auth ID is equal to the id from the Get Record.

```python  theme={null}
WHERE
auth id = var: user.id
```

<Frame caption="Set a precondition where the ID of the user record is equal to the auth id.">
  <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/25e14a51-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=c06ad37b5c137caf65daf6b2eee8413a" width="602" height="666" data-path="images/25e14a51-image.jpeg" />
</Frame>

#### How to enforce the user can only edit data that belongs to them

When it comes to editing data, the function stack will also use a precondition. The API endpoint will once again require authentication.

First, we need to Get the Record of the item that the user wants to edit.

<Frame caption="First, Get the Record that the user is trying to edit.">
  <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/4a98298a-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=7365bf26154b5d64da468f2c35adafc7" width="1765" height="809" data-path="images/4a98298a-image.jpeg" />
</Frame>

Getting the existing record allows us to check if it belongs to the user.

Next, use a Precondition to say:

```python  theme={null}
WHERE
var: items_1 |GET| "user_id" = auth id
```

<Frame caption="The precondition enforces that the record belongs to the user trying to edit it. Using the GET filter makes sure that the record exists - if it doesn't the precondition will fail.">
  <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/222fa1bc-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=feebc5653e5b89eb0c40f5a2c525a952" width="1231" height="734" data-path="images/222fa1bc-image.jpeg" />
</Frame>

Here we use the GET filter with a default value of 0. This helps us account for existence of the record we want to edit. If the record does not exist, the precondition will trigger because a user\_id value of 0 will not match the auth ID.

If the precondition passes, then the function stack will continue to run and edit the data. If it fails, it will throw an error and stop execution.


Built with [Mintlify](https://mintlify.com).