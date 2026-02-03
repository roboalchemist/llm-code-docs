# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/examples/team-management.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Team and User Management

> Learn how to use the Vercel SDK through real-life examples.

## Invite a user to a team

In this example, you will find your team id and invite a new member to that team with a specific role.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function inviteTeamMember() {
  try {
    // Invite a new team member
    const availableTeams = (await vercel.teams.getTeams({})).teams;
    const myTeam = availableTeams.filter(
      (team) => team.slug === 'my-team-slug',
    );
    if (myTeam.length > 0) {
      const teamid = myTeam[0].id;
      const inviteResponse = await vercel.teams.inviteUserToTeam({
        teamId: teamid,
        requestBody: {
          email: 'john@example.com',
          role: 'MEMBER',
        },
      });
      console.log(
        `User with role ${inviteResponse.role} invited: ${inviteResponse.username}`,
      );
    }
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

inviteTeamMember();
```
