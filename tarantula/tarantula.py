def select_one(css, key=None):

    def extraction_function_wrapper(extraction_function):

        key_name = key if key is not None else extraction_function.__name__

        def outer_extraction_function(html):
            # Step 1: Find the element by css selector
            element = html.select_one(css)

            # Step 2: Execute function for one element
            return key_name, extraction_function(element)

        return outer_extraction_function

    return extraction_function_wrapper

def select_all(css, key=None):

    def extraction_function_wrapper(extraction_function):

        key_name = key if key is not None else extraction_function.__name__

        def outer_extraction_function(html):
            # Step 1: Find the element by css selector
            elements = html.select(css)

            # Step 2: Execute function for each element
            return key_name, list(map(extraction_function, elements))
        
        outer_extraction_function.__name__ = extraction_function.__name__

        return outer_extraction_function

    return extraction_function_wrapper

def extract(html, extraction_functions=[]):
    data = {}
    for extraction_function in extraction_functions:
        key, value = extraction_function(html)
        data[key] = value
    return data