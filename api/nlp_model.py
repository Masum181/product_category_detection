import pickle
import spacy

nlp = spacy.load('en_core_web_sm')

with open("./nive_bayes.sav", 'rb') as f:
    clf = pickle.load(f)

def preprocess(text):
    # remove stop words and lemmatize the text
    doc = nlp(text)
    filtered_tokens = []
    for token in doc:
        if token.is_stop or token.is_punct:
            continue
        filtered_tokens.append(token.lemma_)
    
    return " ".join(filtered_tokens) 

def pred_category(text):
    label = {
        0 : "Household",
        1: 'Books' , 
        2: "Electronics",
        3: "Clothing & Accessories"}
    preprocess_text = preprocess(text)

    y_pred= clf.predict([preprocess_text])
    return label[y_pred[0]]


t = "Operating Systems in Depth About the Author Professor Doeppner is an associate professor of computer science at Brown University. His research interests include mobile computing in education, mobile and ubiquitous computing, operating systems and distribution systems, parallel computing, and security."
