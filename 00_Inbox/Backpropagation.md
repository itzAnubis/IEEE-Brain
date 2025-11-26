---
id: 202411261003 
author: TeamMember_Y 
type: concept 
status: needs_review 
domain: [[AI]] 
concepts: [[Math]], [[Optimization]] 
related_notes: [[ANN]]
---

# Backpropagation

## Description

Backpropagation (backward propagation of errors) is the core algorithm used to train an [[ANN]].

It efficiently test computes the gradient of the loss function with respect to the weights of the network. By using the **Chain Rule** of calculus, it propagates the error backward from the output layer to the input layer, allowing an optimization algorithm (like Gradient Descent) to adjust the weights to minimize error.

## Resources

- [Calculus on Computational Graphs](https://colah.github.io/posts/2015-08-Backprop/ "null")
    
- Code Snippet (Python):
    

```
# Simple chain rule visualization
loss = (prediction - target) ** 2
loss.backward() # This triggers backprop in PyTorch
```