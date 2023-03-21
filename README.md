# Tarantula

## Examples

### Example 1: extract links from page

```python
from tarantula import select_all

@select_all('a', key='links')
def get_link(element):
    return element.attrs.get('href')
```

To run, execute `python tarantula/runner.py example/link_extractor.py <url>`.

### Example 2: extract data from Euler project website

```python
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
```

To run, execute `python tarantula/runner.py example/euler.py https://projecteuler.net/archives`.