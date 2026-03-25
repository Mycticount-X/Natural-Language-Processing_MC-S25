import nltk

def download_nltk_resources():
    resources = [
        'punkt', 'punkt_tab', 'stopwords', 'wordnet', 
        'averaged_perceptron_tagger', 'averaged_perceptron_tagger_eng',
        'maxent_ne_chunker', 'maxent_ne_chunker_tab', 'words'
    ]
    for res in resources:
        try:
            nltk.data.find(f'tokenizers/{res}')
        except LookupError:
            try:
                nltk.data.find(f'corpora/{res}')
            except LookupError:
                try:
                    nltk.data.find(f'help/{res}')
                except LookupError:
                     try:
                        nltk.data.find(f'chunkers/{res}')
                     except LookupError:
                        print(f"Mengunduh {res}...")
                        nltk.download(res, quiet=True)

download_nltk_resources()