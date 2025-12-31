# Source: https://docs.hypermode.com/modus/sdk/go/neo4j.md

# Source: https://docs.hypermode.com/modus/sdk/assemblyscript/neo4j.md

# Source: https://docs.hypermode.com/agents/connections/neo4j.md

# Source: https://docs.hypermode.com/modus/sdk/go/neo4j.md

# Source: https://docs.hypermode.com/modus/sdk/assemblyscript/neo4j.md

# Source: https://docs.hypermode.com/agents/connections/neo4j.md

# Source: https://docs.hypermode.com/modus/sdk/go/neo4j.md

# Source: https://docs.hypermode.com/modus/sdk/assemblyscript/neo4j.md

# Source: https://docs.hypermode.com/agents/connections/neo4j.md

# Source: https://docs.hypermode.com/modus/sdk/go/neo4j.md

# Source: https://docs.hypermode.com/modus/sdk/assemblyscript/neo4j.md

# Source: https://docs.hypermode.com/agents/connections/neo4j.md

# Using Neo4j with Hypermode

> Connect your Hypermode agent to Neo4j for graph database operations

<div className="flex items-center gap-3 mb-6">
  <img src="https://mintcdn.com/hypermode/hdAle6Bocil2pzje/images/agents/connections/icons/neo4j-auradb.png?fit=max&auto=format&n=hdAle6Bocil2pzje&q=85&s=31674687cd456181803911b70b0c732d" alt="Neo4j" width={48} height={48} width="216" height="216" data-path="images/agents/connections/icons/neo4j-auradb.png" srcset="https://mintcdn.com/hypermode/hdAle6Bocil2pzje/images/agents/connections/icons/neo4j-auradb.png?w=280&fit=max&auto=format&n=hdAle6Bocil2pzje&q=85&s=f5727e1a5c998406b06c1dbc58e87736 280w, https://mintcdn.com/hypermode/hdAle6Bocil2pzje/images/agents/connections/icons/neo4j-auradb.png?w=560&fit=max&auto=format&n=hdAle6Bocil2pzje&q=85&s=b27ed567643d13a5cb3b296b10e6df27 560w, https://mintcdn.com/hypermode/hdAle6Bocil2pzje/images/agents/connections/icons/neo4j-auradb.png?w=840&fit=max&auto=format&n=hdAle6Bocil2pzje&q=85&s=2806f9380a915549f38049ab33890659 840w, https://mintcdn.com/hypermode/hdAle6Bocil2pzje/images/agents/connections/icons/neo4j-auradb.png?w=1100&fit=max&auto=format&n=hdAle6Bocil2pzje&q=85&s=a56f1f2bcc85a6d409e75733c2f953f8 1100w, https://mintcdn.com/hypermode/hdAle6Bocil2pzje/images/agents/connections/icons/neo4j-auradb.png?w=1650&fit=max&auto=format&n=hdAle6Bocil2pzje&q=85&s=1fccd89031fd28f1f7b119b3ac031034 1650w, https://mintcdn.com/hypermode/hdAle6Bocil2pzje/images/agents/connections/icons/neo4j-auradb.png?w=2500&fit=max&auto=format&n=hdAle6Bocil2pzje&q=85&s=9ed0ef1366fe0754ec49ebcff4e73f12 2500w" data-optimize="true" data-opv="2" />

  <div>
    <h2 className="text-2xl font-bold m-0">Neo4j</h2>

    <p className="text-gray-600 m-0">
      Graph database platform for connected data
    </p>
  </div>
</div>

## Overview

Neo4j is a powerful graph database that excels at managing highly connected data
and complex relationships. This guide will walk you through connecting your
Hypermode agent to Neo4j.

## Prerequisites

Before connecting Neo4j to Hypermode Agents, you'll need:

