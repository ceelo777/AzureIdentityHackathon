# GoPhish
Microsoft Azure Identity Hackathon

https://drive.google.com/file/d/1Hxy9nVNXEQqmgu-LqElMMmy_6f9UiBE2/view?usp=sharing
link to the mymodel.h5 file  

# How to Run

Go to frontend and then run npm install and npm start.
Go to backend and pip3 install required dependencies and then run python3 app.py.

## Inspiration

As Microsoft interns, we were struck by the number of different phishing methods that might arise in our email inboxes when we completed our Security 101 Compliance training modules. Furthermore, we were also surprised at the information that we as employees should not be including in our emails, such as specific email addresses for OOF messages, protecting sensitive user information, etc. Thus, we were inspired to create a portal to help us ensure the security of the emails we send and receive. 

## What it does

GoPhish has two main pages leveraging the GraphAPI to send and receive mail, classifying the messages as malicious or not. On the first page, emails to be sent can be pasted into the console, where a Natural Language Processing (NLP) artificial intelligence model reads in the email and picks out potential vulnerabilities in the text. We used a deep learning model called BERT to predict whether an user inputted email would or would not be considered as spam. We trained BERT on over 7000 email samples containing a mix of spam and not spam emails, using techniques such as sentiment analysis and masked language analysis to learn patterns in what makes an email spam. These vulnerabilities are displayed on the console, and users are able to fix them before using the GraphAPI to send out the email. 

On the second page, a similar idea is applied using natural language processing to externally received emails. The GraphAPI loads in email history and our trained BERT model predicts whether each given email is or is not malicious. The ones that are spam are marked with a red tag, while those that are legitimate are marked with a green tag. Together, these two pages form a security checking schema for email phishing schemes. 

## How we built it

Our app is built with GraphAPI, React JS, CSS, Flask, Tensorflow, and Keras. 

GraphAPI: A large portion of our project hinders on the functionality of this API - as it is responsible for loading in emails, sending emails off of the input page, and more generally, linking a user’s email address to the webpage. 

React JS / Flask / CSS: Together, these three components form the backbone of our web application. The front end is rendered via React and CSS, and communicates with the backend via Flask. 

Tensorflow/Keras: The NLP portion forms the portion of our app responsible for deeming whether or not an email is malicious. During this hackathon, we trained a fully functioning deep learning model, using BERT (Bidirectional Encoder Representations from Transformers neural network) in tangency with the Spam Email database from Kaggle. This dataset was processed and fed through BERT, which was able to learn the patterns that spam emails typically follow and determine the accuracy of spam emails at over 80%. Tensorflow and Keras were used as the frameworks to deploy, train, and test BERT, where we saved the trained model and loaded the file into our webpage for use in the backend. 

## Challenges we ran into

GraphAPI: Our team was unfamiliar with Microsoft Identity and the API’s available for use. It was a big challenge to familiarize ourselves with the API. We learned how to create Azure Active Directory apps, and use the clientID, tenantID, and clientSecret keys to enable support for our GraphAPI web app. There were some gaps in our knowledge that we had to fill by reading through various forms of documentation on the API, and ultimately be able to authenticate and use GraphAPI for our site end to end. As employees, it was great to be able to get to know another portion of the company and the cool API’s we have to offer! 

NLP/BERT: It was a similar challenge to have leveraged deep learning as part of our project. The training process and connection of BERT to our web app required a lot of interfacing between the different components. It took a while to train our model, and it was a great learning experience to utilize Flask to incorporate ML pieces into our webpage. 

## Accomplishments that we're proud of

We’re proud of being able to build a fully functioning web page by the end of this hackathon. Coming in with little to no knowledge on Microsoft Identity API’s, the successful integration of the GraphAPI with Machine Learning, Flask, and CSS was a big accomplishment for us. 

## What we learned

Microsoft Identity API usage and impact potential 
Integration of Machine Learning with Flask and CSS 
Front end positioning, table integration, interfacing with backend 
Time management for ensuring all pieces of our project can come together

## What's next for GoPhish

The ultimate goal for GoPhish is to be integrated into Outlook itself for seamless email flagging and sending. Having a tool to ensure that users are not accidentally leaking sensitive information in the emails they send, as well as a tool that checks the security of emails received is extremely important for cybersecurity. We hope to build upon GoPhish, incorporating more thorough email checking using sentiment analysis and build out a more sophisticated user interface to link directly to an email client such as Outlook. 
