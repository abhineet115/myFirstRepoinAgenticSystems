def read_numbers_from_list(fileName: str):
    """Read numbers from a file and return them as a list"""

    numbers = []

    with open(fileName, "r") as file:
        print("File opened successfully")
        for line in file:
            cleaned_line = line.strip()
            if cleaned_line:
                numbers.append(int(cleaned_line))

    print(f"Read {len(numbers)} numbers")
    return numbers

def compute_statistics(numbers):
    """Compute the total count, sum and average"""
    total_count = len(numbers)
    total_sum = sum(numbers)
    avg_val = total_sum / total_count if total_count > 0 else 0
    return total_count, total_sum, avg_val

def write_log(fileName, total_count, total_sum, average_value):
    """Write results to log file"""
    with open(fileName, "a") as log_file:
        log_file.write("File opened successfully\n")
        log_file.write(f"Read {total_count} numbers\n")
        log_file.write(f"Sum: {total_sum}\n")
        log_file.write(f"Average: {average_value}\n")
        log_file.write("Processing completed")

def main():
    input_file = "numbers.txt"
    log_file = "results.log"

    numbers = read_numbers_from_list(input_file)
    total_count, total_sum, avg_val = compute_statistics(numbers)
    write_log(log_file, total_count, total_sum, average_value=avg_val)

if __name__ == "__main__":
    main()