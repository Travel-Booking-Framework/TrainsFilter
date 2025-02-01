# TrainsFilter

## Introduction

**TrainsFilter** is a core microservice of the **Travel-Booking-Framework** that provides an advanced search and filtering system for Trains. This service is developed using **Django** and **Elasticsearch**, allowing for fast and efficient Train searches based on multiple criteria.

## Features

- **Train Search**: Search Trains based on origin, destination, date, and other parameters.
- **Advanced Filters**: Filter Trains by price, duration, departure time, and other factors.
- **Train Management**: Add, update, and delete Train information.

## Prerequisites

- **Python 3.x**
- **Django**
- **Elasticsearch**

## Installation and Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Travel-Booking-Framework/TrainsFilter.git
   cd TrainsFilter
   ```

2. **Create and Activate a Virtual Environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use: venv\\Scripts\\activate
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Setup Elasticsearch**: Ensure that **Elasticsearch** is installed and running on your system. Update the Django settings (`settings.py`) with the correct Elasticsearch configuration.


## Project Structure

- **TFilter/**: Contains the core settings and configurations for Django.
- **TrainsFilter/**: Manages Train-related operations and filtering functionalities.
- **Class-Diagram/**: Provides class diagrams for understanding the project architecture.
- **logs/**: Contains logs files.

## Contribution Guidelines

We welcome contributions from the community! To contribute:

1. **Fork** the repository.
2. **Create a new branch** for your feature or bug fix.
3. **Commit** your changes.
4. **Submit a Pull Request**.


## Additional Notes

- **Create a Superuser**: To create an admin account, use the command:
  ```bash
  python manage.py createsuperuser
  ```

- **GraphQL Support**: This project includes GraphQL capabilities, which can be accessed at `/graphql/`.