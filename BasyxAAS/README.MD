# Install Git on your Development Environment 

Download GIT from this URL

https://git-scm.com/install/windows

# Clone your project 

```bash
Git clone https://github.com/AbdBelf/digitaltwin-battery.git
```

# Install Docker Desktop on Windows 

Download the Docker Desktop installer for Windows:

https://www.docker.com/products/docker-desktop/

# BaSyx Infrastructure Setup

Run the following command line in the "BasyxAAS" folder: 

```bash
docker compose up -d
```

the following components are started:
* AAS Repository (http://localhost:8081/shells)
* Submodel Repository (http://localhost:8081/submodels)
* ConceptDescription Repository (http://localhost:8081/concept-descriptions)
* AAS Registry (http://localhost:8082/shell-descriptors)
* Submodel Registry (http://localhost:8083/submodel-descriptors)
* AAS Discovery (http://localhost:8084/lookup/shells)
* AAS Web UI (http://localhost:3000)

By leveraging the registry integration features of AAS Repository and Submodel Repository, the preconfigured AAS Environment serializations are loaded and automatically registered.
