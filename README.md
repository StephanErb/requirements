Python Package Requirements
===========================

[![Requirements Status](https://requires.io/github/StephanErb/requirements/requirements.png?branch=master)](https://requires.io/github/StephanErb/requirements/requirements/?branch=master)

The requiremet files in this project serve as a gatekeeper for an internal PyPI mirror. 

Current workflow:
* One requirement file per licence category. 
* Requirement files updated via pull-requests
* Internal build server automatically populates the corresponding internal package index

Ideas worth evaluating:
* Instead of one req.txt per licence category we could use one requirements file per internal team or project


