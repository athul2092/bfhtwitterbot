![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)
# Tweet Thread Saver
 A simple script that uses the Twitter API to save the tweet thread in a suitable form for later consumption.
## Team members
1. Ajmala Hannath [https://github.com/Ajmalahannath123]
2. Gopika Girish [https://github.com/Gopika-maker]
## Team Id
BFH/rec0dNSukwSW0e1Yl/2021
## Link to product walkthrough
[link to video]
## How it Works ?
1. Explaining the working of project
2. Embed video of project demo
## Libraries used
Django - 2.2
Tweepy - 3.10
## How to configure
```
git clone https://github.com/athul2092/bfhtwitterbot
cd bfhtwitterbot
pip install -r requirements.txt
```
Create a config.json file in root directory and add your twitter api credentials
```
{
"BOT_USERNAME" : "@botusername",
"CONSUMER_KEY" : "xxxxxxxxxxxxxxxxxxxxxxxxx",
"CONSUMER_SECRET" : "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
"ACCESS_KEY" : "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
"ACCESS_SECRET" : "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```
## How to Run
```
python manage.py runserver
```
By default the server will use port 8000
http://localhost:8000