1. A Neo4j database instance (free options include
   [Neo4j Sandbox](https://sandbox.neo4j.com) and Neo4j Aura free tier)
2. A [Hypermode Agents](https://agents.hypermode.com) account

<Note>
  This guide will walk you through the steps of connecting to Neo4j using the
  free Neo4j Sandbox, but you can also use Neo4j Aura or a self-hosted instance.
</Note>

## Setting up Neo4j

### Step 1: Create a Neo4j Sandbox

First, navigate to [https://sandbox.neo4j.com/](https://sandbox.neo4j.com/) and create an account. Choose
"Blank Sandbox" from the list of available options.

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/blank-sandbox.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=55aa58413c4ad0e3dc695802790dd806" alt="Create blank sandbox" width="1884" height="1313" data-path="images/connections/neo4j/blank-sandbox.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/blank-sandbox.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=ec810749d6e6c7d12b390f87b23f5c72 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/blank-sandbox.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=e4b1619da8e35f1a333a8f777b5d6026 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/blank-sandbox.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=0893468f04bc5daf9fe40ece48ec9af1 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/blank-sandbox.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=e3c59e3a69c6d4aa43d712e8bd23dcfd 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/blank-sandbox.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=8d8414a289f58d5cadf5ca1f7d3d7aa9 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/blank-sandbox.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=87ba7c39db689e0571c5ccb3919ea1ee 2500w" data-optimize="true" data-opv="2" />

<Note>
  Neo4j Sandbox provides free temporary instances perfect for testing. For
  production use, consider Neo4j Aura or a self-hosted instance.
</Note>

### Step 2: Note your connection details

Once your Neo4j sandbox instance is created (it may take a moment), you can
navigate to the "Connection details" tab to view the connection credentials for
your Neo4j sandbox instance.

Note the username, password, and Bolt URL - you'll use these in the next step to
create a Neo4j connection in Hypermode Agents.
<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/sandbox-credentials.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=3cf2636662c93e0ca4a660cfd94f51b0" alt="Connection details" width="1752" height="962" data-path="images/connections/neo4j/sandbox-credentials.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/sandbox-credentials.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=a36502208476d4bddbc539c5f3351d5e 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/sandbox-credentials.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=5bf719d691ef8b0d7f5c3ff0a22193e9 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/sandbox-credentials.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=b6463938fd1b17bd58bd73fa519347a6 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/sandbox-credentials.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=1082bf46e8b6701c7343291db11e70e0 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/sandbox-credentials.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=e33842ee93e2b04e7356684d4fbf925c 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/sandbox-credentials.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=8136e4c6314959eb9c07f8ea4bf7d5c3 2500w" data-optimize="true" data-opv="2" />

## Creating your Neo4j agent

### Step 1: Create a new agent

From the Hypermode Agents dashboard, create a new agent:

1. Select the "Create agent" button
2. Describe your agent in a few sentences, we'll use "The agent is a Neo4j
   expert"

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/create-agent-modal.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=89c927df4da38db073fb5f32fe3ae543" alt="Create agent modal" width="1562" height="1148" data-path="images/connections/neo4j/create-agent-modal.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/create-agent-modal.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=861cbef799e6a45a6519ac00340dfee3 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/create-agent-modal.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=1199fae297ec0732093c2d6361d8c841 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/create-agent-modal.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=ae750aa639334452e34dc03baf7a3ff2 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/create-agent-modal.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=a4f6f12d1868d12fe79f2f4094acdf7a 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/create-agent-modal.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=5f86822f480056174b90da9f4ee2d191 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/create-agent-modal.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=865f5141153baaa610e741d55181ac1c 2500w" data-optimize="true" data-opv="2" />

### Step 3: View your agent profile

Once created, navigate to your agent's details page. Here you can view and edit
the agent instructions that were created from your initial agent description
preceding the agent creation process.

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/agent-profile.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=47240b0fb7563a10488c361d4342920c" alt="Agent profile" width="2360" height="2616" data-path="images/connections/neo4j/agent-profile.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/agent-profile.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=ac323d9f281ba37b755b6bfbb7d3c244 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/agent-profile.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=76c284ee8790f2f7e034603e88edbb16 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/agent-profile.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=3e139c508356981d024629947e5b265d 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/agent-profile.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=831f3bdadac632b312b146bb5af04d04 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/agent-profile.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=88a0c6bc4ea01f4f64f44403775bd3f4 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/agent-profile.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=82c3feff753b1011a64162ea1874f327 2500w" data-optimize="true" data-opv="2" />

You can update the agent instructions at any time to help align the agent's
background and skills with your use case.

## Connecting to Neo4j

### Step 1: Add the Neo4j connection

Navigate to the **Connections** tab in Hypermode Agents and add Neo4j:

1. Click "Add connection"
2. Select the "Connect" button next to Neo4j in the list of available
   connections

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/add-neo4j-connection.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=9a32fd24452b5998458dd6e42a66bb11" alt="Add Neo4j connection" width="2400" height="1294" data-path="images/connections/neo4j/add-neo4j-connection.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/add-neo4j-connection.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=1e1e316f735b2b6838ce31ff0973671b 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/add-neo4j-connection.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=b98a35cf87c099a1075a45358116477d 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/add-neo4j-connection.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=d2b4ed05c25f0208160a3348d4506456 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/add-neo4j-connection.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=ca27d27b19d51f28eb2799a25c982e16 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/add-neo4j-connection.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=4f605bbae5c69ff280d4452e04f2ae70 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/add-neo4j-connection.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=e355232c5cf85b58c977cdc5f48c2a9e 2500w" data-optimize="true" data-opv="2" />

### Step 2: Configure credentials

Enter your Neo4j credentials from the Neo4j Sandbox details page.

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/neo4j-connection-modal.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=9b3b4a6fb3a1e0be955028b85a4d0957" alt="Neo4j connection modal" width="1324" height="826" data-path="images/connections/neo4j/neo4j-connection-modal.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/neo4j-connection-modal.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=bd034d9d8914ef4f8833fc912f03bf1c 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/neo4j-connection-modal.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=c3e48ba3285921a07cff9be5ffabe166 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/neo4j-connection-modal.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=abe6f9d7cdd2eec5730429c623e24be5 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/neo4j-connection-modal.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=68b8d90dcdc5f4662e350ae41a6385d4 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/neo4j-connection-modal.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=bc301c64d32f47a51790783b01f858ed 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/neo4j-connection-modal.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=8d4f3b21274b8f8660aa38e3c9cf1826 2500w" data-optimize="true" data-opv="2" />

<Warning>Ensure you're using the Bolt URL endpoint format.</Warning>

## Understanding Neo4j's schemaless nature

Unlike traditional databases, Neo4j doesn't require you to define schemas
upfront. This means:

* **Flexible node creation**: Add nodes with any labels and properties on the
  fly
* **Dynamic relationships**: Create relationships of any type between nodes
* **Evolving data models**: Your graph structure can grow and change organically
* **No migrations needed**: Add new node types or properties without schema
  updates

This flexibility makes Neo4j perfect for:

* Exploratory data analysis
* Rapidly evolving data models
* Complex, heterogeneous datasets
* Real-world relationship modeling

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/what-data.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=8e2ba0b3cdb847ff17600de4db01366d" alt="Neo4j Graph Model" width="2174" height="1358" data-path="images/connections/neo4j/what-data.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/what-data.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=c65719949410816cf284ec7b3e7b1859 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/what-data.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=61ec9c9a089d586f1e7dfcef2e3c894d 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/what-data.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=1e6ac8796c763361d76315d9e28f6721 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/what-data.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=ce1d2fbee6e96c95b65717c135adb71b 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/what-data.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=8f22e4b437624ba25293012179b8804a 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/what-data.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=3d5c3f07083d0df56201e826de9fcb48 2500w" data-optimize="true" data-opv="2" />

## Example graph model

Here's a simple example of how nodes and relationships work in Neo4j:

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/model.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=2f183fb83847a14f06366906e2304dd6" alt="Neo4j Graph Model" width="2672" height="1552" data-path="images/connections/neo4j/model.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/model.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=9e8fa503ad28617f9a1347d55cde777b 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/model.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=2d447d1a815df6b1423daeb3da5b39a4 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/model.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=5d67415076f44dd1f72cc8bf487d6dd7 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/model.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=fa262996bd6f87fe862ae35dac684007 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/model.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=c3a04cf28fab16aad233dee874bd061c 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/model.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=5dde9246e660e59253e644d741e524f7 2500w" data-optimize="true" data-opv="2" />

This model shows:

* **Nodes**: Person, Company, and Product (represented as circles)
* **Relationships**: WORKS\_AT, MAKER\_OF, BY\_COMPANY (represented as arrows)
* Each node can have properties (like name, age, price)
* Relationships can also have properties (like since, role)

## Testing the connection

### Test 1: Create your first nodes

Start a new thread with your agent and create some nodes dynamically:

```text
Create nodes for this scenario:
- A Person named "Alice" who is 28 years old
- A Company named "TechCorp" founded in 2020
- A Product named "GraphApp" with a price of $99
```

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/create-nodes-result.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=06365ba5a8bdc2d3c1837c269d842b48" alt="Create nodes result" width="1352" height="1070" data-path="images/connections/neo4j/create-nodes-result.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/create-nodes-result.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=77c33776882178356545b797dffa67bf 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/create-nodes-result.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=d933609b1fe1c25c140f0b47ec5c7efd 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/create-nodes-result.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=2c5f9ad05b3b8d0f09f0ef51e56a76a4 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/create-nodes-result.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=c3a7994cbc22f2831c98fb5505f910c2 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/create-nodes-result.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=2ba8df9c04e94c9d25eea766abb3f58c 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/create-nodes-result.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=8d5ad750800c11e8f84fa4940b052fe0 2500w" data-optimize="true" data-opv="2" />

### Test 2: Create relationships

Now connect your nodes based on our model:

```text
Create these relationships:
- Alice WORKS_AT TechCorp (since 2021)
- Alice is MAKER_OF GraphApp
- GraphApp is BY_COMPANY TechCorp
```

### Test 3: Visualize in Neo4j Browser

After your agent creates the data, switch to Neo4j Browser to see the results:

1. **Click the "Open" button** in your Neo4j Sandbox
2. **Run the visualization query**:

```cypher
   MATCH (n) RETURN n
```

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/neo4j-browser-graph-view.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=f59234f5aa962fa2c9b197f1c1e837d5" alt="graph in browser" width="2352" height="1098" data-path="images/connections/neo4j/neo4j-browser-graph-view.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/neo4j-browser-graph-view.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=f0424c1237987492335ed8b94879b7ab 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/neo4j-browser-graph-view.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=445fc1a2989f0f11dae9d50211c0b20c 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/neo4j-browser-graph-view.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=22813c163c330e8d796aa4d4a4796c65 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/neo4j-browser-graph-view.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=a5158d8dabdfcf1a628af49a08a90625 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/neo4j-browser-graph-view.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=e499a58df322cb0e8431eba148d1b80e 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/neo4j-browser-graph-view.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=5e9a70ce82e05af27a50472d1324d668 2500w" data-optimize="true" data-opv="2" />

### Test 4: Query your graph

Back in your agent thread, use Cypher to explore your data:

```text
Run a Cypher query to find all products made by people who work at TechCorp, showing the full relationship path.
```

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/query-your-graph.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=4160d0c96e2022de472cbb2fc530dea7" alt="Query result" width="1934" height="866" data-path="images/connections/neo4j/query-your-graph.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/query-your-graph.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=8146e044d2f814537a98103e0556a38a 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/query-your-graph.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=ddf64da487249c70d333533b12b76956 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/query-your-graph.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=fb2d5fa82d3a98afbec2363bf0896f5e 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/query-your-graph.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=c55375338a12aff5689b6efc5b3998b8 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/query-your-graph.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=5c3ff926a8c5a5c24a807c145206fb0c 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/query-your-graph.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=69a8e0231859956fdc41580483dc0848 2500w" data-optimize="true" data-opv="2" />

## Example: Building a dynamic knowledge graph

Here's how to leverage Neo4j's schemaless nature to build a flexible knowledge
graph:

```text
Let's expand our graph with more data:
1. Add another Person "Bob" who also works at TechCorp
2. Add a new Company "StartupInc"
3. Add Products "DataTool" and "AIAssistant"
4. Create relationships showing Bob made DataTool, and StartupInc made AIAssistant
5. Add a COMPETES_WITH relationship between the two companies
```

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/dynamic-graph-query-agent.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=e4c12dfabc61fb37d17cc68ffc128a0e" alt="Graph with more data" width="1650" height="914" data-path="images/connections/neo4j/dynamic-graph-query-agent.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/dynamic-graph-query-agent.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=80afa0f634dc0d688c5615cf1a3cd688 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/dynamic-graph-query-agent.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=85c79b9fa8255131640577e60b62e766 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/dynamic-graph-query-agent.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=ded3ff7464fa36f90a852d7cb5ffd7d8 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/dynamic-graph-query-agent.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=18f8510e0a4c833ed5fd231ebbe3d858 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/dynamic-graph-query-agent.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=4663372377fe48cdb4c6ab7ef987c5f2 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/dynamic-graph-query-agent.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=33165fbdea910d9f2e66e37eee6a95b4 2500w" data-optimize="true" data-opv="2" />

Your agent can dynamically add:

* New node types as you discover them
* Properties specific to each entity
* Relationships that make sense in context
* No need to predefine any structure!

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/dynamic-graph-query-results.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=b6eaa3e6c92e9073a8f2db7e27732a6c" alt="Graph with more data" width="2376" height="1098" data-path="images/connections/neo4j/dynamic-graph-query-results.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/dynamic-graph-query-results.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=399c35c35c8929572d0d4ab8e1bfb87b 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/dynamic-graph-query-results.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=71bde552eaf7b734229baae50be1d2fd 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/dynamic-graph-query-results.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=ba61604fd44a8f52377f3c0aa5806bf0 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/dynamic-graph-query-results.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=078d8fc8b5bb3f81feecb4f37ca532bc 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/dynamic-graph-query-results.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=03c3d2e85d9b155465142cd5b4d243f8 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/neo4j/dynamic-graph-query-results.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=8954e592287bd67168e36f995d317c66 2500w" data-optimize="true" data-opv="2" />

## What you can do

With your Neo4j connection and its three core tools, your agent can:

* **Create Node**: Dynamically add entities with any labels and properties
* **Create Relationship**: Connect nodes with typed relationships and properties
* **Run Cypher Query**: Perform complex graph operations including:
  * Pattern matching and traversal
  * Aggregations and analytics
  * Graph algorithms
  * Data updates and deletions
  * Schema-free exploration

## Troubleshooting

### Common issues

#### Connection refused error

* Check if your sandbox is still active (they expire after 3 days)
* Ensure the URL includes the correct port (usually 7474)

#### Authentication failed

* Confirm username and password are correct
* Sandbox passwords are auto-generated - copy carefully
* Try resetting the password in the sandbox console

## Learn more

* [Neo4j Documentation](https://neo4j.com/docs/)
* [Cypher Query Language](https://neo4j.com/docs/cypher-manual/current/)
* [Tutorial: Using Hypermode Agents to extract and build knowledge graphs](/agents/knowledge-graph-extraction)
