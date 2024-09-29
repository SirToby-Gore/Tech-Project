import http.server
import socket
import threading

def start_web_server(port=8000):
    """Starts a simple HTTP server on the specified port.

    Args:
        port (int): The port number to listen on.
    """

    try:
        # Create a server instance
        server_address = ('', port)
        httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

        # Start a separate thread to serve the web server
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.daemon = True  # Set the thread as a daemon so it terminates when the main script exits
        server_thread.start()

        print(f"Web server started on http://localhost:{port}/")

        # Keep the main thread running to prevent the script from exiting
        while True:
            pass

    except socket.error as e:
        print(f"Error starting web server: {e}")

if __name__ == "__main__":
    start_web_server()