# Text Summarization

## Goal
The goal of this project is to generate summaries of medical articles using abstractive text summarization.



## Tools/Libraries Used
- HuggingFace Transformers
- Flask REST API
- Github Actions CI/CD Pipeline
- Docker

## Instructions
1. Do a pip install requirements.txt to install the necessary libraries
2. Then, run summary.py to run the flask server
3. View the index.html page in the browser
4. If you want to run the docker container instead, perform the below steps:
   - Please Install Docker and create a Docker Hub account and run the following commands:
       - docker compose up --build
       - docker login
       - docker tag <source_image_name> <dest_image_name>:<version_name>
       - docker push <image_name>:<version_name>
       - docker run -p<port_number>:<port_number> <image_name>:<version_name>

   

## Resources
- https://huggingface.co/docs/transformers/tasks/summarization
- https://github.blog/2022-02-02-build-ci-cd-pipeline-github-actions-four-steps/
