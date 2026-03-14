# Source: https://pyvis.readthedocs.io/en/latest/documentation.html

Title: Documentation — pyvis 0.1.3.1 documentation

URL Source: https://pyvis.readthedocs.io/en/latest/documentation.html

Markdown Content:
[pyvis](https://pyvis.readthedocs.io/en/latest/index.html)

_class_`pyvis.network.``Network`(_height='600px'_, _width='100%'_, _directed=False_, _notebook=False_, _neighborhood\_highlight=False_, _select\_menu=False_, _filter\_menu=False_, _bgcolor='#ffffff'_, _font\_color=False_, _layout=None_, _heading=''_, _cdn\_resources='local'_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network "Permalink to this definition")
The Network class is the focus of this library. All viz functionality should be implemented off of a Network instance.

To instantiate:

>>> nt = Network()

`add_edge`(_source_, _to_, _**options_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.add_edge)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.add_edge "Permalink to this definition")
Adding edges is done based off of the IDs of the nodes. Order does not matter unless dealing with a directed graph.

>>> nt.add_edge(0, 1) # adds an edge from node ID 0 to node ID
>>> nt.add_edge(0, 1, value = 4) # adds an edge with a width of 4

| Parameters: | * **arrowStrikethrough** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) – When false, the edge stops at the arrow. This can be useful if you have thick lines and you want the arrow to end in a point. Middle arrows are not affected by this. * **from** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")_or_ _num_) – Edges are between two nodes, one to and one from. This is where you define the from node. You have to supply the corresponding node ID. This naturally only applies to individual edges. * **hidden** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) – When true, the edge is not drawn. It is part still part of the physics simulation however! * **physics** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) – When true, the edge is part of the physics simulation. When false, it will not act as a spring. * **title** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")) – The title is shown in a pop-up when the mouse moves over the edge. * **to** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")_or_ _num_) – Edges are between two nodes, one to and one from. This is where you define the to node. You have to supply the corresponding node ID. This naturally only applies to individual edges. * **value** (_num_) – When a value is set, the edges’ width will be scaled using the options in the scaling object defined above. * **width** (_num_) – The width of the edge. If value is set, this is not used. |
| --- |
`add_edges`(_edges_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.add_edges)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.add_edges "Permalink to this definition")
This method serves to add multiple edges between existing nodes in the network instance. Adding of the edges is done based off of the IDs of the nodes. Order does not matter unless dealing with a directed graph.

| Parameters: | **edges** – A list of tuples, each tuple consists of source of edge, edge destination and and optional width. |
| --- |
`add_node`(_n\_id_, _label=None_, _shape='dot'_, _color='#97c2fc'_, _**options_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.add_node)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.add_node "Permalink to this definition")
This method adds a node to the network, given a mandatory node ID. Node labels default to node ids if no label is specified during the call.

>>> nt = Network("500px", "500px")
>>> nt.add_node(0, label="Node 0")
>>> nt.add_node(1, label="Node 1", color = "blue")

