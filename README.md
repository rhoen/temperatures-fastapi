# FastAPI with Auth0 Starter App

### Local development
For dependency management we use `poetry`. Install the latest poetry [here]
(https://python-poetry.org/docs/).

Then install the project dependencies with `poetry install`.

Add new dependencies with `poetry add my-dependency`.

### API
We use [FastAPI](https://fastapi.tiangolo.com/) for the backend. Run using 
poetry with ```poetry run uvicorn main:app --reload```


###Auth0
We use [Auth0](https://auth0.com/) for authentication. You'll need to create 
an 'API' inside their app as well as a machine to machine application (this 
may get created automatically after you make the api) and a javascript front 
end 'SPA' application. The values in `config/config.json` come from the SPA. The 
values in your `.env` come from the M2M. The `.env` can include:
```
AUTH0_DOMAIN=
AUTH0_CLIENT_ID=
AUTH0_API_AUDIENCE=
```
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


###Resources
* Deploying poetry based python app on [heroku](https://github.
com/moneymeets/python-poetry-buildpack)
* Auth0 JS Client [docs](https://auth0.
com/docs/quickstart/spa/vanillajs/02-calling-an-api#calling-the-api)
* Add OAuth to fastapi (the official auth0 docs and libraries only support 
  flask) [video](https://www.youtube.com/watch?v=ZSzzpnsOdrA)
