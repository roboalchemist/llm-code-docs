# Environment Rules and Customization

**Source:** https://github.com/OpenBMB/AgentVerse

The AgentVerse framework abstracts multi-agent environments into five customizable rule components. This modular design enables flexible environment creation for various scenarios while maintaining code reusability.

## The Five Rule Components

### 1. Describer

**Purpose:** Provides environment description to agents each turn.

**Role:**
- Defines what information agents receive about the environment
- Specifies agent visibility and interaction context
- Generates dynamic descriptions based on environment state

**Configuration:**

```yaml
environment:
  rule:
    describer:
      type: basic  # or custom
```

**Types:**

- **basic**: No custom description (agents receive minimal context)
- **task_describer**: For task-solving scenarios
- **simulation_describer**: For simulation scenarios
- **custom**: User-defined describer

**Example Custom Describer:**

```python
from agentverse.environments.rules import BaseDescriber

class LocationAwareDescriber(BaseDescriber):
    """Describes environment based on agent location."""

    def describe(self, agent, environment):
        """Return description for agent."""
        location = agent.location
        visible_agents = self._get_nearby_agents(agent, environment)

        description = f"""
        Location: {location}
        Nearby agents: {visible_agents}
        Available actions: {self._get_available_actions(location)}
        """
        return description
```

### 2. Order

**Purpose:** Defines the sequence in which agents take actions.

**Role:**
- Controls turn order and action timing
- Determines synchronization of agent actions
- Manages action scheduling

**Configuration:**

```yaml
environment:
  rule:
    order:
      type: sequential  # or random, concurrent
```

**Types:**

- **sequential**: Agents act one at a time in defined order
- **random**: Random agent selection for each turn
- **concurrent**: All agents act simultaneously each turn
- **custom**: User-defined ordering

**Example Configurations:**

Sequential Order:
```yaml
order:
  type: sequential
  agent_sequence: [Professor, Student1, Student2, ...]
```

Random Order:
```yaml
order:
  type: random
  seed: 42  # For reproducibility
```

Concurrent Order:
```yaml
order:
  type: concurrent
```

**Custom Order Example:**

```python
from agentverse.environments.rules import BaseOrder

class PriorityBasedOrder(BaseOrder):
    """Prioritize certain agents based on status."""

    def get_agent_order(self, agents, environment):
        """Return agent order based on priority."""
        # Prioritize urgent agents
        urgent = [a for a in agents if a.status == 'urgent']
        normal = [a for a in agents if a.status != 'urgent']

        return urgent + normal
```

### 3. Selector

**Purpose:** Filters and validates agent-generated messages.

**Role:**
- Accepts or rejects agent outputs
- Validates message format and content
- Implements business logic constraints

**Configuration:**

```yaml
environment:
  rule:
    selector:
      type: basic  # or classroom, custom
```

**Types:**

- **basic**: Accept all messages (no filtering)
- **classroom**: Validates hand-raising and professor calls in classroom
- **custom**: User-defined validation logic

**Example: Classroom Selector**

In a classroom environment:
- Students can only speak after being called on
- Professor can call on any student
- Invalid messages are filtered

**Custom Selector Example:**

```python
from agentverse.environments.rules import BaseSelector

class RoleBasedSelector(BaseSelector):
    """Filter messages based on agent roles and permissions."""

    def select(self, message, agent, environment):
        """Validate message before accepting."""
        # Only allow certain agents to issue commands
        if "command:" in message.lower():
            if agent.role != "admin":
                return False, "Only admins can issue commands"

        # Validate message length
        if len(message) > 5000:
            return False, "Message too long"

        # Check for prohibited content
        if self._contains_prohibited(message):
            return False, "Message contains prohibited content"

        return True, None
```

### 4. Updater

**Purpose:** Updates agent memory with relevant messages.

**Role:**
- Decides which agents receive which messages
- Manages selective information distribution
- Maintains memory consistency

**Configuration:**

```yaml
environment:
  rule:
    updater:
      type: basic  # or location_aware, custom
```

**Types:**

- **basic**: All agents receive all messages
- **location_aware**: Only nearby agents receive messages
- **room_based**: Agents in same room receive messages
- **custom**: User-defined distribution logic

**Example: Location-Aware Updater**

```python
from agentverse.environments.rules import BaseUpdater

class LocationAwareUpdater(BaseUpdater):
    """Update only agents within communication range."""

    def update(self, message, sender, environment):
        """Distribute message to relevant agents."""
        recipients = []

        # Find agents within communication range
        for agent in environment.agents:
            distance = self._calculate_distance(sender, agent)

            if distance <= self.communication_range:
                agent.update_memory(message)
                recipients.append(agent)

        return recipients
```

### 5. Visibility

**Purpose:** Maintains the list of agents each agent can see/interact with.

**Role:**
- Defines agent perception and awareness
- Updates visibility as environment changes
- Controls interaction possibilities

**Configuration:**

```yaml
environment:
  rule:
    visibility:
      type: all  # or location_based, custom
```

**Types:**

