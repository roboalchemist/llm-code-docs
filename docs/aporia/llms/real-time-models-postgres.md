# Source: https://docs.aporia.com/storing-your-predictions/real-time-models-postgres.md

# Source: https://docs.aporia.com/v1/storing-your-predictions/real-time-models-postgres.md

# Real-time Models (Postgres)

For real-time models with mid-level throughput (e.g models with an HTTP endpoint such as `POST /predict`), you can insert predictions to a database such as [Postgres](https://www.postgresql.org/), [MySQL](https://www.mysql.com/), or even [Elasticsearch](https://www.elastic.co/).

If you are dealing with billions of predictions, this solution might not be sufficient for you.

{% hint style="warning" %}
**Dealing with billions of predictions?**

If you are dealing with billions of predictions, this solution might not be sufficient for you.

Please consider the guide on [real-time models with Kafka](https://docs.aporia.com/v1/storing-your-predictions/real-time-models-kafka).&#x20;
{% endhint %}

### Example: FastAPI + SQLAlchemy

If you are serving models with Flask or FastAPI, and don't have an extremely high throughput, you can simply insert predictions to a standard database.

Here, we'll use [SQLAlchemy](https://www.sqlalchemy.org/), which is a Python ORM to replace writing SQL `INSERT` statements directly with something a bit nicer. Please see the [FastAPI + SQLAlchemy tutorial](https://fastapi.tiangolo.com/tutorial/sql-databases/) for more details.

First, we can define the structure of our database table using Pydantic:

```python
class IrisModelPrediction(BaseModel):
    id: str
    timestamp: datetime

    # Features
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    # Predictions
    prediction: int
    confidence: float
```

And here is a sample implementation of `POST /predict` endpoint:

```python
@app.post("/predict")
def predict(request: PredictRequest):
    # Preprocess & predict
    df = pd.DataFrame(columns=['sepal.length', 'sepal.width', 'petal.length', 'petal.width'],
                      data=[[request.sepal.length, request.sepal.width, request.petal.length, request.petal.width]])

    y, confidence = model.predict(df)

    # Insert prediction to DB
    prediction = IrisModelPrediction(
        id=str(uuid.uuid4()),
        timestamp=datetime.now(),
        sepal_length=request.sepal.length,
        sepal_width=request.sepal.width,
        petal_length=request.petal.length,
        petal_width=request.petal.width,
        prediction=y,
        confidence=confidence,
    )

    db.add(prediction)
    db.commit()

    return {"prediction": y_pred}
```
