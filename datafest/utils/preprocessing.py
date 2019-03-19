from nltk.corpus import stopwords
from sklearn.base import TransformerMixin
from nltk.tokenize import RegexpTokenizer

import chardet
import os


class ReadTextFiles(TransformerMixin):

    def __init__(self, ignored_files=None):
        if ignored_files is not None:
            self.ignored_files = ignored_files
        else:
            self.ignored_files = []

    def transform(self, root_folder, *_):
        contents = []
        for root, folder, file_names in os.walk(root_folder):
            for file_name in file_names:
                if file_name.endswith('.txt') and file_name not in self.ignored_files:
                    file_path = os.path.join(root, file_name)
                    try:
                        with open(file_path, 'r') as fp:
                            yield [line for line in fp.read().split('\n') if line]
                    except UnicodeDecodeError:
                        with open(file_path, 'rb') as fp:
                            raw_data = fp.read()
                        detected_encoding = chardet.detect(raw_data)
                        yield [line for line in raw_data.decode(detected_encoding['encoding']).split('\n') if line]

    def fit(self, *_):
        return self

class GetTextFileNames(TransformerMixin):

    def __init__(self, ignored_files=None):
        if ignored_files is not None:
            self.ignored_files = ignored_files
        else:
            self.ignored_files = []

    def transform(self, root_folder, *_):
        contents = []
        for root, folder, file_names in os.walk(root_folder):
            for file_name in file_names:
                if file_name.endswith('.txt') and file_name not in self.ignored_files:
                    yield os.path.join(root, file_name)

    def fit(self, *_):
        return self


class JoinText(TransformerMixin):

    def transform(self, documents, *_):
        for sentences in documents:
            yield ' '.join(sentences)

    def fit(self, *_):
        return self


class Tokenizer(TransformerMixin):

    def __init__(self, language='english'):
        self.language = language

    def transform(self, documents, *_):
        tokenizer = RegexpTokenizer(r'\w+')

        for document in documents:
            yield tokenizer.tokenize(document)

    def fit(self, *_):
        return self


class RemoveStopwords(TransformerMixin):
    def __init__(self, language='english'):
        self.language = language

    def transform(self, documents, *_):
        language_stopwords = set(stopwords.words(self.language))
        for document in documents:
            yield [token for token in document if token not in language_stopwords]

    def fit(self, *_):
        return self


class LowerCaser(TransformerMixin):

    def transform(self, documents, *_):
        for document in documents:
            yield [token.lower() for token in document]

    def fit(self, *_):
        return self


class ExecuteGenerator(TransformerMixin):

    def transform(self, documents, *_):
        result = []
        for document in documents:
            result.append(document)
        return result

    def fit(self, *_):
        return self
