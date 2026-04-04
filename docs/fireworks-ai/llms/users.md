# Source: https://docs.fireworks.ai/accounts/users.md

# Managing users

> Add and delete additional users in your Fireworks account

See the concepts [page](/getting-started/concepts#account) for definitions of accounts and users. Only admin users can manage other users within the account.

## Adding users

To add a new user to your Fireworks account, run the following command. If the email for the new user is already associated with a Fireworks account, they will have the option to freely switch between your account and their existing account(s). You can also add users in the Fireworks web UI at [https://app.fireworks.ai/account/users](https://app.fireworks.ai/account/users).

```bash  theme={null}
firectl create user --email="alice@example.com"
```

To create another admin user, pass the `--role=admin` flag:

```bash  theme={null}
firectl create user --email="alice@example.com" --role=admin
```

## Updating a user's role

To update a user's role, run

```bash  theme={null}
firectl update user <USER_ID> --role="{admin,user}"
```

## Deleting users

You can remove a user from your account by running:

```bash  theme={null}
firectl delete user <USER_ID>
```
