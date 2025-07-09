def calculate_area(shape, *args):  # Commented by AI Agent
    if shape == "circle":  # Commented by AI Agent
        radius = args[0]  # Commented by AI Agent
        return 3.14159 * radius * radius  # Commented by AI Agent
    elif shape == "rectangle":  # Commented by AI Agent
        length, width = args  # Commented by AI Agent
        return length * width  # Commented by AI Agent
    elif shape == "triangle":  # Commented by AI Agent
        base, height = args  # Commented by AI Agent
        return 0.5 * base * height  # Commented by AI Agent
    else:  # Commented by AI Agent
        print("hi")  # Commented by AI Agent
        return None  # Commented by AI Agent
  # Commented by AI Agent
def process_data(data):  # Commented by AI Agent
    result = []  # Commented by AI Agent
    for item in data:  # Commented by AI Agent
        if isinstance(item, int):  # Commented by AI Agent
            if item % 2 == 0:  # Commented by AI Agent
                result.append(item * 2)  # Commented by AI Agent
            else:  # Commented by AI Agent
                result.append(item * 3)  # Commented by AI Agent
        elif isinstance(item, str):  # Commented by AI Agent
            result.append(item.upper())  # Commented by AI Agent
    return result  # Commented by AI Agent
  # Commented by AI Agent
def validate_user(username, password):  # Commented by AI Agent
    if len(username) < 4:  # Commented by AI Agent
        return False  # Commented by AI Agent
    if len(password) < 8:  # Commented by AI Agent
        return False  # Commented by AI Agent
    if not any(char.isdigit() for char in password):  # Commented by AI Agent
        return False  # Commented by AI Agent
    if not any(char.isupper() for char in password):  # Commented by AI Agent
        return False  # Commented by AI Agent
    return True  # Commented by AI Agent
  # Commented by AI Agent
def format_output(data, format_type):  # Commented by AI Agent
    if format_type == "json":  # Commented by AI Agent
        import json  # Commented by AI Agent
        return json.dumps(data)  # Commented by AI Agent
    elif format_type == "csv":  # Commented by AI Agent
        import csv  # Commented by AI Agent
        import io  # Commented by AI Agent
        output = io.StringIO()  # Commented by AI Agent
        writer = csv.writer(output)  # Commented by AI Agent
        for row in data:  # Commented by AI Agent
            writer.writerow(row)  # Commented by AI Agent
        return output.getvalue()  # Commented by AI Agent
    else:  # Commented by AI Agent
        return str(data)  # Commented by AI Agent
  # Commented by AI Agent
def main():  # Commented by AI Agent
    print(calculate_area("circle", 5))  # Commented by AI Agent
    print(calculate_area("rectangle", 4, 7))  # Commented by AI Agent
    print(process_data([1, 2, 3, "hello"]))  # Commented by AI Agent
    print(validate_user("admin", "Password123"))  # Commented by AI Agent
    print(format_output([["a", "b"], ["c", "d"]], "csv"))  # Commented by AI Agent
  # Commented by AI Agent
if __name__ == "__main__":  # Commented by AI Agent
    main()  # Commented by AI Agent
