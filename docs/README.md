# Structure

### Problem Definition and Stakeholders

The stakeholders of my application will be **fellow students of Loreto Sixth Form College**.
Being A Level students, they need to organize revision sessions, in order to maintain the grades
required for their chosen university. Many Loreto college students have issues with organising a
revision timetable.
For example, creating study sessions that do not clash with classes, or setting up
reminders for each of these study sessions. The needs of a College student also include regularly
checking up on their performance
(grades, attendance) to ensure that they are making the best of their study periods. <br>

I have chosen a fellow Computer Science student, Troy Sherlock, to be my stakeholder for this
project. Troy is an ideal candidate for my software, as he is currently in his second year of A
Levels with Maths, Physics and Computer Science. This means that efficient organisation of free
study periods is vital, so he will benefit greatly from my solution.

The current system for achieving these tasks is the following:
* Checking the current timetable
* Checking grades and subject performance
* Use this information to create a manual revision timetable
* Regularly update this timetable manually based on performance

The issue with this system is that it is entirely manual, which means that students may neglect
to create or update a revision timetable. Also, the current system does not allow students to add
their own custom lessons, or be notified for a lesson. My idea is to have a user-friendly system
that integrates all these features, in one easy to use web application.

My application will solve this problem, by **integrating revision session management**, **homework
reminders** and **performance analysis** in one simple dashboard. Students will be able to access this
dashboard via a **Django web application**, and possibly a **Flutter mobile application**.

In order to solve this problem with the suggested solution, I will need to learn the following:
* Usage of the Django web framework
* Usage of the PostgreSQL Database Management System with Python
* Usage of JavaScript graphing libraries such as D3.js
* Use of the Dart standard library, and usage with Flutter

### Justification for Computational Method

This problem lends itself to utilization of computational methods for several reasons: <br/>

* Student performance data will be abstracted, instead displayed as as a simple line graph.
    * In order to display data as a graph, a computational device is needed.
* The application will also automatically generate a study timetable that adapts to this data.
    * This solution utilizes algorithms that can only be executed on a computational device.
* The application stack is a system that includes my webserver, which will run on a computer.

Therefore, there is no alternative solution that would not require a computer to execute.

### Applications of Computational Methods

There are several ways that computational methods can be applied to this project.

| **Method of computational thinking**  | **Explanation of relevant features** |
|:-------------------------------------:|:------------------------------------:|
| Abstract | My web application will be as user-friendly as possible. this will require me to hide certain details from the user - for example, the raw data that is scraped by my webscraper. Instead, the user will only see data that is relevant to their current page: If they are on the summary page, they will only see simple summarized data and graphs for their performance. |
| Heuristic | The summary page of my dashboard will include rounded, approximate values to represent the correlation between various properties of the student's study time, free time, grades, and punctuality. |
| Procedural | My application stack will be comprised of several Python modules, each separated into classes, methods and functions. I will be able to remove modules, test modules and edit modules in a way that does not affect any irrelevant components of the application. |
| Concurrent | The web application must be able to handle multiple HTTP requests simultaneously. I will be applying concurrent thinking to plan and design the processing and response for each request. |



### Conclusion

The statements above have shown that my problem can be solved with a computational method. This makes it suited for a computer to solve with a program.

If the problem is successfully solved, the stakeholders will be able to access a web dashboard where they will be able to **view their school timetable**,
**add and remove events from this timetable**, and **view statistics of their study progress**.

### Research

### Stakeholder Interview Questions

* Have you ever used a homework management system before?
* If so, what are your favourite features of this system?
* Are there any features you want to see from a system like this?
* Are there any features you want removed?

### Interview results: Troy Sherlock
#### Have you ever used a homework management system before?
*Yes, I have used Show My Homework in high school to manage my timetabled lessons and homework.*
#### If so, what are your favourite features of this system?
*My favourite feature is the ability to colour-code homework slots depending on whether they are completed or not.*
#### Are there any features you want to see from a system like this?
*I would like to see a reminder system, such as push notifications for due homework.*
#### Are there any features you want removed?
*I do not like Show My Homework's "my calendar" system, and would like it to display more accurate time stamps.*

