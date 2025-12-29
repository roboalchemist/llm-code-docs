# Source: https://onnxruntime.ai/docs/api/python/tutorial.html

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSJkaXNwbGF5OiBub25lOyI+CiAgPHN5bWJvbCBpZD0ic3ZnLXRvYyIgdmlld2JveD0iMCAwIDI0IDI0Ij4KICAgIDx0aXRsZT5Db250ZW50czwvdGl0bGU+CiAgICA8c3ZnIHN0cm9rZT0iY3VycmVudENvbG9yIiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMCIgdmlld2JveD0iMCAwIDEwMjQgMTAyNCI+CiAgICAgIDxwYXRoIGQ9Ik00MDggNDQyaDQ4MGM0LjQgMCA4LTMuNiA4LTh2LTU2YzAtNC40LTMuNi04LTgtOEg0MDhjLTQuNCAwLTggMy42LTggOHY1NmMwIDQuNCAzLjYgOCA4IDh6bS04IDIwNGMwIDQuNCAzLjYgOCA4IDhoNDgwYzQuNCAwIDgtMy42IDgtOHYtNTZjMC00LjQtMy42LTgtOC04SDQwOGMtNC40IDAtOCAzLjYtOCA4djU2em01MDQtNDg2SDEyMGMtNC40IDAtOCAzLjYtOCA4djU2YzAgNC40IDMuNiA4IDggOGg3ODRjNC40IDAgOC0zLjYgOC04di01NmMwLTQuNC0zLjYtOC04LTh6bTAgNjMySDEyMGMtNC40IDAtOCAzLjYtOCA4djU2YzAgNC40IDMuNiA4IDggOGg3ODRjNC40IDAgOC0zLjYgOC04di01NmMwLTQuNC0zLjYtOC04LTh6TTExNS40IDUxOC45TDI3MS43IDY0MmM1LjggNC42IDE0LjQuNSAxNC40LTYuOVYzODguOWMwLTcuNC04LjUtMTEuNS0xNC40LTYuOUwxMTUuNCA1MDUuMWE4Ljc0IDguNzQgMCAwIDAgMCAxMy44eiIgLz4KICAgIDwvc3ZnPg==)

Menu

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBjbGFzcz0iZmVhdGhlci1tZW51Ij4KICAgICAgPGxpbmUgeDE9IjMiIHkxPSIxMiIgeDI9IjIxIiB5Mj0iMTIiPjwvbGluZT4KICAgICAgPGxpbmUgeDE9IjMiIHkxPSI2IiB4Mj0iMjEiIHkyPSI2Ij48L2xpbmU+CiAgICAgIDxsaW5lIHgxPSIzIiB5MT0iMTgiIHgyPSIyMSIgeTI9IjE4Ij48L2xpbmU+CiAgICA8L3N2Zz4=)

Expand

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBjbGFzcz0iZmVhdGhlci1jaGV2cm9uLXJpZ2h0Ij4KICAgICAgPHBvbHlsaW5lIHBvaW50cz0iOSAxOCAxNSAxMiA5IDYiPjwvcG9seWxpbmU+CiAgICA8L3N2Zz4=)

Light mode

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJmZWF0aGVyLXN1biI+CiAgICAgIDxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjUiPjwvY2lyY2xlPgogICAgICA8bGluZSB4MT0iMTIiIHkxPSIxIiB4Mj0iMTIiIHkyPSIzIj48L2xpbmU+CiAgICAgIDxsaW5lIHgxPSIxMiIgeTE9IjIxIiB4Mj0iMTIiIHkyPSIyMyI+PC9saW5lPgogICAgICA8bGluZSB4MT0iNC4yMiIgeTE9IjQuMjIiIHgyPSI1LjY0IiB5Mj0iNS42NCI+PC9saW5lPgogICAgICA8bGluZSB4MT0iMTguMzYiIHkxPSIxOC4zNiIgeDI9IjE5Ljc4IiB5Mj0iMTkuNzgiPjwvbGluZT4KICAgICAgPGxpbmUgeDE9IjEiIHkxPSIxMiIgeDI9IjMiIHkyPSIxMiI+PC9saW5lPgogICAgICA8bGluZSB4MT0iMjEiIHkxPSIxMiIgeDI9IjIzIiB5Mj0iMTIiPjwvbGluZT4KICAgICAgPGxpbmUgeDE9IjQuMjIiIHkxPSIxOS43OCIgeDI9IjUuNjQiIHkyPSIxOC4zNiI+PC9saW5lPgogICAgICA8bGluZSB4MT0iMTguMzYiIHkxPSI1LjY0IiB4Mj0iMTkuNzgiIHkyPSI0LjIyIj48L2xpbmU+CiAgICA8L3N2Zz4=)

