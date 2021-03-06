# -*- coding: utf-8 -*-
"""Email Classification Using Bert.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YSJ9NJpu3eDi8KohgDVfLQAYd-lXvUWh

OVERVIEW:

In this tutorial notebook, we will be covering a simple approach to email classification(spam or not spam) using BERT

Steps are:
- We will load our data - mainly sentences and labels-span or not spam
- Load these in bert to generate an contextualized embedding vector of length 768

- - We will first apply preprocessing using the preprocessor object , refer the documentation

- - We will pass this preprocessed text to our model to generate the contexutailized embedding vector


- Finally pass this embedding vector to single neuron in output to do binary classificaton

- For maximizing performance we will be balancing our dataset and use a dropout layer to regularize the model and prevent overfitting

# Loading Dependencies

Includes
- Tensorflow_hub : Place where all tenseorflow pretrained models are stored.
- Pandas : For data loading, manipulation and wrangling.
- Tensorflow_text : Allows addditional NLP text processing capablities outside scope of tensorflow
- Skelarn : For doing data evaluation and splitting
- Matplotlib : For visualization
"""

# installing tensorflow_text
#!pip install tensorflow-text

import tensorflow_hub as hub
import pandas as pd
import tensorflow_text as text
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np

"""# Loading Data

- Read Data
- Display data
USING PANDAS
"""

# load data
df = pd.read_csv('spam_ham.csv')

df.head()

"""# Data Analysis

- Check the description by grouping by category :
* no of data points for each category - count
* no of unique values in each category - unique



"""

# check count and unique and top values and their frequency
df['label'].value_counts()

"""**Clearly dataset is imbalanced - not so much but still it can affect our model. Need to use some type of regulariztion like downsampling dataset for mazority class**

# Downsampling Dataset 

**Includes:**
- Check percentage of unbalances.
- Creating 2 new dataframes out of existing one.
- Taking any random minority no of samples - `(747)` for majority class`(4825)`.
- Creating a balanced dataset by concating 2 new data frames.
"""

# check percentange of data - states how much data needs to be balanced
str(round(747/4825,2))+'%'

# creating 2 new dataframe as df_ham , df_spam

df_spam = df[df['label']=='spam']
print("Spam Dataset Shape:", df_spam.shape)

df_ham = df[df['label']=='ham']
print("Ham Dataset Shape:", df_ham.shape)

# downsampling ham dataset - take only random 747 example
# will use df_spam.shape[0] - 747

df_ham_downsampled = df_ham.sample(df_spam.shape[0])
df_ham_downsampled.shape

# concating both dataset - df_spam and df_ham_balanced to create df_balanced dataset
df_balanced = pd.concat([df_spam , df_ham_downsampled])
df_balanced.head()

df_balanced['label'].value_counts()

df_balanced.sample(10)

"""# Data Prepration

1. Create Numerical Repersentation Of Category - One hot encoding
* Create a new column
* Use `df[col].apply(lambda function)`
* Lambda Function - if spam return 1, else return 0 (for ham) - ternary operators : [`lambda x : value expression else value`]
"""

# creating numerical repersentation of category - one hot encoding
df_balanced['spam'] = df_balanced['label'].apply(lambda x:1 if x=='spam' else 0)

# displaying data - spam -1 , ham-0
df_balanced.sample(4)

"""2. Do train-test split
* split dataset into 80-20 ratio with 80% train and remaing as test
* for eveness of data we will use `stratify` agrument which ensures same ratio of both category is loaded for each case, even if one categoy has more training samples - prevents overfitting 

Store our data in: 
- `X_train, y_train` - traininge set(training_data and labels respectively)
- `X_test,, y_test` - testing set(testing_data and labels)
"""

# loading train test split
from sklearn.model_selection import train_test_split

X_train, X_test , y_train, y_test = train_test_split(df_balanced['text'], df_balanced['spam'],
                                                    stratify = df_balanced['spam'])

# check for startification
y_train.value_counts()

#560/560

y_test.value_counts()

#187/187

"""***-> Almost similar, means data is downsampled now ***

# Model Creation 

Our Model is BERT , which will do 2 thing:
- Preporcess our training data that will be feeded - includes **adding additional token CLF , PAD and SEP** to genrate `input_mask`, `input_type_ids`, `input_word_ids(token given to each word in  sentences)` 

* Note: no of words in sentence - 128/ max length of sentence can be 128

## Downloading BERT

Model specification : 
- Layers - 12
- Hidden layers - 768 - embedding size
- Attention - 12
Name - Bert Small
---
This model has 2 parts:
- Bert_preprocessor - preprocess the text to be BERT ready
- Bert_encoder - do the actual encoding
---
Steps:
> Preprocessor
* create a keras hub layer from the preprocessing url 

> Encoder
* create a keras hub layer from the encoder/ model url

Awesome functionality provided by Tf hub API


                            +

Creating our own model using functional model api- link old layers to new layers rather than building it(in a sequential way) and allows sharing of layers too

Info:
- Text the embedding as input - text_input
- Create a Sinlge output dense layer
- Add dropout to reduce overfitting
"""

# downloading preprocessing files and model
bert_preprocessor = hub.KerasLayer('https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3')
bert_encoder = hub.KerasLayer('https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/4')

"""## Process And Encode Data

Use functional API to process and encode data in the layers itself

- Create a input layers with shape() , type - tf.string, and layer name - text - `TEXT_INPUT`

- Pass TEXT_INPUT into bert_prerocessor - `PREPROCESSED TEXT[*]`
- Pass the above[*] to encoder - `EMBEED`
- pass pooled_outputs of EMBEED to dropout layer - `DROPOUT`
- create a dense layer with activation as `sigmoid` `OUTPUTS`
- Create out MODEL (inputs - text_input, outputs - dropout) 
"""

