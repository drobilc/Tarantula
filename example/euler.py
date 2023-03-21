from tarantula import select_all, select_one, extract

@select_all('#problems_table tr:not(:first-child)', key='problems')
def parse_row(element):

    @select_one('td.id_column')
    def id(element):
        return int(element.text)

    @select_one('td a')
    def title(element):
        return element.text.strip()
    
    @select_one('td div')
    def solved_by(element):
        return int(element.text)

    return extract(element, [ id, title, solved_by ])