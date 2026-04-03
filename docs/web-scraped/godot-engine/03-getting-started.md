# Source: https://docs.godotengine.org/en/stable/getting_started/

## Getting Started with Godot Engine

### Installation and Setup

#### Download Godot

1. Visit https://godotengine.org/download
2. Choose your operating system (Windows, macOS, or Linux)
3. Choose between Standard or Mono version:
   - **Standard**: Uses GDScript only
   - **Mono**: Includes C# support
4. Download the executable or archive

#### Installation

**Windows**

- Download the .exe or .zip file
- For .exe: Run the installer and follow prompts
- For .zip: Extract to desired location
- Run godot.exe to launch

**macOS**

- Download the .zip file
- Extract the archive
- Drag Godot.app to Applications folder (optional)
- Run Godot.app

**Linux**

- Download the executable
- Make it executable: `chmod +x godot_engine`
- Run: `./godot_engine`

#### First Launch

When you launch Godot for the first time:

1. Godot displays a project manager window
2. You can create a new project or open an existing one
3. The editor opens with your project

### Your First Project

#### Creating a New Project

1. Click "New Project" in the Project Manager
2. Set project path (where to save the project)
3. Choose rendering backend:
   - **Vulkan**: Modern, high-performance (requires compatible GPU)
   - **OpenGL ES 3.0**: Good compatibility
4. Choose GDScript or C# scripting language
5. Click "Create & Edit"

#### Project Structure

A Godot project contains:

