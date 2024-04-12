# AirBnB Clone - Tests

This directory contains tests for the AirBnB clone application. Each module represents a different aspect or component being tested.

## Contents

- **[test_console.py](test_console.py):** Module containing tests for the application's console functionality.
- **[__init__.py](./__init__.py):** Initialization file indicating this directory is a Python package.
- **[test_models](test_models):** Directory containing tests for the application's models

### Subdirectory: test_models

The `test_models` subdirectory contains tests for the application's models.

#### Contents

- **[test_amenity.py](test_models/test_amenity.py):** Module with tests for the Amenity model.
- **[test_base_model.py](test_models/test_base_model.py):** Module with tests for the BaseModel class, the base class for all data models.
- **[test_city.py](test_models/test_city.py):** Module with tests for the City model.
- **[test_place.py](test_models/test_place.py):** Module with tests for the Place model.
- **[test_state.py](test_models/test_state.py):** Module with tests for the State model.
- **[test_review.py](test_models/test_review.py):** Module with tests for the Review model.
- **[test_user.py](test_models/test_user.py):** Module with tests for the User model.
- **[__init__.py](test_models/__init__.py):** Initialization file indicating this directory is a Python package.
- **[test_engine](test_engine):** Directory containing tests related to the application's data storage engine.
- **[__pycache__](test_models/__pycache__):** Directory containing cached bytecode files (generated automatically by Python).

### Subdirectory: test_engine

The `test_engine` subdirectory contains tests related to the application's data storage engine.

#### Contents

- **[__init__.py](test_engine/__init__.py):** Initialization file indicating this directory is a Python package.
- **[test_db_storage.py](test_engine/test_db_storage.py):** Module with tests for database storage functionality.
- **[test_file_storage.py](test_engine/test_file_storage.py):** Module with tests for file storage functionality.
- **[__pycache__](test_engine/__pycache__):** Directory containing cached bytecode files (generated automatically by Python).
