# Source: https://docs.inkeep.com/api-reference

# Inkeep API (/api-reference)

Explore the Inkeep Agents API endpoints for managing, running, and evaluating agents.



import { source } from '@/lib/source';

<Cards>
  {source
      .getPages()
      .filter((item) => item.url.startsWith('/api-reference/'))
      .map((item) => (
        <Card
          key={item.url}
          title={item.data.title}
          href={item.url}
          icon={item.data.icon}
        >
          {item.data.description}
        </Card>
      ))}
</Cards>

***