import tensorflow as tf

text_input = tf.keras.layers.Input(shape = (), dtype = tf.string, name = 'Inputs')
preprocessed_text = bert_preprocessor(text_input)
embeed = bert_encoder(preprocessed_text)
dropout = tf.keras.layers.Dropout(0.1, name = 'Dropout')(embeed['pooled_output'])
outputs = tf.keras.layers.Dense(1, activation = 'sigmoid', name = 'Dense')(dropout)

# creating final model
model = tf.keras.Model(inputs = [text_input], outputs = [outputs])

# check summary of model
model.summary()

"""##  Compiling model

- Optimizer - ADAM
- Loss - binary_crossentropy
- metrics - accuracy , precesion and recall
"""

Metrics = [tf.keras.metrics.BinaryAccuracy(name = 'accuracy'),
           tf.keras.metrics.Precision(name = 'precision'),
           tf.keras.metrics.Recall(name = 'recall')
           ]

model.compile(optimizer ='adam',
               loss = 'binary_crossentropy',
               metrics = Metrics)

# Commented out IPython magic to ensure Python compatibility.
#@title Optional 
# optional - defining tensorflow callbacks
import tensorflow as tf
import datetime
# %load_ext tensorboard


log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
checkpoint_path = "training_2/cp-{epoch:04d}.ckpt"
tensorboard_callback=tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)
cp_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_path, 
    verbose=1, 
    save_weights_only=True,
    save_freq=2*71)
"""##  Training Model
- Recomended to use `GPU` - providing so many training data

- We traing our model on training set
- For 10 epochs only - so model don't overfit - given enough training data
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorboard --logdir logs/fit
model.save_weights(checkpoint_path.format(epoch=0))
history = model.fit(X_train, y_train, epochs = 5 , callbacks = [tensorboard_callback, cp_callback])

"""# Model Evaluation 

- Evaulating model performance 
using `model.evaluate(X_test, y_test)`

- Predicting X_test - `y_pred`
-- Checking its values as 1 or 0 
- Getting Confusion matrix
-- Flattening y_pred 
-- Ploting consufion matrix

- Getting classification report 
"""

# Evaluating performace
model.evaluate(X_test,y_test)

# getting y_pred by predicting over X_text and flattening it
y_pred = model.predict(X_test)
y_pred = y_pred.flatten() # require to be in one dimensional array , for easy maniputation

# checking the results y_pred
import numpy as np

y_pred = np.where(y_pred>0.5,1,0 )
y_pred

model.save("mymodel.h5")

"""**Not so understandable so plotting confusion matrix and classification report  for good visualization**"""

# importing consfusion maxtrix
from sklearn.metrics import confusion_matrix , classification_report

# creating confusion matrix 
cm = confusion_matrix(y_test,y_pred)
cm

# plotting as graph - importing seaborn
import seaborn as sns

# creating a graph out of confusion matrix
sns.heatmap(cm, annot = True, fmt = 'd')
plt.xlabel('Predicted')
plt.ylabel('Actual')

# printing classification report
print(classification_report(y_test , y_pred))

"""**Good Precesion And Recall Score, but can be improved**

# Model Prediction

- We will be predicting data on text coprus,
value > 5 is most likely be `spam`
"""

predict_text = [
                # Spam
                'We???d all like to get a $10,000 deposit on our bank accounts out of the blue, but winning a prize???especially if you???ve never entered a contest', 
                'Netflix is sending you a refund of $12.99. Please reply with your bank account and routing number to verify and get your refund', 
                'Your account is temporarily frozen. Please log in to to secure your account ', 

                #ham
                'The article was published on 18th August itself',
                'Although we are unable to give you an exact time-frame at the moment, I would request you to stay tuned for any updates.',
                'The image you sent is a UI bug, I can check that your article is marked as regular and is not in the monetization program.'
]

test_results = model.predict(predict_text)

output = np.where(test_results>0.5,'spam', 'ham')

output

"""# Additional Content

- Create a function which will take in `sentece array` and return the embedding vector for entire sentece -`pooled_output`
---
STEPS:
To do so inside the we follow 3 steps:

1. We `pass the sentence array to bert_preprocessor` as it can act a function point and name it **preprocessed_text**

2. Now we `pass this preprocessed sentence into encoder` and it return a embedding vector dictonary 

3. We retun only the `pooled output` as we are interested in only the entire sentence encoding

---
Later we compare the embedding vector using `cosine - similarity from sklearn.metrics.parwiase` class

"""

def get_embedding(sentence_arr):
    'takes in sentence array and return embedding vector'
    preprocessed_text = bert_preprocessor(sentence_arr)
    embeddings = bert_encoder(preprocessed_text)['pooled_output']
    return embeddings

e = get_embedding([
               'We???d all like to get a $10,000 deposit on our bank accounts out of the blue, but winning a prize???especially if you???ve never entered a contest',
               'The image you sent is a UI bug, I can check that your article is marked as regular and is not in the monetization program.'
])



# load similartiy score
from sklearn.metrics.pairwise import cosine_similarity

# check similarity score
print(f'Similarity score between 1st sentence(spam) and second sentence(spam) : {cosine_similarity([e[0]] , [e[1]])}')

"""* Not exact similarity, may show un expected results as can be seen - they are somewhat similar but its false as spam and actual can't be same"""
