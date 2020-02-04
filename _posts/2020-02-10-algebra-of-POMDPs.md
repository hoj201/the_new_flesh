---
layout: post
title: The Algebra of Markov Decision Processes
---
In earlier posts I re-discovered the category of probabilistic relations.
To me this is a very useful category to get comfortable with if you're
a machine learning practitioner with a taste for mathematical abstraction.
In this post we will see how this category, literally, reduces the definition
of markov decision processes to cartoon sketches of arrows and dots.

## TL;DR
The main take-aways of this post are that within the category of probabilistic
relations:
 - discrete time markov models
 - hidden markov models
 - markov decision processes
 - and partially observeable markov decision processes

are given bythe diagrams

![markov]({{"assets/pomdp/markov_chain.svg" | absolute_url }}){:width="100em"},
![hmm]({{"assets/pomdp/hmm.svg" | absolute_url }}){:width="100em"}, 
![mdp]({{"assets/pomdp/mdp.svg" | absolute_url }}){:width="200em"}, 
![pomdp]({{"assets/pomdp/pomdp.svg" | absolute_url }}){:width="400em"}

okay, i'm sure you understood all that.  Thank god for these TL;DRs.  Now you
don't need to read this post.  Toodeloo! Have a nice day!

## The category of probabilistic relations
Oh, hey there. You're still reading. We'll it's your life, thanks for using it
to study arrows and dots with me. The category of probabilistic relations,
denoted $$\mathrm{PRel}$$, has many equivalent definitions of its arrows and
its objects. Personally find the one used by Anandan to be a bit convoluted,
although it seems to be the most popular for some reason.
I'll give my favorite one, which is different.

The objects of $$\mathrm{PRel}$$ are simply the set of measureable spaces.
However, the morphisms **are not measureable maps**. They are what engineers
might call "stochastic maps", a terminology I like as well.

A conditional probability distribution/kernel/stochastic map,
is typically denoted as if it were a function of two arguments,
e.g. $$\rho(y \mid x)$$.  Such an object can be viewed as map that eats
distributions over $$x$$'s and outputs distributions over $$y$$'s.  
Here's how.
Given a prior, $$\mu(x)$$, we can construct a posterior distribution,

$$
    \nu(y) := \int \rho(y \mid x ) \mu(x) dx 
$$

So we have expressed $$\rho$$ as a map which sends distributions over 
one measurable space, into distributions over some other measureable space.
**In fact, this mapping between measureable spaces  uniquely characterizes $$\rho$$**.
Therefore it is fair to say that kernels **are** the arrows
of $$\mathrm{PRel}$$.  The composition of two kernels being

$$
    (\rho_2 \circ \rho_1)(z|x) = \int \rho_2(z | y) \rho_1(y | x) dy
$$

### Some limits and co-limits
So the objects are measureable space, and the arrows are
stochastic maps. A co-limit within this category is the discrete $\sigma$-algebra
on one element, $\cdot$. There is no limit me-thinks.

In the category, $$\mathrm{Set}$$, the limit of the diagram 
$$X \stackrel{f}{\to} Y$$
is given by graph, $$\Gamma[f] := \{ (x,f(x)) \in X \times Y\}$$.

Within $$\mathrm{PRel}$$ the same construction holds. In this case we 
have a stochastic map, $$(X,\Sigma_X) \stackrel{\rho}{\to} (Y, \Sigma_Y)$$,
and the limit is the measureable space 

$$
    \Gamma[\rho] := \{(U,V) \in \Sigma_X \times \Sigma_Y 
        \mid V = \mathrm{supp}(\rho(\mu)), \mathrm{supp}(\mu) = U \}
$$

which is a sub-algebra of $$(X \times Y, \Sigma_X \otimes \Sigma_Y)$$.

### Determinism and measureable maps
Lastly, there are some arrows in $$\mathrm{PRel}$$ which are special. These
are the arrows that are given by measureable maps.  The universal property
that characterizes a measureable map is ... they are the least fuzzy...
Sorry, I'm having trouble expressing this without getting too in the weeds,
but I think it involves taking limits in the $$2$$-category of commutative squares.
Let's just trust that measurable maps satisfy a universal property
within $$\mathrm{PRel}$$, by virtue of being the "least fuzzy".


## Markov models
Traditionally, a discrete time, finite state Markov process in one where
the sequence of events, $$x_0, x_1, \dots $$, takes place in a measureable
space $$X$$ and 
$$\Pr(x_{n} \mid x_{0}, x_{1}, \dots, x_{n-1}) = \Pr(x_{n} \mid x_{n-1})$$.
In fact, the entire systems is characterized by the conditional probability
function $$\Pr(x_{n} \mid x_{n-1})$$.

In other worse, a discrete time Markov process is nothing but a diagram within
$$\mathrm{PRel}$$ that looks like

![markov]({{"assets/pomdp/markov_chain.svg" | absolute_url }}){:width="100em"}


