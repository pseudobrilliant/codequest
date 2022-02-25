# Codequest Development
This repo contains a development setup for working on Lockheed Martin Codequest problems and
will serve as the main location for all our problem development and solutions.

## Codequest Setup

Make sure to register to [CodeQuest Academy](https://lmcodequestacademy.com/) in order to be able to access all the practice questions available. 
- Solutions developed in this repo should each be in a single python or C++ file.
- Each solution should be in it's own directory with its own input.txt containing the provided sample inputs.
- When submitting to Codequest you should only submit your single python or C++ file to the system. 

Basically, develop on this repo and deliver on the Codequest website your single file solution.

## Development Environment
This repo is setup with a working configuration for Visual Studio Code and python. 
- To run any single python script you can use the Run & Debug window within VSCode.
- Make sure the python file you want to run is selected in the main window.
- Then hit the Green Play button next to "Codequest: Current File". 
- You should see your results in a terminal window on bottom of screen.

NOTE: You must have a "input.txt" file within the same directory as the selected python file.

## Additional Tools
To make life easy there is a setup_problem.sh script. It is mainly written for Linux systems but may work in Windows with some changes. 

- In linux run 'source setup_problem.sh {problem_name}' and a directory will be created with the problem description downloaded for you, a starter python script, and a blank input.txt for you to start from. 
- Problem_name can be sourced from the problems list provided in codequest academy 
- Ex. source setup_problem.sh hello_world

