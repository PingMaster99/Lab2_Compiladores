from antlr4.error.ErrorListener import ErrorListener


class ErrorGenerator:
    def __init__(self, message, line=None):
        self.message = message
        self.line = line

    def __repr__(self):
        if self.line:
            return f"ERROR: {self.message} [LINE {self.line}]"
        else:
            return f"ERROR: {self.message}"


class ErrorListener(ErrorListener):
    """
    Overrides the antlr4 error listener in order to display error messages in GUI
    """
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"ERROR: {msg} [LINE {line}:{column}]")

