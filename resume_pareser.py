# pip install spacy==2.4.5
# pip install nltk
# import spacy.cli
# spacy.cli.download("en_core_web_sm")
# pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz
# import nltk
#  nltk.download("")
# python -m nltk.downloader words
# python -m nltk.downloader stopwords
from pyresparser import ResumeParser
data = ResumeParser('path').get_extracted_data()
print(data)
