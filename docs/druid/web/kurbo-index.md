druid

# Crate kurbo

Source

## Modules§

commonCommon mathematical operationsoffsetComputation of offset curves of cubic Béziers, based on a curve fitting
approach.simplifySimplification of a Bézier path.

## Structs§

AffineA 2D affine transform.ArcA single arc segment.BezPathA Bézier path.CircleA circle.CircleSegmentA segment of a circle.ConstPointA trivial “curve” that is just a constant.CubicBezA single cubic Bézier segment.CubicBezIterAn iterator for cubic beziers.CurveFitSampleA sample point of a curve for fitting.EllipseAn ellipse.InsetsInsets from the edges of a rectangle.LineA single line.LineIntersectionAn intersection of a `Line` and a `PathSeg`.MinDistanceThe minimum distance between two Bézier curves.NearestThe nearest position on a curve to some point.PathSegIterAn iterator for path segments.PointA 2D point.QuadBezA single quadratic Bézier segment.QuadBezIterAn iterator for quadratic beziers.QuadSplineA quadratic Bézier spline in B-spline format.RectA rectangle.RoundedRectA rectangle with equally rounded corners.RoundedRectRadiiRadii for each corner of a rounded rectangle.SegmentsAn iterator that transforms path elements to path segments.SizeA 2D size.SvgArcA single SVG arc segment.TranslateScaleA transformation including scaling and translation.Vec2A 2D vector.

## Enums§

PathElThe element of a Bézier path.PathSegA segment of a Bézier path.SvgParseErrorAn error which can be returned when parsing an SVG.

## Constants§

DEFAULT_ACCURACYA default value for methods that take an ‘accuracy’ argument.MAX_EXTREMAThe maximum number of extrema that can be reported in the `ParamCurveExtrema` trait.

## Traits§

ParamCurveA curve parametrized by a scalar.ParamCurveArclenA parametrized curve that can have its arc length measured.ParamCurveAreaA parametrized curve that can have its signed area measured.ParamCurveCurvatureA parametrized curve that reports its curvature.ParamCurveDerivA differentiable parametrized curve.ParamCurveExtremaA parametrized curve that reports its extrema.ParamCurveFitThe source curve for curve fitting.ParamCurveNearestA parametrized curve that reports the nearest point.ShapeA generic trait for open and closed shapes.

## Functions§

cubics_to_quadratic_splinesConvert multiple cubic Bézier curves to quadratic splines.fit_to_bezpathGenerate a Bézier path that fits the source curve.fit_to_bezpath_optGenerate a highly optimized Bézier path that fits the source curve.fit_to_cubicFit a single cubic to a range of the source curve.flattenFlatten the path, invoking the callback repeatedly.segmentsTransform an iterator over path elements into one over path
segments.
