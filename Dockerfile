# Start from the official Python base image
FROM python:3.9

# Set the working directory
WORKDIR /code

# Copy poetry files to the working directory
COPY poetry.lock pyproject.toml /code/
# Copy our files to inside the working directory
COPY ./api /code/

# Install dependencies
RUN pip install poetry
RUN poetry export --without-hashes --format=requirements.txt > requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Start the server
EXPOSE 5432
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]