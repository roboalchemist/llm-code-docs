# Source: https://docs.anchorbrowser.io/examples/research-task.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Deep Research

The following example demonstrates how to use Anchor Browser to perform web research tasks.

<CodeGroup>
  ```tsx node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';

  const anchorClient = new Anchorbrowser()
  const session = await anchorClient.sessions.create()
  const sessionId = session.data?.id

  const result = await anchorClient.agent.task(
    `Find the most recent NBA game played by the Milwaukee Bucks
     and provide the result.`,
    {
      taskOptions: {
        url: 'https://nba.com/',
      },
      sessionId: sessionId,
    }
  )
  console.log(result)

  const author = await anchorClient.agent.task(
    `Find an article discussing the game and provide the author's name.`,
    {
      sessionId: sessionId,
    }
  )
  console.log(author)
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser

  anchor_client = Anchorbrowser()
  session = anchor_client.sessions.create()
  session_id = session.data.id

  result = anchor_client.agent.task(
    '''Find the most recent NBA game played by the Milwaukee Bucks
       and provide the result.''',
    task_options={
      'url': 'https://nba.com/',
    },
    session_id=session_id,
  )
  print(result)

  author = anchor_client.agent.task(
    'Find an article discussing the game and provide the author\'s name.',
    session_id=session_id,
  )
  print(author)
  ```
</CodeGroup>
