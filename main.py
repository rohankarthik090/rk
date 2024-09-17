import socket
import json

def send_json_data(ip, port, data):
    # Convert data to JSON format
    json_data = json.dumps(data)
    
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # Send JSON data over the socket
        sock.sendto(json_data.encode(), (ip, port))
        print(f"Sent JSON data to {ip}:{port}")
    finally:
        sock.close()

if __name__ == "__main__":
    # Data to send
    data = {
        "name": "D.V.S Sai Prasad",
        "project": "Real-time PDF generation system",
        "status": "In Progress"
    }
    
    # Define the IP and port of the C++ server
    server_ip = "127.0.0.1"  # Replace with the server's IP
    server_port = 12345       # Replace with the correct port
    
    # Send the data
    send_json_data(server_ip, server_port, data)
