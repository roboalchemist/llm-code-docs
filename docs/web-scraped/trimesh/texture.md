# Texture¶

Load and display a mesh with UV coordinates and texture images.
    
    
    import trimesh
    
    
    
    mesh = trimesh.load("../models/fuze.obj")
    
    
    
    mesh.show()
    
    
    
    mesh.visual.uv.shape
    
    
    
    (664, 2)