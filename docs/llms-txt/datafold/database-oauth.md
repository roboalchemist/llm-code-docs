# Source: https://docs.datafold.com/security/database-oauth.md

# Database OAuth

> Datafold enables secure workflows like data diffs through OAuth, ensuring compliance with user-specific database permissions.

To improve data security and privacy, Datafold supports running workflows like data diffs through OAuth. This ensures queries are executed using the user's own database credentials, fully complying with granular access controls like data masking and object-level permissions.

The diagram below illustrates how the authentication flow proceeds:

1. Users authenticate using the configured OAuth provider.
2. Users can then create diffs between data sets that their user can access using OAuth database permissions.
3. During Continuous Integration (CI), Datafold executes diffs using a Service Account with the least privileges, thus masking sensitive/PII data.
4. If a user needs to see sensitive/PII data from a CI diff, and they have permission via OAuth to do so, they can rerun the diff, and then Datafold will authenticate the user using OAuth database permissions. Then, the user will have access to the data based on these permissions.

This structure ensures that diffs are executed with the user's database credentials with their configured roles and permissions. Data access permissions are thus fully managed by the database, and Datafold only passes through queries.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/rbac-with-sso-auth-flow-f641e578b9ee12f4ab09e5573125cb0a.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=c97a5cc781ff4bd1209c9efe06e5c1c6" data-og-width="3898" width="3898" data-og-height="2950" height="2950" data-path="images/rbac-with-sso-auth-flow-f641e578b9ee12f4ab09e5573125cb0a.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/rbac-with-sso-auth-flow-f641e578b9ee12f4ab09e5573125cb0a.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=4cb1a240af1a8ef1c8a1a6fe4d5042e0 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/rbac-with-sso-auth-flow-f641e578b9ee12f4ab09e5573125cb0a.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=3c4de42e0b5ce184e5bf2a29771e1245 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/rbac-with-sso-auth-flow-f641e578b9ee12f4ab09e5573125cb0a.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=59dddd239015bd7ca4a9db203ecd3e17 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/rbac-with-sso-auth-flow-f641e578b9ee12f4ab09e5573125cb0a.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ded86dded41cde0752adc01c543bfd2a 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/rbac-with-sso-auth-flow-f641e578b9ee12f4ab09e5573125cb0a.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2ccf9b36a6cf6963c5274185a20bd867 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/rbac-with-sso-auth-flow-f641e578b9ee12f4ab09e5573125cb0a.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=50eb3fcc49b9bbe49b592547905a46ff 2500w" />
</Frame>
