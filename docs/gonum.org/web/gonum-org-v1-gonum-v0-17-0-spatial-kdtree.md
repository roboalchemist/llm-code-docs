# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree

Title: kdtree package - gonum.org/v1/gonum/spatial/kdtree - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree

Markdown Content:
Package kdtree implements a k-d tree.

See [https://en.wikipedia.org/wiki/K-d_tree](https://en.wikipedia.org/wiki/K-d_tree) for more details of k-d tree functionality.

Output:

 Stations within 750 m of 51.501476N 0.140634W. St. James's Park: 0.545 km Green Park: 0.600 km Victoria: 0.621 km 5 closest stations to 51.501476N 0.140634W. St. James's Park: 0.545 km Green Park: 0.600 km Victoria: 0.621 km Hyde Park Corner: 0.846 km Picadilly Circus: 1.027 km 

*   [func MedianOfMedians(list SortSlicer) int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#MedianOfMedians)
*   [func MedianOfRandoms(list SortSlicer, n int) int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#MedianOfRandoms)
*   [func Partition(list sort.Interface, pivot int) int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Partition)
*   [func Select(list SortSlicer, k int) int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Select)
*   [type Bounder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Bounder)
*   [type Bounding](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Bounding)
*       *   [func (b *Bounding) Contains(c Comparable) bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Bounding.Contains)

*   [type Comparable](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Comparable)
*   [type ComparableDist](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#ComparableDist)
*   [type Dim](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Dim)
*   [type DistKeeper](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#DistKeeper)
*       *   [func NewDistKeeper(d float64) *DistKeeper](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#NewDistKeeper)

*       *   [func (k *DistKeeper) Keep(c ComparableDist)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#DistKeeper.Keep)

*   [type Extender](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Extender)
*   [type Heap](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Heap)
*       *   [func (h *Heap) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Heap.Len)
    *   [func (h *Heap) Less(i, j int) bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Heap.Less)
    *   [func (h *Heap) Max() ComparableDist](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Heap.Max)
    *   [func (h *Heap) Pop() (i interface{})](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Heap.Pop)
    *   [func (h *Heap) Push(x interface{})](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Heap.Push)
    *   [func (h *Heap) Swap(i, j int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Heap.Swap)

*   [type Interface](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Interface)
*   [type Keeper](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Keeper)
*   [type NKeeper](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#NKeeper)
*       *   [func NewNKeeper(n int) *NKeeper](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#NewNKeeper)

*       *   [func (k *NKeeper) Keep(c ComparableDist)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#NKeeper.Keep)

*   [type Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Node)
*       *   [func (n *Node) String() string](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Node.String)

*   [type Operation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Operation)
*   [type Plane](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Plane)
*       *   [func (p Plane) Less(i, j int) bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Plane.Less)
    *   [func (p Plane) Pivot() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Plane.Pivot)
    *   [func (p Plane) Slice(start, end int) SortSlicer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Plane.Slice)
    *   [func (p Plane) Swap(i, j int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Plane.Swap)

*   [type Point](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Point)
*       *   [func (p Point) Compare(c Comparable, d Dim) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Point.Compare)
    *   [func (p Point) Dims() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Point.Dims)
    *   [func (p Point) Distance(c Comparable) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Point.Distance)
    *   [func (p Point) Extend(b *Bounding) *Bounding](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Point.Extend)

*   [type Points](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Points)
*       *   [func (p Points) Bounds() *Bounding](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Points.Bounds)
    *   [func (p Points) Index(i int) Comparable](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Points.Index)
    *   [func (p Points) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Points.Len)
    *   [func (p Points) Pivot(d Dim) int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Points.Pivot)
    *   [func (p Points) Slice(start, end int) Interface](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Points.Slice)

*   [type SortSlicer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#SortSlicer)
*   [type Tree](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Tree)
*       *   [func New(p Interface, bounding bool) *Tree](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#New)

*       *   [func (t *Tree) Contains(c Comparable) bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Tree.Contains)
    *   [func (t *Tree) Do(fn Operation) bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Tree.Do)
    *   [func (t *Tree) DoBounded(b *Bounding, fn Operation) bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Tree.DoBounded)
    *   [func (t *Tree) Insert(c Comparable, bounding bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Tree.Insert)
    *   [func (t *Tree) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Tree.Len)
    *   [func (t *Tree) Nearest(q Comparable) (Comparable, float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Tree.Nearest)
    *   [func (t *Tree) NearestSet(k Keeper, q Comparable)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Tree.NearestSet)

*   [Package (AccessiblePublicTransport)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#example-package-AccessiblePublicTransport)
*   [Tree](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#example-Tree)
*   [Tree (Bounds)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#example-Tree-Bounds)
*   [Tree.Do](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#example-Tree.Do)
*   [Tree.DoBounded](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#example-Tree.DoBounded)

This section is empty.

This section is empty.

func MedianOfMedians(list [SortSlicer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#SortSlicer)) [int](https://pkg.go.dev/builtin#int)

MedianOfMedians returns the index to the median value of the medians of groups of 5 consecutive elements.

#### func [MedianOfRandoms](https://github.com/gonum/gonum/blob/v0.17.0/spatial/kdtree/medians.go#L90)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#MedianOfRandoms "Go to MedianOfRandoms")

func MedianOfRandoms(list [SortSlicer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#SortSlicer), n [int](https://pkg.go.dev/builtin#int)) [int](https://pkg.go.dev/builtin#int)

MedianOfRandoms returns the index to the median value of up to n randomly chosen elements in list.

Partition partitions list such that all elements less than the value at pivot prior to the call are placed before that element and all elements greater than that value are placed after it. The final location of the element at pivot prior to the call is returned.

Select partitions list such that all elements less than the kth element are placed before k in the resulting list and all elements greater than it are placed after the position k.

type Bounder interface {
 Bounds() *[Bounding](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Bounding)}

Bounder returns a bounding volume containing the list of points. Bounds may return nil.

type Bounding struct {
 Min, Max [Comparable](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Comparable)}

Bounding represents a volume bounding box.

Contains returns whether c is within the volume of the Bounding. A nil Bounding returns true.

Comparable is the element interface for values stored in a k-d tree.

type ComparableDist struct {
 Comparable [Comparable](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Comparable) Dist [float64](https://pkg.go.dev/builtin#float64)}

ComparableDist holds a Comparable and a distance to a specific query. A nil Comparable is used to mark the end of the heap, so clients should not store nil values except for this purpose.

Dim is an index into a point's coordinates.

type DistKeeper struct {
[Heap](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Heap)}

DistKeeper is a Keeper that retains the ComparableDists within the specified distance of the query that it is called to Keep.

NewDistKeeper returns an DistKeeper with the maximum value of the heap set to d.

func (k *[DistKeeper](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#DistKeeper)) Keep(c [ComparableDist](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#ComparableDist))

Keep adds c to the heap if its distance is less than or equal to the max value of the heap.

type Extender interface {
	[Comparable](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Comparable)

	
	Extend(*[Bounding](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Bounding)) *[Bounding](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Bounding)
}

Extender is a Comparable that can increase a bounding volume to include the point represented by the Comparable.

type Heap [][ComparableDist](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#ComparableDist)

Heap is a max heap sorted on Dist.

func (h *[Heap](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Heap)) Max() [ComparableDist](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#ComparableDist)

func (h *[Heap](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Heap)) Pop() (i interface{})

func (h *[Heap](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Heap)) Push(x interface{})

func (h *[Heap](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Heap)) Swap(i, j [int](https://pkg.go.dev/builtin#int))

type Interface interface {
	Index(i [int](https://pkg.go.dev/builtin#int)) [Comparable](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Comparable)

	Len() [int](https://pkg.go.dev/builtin#int)

	Pivot([Dim](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Dim)) [int](https://pkg.go.dev/builtin#int)

	
	Slice(start, end [int](https://pkg.go.dev/builtin#int)) [Interface](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Interface)
}

Interface is the set of methods required for construction of efficiently searchable k-d trees. A k-d tree may be constructed without using the Interface type, but it is likely to have reduced search performance.

Keeper implements a conditional max heap sorted on the Dist field of the ComparableDist type. kd search is guided by the distance stored in the max value of the heap.

type NKeeper struct {
[Heap](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Heap)}

NKeeper is a Keeper that retains the n best ComparableDists that have been passed to Keep.

func NewNKeeper(n [int](https://pkg.go.dev/builtin#int)) *[NKeeper](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#NKeeper)

NewNKeeper returns an NKeeper with the max value of the heap set to infinite distance. The returned NKeeper is able to retain at most n values.

func (k *[NKeeper](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#NKeeper)) Keep(c [ComparableDist](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#ComparableDist))

Keep adds c to the heap if its distance is less than the maximum value of the heap. If adding c would increase the size of the heap beyond the initial maximum length, the maximum value of the heap is dropped.

type Node struct {
 Point [Comparable](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Comparable) Plane [Dim](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Dim) Left, Right *[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Node) *[Bounding](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Bounding)}

Node holds a single point value in a k-d tree.

Operation is a function that operates on a Comparable. The bounding volume and tree depth of the point is also provided. If done is returned true, the Operation is indicating that no further work needs to be done and so the Do function should traverse no further.

type Plane struct {
[Dim](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Dim)[Points](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Points)}

Plane is a wrapping type that allows a Points type be pivoted on a dimension. The Pivot method of Plane uses MedianOfRandoms sampling at most 100 elements to find a pivot element.

func (p [Plane](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Plane)) Pivot() [int](https://pkg.go.dev/builtin#int)

func (p [Plane](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Plane)) Slice(start, end [int](https://pkg.go.dev/builtin#int)) [SortSlicer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#SortSlicer)

func (p [Plane](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Plane)) Swap(i, j [int](https://pkg.go.dev/builtin#int))

Point represents a point in a k-d space that satisfies the Comparable interface.

Compare returns the signed distance of p from the plane passing through c and perpendicular to the dimension d. The concrete type of c must be Point.

func (p [Point](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Point)) Dims() [int](https://pkg.go.dev/builtin#int)

Dims returns the number of dimensions described by the receiver.

Distance returns the squared Euclidean distance between c and the receiver. The concrete type of c must be Point.

func (p [Point](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Point)) Extend(b *[Bounding](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Bounding)) *[Bounding](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Bounding)

Extend returns a bounding box that has been extended to include the receiver.

Points is a collection of point values that satisfies the Interface.

func (p [Points](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Points)) Bounds() *[Bounding](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Bounding)

func (p [Points](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Points)) Index(i [int](https://pkg.go.dev/builtin#int)) [Comparable](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Comparable)

func (p [Points](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Points)) Len() [int](https://pkg.go.dev/builtin#int)

func (p [Points](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Points)) Pivot(d [Dim](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Dim)) [int](https://pkg.go.dev/builtin#int)

func (p [Points](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Points)) Slice(start, end [int](https://pkg.go.dev/builtin#int)) [Interface](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Interface)

SortSlicer satisfies the sort.Interface and is able to slice itself.

type Tree struct {
 Root *[Node](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Node) Count [int](https://pkg.go.dev/builtin#int)}

Tree implements a k-d tree creation and nearest neighbor search.

Output:

[9 6] is closest point to [8 7], d=1.414214 

Output:

Bounding box of points is &{Min:[2 1] Max:[9 7]} 

func New(p [Interface](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Interface), bounding [bool](https://pkg.go.dev/builtin#bool)) *[Tree](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Tree)

New returns a k-d tree constructed from the values in p. If p is a Bounder and bounding is true, bounds are determined for each node. The ordering of elements in p may be altered after New returns.

func (t *[Tree](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Tree)) Contains(c [Comparable](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Comparable)) [bool](https://pkg.go.dev/builtin#bool)

Contains returns whether a Comparable is in the bounds of the tree. If no bounding has been constructed Contains returns true.

Do performs fn on all values stored in the tree. A boolean is returned indicating whether the Do traversal was interrupted by an Operation returning true. If fn alters stored values' sort relationships, future tree operation behaviors are undefined.

Output:

[2 3] [4 7] [5 4] 

func (t *[Tree](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Tree)) DoBounded(b *[Bounding](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Bounding), fn [Operation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Operation)) [bool](https://pkg.go.dev/builtin#bool)

DoBounded performs fn on all values stored in the tree that are within the specified bound. If b is nil, the result is the same as a Do. A boolean is returned indicating whether the DoBounded traversal was interrupted by an Operation returning true. If fn alters stored values' sort relationships future tree operation behaviors are undefined.

Output:

p=[5 4] bound=&{Min:[2 3] Max:[5 7]} depth=1 p=[4 7] bound=&{Min:[4 7] Max:[4 7]} depth=2 

func (t *[Tree](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Tree)) Insert(c [Comparable](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Comparable), bounding [bool](https://pkg.go.dev/builtin#bool))

Insert adds a point to the tree, updating the bounding volumes if bounding is true, and the tree is empty or the tree already has bounding volumes stored, and c is an Extender. No rebalancing of the tree is performed.

Len returns the number of elements in the tree.

Nearest returns the nearest value to the query and the distance between them.

func (t *[Tree](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Tree)) NearestSet(k [Keeper](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Keeper), q [Comparable](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/kdtree#Comparable))

NearestSet finds the nearest values to the query accepted by the provided Keeper, k. k must be able to return a ComparableDist specifying the maximum acceptable distance when Max() is called, and retains the results of the search in min sorted order after the call to NearestSet returns. If a sentinel ComparableDist with a nil Comparable is used by the Keeper to mark the maximum distance, NearestSet will remove it before returning.
