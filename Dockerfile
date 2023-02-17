# Start from the official Python base image
FROM python:3.9
# Install Poetry
RUN pip install poetry

# Set the working directory
WORKDIR /code
# Copy poetry files to the working directory
COPY poetry.lock pyproject.toml /code/
# Copy our files to inside the working directory
COPY ./api /code/api

# Install dependencies with poetry
RUN poetry install

# Start the server 
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]