| Parameters: | * **n_id** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")_or_[_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – The id of the node. The id is mandatory for nodes and they have to be unique. This should obviously be set per node, not globally. * **label** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")_or_[_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – The label is the piece of text shown in or under the node, depending on the shape. * **borderWidth** (_num_ _(_ _optional_ _)_) – The width of the border of the node. * **borderWidthSelected** (_num_ _(_ _optional_ _)_) – The width of the border of the node when it is selected. When undefined, the borderWidth * 2 is used. * **brokenImage** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")_(_ _optional_ _)_) – When the shape is set to image or circularImage, this option can be an URL to a backup image in case the URL supplied in the image option cannot be resolved. * **group** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")_(_ _optional_ _)_) – When not undefined, the node will belong to the defined group. Styling information of that group will apply to this node. Node specific styling overrides group styling. * **hidden** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")_(_ _optional_ _)_) – When true, the node will not be shown. It will still be part of the physics simulation though! * **image** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")_(_ _optional_ _)_) – When the shape is set to image or circularImage, this option should be the URL to an image. If the image cannot be found, the brokenImage option can be used. * **labelHighlightBold** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")_(_ _optional_ _)_) – Determines whether or not the label becomes bold when the node is selected. * **level** (_num_ _(_ _optional_ _)_) – When using the hierarchical layout, the level determines where the node is going to be positioned. * **mass** (_num_ _(_ _optional_ _)_) – The barnesHut physics model (which is enabled by default) is based on an inverted gravity model. By increasing the mass of a node, you increase it’s repulsion. Values lower than 1 are not recommended. * **physics** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")_(_ _optional_ _)_) – When false, the node is not part of the physics simulation. It will not move except for from manual dragging. * **shape** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")_(_ _optional_ _)_) – The shape defines what the node looks like. There are two types of nodes. One type has the label inside of it and the other type has the label underneath it. The types with the label inside of it are: ellipse, circle, database, box, text. The ones with the label outside of it are: image, circularImage, diamond, dot, star, triangle, triangleDown, square and icon. * **size** (_num_ _(_ _optional_ _)_) – The size is used to determine the size of node shapes that do not have the label inside of them. These shapes are: image, circularImage, diamond, dot, star, triangle, triangleDown, square and icon. * **title** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")_or_ _html element_ _(_ _optional_ _)_) – Title to be displayed when the user hovers over the node. The title can be an HTML element or a string containing plain text or HTML. * **value** (_num_ _(_ _optional_ _)_) – When a value is set, the nodes will be scaled using the options in the scaling object defined above. * **x** (_num_ _(_ _optional_ _)_) – This gives a node an initial x position. When using the hierarchical layout, either the x or y position is set by the layout engine depending on the type of view. The other value remains untouched. When using stabilization, the stabilized position may be different from the initial one. To lock the node to that position use the physics or fixed options. * **y** (_num_ _(_ _optional_ _)_) – This gives a node an initial y position. When using the hierarchical layout,either the x or y position is set by the layout engine depending on the type of view. The other value remains untouched. When using stabilization, the stabilized position may be different from the initial one. To lock the node to that position use the physics or fixed options. |
| --- |
`add_nodes`(_nodes_, _**kwargs_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.add_nodes)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.add_nodes "Permalink to this definition")
This method adds multiple nodes to the network from a list. Default behavior uses values of ‘nodes’ for node ID and node label properties. You can also specify other lists of properties to go along each node.

Example:

>>> g = net.Network()
>>> g.add_nodes([1, 2, 3], size=[2, 4, 6], title=["n1", "n2", "n3"])
>>> g.nodes
>>> [{'id': 1, 'label': 1, 'shape': 'dot', 'size': 2, 'title': 'n1'},

Output:

>>> {'id': 2, 'label': 2, 'shape': 'dot', 'size': 4, 'title': 'n2'},
>>> {'id': 3, 'label': 3, 'shape': 'dot', 'size': 6, 'title': 'n3'}]

| Parameters: | **nodes** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.11)")) – A list of nodes. |
| --- |
`barnes_hut`(_gravity=-80000_, _central\_gravity=0.3_, _spring\_length=250_, _spring\_strength=0.001_, _damping=0.09_, _overlap=0_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.barnes_hut)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.barnes_hut "Permalink to this definition")
BarnesHut is a quadtree based gravity model. It is the fastest. default and recommended solver for non-hierarchical layouts.

| Parameters: | * **gravity** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – The more negative the gravity value is, the stronger the repulsion is. * **central_gravity** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")) – The gravity attractor to pull the entire network to the center. * **spring_length** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – The rest length of the edges * **spring_strength** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")) – The strong the edges springs are * **damping** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")) – A value ranging from 0 to 1 of how much of the velocity from the previous physics simulation iteration carries over to the next iteration. * **overlap** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")) – When larger than 0, the size of the node is taken into account. The distance will be calculated from the radius of the encompassing circle of the node for both the gravity model. Value 1 is maximum overlap avoidance. |
| --- |
`force_atlas_2based`(_gravity=-50_, _central\_gravity=0.01_, _spring\_length=100_, _spring\_strength=0.08_, _damping=0.4_, _overlap=0_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.force_atlas_2based)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.force_atlas_2based "Permalink to this definition")
The forceAtlas2Based solver makes use of some of the equations provided by them and makes use of the barnesHut implementation in vis. The main differences are the central gravity model, which is here distance independent, and the repulsion being linear instead of quadratic. Finally, all node masses have a multiplier based on the amount of connected edges plus one.

