# Source: https://docs.hypermode.com/agents/connections/supabase.md

# Using Supabase with Hypermode

> Connect your Hypermode agent to Supabase for real-time database operations

<div className="flex items-center gap-3 mb-6">
  <img src="https://mintcdn.com/hypermode/168JkHD55lMGo3-U/images/agents/connections/icons/supabase.svg?fit=max&auto=format&n=168JkHD55lMGo3-U&q=85&s=8b4b996ced58875847d79eece6689329" alt="Supabase" width={48} height={48} width="375" height="375" data-path="images/agents/connections/icons/supabase.svg" srcset="https://mintcdn.com/hypermode/168JkHD55lMGo3-U/images/agents/connections/icons/supabase.svg?w=280&fit=max&auto=format&n=168JkHD55lMGo3-U&q=85&s=1c5467e102cd96211d81282a089b7d1d 280w, https://mintcdn.com/hypermode/168JkHD55lMGo3-U/images/agents/connections/icons/supabase.svg?w=560&fit=max&auto=format&n=168JkHD55lMGo3-U&q=85&s=4eee194a571802185acf8bad5ada9929 560w, https://mintcdn.com/hypermode/168JkHD55lMGo3-U/images/agents/connections/icons/supabase.svg?w=840&fit=max&auto=format&n=168JkHD55lMGo3-U&q=85&s=62f36e19dd47c465b3e02abf7442a2ca 840w, https://mintcdn.com/hypermode/168JkHD55lMGo3-U/images/agents/connections/icons/supabase.svg?w=1100&fit=max&auto=format&n=168JkHD55lMGo3-U&q=85&s=62b3f0dbeb89e764656964f38ea0253b 1100w, https://mintcdn.com/hypermode/168JkHD55lMGo3-U/images/agents/connections/icons/supabase.svg?w=1650&fit=max&auto=format&n=168JkHD55lMGo3-U&q=85&s=0ab1b6a753b229c9f78003d5811207d3 1650w, https://mintcdn.com/hypermode/168JkHD55lMGo3-U/images/agents/connections/icons/supabase.svg?w=2500&fit=max&auto=format&n=168JkHD55lMGo3-U&q=85&s=f7f3752aee785880944b012b479b2a10 2500w" data-optimize="true" data-opv="2" />

  <div>
    <h2 className="text-2xl font-bold m-0">Supabase</h2>

    <p className="text-gray-600 m-0">
      Open source PostgreSQL development platform
    </p>
  </div>
</div>

## Overview

Supabase is an open source alternative to Firebase that provides a complete
backend solution with PostgreSQL at its core. This guide will walk you through
connecting your Hypermode agent to Supabase, enabling powerful database
operations and real-time interactions.

## Prerequisites

Before connecting Supabase to Hypermode, you'll need:

