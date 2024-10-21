# Mist 2 - Game Platform

Mist 2 is a game platform that allows you to create, delete, and edit your games. You can post your games for others to see, and users have the option to "buy" them.

## Prerequisites

Before running this project, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)

## Getting Started

1. Clone this repository:

```bash
git clone https://github.com/FREDYKRUGE/Mist2.git
cd Mist2
```
Make Changes to docker-compose.yml:
In the docker-compose.yml file, you may need to make the following changes based on your environment:

Modify database credentials if needed to ensure proper connection to your database server.
Important: Change the context of the web service to the desired folder where you want the project to live. This should be the absolute path to your project directory.
Setting Up Virtual Environment:
It's highly recommended to set up a virtual environment for your Python dependencies to keep the project isolated. Follow these steps:

bash
Copy code
# Install virtualenv if you haven't already
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
# (On Windows)
venv\Scripts\activate
# (On macOS/Linux)
source venv/bin/activate
Building and Running the Docker Containers:
Now, build and run the Docker containers using the following commands:

bash
Copy code
docker-compose build
docker-compose up
Accessing the Platform:
Once the Docker containers are up and running, you can access the platform in your web browser at http://localhost:8000/.

# Features
Create, delete, and edit your games on the platform.
Publish your games for other users to see and potentially "buy" them.

# License
GNU General Public License v3.0

# Acknowledgments
This project wouldn't have been possible without the contributions of the open-source community and the developers behind the following libraries and dependencies:

Ansicon - Version 1.89.0
Asgiref - Version 3.6.0
Attrs - Version 20.3.0
Autopep8 - Version 2.0.1
Blessed - Version 1.19.1
Certifi - Version 2022.12.7
Cffi - Version 1.15.1
Charset-normalizer - Version 3.0.1
Cryptography - Version 39.0.0
Cursed - Version 0.2.1
Cython - Version 3.0.0
Distlib - Version 0.3.6
Django - Version 4.1.5
Filelock - Version 3.9.0
Gevent - Version 22.10.2
Greenlet - Version 2.0.1
Idna - Version 3.4
Jellyfish - Version 0.9.0
Jinxed - Version 1.2.0
Markdown - Version 3.4.1
Markdown2 - Version 2.4.7
Pexpect - Version 4.8.0
Pillow - Version 9.4.0
Platformdirs - Version 2.6.2
Psycopg2 - Version 2.9.6
Psycopg2-binary - Version 2.9.6
Ptyprocess - Version 0.7.0
Pycodestyle - Version 2.10.0
Pycparser - Version 2.21
Pyperclip - Version 1.8.2
Requests - Version 2.28.2
Six - Version 1.16.0
Sqlparse - Version 0.4.3
Termcolor - Version 1.1.0
Tomli - Version 2.0.1
Tzdata - Version 2022.7
Urllib3 - Version 1.26.14
Virtualenv - Version 20.17.1
Wcwidth - Version 0.2.5
Zope.event - Version 4.6
Zope.interface - Version 5.5.2
Thank you to all the developers and contributors who have worked on these fantastic projects, enabling us to create Mist 2 and build upon your exceptional work.

# Contact
email: litovmomchil@gmail.com
