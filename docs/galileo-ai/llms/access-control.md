# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-observe/how-to/access-control.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/access-control.md

# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/galileo-product-features/access-control.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Access Control Features | Galileo NLP Studio

> Discover Galileo NLP Studio's access control features, including user roles and group management, to securely share and manage projects within your organization.

Galileo supports fine-grained control over granting users different levels of access to the system, as well as organizing users into groups for easily sharing projects.

## System-level Roles

There are 4 roles that a user can be assigned:

**Admin** – Full access to the organization, including viewing all projects.

**Manager** – Can add and remove users.

**User** – Can create, update, share, and delete projects and resources within projects.

**Read-only** – Cannot create, update, share, or delete any projects or resources. Limited to view-only permissions.

In chart form:

|                                       | Admin                              | Manager                                         | User                                       | Read-only                                  |
| ------------------------------------- | ---------------------------------- | ----------------------------------------------- | ------------------------------------------ | ------------------------------------------ |
| View all projects                     | <Icon icon="square-check" />       | <Icon icon="square-xmark" />                    | <Icon icon="square-xmark" />               | <Icon icon="square-xmark" />               |
| Add/delete users                      | <Icon icon="square-check" />       | <Icon icon="square-check" /> (excluding admins) | <Icon icon="square-xmark" />               | <Icon icon="square-xmark" />               |
| Create groups, invite users to groups | <Icon icon="square-check" />       | <Icon icon="square-check" />                    | <Icon icon="square-check" />               | <Icon icon="square-xmark" />               |
| Create/update projects                | <Icon icon="square-check" />       | <Icon icon="square-check" />                    | <Icon icon="square-check" />               | <Icon icon="square-xmark" />               |
| Share projects                        | <Icon icon="square-check" />       | <Icon icon="square-check" />                    | <Icon icon="square-check" />               | <Icon icon="square-xmark" />               |
| View projects                         | <Icon icon="square-check" /> (all) | <Icon icon="square-check" /> (only shared)      | <Icon icon="square-check" /> (only shared) | <Icon icon="square-check" /> (only shared) |

System-level roles are chosen when users are invited to Galileo:

<Frame caption="Invite new users">
  <img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/access-control.png?fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=074b1ef064e1b4ed46886584d6332a4a" width="400" data-og-width="774" data-og-height="1100" data-path="images/access-control.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/access-control.png?w=280&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=8057254bc60bbe79bd3ac849affbff0c 280w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/access-control.png?w=560&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=0115b567cf740b6735089d6745934487 560w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/access-control.png?w=840&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=3be571e80881c1783ccc5a6382bf2d84 840w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/access-control.png?w=1100&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=d0e92f5188ba10118028487e1888faa1 1100w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/access-control.png?w=1650&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=df98c6de67ec0f2646917dcb6055a8e9 1650w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/access-control.png?w=2500&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=6e7fd3cd89ecaac738753e370ea9328d 2500w" />
</Frame>

## Groups

Users can be organized into groups to streamline sharing projects.

There are 3 types of groups:

**Public** – Group and members are visible to everyone in the organization. Anyone can join.

**Private** – Group is visible to everyone in the organization. Members are kept private. Access is granted by a group maintainer.

**Hidden** – Group and its members are hidden from non-members in the organization. Access is granted by a group maintainer.

Within a group, each member has a group role:

**Maintainer** – Can add and remove members.

**Member** – Can view other members and shared projects.

## Sharing Projects

By default, only a project's creator (and managers and admins) have access to a project. Projects can be shared both with individual users and entire groups. Together, these are called *collaborators.* Collaborators can be added when you create a project:

<Frame caption="Create a project with collaborators">
  <img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/access-control-2.png?fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=1dd70c3df9c2cf6e5607dbcbce9a98b4" width="400" data-og-width="1066" data-og-height="1220" data-path="images/access-control-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/access-control-2.png?w=280&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=10b46db14d8a7587baea9aaab35ed522 280w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/access-control-2.png?w=560&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=c83085a3f7e87f5dafdda222a63e3d72 560w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/access-control-2.png?w=840&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=a68a77ba219e989a952217ce39c9f8c7 840w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/access-control-2.png?w=1100&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=b8820c70b96cb860e23cbad23f47df54 1100w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/access-control-2.png?w=1650&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=2bafed1c254e8bd65d4cab33f7bc0f38 1650w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/access-control-2.png?w=2500&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=a2afbd55f5e6e532075a0fd3330cd542 2500w" />
</Frame>

Or anytime afterwards:

<Frame caption="Share a project">
  <img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/access-control-3.png?fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=e2671c2f7ee1b6f09ea10c7ec0f000e0" width="400" data-og-width="1042" data-og-height="330" data-path="images/access-control-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/access-control-3.png?w=280&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=6b8ca1c8328b956e41312ea6acf569c5 280w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/access-control-3.png?w=560&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=7216aa0ffc2bf1bd067dccb821f764cc 560w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/access-control-3.png?w=840&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=7d07f70896b39d06ee9794f38479fd9c 840w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/access-control-3.png?w=1100&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=33ba4dca51fb0a0f27a290bb9bac333b 1100w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/access-control-3.png?w=1650&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=301a48b3753d8196fc1fee3791d7e535 1650w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/access-control-3.png?w=2500&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=d50b9aa98f106c42ed11612f679771fb 2500w" />
</Frame>
