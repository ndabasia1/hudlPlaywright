# hudlPlaywright

## Getting started

1. **Clone the Repository**:

2. **Create a Virtual Environment**:
    Navigate to where the repo is stored and activate a virtual environment. The below is how to activate it through command prompt.
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install requirement.txt dependencies**:
    All dependencies used for this project can be found in the requirement.txt file. The main dependencies are pytest, pytest-playwright, pytest-html and python-dotenv.
    ```sh
    pip install -r requirements.txt
    ```

4. **Set-up tests - IMPORTANT**:
    In order for the tests to run correctly, a valid email and password needs to be added to the .env file. EMAIL= and PASSWORD= needs to be filled in otherwise the tests will not pass.

5. **Run tests**
    - Once the necessary information has been entered within the .env file, to run a test through the command line, ensure you are in the root of the repo and then run
    ```sh
    pytest
    ```
      and this will run all files that start with test_
    - To run a specific test within the test file, 
    ```sh
    pytest tests/login/test_login.py::[test_name]
    ```
    - To run through VS Code, hover over the function name found within the test_login.py file and you will have the option to run a test

## Project Structure
- `.env`: Important environment details which needs to be pre-filled
- `config/`: Constants and config set-up is stored here
- `pages/`: POM pattern is followed to store elements and methods
- `tests/`: tests are stored here