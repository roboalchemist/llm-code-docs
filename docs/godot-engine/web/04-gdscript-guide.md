# Source: https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/

## GDScript Programming Guide

GDScript is a dynamically-typed, interpreted programming language designed specifically for Godot. It is simple to learn for beginners while powerful enough for complex game logic.

### GDScript Basics

#### Hello World

```gdscript
extends Node

func _ready():
    print("Hello, World!")
```

#### Variables

```gdscript
# Variable declaration without type (dynamic)
var my_variable = 10
var my_string = "Hello"
var my_float = 3.14

# Variable declaration with type hint (optional)
var my_typed_variable: int = 10
var my_typed_string: String = "Hello"

# Multiple assignment
var a, b, c = 1, 2, 3
```

#### Basic Types

```gdscript
# Numbers
var integer: int = 42
var floating_point: float = 3.14
var hexadecimal: int = 0xFF

# Strings
var text: String = "Hello"
var multiline_text: String = """
This is a
multiline string
"""

# Boolean
var is_active: bool = true

# Null value
var nothing = null

# Empty collections
var empty_array: Array = []
var empty_dict: Dictionary = {}
```

#### Arrays and Dictionaries

```gdscript
# Arrays (lists)
var numbers: Array = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.pop_back()
var first = numbers[0]
var length = numbers.size()

# Iterating arrays
for num in numbers:
    print(num)

# Dictionaries (key-value pairs)
var player: Dictionary = {
    "name": "John",
    "level": 5,
    "health": 100
}

# Accessing dictionary values
var player_name = player["name"]
var player_level = player.get("level", 1)  # With default

# Iterating dictionaries
for key in player:
    print(key, ": ", player[key])
```

### Control Flow

#### If Statements

```gdscript
# Simple if
if health <= 0:
    print("Player died")

# If-else
if score > 100:
    print("High score!")
else:
    print("Try again")

# If-elif-else
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")
```

#### Loops

```gdscript
# While loop
var count = 0
while count < 10:
    print(count)
    count += 1

# For loop with range
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# For loop with range step
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

# For-in loop (iterating collections)
var items = ["sword", "shield", "potion"]
for item in items:
    print(item)

# Break and continue
for i in range(10):
    if i == 3:
        continue  # Skip to next iteration
    if i == 7:
        break  # Exit loop
    print(i)
```

#### Switch-Case

```gdscript
var weapon = "sword"

match weapon:
    "sword":
        print("Melee damage: 10")
    "bow":
        print("Ranged damage: 8")
    "wand":
        print("Magic damage: 12")
    _:  # Default case
        print("Unknown weapon")
```

### Functions

#### Function Definition

```gdscript
# Simple function
func greet():
    print("Hello!")

# Function with parameters
func add(a, b):
    return a + b

# Function with type hints
func multiply(a: int, b: int) -> int:
    return a * b

# Function with default parameters
func jump(force: float = 100.0):
    apply_vertical_impulse(force)

# Variable number of arguments
func print_all(args):
    for arg in args:
        print(arg)

# Function with return value
func get_player_name() -> String:
    return "Player"
```

#### Function Calling

```gdscript
greet()
var result = add(5, 3)  # result = 8
var product = multiply(4, 5)  # product = 20
```

### Classes and Inheritance

#### Class Basics

```gdscript
extends Node

# Member variables (properties)
var health: int = 100
var max_health: int = 100

# Called when node enters scene tree
func _ready():
    print("Node is ready!")

# Called every frame
func _process(delta):
    # delta = time elapsed since last frame
    pass

# Custom function
func take_damage(amount: int):
    health -= amount
    if health <= 0:
        die()

func die():
    queue_free()  # Remove node from scene
```

#### Inheritance

```gdscript
# Player script inheriting from Character
extends "Character.gd"

# Override a function from parent class
func _ready():
    super._ready()  # Call parent's _ready
    print("Player initialized")

# Access parent properties/methods
func my_method():
    health = 50  # Parent property
    take_damage(10)  # Parent method
```

### Signals (Events)

#### Defining Signals

```gdscript
extends Node

# Define a signal
signal health_changed(new_health)
signal died

# Emit a signal
func take_damage(amount):
    health -= amount
    emit_signal("health_changed", health)
    
    if health <= 0:
        emit_signal("died")
```

#### Connecting Signals

```gdscript
# In a script managing the player
func _ready():
    # Connect player's health_changed signal
    player.health_changed.connect(_on_player_health_changed)
    player.died.connect(_on_player_died)

# Signal handler functions
func _on_player_health_changed(new_health):
    print("Player health: ", new_health)
    update_health_bar(new_health)

func _on_player_died():
    print("Player died!")
    show_game_over_screen()
```

### Input Handling

```gdscript
func _input(event):
    # Keyboard input
    if event is InputEventKey and event.pressed:
        if event.keycode == KEY_SPACE:
            jump()
    
    # Mouse input
    if event is InputEventMouseButton and event.pressed:
        if event.button_index == MOUSE_BUTTON_LEFT:
            attack(event.position)

# Better way using input map
func _process(delta):
    if Input.is_action_pressed("ui_right"):
        move_right()
    if Input.is_action_just_pressed("ui_accept"):
        jump()
```

