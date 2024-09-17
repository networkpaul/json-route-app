# Flask JSON UI

This repository provides a Flask application for interacting with JSON data through a web interface.

## Getting Started

### Prerequisites

Make sure you have Docker and Docker Compose installed on your machine. You can download and install Docker from [Docker's official website](https://www.docker.com/get-started).

### Running the Application

To get started, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/networkpaul/json-route-app.git
   cd json-route-app.git
   ```

2. Start the Application with Docker Compose:

    ```bash
   docker-compose up -d
   ```

This command will start the Flask application in detached mode.

3. Point your domain to the server:

Ensure your domain is pointed to the server where the Flask application is running, and the server is accessible on the port you specified in the `.env` file. By default, the application is running on port 5000.

4. Access the application:

Open your web browser and navigate to:

```arduino
http://your-domain-or-ip:5000
```

> Note: Replace `your-domain-or-ip` with your actual domain or IP address. If you change the port, replace `5000` with the appropriate port number.

5. Enter valid JSON:

Once you access the application, you will be prompted to enter valid JSON data. Input your JSON and interact with the application as needed.

## Local Development

If you want to run the application locally, you can use Docker Compose to build and run the application in a container.

1. Start the Application with Docker Compose:

    ```bash
   docker-compose -f docker-compose.local.yml up -d --build
   ```
   
> Note: This command will build the Docker image and start the application in detached mode. The FLASK_PORT can still be changed in the .env file. By default, the application is running on port 5000.

## Example Usage

- Visit the application at `http://your-domain-or-ip:5000`.
- Enter your JSON data into the provided input field.
- Submit and view the results.

## Troubleshooting

- **If the application does not start:** Ensure Docker and Docker Compose are correctly installed and running.
- **If you encounter issues:** Check the logs using `docker-compose logs` for more details.

## License

This project is licensed under the [MIT License](LICENSE).





