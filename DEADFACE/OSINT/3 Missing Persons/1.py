import ftplib
import random


def generate_random_number():
    return random.randint(1, 100)


def print_random_message():
    messages = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is awesome!",
        "FTP stands for File Transfer Protocol.",
        "Always remember to secure your connections.",
        "Coding is fun and challenging."
    ]
    print(random.choice(messages))


def connect_to_ftp():
    ftp_host = "3.208.232.204"
    ftp_port = 21  # Default FTP port
    ftp_user = "truthseeker"  # Find me elsewhere!
    ftp_pass = "Truth!seeKer123"  # Find me elsewhere!
    # ftp_user = "username"  # Replace with actual username
    # ftp_pass = "password"  # Replace with actual password
    try:
        # Establish FTP connection
        ftp = ftplib.FTP()
        ftp.connect(ftp_host, ftp_port)
        ftp.login(ftp_user, ftp_pass)

        print(f"Successfully connected to FTP server at {ftp_host}")

        # List contents of the root directory
        print("Contents of root directory:")
        ftp.dir()
        ftp.retrbinary("RETR flag.txt.txt", open('flag.txt', 'wb').write)
        # Close the connection
        ftp.quit()
    except ftplib.all_errors as e:
        print(f"FTP connection failed: {str(e)}")


# Main script execution
if __name__ == "__main__":
    print("Welcome to the random FTP connection script!")

    # Generate and print a random number
    random_num = generate_random_number()
    print(f"Random number: {random_num}")

    # Print a random message
    print_random_message()

    # Attempt FTP connection
    print("\nAttempting FTP connection...")
    connect_to_ftp()


def simulate_dice_roll():
    return random.randint(1, 6)


def random_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"


def random_geometric_shape():
    shapes = ["Circle", "Square", "Triangle", "Rectangle", "Pentagon", "Hexagon"]
    return random.choice(shapes)


def random_math_operation():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    operations = [
        ("+", lambda x, y: x + y),
        ("-", lambda x, y: x - y),
        ("*", lambda x, y: x * y),
        ("/", lambda x, y: x / y if y != 0 else "undefined")
    ]
    op, func = random.choice(operations)
    result = func(a, b)
    return f"{a} {op} {b} = {result}"


def random_fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib