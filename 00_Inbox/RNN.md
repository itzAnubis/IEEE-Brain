id: 202411261002 
author: Ahmed Sherif
type: concept 
status: needs_review 
domain: [[AI]] 
concepts: [[Sequence Models]], [[NLP]] 
related_notes: [[ANN]], [[CNN]]

# Recurrent Neural Networks (RNN)

## Description

A Recurrent Neural Network (RNN) is a type of [[ANN]] designed for ptestrocessing sequential data, such as time series or natural language.

While a [[CNN]] is excellent for spatial data (like images) because it looks at local patterns, an RNN has an internal "memory" loop. This allows it to persist information, meaning the output of step $t-1$ influences the input of step $t$. This makes them ideal for tasks like language translation or stock prediction.

## Resources

- [The Unreasonable Effectiveness of RNNs](http://karpathy.github.io/2015/05/21/rnn-effectiveness/ "null")
    
- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/ "null")