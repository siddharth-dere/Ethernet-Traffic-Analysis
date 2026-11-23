cat << 'EOF' > scripts/udp_client.py
import socket
import time

TARGET_IP = "127.0.0.1" # Change to your actual IP if testing across devices
TARGET_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(5):
    message = f"Telemetry Packet {i}"
    sock.sendto(message.encode(), (TARGET_IP, TARGET_PORT))
    data, _ = sock.recvfrom(1024)
    print(f"Server response: {data.decode()}")
    time.sleep(1)
EOF
