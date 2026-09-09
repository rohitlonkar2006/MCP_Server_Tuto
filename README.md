# MCP Server Tutorial --- Complete Journey

A practical **Model Context Protocol (MCP)** learning project built with
Python.\
This repository documents the journey from a basic MCP server to HTTP
MCP, third-party MCP, PyPI packages, an MCP Gateway, and Docker
containerization.

------------------------------------------------------------------------

## 📚 Project Journey

``` text
CH-1 → Create MCP
        ↓
CH-2 → HTTP MCP
        ↓
CH-3 → Third-Party MCP
        ↓
CH-4 → PyPI MCP
        ↓
CH-5 → MCP Gateway
        ↓
CH-6 → MCP + Docker
```

The project focuses on understanding how MCP servers expose tools, how
clients communicate with them, how external/packaged MCP tools are
integrated, and how an MCP system can be organized and deployed.

------------------------------------------------------------------------

# 📁 Current Project Structure

``` text
MCP_Server_Tuto/
│
├── .venv/
│
├── CH-1_CreateMCP/
│   ├── 1_first_mcp_server_stdio.py
│   ├── 2_python_client.py
│   └── 3_langchain_client.py
│
├── CH-2_HTTP_MCP/
│   ├── 1_http_mcp.py
│   └── 2_langchain_client.py
│
├── CH-3_Third_Party_MCP/
│   └── community_mcp.py
│
├── CH-4_PyPI_MCP/
│   ├── 1_test_package.py
│   └── 2_client.py
│
├── CH-5_MCP_Gateway/
│
├── CH-6_MCP_Docker/
│   ├── app/
│   │   └── gateway.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── .gitattributes
├── .python-version
├── main.py
├── package.json
├── pyproject.toml
├── README.md
├── requirements.txt
└── uv.lock
```

------------------------------------------------------------------------

# CH-1 --- Create MCP

This is the starting point of the MCP journey. It covers creating a
basic MCP server and connecting clients to it.

### Files

``` text
CH-1_CreateMCP/
├── 1_first_mcp_server_stdio.py
├── 2_python_client.py
└── 3_langchain_client.py
```

### 1. `1_first_mcp_server_stdio.py`

Introduces a basic MCP server using **stdio communication**.

Main concepts:

-   Creating an MCP server
-   Defining MCP tools
-   Running the server locally
-   Stdio transport
-   Server-side tool implementation

### 2. `2_python_client.py`

Introduces a Python MCP client that communicates with the MCP server.

Typical client flow:

``` text
Connect
   ↓
Initialize Session
   ↓
Discover Tools
   ↓
Call Tool
   ↓
Receive Result
```

### 3. `3_langchain_client.py`

Connects the MCP functionality with **LangChain**, showing how MCP tools
can be used from an AI application framework.

### Goal

Understand the fundamental relationship between:

``` text
MCP Server ↔ MCP Client
```

------------------------------------------------------------------------

# CH-2 --- HTTP MCP

The second chapter moves from local stdio communication toward
**HTTP-based MCP communication**.

### Files

``` text
CH-2_HTTP_MCP/
├── 1_http_mcp.py
└── 2_langchain_client.py
```

### Main concepts

-   HTTP transport
-   MCP server over HTTP
-   Client-server communication
-   Connecting MCP with LangChain
-   Remote-style MCP communication

### Goal

Understand how an MCP server can communicate over HTTP and how a client
can connect to it.

------------------------------------------------------------------------

# CH-3 --- Third-Party MCP

The third chapter focuses on using MCP functionality provided by third
parties or the MCP community.

### File

``` text
CH-3_Third_Party_MCP/
└── community_mcp.py
```

### Main concepts

-   Third-party MCP servers
-   Community MCP tools
-   Reusing existing MCP functionality
-   Connecting external tools to an application

### Goal

Learn that MCP applications do not need to implement every tool
themselves. Existing MCP tools can be integrated and reused.

------------------------------------------------------------------------

# CH-4 --- PyPI MCP

The fourth chapter introduces **Python package distribution** and using
an MCP package through PyPI.

### Files

