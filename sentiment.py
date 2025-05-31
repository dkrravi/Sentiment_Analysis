from textblob import TextBlob

sentence  = 'This is the best day of my life!'
blob =  TextBlob(sentence)
print(blob.sentiment.polarity)