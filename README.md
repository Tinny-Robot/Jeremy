# Project Name

Brief description of your project.

#

## API Documentation

### Endpoint: `/predict`

#### Method: POST

- **Description**: Endpoint for making predictions.

- **Request Body**:
  - **Type**: form-data
  - **Key**: file
  - **Value**: Image file to be predicted.

- **Responses**:
  - **200 OK**:
    - **Content-Type**: text/plain
    - **Body**: Predicted class.
    - **Example**: `Predicted Class: Glioblastoma`
  
  - **400 Bad Request**:
    - **Content-Type**: application/json
    - **Body**: `{"error": "File not found."}`

    - **Example**: 
      ```json
      {
        "error": "File not found."
      }
      ```

    - **Description**: Returned if the file is not found in the request.

    - **Body**: `{"error": "Invalid file format."}`

    - **Example**: 
      ```json
      {
        "error": "Invalid file format."
      }
      ```

    - **Description**: Returned if the file format is not supported.

    - **Body**: `{"error": "Internal Server Error."}`

    - **Example**: 
      ```json
      {
        "error": "Internal Server Error."
      }
      ```

    - **Description**: Returned if there is an internal server error.

## Author

- **Name**: Nathaniel Handan
- **Email**: handanfoun@gmail.com
