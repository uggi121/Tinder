# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 21:55:27 2019

@author: Rahul
"""
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup


def scraper(string):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    link = 'https://www.google.com/search?q='+string+'&rlz=1C1CHBF_enSG844SG844&sxsrf=ACYBGNQgJj-CMJn_9P22w6sHIlgAB4yzBA:1570889350040&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjh88Lt8pblAhW58HMBHcfVA7UQ_AUIEigB&biw=1504&bih=843&dpr=1.5'
    try:
        req = Request(url = link, headers=headers)
    except: 
        req =link
    page = urlopen(req).read()
    soup = BeautifulSoup(page)
    counter = 0
    for img in soup.find_all('img'):
        print(img)
        with open("image" + str(counter),'w') as f:
            f.write("images/"+urlopen(img['src']).read())
        counter += 1
        if counter >30:
            break
scraper("willsmith")


'''
from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os
import argparse
import sys
import json

# adapted from http://stackoverflow.com/questions/20716842/python-download-images-from-google-image-search

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

def main(args):
	parser = argparse.ArgumentParser(description='Scrape Google images')
	parser.add_argument('-s', '--search', default='bananas', type=str, help='search term')
	parser.add_argument('-n', '--num_images', default=10, type=int, help='num images to save')
	parser.add_argument('-d', '--directory', default='/Users/gene/Downloads/', type=str, help='save directory')
	args = parser.parse_args()
	query = args.search#raw_input(args.search)
	max_images = args.num_images
	save_directory = args.directory
	image_type="Action"
	query= query.split()
	query='+'.join(query)
	url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
	header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
	soup = get_soup(url,header)
	ActualImages=[]# contains the link for Large original images, type of  image
	for a in soup.find_all("div",{"class":"rg_meta"}):
	    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
	    ActualImages.append((link,Type))
	for i , (img , Type) in enumerate( ActualImages[0:max_images]):
	    try:
	        req = urllib2.Request(img, headers={'User-Agent' : header})
	        raw_img = urllib2.urlopen(req).read()
	        if len(Type)==0:
	            f = open(os.path.join(save_directory , "img" + "_"+ str(i)+".jpg"), 'wb')
	        else :
	            f = open(os.path.join(save_directory , "img" + "_"+ str(i)+"."+Type), 'wb')
	        f.write(raw_img)
	        f.close()
	    except Exception as e:
	        print "could not load : "+img
	        print e

if __name__ == '__main__':
    from sys import argv
    try:
        main(argv)
    except KeyboardInterrupt:
        pass
    sys.exit()
'''