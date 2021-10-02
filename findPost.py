from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time
# import songline

# hide google chrome
opt = webdriver.ChromeOptions()
opt.add_argument('headless')

driver = webdriver.Chrome(executable_path='/Users/anousonefs/Downloads/chromedriver', options=opt)

def twitterPostName(name):
    url = f'https://twitter.com/{name}'

    driver.get(url)
    time.sleep(15)

    # scrolling
    # pixel = 10000
    # for i in range(3):
    #     driver.execute_script("window.scrollTo(0, {})".format(pixel))
    #     time.sleep(3)
    #     pixel = pixel + 10000

    page_html = driver.page_source
    # print(page_html)

    data = soup(page_html, 'html.parser')
    posts = data.find_all('span', {'class':'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})

    founddot = False
    post_all = []

    for p in posts:
        if founddot:
            post_all.append(p.text)
            founddot = False

        if p.text == '·':
            founddot = True
    # driver.close()

    # separator = ' | '
    # print(separator.join(post_all))
    return post_all

checkTwitter = ['elonmusk', 'BillGates', 'cnnbrk', 'SpaceX']

for ct in checkTwitter:
    post = twitterPostName(ct)
    print(f'------------{ct}-------------') 
    for p in post:
        print(p)
        print('--------')

driver.close()