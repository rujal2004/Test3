# AI Chat System - Django REST API

#### Overview

This project implements REST APIs for an AI chat system using Django. Users can:

Register with a unique username and password

Login and receive an authentication token

Send messages to the AI chatbot (dummy responses for simplicity)

Track token usage (100 tokens per chat) and view remaining tokens

All functionalities are demonstrated with Postman test cases.

## Installation & Setup

#### Clone the repository:

git clone https://github.com/rujal2004/Test3.git
cd Test3

Create and activate virtual environment:

python -m venv venv
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


Apply migrations and start server:

python manage.py migrate
python manage.py runserver

#### API Testing

All APIs have been tested using Postman.

Screenshots for each API request and response are saved in the Postmanimages folder.