## Hidden markov models
Traditionally, a hidden markov model consists of a markov process, as well as
a stochastic observation of the state. Formally, this is given by two maps, the
stochastic transition map which sends $$x_{n} \mapsto x_{n+1}$$ and the stochastic
observation, $$x_n \mapsto y_n$$.  More precisely, a hidden Markov model is 
nothing but a diagram


![hmm]({{"assets/pomdp/hmm.svg" | absolute_url }}){:width="100em"}

## Markov decision process
A markov decision process is, roughly speaking, a controllable markov process.
The typical definition is needlessly restrictive, but let's go through it
for the sake of connecting to the literature.

### The traditional definition
Many textbooks define an MDP with states $$X$$ and actions $$A$$
as a triple $$(\phi, r, \gamma)$$ where $$\phi:X \times A \to X$$,
expresses that if you're in state $x \in X$ and apply action $a \in A$,
then you will end up in a random state drawn from  $$\phi( \cdot \mid x,a)$$.
The reward function, $$r: (x_n, a_n, x_{n+1}) \in X \times A \times X \mapsto r(x_n,a_b, x_{n+1}) \in \mathbb{R}$$, 
is something that rewards us when the transition $$(x_n, a_n) \stackrel{\phi}{\mapsto} x_{n+1}$$
is executed. Lastly, $$\gamma$$ is a real number between 0 and 1, called the
"discount rate".

"Solving" and MDP means finding a policy, $$\pi: X \to A$$ which maximizes

$$
    V[\pi](x_0) := \sum_{t \geq 0 } \gamma^t r_t
$$

where $$r_t$$ denotes the expected value of the reward given at time $$t$$.


### A superior definition
The traditional definition is needlessly restricted,
and is frequently violated in practice.
In many cases the set of allowable actions is dependent on the state. For example,
consider an $$n$$-state system, where all the states are numbered $$0$$ through
$$n$$, and the actions are to increase/decrease by one.  Then there are two possible
actions on states $$1$$ through $$n-1$$, but only one possible action at the boundaries
$$0$$ and $$n$$. Perhaps this is gnit-picky, but it's too easy to leave un-fixed.

Here's the fix.
We assume the existence of a measureable surjection $$\tau: \mathcal{A} \to X$$.
The action space for a given state $$x \in X$$ is given by the pre-image $$\tau^{-1}(x) \subset \mathcal{A}$$.
The transition map, in this formalism, is a stochastic map $$\phi:\mathcal{A} \to X$$.

Another gnit-pick I have of the traditional definition of MDPs is the suggestion
that the reward function be definied over all of $$X \times A \times X$$.
This is not the case.  The reward function only needs to reward transitions
generated by $$\phi$$.  In otherwords, the reward function is a 
stochastic map $$r:\Gamma[\phi] \to \mathbb{R}$$

As a result, an MDP is given by a triple $$(\tau, \phi, r, \gamma)$$
where $$\tau$$ is deterministic ans surjective
and the triple satisfies the diagram

![mdp]({{"assets/pomdp/mdp.svg" | absolute_url }}){:width="200em"}


A policy, under this definition, is a section of $$\tau$$.
i.e. a stochastic map $$\pi:X \to \mathcal{A}$$ such that $$\tau \circ \pi = id_{\mathcal{A}}$$

Note that given a policy, we can form the composition $$\phi \circ \pi: X \to X$$.
Thus a policy transforms an MDP into a markov process.

## Partially observeable markov decision processes
A partially observeable Markov decision process (POMDP) is to an MDP
as a hidden Markov model is to a Markov model. The traditional definition
does little more than append a stochastic map $$y:X \to Y$$
of observations to the standard definition of an MDP. A little more care should
be applied.  I think it's reasonable to assume that the set of controls one
can apply in a given state is itself observeable.

As a result, we assume a deterministic surjection, $$\tau:\mathcal{A} \to Y$$.
A pomdp consists of a tuple $$(\tau, \phi, r, \gamma, y)$$
where
 - $$Y$$ denotes the observation space
 - $$X$$ denotes the state space
 - $$\tau:\mathcal{A} \to Y$$ relates actions to observations
 - $$y:X \to Y$$ is the observation map
 - $$\phi: X \times_Y \mathcal{A} \to X$$ is the transition map
 - $$r: \Gamma[\phi] \to \mathbb{R}$$ is the reward function
 - $$\gamma \in (0,1)$$ is the discount factor.

The measureable space $$X \times_Y \mathcal{A}$$ is the pull-back obtained by
the maps $$y$$ and $$\tau$$.

![pomdp]({{"assets/pomdp/pomdp.svg" | absolute_url }}){:width="400em"}

What is a policy in this context?
This continues to be debated within the reinforcement learning community.
Some people believe that it should be something like a section of $$\tau$$, i.e. a map from $$Y \to \mathcal{A}$$.
Personally, coming from a control-theory background that sounds ridiculous
to me.  In control theory, you look at the history of observations to make
an informed decision.  I could get behind that a little more,
but there is a more eleagant solution, which I'll propose in the next post.

Thanks for sticking with me thus far!

