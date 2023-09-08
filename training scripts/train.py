
import pandas as pd
#from sklearn import datasets
from sklearn.metrics import confusion_matrix
#from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
import joblib

# Assuming you have a trained RandomForestClassifier in the variable 'rf'
# Save the model to a .sav file


def training():
    excel_file = 'Indian Snakes Dataset.xlsx'
    data = pd.concat(pd.read_excel(excel_file, sheet_name=None), ignore_index=True)


    data = data.drop(['Character', 'Venomous',
       'Type of Venom', 'Extra Information', 'Type of Venom.1'], axis=1)


    data = data.dropna()

    # Find rows with NaN values
    #rows_with_nan = data[data.isna().any(axis=1)]



    # Define the ordinal mapping for each categorical column
    thickness_mapping = {'moderate':4, 'thick':5, 'thin':3, 'Moderate':4, 'Thin':3, 'lean':1, 'slender':2,
   'elongated':6, 'Very thick':7, 'other':0}

    head_shape_mapping = {'hooded':9, 'Triangular':1, 'V-shapre':2, 'extension of body':3,
    'elongated':4, 'v shape':5, 'triangular':1, 'flatten':7, 'large elongated':8,
    'pointed':11, 'small':10, 'other':0}

    head_size_mapping ={'large':5, 'Large':5, 'Bigger than body':1, 'small':2, 'larger than body':1,
    'moderate':3, 'extension of body':4, 'elongated':5, 'other':0}

    colour_mapping = {'brown':1, 'black':2, 'green':3, 'blue':4, 'yellow':5, 'gray':6, 'yellow head':7,
    'black body':8, 'black and white':9, 'cream':10, 'grey':11, 'yellowish':12,
    'reddish brown':13, 'light brown':14, 'yellowish-brown':15, 'dark':16,
    'black white':17, 'glossy black':18, 'other':0}

    pattern_mapping = {'hood':1, 'blotches':2, 'stripes':3, 'black lines':4,
    'black and white lines':5, 'bands':6,
    'two white lines with black bands':7, 'white lines':8, 'back bands':9,
    'white lines ':10, 'alternating bands':11, 'solid colour':12,
    'lines near the mouth':13, 'lines on the face':14, 'checkered':15,
    'saw like scales':16, 'keeled scales':17, 'stripes or bands':18,
    'dark blotches':19, 'irregularly shaped blotches or patches':20, 'spots':21,
    'white bands':22, 'white stripes':23, 'white rings':24, 'yellow bands':25,
    'dark circles':26, 'zigzag ':27, 'dark round':28, 'vine-like':29, 'other':0}

    nocturnal_mapping = {'Yes':1, 'yes':1, 'No':2, 'no':2, 'other':0}

    agility_mapping = {'fast':3, 'slow':2, 'agile':4, 'very slow':1, 'tree climbers':5, 'other':0}

    habitat_mapping = {'forests':42, 'plains':1, 'agricultural lands':2, 'rocky terrain':3,
    'wetlands':4, 'Ghats':5, 'mountains':6, 'plains ':7, 'hills ':8, 'forests ':9,
    'plantations':10, 'close to water':11, 'lake':12, 'rivers':13, 'swamps':14,
    'marsh':15, 'bamboo thickets':16, 'mangrove swamps':17, 'fields':18,
    'woodlands':19, 'farmlands':20, 'residential areas':21, 'freshwater ponds':22,
    'lakes':23, 'streams':24, 'sand':25, 'rock':26, 'soft soil,':27, 'scrubland':28,
    'hilly forests':29, 'grasslands':30, 'marshes':31, 'rocky foothills':32,
    'forest':33, 'river valleys':34, 'forest edge':35, 'trees':36, 'farmland':37,
    'fields ':38, 'jungle ':39, 'settled areas':40, 'sandy beaches':41, 'other':0}

    #'Thickness', 'Head shape', 'Head size','Colour', 'Pattern', 'Nocturnal', 'Agility', 'Habitat'

    # Apply ordinal encoding to the categorical columns
    data['Thickness'] = data['Thickness'].map(thickness_mapping)
    data['Head size'] = data['Head size'].map(head_size_mapping)
    data['Head shape'] = data['Head shape'].map(head_shape_mapping)
    data['Colour'] = data['Colour'].map(colour_mapping)
    data['Nocturnal'] = data['Nocturnal'].map(nocturnal_mapping)
    data['Pattern'] = data['Pattern'].map(pattern_mapping)
    data['Habitat'] = data['Habitat'].map(habitat_mapping)
    data['Agility'] = data['Agility'].map(agility_mapping)



    min_length = data['Length'].min()
    max_length = data['Length'].max()
    max_range = 1
    min_range = -1
    # Normalize the 'Age' column using Min-Max scaling
    data['Length_normalized'] = (data['Length'] - min_length) / (max_length - min_length) * (max_range - min_range) + min_range


    data = data.drop('Length', axis=1)



    X = data.drop('Snake Name', axis=1)  # Replace 'target_column' with the name of your target variable
    y = data['Snake Name']  # Replace 'target_column' with the name of your target variable


    # Assuming X is your feature matrix, y is your target variable
    sss = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)



    # Split the data into training and testing sets using stratified sampling
    for train_index, test_index in sss.split(X, y):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]



    scores = []
    
    # using regression to get predicted data
    rf = RandomForestClassifier(n_estimators=40, max_depth=7)
    rf.fit(X_train, y_train)
    pred = rf.predict(X_test)
    scores.append(accuracy_score(y_test, pred))
    
    # get accuracy of each prediction
    print(scores)
    joblib.dump(rf, 'random_forest_model.sav')
    
    return 



if __name__ == '__main__':
    training()