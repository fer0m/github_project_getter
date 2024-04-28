# GitHub Projects Getter

## Description
This Django web application is designed to search for and display GitHub repositories. It offers functionality for searching repositories by programming language and other criteria through a user-friendly web interface and a REST API.

## Key Features
- **Repository Search**: Users can search for repositories by programming language and other filters. The search returns results with essential information about each repository, such as the link, star count, description, etc.
- **Repository Listing**: Displays a list of all repositories, sorted by star count.
- **REST API**: The API provides access to the search functionality and retrieves data about the repositories, allowing for integration into other applications or services.
- **Administration**: Integration with the Django admin interface for managing repository data.

## Technologies
- **Django**: The primary web application framework, providing routing, view control, and templating.
- **Django REST Framework**: Used for creating API endpoints.
- **SQLite**: Database for storing repository information.

## Getting Started
To get a local copy up and running follow these simple steps.

### Prerequisites
- Python 3.8+
- pip
- Virtualenv (recommended)

### Installation

You have two options for setting up the environment: using Docker (recommended for its simplicity) or setting up manually.

### Option 1: Using Docker (Recommended)
Using Docker simplifies the setup process and eliminates the need for manual configuration of the environment and dependencies. Here’s how you can get started:

1. Clone the repo
   ```bash
   git clone https://github.com/fer0m/github_project_getter.git
   
2. Navigate to the project directory
   ```bash
   cd github_project_getter
    ```
   
3. Build and run the Docker containers
   ```bash
   docker-compose up --build
    ```

### Option 2: Manual Setup
If you prefer not to use Docker, follow these steps to set up the environment manually:


1. Clone the repo
   ```bash
   git clone https://github.com/yourusername/github-project-getter.git
    ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate
    ```

3. Install required packages
   ```bash
   pip install -r requirements.txt
    ```

4. Run migrations
   ```bash
   python manage.py migrate
    ```

5. Start the development server
   ```bash
   python manage.py runserver
    ```