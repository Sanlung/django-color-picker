<p align="center"><img width="100" src="./img/avatar.png" /></p>
<h2 align="center">Chung Kao's</h2>
<h4 align="center">Color Picker Django Project</h4>
<p align="center">Columbia University - Justice Through Code</p>
<p align="center"><img width="600" src="./img/jtc_site_screenshot.png" /></p>

## About

This is a simeple Django app that lets the user set the background color of the page by picking a rgb color with the form provided. It is created to fulfill a project requirement for the Columbia University's Justice Through Code, Spring 2022 program. Participants of JTC undergo an intensive of Python programming and app development using the Django framework. This is the second of the Django projects that will have been completed before the final project and before participants move on to the career development phase of the program.

### Usage

To clone a copy of this project using https, run the following command in the command line:

```bash
$ git clone https://github.com/Sanlung/django-color-picker.git <your_project_directory_name>
```

To clone using SSH run the following command:

```bash
$ git clone git@github.com:Sanlung/django-color-picker.git <your_project_directory_name>
```

In the same directory as `<your_local_project_name>/colorpicker/colorpicker/settings.py` file, create a `.env` file and, in it, save a secret key that you create. You may generate a key in the terminal like so:

```bash
$ shasum<<<test
```

A hash will be generated and printed to the terminal, which you can use as the key and save it in the `.env` file, like so:

```.env
SECRET_KEY=<the_hash_you_generated>
```

Create a Python virtual environment and activate it in your local project: (assuming you already have Python installed)

```bash
$ cd <your_local_project_directory_name>
$ python3 -m venv venv
$ . venv/bin/activate
```

Install the packages from `requirements.txt`:

```bash
$ pip install -r requirements.txt
```

In the `colorpicker/` directory run the following command to start the server:

```bash
$ cd colorpicker
$ python3 manage.py runserver
```

And you can take the app further with your own tweaks. The steps in the above are for Mac and Linux users. Please look up online for equivalent commands for Windows machines.

### Author

[![Chung Kao](./img/Chung_button.svg)](https://github.com/Sanlung)
