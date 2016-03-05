""" Delete here when submitting!!!
#############################################################################
Notes which demonstrate an understanding of:
    - Servers: 
        how servers handle requests, process them, and deliver responses
    - The Importance of Validating Input: 
        acknowledge the importance of validating user input, expecially the implications that validation has on site security and user experience.
    - HTML Templates and Abstraction:
        an understanding of why programmers use HTML templates, how these templates allow programmers to avoid repetition, and understanding of WHY avoiding repetition is important
#############################################################################
"""


unit1 = {
    "unit_title": "Unit 4.1: Introduction to Networks",
    "concepts": {
        "concept1": {
            "concept_title": "Networks",
            "concept_description": "Networks have at least 3 entities and every entity can communicate even with indirectly connected entities." 
        },
        "concept2": {
            "concept_title": "Latency & Bandwidth",
            "concept_description": "There are two main way to measure networks.",
            "html_list": [
                "Latency: a duration of a message sent from its source to its destination",
                "Bandwidth: an amount of information that can be transmitted per unit time"
            ]
        },
        "concept3": {
            "concept_title": "Client / Server / Protocol",
            "concept_description": "Your computer(= Client) is connected to a server through a network called the Internet. When your browser requests a page, the server sends back the requested page. For the web, a protocol gives rules about how a client and a server talk to each other (Hypertext Transfer Protocol(HTTP)).",
            "image": "http://i.imgur.com/0vPATU6.png" 
        }
    }
}

unit2 = {
    "unit_title": "Unit 4.2: Make the Internet Work For You",
    "concepts": {
        "concept1": {
            "concept_title": "URL",
            "concept_description": "URL is abbreviation of Uniform Resource Locator.",
            "image": "http://i.imgur.com/vdwt3eC.png"
        },
        "concept2": {
            "concept_title": "GET vs POST",
            "concept_description": "Requests which are sent from your browser to a server. A type of requests making to the server is called 'method': GET(= get a document from the server) & POST(send data to the server). When making requests, request line if followed by a number of headers.",
            "image": "http://i.imgur.com/uot62jp.png"
        },
        "concept3": {
            "concept_title": "Purpose of a Server",
            "concept_description": "Servers respond to HTTP requests from a browser:",
            "html_list": [
                "Static content --- pre-written files, images",
                "Dynamic content --- built on the fly by a Web application on a web server. Web applications dinamically generates content that the browser requests. Ex. Facebook or Google Search Engine."
            ]
        }
    }
}

unit3 = {
    "unit_title": "Unit 4.3: Forms",
    "concepts": {
        "concept1": {
            "concept_title": "What is Forms?",
            "concept_description": "Forms are the ways which allow websites to collect information from users."
        },
        "concept2": {
            "concept_title": "Examples of Forms",
            "concept_description": "There are various types of forms, such as text boxes, check boxes, radio buttons, or dropdown meues, etc...",
            "forms": [
                {"form_name": "Text Box",
                 "form_example": """<label>
        Name:
        <input name='q'>
    </label>
    <label>
        Age:
        <input name='r'>
    </label>"""
                },
                {"form_name": "Check Box",
                 "form_example": """<label>
        One
        <input type="checkbox" name="q">
    </label>
    <label>
        Two
        <input type="checkbox" name="q">
    </label>
    <label>
        Three
        <input type="checkbox" name="q">
    </label>
    <br>
    <input type="submit">"""
            },
            {"form_name": "Radio Buttons",
             "form_example": """<label>
        One
        <input type="radio" name="q">
    </label>
    <label>
        Two
        <input type="radio" name="q">
    </label>
    <label>
        Three
        <input type="radio" name="q">
    </label>
    <br>
    <input type="submit">"""
                }
            ]
        }
    }
}

unit4 = {
    "unit_title": "Unit 4.4: Modulus & Dictionaries",
    "concepts": {
        "concept1": {
            "concept_title": "The Modulus Operator",
            "concept_description": "The modulus operator '%' returns the reminder of integer division.",
            "code": """<Number> % <Modulus> ---> <Reminder>
   14    %    12     --->    2""",
        },
        "concept2": {
            "concept_title": "Dictionaries",
            "concept_description": "'Dictionaries' are data structures which uses keys to access information. With 'lists' in Python, you need to remember locations of elements. With 'dictionaries', you can map or access information you want to store to keys.",
            "code": """
"""
        }       
    }
}

