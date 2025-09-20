"""
This script runs the FlaskWebProject application using a WSGI server on Azure.
"""

from FlaskWebProject import app

# This is a standard entry point for WSGI servers
# app is the Flask application instance
if __name__ == '__main__':
    # This block is for local development only
    app.run()
