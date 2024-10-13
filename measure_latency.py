import requests
import time

# Check if a server URL is provided as an argument
if len(sys.argv) != 2:
    print("Usage: python script.py <server_url>")
    sys.exit(1)

# Assign the server URL to a variable
server_url = sys.argv[1]

# Number of requests to send
num_requests = 5

# Counter for successful requests
success_count = 0

# Total latency
total_latency = 0

# Send HTTP requests and measure latency
for _ in range(num_requests):
    try:
        start_time = time.time()
        response = requests.get(server_url)
        end_time = time.time()
        
        if response.status_code == 200:
            success_count += 1
            latency = end_time - start_time
            total_latency += latency
            print(f"Request successful. Latency: {latency:.2f} seconds")
        else:
            print(f"Request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

# Calculate average latency and packet loss
average_latency = total_latency / success_count if success_count > 0 else 0
packet_loss = (num_requests - success_count) / num_requests * 100

print(f"\nAverage Latency: {average_latency:.2f} seconds")
print(f"Packet Loss: {packet_loss:.2f}%")
