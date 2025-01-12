class Console:
    def __init__(self, memory):
        self.memory = memory  # Variable storage

    def resolve_token(self, token):
        """Resolve a single token."""
        if isinstance(token, str) and token.startswith('"') and token.endswith('"'):
            # String literal
            return token.strip('"')
        elif token.isdigit():
            # Numeric literal
            return int(token)
        elif token in self.memory:
            # Variable
            return self.memory[token]
        else:
            # Assume it's an expression and evaluate it

            return self.evaluate_expression(token)

    def evaluate_expression(self, expr):
        """Basic expression evaluator (extend for complex cases)."""
        try:
            # Replace variables in the expression with their values
            for var, value in self.memory.items():
                expr = expr.replace(var, str(value))
            # Evaluate the resulting expression
            return eval(expr)  # WARNING: Avoid eval() in production
        except Exception as e:
            raise ValueError(f"Error evaluating expression: {expr}") from e

    def print(self, *args):
        """Prints resolved tokens."""
        output = []
        for arg in args:
            resolved = self.resolve_token(arg)
            output.append(str(resolved))
        print(" ".join(output))  # Combine all parts into a single string



if __name__ == "__main__":
    memory = {
        "x": 10,
        "y": 5,
        "z": 3
    }

    console = Console(memory)

    # Simple print
    console.print('"Hello, World!"')

    # Variable print
    console.print('"Value of x is:"', "x")

    # Expression print
    console.print('"Sum of x and y is:"', "x + y")


