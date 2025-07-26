# FastAPI Microservice Template

This template includes a basic setup for a dockerized fastapi microservice. 

## Running

### Running in docker
1. Build the docker image
    ```bash
    docker build -t image-name:latest .
    ```
2. Run the container
    ```bash
    # To just run a container
    docker run -p 80:80 --rm mcp-server:latest
   
    # To enable live reloading when coding
    docker run -p 80:80 -v .:/app --rm mcp-server:latest
    ```

### Running without docker
1. Create a python virtual environment
    ```bash
    python -m venv .venv
    ```
2. Activate the venv
    ```bash
    # MacOS / Linux
    source .venv/bin/activate

    # Windows
    .venv/Scripts/Activate.bat # .ps1 if using powershell
    ```
3. Install the requirements
    ```bash
    pip install -r requirements.txt
    ```
4. Run the API
    ```bash
    uvicorn public.index:app --host 0.0.0.0 --port 80 --reload
    ```


## Usage
The app contains a default example endpoint that can be visited at [http://localhost/](http://localhost/)
