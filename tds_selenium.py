from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from re import search
from datetime import date
import sys
import random
import pandas as pd
#  learn logging https://docs.python.org/3/howto/logging-cookbook.html


# mobile_emulation = { "deviceName": "Nexus 5" }
options = webdriver.ChromeOptions()
options.add_argument ("lang = en_us")
# options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_argument("--headless")
driver = webdriver.Chrome(executable_path='chromedriver.exe',options = options)
# driver.maximize_window()
driver.set_window_position(-1500, 100)
# driver.implicitly_wait(5)
# driver.get("https://www.leons.ca")
# sleep(1)
# driver.find_element_by_xpath("//div/a[@class='ltkmodal-close'][@title='Close']").click()

# set source urls
urls = [
    'https://towardsdatascience.com/',


    ]


def retry_next():
    next_butt_selector = ".pagination-list-next a"
    if len(driver.find_elements_by_css_selector(next_butt_selector)) > 0:
        click_attempt = 0
        while click_attempt < 2:
            try:
                driver.execute_script("window.scrollTo(0, 300);")
                sleep(1)
                driver.find_element_by_css_selector(next_butt_selector).click()
                sleep(1)
                scrape()
            except:
                print("error\nretrying")
                click_attempt += 1
                print(click_attempt)
            finally:
                pass



# setting lists to collect scraped data
article_url_list = []
article_title_list = []
listitem_list = []
# surface_list = []
# cart_list = []
# originurl_list = []
# listitem_list = []




# setting dataframe to collect lists of data
df = pd.DataFrame()
# (columns= [
#     'modelUrl',
#     'model',
#     'surface',
#     'cart',
#     'origin_url',
#     'sitename'
# ])

def close_footer():
    footer_selector = "//div/a[@class='cookiebar-close']"
    if len(driver.find_elements_by_xpath(footer_selector)) > 0:
        try:
            driver.find_element_by_xpath(footer_selector).click()
        except:
            print('No footer')
            
def scrape():
    listitem = 0
    for cell in driver.find_elements_by_css_selector(cell_selector):
        # driver.execute_script("window.scrollTo(0, 100);")
        listitem += 1
        print(listitem)
        article_url = cell.find_element_by_css_selector(url_selector).get_attribute('href')
        # driver.execute_script("window.scrollTo(0, -200);")
        article_title = cell.find_element_by_css_selector(title_selector).text
        print(article_url)
        print(article_title)
        # push data to list

        article_url_list.append(article_url)
        article_title_list.append(article_url)
        # originurl_list.append(url)
        listitem_list.append(listitem)
                                                                # ** ? if "open-box" not in modelurl: doesn't work??? nvm it does. I'm just fuckin stupid
        # if len(cell.find_elements_by_css_selector(surface_selector)) > 0:
        #     surface = cell.find_element_by_css_selector(surface_selector).get_attribute('innerHTML').replace('$','').replace(' ','')
        #     print(surface)
        #     print('pushed surface')
        #     surface_list.append(surface)
        # else:
        #     surface_list.append('')

    


# scraping data
url_count = 0
for url in urls:
    url_count += 1
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # close_footer()


    # setting selectors in url loop and after get url due to "stale" error
    cell_selector = "div.postItem"
    url_selector = "a"
    title_selector = "span"

    # next_butt_selector = ".pagination-list-next a"

    scrape()
    print("Navigating to url # " + str(url_count) + " out of 10")
    # if len(driver.find_elements_by_css_selector(next_butt_selector)) > 0:
    #     retry_next()


                                                    # ** todo Need to add scroll down command before selectors each loop
                                                    # ** todo add next button clicker

                                                    # ** todo also, shit aint consistent between runs. It'll scrape correctly sometimes and others we'll get a stale element error or no attached to DOM or some shit
                                                    # ** ? really gotta figure out this consistency thing. It's pretty terrible



    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # sleep(1)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # sleep(2)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # sleep(2)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # sleep(1)
        # # if len(driver.find_elements_by_css_selector("//div[@role='main']/div/div/button[@type='button'][@aria-label='Minimize window']")) > 0:
        # #     driver.find_element_by_css_selector("//div[@role='main']/div/div/button[@type='button'][@aria-label='Minimize window']").click()
        # driver.find_element_by_css_selector(next_butt_selector).click()
        # sleep(3)
    # cleaning selectors

    # model_link = modelurl_selector.get_attrbute('href')





# load lists of scraped data into data frame
# todo add items scraped through dataframe count



df['article url'] = article_url_list
df['article title'] = article_title_list
df['list item'] = listitem_list
df['siteName'] = 'Towards Data Science'


print(df.head())
print(f'{df["siteName"].count()} items scraped')
print('Exporting df to csv')
                            #* todo input some kinda index=false in df.to_csv
                            #*  todo maybe add a list item?? idk. idk what I'm doing tbh
df.to_csv(r'E:\Downloads2\tds_selenium_' + str(date.today()).replace('-','') + '.csv', index = False)




# def working(self):







    
sleep(3)
print('closing')
driver.quit()
sys.exit()

# print('init')        
# leons_sel = leons()
# print('close init')
#     leons_sel.scraping()
#     print(product_selector)

# leons_sel.close()
# leons_sel.openDM()
# leons_sel.sendDM()
# print('after sendDM')
# my_bot.closeDM()
