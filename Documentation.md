# Intent Analysis (on Audio Input)

## Challenges Faced

When considering NLP problems the main challenge is that the input data (i.e. Text data) should be clean, and should be absent of any syntactic and semantic errors.
But when considering the same problem with an audio input, a lot of things go haywire, i.e the way of saying a word for different human beings would be different, creating a lot of misspelled words and syntactic errors.

### Approaches

The very first step to approaching any audio based input is to convert it into a textual representation.
Once converted we can apply the following approaches to addressing the problem;

#### Supervised Approaches

When considering supervised approach we have tagged sentences, with these tagged sentences we can perform the following;
```bash
1) Utilise the most frequent item(word) set present with the use of Apriori Algorithm in a specific category and utilizing the top 30 - 40 percent to identify the intents

2) Take the tfidf and with a CBOW approach, with a sequential neural network to categorise into intent buckets

3) Use predefinded word-vectors and utilize it to train a neural network
```
#### Unsupervised Approaches

For the Unsupervised way of dealing this prolem would be;
```bash
1) If its a domain specific, then we could do is that we could use pre-trained word vector to create n-intent clusters and with a human intervention assign tags to those clusters and compute the similarity between the new text input to the vector

2) If its a domain independent, we can the pre-define some of the categories and compute the distance in-between the text and all the categories predefined.
```

### Approach Utilized

The approach can be broken down in the following sub steps;

```bash
1) Coversion of Audio data into text: Utilized Google Cloud API Service for converting the input audio file to a text format. The Api service is just a post call that takes the audio file and processes it on the cloud and returns the text extracted

2) Extracted the Noun Phrases present, this process is known as chunking, where you exploit a specific grammatical pattern present to extract your crucial information, and noun phrases in proper text data follow a specific pattern and also this is supervised with trained corpus in nltk

3) Calculate the average vector for the extracted noun phrases

4) Do a distance analysis from the pre-defined categories

5) Extract the top n categories that the sentence is closer to
```

#### Challenges
```bash
1) There would be chances that the word we are looking for is not present in the pre-defined embedding dictionary, also known as out-of-vocab problem,
for tacking this, we can scrape the internet and can end up with related words in the embedding, and with those we can eventually construct the vector of the unknown word

2) Speech to text output is not very satisfactory, for this we need to analyse and tune parameters like the sampling rate and compare to see which works best for us.
```

# Sentiment Analysis (on Audio Input)

## Deduction

So in this part we have an advantage over the intent analysis because understanding sentiment we can takes two factors in mind;
```bash
1) The features of the audio wave, will play a crucial part as people are more expressive and emphasise on words, which can be captured.

2) The extracted words can also be used to identify the polarity of the sentence

```
For extracting features we can use pyAudioAnalysis, scipy.io libaries to visualise and feature extraction on a wav file,
which can eventually be used for a supervised method to train a neural network and estimate the sentiment polarity of the audio file.

This can be further be backed up with the converted text analysis and eventually can be a better solution to sentiment analysis.