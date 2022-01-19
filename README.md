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
We use Heroku to deploy. Heroku users 'buildpacks' to translate the code in 
the repo into what ever it needs to run our app in their virtual machines. 
We use a non-standard buildpack to convert the poetry depenency management 
(pyproject.toml) into the more common 'requirements.txt' which heroku needs. 
With the heroku CLI run the following: 

```
heroku buildpacks:clear
heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git
heroku buildpacks:add heroku/python
```
as documented (here)[https://github.com/moneymeets/python-poetry-buildpack].

