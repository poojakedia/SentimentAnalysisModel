
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier



negative_texts = [ "we hate you", "they hate us", "you are bad", "he is bad", "we hate mary", "he is the worst", "they are the worst", "she is terrible", "this feels terrible", "we dislike you", "they dislike us"]


positive_texts = ["we love you", "they love us", "you are good", "he is good", "they love mary", "he likes you", "I like you", "she is nice", "you are nice", "she is kind", "they are kind"]


training_texts = negative_texts + positive_texts


training_labels = ["negative"] * len(negative_texts) + ["positive"] * len(positive_texts)



test_texts = [ "they love mary", "they are good", "why do you hate mary", "they are almost always good", "we are very bad", "he is terrible", "you are very nice", "my mom is very kind"] 


vectorizer = CountVectorizer()


vectorizer.fit(training_texts)


training_vectors = vectorizer.transform(training_texts) 

 
testing_vectors = vectorizer.transform(test_texts)


classifier = DecisionTreeClassifier() 


classifier.fit(training_vectors, training_labels) 


predictions = classifier.predict(testing_vectors) 




text = "he is terrible"

def sentiment_classification(text):
  

  text_vector = vectorizer.transform([text])


  prediction = classifier.predict(text_vector)



  return prediction[0]