| Parameters: | * **gravity** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – The more negative the gravity value is, the stronger the repulsion is. * **central_gravity** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")) – The gravity attractor to pull the entire network to the center. * **spring_length** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – The rest length of the edges * **spring_strength** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")) – The strong the edges springs are * **damping** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")) – A value ranging from 0 to 1 of how much of the velocity from the previous physics simulation iteration carries over to the next iteration. * **overlap** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.11)")) – When larger than 0, the size of the node is taken into account. The distance will be calculated from the radius of the encompassing circle of the node for both the gravity model. Value 1 is maximum overlap avoidance. |
| --- |
`from_DOT`(_dot_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.from_DOT)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.from_DOT "Permalink to this definition")
This method takes the contents of .DOT file and converts it to a PyVis visualization.

Assuming the contents of test.dot contains: digraph sample3 { A -> {B ; C ; D} C -> {B ; A} }

Usage:

>>> nt.Network("500px", "500px")
>>> nt.from_DOT("test.dot")
>>> nt.show("dot.html")

| Parameters: | **dot** (_dot file_) – The path of the dotfile being converted. |
| --- |
`from_nx`(_nx\_graph_, _node\_size\_transf=<function Network.<lambda>>_, _edge\_weight\_transf=<function Network.<lambda>>_, _default\_node\_size=10_, _default\_edge\_weight=1_, _show\_edge\_weights=True_, _edge\_scaling=False_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.from_nx)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.from_nx "Permalink to this definition")
This method takes an exisitng Networkx graph and translates it to a PyVis graph format that can be accepted by the VisJs API in the Jinja2 template. This operation is done in place.

| Parameters: | * **nx_graph** (_networkx.Graph instance_) – The Networkx graph object that is to be translated. * **node_size_transf** (_func_) – function to transform the node size for plotting * **edge_weight_transf** (_func_) – function to transform the edge weight for plotting * **default_node_size** – default node size if not specified * **default_edge_weight** – default edge weight if not specified |
| --- |

>>> nx_graph = nx.cycle_graph(10)
>>> nx_graph.nodes[1]['title'] = 'Number 1'
>>> nx_graph.nodes[1]['group'] = 1
>>> nx_graph.nodes[3]['title'] = 'I belong to a different group!'
>>> nx_graph.nodes[3]['group'] = 10
>>> nx_graph.add_node(20, size=20, title='couple', group=2)
>>> nx_graph.add_node(21, size=15, title='couple', group=2)
>>> nx_graph.add_edge(20, 21, weight=5)
>>> nx_graph.add_node(25, size=25, label='lonely', title='lonely node', group=3)
>>> nt = Network("500px", "500px")
# populates the nodes and edges data structures
>>> nt.from_nx(nx_graph)
>>> nt.show("nx.html")

`generate_html`(_name='index.html'_, _local=True_, _notebook=False_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.generate_html)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.generate_html "Permalink to this definition")
This method gets the data structures supporting the nodes, edges, and options and updates the template to write the HTML holding the visualization. :type name_html: str

`get_adj_list`()[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.get_adj_list)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.get_adj_list "Permalink to this definition")
This method returns the user an adjacency list representation of the network.

| Returns: | dictionary mapping of Node ID to list of Node IDs it |
| --- |

is connected to.

`get_edges`()[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.get_edges)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.get_edges "Permalink to this definition")
This method returns an iterable list of edge objects

| Returns: | list |
| --- |
`get_network_data`()[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.get_network_data)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.get_network_data "Permalink to this definition")
Extract relevant information about this network in order to inject into a Jinja2 template.

Returns:nodes (list), edges (list), height (string), width (string), options (object)
Usage:

