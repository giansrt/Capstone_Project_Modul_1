# Rental Vehicle Management System

This project is a rental vehicle management system implemented in Python. It allows users to interact with a database of vehicles, manage rentals, and perform administrative tasks. The system provides both a command-line interface for interaction and leverages tabulate for data presentation.

## Features

- **User Authentication:**
  - Supports login and registration for both users and an admin.
  - User roles (admin and user) determine access privileges within the system.

- **Vehicle Management:**
  - Add new vehicles with details such as brand, model, stock, wheels, and price.
  - View available vehicles sorted by the number of wheels (4 wheels and 2 wheels).

- **Rental Functionality:**
  - Users can rent available vehicles, specifying the start and end dates for the rental period.
  - The system calculates rental costs based on the number of days and the number of vehicles rented.

- **Admin Functions:**
  - Administrators have additional privileges such as deleting vehicles, updating stock or prices, and managing rental data.
  - Admins can also view all rental data and delete user rental records.

- **Data Display:**
  - Utilizes tabulate library to display data in a formatted table for clear presentation.

## Flowchart
Before looking at the implementation details and features of the Rental Vehicle Management system, let's take a look at the flowchart that illustrates the main processes of this system.The following flowchart provides a visual representation of how users can interact with the system, from user authentication to vehicle management and loaning process.This diagram will help you understand the overall workflow of the system before further exploring the features provided by the application.
![Flowchart](https://github.com/giansrt/Capstone_Project_Modul_1/blob/main/Diagaram/gambar/main.png)
## Requirements

- Python 3.12.2
- tabulate library [install via `pip install tabulate`]

## Installation

### Clone the Repository:

```bash
git clone [https://github.com/giansrt/Capstone_Project_Modul_1.git]
