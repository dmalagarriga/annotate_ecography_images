# Annotate ecography images
A dockerized Dash app to annotate ecography images

To build the image use:
```docker-compose build```

Having the image built, build and start the container by typing:
```docker-compose up -d```

The option “-d” ensures the app is running in the background. Without the option, you will directly see the logs, which can be useful for the first few runs, to test the setting. 

## Not running on Docker

Follow the instructions below if you don't want to run the app on Docker.

### Installing packages
Run pip install -r requirements.txt in your preferred environment manager.

### Running the app
Run python index.py to run the app
