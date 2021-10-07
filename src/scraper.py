from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_path = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(driver_path)
driver.set_window_position(-10000, 0)

driver.get('https://www.azlyrics.com/')

def query():
    song = input("Enter a song to search or type 'EXIT' to exit: ")
    if song.upper() == 'EXIT':
        return 'EXIT'

    search = driver.find_element_by_tag_name('input')
    search.send_keys(song)
    search.send_keys(Keys.RETURN)
    try:
        driver.find_element_by_tag_name('table')
    except:
        driver.quit()
        print("No results found!")
        return

    obj_link = driver.find_element_by_tag_name('tr')
    artist = obj_link.text[obj_link.text.find('1. ')+2:]
    print('Getting lyrics for {}...'.format(artist))
    driver.find_element_by_link_text(obj_link.text).click()
    print('Done!')

    lyr_body = driver.find_element_by_class_name('az-song-text').text
    lyrics = lyr_body[lyr_body.find("(ad)")+5:lyr_body.find("Submit Corrections")].split("\n")
    return [artist, lyrics]

def quit():
    driver.quit()



