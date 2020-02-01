import discord
import random
import configparser
config = configparser.ConfigParser()
def loadconfig():
    config = configparser.ConfigParser()
    config.read('config.sffc')
    Version = config['Data']['version']
    token = config['Data']['token']
    alttoken = config['Data']['alttoken']
    prefix = config['Data']['prefix']
    currency = config['Data']['currency']
    return Version, token, alttoken, prefix, currency;
def cserverconfig(sID, sCH, sMO):
    config = configparser.ConfigParser()
    config.add_section("Data")
    config.add_section("Flags")
    config['Data']['Version'] = '1'
    config['Data']['Server ID'] = sID
    config['Flags']['SuggestChannel'] = sCH
    config['Data']['Moderators'] = sMO
    with open(sID + '.sffs', 'w') as configfile:
        config.write(configfile)
def lserverconfig():
    config = configparser.ConfigParser(sID)
    config.read(sID + '.sffs')
    sID = config['Data']['Server ID']
    sCH = config['Flags']['SuggestChannel']
    sMO = config['Data']['Moderators']
    return sID, sCH, sMO;
def cuserconfig(money, uID):      #Actually just writes money
    config = configparser.ConfigParser()
    config.add_section("Metadata")
    config.add_section("Economy")
    config['Metadata']['UserID'] = uID
    config['Metadata']['Version'] = '1'
    config['Economy']['money'] = money
    with open(uID + '.sffu', 'w') as configfile:
        config.write(configfile)
def luserconfig(uID):      #Actually just returns amount of money
    config = configparser.ConfigParser()
    config.read(uID + '.sffu')
    Money = config['Economy']['money']
    return Money
    
    

