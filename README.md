# Project Setup and Authentication Guide

## Setup Virtual Environment

1. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

2. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

## Install Requirements

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Database Migrations

4. **Make migrations**:
    ```sh
    python manage.py makemigrations
    ```

5. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

## Create Superuser

6. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```
   Follow the prompts to set up your superuser account.

## Obtain Authentication Token

7. **Start the Django development server**:
    ```sh
    python manage.py runserver
    ```

8. **Obtain an authentication token**:
    ```sh
    curl -X POST -d "username=<username>&password=<password>" http://127.0.0.1:8000/api-token-auth/
    ```
   Replace `<username>` and `<password>` with your superuser credentials. This command will return a token if the credentials are correct.

## Use the Authentication Token

9. **Pass the token in the header for authenticated requests**:
    - Using Postman:
      - In the request headers, add a key `Authorization` with the value `Token <your_token>`.
    - Using curl:
      ```sh
      curl -H "Authorization: Token <your_token>" http://127.0.0.1:8000/api/events/
      ```
    Replace `<your_token>` with the token obtained from the previous step.

## Example Request Using Token
**Example request to fetch events**:

```sh
curl -H "Authorization: Token 5e029ecc190f16cbbb3fd3b9db4731b86f933d7c" http://127.0.0.1:8000/api/events/
```
    
Replace `5e029ecc190f16cbbb3fd3b9db4731b86f933d7c` with your actual token obtained from step 8.
