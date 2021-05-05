from flask import Flask, render_template,request
from joblib import load
import pandas as pd
import numpy as np

app= Flask(__name__)
def load_sim():
    return load('sim.joblib')

def df():
    return pd.read_csv('movies_metadata.csv')
def indices(df):
    return pd.Series(df.index, index=df['title']).drop_duplicates()

def content_recommender(title, cosine_sim=load_sim(), df=df, indices=indices):
    # Obtain the index of the movie that matches the title
    idx = indices[title]
    # Get the pairwsie similarity scores of all movies with that movie
    # And convert it into a list of tuples as described above
    sim_scores = list(enumerate(cosine_sim[idx]))
    # Sort the movies based on the cosine similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Get the scores of the 10 most similar movies. Ignore the first movie.
    sim_scores = sim_scores[1:11]
    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]
    # Return the top 10 most similar movies
    return df['title'].iloc[movie_indices]


@app.route('/',methods = ['GET','POST'])
def index():    
    cosine=load_sim()
    df=df()
    indices=indices(df)
    if request.method == 'POST': # basic Flask structure 
        title = request.form['movie_name'] 
        while title!='':
            print(content_recommender(title,cosine,df, indices))
			#return '''{}'''.format(prsdata)
    return render_template('index.html')


if __name__=='__main__':
    app.run()