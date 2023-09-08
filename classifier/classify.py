import pandas as pd
import joblib

def predict_species(input_list):
    # To load the model back
    loaded_rf = joblib.load('snake dataset/random_forest_model.sav')
    
    #test columns and mapped dictionaries
    test_columns = ['Thickness', 'Head shape', 'Head size', 'Colour', 'Pattern',
       'Nocturnal', 'Agility', 'Habitat', 'Length_normalized']
    
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

    # Create a dictionary to hold all mappings
    mappings = {
        'Thickness': thickness_mapping,
        'Head shape': head_shape_mapping,
        'Head size': head_size_mapping,
        'Colour': colour_mapping,
        'Pattern': pattern_mapping,
        'Nocturnal': nocturnal_mapping,
        'Agility': agility_mapping,
        'Habitat': habitat_mapping
    }

    # Replace values in input_list with mapped values from the dictionaries
    mapped_input_list = []
    for column, value in zip(test_columns, input_list):
        mapping = mappings.get(column, {})  # Get the mapping for the specific column
        mapped_value = mapping.get(value, 0)  # If not found, use -1(the original value/ provided)
        mapped_input_list.append(mapped_value)

    # Append the last numeric value to the mapped input list
    #mapped_input_list.append(input_list[-1])

    # Print the mapped input list
    #print("Mapped Input List:", mapped_input_list)
    
    #get mapped values
    input_df = pd.DataFrame([mapped_input_list], columns=test_columns)
    
    #result
    result = loaded_rf.predict(input_df)
    return str(result[0])

#input_list = ['moderate','hooded',	'large',	'brown',	'hood',	'Yes',	'fast', 'forests', 1.2] #indian cobra
#input_list = ['moderate','Triangular',	'large',	'gray',	'slow',	'Yes',	'slow', 'forests', 0.8] #malabar pit viper
#input_list = ['Very thick','large',	'elongated large',	'yellowish-brown',	'blotches',	'no',	'very slow', 'forests', 6] #malabar pit viper


#print(predict_species(input_list))
