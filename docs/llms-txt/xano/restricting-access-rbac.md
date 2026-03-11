# Source: https://docs.xano.com/building-backend-features/user-authentication-and-user-data/restricting-access-rbac.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Restricting Access (RBAC)

RBAC (Role-based access control) or role-based permissions is a way to restrict access based on a user's defined role. This guide will cover two different methods of enforcing access / RBAC to an API endpoint based on the user's role.

<Frame>
  <iframe width="609" height="342" src="https://www.youtube.com/embed/LZMTEEdnd5o" title="Role-based Access Control (RBAC)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

Let's use the following user table for both examples of RBAC. Make note of the role field and the values for each user.

<Frame caption="In this example, each user has one of two roles: admin or staff.">
  <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/488995f4-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=55af08a0483765f84a0f3650c8da53af" width="960" height="540" data-path="images/488995f4-image.jpeg" />
</Frame>

#### **RBAC Example 1: Use Get Record**

Now, let's set up an API endpoint that GETs all users but only if the user trying to call the endpoint has a role of admin.

Take note of the endpoint below, user authentication is required. Additionally, take note of the Function Stack:

1. Get Record from user: This will use the authToken to find the user's ID and look up their information.

2. Precondition: This will enforce that the user's role is equal to admin. If it is not, then it will throw and error and stop the endpoint.

3. Query all records from user: This will only be performed if the user's role is an admin by passing the precondition.

<Frame caption="In this example, the API endpoint requires an authenticated user. Then the Function Stack is set up to perform only if the user's role is equal to admin.">
  <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/5232b6d5-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=d398aa4e2ad8d0d79888ee5abac9c66c" width="960" height="540" data-path="images/5232b6d5-image.jpeg" />
</Frame>

Get the record of the user who's calling the endpoint (requester) with the auth ID.

<Frame caption="In this example, we are getting the record of the user based on their authenticated ID.">
  <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/2b095778-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=7262821dc152f8224c48abc351110cd0" width="960" height="540" data-path="images/2b095778-image.jpeg" />
</Frame>

Next, set a precondition to enforce that the user (called requester in the example) has a role equal to admin.

<Frame caption="Click on the pencil icon to open the Expression Builder and set the conditions for the precondition. Additionally, set your error type and message if the conditions are not met.">
  <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/4fb40188-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=15f59c7a102844ba80781a63b124ef3a" width="960" height="540" data-path="images/4fb40188-image.jpeg" />
</Frame>

<Frame caption="In this example, the requester.role must be equal to admin in order to pass the precondition.">
  <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/dbd9ddaf-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=df3d9eeddce79018c29fdae3e11a266d" width="960" height="540" data-path="images/dbd9ddaf-image.jpeg" />
</Frame>

If the precondition is met, then the user who is the requester will have permission to execute the rest of the Function Stack and complete the API endpoint.

#### RBAC Example 2: Use Extras

[Extras](/building-backend-features/user-authentication-and-user-data#extras) allow you to store data within the authentication token, which you can access and use on authenticated API endpoints.

First, you must set up the [sign-up & login](/building-backend-features/user-authentication-and-user-data) to include the user's role at the time of authentication.

In this example, we will use the login endpoint to pass the user's role into extras of the auth token at the time of authentication.

<Frame caption="In this example, we are passing the user's role into the authToken at the time of login by utilizing extras.">
  <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/0da46626-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=1f194df6428425bf25ea3e36c2416530" width="960" height="540" data-path="images/0da46626-image.jpeg" />
</Frame>

Now that the user's role is passed into the authToken, we can eliminate the Get Record function from the previous example and reference "extras.role" in the precondition to enforce the user's role.

<Frame caption="In this example, we can use the extras of the authenticated user to access the user's role and set the precondition equal to admin.">
  <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e63d49e6-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=d93105a19f4eeef99171c09c4c816ad2" width="960" height="540" data-path="images/e63d49e6-image.jpeg" />
</Frame>

<Frame caption="Set extras.role (as defined in the creation of the authentication token) equal to admin.">
  <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/799beb5e-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=c6f475495c578deef866f70b95b8a4b1" width="960" height="540" data-path="images/799beb5e-image.jpeg" />
</Frame>

If the user's role is equal to admin then they will pass the precondition and have permission to execute the rest of the Function Stack.


Built with [Mintlify](https://mintlify.com).