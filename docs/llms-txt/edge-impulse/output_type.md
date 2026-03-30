# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/studio/python/edgeimpulse/model/output_type.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse.model.output_type

## Classes

### Classification

```python  theme={"system"}
edgeimpulse.model.output_type.Classification(
	labels: List[str] | None = None
)
```

| Parameters |                            |
| ---------- | -------------------------- |
| `labels`   | `List[str] \| None = None` |

| Bases           |
| --------------- |
| `builtins.dict` |

### ObjectDetection

```python  theme={"system"}
edgeimpulse.model.output_type.ObjectDetection(
	labels: List[str],
	last_layer: Literal['mobilenet-ssd', 'fomo', 'yolov5', 'yolo5v5-drpai', 'yolox', 'yolov7'] | str,
	minimum_confidence: float
)
```

| Parameters           |                                                                                         |
| -------------------- | --------------------------------------------------------------------------------------- |
| `labels`             | `List[str]`                                                                             |
| `last_layer`         | `Literal['mobilenet-ssd', 'fomo', 'yolov5', 'yolo5v5-drpai', 'yolox', 'yolov7'] \| str` |
| `minimum_confidence` | `float`                                                                                 |

| Bases           |
| --------------- |
| `builtins.dict` |

### Regression

```python  theme={"system"}
edgeimpulse.model.output_type.Regression(
	
)
```

| Bases           |
| --------------- |
| `builtins.dict` |


Built with [Mintlify](https://mintlify.com).