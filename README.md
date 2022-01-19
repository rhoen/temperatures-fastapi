# Steal

### Local development
For dependency management we use `poetry`. Install the latest poetry [here]
(https://python-poetry.org/docs/).

Then install the project dependencies with `poetry install`.

Add new dependencies with `poetry add my-dependency`.

### API
We use [FastAPI](https://fastapi.tiangolo.com/) for the backend. Run using 
poetry with ```poetry run uvicorn main:app --reload```


### Deploy
We use Heroku to deploy
