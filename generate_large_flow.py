import random
import time

# Function to generate a single log entry
def generate_log_entry():
    eni_id = f"eni-{random.randint(1000, 9999)}"
    src_ip = f"192.168.{random.randint(0, 255)}.{random.randint(1, 254)}"
    dst_ip = f"10.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"
    src_port = random.randint(1024, 65535)
    dst_port = random.choice([80, 443, 25, 110, 143, 993])
    protocol = random.choice([6, 17])  # 6 for TCP, 17 for UDP
    packets = random.randint(1, 100)
    bytes_transferred = random.randint(1000, 50000)
    start_time = int(time.time())
    end_time = start_time + random.randint(1, 100)
    action = random.choice(["ACCEPT", "REJECT"])
    
    return f"2 123456789012 {eni_id} {src_ip} {dst_ip} {dst_port} {src_port} {protocol} {packets} {bytes_transferred} {start_time} {end_time} {action} OK\n"

# Write flow log entries to a file to reach 10 MB
def generate_large_flow_log(file_name, file_size_mb):
    with open(file_name, 'w') as f:
        current_size = 0
        while current_size < file_size_mb * 1024 * 1024:
            log_entry = generate_log_entry()
            f.write(log_entry)
            current_size += len(log_entry)

# Generate a 10 MB flow log file
generate_large_flow_log('flow_log_10MB.txt', 10)
