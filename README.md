# Flask Chatbot Application

This project is a Flask-based chatbot application that interacts with a backend API to generate responses based on user prompts. The application maintains a conversation history and displays it on a web page.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Endpoints](#endpoints)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/flask-chatbot.git
    cd flask-chatbot
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Ensure the backend API is running:**

    Make sure the backend API that generates responses is running on `http://localhost:11434/api/generate`.

5. **Run the Flask application:**

    ```bash
    python app.py
    ```

    The application will be accessible at `http://127.0.0.1:5000`.

## Usage

1. Open your web browser and go to `http://127.0.0.1:5000`.

2. Enter a prompt in the input field and click "Submit" to receive a response from the chatbot.

3. The conversation history will be displayed on the web page.

4. To clear the conversation history, click the "Clear" button.

## Endpoints

### `/`

- **Method:** GET, POST
- **Description:** Renders the main page of the chatbot application. Handles user prompts and displays the conversation history.

### `/clear`

- **Method:** POST
- **Description:** Clears the conversation history.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
