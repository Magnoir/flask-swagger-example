
# API Example

A simple API built with Flask and Flask-RESTX. This API allows you to manage a collection of `items` through RESTful endpoints. Swagger documentation is also available for easy usage.

## Features

- **List items**: Retrieve all available items.
- **Add an item**: Create a new item with an `id` and a `name`.
- **Get an item**: Fetch a specific item by its `id`.
- **Delete an item**: Remove an item by its `id`.

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Magnoir/flask-swagger-example.git
   cd flask-swagger-example
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the Flask app using:
```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000/`, and the Swagger documentation can be accessed at `http://127.0.0.1:5000/docs`.

## Usage

### Endpoints

- **GET /items/**: List all items.
- **POST /items/**: Add a new item.
- **GET /items/<int:id>**: Get an item by its `id`.
- **DELETE /items/<int:id>**: Delete an item by its `id`.

## Example JSON for `data.json`

```json
[
    {
        "id": 1,
        "name": "Chair"
    },
    {
        "id": 2,
        "name": "Table"
    },
    {
        "id": 3,
        "name": "Lamp"
    }
]
```