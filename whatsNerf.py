# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 19:22:25 2018
@title: whatsNerf.py
@author: Robin
"""

# -*- coding: utf-8 -*-

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# WhatsApp parameters #
print('########################\n# Welcome to whatsNerf #\n########################\n\n')
victim = raw_input("Contact Name:\t")
msg = raw_input("Type Message:\t")

print('Have the text sent\n\ta. As one message (as usual)\n\tb. As single letters (very annoying for recipient)\n')
msg_style = raw_input("Choose: ")


if msg_style == 'a':
    
    print("\n\nKeep ready to scan WhatsApp Web QR-Code with your Phone as soon as it is loadad...")
    
    # Open WhatsApp Web in browser # (requires mobile phone to scan QR-code via WhatsApp) #
    browser = webdriver.Firefox(executable_path=os.getcwdu()+'\\lib\\geckodriver.exe')
    browser.get('https://web.whatsapp.com/')
    
    # Search for victim and open chat #
    searchfield = browser.find_element_by_css_selector('.jN-F5')
    searchfield.send_keys(victim+Keys.RETURN)
    
    # Send Message #
    msgfield = browser.find_element_by_css_selector('._2S1VP')
    msgfield.send_keys(str(msg)+Keys.RETURN)
    msgfield.send_keys('(sent by Borin\'s WhatsApp-Bot)'+Keys.RETURN)
    
    # done
    
elif msg_style == 'b':
    
    print("\n\nKeep ready to scan WhatsApp Web QR-Code with your Phone as soon as it is loadad...")
    
    # Message processing #
    msg = msg.replace(' ','-')
    msg = [c for c in msg]
    
    # Open WhatsApp Web in browser # (requires mobile phone to scan QR-code via WhatsApp) #
    browser = webdriver.Firefox()
    browser.get('https://web.whatsapp.com/')
    
    # Search for victim and open chat #
    searchfield = browser.find_element_by_css_selector('.jN-F5')
    searchfield.send_keys(victim+Keys.RETURN)
    
    # Send Messages #
    msgfield = browser.find_element_by_css_selector('._2S1VP')
    #msgfield.send_keys(''+Keys.RETURN)
    msgfield.send_keys('Bot START \\nerfMode = ON'+Keys.RETURN)
    
    for msg_c in msg:
        msgfield.send_keys(str(msg_c)+Keys.RETURN)
    
    msgfield.send_keys('Bot STOP'+Keys.RETURN)
    #msgfield.send_keys('(sent by Borin\'s WhatsApp-Bot)'+Keys.RETURN)
        
    # done
else:
    print('Error: Did not understand input')
    

