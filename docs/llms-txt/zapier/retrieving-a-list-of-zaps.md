# Source: https://docs.zapier.com/powered-by-zapier/zap-creation/retrieving-a-list-of-zaps.md

# Retrieving a list of Zaps

> Listing a users zaps reveals existing workflows created by users.

### Prerequisites

* Your app needs to be published as a [public integration](https://platform.zapier.com/quickstart/private-vs-public-integrations) in Zapier's App Directory.

### Example Implementation

<Frame caption="Unbounce uses the /zaps endpoint to display users' Zaps using their integration directly within the Unbounce platform.">
  <video controls className="w-full aspect-video" src="https://cdn.zappy.app/c272eef3c4261c529e8e9e0ce9d5630b.mp4" />
</Frame>

## Fetching a list of Zaps for a user

<Steps>
  <Step title="Authenticate with Zapier">
    Following the [authentication
    guide](/powered-by-zapier/authentication/methods/user-access-token), receive
    a token from the Zapier Workflow API.
  </Step>

  <Step title="Create your request, and filter as needed">
    Leverage the [`/zaps`
    endpoint](/powered-by-zapier/api-reference/zaps/get-zaps-\[v2]) to fetch a
    users zaps. - You can optionally filter the list by specific input values,
    which can be helpful for instances where a user has a zap associated to
    specific resources. Example might be a specific trello board or google
    sheet. See [the
    api-reference](/powered-by-zapier/api-reference/zaps/get-zaps-\[v2]) for more
    info. - Leverage the `expand` parameter to return additional zap detail such
    as step information. - Use the `zap:all` scope to return all the owned zaps
    on a user's acccount, regardless of paired apps. - Use the
    `include_shared=true` query parameter to return all the owned *and* visible
    zaps on a user's account. (This requires the `zap:account:all` scope which
    otherwise behaves as `zap:all`).

    <Info>
      {" "}

      By default, only zaps that contain the authenticating app and that are
      **owned** by the user are returned. Use of the `zap:account:all` scope is
      required to access shared zaps or zaps the user may have permission to
      view/edit.{" "}
    </Info>
  </Step>

  <Step title="Integrate with your product">
    Shape the zaps returned to match the look and feel of your product,
    showcasing any existing workflows ✨
  </Step>
</Steps>