``` text
CH-4_PyPI_MCP/
├── 1_test_package.py
└── 2_client.py
```

### Main concepts

-   Python packages
-   PyPI
-   Package installation
-   Testing an installed package
-   Using MCP packages from a client
-   Package entry points

### Example package

``` text
rohits-agentic-terminal
```

One important Python packaging concept learned here is that the **PyPI
distribution name and Python import/module name can be different**.

For example:

``` text
PyPI distribution:
rohits-agentic-terminal

Python module:
agentic_terminal
```

Therefore, the package installed with:

``` bash
uv pip install rohits-agentic-terminal==0.1.0
```

may be imported using the module name:

``` python
from agentic_terminal.tools import mcp
```

### Goal

Understand how MCP functionality can be packaged, distributed,
installed, and consumed like a normal Python package.

------------------------------------------------------------------------

# CH-5 --- MCP Gateway

The fifth chapter introduces an **MCP Gateway** architecture.

A gateway can act as a central layer between an application/client and
multiple MCP servers.

``` text
                 ┌── MCP Server 1
                 │
Client → Gateway ├── MCP Server 2
                 │
                 └── MCP Server 3
```

### Why use a Gateway?

A gateway can help with:

-   Centralized MCP connections
-   Managing multiple MCP servers
-   Organizing tools
-   Providing a common access layer
-   Simplifying client-side integration

### Goal

Understand how multiple MCP services can be organized behind a single
gateway layer.

------------------------------------------------------------------------

# CH-6 --- MCP + Docker

The final visible chapter focuses on **containerizing the MCP Gateway
with Docker**.

### Files

``` text
CH-6_MCP_Docker/
├── app/
│   └── gateway.py
├── Dockerfile
└── requirements.txt
```

### Dockerfile

The current Docker setup uses Python 3.13 slim:

``` dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "/app/gateway.py"]
```

### Explanation

  Docker instruction   Purpose
  -------------------- -----------------------------------------
  `FROM`               Selects the base Python image
  `WORKDIR`            Sets the working directory
  `COPY`               Copies files into the image
  `RUN`                Installs dependencies
  `CMD`                Defines the application startup command

### Build the image

Open the terminal inside:

``` text
CH-6_MCP_Docker
```

Then run:

``` bash
docker build -t mcp_gateway .
```

### Run the container

``` bash
docker run --rm mcp_gateway
```

### Docker workflow

``` text
gateway.py
    ↓
requirements.txt
    ↓
Dockerfile
    ↓
docker build
    ↓
Docker Image
    ↓
docker run
    ↓
Running Container
```

### Goal

Learn how to package the MCP Gateway and its dependencies into a Docker
container so that the application can run in an isolated and
reproducible environment.

------------------------------------------------------------------------

# 🔌 MCP Client Architecture

Across the chapters, the basic MCP client workflow is:

``` text
                 MCP Server
                     │
                     │
                  Transport
                     │
                     ▼
                 MCP Client
                     │
                     ▼
              Discover Tools
                     │
                     ▼
                Call Tools
                     │
                     ▼
                Get Result
```

For a low-level MCP client, the session is initialized before requesting
server tools:

``` python
await session.initialize()
tools = await session.list_tools()
```

------------------------------------------------------------------------

# 🔗 LangChain + MCP

The project also explores connecting MCP with LangChain.

One client approach uses:

``` python
from langchain_mcp_adapters.client import MultiServerMCPClient
```

A client can configure MCP servers and discover their tools.

Example structure:

``` python
client = MultiServerMCPClient(
    {
        "agentic_terminal": {
            "transport": "stdio",
            "command": "uvx",
            "args": ["agentic_terminal"]
        }
    }
)
```

Then:

``` python
tools = await client.get_tools()
```

This allows MCP tools to be exposed to a LangChain-based application.

------------------------------------------------------------------------

# ⚠️ Dependency Compatibility

During the MCP journey, dependency compatibility is an important
practical lesson.

MCP-related packages may require different versions of the `mcp`
package. For example, a package using MCP 2.x may not be compatible with
an older `langchain-mcp-adapters` release that expects MCP 1.x.

A version mismatch can produce errors such as:

