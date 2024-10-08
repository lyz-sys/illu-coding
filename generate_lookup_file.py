# Generate a lookup file with 10,000 mappings
import random


def generate_lookup_file(file_name, num_entries):
    with open(file_name, 'w') as f:
        f.write("dstport,protocol,tag\n")  # Header
        for i in range(num_entries):
            dstport = random.randint(1, 65535)
            protocol = random.choice(["tcp", "udp"])
            tag = f"sv_P{i % 100}"  # Cycle through 100 tags for simplicity
            f.write(f"{dstport},{protocol},{tag}\n")

# Generate lookup file with 10,000 mappings
generate_lookup_file('lookup_file_10000.csv', 10000)
