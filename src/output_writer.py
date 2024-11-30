def write_log(log_file, message):
    with open(log_file, "a") as file:
        file.write(message)