>>> nodes, edges, heading, height, width, options = net.get_network_data()

`get_node`(_n\_id_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.get_node)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.get_node "Permalink to this definition")
Lookup node by ID and return it.

| Parameters: | **n_id** – The ID given to the node. |
| --- |
| Returns: | dict containing node properties |
`get_nodes`()[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.get_nodes)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.get_nodes "Permalink to this definition")
This method returns an iterable list of node ids

| Returns: | list |
| --- |
`hrepulsion`(_node\_distance=120_, _central\_gravity=0.0_, _spring\_length=100_, _spring\_strength=0.01_, _damping=0.09_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.hrepulsion)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.hrepulsion "Permalink to this definition")
This model is based on the repulsion solver but the levels are taken into account and the forces are normalized.

| Parameters: | * **node_distance** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – This is the range of influence for the repulsion. * **central_gravity** – The gravity attractor to pull the entire network to the center. * **spring_length** – The rest length of the edges * **spring_strength** – The strong the edges springs are * **damping** – A value ranging from 0 to 1 of how much of the velocity from the previous physics simulation iteration carries over to the next iteration. |
| --- |

:type central_gravity float :type spring_length: int :type spring_strength: float :type damping: float

`inherit_edge_colors`(_status_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.inherit_edge_colors)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.inherit_edge_colors "Permalink to this definition")
Edges take on the color of the node they are coming from.

| Parameters: | **status** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) – True if edges should adopt color coming from. |
| --- |
`neighbors`(_node_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.neighbors)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.neighbors "Permalink to this definition")
Given a node id, return the set of neighbors of this particular node.

| Parameters: | **node** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")_or_[_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – The node to get the neighbors from |
| --- |
| Returns: | set |
`num_edges`()[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.num_edges)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.num_edges "Permalink to this definition")
Return number of edges

| Returns: | [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)") |
| --- |
`num_nodes`()[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.num_nodes)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.num_nodes "Permalink to this definition")
Return number of nodes

| Returns: | [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)") |
| --- |
`prep_notebook`(_custom\_template=False_, _custom\_template\_path=None_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.prep_notebook)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.prep_notebook "Permalink to this definition")
Loads the template data into the template attribute of the network. This should be done in a jupyter notebook environment before showing the network.

Example:

>>> net.prep_notebook()
>>> net.show("nb.html")

| Parameters: | **path** (_string_) – the relative path pointing to a template html file |
| --- |
`repulsion`(_node\_distance=100_, _central\_gravity=0.2_, _spring\_length=200_, _spring\_strength=0.05_, _damping=0.09_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.repulsion)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.repulsion "Permalink to this definition")
Set the physics attribute of the entire network to repulsion. When called, it sets the solver attribute of physics to repulsion.

| Parameters: | * **node_distance** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.11)")) – This is the range of influence for the repulsion. * **central_gravity** – The gravity attractor to pull the entire network to the center. * **spring_length** – The rest length of the edges * **spring_strength** – The strong the edges springs are * **damping** – A value ranging from 0 to 1 of how much of the velocity from the previous physics simulation iteration carries over to the next iteration. |
| --- |

:type central_gravity float :type spring_length: int :type spring_strength: float :type damping: float

`save_graph`(_name_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.save_graph)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.save_graph "Permalink to this definition")
Save the graph as html in the current directory with name.

| Parameters: | **name** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")) – the name of the html file to save as |
| --- |
`set_edge_smooth`(_smooth\_type_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.set_edge_smooth)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.set_edge_smooth "Permalink to this definition")
Sets the smooth.type attribute of the edges.

| Parameters: | **smooth_type** (_string_) – Possible options: ‘dynamic’, ‘continuous’, ‘discrete’, ‘diagonalCross’, ‘straightCross’, ‘horizontal’, ‘vertical’, ‘curvedCW’, ‘curvedCCW’, ‘cubicBezier’. When using dynamic, the edges will have an invisible support node guiding the shape. This node is part of the physics simulation. Default is set to continous. |
| --- |
`set_options`(_options_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.set_options)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.set_options "Permalink to this definition")
Overrides the default options object passed to the VisJS framework. Delegates to the `options.Options.set()` routine.

| Parameters: | **options** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")) – The string representation of the Javascript-like object to be used to override default options. |
| --- |
`set_template`(_path\_to\_template: str_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.set_template)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.set_template "Permalink to this definition")
Path to full template assumes that it exists inside of a template directory. Use set_template_dir to set the relative template path to the template directory along with the directory location itself to change both values otherwise this function will infer the results. :path_to_template path: full os path string value of the template directory

`set_template_dir`(_template\_directory_, _template\_file='template.html'_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.set_template_dir)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.set_template_dir "Permalink to this definition")
Path to template directory along with the location of the template file. :template_directory path: template directory :template_file path: name of the template file that is going to be used to generate the html doc.

`show`(_name_, _local=True_, _notebook=True_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.show)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.show "Permalink to this definition")
Writes a static HTML file and saves it locally before opening.

| Param: | name: the name of the html file to save as |
| --- |
`show_buttons`(_filter\_=None_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.show_buttons)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.show_buttons "Permalink to this definition")
Displays or hides certain widgets to dynamically modify the network.

Usage: >>> g.show_buttons(filter_=[‘nodes’, ‘edges’, ‘physics’])

Or to show all options: >>> g.show_buttons()

| Parameters: | * **status** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) – When set to True, the widgets will be shown. Default is set to False. * **filter** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")_or_ _list:_) – Only include widgets specified by filter_. Valid options: True (gives all widgets) > List of nodes, edges, layout, interaction, manipulation, physics, selection, renderer. |
| --- |
`toggle_drag_nodes`(_status_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.toggle_drag_nodes)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.toggle_drag_nodes "Permalink to this definition")
Toggles the dragging of the nodes in the network.

| Parameters: | **status** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) – When set to True, the nodes can be dragged around in the network. Default is set to True. |
| --- |
`toggle_hide_edges_on_drag`(_status_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.toggle_hide_edges_on_drag)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.toggle_hide_edges_on_drag "Permalink to this definition")
Displays or hides edges while dragging the network. This makes panning of the network easy.

| Parameters: | **status** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) – True if edges should be hidden on drag |
| --- |
`toggle_hide_nodes_on_drag`(_status_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.toggle_hide_nodes_on_drag)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.toggle_hide_nodes_on_drag "Permalink to this definition")
Displays or hides nodes while dragging the network. This makes panning of the network easy.

| Parameters: | **status** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) – When set to True, the nodes will hide on drag. Default is set to False. |
| --- |
`toggle_physics`(_status_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.toggle_physics)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.toggle_physics "Permalink to this definition")
Toggles physics simulation

| Parameters: | **status** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) – When False, nodes are not part of the physics simulation. They will not move except for from manual dragging. Default is set to True. |
| --- |
`toggle_stabilization`(_status_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.toggle_stabilization)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.toggle_stabilization "Permalink to this definition")
Toggles the stablization of the network.

