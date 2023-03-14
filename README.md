# Django Next Template

Template that uses Django as a backend and NextJS as a frontend.

1. Clone this project
2. Have two separate terminal windows, one in `django-next-template/next` and another in `django-next-template/django`

Django window

1. Run `python3 -m venv venv` to create a virtual environment
2. Run `source venv/bin/activate` to activate the virtual environment
3. Run `pip install -r requirements.txt` to install requirements
4. Run `manage.py migrate` to migrate existing models
5. Run `manage.py runserver` to run backend
6. Visit `localhost:8000/api` to view the backend (or replace `api` with `admin` for Django admin)

NextJS window

1. Run `yarn install` to install requirements
2. Run `npm run dev` to run frontend
3. Visit `localhost:3000` to view the frontend
