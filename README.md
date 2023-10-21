# spammer
Spam those bootlickers out of existence! but what?
Fake Information provided by [Fake Name Generator](https://www.fakenamegenerator.com "Fake Name Generator")

## Instructions

pip install -r requirements.txt

1. Configure the options you need at the top of the file.
```python
# Change configuration settings here.
config.zipFile = "fake-details.zip"
config.fakeDetailsFile = "FakeNameGenerator.com-100000-UK,US,AUS,CAN.csv"
config.fakeDetailsLength = 100000
config.multiThreading = True
config.multiThreads = 50
```
2. Add your target URL to the variable in the make_request function.
```python
url = '[https://ago.mo.gov/file-a-complaint/transgender-center-concerns](https://canarymission.org/contact_us)'
```
3. Configure your web request in the data variable. Use the person variable created from the fakePerson class to get your fake information (see example).
```python
data = {'msg':"method",'method':"/contact_us/insert",'params':'[{"email":'+person.email+'","contactType":"Submit a Name","message":"'+person.firstName+" "+person.lastName+'- '+person.username+' on twitter and '+person.username+'1998 on insta. very anti israel and advocating for the killing of israeli children. Is a '+person.occupation+'"}]','id':"1",'randomSeed':id_generator(20, "abcdefghijklmnopqrstuvwxyz1234567890")}


```
5. Run and Attack!