| Parameters: | **status** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.11)")) – Default is set to True. |
| --- |
`write_html`(_name_, _local=True_, _notebook=False_, _open\_browser=False_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/network.html#Network.write_html)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.write_html "Permalink to this definition")
This method gets the data structures supporting the nodes, edges, and options and updates the template to write the HTML holding the visualization.

To work with the old local methods local is being depricated, but not removed. :type name_html: str @param name: name of the file to save the graph as. @param local: Depricated parameter. Used to be used to determine how the graph needs deploy. Has been removed in favor of using the class cdn_resources instead. @param notebook: If true, this object will return the iframe document for use in juptyer notebook. @param open_browser: If true, will open a web browser with the generated graph.

_class_`pyvis.options.``Configure`(_enabled=False_, _filter\_=None_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/options.html#Configure)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.options.Configure "Permalink to this definition")
Handles the HTML part of the canvas and generates an interactive option editor with filtering.

_class_`pyvis.options.``EdgeOptions`[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/options.html#EdgeOptions)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.options.EdgeOptions "Permalink to this definition")
This is where the construction of the edges’ options takes place. So far, the edge smoothness can be switched through this object as well as the edge color’s inheritance.

_class_`Color`[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/options.html#EdgeOptions.Color)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.options.EdgeOptions.Color "Permalink to this definition")
The color object contains the color information of the edge in every situation. When the edge only needs a single color value like ‘rgb(120,32,14)’, ‘#ffffff’ or ‘red’ can be supplied instead of an object.

_class_`Smooth`[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/options.html#EdgeOptions.Smooth)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.options.EdgeOptions.Smooth "Permalink to this definition")
When the edges are made to be smooth, the edges are drawn as a dynamic quadratic bezier curve. The drawing of these curves takes longer than that of the straight curves but it looks better. There is a difference between dynamic smooth curves and static smooth curves. The dynamic smooth curves have an invisible support node that takes part in the physics simulation. If there are a lot of edges, another kind of smooth than dynamic would be better for performance.

`inherit_colors`(_status_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/options.html#EdgeOptions.inherit_colors)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.options.EdgeOptions.inherit_colors "Permalink to this definition")
Whether or not to inherit colors from the source node. If this is set to from then the edge will take the color of the source node. If it is set to to then the color will be that of the destination node.

Note

If set to True then the from behavior is adopted and vice versa.

`toggle_smoothness`(_smooth\_type_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/options.html#EdgeOptions.toggle_smoothness)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.options.EdgeOptions.toggle_smoothness "Permalink to this definition")
Change smooth option for edges. When using dynamic, the edges will have an invisible support node guiding the shape. This node is part of the physics simulation,

| Parameters: | **smooth_type** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")) – Possible options are dynamic, continuous, discrete, diagonalCross, straightCross, horizontal, vertical, curvedCW, curvedCCW, cubicBezier |
| --- |
_class_`pyvis.options.``Interaction`[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/options.html#Interaction)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.options.Interaction "Permalink to this definition")
Used for all user interaction with the network. Handles mouse and touch events as well as the navigation buttons and the popups.

_class_`pyvis.options.``Layout`(_randomSeed=None_, _improvedLayout=True_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/options.html#Layout)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.options.Layout "Permalink to this definition")
Acts as the camera that looks on the canvas. Does the animation, zooming and focusing.

`set_edge_minimization`(_status_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/options.html#Layout.set_edge_minimization)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.options.Layout.set_edge_minimization "Permalink to this definition")
Method for reducing whitespace. Can be used alone or together with block shifting. Enabling block shifting will usually speed up the layout process. Each node will try to move along its free axis to reduce the total length of it’s edges. This is mainly for the initial layout. If you enable physics, they layout will be determined by the physics. This will greatly speed up the stabilization time

`set_separation`(_distance_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/options.html#Layout.set_separation)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.options.Layout.set_separation "Permalink to this definition")
The distance between the different levels.

`set_tree_spacing`(_distance_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/options.html#Layout.set_tree_spacing)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.options.Layout.set_tree_spacing "Permalink to this definition")
Distance between different trees (independent networks). This is only for the initial layout. If you enable physics, the repulsion model will denote the distance between the trees.

_class_`pyvis.options.``Options`(_layout=None_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/options.html#Options)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.options.Options "Permalink to this definition")
Represents the global options of the network. This object consists of indiviual sub-objects that map to VisJS’s modules of:

> *   configure
> *   layout
> *   interaction
> *   physics
> *   edges

The JSON representation of this object is directly passed in to the VisJS framework. In the future this can be expanded to completely mimic the structure VisJS can expect.

`set`(_new\_options_)[[source]](https://pyvis.readthedocs.io/en/latest/_modules/pyvis/options.html#Options.set)[¶](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.options.Options.set "Permalink to this definition")
This method should accept a JSON string and replace its internal options structure with the given argument after parsing it. In practice, this method should be called after using the browser to experiment with different physics and layout options, using the generated JSON options structure that is spit out from the front end to serve as input to this method as a string.

| Parameters: | **new_options** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")) – The JSON like string of the options that will override. |
| --- |
