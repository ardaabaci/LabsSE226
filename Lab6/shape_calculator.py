import geometry_utils

def main():
    operations = {
        "circle_area": geometry_utils.circle_area,
        "circle_perimeter": geometry_utils.circle_perimeter,
        "rectangle_area": geometry_utils.rectangle_area,
        "rectangle_perimeter": geometry_utils.rectangle_perimeter,
        "triangle_area": geometry_utils.triangle_area
    }

    print("Available shapes: circle, rectangle, triangle")
    print("Available calculations: _area, _perimeter (e.g., circle_area)")

    op_name = input("Enter the operation you want to perform: ").strip().lower()

    if op_name not in operations:
        print("Input Error: Invalid operation.")
        return

    try:
        if "circle" in op_name:
            r = float(input("Enter radius: "))
            result = operations[op_name](r)
        elif "rectangle" in op_name:
            w = float(input("Enter width: "))
            h = float(input("Enter height: "))
            result = operations[op_name](w, h)
        elif op_name == "triangle_area":
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            result = operations[op_name](b, h)
            
        print(f"Result: {result:.2f}")

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception:
        print("An error occurred.")

if __name__ == "__main__":
    main()