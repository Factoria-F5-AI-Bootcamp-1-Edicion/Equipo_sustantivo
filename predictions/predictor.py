import pandas as pd
import tensorflow as tf

loaded_vectorize_layer_model = tf.keras.models.load_model('vectorize_layer_model')
loaded_vectorize_layer = loaded_vectorize_layer_model.layers[0]

model = tf.keras.models.load_model('toxicity.Pablo')

Data = pd.read_csv('comments_5vF4si3hoRA_05-12-2022.csv')

res = model.predict(loaded_vectorize_layer((Data)['Text']))
res = (res>0.5).astype(int)
Datares = pd.DataFrame(res, columns=['IsToxic', 'IsAbusive', 'IsThreat', 'IsProvocative', 'IsObscene', 'IsHatespeech', 'IsRacist', 'IsNationalist', 'IsSexist', 'IsHomophobic', 'IsReligiousHate', 'IsRadicalism'])
Datafinal = pd.concat([Data, Datares], axis=1)

Datafinal.to_csv('predicciones.csv')
