Tornado skeleton
===

This is my boilerplate to build a simple, fast and rock solid website based upon
the Tornado framework. There are quite many Tornado template projects out there,
but I wanted to start something new, adapting for my needs. It is a full Python3 project.

Of course this template is not designed for larger data structures. The main
focus is on scalability, fast data access and small library dependencies.

This skeleton was based in the works of Henning Kage at this [repository](https://github.com/hkage/tornado-project-skeleton).
I pulled out the quality mechanism from setup.py for more freedom. A requirements.txt
was added to install development dependencies.
Change fabfile to invoke to Python3 better support.
Some minor modifications in the structure.

Features
---
* pytest for testing
* pylama for check styles and linters

Installation
---

Start a new project based on this skeleton (need a new repository):

    $ git clone --bare https://github.com/uiansol/tornado-skeleton.git

    $ cd tornado-skeleton.git

    $ git push --mirror https://github.com/exampleuser/new-repository.git

You can remove the skeleton and clone your new repository.

To install the basic requirements for a Tornado project execute:

    $ python setup.py install

To install the requirements for development:

    $ pip install -r requirements.txt

Testing
---
All test files will be added to the ``tests`` directory. To run the tests, simply call:

    $ invoke test

To verify code styles:

    $ invoke quality

Start the server
---

To start the final application, just run the following invoke command:

    $ invoke devserver

This will tell Tornado to start the applicaton with the default port 8888. If you
deploy with another tool like docker the default port is 8000.

In addition to that, see the task.py Script for other parameters and
commands.
