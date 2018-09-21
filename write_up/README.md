# Analysis

### Problem Definition and Stakeholders

The stakeholders of my application will be **fellow students of Loreto Sixth Form College**.
Being students, they need to organize revision sessions, in order to maintain the grades required
for their chosen university. Many Loreto college students have issues with organising a revision
timetable. For example, creating study sessions that do not clash with classes, or setting up
reminders for each of these study sessions, can be difficult. The needs of a College student also include
regularly checking up on their performance (grades, attendance) to ensure that they are making the
best of their study periods.

The current system for acheiving these tasks is the following:
* Checking the current timetable
* Checking grades and subject performance
* Use this information to create a manual revision timetable
* Regularly update this timetable manually based on performance

The issue with this system is that it is entirely manual, which means that students may neglect to create
or update a revision timetable. Also, the current system does not allow srudents to add their own custom
lessons, or be notified for a lesson.

My application will solve this problem, by **integrating revision session management**, **homework
reminders** and **performance analysis** in one simple dashboard. Students will be able to access this
dashboard via a **Django web application**, and **React Native mobile application**.

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
