# Source: https://docs.fireflies.ai/schema/user-groups.md

# Source: https://docs.fireflies.ai/graphql-api/query/user-groups.md

# Source: https://docs.fireflies.ai/schema/user-groups.md

# Source: https://docs.fireflies.ai/graphql-api/query/user-groups.md

# Source: https://docs.fireflies.ai/schema/user-groups.md

# User Groups

> Schema for User Groups

<ResponseField name="id" type="String">
  Unique ID for the user group
</ResponseField>

<ResponseField name="name" type="String">
  Name of the user group.
</ResponseField>

<ResponseField name="handle" type="String">
  Unique identifier or handle for the user group.
</ResponseField>

<ResponseField name="members" type="[UserGroupMember]" nullable="true">
  List of members in the user group. See [UserGroupMember](/schema/user-group-member)
</ResponseField>

## Additional Resources

<CardGroup cols={2}>
  <Card title="User" icon="link" href="/schema/user">
    Schema for User
  </Card>

  <Card title="User Group Member" icon="link" href="/schema/user-group-member">
    Schema for User Group Member
  </Card>
</CardGroup>
