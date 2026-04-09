rapier3d

# Module pipeline

Source

## Structs§

ActiveEventsFlags that control which physics events are generated for a collider.ActiveHooksFlags that enable custom collision filtering and contact modification callbacks.ChannelEventCollectorA ready-to-use event handler that collects events into channels for later processing.CollisionPipelineA collision detection pipeline that can be used without full physics simulation.ContactModificationContextContext given to custom contact modifiers to modify the contacts seen by the constraints solver.DebugRenderModeFlags indicating what part of the physics engine should be rendered
by the debug-renderer.DebugRenderPipelinePipeline responsible for rendering the state of the physics engine for debugging purpose.DebugRenderStyleStyle used for computing colors when rendering the scene.PairFilterContextContext given to custom collision filters to filter-out collisions.PhysicsPipelineThe main physics simulation engine that runs your physics world forward in time.QueryFilterFiltering rules for spatial queries (raycasts, shape casts, etc.).QueryFilterFlagsFlags for filtering spatial queries by body type or sensor status.QueryPipelineA query system for performing spatial queries on your physics world (raycasts, shape casts, intersections).QueryPipelineMutSame as `QueryPipeline` but holds mutable references to the body and collider sets.

## Enums§

DebugRenderObjectThe object currently being rendered by the debug-renderer.

## Traits§

DebugRenderBackendTrait implemented by graphics backends responsible for rendering the physics scene.EventHandlerA callback interface for receiving physics events (collisions starting/stopping, contact forces).PhysicsHooksUser-defined functions called by the physics engines during one timestep in order to customize its behavior.

## Type Aliases§

DebugColorA color for debug-rendering.
