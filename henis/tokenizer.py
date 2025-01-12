import re

class Tokenizer:
    def __init__(self):
        # Define regex patterns for different token types
        self.token_patterns = [
            ("function_call", r'@[a-zA-Z_]\w*'),  # Function calls starting with @
            ("string", r'"[^"]*"'),              # Strings enclosed in double quotes
            ("number", r'\d+(\.\d+)?'),          # Integers or decimals
            ("variable", r'[a-zA-Z_]\w*'),       # Variables (alphabets + underscore)
            ("operator", r'[+\-*/=]'),           # Operators
            ("paren_open", r'\('),               # Open parenthesis
            ("paren_close", r'\)'),              # Close parenthesis
            ("whitespace", r'\s+'),     
            ("unknown", r'.'), # Unknown
            ('escape', r'"([^"\\]|\\.)*"')

              # Matches any unrecognized character
         # Whitespace (to be ignored)
        ]

        # Combine all patterns into a single regex
        self.master_pattern = re.compile("|".join(f"(?P<{name}>{pattern})" for name, pattern in self.token_patterns))

    def tokenize(self, code):
        tokens = []
        for match in self.master_pattern.finditer(code):
            token_type = match.lastgroup
            token_value = match.group(token_type)

            # Ignore whitespace tokens
            if token_type == "whitespace":
                continue

            tokens.append({"type": token_type, "value": token_value})
        return tokens

if __name__ == "__main__":

    code = '@print("Result is: " + (x + y)) -1'

    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(code)
    print(tokens)
    for token in tokens:
        print(token)