unit5 = {
    "unit_title": "Unit 4.5: Working with App Engine",
    "concepts": {
        "concept1": {
            "concept_title": "Google App Engine (GAE)",
            "concept_description": "A tool to host a webpage for free. For more info about GAE, please visit the link below.",
            "link": {
                "link_title": "Google App Engine Docs",
                "url": "https://cloud.google.com/appengine/docs"
            }
        },
        "concept2": {
            "concept_title": "How to Add Forms",
            "concept_description": "The following code is and example of a form using GAE. By using post method, when a user type some text, the text they enter will be displayed in '/testform' page."
        },
        "concept3": {
            "concept_title": "Difference between GET and POST",
            "concept_description": "The big difference between GET and POST is; GETs include prameters in a URL, whereas POSTs include the data in the request body."
        }
    }
}

unit6 = {
    "unit_title": "Unit 4.6: Validation",
    "concepts": {
        "concept1": {
            "concept_title": "Why Input Validation is Important?",
            "concept_description": "When a user enters bad input, varidating input will prevent our web application from being hacked. Make sure to validate data on the server side as it's more secure than one on the Client side. If you are using Python and HTML template for making a web app, validation should occur in a python file. If you get an error, redirect to the form without storing invalid data to a database.",
        },
        "concept2": {
            "concept_title": "Steps for Validation & Redirection",
            "concept_description": "With varidation, the user will know that there's an error.",
            "html_list": [
                "Verify the user's input",
                "On error, render form again",
                "Include error message",
                "With a valid input, store data and redirect a page without an error message"
            ],
            "image": "http://i.imgur.com/NibKQte.png"
        },
        "concept3": {
            "concept_title": "HTML Escaping",
            "concept_description": "If a user enters HTML into the input, it will mess up the web form. It's important to escape the HTML characters. ",
                "image": "http://i.imgur.com/g4y4GV1.png?1"
        }       
    }
}

unit7 = {
    "unit_title": "Unit 4.7: HTML Templates",
    "concepts": {
        "concept1": {
            "concept_title": "String substitution",
            "concept_description": "One way to format html is to use the modulus operator %s in html string in Python. But it has quite a few problems;",
            "html_list": [
                "Hardcoded %s everywhere and difficult to change",
                "Putting html in python code as strings won't get syntax highlighted",
                "Can be made more clear",
                "If you miss changing %s, output will show %s as it is"
            ]
        },
        "concept2": {
            "concept_title": "Templates",
            "concept_description": "Better way than string substitution is to use Templates. In this lesson, we use jinja2 templates. With templates, you can...",
            "html_list": [
                "Separate different types of code (ex. sparate HTML from Python)",
                "Have better organized and more readable code",
                "More secure websites with autoescaping feature",
                "HTML that is easier to manipulate"
            ]
        },
        "concept3": {
            "concept_title": "Template Inheritance",
            "concept_description": "The most advantage of using jinja2 template is template inheritance, which 'allow you to build a base 'skeleton' template that contains all the common elements of your site and defines blocks that child template can override'. So, the template inheritance can avoid writing the same code over and over again when generating html. ",
            "link": {
                "link_title": "reference",
                "url": "http://jinja.pocoo.org/docs/dev/templates/#template-inheritance"
            }
        }
    }
}

unit8 = {
    "unit_title": "Unit 4.8: Databases",
    "concepts": {
        "concept1": {
            "concept_title": "What is a Database?",
            "concept_description": "A program that stores and retrieves large amount of structured data. It also refers to the machine running that program and a system of machines running the program together to store/retrieve data."
        },
        "concept2": {
            "concept_title": "Benefits of Databases",
            "concept_description": "Databases can take huge amount of data and answer queries on them in a reasonable amount of time without having to write a lot of custom code."
        }
    }
}

concepts_order = ["concept1", "concept2", "concept3", "concept4"]