Dark mode

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJpY29uLXRhYmxlci1tb29uIj4KICAgICAgPHBhdGggc3Ryb2tlPSJub25lIiBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIiAvPgogICAgICA8cGF0aCBkPSJNMTIgM2MuMTMyIDAgLjI2MyAwIC4zOTMgMGE3LjUgNy41IDAgMCAwIDcuOTIgMTIuNDQ2YTkgOSAwIDEgMSAtOC4zMTMgLTEyLjQ1NHoiIC8+CiAgICA8L3N2Zz4=)

Auto light/dark mode

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJpY29uLXRhYmxlci1zaGFkb3ciPgogICAgICA8cGF0aCBzdHJva2U9Im5vbmUiIGQ9Ik0wIDBoMjR2MjRIMHoiIGZpbGw9Im5vbmUiIC8+CiAgICAgIDxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjkiPjwvY2lyY2xlPgogICAgICA8cGF0aCBkPSJNMTMgMTJoNSIgLz4KICAgICAgPHBhdGggZD0iTTEzIDE1aDQiIC8+CiAgICAgIDxwYXRoIGQ9Ik0xMyAxOGgxIiAvPgogICAgICA8cGF0aCBkPSJNMTMgOWg0IiAvPgogICAgICA8cGF0aCBkPSJNMTMgNmgxIiAvPgogICAgPC9zdmc+)

Hide navigation sidebar

Hide table of contents sidebar

Toggle site navigation sidebar

*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctbWVudSIgLz48L3N2Zz4=)*

[](index.html)

Python API documentation

Toggle Light / Dark / Auto color theme

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idGhlbWUtaWNvbi13aGVuLWF1dG8iPjx1c2UgaHJlZj0iI3N2Zy1zdW4taGFsZiIgLz48L3N2Zz4=) ![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idGhlbWUtaWNvbi13aGVuLWRhcmsiPjx1c2UgaHJlZj0iI3N2Zy1tb29uIiAvPjwvc3ZnPg==) ![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idGhlbWUtaWNvbi13aGVuLWxpZ2h0Ij48dXNlIGhyZWY9IiNzdmctc3VuIiAvPjwvc3ZnPg==)

Toggle table of contents sidebar

*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctdG9jIiAvPjwvc3ZnPg==)*

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+CiAgICAgICAgICAgIDxwYXRoIGQ9Ik0xMyAyMGgtMlY4bC01LjUgNS41LTEuNDItMS40MkwxMiA0LjE2bDcuOTIgNy45Mi0xLjQyIDEuNDJMMTMgOHYxMnoiIC8+CiAgICAgICAgICA8L3N2Zz4=) Back to top](#)

Toggle Light / Dark / Auto color theme

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idGhlbWUtaWNvbi13aGVuLWF1dG8iPjx1c2UgaHJlZj0iI3N2Zy1zdW4taGFsZiIgLz48L3N2Zz4=) ![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idGhlbWUtaWNvbi13aGVuLWRhcmsiPjx1c2UgaHJlZj0iI3N2Zy1tb29uIiAvPjwvc3ZnPg==) ![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idGhlbWUtaWNvbi13aGVuLWxpZ2h0Ij48dXNlIGhyZWY9IiNzdmctc3VuIiAvPjwvc3ZnPg==)

