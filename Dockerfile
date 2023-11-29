FROM python:3.10
COPY . /it_solution
WORKDIR /it_solution
COPY poetry.lock pyproject.toml it_solution/

RUN pip install poetry
RUN poetry install
RUN poetry config virtualenvs.create false
RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN apt-get update && apt-get install -y ffmpeg

EXPOSE 8000
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]