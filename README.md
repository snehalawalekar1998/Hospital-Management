# Microservices Platform for Hospital Solutions
**Snehal Awalekar, Bhavna Gupta, Abhilash Chaudhary**

## Objective
The objective of this project is to develop a **microservices-based Hospital Management System** that streamlines key hospital functions such as patient registration, appointment scheduling, billing, and doctor-patient communication. Leveraging a client-server architecture, each service operates independently for scalability and modularity. Containerized using **Docker** and orchestrated via **Docker Compose**, the system is designed for efficient data handling, seamless scaling, and high availability. With cloud connectivity for real-time collaboration, this innovative solution enhances operational efficiency and patient care, setting a new standard for modern healthcare systems.

## Features
- **Doctor Service**: Manage doctor information, including specialties, availability, and updates.
- **Patient Service**: Manage patient information including registration, updates, and retrieval of medical records.
- **Appointment Service**: Facilitate scheduling, canceling, and managing doctor appointments.
- **Billing Service**: Manage patient billing and track payments.

## Technology Stack
- **Flask**: Python web framework for creating REST APIs for the services.
- **SQLAlchemy**: Database management for handling data models and operations.
- **SQLite**: Lightweight database for storing service data.
- **Docker**: Containerization for services.
- **Docker Compose**: Service orchestration and management.

## Prerequisites
- **Docker**: Ensure Docker is installed and running.
- **Docker Compose**: To orchestrate the microservices.

## Setup Instructions

### Installation
1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the project directory**:
    ```bash
    cd hospital-management-main
    ```

3. **Build and start all services using Docker Compose**:
    ```bash
    docker-compose up --build
    ```

4. **Access the services at their respective endpoints**.

### How to Run the Project
The **Hospital Management System** is structured as independent microservices that communicate through HTTP APIs. Each service manages its respective database using **SQLite** and exposes RESTful endpoints to other services. **Docker Compose** handles service orchestration, making it easy to scale, maintain, and deploy the system in different environments.

### Services Endpoints
- **Patient Service**: `http://localhost:5001`
- **Doctor Service**: `http://localhost:5002`
- **Appointment Service**: `http://localhost:5003`
- **Billing Service**: `http://localhost:5004`

## Scalability and Upcoming Improvements
- **Horizontal scaling**: To accommodate increasing workloads, each service can be scaled separately.
- **Security Enhancements**: To improve security, include authorization and authentication methods (like OAuth).

## Conclusion
This project demonstrates a modular and scalable approach to hospital management, leveraging the power of microservices architecture, **Docker**, and **Flask** for improved patient care and operational efficiency.

