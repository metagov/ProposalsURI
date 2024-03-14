
# Flask API for Proposals URI via Boardroom

This Flask application serves as an API to fetch and display proposals from the Boardroom platform based on the network and ID parameters provided by the user. It showcases how to integrate external APIs securely using environment variables for API keys.

## Features

- Fetch proposals from Boardroom based on network and ID.
- Secure API key management using environment variables.
- Basic API documentation served at the root endpoint.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.6+
- pip
- A Boardroom API key

## Installation

Clone this repository to your local machine:

```bash
git clone https://your-repository-url.git
cd your-repository-directory
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the root directory of your project and add your Boardroom API key:

```
BOARDROOM_KEY=your_api_key_here
```

Make sure to replace `your_api_key_here` with your actual Boardroom API key.

## Running the Application

To run the application, use the following command:

```bash
flask run
```

The API will be available at [http://localhost:5000](http://localhost:5000).

## Usage

The API provides endpoints to fetch Boardroom proposals. Here are some example requests you can make:

```
GET /api/v1/boardroom/proposals/{network}/{id}
```

Replace `{network}` and `{id}` with the appropriate values.

## Contributing

To contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).



