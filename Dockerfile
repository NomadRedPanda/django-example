# Set the python version as a build-time argument
# with Python 3.12 as the default
ARG PYTHON_VERSION=3.12-slim-bullseye
FROM python:${PYTHON_VERSION}

# Set Python-related environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a virtual environment
RUN python -m venv /opt/venv

# Set the virtual environment as the current location
ENV PATH=/opt/venv/bin:$PATH

# Upgrade pip
RUN pip install --upgrade pip


# Install os dependencies for our mini vm
RUN apt-get update && apt-get install -y \
    # for postgres
    libpq-dev \
    # for Pillow
    libjpeg-dev \
    # for CairoSVG
    libcairo2 \
    # other
    gcc \
    # install netcat for the "nc" command
    netcat \  
    && rm -rf /var/lib/apt/lists/*

# Set the working directory to that same app directory
WORKDIR /app/src

# copy the project app into the container's working directory
COPY . /app/

# Install the Python project requirements
RUN pip install -r /app/requirements.txt

# make the bash script executable
RUN chmod +x /app/start.sh

# Expose port 8000 (for Gunicorn)
EXPOSE 3003

# Clean up apt cache to reduce image size
RUN apt-get remove --purge -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Start the Gunicorn server
CMD ["/app/start.sh"]