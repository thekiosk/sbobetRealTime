from sbobetManager import sbobetManager
from collections import defaultdict
import re
 

class robotManager():
    def __init__(self):
        self.config = self.read_config()

    def read_config(self):
        configFile = './config.ini'
        #configFile = os.path.abspath('../control') + '/config.ini'
        oConfig = self.nested_dict(1,list)
        f = open(configFile, "r")
        for x in f:
            checkComment = re.match('^[#]', x.strip())
            if not checkComment and x.strip() != '':
                confDetails = x.strip().split('=')
                if len(confDetails) > 2 :                
                    j = 0
                    strData = ""
                    for item in confDetails :                                 
                        if j > 0:
                            if j == 1 :                            
                                strData = item
                            else :
                                strData = strData + "=" + item

                        j = j+1

                    oConfig[confDetails[0]] = strData            
                else:                
                    oConfig[confDetails[0]] = confDetails[1]
        return oConfig

    def nested_dict(self,n, type):
        if n == 1:
            return defaultdict(type)
        else:
            return defaultdict(lambda: nested_dict(n-1, type))

    def initialBot(self):
        self.botSbobet = sbobetManager(self.config)

    def killBot(self):
        self.botSbobet.close()        
 
if __name__ == '__main__':
    # Enter your login credentials here
    urls = {
        "url1":"https://www.hillapple.com/euro/football/english-league-one",
        "thailand":"https://www.hillapple.com/euro/football/thailand",
        "germany":"https://www.hillapple.com/euro/football/germany",
        "italy":"https://www.hillapple.com/euro/football/italy",
        "spain":"https://www.hillapple.com/euro/football/spain"        
    }
    bot = robotManager()
    bot.initialBot()

    for item in urls:        
        bot.botSbobet.get_RT_SBOBET(urls[item])

    bot.killBot()

    

   

    
