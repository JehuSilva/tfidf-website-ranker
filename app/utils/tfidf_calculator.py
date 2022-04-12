# packages
import numpy as np
import pickle

# Skip future warnings
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


class TfIdfCalculator():
    def __init__(self, models_directory = 'models/'):
        self.models_directory = models_directory
    
    def load_models(self):
        '''
        Loads the models from the filesystem
        '''
        self.vectorizer = pickle.load(open(
            self.models_directory + 'vectorizer', 'rb'
        ))
        self.tf_idf = pickle.load(open(
            self.models_directory + 'tf_idf', 'rb'
        ))

    @staticmethod
    def top_tfidf_feats(tokens, features, top_n=25):
        ''' 
        Get top n tfidf values in row and return them 
        with their corresponding feature names.

        Parameters
        ----------
        Xtr : sparse matrix, (n_samples, n_features)
            Training data.
        features : list, (n_features,)
            Feature names.
        top_n : int, optional
            Number of top features to return.

        Returns
        -------
        top_features : list of dicts
            List of top features with their names.
        '''
        topn_ids = np.argsort(tokens.toarray()).flatten()[::-1][:top_n]
        top_feats = {
            'terms': [{
                'term': features[i], 'tf-idf': round(tokens[(0,i)],3)
            } for i in topn_ids]
        }
        return top_feats
    
    def calculate_tfidf(self, article, top_n=10):
        '''
        Calculates the tfidf values for the given articles.

        Parameters
        ----------
        article : str
            Article to calculate the tfidf values.
        Returns
        -------
        tfidf : list
            List of tfidf values.
        '''
        tokens = self.vectorizer.transform([article])
        feature_names = self.vectorizer.get_feature_names()
        top_feats = self.top_tfidf_feats(tokens, feature_names, top_n=top_n)
        return top_feats
