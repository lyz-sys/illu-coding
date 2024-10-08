import csv
from collections import defaultdict

def load_lookup_table(lookup_file):
    lookup_table = {}
    with open(lookup_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (int(row['dstport']), row['protocol'].lower())
            lookup_table[key] = row['tag']
    return lookup_table

def parse_flow_log(flow_log_file):
    flow_entries = []
    with open(flow_log_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 13:
                dst_port = int(parts[6])
                protocol = 'tcp' if parts[7] == '6' else 'udp' if parts[7] == '17' else 'icmp'
                flow_entries.append((dst_port, protocol))
    return flow_entries

def tag_flow_entries(flow_entries, lookup_table):
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)
    for dst_port, protocol in flow_entries:
        tag = lookup_table.get((dst_port, protocol), 'Untagged')
        tag_counts[tag] += 1
        port_protocol_counts[(dst_port, protocol)] += 1
    return tag_counts, port_protocol_counts

def write_output(tag_counts, port_protocol_counts, output_file):
    with open(output_file, 'w') as f:
        f.write("Tag Counts:\n")
        f.write("Tag,Count\n")
        for tag, count in sorted(tag_counts.items()):
            f.write(f"{tag},{count}\n")
        
        f.write("\nPort/Protocol Combination Counts:\n")
        f.write("Port,Protocol,Count\n")
        for (port, protocol), count in sorted(port_protocol_counts.items()):
            f.write(f"{port},{protocol},{count}\n")

def main(flow_log_file, lookup_file, output_file):
    # Step 1: Load the lookup table
    lookup_table = load_lookup_table(lookup_file)
    
    # Step 2: Parse the flow log
    flow_entries = parse_flow_log(flow_log_file)
    
    # Step 3: Tag flow entries based on the lookup table
    tag_counts, port_protocol_counts = tag_flow_entries(flow_entries, lookup_table)
    
    # Step 4: Write the output to file
    write_output(tag_counts, port_protocol_counts, output_file)

if __name__ == '__main__':
    # Example usage:

    # simple example
    flow_log_file = 'flow_log.txt'     # Input flow log file
    lookup_file = 'lookup.csv'         # Input lookup table file
    output_file = 'output.txt'         # Output file

    # large input file size example
    # flow_log_file = 'flow_log_10MB.txt'     # Input flow log file
    # lookup_file = 'lookup_file_10000.csv'         # Input lookup table file
    # output_file = 'output.txt'         # Output file

    main(flow_log_file, lookup_file, output_file)
