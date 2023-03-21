from tarantula import select_all

@select_all('a', key='links')
def get_link(element):
    return element.attrs.get('href')