1. A [Supabase account](https://supabase.com/)
2. A Supabase project with API credentials
3. A [Hypermode workspace](https://hypermode.com/)

## Setting up Supabase

### Step 1: Create your Supabase account

If you haven't already, sign up for a free Supabase account.

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/signup-supabase.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=f90a1dd2a1aad6112b853fc180cfbd11" alt="Supabase signup" width="2806" height="1968" data-path="images/connections/supabase/signup-supabase.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/signup-supabase.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=013da685bf104a1245a76f0923c7ee94 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/signup-supabase.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=bd00387c819ee678c3751551583203de 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/signup-supabase.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=d5a619b23faac359c78f722b7d67e9e8 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/signup-supabase.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=b4bb508ae2b7d76b88167a683e2cb614 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/signup-supabase.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=0fa449584714d9146c154ccc504ce430 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/signup-supabase.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=f2c1a0c98c89474578d1005525a052e5 2500w" data-optimize="true" data-opv="2" />

### Step 2: Generate API credentials

Navigate to your project settings and create a new API key:

1. Go to **Settings** → **API** in your Supabase dashboard
2. Create a new service role key (this bypasses Row Level Security)
3. Copy your project URL to extract the subdomain ID

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/create-key.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=290027ec4c2266da2e03d8c0f8c4c66d" alt="Create API key" width="2542" height="1948" data-path="images/connections/supabase/create-key.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/create-key.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=4a06ddfc426932705754cc2d21e5fc7c 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/create-key.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=05317ac489bab6e73a305775f973986f 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/create-key.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=0e8e1d2b933f26ebee3fa30d58db3255 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/create-key.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=3c86118e7a31f77973f3f33bf5c63bec 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/create-key.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=a4dac4930e32686eb3d8f90f658af4e7 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/create-key.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=b8c24b39faf977206f0a36fbb2462f57 2500w" data-optimize="true" data-opv="2" />

<Note>
  The subdomain ID is the part before `.supabase.co` in the project URL. For
  example, if the URL is `https://supa-project-id.supabase.co`, then the
  subdomain ID is `supa-project-id`.
</Note>

## Creating your Supabase agent

### Step 1: Create a new agent

From the Hypermode interface, create a new agent manually:

1. Click the agent dropdown menu
2. Select "Create new Agent"

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/navigate-create-agent.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=2260ab4551efec9748f95c6c54903582" alt="Navigate to create agent" width="2542" height="1948" data-path="images/connections/supabase/navigate-create-agent.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/navigate-create-agent.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=68b8b25141ed6caeb07511167a84004c 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/navigate-create-agent.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=fe775f60655cb2f2b90700ee5d186040 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/navigate-create-agent.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=5c772891fac1d91dd91eafc800ec2a9f 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/navigate-create-agent.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=ad869d30c432ef02b8cbfc2cc4773cf5 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/navigate-create-agent.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=29564178887d880ae66d7be1040a369b 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/navigate-create-agent.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=75b6913940510d314e101cb24cfc6716 2500w" data-optimize="true" data-opv="2" />

### Step 2: Configure agent settings

Use these recommended settings for your Supabase agent:

* **Agent Name**: SupaAgent
* **Agent Title**: Connects to Supabase
* **Description**: SupaAgent issues queries
* **Instructions**: You have a connection to Supabase and various other
  developer tools to streamline data access and awareness
* **Model**: GPT-4.1

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/create-agent-modal.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=a329ce0c8623830ac58663bf1d589828" alt="Create agent modal" width="2542" height="1948" data-path="images/connections/supabase/create-agent-modal.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/create-agent-modal.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=fbb222de666dab8b10b8fe89e341f21b 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/create-agent-modal.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=919a915a1bb7ac6ae47f26e435efec8c 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/create-agent-modal.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=1217435fd6a8b383ab8cf690fc95d554 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/create-agent-modal.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=47acedcbf271a740b042ef7a9795b80b 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/create-agent-modal.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=92f00e74a29fc4a4e3126c4c77b03a73 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/create-agent-modal.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=a684b7bcc8e101e4dfe6976f9d543ba6 2500w" data-optimize="true" data-opv="2" />

### Step 3: View your agent profile

Once created, navigate to your agent's settings page to see the profile:

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/agent-profile.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=321fc06172ef8f70aa07fcb88829339a" alt="Agent profile" width="2512" height="1946" data-path="images/connections/supabase/agent-profile.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/agent-profile.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=b92b9183292ea6ad4d60cd7aab8ccc82 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/agent-profile.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=79e4b0e5f0caab5834ec2e676c1cf0e9 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/agent-profile.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=0f606053b88cc361cd3d5e9df98baaf5 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/agent-profile.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=8bfcb31d6821e1523dce5c79bb58e501 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/agent-profile.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=598a3fdd0f17744e4089ebc36c8681ba 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/agent-profile.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=c4bbc2355c4a579eddd9f7a64dc62cb0 2500w" data-optimize="true" data-opv="2" />

## Connecting to Supabase

### Step 1: Add the Supabase connection

Navigate to the **Connections** tab and add Supabase:

1. Click "Add connection"
2. Select "Supabase" from the dropdown

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/add-supabase-connection.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=344db75531bd01d7d5dc7759db30b9b8" alt="Add Supabase connection" width="1886" height="1172" data-path="images/connections/supabase/add-supabase-connection.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/add-supabase-connection.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=79a990d742f9f1ada25239747fbd6293 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/add-supabase-connection.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=78d592173453a850493bf80440153b4d 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/add-supabase-connection.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=64253bb1a3d22d0d12aa1f7038c589f1 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/add-supabase-connection.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=72f9e97e10c365a0158b54bf58f82277 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/add-supabase-connection.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=23a87e4456c250c51b6b4b6aeabfa564 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/add-supabase-connection.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=c7138504fe4109ceb1fd8fa66cb63505 2500w" data-optimize="true" data-opv="2" />

### Step 2: Configure credentials

Enter your Supabase credentials:

* **Subdomain ID**: Your project reference `supa-project-id`
* **Service Key**: Your service role key from Supabase

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/supabase-connection-modal.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=99f792ae5723f44b44dc7f1ea5611516" alt="Supabase connection modal" width="1886" height="1554" data-path="images/connections/supabase/supabase-connection-modal.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/supabase-connection-modal.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=aa930cf959cccc7f18d345f699d4559c 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/supabase-connection-modal.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=089de972953db9a5cf32b680ff10cffa 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/supabase-connection-modal.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=6331d60bd55817ac6be0bfb12f56ae67 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/supabase-connection-modal.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=aaebc407cbec31c01cf0097b5c290f4e 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/supabase-connection-modal.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=9d0f36a00fbfdca2caf555daaea6b632 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/supabase-connection-modal.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=46cadf669234df1e2397048883a31cde 2500w" data-optimize="true" data-opv="2" />

<Warning>
  Keep your service key secure! This key bypasses Row Level Security and should
  never be exposed in client-side code.
</Warning>

## Setting up your database

<Note>
  The Supabase connector allows you to query and manipulate data but doesn't
  modify schemas. You'll need to create your database schema directly in
  Supabase.
</Note>

### Step 1: Create your schema

Navigate to the SQL editor in your Supabase dashboard and run this example
schema:

```sql
-- 1. Movies Table
CREATE TABLE IF NOT EXISTS public."Movies" (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    year INTEGER
);

-- 2. Actors Table
CREATE TABLE IF NOT EXISTS public."Actors" (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- 3. MovieActors Join Table
CREATE TABLE IF NOT EXISTS public."MovieActors" (
    movie_id INTEGER NOT NULL REFERENCES public."Movies"(id) ON DELETE CASCADE,
    actor_id INTEGER NOT NULL REFERENCES public."Actors"(id) ON DELETE CASCADE,
    PRIMARY KEY (movie_id, actor_id)
);
```

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/migrate.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=2febe872d46352da14528ee801735bcd" alt="Migrate database" width="2236" height="1236" data-path="images/connections/supabase/migrate.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/migrate.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=1cc715f043c9fb0964f0ba5823405224 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/migrate.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=a816aa53ce0e29148353b24705d73867 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/migrate.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=0c9d567a510f5dde5915729f085dce5e 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/migrate.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=30a1dcd0d1897c6a689de9b13377ba10 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/migrate.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=8c1f59ae14805d26b5942499e5d1c396 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/migrate.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=ac4ef94e1e5747b0e978b79bd5283715 2500w" data-optimize="true" data-opv="2" />

### Step 2: View your schema

Confirm your tables are created successfully:

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/supabase-schema.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=e4c9f02e30ac20d7095906afdf04e0bc" alt="Database schema" width="1636" height="1742" data-path="images/connections/supabase/supabase-schema.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/supabase-schema.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=a3c31d17ec517d69cedbeb9287b94d51 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/supabase-schema.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=6446e7c5dbcd05fc4fbf9ae7d28959e2 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/supabase-schema.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=9a3430334f030481a42d6784d82df16e 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/supabase-schema.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=47d9d8a10029d8806cf25cfbcca72fcc 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/supabase-schema.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=38a7cd31278ef19e4cabf1fb6accc4bd 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/supabase-schema.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=b0e7ed4ab637bf1f5a4d7051badaef4d 2500w" data-optimize="true" data-opv="2" />

### Step 3: Update agent instructions

For your agent to understand your database structure, update its instructions
with your schema information:

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/agent-update-prompt.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=782b0648047fc76af45daef99938c7cc" alt="Update agent prompt" width="2236" height="1942" data-path="images/connections/supabase/agent-update-prompt.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/agent-update-prompt.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=277f7d6753cfa370e171639a43069b1a 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/agent-update-prompt.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=051780469b139a5fd3775e8c762a1ea1 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/agent-update-prompt.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=fbed28e8202eb91f8e00791c27fe4a7a 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/agent-update-prompt.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=3e9aa5d6cbe64e85d4d402986d28a39c 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/agent-update-prompt.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=7ea099a6f23cef7b993aee8b7dffb4be 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/agent-update-prompt.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=baa91f4d78536845f723f5b43b7afbc2 2500w" data-optimize="true" data-opv="2" />

## Testing the connection

### Test 1: Query empty tables

Start a new thread and test with a simple query:

```text
Can you list the movies?
```

You should see a Supabase tool call in the chat history, confirming the
connection works:

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/empty-movies.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=a9a895f0e14884f33c2a6c5feb20f6c8" alt="Empty movies query" width="2230" height="1942" data-path="images/connections/supabase/empty-movies.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/empty-movies.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=392da6772ff72425a613786f91d4c27d 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/empty-movies.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=1da278596c7f6f1f66748248cc991032 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/empty-movies.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=05b11d5fd9e4cd669678292879cfbd49 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/empty-movies.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=fb642f594ef6e289909e12a7da0ed11b 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/empty-movies.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=83af3cbe3fed06021a4003cdadbe0ef6 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/empty-movies.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=6b850e234b3a4574f124100b2059c827 2500w" data-optimize="true" data-opv="2" />

### Test 2: Insert data

Now try adding data to your database:

```text
Can you add The Matrix 1999 and Neo the actor into my Supabase database?
```

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/add-matrix.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=766e57eb0c707d5abb89c81bb9b743d6" alt="Add Matrix movie" width="2512" height="1946" data-path="images/connections/supabase/add-matrix.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/add-matrix.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=b3ebb75ce854218e4dda2a8bdc739260 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/add-matrix.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=048b432360610389ececf6e13112ed75 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/add-matrix.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=5d2a2527ab61876601fe374ea920d6c7 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/add-matrix.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=519edf09c4157807cd7bf3c4d49e4f51 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/add-matrix.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=7eb8f354391239b52d0ecb1bbfd6fa9d 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/supabase/add-matrix.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=63dc55f700b6abf2bb7b7f96654e0b24 2500w" data-optimize="true" data-opv="2" />

## What you can do

With your Supabase connection established, your agent can:

* **Query data** with complex filters and joins
* **Insert, update, and delete** records
* **Execute transactions** for data consistency
* **Work with relationships** between tables
* **Integrate with other tools** like GitHub, Slack, and Stripe

## Best practices

1. **Schema documentation**: Keep your agent's instructions updated with your
   current schema
2. **Security**: Use Row Level Security policies for additional protection
3. **Performance**: Create indexes for frequently queried columns
4. **Error handling**: Your agent will handle common database errors gracefully

## Learn more

* [Supabase Documentation](https://supabase.com/docs)
* [MCP Supabase Connector](https://mcp.pipedream.com/app/supabase)
* [PostgreSQL Best Practices](https://www.postgresql.org/docs/current/index.html)

<Tip>
  Combine Supabase with other Hypermode connections to build powerful workflows.
  For example, use GitHub to track code changes that affect your database, or
  Slack to notify your team of important data updates.
</Tip>
