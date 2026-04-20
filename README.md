CLI Expense Tracker: Labor and Materials

A lightweight Command Line Interface (CLI) application designed for real-time tracking of project expenditures. This tool allows users to log expenses for labor and materials, ensuring data persistence through JSON serialization and automated temporal logging.
## Project Overview

In the lifecycle of any technical project, managing resources efficiently is as critical as the development itself. This script provides a structured environment to:

    Log Entries: Input costs dynamically during runtime.

    Automate Timestamps: Utilize system clocks for precise data auditing.

    Persistent Storage: Transition from volatile memory to non-volatile storage using the JSON format.

    Data Aggregation: Calculate total overhead across different categories.

## Technical Architecture

The application is built on a modular logic flow, mirroring basic CRUD (Create, Read, Update, Delete) operations found in more complex database systems.
### Core Logic Flow

The program utilizes a while loop to maintain an active state, processing user input through a series of conditional gates.
### Data Structure

Individual records are encapsulated in Dictionaries, which are then aggregated into a List. This mimics a table-like structure common in data science and AI preprocessing.
Python

{
    "timestamp": "2026-04-05 19:30:00",
    "category": "Labor",
    "amount": 1500.00,
    "description": "Senior Developer hourly rate"
}

## Key Modules & Research Areas
### 1. Data Persistence (json)

Standard variables in Python reside in RAM and are cleared upon process termination. To maintain a history of expenses, we implement the json module:

    json.dump(): Serializes the list of dictionaries into a .json file.

    json.load(): Deserializes the file back into Python objects upon script execution.

### 2. Temporal Logic (datetime)

To ensure data integrity, every entry is automatically stamped using datetime.now(). This removes human error and provides a chronological trail for future data analysis or visualization.
## Setup and Execution

    Clone the Repository:
    Bash

    git clone https://github.com/your-username/expense-tracker-cli.git

    Navigate to Directory:
    Bash

    cd expense-tracker-cli

    Run the Script:
    Bash

    python main.py

## Future Roadmap

    Data Visualization: Integration with matplotlib or pandas to generate expenditure graphs.

    Export Functionality: Capability to export logs to CSV for integration with larger financial models.

    Search and Filter: Implement algorithms to query specific date ranges or high-value transactions.
