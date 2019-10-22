#TOKENIZATION
from nltk.tokenize import word_tokenize, sent_tokenize
#from nltk.tokenize import PunktSentenceTokenizer
sentence = "Hello Mr. Human, how are you today? The weather is great and python is awesome. I am running like the wind"
sentence_token = sent_tokenize(sentence)
word_token = word_tokenize(sentence)

#STOP WORDS
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
print(stop_words)

filtered_sentence = []

for w in word_token:
        if w not in stop_words:
            filtered_sentence.append(w)
        
#filtered_sentence = [w for w in word_token if not w in stop_words]
print(filtered_sentence)

#STEMMING
from nltk.stem import PorterStemmer
ps = PorterStemmer() 
stemmed_sentence = []
for w in filtered_sentence:
    stemmed_words = (ps.stem(w))
    stemmed_sentence.append(stemmed_words)
    

#LEMMATIZATION
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

lemmatized_sentence = []
for w in filtered_sentence:
    lemmatized_words = lemmatizer.lemmatize(w)
    lemmatized_sentence.append(lemmatized_words)
    

#PARTS OF SPEECH
from nltk import pos_tag    
pos_word = pos_tag(filtered_sentence)