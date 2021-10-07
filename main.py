import scraper
import file_manager as fm
import email_manager as em
import os

def Main():
    print('Welcome to LyricScraper!')
    while True:
        lyr = scraper.query()
        if lyr != 'EXIT':
            f = fm.write_to_file(lyr)
            em.send_file(f)
            os.remove(f.name)
        else:
            break
    print('Goodbye!')
    scraper.quit()
    em.quit()

if __name__ == '__main__':
    Main()