### Physics

```gdscript
extends RigidBody2D

func _ready():
    # Set initial velocity
    velocity = Vector2(100, 0)

func _physics_process(delta):
    # Apply gravity
    velocity.y += 9.8 * delta
    
    # Move the body
    velocity = move_and_collide(velocity * delta)

# Apply force
func push(force: Vector2):
    apply_central_impulse(force)
```

### Working with Nodes

#### Finding Nodes

```gdscript
# Get node by path (relative to current node)
var child = get_node("ChildNodeName")
var deep_child = get_node("Parent/Child/DeepChild")

# Get node by unique name (must be set in editor)
var player = get_node_or_null("%Player")

# Get parent
var parent = get_parent()

# Get all children
for child in get_children():
    print(child.name)

# Find nodes by type
var sprites = get_tree().get_nodes_in_group("enemies")
```

#### Creating Nodes Dynamically

```gdscript
# Create a new node
var sprite = Sprite2D.new()
sprite.texture = load("res://player.png")
sprite.position = Vector2(100, 100)

# Add to scene
add_child(sprite)

# Instantiate a scene
var enemy = load("res://enemy.tscn").instantiate()
add_child(enemy)
```

#### Removing Nodes

```gdscript
# Remove this node
queue_free()

# Remove a child
child.queue_free()

# Immediate removal (not recommended)
remove_child(child)
```

### Vectors and Transforms

```gdscript
# Vector2 for 2D
var position: Vector2 = Vector2(100, 50)
var direction: Vector2 = Vector2.RIGHT  # (1, 0)
var up: Vector2 = Vector2.UP  # (0, -1)

# Vector operations
var distance = position.distance_to(other_position)
var normalized_direction = direction.normalized()
var length = direction.length()
var dot_product = direction.dot(other_direction)

# Vector3 for 3D
var position_3d: Vector3 = Vector3(100, 50, 200)

# Transform (position, rotation, scale)
position = Vector2(100, 100)
rotation_degrees = 45
scale = Vector2(2, 2)

# Get global vs local transform
var global_pos = global_position
var local_pos = position
```

### Resource Loading

```gdscript
# Load resources
var texture = load("res://player.png")
var scene = load("res://player.tscn")
var font = load("res://fonts/myfont.tres")

# Use loaded resource
sprite.texture = texture
var player_instance = scene.instantiate()

# Preload (loads at parse time, not runtime)
@onready var my_texture = preload("res://player.png")
```

### Debugging

```gdscript
# Print to console
print("Debug message")
print("Health: ", health)

# Assert (check condition, error if false)
assert(health >= 0, "Health cannot be negative")

# Breakpoint in debugger
breakpoint

# Print call stack
print_stack()

# Print object info
print(self)
```

### Common Patterns

#### Singleton (Autoload)

```gdscript
# In project settings, add script as autoload "GameManager"
extends Node

var score = 0
var level = 1

func add_score(amount: int):
    score += amount
```

#### State Machine

```gdscript
extends Node

enum State { IDLE, RUNNING, JUMPING, FALLING }
var current_state: State = State.IDLE

func _process(delta):
    match current_state:
        State.IDLE:
            idle_state(delta)
        State.RUNNING:
            running_state(delta)
        State.JUMPING:
            jumping_state(delta)

func idle_state(delta):
    if Input.is_action_pressed("ui_right"):
        current_state = State.RUNNING

func running_state(delta):
    # Movement code
    if Input.is_action_just_pressed("ui_accept"):
        current_state = State.JUMPING
```

#### Tween Animation

```gdscript
var tween = create_tween()
tween.tween_property(sprite, "position", Vector2(200, 200), 1.0)
tween.tween_callback(func(): print("Done"))
```

### Performance Tips

1. **Cache node references**: Store frequently accessed nodes instead of calling get_node() repeatedly
2. **Use object pooling**: Reuse instances instead of creating/destroying frequently
3. **Optimize physics**: Use appropriate collision layers and masks
4. **Profile first**: Use the profiler to find actual bottlenecks
5. **Consider C++**: For performance-critical code, use GDExtension

### Useful Built-in Functions

```gdscript
# Math
sqrt(value)
pow(base, exp)
max(a, b)
min(a, b)
randf()  # Random float 0-1
randi_range(from, to)  # Random int

# String operations
str.to_lower()
str.to_upper()
str.split(",")
str.join(array)

# Array operations
array.append(value)
array.pop_back()
array.sort()
array.reverse()

# Type checking
typeof(value)
value is TypeName
```

### Advanced Features

#### Annotations

```gdscript
# Mark virtual method
@virtual
func _ready():
    pass

# Deprecate function
@deprecated
func old_function():
    pass

# Export to editor
@export
var my_export_var: int

@export_range(0, 100)
var slider_value: int
```

#### Type Hints for Performance

```gdscript
# Type hints allow optimizations
var position: Vector2 = Vector2(100, 100)
var health: int = 100

func add_numbers(a: int, b: int) -> int:
    return a + b
```

---

GDScript is powerful and expressive. Start simple and gradually explore advanced features as your projects grow more complex. The best way to learn is by creating games!

For more information, visit: https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/
