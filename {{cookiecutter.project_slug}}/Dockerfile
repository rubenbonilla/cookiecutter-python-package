FROM python:3.6-slim

WORKDIR /usr/src/app

# RUN apt-get update && apt-get install -y \
#     dependencies-here \
# && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

VOLUME /usr/src/app
CMD ["python", "{{cookiecutter.project_slug}}", "-dv"]
