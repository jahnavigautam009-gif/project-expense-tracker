from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample training data
texts = ["pizza", "burger", "uber", "bus", "shirt", "amazon"]
labels = ["Food", "Food", "Travel", "Travel", "Shopping", "Shopping"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

def predict_category(expense_text):
    X_test = vectorizer.transform([expense_text])
    return model.predict(X_test)[0]
