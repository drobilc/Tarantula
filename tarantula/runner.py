import requests
from bs4 import BeautifulSoup
import argparse
import inspect
import importlib.util
from pprint import pprint
import tarantula

def get_page_source(url):
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html5lib')
    return html

def get_extraction_functions(module_name, reserved_function_names=[]):
    spec = importlib.util.spec_from_file_location(module_name, module_name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Get all function names
    functions = []
    for name, obj in inspect.getmembers(module):
        if not inspect.isfunction(obj): continue
        if name in reserved_function_names: continue
        functions.append(obj)
    
    return functions

def run(arguments):
    html = get_page_source(arguments.url)
    
    # Get reserved function names (located in tarantula/tarantula.py). The user
    # can not use those names in their parser.
    reserved_names = [name for name, obj in inspect.getmembers(tarantula) if inspect.isfunction(obj)]

    # Find all functions in the parser python file.
    extraction_functions = get_extraction_functions(
        arguments.parser,
        reserved_function_names=reserved_names
    )
    
    result = tarantula.extract(html, extraction_functions)
    return result

if __name__ == '__main__':

    # Construct a parser and add arguments
    parser = argparse.ArgumentParser(
        prog='Tarantula',
        description='A web scraper that extracts data by parsing the source code of a website.',
    )
    parser.add_argument('parser')
    parser.add_argument('url')
    
    # Parse arguments
    arguments = parser.parse_args()
    
    # Get the page source and extract data.
    result = run(arguments)

    # Output data
    pprint(result)