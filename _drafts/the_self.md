---
title: Hidden Markov Models and the illusion of free will
layout: post
tags: math, philosophy
---

## TLDR
I do not believe in free will. However, I "feel" as if I have it. At a fundamental level, everything is governed by physical laws.  Not the will of "me".  However, at that level "I" am not well defined (the h-bar of the self.)
This is well illustrated by a deterministic Hidden Markov Model.  Under the hood, there are deterministic rules, but at the level of course observation it appears as randomness.  The feeling of being conscious is that of witnessing these sensor readings evolve in time. From the perspective of the observer, these readings are not evolving deterministically. We then give the randomness a name, "the will".

In fact there is this tower of models, because an HMM (nearly) induces a Markov chain on the observation space.

\begin{align}
Pr(y_{t+1} \mid y_t ) &= \sum_{x_{t+1}} \Pr(y_{t+1} \mid x_{t+1} , y_t ) \\
  &= \sum_{x_{t+1}} \Pr(y_{t+1} \mid x_{t+1}) \Pr( x_{t+1} \mid y_t ) \\
  &= \sum_{x_{t+1}, x_t} \Pr(y_{t+1} \mid x_{t+1}) \Pr( x_{t+1} \mid x_t, y_t ) \\
  &= \sum_{x_{t+1}, x_t} \Pr(y_{t+1} \mid x_{t+1}) \Pr( x_{t+1} \mid x_t) \Pr(x_t \mid y_t ) \\
\end{align}

The only issue is that we don't really know $\Pr(x_t \mid y_t)$. The most natural thing would be to define it as an entropy maximizing section of $$\Pr(y_t \mid x_t)$$. After this is done we obtain a Markov model on the space of observations.

## Strange loop
Once the observation process is realized as a Markov chain, we can observe the observation process to get another HMM.  Iterating this process, we can get nested HMMs. One high level version of the self, looking at a lower level. This is what consciousness feels like to me.