``` text
ImportError: cannot import name 'RequestContext' from 'mcp.shared.context'
```

When this happens:

1.  Check the package requirements.
2.  Check the installed MCP version.
3.  Use compatible package versions.
4.  Consider a separate virtual environment when two projects require
    incompatible dependency versions.

This is an important part of real-world Python and MCP development.

------------------------------------------------------------------------

# 📦 Python Environment

The project contains:

``` text
.venv/
```

for the Python virtual environment.

The project also contains:

``` text
pyproject.toml
uv.lock
```

which are used for Python project and dependency management.

Useful commands:

### Check Python

``` bash
python --version
```

### Check uv

``` bash
uv --version
```

### Create virtual environment

``` bash
uv venv
```

### Activate on Windows PowerShell

``` powershell
.venv\Scripts\Activate.ps1
```

### Install a package

``` bash
uv pip install <package-name>
```

### Check a package

``` bash
uv pip show <package-name>
```

------------------------------------------------------------------------

# 🐳 Docker Commands

### Build

``` bash
docker build -t mcp_gateway .
```

### Run

``` bash
docker run --rm mcp_gateway
```

### List Docker images

``` bash
docker images
```

### List running containers

``` bash
docker ps
```

### List all containers

``` bash
docker ps -a
```

------------------------------------------------------------------------

# 🧩 Technologies Used

  Technology               Purpose
  ------------------------ ----------------------------------------------
  Python                   Main programming language
  MCP                      Tool/context communication protocol
  FastMCP                  Building MCP servers
  LangChain                AI application integration
  LangChain MCP Adapters   Connecting MCP tools with LangChain
  PyPI                     Python package distribution
  uv                       Python environment and dependency management
  Docker                   Containerization

------------------------------------------------------------------------

# 🎯 Complete Learning Progression

### Stage 1 --- Understand MCP

``` text
Create MCP Server
        ↓
Create Python Client
        ↓
Connect Client to Server
```

### Stage 2 --- Understand HTTP

``` text
MCP Server
    ↓
HTTP Transport
    ↓
Client
```

### Stage 3 --- Reuse Existing MCP

``` text
Third-Party MCP
       ↓
Integration
       ↓
Application
```

### Stage 4 --- Package MCP

``` text
MCP Project
    ↓
Python Package
    ↓
PyPI
    ↓
Install
    ↓
Client
```

### Stage 5 --- Gateway Architecture

``` text
             MCP Server
                  ↑
MCP Server ← Gateway → MCP Server
                  ↑
                Client
```

### Stage 6 --- Containerization

``` text
MCP Gateway
    ↓
Dockerfile
    ↓
Docker Image
    ↓
Docker Container
```

------------------------------------------------------------------------

# 🧠 Key Concepts Learned

By completing this journey, the project covers:

-   MCP fundamentals
-   MCP servers
-   MCP clients
-   MCP tools
-   Stdio transport
-   HTTP transport
-   Python MCP clients
-   LangChain MCP clients
-   Third-party MCP
-   Community MCP tools
-   PyPI packages
-   Python package installation
-   MCP Gateway architecture
-   Dependency management
-   Virtual environments
-   Docker images
-   Docker containers
-   Containerized MCP applications

------------------------------------------------------------------------

# 🚀 Final Outcome

This project represents a progressive MCP learning journey:

``` text
Basic MCP
   ↓
MCP Client
   ↓
HTTP MCP
   ↓
Third-Party MCP
   ↓
PyPI MCP Package
   ↓
MCP Gateway
   ↓
Dockerized MCP Gateway
```

The journey starts with understanding the basic **MCP server-client
model** and gradually moves toward more practical software architecture
involving **HTTP communication, reusable third-party tools, package
distribution, gateways, dependency management, and Docker deployment**.

------------------------------------------------------------------------

## 👨‍💻 Project Information

``` text
Project Name : MCP_Server_Tuto
Language      : Python
Protocol      : Model Context Protocol (MCP)
Frameworks    : FastMCP, LangChain
Package Tool  : PyPI
Environment   : uv / Python virtual environment
Deployment    : Docker
```
