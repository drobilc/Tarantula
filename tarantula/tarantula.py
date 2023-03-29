def select_one(css, key=None):

    def extraction_function_wrapper(extraction_function):

        key_name = key if key is not None else extraction_function.__name__

        def outer_extraction_function(html):
            # Step 1: Find the element by css selector
            element = html.select_one(css)

            if element is None:
                return key_name, None

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
            def safe_extraction_function(element):
                if element is None: return None
                return extraction_function(element)

            return key_name, list(map(safe_extraction_function, elements))
        
        outer_extraction_function.__name__ = extraction_function.__name__

        return outer_extraction_function

    return extraction_function_wrapper

def extract(html, extraction_functions=[]):    
    if html is None:
        return None

    data = {}
    for extraction_function in extraction_functions:
        key, value = extraction_function(html)
        data[key] = value
    return data