- **project.godot**: Project configuration file
- **scenes/**: Folder for your scene files (.tscn)
- **scripts/**: Folder for your scripts (.gd or .cs)
- **assets/**: Folder for images, audio, models, etc.
- **.godot/**: Hidden folder with engine cache

### Understanding the Editor

#### Main Windows

The Godot editor consists of several key areas:

**Top Menu**

- File: New, Open, Save project
- Edit: Undo, Redo, Preferences
- Scene: Scene-specific operations
- Debug: Debugging tools
- Window: Editor layout options
- Help: Documentation and resources

**Left Panel (Scene Tree)**

- Hierarchical view of all nodes in current scene
- Add/remove nodes
- Change node order (hierarchy)
- Show/hide nodes

**Center (Viewport)**

- Visual editing of your scene
- Move, rotate, scale objects
- Real-time preview of your game

**Right Panel (Inspector)**

- Properties of selected node
- Edit transform (position, rotation, scale)
- Edit node-specific properties
- Assign scripts and resources

**Bottom Panel (Output)**

- Console output from scripts
- Error messages and warnings
- Debugger information
- Search results

#### Customizing the Layout

The editor interface is highly customizable:

- Drag panel borders to resize
- Click the X on panels to hide them
- Use Window menu to show/hide panels
- Save your layout for future sessions
- Multiple layout presets available

### Creating Your First Scene

#### 1. Create a Scene

1. In Scene menu, click "New Scene"
2. A new scene is created with a single Node
3. In Scene tree, right-click "Node" and rename it to "Main"

#### 2. Add Nodes

Click the "+" button in Scene tree to add nodes:

- **Sprite2D**: Displays images (for 2D games)
- **Label**: Displays text
- **Button**: Interactive button
- **Area2D**: 2D area for detection
- **CollisionShape2D**: Defines collision area
- **Marker2D**: Invisible marker/anchor point

#### 3. Configure Nodes

Select a node and modify properties in the Inspector:

- **Transform**: Position (X, Y), Rotation, Scale
- **Modulate**: Color and transparency
- **Texture**: For Sprite2D, choose image file
- **Text**: For Label, enter text

#### 4. Save the Scene

1. Press Ctrl+S (or Cmd+S on macOS)
2. Choose save location (usually scenes/ folder)
3. Give scene a name with .tscn extension
4. Scene is saved and ready to use

### Writing Your First Script

#### Create a Script

1. Select a node in Scene tree
2. In Inspector, look for "Script" property
3. Click the small script icon next to "Script"
4. Click "Create" to create a new script
5. Choose location and click "Save"

#### GDScript Basics

```gdscript
extends Node

# Called when the node enters the scene
func _ready():
    print("Hello from Godot!")

# Called every frame
func _process(delta):
    # delta = time since last frame in seconds
    pass

# Custom function
func my_function():
    print("This is my function")
```

#### C# Basics

```csharp
using Godot;

public class Main : Node
{
    public override void _Ready()
    {
        GD.Print("Hello from Godot!");
    }

    public override void _Process(float delta)
    {
        // delta = time since last frame in seconds
    }
}
```

### Running Your Game

#### Run in Editor

1. Press F5 (or play button in toolbar)
2. Your game runs in the editor viewport
3. Press F8 to pause/resume
4. Press F6 to stop

#### Run Standalone

1. Press Ctrl+Shift+F5 (runs in separate window)
2. Better for testing mobile/web features
3. Useful for performance testing

#### Export

1. Project menu → Export
2. Configure export presets for different platforms
3. Click Export to create distributable builds

### Basic Game Concepts

#### Nodes and Scenes

- **Nodes**: Basic building blocks of Godot games
- **Scene**: Collection of nodes organized hierarchically
- Every game is a tree of nodes
- Scenes can contain other scenes (instances)

#### Signals

Godot uses signals for event-driven programming:

```gdscript
# Emit a signal
signal my_signal
emit_signal("my_signal")

# Connect to a signal
button.pressed.connect(_on_button_pressed)

func _on_button_pressed():
    print("Button was pressed!")
```

#### Input Handling

```gdscript
func _input(event):
    if event is InputEventKey and event.pressed:
        if event.keycode == KEY_SPACE:
            print("Space was pressed")
```

#### Physics

```gdscript
extends RigidBody2D

func _ready():
    # Apply an impulse to the body
    apply_central_impulse(Vector2(100, 0))
```

### Important Classes

#### Node

Base class for all scene elements. Key methods:

- `_ready()`: Called when node enters scene
- `_process(delta)`: Called every frame
- `_input(event)`: Called on input events

#### Node2D

Base class for 2D objects. Adds:

- Position, rotation, scale properties
- `get_global_position()`: World position
- `get_local_position()`: Parent-relative position

#### Control

Base class for UI elements:

- Layout management
- Focus handling
- Theme system
- Signal emission

#### Sprite2D / Sprite3D

Displays images in 2D or 3D space:

- Texture property for image
- Animation support
- Modulation for color/alpha

#### Area2D / Area3D

Detects overlapping objects:

- `area_entered` signal
- `body_entered` signal
- Used for triggers and detection

### Useful Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| F5 | Play scene |
| Ctrl+Shift+F5 | Play standalone |
| F6 | Stop game |
| Ctrl+S | Save scene |
| Ctrl+Z | Undo |
| Ctrl+Y | Redo |
| Ctrl+A | Select all |
| Delete | Delete selected |
| Ctrl+Shift+I | Open import dialog |

### Next Steps

1. **Follow a Tutorial**: Complete the "Your First Game" tutorial
2. **Explore Examples**: Try built-in example projects
3. **Read Documentation**: Deep-dive into topics you're interested in
4. **Join Community**: Connect with other developers
5. **Create Projects**: Start building your own games!

### Helpful Resources

- **Official Website**: https://godotengine.org
- **Documentation**: https://docs.godotengine.org
- **Community Forums**: https://forum.godotengine.org
- **Discord**: https://discord.gg/godotengine
- **YouTube Channel**: https://www.youtube.com/@GodotEngine
- **Social Media**: Twitter (@godotengine), Reddit (/r/godot)
- **Asset Library**: https://godotengine.org/asset-library

### Troubleshooting

#### Editor Won't Open

- Make sure system meets minimum requirements
- Try deleting the .godot folder in your project
- Ensure graphics drivers are up to date

#### Project Won't Run

- Check console for error messages (bottom panel)
- Verify all scripts are saved
- Check that all referenced resources exist

#### Slow Performance

- Profile using Debug → Profiler
- Look for bottlenecks in scripts
- Reduce draw calls (use atlasing, instancing)
- Enable rendering optimizations

---

Congratulations! You're ready to start your Godot journey. Happy game developing!
