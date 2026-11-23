cat << 'EOF' > scripts/udp_server.py
import socket

SERVER_IP = "0.0.0.0"
SERVER_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))
print(f"UDP Server listening on {SERVER_IP}:{SERVER_PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Received message: {data.decode()} from {addr}")
    sock.sendto(b"ACK: Message received", addr)
EOF
