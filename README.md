## Celery Basics Project

This project is designed to provide a basic understanding of Celery, a distributed task queue framework for Python. It serves as a teaching tool to help students grasp the fundamental concepts and usage of Celery.

## Prerequisites

Before getting started with this project, ensure that you have the following prerequisites:

1. Python 3.x installed on your machine
2. pip package manager

## Getting Started

To set up the project and run Celery tasks locally, follow these steps:

1. Clone the repository:
   ```sh
   git clone <repository-url>
   ```

2. Change to the project directory:
   ```sh
   cd celery-basics-project
   ```

3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Start the Celery worker:
   ```sh
   celery -A app_name worker --loglevel=info
   ```

## Usage

This project provides a simple example of a Celery task that calculates the sum of two numbers. The task is defined in the `tasks.py` file, and the calculation logic resides in the `add_numbers` function. To execute this task, follow these steps:

1. In a Python script or interactive shell, import the add_numbers task:
   ```py
   from tasks import add_numbers
   ```

2. Submit the task with two numbers as arguments:
   ```py
   result = add_numbers.delay(5, 10)
   ```
   The delay method asynchronously schedules the task for execution and returns a AsyncResult object.

3. To retrieve the result of the task, call the get method on the AsyncResult object:
   ```py
   print(result.get())
   ```
   This will print the sum of the two numbers.

## Folder Structure

The project has the following folder structure:

```
.
├── celery.py
├── tasks.py
├── README.md
└── requirements.txt

```

  `tasks.py`: Contains the Celery task definition.
  `README.md`: Provides instructions and information about the project.
  `requirements`.txt: Lists the dependencies required by the project.

## Resources

To learn more about Celery, refer to the official documentation:

Celery Documentation: https://docs.celeryproject.org/

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

Special thanks to the creators and contributors of Celery for providing such a powerful and useful task queue framework