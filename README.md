The Blog-A-Lator App

This app is my first attempt at writing a Python program that uses the OpenAI API. This is both my first attempt at writing a Python program with a GUI and also using the OpenAI API.

What this app does is create an outline for a blog article based on a topic that you input. It asks you for how many bullet points that you would like in the outline and then generates an outline use the topic and number of bullet points anss parameters.

A drop down list of bullet points is then presented to the user. The user selects a bullet point and then a prompt is submitted back to the OpenAI API to provide expanded information on that topic.

A couple of things to keep in mind before you run the code:

    1. You will need add your own OpenAI API Key at the top of the program to the variable named openai.api.key. Without this informtion, nothing will happen when you run the progoram.

           ![Screenshot 2023-07-30 172521](https://github.com/tbedwards1028/blog-a-lator/assets/89990908/163ca588-fe8a-4e69-9e28-cc5b4a1373a3)

            
    2. You will need to install the tkinter and openai libraries, if you have not already done so.