- **all**: All agents see all other agents
- **location_based**: Agents only see nearby agents
- **group_based**: Agents see agents in same group
- **custom**: User-defined visibility logic

**Example: Dynamic Visibility**

```python
from agentverse.environments.rules import BaseVisibility

class DynamicVisibility(BaseVisibility):
    """Update visibility as agents move."""

    def get_visible_agents(self, agent, environment):
        """Return list of visible agents for given agent."""
        visible = []

        for other in environment.agents:
            if other == agent:
                continue

            # Check if in same location
            if agent.location == other.location:
                visible.append(other)

            # Check if in adjacent rooms
            elif self._adjacent_locations(agent.location, other.location):
                visible.append(other)

        return visible

    def update_visibility(self, environment):
        """Update visibility for all agents."""
        for agent in environment.agents:
            agent.visible_agents = self.get_visible_agents(agent, environment)
```

## Complete Environment Configuration

A complete environment specification integrating all five components:

```yaml
environment:
  env_type: basic
  max_turns: 30
  rule:
    # Agent action sequence
    order:
      type: sequential

    # Environment description
    describer:
      type: basic

    # Message filtering
    selector:
      type: classroom
      hand_raise_required: true

    # Message distribution
    updater:
      type: basic

    # Agent perception
    visibility:
      type: all

    # Additional parameters shared between components
    rule_params:
      location_threshold: 10  # For location-based logic
      communication_range: 5

agents:
  # Agent definitions...
```

## Environment Customization Strategies

### Strategy 1: Simple Modification

Start with built-in types and override minimal logic:

```python
class SlightlyCustomSelector(BaseSelector):
    """Adds length validation to basic selector."""

    def select(self, message, agent, environment):
        # Add custom validation
        if len(message) > 3000:
            return False, "Message exceeds length limit"
        # Use parent default
        return True, None
```

### Strategy 2: Specialized Environment

Create domain-specific rule components:

**Example: Game Environment**

```python
class GameDescriber(BaseDescriber):
    """Describes game board state."""
    def describe(self, agent, environment):
        board = environment.game_board
        return f"Board state:\n{board}\nYour pieces: {agent.pieces}"

class GameOrder(BaseOrder):
    """Alternates turns between players."""
    def get_agent_order(self, agents, environment):
        # Alternate between red and blue teams
        return sorted(agents, key=lambda a: a.team)

class GameSelector(BaseSelector):
    """Validates legal moves."""
    def select(self, message, agent, environment):
        move = self._parse_move(message)
        return environment.is_legal_move(move, agent)

class GameUpdater(BaseUpdater):
    """Update both players with move."""
    def update(self, message, sender, environment):
        for agent in environment.agents:
            agent.update_memory(f"Opponent: {message}")

class GameVisibility(BaseVisibility):
    """Both players see entire board."""
    def get_visible_agents(self, agent, environment):
        return [a for a in environment.agents if a != agent]
```

### Strategy 3: Component Interaction

Components communicate via `rule_params`:

```python
class SmartDescriber(BaseDescriber):
    def describe(self, agent, environment):
        # Access rule_params set by other components
        urgent_agents = environment.rule_params.get('urgent_agents', [])
        return f"Urgent agents: {urgent_agents}"

class SmartSelector(BaseSelector):
    def select(self, message, agent, environment):
        # Mark urgent agents
        if "urgent" in message:
            environment.rule_params['urgent_agents'] = [agent]
        return True, None

class SmartOrder(BaseOrder):
    def get_agent_order(self, agents, environment):
        # Prioritize agents marked urgent
        urgent = environment.rule_params.get('urgent_agents', [])
        normal = [a for a in agents if a not in urgent]
        return urgent + normal
```

## Best Practices

1. **Start Simple**: Use built-in rule types before creating custom ones
2. **Clear Separation**: Keep logic isolated in single rule component
3. **Testing**: Test each rule component independently
4. **Documentation**: Document custom rules clearly
5. **Performance**: Consider efficiency of rule execution in loops
6. **Flexibility**: Use `rule_params` for inter-component communication
7. **Inheritance**: Extend base classes rather than reimplementing
8. **Logging**: Add logging to rule components for debugging

## Common Patterns

### Multi-Room Environment

```python
class RoomAwareRules:
    """Rules for multi-room environments."""

    describer = RoomAwareDescriber()
    order = SequentialOrder()
    selector = RoleBasedSelector()
    updater = RoomAwareUpdater()
    visibility = RoomAwareVisibility()
```

### Game Environment

```python
class GameRules:
    """Rules for turn-based games."""

    describer = GameDescriber()
    order = TurnBasedOrder()
    selector = GameSelector()
    updater = BroadcastUpdater()
    visibility = FullVisibility()
```

### Hierarchical Organization

```python
class HierarchicalRules:
    """Rules for hierarchical structures (company, military)."""

    describer = HierarchyAwareDescriber()
    order = HierarchyBasedOrder()
    selector = RankBasedSelector()
    updater = HierarchyAwareUpdater()
    visibility = RankAwareVisibility()
```
