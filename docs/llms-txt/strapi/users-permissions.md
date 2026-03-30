# Users & Permissions

The Users & Permissions feature allows the management of the end-users  of a Strapi project. It provides a full authentication process based on JSON Web Tokens (JWT) to protect your API, and an access-control list (ACL) strategy that enables you to manage permissions between groups of users.

</IdentityCard>

## Admin panel configuration

The Users & Permissions feature is configured from both the admin panel settings, and via the code base.

### Roles

The Users & Permissions feature allows to create and manage roles for end users, to configure what they can have access to.

#### Creating a new role

**Path:** 

<!---
:::tip
Click the search button 

</Tabs>

### Registration configuration

If you have added any additional fields in your User **model**  that need to be accepted on registration, you need to added them to the list of allowed fields in the `config.register` object of [the `/config/plugins` file](/cms/configurations/plugins), otherwise they will not be accepted.

The following example shows how to ensure a field called "nickname" is accepted by the API on user registration:

</Tabs>

### Rate limiting configuration

Rate limiting is applied to authentication and registration endpoints to prevent abuse.  The following parameters can be configured to change its behavior. Additional configuration options are provided by the 

</Tabs>

### Templating emails

By default this plugin comes with two templates: reset password and email address confirmation. The templates use 

</Tabs>

### Security configuration

JWTs can be verified and trusted because the information is digitally signed. To sign a token a _secret_ is required. By default Strapi generates and stores it in `/extensions/users-permissions/config/jwt.js`.

This is useful during development but for security reasons it is recommended to set a custom token via an environment variable `JWT_SECRET` when deploying to production.

By default you can set a `JWT_SECRET` environment variable and it will be used as secret. If you want to use another variable you can update the configuration file.

</Tabs>

#### Creating a custom callback validator {#creating-a-custom-password-validation}

By default, Strapi SSO only redirects to the redirect URL that is exactly equal to the url in the configuration:

</ApiCall>

To log out of all sessions, send the following request:

</ApiCall>

#### Identifier

The `identifier` parameter sent with requests can be an email or username, as in the following examples:

</Tabs>

#### Token usage

The `jwt` may then be used for making permission-restricted API requests. To make an API request as a user place the JWT into an `Authorization` header of the `GET` request.

Any request without a token will assume the `public` role permissions by default. Modify the permissions of each user's role in the admin dashboard.

Authentication failures return a `401 (unauthorized)` error.

The `token` variable is the `data.jwt` received when logging in or registering.

```js

const token = 'YOUR_TOKEN_HERE';

// Request API.
axios
  .get('http://localhost:1337/posts', {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  })
  .then(response => {
    // Handle success.
    console.log('Data: ', response.data);
  })
  .catch(error => {
    // Handle error.
    console.log('An error occurred:', error.response);
  });
```

#### User registration

Creating a new user in the database with a default role as 'registered' can be done like in the following example:

```js

// Request API.
// Add your own code here to customize or restrict how the public can register new users.
axios
  .post('http://localhost:1337/api/auth/local/register', {
    username: 'Strapi user',
    email: 'user@strapi.io',
    password: 'strapiPassword',
  })
  .then(response => {
    // Handle success.
    console.log('Well done!');
    console.log('User profile', response.data.user);
    console.log('User token', response.data.jwt);
  })
  .catch(error => {
    // Handle error.
    console.log('An error occurred:', error.response);
  });
```

#### User object in Strapi context

The `user` object is available to successfully authenticated requests.

The authenticated `user` object is a property of `ctx.state`.

```js
create: async ctx => {
  const { id } = ctx.state.user;

  const depositObj = {
    ...ctx.request.body,
    depositor: id,
  };

  const data = await strapi.services.deposit.add(depositObj);

  // Send 201 `created`
  ctx.created(data);
};
```