from langchain_core.tools import tool

@tool
def calculator_tool(first_num: float, second_num: float, operation: str) -> dict:
    """
    Perform arithmetic operations.
    Supported:
    add
    sub
    mul
    div
    """

    try:
        if operation == "add":
            result = first_num + second_num

        elif operation == "sub":
            result = first_num - second_num

        elif operation == "mul":
            result = first_num * second_num

        elif operation == "div":
            if second_num == 0:
                return {"error": "Division by zero"}

            result = first_num / second_num

        else:
            return {"error": "Unsupported operation"}

        return {
            "first_num": first_num,
            "second_num": second_num,
            "operation": operation,
            "result": result,
        }

    except Exception as e:
        return {"error": str(e)}