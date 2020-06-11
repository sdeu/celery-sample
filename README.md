# celery-chord-sample
Sample application for using Celery chords running on Docker to generate and combine files. 

## pyworker
Contains tasks for generating some dummy files. Another task then reads the generated files and combines them into a single file.

## webapp
A simple file storage with a REST api.

## Usage

1. docker-compose build
2. docker-compose up
3. python app.py
4. curl localhost:5001