#!/home/dd/anaconda3/bin/python
import requests, re, sys

def next_page(url):
    
    """Takes LibGen URL, returns the next page URL."""

    pre_url = 'http://gen.lib.rus.ec/search.php?req=windows+powershell+&open=0&res=25&view=simple&phrase=0&column=def'
    pre_next_page_url = 'http://gen.lib.rus.ec/search.php?&req=windows+powershell+&phrase=0&view=simple&column=def&sort=def&sortmode=ASC&page=2'
    
    m = re.search('req=(.*?)&', url)
    search_term = m.group(1)
    m = re.search('page=\d', url)
    
    if not m:
        next_page_url = pre_next_page_url.replace("windows+powershell+", search_term)
    else:
        m = re.search('\d{1,2}$', url)
        page_number = m.group(0)
        next_page_url = pre_next_page_url.replace('page=' + page_number, 'page=' + (str(int(page_number) + 1)))
        
    return(next_page_url)

if __name__ == '__main__':

    print(next_page(sys.argv[1]))
        