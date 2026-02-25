FROM ubuntu:latest
LABEL authors="eugenkonyshev"

RUN apt update && apt install curl -y

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh
# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh
# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

RUN mkdir /code

WORKDIR /code

COPY ./pyproject.toml /code/
COPY ./uv.lock /code/
COPY ./.python-version /code/
RUN uv sync

CMD ["uv", "run", "main.py"]