from app import create_app
import argparse
import os
import logging

app = create_app()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the Flask app')
    parser.add_argument('--host', default='127.0.0.1', help='Host to run the app on')
    parser.add_argument('--port', type=int, default=5000, help='Port to run the app on')
    args = parser.parse_args()

    debug = os.environ.get('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')
    
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    print(f"Starting application on {args.host}:{args.port}")
    app.run(debug=debug, host=args.host, port=args.port)