Toggle table of contents sidebar

*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctdG9jIiAvPjwvc3ZnPg==)*

# Tutorial[\#](#tutorial "Permalink to this heading")

*ONNX Runtime* provides an easy way to run machine learned models with high performance on CPU or GPU without dependencies on the training framework. Machine learning frameworks are usually optimized for batch training rather than for prediction, which is a more common scenario in applications, sites, and services. At a high level, you can:

1.  Train a model using your favorite framework.

2.  Convert or export the model into ONNX format. See [ONNX Tutorials](https://github.com/onnx/tutorials) for more details.

3.  Load and run the model using *ONNX Runtime*.

In this tutorial, we will briefly create a pipeline with *scikit-learn*, convert it into ONNX format and run the first predictions.

[]

## Step 1: Train a model using your favorite framework[\#](#step-1-train-a-model-using-your-favorite-framework "Permalink to this heading")

We'll use the famous iris datasets.

\<\<\<

    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    from sklearn.linear_model import LogisticRegression
    clr = LogisticRegression()
    clr.fit(X_train, y_train)
    print(clr)

\>\>\>

        LogisticRegression()

## Step 2: Convert or export the model into ONNX format[\#](#step-2-convert-or-export-the-model-into-onnx-format "Permalink to this heading")

[ONNX](https://github.com/onnx/onnx) is a format to describe the machine learned model. It defines a set of commonly used operators to compose models. There are [tools](https://github.com/onnx/tutorials) to convert other model formats into ONNX. Here we will use [ONNXMLTools](https://github.com/onnx/onnxmltools).

\<\<\<

    from skl2onnx import convert_sklearn
    from skl2onnx.common.data_types import FloatTensorType

    initial_type = [('float_input', FloatTensorType([None, 4]))]
    onx = convert_sklearn(clr, initial_types=initial_type)
    with open("logreg_iris.onnx", "wb") as f:
        f.write(onx.SerializeToString())

\>\>\>

        

## Step 3: Load and run the model using ONNX Runtime[\#](#step-3-load-and-run-the-model-using-onnx-runtime "Permalink to this heading")

We will use *ONNX Runtime* to compute the predictions for this machine learning model.

\<\<\<

    import numpy
    import onnxruntime as rt

    sess = rt.InferenceSession(
        "logreg_iris.onnx", providers=rt.get_available_providers())
    input_name = sess.get_inputs()[0].name
    pred_onx = sess.run(None, )[0]
    print(pred_onx)

\>\>\>

        [0 2 2 1 0 2 1 1 0 0 1 1 2 2 0 1 2 0 0 0 2 0 1 2 0 1 0 0 1 0 1 2 1 2 2 2 0
         2]

The code can be changed to get one specific output by specifying its name into a list.

\<\<\<

    import numpy
    import onnxruntime as rt

    sess = rt.InferenceSession(
        "logreg_iris.onnx", providers=rt.get_available_providers())
    input_name = sess.get_inputs()[0].name
    label_name = sess.get_outputs()[0].name
    pred_onx = sess.run(
        [label_name], )[0]
    print(pred_onx)

\>\>\>

        [0 2 2 1 0 2 1 1 0 0 1 1 2 2 0 1 2 0 0 0 2 0 1 2 0 1 0 0 1 0 1 2 1 2 2 2 0
         2]

[](api_summary.html)

Next

API

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZnVyby1yZWxhdGVkLWljb24iPjx1c2UgaHJlZj0iI3N2Zy1hcnJvdy1yaWdodCIgLz48L3N2Zz4=) [![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZnVyby1yZWxhdGVkLWljb24iPjx1c2UgaHJlZj0iI3N2Zy1hcnJvdy1yaWdodCIgLz48L3N2Zz4=)](index.html)

Previous

Home

Copyright © 2018-2024, Microsoft

Made with [Sphinx](https://www.sphinx-doc.org/) and [\@pradyunsg](https://pradyunsg.me)\'s [Furo](https://github.com/pradyunsg/furo)