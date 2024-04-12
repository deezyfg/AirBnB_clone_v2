# AirBnB Clone - Models

This directory contains the models used in the AirBnB clone application. Each module represents a different entity or aspect within the application.

## Contents

- [amenity.py](amenity.py): Module defining the Amenity class, which represents amenities available in accommodations.
- [city.py](city.py): Module defining the City class, which represents cities where accommodations are located.
- [state.py](state.py): Module defining the State class, which represents states or regions where accommodations are located.
- [place.py](place.py): Module defining the Place class, which represents individual accommodations available for rent.
- [review.py](review.py): Module defining the Review class, which represents reviews left by users for accommodations.
- [user.py](user.py): Module defining the User class, which represents users of the application.
- [__pycache__](engine/__pycache__): Directory containing cached bytecode files (generated automatically by Python).

### Base Model

- [base_model.py](./base_model.py): Module defining the BaseModel class, which serves as the base class for all other data models. It provides common attributes and methods shared by all models.

## Subdirectory: Engine

The `engine` subdirectory contains modules responsible for managing data storage and retrieval.

### Contents

-[db_storage.py](engine/fdb_storage.py): Module provides functionality for managing data storage using a database.
- [file_storage.py](engine/file_storage.py): Module defining the FileStorage class, which provides methods for storing and retrieving data models using JSON files.
- [__init__.py](engine/__init__.py): Initialization file indicating that the `engine` directory is a Python package.
- [__pycache__](engine/__pycache__): Directory containing cached bytecode files (generated automatically by Python).