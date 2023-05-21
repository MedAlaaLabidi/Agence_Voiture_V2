import pandas as pd
import datetime
from sklearn.preprocessing import OneHotEncoder



class transformation:
    def __init__(self, dateCirculationTo="age"):
        self.dateCirculationTo = dateCirculationTo

    def fit(self, df):
        df_ = df.copy()
        # marquecouleur = pd.DataFrame()
        self.OHE = OneHotEncoder()
        self.OHE.fit(df_[['marque']])
        self.OHE1 = OneHotEncoder()
        self.OHE1.fit(df_[['couleur']])

    def transformer(self, df):
        df_transformer = df.copy()

        df_transformer.drop(columns=['matricule'], axis=1, inplace=True)

        df_transformer['date_circ'] = pd.to_datetime(df_transformer['date_circ'], format='%d/%m/%Y')
        df_transformer['age'] = datetime.datetime.now().year - df_transformer['date_circ'].dt.year
      
        df_transformer = df_transformer.drop(columns=['date_circ'], axis=1)

        transformedMarque = self.OHE.transform(df_transformer[['marque']]).toarray()
        df_transformer["Marque_"+self.OHE.categories_[0]] = transformedMarque

        transformedCouleur = self.OHE1.transform(df_transformer[['couleur']]).toarray()
        df_transformer["Couleur_" +self.OHE1.categories_[0]] = transformedCouleur

        df_transformer.drop(columns=['marque'], axis=1, inplace=True)

        df_transformer.drop(columns=['couleur'], axis=1, inplace=True)

        return df_transformer


if __name__ == '__main__':
    df = pd.read_csv("dataset.csv", sep=';')
    transformation = transformation("age")
    transformation.fit(df)
    df_transformer = transformation.transformer(df)
    print(df_transformer)
