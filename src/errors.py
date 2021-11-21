class Error(Exception):
    """Base class for other exceptions"""
    pass

class VectorWithDifferenceSizes(Error):
    """
    Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, v, w, message="Os dois vetores precisam ter o mesmo tamanho"):
        self.message = message
        self.v = v
        self.w = w
        super().__init__(self.message)

    def __str__(self):
        return f'vector len {len(self.v)} != vector len {len(self.w)}'