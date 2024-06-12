from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

reviews = [
 "I hate this new feature. Now I do not want to use this app.",
 "Oh, this feature is cool! I am enjoying this app now more.",
 "This new feature is not good.",
 "This new feature is not bad.",
 "Neither here nor there."
]

for review in reviews:
  scores = sia.polarity_scores(review)
  print(review)
  print(scores)
  print()