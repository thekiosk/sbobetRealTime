from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from lxml import html

 
class sbobetManager():
    def __init__(self,config, browser='Chrome'):
        if browser.upper() == 'CHROME':
            # Use chrome
            
            chromeDriver_path = config['chromeDriver_path']
            chrome_driver = chromeDriver_path + '/chromedriver'
            s = Service(chrome_driver)
            opts = Options()
            opts.add_argument('--headless')
            opts.add_argument('--no-sandbox')
            opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36")                
            self.driver = webdriver.Chrome(service=s, options=opts)
  
    def get_RT_SBOBET(self, url):      
        self.driver.get(url)
        content = self.driver.page_source        
        elements = html.fromstring(content).xpath('/html/body/div[2]/div[2]/div[2]/div[4]/div/div[2]/div[3]/div/div[2]/table')
        
        for tbl in elements:
            #elements = tbl.xpath('.//tr/td//text()')
            rows = tbl.xpath('.//tr')
            for row in rows:
                print(row.xpath('.//td//text()'))
                cols = row.xpath('.//td//text()')                
                #for col in cols:
                #    print(col)        
    
    def close(self):      
        self.driver.close()
        self.driver.quit()  
        print("Close SBOBET connection !!!")
 