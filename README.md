# Recommender System :zap:
This is a movie content based recommender system. This system uses tfidf and the cosine similarities. The output of the system is 10 other similar movies
> Tried to deploy the model using flask, however due to hardware constraints was not able to. However a working example of the system is saved in the `.ipynb` file. Feel free to take a  look at that out ! 
## Dataset  :tada:
The dataset used for the recommender system is `movies_metadata` from [ Kaggle ] ( https://www.kaggle.com/rounakbanik/the-movies-dataset ) <br>Using tfidf and cosine similarites took a toll on the RAM and even caused  Google colab to crash. To solve the probem used 1/3 of the dataset 

# TFIDF
TF-IDF is an abbreviation for Term Frequency Inverse Document Frequency. This is very common algorithm to transform text into a meaningful representation of numbers which is used to fit machine algorithm for prediction.

# Cosine similarity
Cosine similarity is a metric used to measure how similar two items are. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The output value ranges from **0–1**.

> **_0 means no similarity, where as 1 means that both the items are 100% similar._**
# Contributing Help :boom:

If you are really interested in contributing to the please follow the below steps and rules.
1. Fork the project :fork_and_knife: (Star :star: the repo before that :stuck_out_tongue:)
2. Clone it.

3. Look for any issues clicking the issues tab. Go through it and assign take one. Make sure you get assigned or atleast say that you are gonna work on it.
5. Always create a new branch and work on the feature or bug. Check this if you are not that familiar with branching, [Git Branching](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging).
6. If you are using any other module for implementing any new features, please install the modules in the virtual environment and update it in the `requirements.txt` by using the below command.
```
pip freeze > requirements.txt
```

If you have any doubts or issues, let the maintainers know about it. They would be ready to help.

# ToDo
- [ ] Add a final page for flask deployment, as of now the model 
