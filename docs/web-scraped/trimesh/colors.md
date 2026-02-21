# Colors¶

A simple example of loading and displaying a mesh with face colors.
    
    
    import trimesh
    
    
    
    m = trimesh.load("../models/machinist.XAML", process=False)
    
    
    
    m.visual.kind
    
    
    
    'face'
    
    
    
    m.show()