I found a service that is a similar solution to my own, **showmyhomework.co.uk**, by Satchel:

#### Show my Homework

Show My Homework is a service designed for schools, that aims to unify student timetables,
homework tasks and revision session management.

|    Online Dashboard      |    Mobile Application    |
|:------------------------:|:------------------------:|
![](https://satchel-sw-prod.imgix.net/images/products/timetables/timetables_@2x.png) | ![](https://satchel-sw-prod.imgix.net/images/products/timetables/mobile_timetables_@2x.png) |
| Fully-featured management system | Minimal features, simple timetable with reminders  |

**Features worth including in my solution:**
* **The simple, intuitive interface.**
  This is because my users must be able to understand how the timetable is structured, and the best way to acheive this is to
  use a format like the one that is used by ShowMyHomework, where the columns are for "time", and the rows for "day".

**Possible limitations of the project:**
* **The time limit.**
  As I am given a relatively short time frame to complete a project of this scale, sacrifices must be made in order to complete the project
  on time. These sacrifices may be manifested as libraries utilised when the standard library could be used, or features cut from the final
  project due to high complexity.
* **The cost.**
  Part of this solution requires me to run the web application on server-level hardware. Although the ideal solution would be using a paid service,
  I will be using a free service for this project. This may limit my solution efficiency.

**Final requirements of the project:** <br>
From the aforementioned statements, I have produced a detailed list of essential features of the solution:

**Functionality** <br>
The solution will be required to do the following:
* **Display any Loreto student's timetable in an intuitive manner.**
  This means that I will need to communicate with MyLoreto to retrieve this information, then parse it in such a way that my program will be able to
  extract the necessary information from it, and finally render this information in a simple manner. As intuitiveness of the solution is subjective,
  I will be using the opinion of my stakeholders to judge this.

* **Allow students to create their own custom entries in the timetable.**
  This means that I will need to store the student's timetable in a persistent way, suggesting that I will need to use a database. This database will
  store student timetables, as well as authentication for MyLoreto to verify the lessons. I will need to insert and remove data from the database upon
  the user's request, so usage of SQL may be required.

**Requirements:** <br>
Due to the nature of my solution, there are two separate hardware requirements:

* **Server Requirements:** The server-side application must be run on hardware that can maximise uptime, that is stay online for extended periods of time.
This kind of hardware is provided by a number of services, however I will be using a [Heroku free tier](https://www.heroku.com) virtualised private server.
I have mentioned above that running this application on a free service is not ideal, however Heroku provides build integration with GitHub, allowing me to
manually check the uptime of my service. As for software requirements, the server will need to support the Python runtime. Heroku has this functionality
builtin.

* **Client Requirements:** As the bulk of my code will be executed server-side, the client only needs to be able to render HTML and execute JavaScript.
This minor task can be done by most modern ARM/x86/x64 devices, such as mobile phones, laptops, raspberry pis or desktop PCs. I do not therefore have
any particular hardware requirements. The only software that is required is a web browser.

### Success Criteria
There are some specific areas of my solution that will need to be checked to ensure that my project was a success. These areas are described below:
* **User friendliness:** My stakeholders will need to check that the web interface of my project is sufficiently user friendly. To do this, they will score the
user interface on a scale of 1 to 10.
* **Robustness:** My stakeholders need to check that the system is robust, and so will be stress testing the system over the course of a week, with some provided
test data. They will then rate the reliability of the service on a scale of 1 to 10.
* **Scalability:** My stakeholders need to ensure that the system is scalable. To do this, I will ask multiple stakeholders to test the system at the same time,
starting at a score of 10 and docking points for any issues or errors caused by this.

### Decomposing the Problem

![image](https://github.com/AnonGuy/Structure/blob/master/docs/images/StructureDecomposition.png?raw=true)
Using procedural thinking, I have broken down my solution into six main problems: 
* **Web Scraper**
   * The Web Scraper will be the system that communicates with MyLoreto. It will utilize the `requests` library to
   authenticate a MyLoreto session, and scrape the relevant HTML elements such as timetabled lessons, markbook grades
   and attendance data, with the `re` library to match [HTML Regular Expressions](https://stackoverflow.com/a/1732454).
* **Django Webserver**
   * The Webserver will be the system that communicates with the customer. It will utilize the [Django](https://www.djangoproject.com/)
   backend web framework to handle HTTP requests from multiple users in parallel, and it will dynamically generate unique HTML files for
   each user, based on defined templates. This system will also render data such as timetabled lessons, in the form of styled HTML elements.
* **Object-Relational Mapper**
   * An Object-Relational Mapper (ORM) is a library that utilises Object-Oriented Programming (OOP) to abstract complex SQL queries from
   the developer. For example, with a defined class `User`, `User(name="Jeremiah", age=18).save()` will execute the equivalent SQL statement,
   `INSERT INTO User (name, age) VALUES ("Jeremiah", 18)`. Although Django provides a builtin ORM for this purpose, I will be writing my own
   implementation from scratch.
* **Web Application Programming Interface**
   * The server-side API will be an interface providing raw data - for example, a POST request with authorization headers to `/api/student-data`
   might return JSON-formatted data about the student in question. This will be used for any further client applications, such as a mobile app
   or desktop feature.
* **Web Dashboard**
   * The Web Dashboard will be the HTML frontend that will be displayed to the customers. The Django backend will generate this HTML from a defined
   template, and I will be using a popular frontend web framework, [Bootstrap](https://getbootstrap.com/), to create and style this template. 
* **Mobile Application**
   * The Mobile application will be a portable client for the Web API. It will be able to retrieve student timetables, add reminders for
   lessons, add custom timetable entries and add homework notes.

| Database Relationships | Data Flow Diagram |
|:----------------------:|:-----------------:|
|![](https://github.com/AnonGuy/Structure/blob/master/docs/images/StructureERD.png?raw=true)|![](https://github.com/AnonGuy/Structure/blob/master/docs/images/StructureDataFlow.png?raw=true) Users communicate with the system via the Mobile Client and online Dashboard.|

# Development

Before starting development, I have decided on the naming convention and code style I will use throughought the project. This will be based on [PEP8](https://www.python.org/dev/peps/pep-0008/),
a document stating the standard conventions for Python style guide. <br>

In summary, I will be conforming to the following rules:

**All functions and methods I define must contain a docstring explaining its use.**
```python
def add_two_numbers(a, b):
    """Adds two numbers, a and b."""
    return a + b
```

**All variables, methods and functions will use `snake_case`, rather than `mixedCase`.** <br>
Any classes which I define will use `PascalCase`.
```python
some_variable = 'foo'

class SomeClass:
    def __init__(self):
        self.bar = 'baz'

    def what_is_bar(self):
        """Returns the value of bar."""
        return self.bar

some_instance = SomeClass()
```
As is usual with any code (but particularly Python) I will be naming my variables and methods with thought, using names that enhance readability.

I started by creating a simple script that will allow me to request and parse data from MyLoreto.
I have decided to use the `requests` library to handle HTTP requests and responses, and the `re` builtin module to parse the content with regular expressions.

I will be using Regular Expression patterns to catch certain substrings of a HTTP response. For example, from this snippet of HTML:
```html
	<dl class="dl-horizontal" style="font-size: 0.9em">
		<dt>Reference: </dt>
		<dd>S20170000420</dd>
	</dl>
```
I am able to catch the Reference number with the following regex pattern: `Reference: </dt>\s+<dd>([A-Z0-9]+)`
The `\s+` represents one or more whitespace characters, and the `[A-Z0-9]+` represents one or more capital alphanumeric characters.
```python
>>> import re
>>> html = """
... 	<dl class="dl-horizontal" style="font-size: 0.9em">
... 		<dt>Reference: </dt>
... 		<dd>S20170000420</dd>
... 	</dl>"""

>>> match = re.search(r'Reference: </dt>\s+<dd>([A-Z0-9]+)', html)
>>> match.group(1)
'S20170000420'
```
An example prototype of the script is below:
```python
import re

import requests


endpoint = "https://my.loreto.ac.uk/"

patterns = {
    'name': b'fullName: "([A-Za-z ]+)"',
    'username': b'username: "([A-Za-z0-9]+)"',
    'avatar': b'base64,(.*?)">',
    'reference_number': br'Reference: </dt>\s+<dd>([A-Z0-9]+)',
    'tutor': b'Tutor: </dt> <dd> (.*?) </dd>'
}


def get_student_data(*credentials: str) -> dict:
    """Get data about a student, given their username and password."""
    student_data = {}
    landing_page = requests.get(endpoint, auth=credentials).content
    for key, pattern in patterns.items():
        student_data[key] = re.search(pattern, landing_page).group(1)
    return student_data
```
An example of this function is use can be seen below:
```python
>>> get_student_data('jerbob42', 'password')
{
    'name': b'Jeremiah Boby',
    'username': b'JerBob42',
    'avatar': b'/9j/4AAQSkZJRgABAQEASABIAAD...',
    'reference_number': 'S20170000420',
    'tutor': 'Mr Bloggs'
}
```
### Potential Improvement
**I could improve this function's performance by utilising Python's builtin `threading` module, starting a new `Thread` for each regex search that I start. This means that each regex search will not block the execution of the next.**

I then decided to create a function for validating user credentials. I decided to create this function so that users are not presented with an error immediately after providing incorrect credentials. <br>
In the case of incorrect credentials, this function will return `False`, and an alert will be provided to the user.
```python
def valid_user(*credentials: str) -> bool:
    """Take a student's credentials and validate them."""
    print('Validating user...')
    return requests.get(
        endpoint, auth=credentials
    ).status_code == 200
```
This function checks that the HTTP response code for a request with the provided credentials is successful. <br>
With some simple validation and webscraping done, I then decided to start work on the main webserver. To begin with, I used the `django-admin` command-line tool to generate the skeleton project required for the webserver:

```bash
$ django-admin startproject structure
```

This created a directory with the following structure:

```
structure/
    manage.py
    structure/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```
In order to comply with separation of concerns, I have decided to implement my student dashboard as a separate module in the project, to be named `dashboard`. To do this, I used the following command:
```bash
$ python manage.py startapp dashboard
```
I then removed all redundant files which were not required for the project. This resulted in the following directory structure:
```
structure/
    manage.py
    structure/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    dashboard/
        __init__.py
        models.py
        views.py
```
In order to be able to modify and update my database, I did some research into [the Django documentation](https://github.com/AnonGuy/structure/blob/master/docs/README.md#django-documentation-database-fields) on its builtin ORM.
Though I initially decided to create my own ORM for this project, I have made the decision to use Django's builtin ORM to save time on the project. <br>
If I had more time to enhance this project, I would have written a custom ORM for this purpose.

I described the following database models below in the `structure/dashboard/models.py` file:

```python
"""Define database models for use in the PostgreSQL server."""

from django.contrib.postgres import fields
from django.db import models


class Student(models.Model):
    """Student model: contains information used by the dashboard."""

    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=29)
    avatar = models.CharField(max_length=20000)
    reference_number = models.CharField(max_length=12)
    tutor = models.CharField(max_length=50)
    timetable = fields.JSONField()
    attendance = fields.JSONField()
    markbook = fields.JSONField()

    class Meta:
        # Give the database table a specific name.
        db_table = "student"


class User(models.Model):
    """User model: contains information specific to user authorization."""

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=8, unique=True)
    password = models.CharField(max_length=20)

    class Meta:
        # Give the database table a specific name.
        db_table = "user"
```
As you can see, these models do not match the ones that I created during the Design phase. This is because I needed to create a simplified version of the product, so that I was able to test it as soon as possible.
Next, I added some simple views to run when a user requests pages. These were defined in the `structure/dashboard/views.py` file:
```python
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .models import User
from .scraper import valid_user


# Dictionary containing data about a user's session
current_session: dict = {}


class HomePageView(TemplateView):
    """HomePage view: default view of the landing page."""

    def get(self, request, *args, **kwargs):
        """Runs on a HTTP GET request."""
        if current_session.get('authenticated'):
            # If the current user is authenticated, render the dashboard
            return render(request, "dashboard.html", context=current_session)
        else:
            # If the current user is not authenticated, redirect to the signin page
            return redirect("/sign-in")


class SignInView(TemplateView):
    """SignInView: view for the sign in page."""

    def get(self, request, *args, **kwargs):
        """Runs on a HTTP GET request."""
        return render(request, "sign-in.html", context=None)

    def post(self, request):
        """Runs on a HTTP POST request."""
        # Get the username and password from the POST request
        username, password = (
            request.POST.get('username'), request.POST.get('password')
        )
        # Create a User object with the username and password
        user = User(username=username, password=password)
        # Validate the user object
        if valid_user(user.username, user.password):
            # If the current user is valid, add the user to the session
            current_session['user'] = user
            # Set the "authenticated" flag to True
            current_session['authenticated'] = True
            # Redirect to the home page
            return redirect('/')
        else:
            # If the current user is not valid, set the "authenticated" flag to False:
            current_session['authenticated'] = False
        # If there has been no previous returns, render the signin page
        return render(request, "sign-in.html", context=None)
```
As shown above, when a user's browser requests the home page, the following code is executed:
```python
def get(self, request, *args, **kwargs):
    """Runs on a HTTP GET request."""
    if current_session.get('authenticated'):
        # If the current user is authenticated, render the dashboard
        return render(request, "dashboard.html", context=current_session)
    else:
        # If the current user is not authenticated, redirect to the signin page
        return redirect("/sign-in")
```
In `dashboard/templates`, I have added `dashboard.html` and `sign-in.html`. `dashboard.html` is a simple example page for the CSS framework that I am using, Bootstrap:
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="https://getbootstrap.com/favicon.ico">

    <title>Structure - Dashboard</title>

    <!-- Bootstrap core CSS -->
    <link href="../static/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="../static/css/dashboard.css" rel="stylesheet">
  </head>

  <body>
    <nav class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0">
      <a class="navbar-brand col-sm-3 col-md-2 mr-0" href="dashboard.html#">Structure Dashboard</a>
      <input class="form-control form-control-dark w-100" type="text" placeholder="Search" aria-label="Search">
      <ul class="navbar-nav px-3">
        <li class="nav-item text-nowrap">
          <a class="nav-link" href="dashboard.html#">Sign out</a>
        </li>
      </ul>
    </nav>

    <div class="container-fluid">
      <div class="row">
        <nav class="col-md-2 d-none d-md-block bg-light sidebar">
          <div class="sidebar-sticky">
            <ul class="nav flex-column">
              <li class="nav-item">
                <a class="nav-link active" href="dashboard.html#">
                  <span data-feather="home"></span>
                  Dashboard <span class="sr-only">(current)</span>
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="dashboard.html#">
                  <span data-feather="file"></span>
                  Summary
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="dashboard.html#">
                  <span data-feather="shopping-cart"></span>
                  Reminders
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="dashboard.html#">
                  <span data-feather="users"></span>
                  Timetable
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="dashboard.html#">
                  <span data-feather="bar-chart-2"></span>
                  Homework
                </a>
              </li>
            </ul>

            <h6 class="sidebar-heading d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-muted">
              <span>Saved reports</span>
              <a class="d-flex align-items-center text-muted" href="dashboard.html#">
                <span data-feather="plus-circle"></span>
              </a>
            </h6>
            <ul class="nav flex-column mb-2">
              <!--
              <li class="nav-item">
                <a class="nav-link" href="dashboard.html#">
                  <span data-feather="file-text"></span>
                  Example Entry
                </a>
              </li>
              -->
            </ul>
          </div>
        </nav>

        <main role="main" class="col-md-9 ml-sm-auto col-lg-10 pt-3 px-4">
          <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pb-2 mb-3 border-bottom">
            <h1 class="h2">Dashboard</h1>
            <div class="btn-toolbar mb-2 mb-md-0">
              <div class="btn-group mr-2">
                <button class="btn btn-sm btn-outline-secondary">Save</button>
                <button class="btn btn-sm btn-outline-secondary">Export</button>
              </div>
              <button class="btn btn-sm btn-outline-secondary dropdown-toggle">
                <span data-feather="calendar"></span>
                This week
              </button>
            </div>
          </div>

          <canvas class="my-4" id="myChart" width="900" height="380"></canvas>

          <h2>Section title</h2>
          <div class="table-responsive">
            <table class="table table-striped table-sm">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Header</th>
                  <th>Header</th>
                  <th>Header</th>
                  <th>Header</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>1,001</td>
                  <td>Lorem</td>
                  <td>ipsum</td>
                  <td>dolor</td>
                  <td>sit</td>
                </tr>
              </tbody>
            </table>
          </div>
        </main>
      </div>
    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="../static/js/vendor/jquery-slim.min.js"><\/script>')</script>
    <script src="../static/js/vendor/popper.min.js"></script>
    <script src="../static/js/bootstrap.min.js"></script>

    <!-- Icons -->
    <script src="https://unpkg.com/feather-icons/dist/feather.min.js"></script>
    <script>
      feather.replace()
    </script>

    <!-- Graphs -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.1/Chart.min.js"></script>
    <script>
      var ctx = document.getElementById("myChart");
      var myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
          datasets: [{
            data: [15339, 21345, 18483, 24003, 23489, 24092, 12034],
            lineTension: 0,
            backgroundColor: 'transparent',
            borderColor: '#007bff',
            borderWidth: 4,
            pointBackgroundColor: '#007bff'
          }]
        },
        options: {
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: false
              }
            }]
          },
          legend: {
            display: false,
          }
        }
      });
    </script>
  </body>
</html>
```
This resulted in the following web page:

![Bootstrap example](https://github.com/AnonGuy/Structure/blob/master/docs/images/BootstrapExample.png)

`sign-in.html` contains just a login form:

```html
<form action="", method="post", class="form-signin">
  <h1 class="h3 mb-3 font-weight-normal">Sign in to Structure</h1>

  <input class="form-control" id="inputUsername" name="username" placeholder="College username" required type="text" value="">
  <input class="form-control" id="inputPassword" name="password" placeholder="College password" required type="password" value="">
  <input class="btn btn-lg btn-primary btn-block" id="submit" name="submit" type="submit" value="Sign in">

  <br/>
</form>
```
This resulted in the following web page:

![Signin example](https://github.com/AnonGuy/Structure/blob/master/docs/images/SigninProof.png)

When the user enters their username and password, these parameters are sent as part of the POST request to the same endpoint.
This will execute the following code:
```python
def post(self, request):
    """Runs on a HTTP POST request."""
    # Get the username and password from the POST request
    username, password = (
        request.POST.get('username'), request.POST.get('password')
    )
    # Create a User object with the username and password
    user = User(username=username, password=password)
    # Validate the user object
    if valid_user(user.username, user.password):
        # If the current user is valid, add the user to the session
        current_session['user'] = user
        # Set the "authenticated" flag to True
        current_session['authenticated'] = True
        # Redirect to the home page
        return redirect('/')
    else:
        # If the current user is not valid, set the "authenticated" flag to False:
        current_session['authenticated'] = False
    # If there has been no previous returns, render the signin page
    return render(request, "sign-in.html", context=None)
```

### Potential Improvement
**Currently, I am relying on the mutability of a global variable. This is unreliable, as it will only work for one user at a time. It is not scalable, nor lend itself to concurrent thinking. Instead, I could use Django's builtin `request.session` object, which is unique for each request, as it is an attribute of one parameter of the request method.**

However, this does not store user details. Instead, it only stores a global `authenticated` flag.

In order to display student information, I will need to add more information to the scraper. In order to acheieve this, I decided
to create a custom class, which I will use solely to parse the MyLoreto landing page.

There are several reasons why I have decided to use a class for parsing the landing page:

* It allows me to create a combination of variables, methods and statements that I can reproduce whenever I need to.
* It allows me to import this class into any module I need, lending to **modular thinking**.
* It helps with separation of concerns, as all variables and methods will only have the scope of the instance it applies to.
* It creates more readable, maintainable code, as I write less and document more.



The class is defined as follows:
```python
class LandingPageParser:
    """Class for parsing the Loreto landing page."""

    def _set_regex_group(self, page: bytes, name: str, pattern: bytes):
        """Set the Student data to the first group of the given match."""
        match = re.search(pattern, page)
        if match is not None:
            # If the Regex match was successful
            self.student.__setattr__(name, match.group(1).decode())

    def _get_short_timetable(self):
        """Get the timetable for the current day."""
        # List of lessons in the current day.
        timetable = []
        # Regular Expression pattern for a lesson.
        pattern = re.compile(
            b'TimetableEntry .*?>(?P<time>[0-9 -:]+)'
            b'.*?(?P<room>[()A-Z0-9]+)'
            b'.*?(?P<teacher>[()A-Za-z0-9 -]+) ',
            re.DOTALL
        )
        # Iterate each attribute of every lesson in the timetable
        for time, room, teacher in pattern.findall(self.page):
            # Remove brackets from the lesson
            room = room.strip(b'()')
            subject, teacher = teacher.split(b' - ')
            # Append this lesson dictionary to the list
            timetable.append(
                {
                    'time': time.decode(),
                    'room': room.decode(),
                    'subject': subject.decode(),
                    'teacher': teacher.decode()
                }
            )
        # Set the student's timetable to this list
        self.student.short_timetable = timetable

    def _get_timetable(self):
        """Get the timetable for the current week."""
        # Create a dictionary of day -> lesson list
        timetable = {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': []
        }
        # Extract the HTML snippets for each day
        day_meta = '<th>{0}(.*?)(<th>|</script>)'
        # Pattern that will be applied to the previous day snippet
        lesson_meta = (
            'Times">(?P<time>[0-9: -]*)'
            '<.+?Code">(?P<subject>[A-Za-z() -]*)'
            '<.+?Staff"> *?(?P<teacher>[A-Za-z ]*) *?'
            '<.+?right">(?P<room>[A-Z0-9]*)'
        )
        # Get the Monday of the current week
        now = datetime.now()
        start = now - timedelta(days=now.weekday())
        start = start.strftime('%Y-%m-%d')
        # Create a HTTP request to MyLoreto with the student's data
        response: bytes = requests.post(
            f'{endpoint}attendance/timetable/studentWeek',
            data={'week': start, 'student_user_id': self.user_id},
            auth=(self.user.username, self.user.password),
            headers={'X-Requested-With': 'XMLHttpRequest'}
        ).content
        # Iterate each day and lesson list in the timetable
        for day, lesson in timetable.items():
            # Extract the content
            content = re.search(
                day_meta.format(day).encode(), response, re.DOTALL
            ).group(1).decode()
            for match in re.finditer(lesson_meta, content, re.DOTALL):
                # Append each lesson to the timetable
                lesson.append(match.groupdict())
        # Set the parser instance's "timetable" attribute to this timetable
        self.student.timetable = timetable

    def __init__(self, user: User):
        # Get the student's landing page with their credentials
        self.page = requests.get(
            endpoint, auth=(user.username, user.password)
        ).content
        # Set the student and user attributes persistently
        self.user = user
        self.student: Student = Student()
        # Pull the user's UserId with a regular expression
        user_id = re.search(
            br'UserId = "(\d+)"', self.page
        )
        if user_id is not None:
            # if the UserId was found:
            self.user_id: int = int(user_id.group(1))
        # Define regex patterns for use by core components of the student object.
        patterns = {
            'name': b'fullName: "([A-Za-z ]+)"',
            'username': b'username: "([A-Za-z0-9]+)"',
            'avatar': b'base64,(.*?)">',
            'reference_number': br'Reference: </dt>\s+<dd>([A-Z0-9]+)',
            'tutor': b'Tutor: </dt> <dd> (.*?) </dd>'
        }

    def parse(self) -> Student:
        """Parse the webpage content and return the resulting Student."""
        self._get_short_timetable()
        self._get_timetable()
        for key, pattern in patterns.items():
            self._set_regex_group(self.page, key, pattern)
        self.student.email = '{0}@student.loreto.ac.uk'.format(
            self.student.username
        )
        return self.student


def valid_user(user: User) -> bool:
    """Take a User object and validate credentials."""
    print('Validating user...')
    return requests.get(
        endpoint, auth=(user.username, user.password)
    ).status_code == 200


def create_student(user: User) -> Student:
    """Take a User object and intialize a Student object."""
    parser = LandingPageParser(user)
    student = parser.parse()
    print('Created student:', repr(student.name))
    return student
```
I am using regular expressions to extract parts of the HTML page. I use regular expressions for the following reasons:
* Regular expressions enable me to reduce my code base drastically. If I were to use simple string manipulation to extract the data I need, I would have significantly more **unmaintainable** code.
* Regular expressions are much easier to read than many different string manipulations.
* Regular expression patterns are **reusable** once compiled.

However, I soon realised that each of these regular expression searches are blocking the thread of execution. Each extraction prevents the next one from being carried out. In order to apply **concurrent thinking** to this problem, I decided to use the `threading` module, part of Python's standard library, to run each regex search in a separate thread:

```python
    def __init__(self, user: User):
        self.page = requests.get(
            endpoint, auth=(user.username, user.password)
        ).content
        self.user = user
	# Set of threads used in the parser.
	# I am using a set to ensure that threads are not duplicated.
        self.threads: set = set()
        self.student: Student = Student()
        user_id = re.search(
            br'UserId = "(\d+)"', self.page
        )
        if user_id is not None:
            self.user_id: int = int(user_id.group(1))
        patterns = {
            'name': b'fullName: "([A-Za-z ]+)"',
            'username': b'username: "([A-Za-z0-9]+)"',
            'avatar': b'base64,(.*?)">',
            'reference_number': br'Reference: </dt>\s+<dd>([A-Z0-9]+)',
            'tutor': b'Tutor: </dt> <dd> (.*?) </dd>'
        }
	# Create a thread for getting the student's daily timetable, add it to threads
        self.threads.add(Thread(target=self._get_short_timetable))
	# Create a thread for getting the student's full timetable, add it to threads
        self.threads.add(Thread(target=self._get_timetable))
	# The threads created so far have not been started yet
        for key, pattern in patterns.items():
	    # For every regex pattern in the patterns I need to extract:
            self.threads.add(
	    	# Create a thread to extract that pattern and add it to threads
                Thread(
                    target=self._set_regex_group,
                    args=(self.page, key, pattern)
                )
            )

    def parse(self) -> Student:
        """Parse the webpage content and return the resulting Student."""
	# The __init__ method does not start the threads.
	# Instead, this parse method will start each thread.
        for thread in self.threads:
	    # Start each thread concurrently
            thread.start()
        for thread in self.threads:
	    # Close each thread once they have completed
            thread.join()
        self.student.email = '{0}@student.loreto.ac.uk'.format(
            self.student.username
        )
        return self.student
```

There are several reasons why using a threaded solution is an improvement:
* Decreases the time needed for initialising the student object
* Increases maximum code throughput, as multiple methods of my code will be running at one time
* This solution therefore lends itself to **concurrent thinking** well

# Bibliography

## Django Documentation: Database Fields
https://docs.djangoproject.com/en/2.1/topics/db/models/

## Heroku Documentation: The Procfile
https://devcenter.heroku.com/articles/procfile

## Heroku Documentation: Monitoring and Metrics
https://devcenter.heroku.com/categories/reference#monitoring-metrics

## Bootstrap Documentation
https://getbootstrap.com/docs/4.0/examples/

## Timetables.js Documentation
http://timetablejs.org
