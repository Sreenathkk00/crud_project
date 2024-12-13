# CRUD Operations - Django Project



https://github.com/user-attachments/assets/58de9b4b-2e90-48cf-b5e4-472cd568adcb


This project demonstrates a simple implementation of CRUD (Create, Read, Update, Delete) operations using Python Django, HTML, CSS, and Bootstrap 5. The application allows users to manage a collection of items, performing basic operations such as creating new items, viewing details, updating existing entries, and deleting records.

## Technologies Used
- **Python Django:** Backend framework used to handle server-side logic and database operations.
- **HTML:** Used for structuring the web pages in the project.
- **CSS:** Provides styling for a visually appealing user interface.
- **Bootstrap 5:** Front-end framework for designing responsive and modern web applications.

## Features
- **Create:** Users can add new items to the collection by filling out a form.
- **Read:** Displays a list of items with details, allowing users to view information.
- **Update:** Edit existing entries to update information as needed.
- **Delete:** Remove items from the collection.

## Project Structure
- **/details_app:** Django app directory for the CRUD operations.
- **/templates:** Contains HTML templates for rendering the views.
- **/static:** Contains CSS and Bootstrap files for styling.

## Class-Based Views
This project uses Django's class-based views to manage CRUD operations:
- **CreateView:** Handles the creation of new items.
- **ListView:** Displays a list of all items in the collection.
- **UpdateView:** Allows updating of existing items.
- **DeleteView:** Enables deletion of items.



## Getting Started

### 1. Clone the Repository:

    git clone https://github.com/sreenath-pydev/crud_operations
    
    cd crud_operations

### 2. Set Up the Virtual Environment:

 Create a virtual environment to manage project dependencies:

    python -m venv venv


Activate the virtual environment:

- Windows:

      venv\Scripts\activate
- macOS/Linux:

      source venv/bin/activate
### 3. Install Dependencies:
Once the virtual environment is activated, install the required dependencies:

    pip install -r requirements.txt


## Database Setup

### Option 1: Using PostgreSQL Database

If you prefer to use PostgreSQL, follow these steps to configure it:

#### 1. Install PostgreSQL:
Ensure you have PostgreSQL installed and running on your machine. You can download it from [the official PostgreSQL website](https://www.postgresql.org/download/).

#### 2. Create a Database:
Once PostgreSQL is installed, create a new database for the project:

    psql -U postgres
    CREATE DATABASE crud_operations;
#### 3. Configure Database in Django:
In your settings.py, configure the DATABASES section to use PostgreSQL:

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'crud_operations',
                'USER': 'username', # Add Your your_postgres_username
                'PASSWORD': 'password', # Add Your your_postgres_password
                'HOST': 'localhost',
                'PORT': '5432',
            }
        }
#### 4. Install PostgreSQL Dependencies:
You need to install psycopg2 to connect Django to PostgreSQL:

    pip install psycopg2
### Option 2: Using Default SQLite Database
If you choose to use the default database (SQLite), Django automatically uses it without requiring any additional configuration. The default settings in settings.py are sufficient to run the application with SQLite.


    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / "db.sqlite3",
        }
    }
#### 5. Migrations:
Initial Migration:
After configuring your database, run the migrations to set up the database schema:


    python manage.py migrate
Creating Superuser (Optional):
You can create a superuser to access the Django admin interface:


    python manage.py createsuperuser
### 6. Run the Application: 
    python manage.py runserver
### 7. Access the Application:
Open your web browser and navigate to http://localhost:8000 or http://127.0.0.1:8000/.

### Usage
1. Use the "Create" button to add new entries.  

2. Navigate to the homepage to view the list of items. 

3. For editing and deleting, use the "Advanced" dropdown button located on each item's card.
### Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

### License
This project is licensed under the [MIT License](LICENSE)

