import numpy as np
import pandas as pd
global  cosine_sim , db
def load_artifacts():
    global cosine_sim
    global db
    cosine_sim = np.load(r'C:\Users\Mohamed\Downloads\projects\Movie Recommendation System Project\Model\cosine_sim.npy')
    db = pd.read_csv(r'C:\Users\Mohamed\Downloads\projects\Movie Recommendation System Project\Model\final.csv')
    return "success"


#def get_recommendations(title, db, cosine_sim):
def get_recommendations(title):
    # convert title to lower
    global db
    global cosine_sim
    get_ind = pd.Series(db.index, index=db.iloc[:,0])
    title = title.lower()

    # Get the index of the movie that matches the title
    try:

        ind = get_ind[title]
        # Get the pairwsie similarity scores of all movies with that movie
        sim_scores = list(enumerate(cosine_sim[ind]))

        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the 10 most similar movies * neglecting first because it reflects the same movie
        sim_scores = sim_scores[1:11]

        # Get the movie indices
        movie_indices = [i[0] for i in sim_scores]

        # Return the top 10 most similar movies
        # return saved_df['title'].iloc[movie_indices]
        return np.array(db.iloc[movie_indices][0:3])
    except:
        return np.array(["Movie Not Found","Try double checking movie name","Try another movie"])

