---
layout: post
title: Categorification of Markov Decision Processes
---
In earlier posts I re-discovered the category of stochastic relations. To me this is a very useful category to get comfortable with if you're a machine learning practitioner with a taste for mathematical abstraction. In this post we will see how this category, literally, reduces the definition of markov decision processes to cartoon sketches of arrows and dots.

## TL;DR
The main take-aways of this post are that within the category of stochastic relations, $$\mathrm{SRel}$$:
 - discrete time markov models
 - hidden markov models
 - markov decision processes
 - and partially observeable markov decision processes

are given by the diagrams

![markov]({{"assets/pomdp/markov_chain.svg" | absolute_url }}){:width="100em"},
![hmm]({{"assets/pomdp/hmm.svg" | absolute_url }}){:width="100em"}, 
![mdp]({{"assets/pomdp/mdp.svg" | absolute_url }}){:width="200em"}, 
![pomdp]({{"assets/pomdp/pomdp.svg" | absolute_url }}){:width="300em"}

and the categories for each of these items is (at least in spirit) a functor category of the form $$\mathrm{SRel}^{J}$$ where $$J$$ is replaced by each of the diagrams above.

TL;DRs are so useful! You understood everything just said, and now you don't need to read this post. It's a wonder I wasted time writing it. Toodeloo!

## The category of stochastic relations
The category of stochastic relations, $$\mathrm{SRel}$$, is basically the category of random variables. The objects of $$\mathrm{SRel}$$ are measureable spaces. The morphisms are what engineers might call "stochastic maps" and what mathematicians call conditional probability distributions. The composition of two conditional probability distributions is (at least hueristically) given by

$$
    (\rho_2 \circ \rho_1)(z|x) = \int \rho_2(z | y) \rho_1(y | x) dy
$$

Obviously you replace integrals with sums in the case where $$y$$ is discrete. The discovery of this category is generally credited to an unpublished note by Lawvere in 1962.[^lawvere]

### Notable limits within $$\mathrm{SRel}$$
The terminal object of $$\mathrm{Srel}$$ is the trivial measureable space, $$1$$. A morphism, $$\rho:1 \to X$$ is equivalent to a probability distribution over $$X$$, i.e. $$\mathrm{SRel}(1,X) = \Pr(X)$$.

Within the category of sets, $$\mathrm{Set}$$, the limit of the diagram $$X \stackrel{f}{\to} Y$$ is given by the graph, $$\Gamma[f] := \{ (x,f(x)) \in X \times Y\}$$. Within $$\mathrm{SRel}$$ the same construction holds. In this case we have a stochastic map, $$X \stackrel{\rho}{\to} Y$$, and the limit is the measureable space 

$$
    \Gamma[\rho] := \{(U,V) \mid V = \mathrm{supp}(\rho( \cdot \mid U)), U \subset X \text{is measureable}\}
$$

which is a measureable sub-space of $$X \times Y$$.

### Determinism and measureable maps
The category of measureable spaces $$\mathcal{M}$$ is a subcategory of $$\mathrm{SRel}$$.  The objects of both categories are identical, and for each  measureable map, $$f \in \mathcal{M}(X, Y)$$, we can define the stochastic map, $$f_{\#} \in \mathrm{SRel}(X, Y)$$ by 

$$
    f_{\#}(V \mid x) = \begin{cases} 1 & \text{if } x \in f^{-1}(V) \\
        0 & \text{else}
    \end{cases}
$$
 for $$V \subset Y$$ a measureable set and $$x \in X$$. We call such morphisms **deterministic**. There is a universal property which characterizes a the deterministic maps ... they are the least fuzzy... Okay, to be the honest I've not tightened all the screws here, but here goes.

#### A natural (re)definition of determistic
The deterministic maps are special within $$\mathrm{SRel}$$ because they preserve some notion of locality. So, I'll make an attempt to nail down what locality means in $$\mathrm{SRel}$$.  Firstly, Each measureable space, $$X$$ is naturally equipped with a collection of (measureable) inclusion maps, $$i_U:U \hookrightarrow X$$ for each measureable $$U \subset X$$. Perhaps you can question if it's really so natural.  I'd say it is because I believe in the following

> Conjecture: The monomorphisms of $$\mathrm{SRel}$$ are (up to isomorphism) the inclusion maps which embed measureable subsets into measureable spaces.

Certainly the inclusion maps are monic.  I believe the converse holds as well (anything monic is isomorphic to one of these inclusion maps). Dually, I also believe that the epimorphism are the deterministic surjections.

> Corollary: A stochastic relation, $$f: X \to Y$$, is deterministic if and only if for each inclusion map, $$i_V : V \to Y$$, the pushout consists of an inclusion map $$i_U : U \to X$$ and a stochastic relation, $$i_U^*f : U \to V$$ so that we get the commutative square
> $$
> \require{AMScd}
> \begin{CD}
> X @>f>> Y\\
> @AA i_U A @AA i_V A\\
> U @> i_U^*f >> V
> \end{CD} .
> $$


## The category of Markov models
A discrete time Markov process is one where we witness a random sequence of objects $$x_0, x_1, \dots $$ existing withing some measureable space $$X$$, where the dependency between subsequent observations satisfies $$\Pr(x_{n} \mid x_{0}, x_{1}, \dots, x_{n-1}) = \Pr(x_{n} \mid x_{n-1})$$. In fact, the entire systems is characterized by the conditional probability function $$\Pr(x_{n} \mid x_{n-1})$$, sometimes referred to as the transition function. In other words, a discrete time Markov process is one whose diagram in $$\mathrm{SRel}$$ is given by

![markov]({{"assets/pomdp/markov_chain.svg" | absolute_url }}){:width="100em"}

These models form a category, denoted $$\mathrm{MM}$$, in the obvious way. The objects are $$\mathrm{SRel}$$ endomorphisms, $$T:X \to X$$, and an arrow from $$T$$ to $$T':Y \to Y$$ is given by a similarity transformation, i.e. a morphism $$f:X \to Y$$ such that $$T' \circ f = f \circ T$$. In Lawvere's 1962 note[^lawvere], which is credited for kicking off the categorification of probability theory, making $$\mathrm{MM}$$ explicit was (at least ostensibly for funding purposes) a prime motive. In that pre-moon-landing era note, Lawvere identified $$\mathrm{MM} = \mathrm{SRel}^{\mathbb{N}}$$, where $$\mathbb{N}$$ was viewed as a monoidal category. Now days we might write something more like $$\mathrm{MM} = \mathrm{SRel}^{\circlearrowleft}$$

## The category of hidden Markov models
Traditionally, a hidden markov model consists of a markov process, as well as a stochastic observation of the state. Formally, this is given by two maps, the stochastic transition map which sends $$x_{n} \mapsto x_{n+1}$$ and the stochastic observation, $$x_n \mapsto y_n$$.  More precisely, a hidden Markov model is nothing but a diagram

![hmm]({{"assets/pomdp/hmm.svg" | absolute_url }}){:width="100em"}

We can form a category, $$\mathrm{HMM}$$, in the obvious way. The objects of $$\mathrm{HMM}$$ are hidden markov models, and an arrow in $$\mathrm{HMM}$$ from $$(T:X \to X,y:X\to Y)$$ to $$(T':X'\to X', y':X' \to Y')$$ is a pair of morphisms, $$\alpha_X:X \to X'$$ and $$\alpha_Y:Y \to Y'$$ of $$\mathrm{SRel}$$ such that $$T' \circ \alpha_X = \alpha_X \circ T$$ and $$y' \circ \alpha_X = \alpha_Y \circ y$$. In other-words we have a functor category, $$\mathrm{HMM} = \mathrm{SRel}^{J_{HMM}}$$, where $$J_{HMM}$$ is the diagram depicted above.

At this point a pattern has been established for this blog post.  We will continue in our caveman like fashion to
 - look at $$thing$$
 - diagram $$thing$$
 - define functor-category $$\mathrm{Things} := \mathrm{SRel}^{J_{thing}}$$
  
Let's do this next for Markov Decision processes.

## Markov decision process
A markov decision process is, roughly speaking, a controllable markov process with rewards. The goal is to pull levers in the correct way in order to maximize a cumulative reward. In this section we will discover that all Markov decision processes can be represented as a diagram within the category $$\mathrm{SRel}$$. Before doing that we'll go over the traditional definition. The traditional definition is needlessly restrictive, but let's go through it for the sake of tradition.

<iframe src="https://giphy.com/embed/XNhmbeWeZl0By" width="480" height="350" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/meatballs-spaghetti-alka-seltzer-XNhmbeWeZl0By">via GIPHY</a></p>

### The traditional definition
Many textbooks define an MDP with states $$X$$ and actions $$A$$ as a triple $$(\phi, r, \gamma)$$ where $$\phi:X \times A \to X$$, expresses that if you're in state $$x \in X$$ and apply action $$a \in A$$, then you will end up in a random state drawn from  $$\phi( \cdot \mid x,a)$$. The reward function, $$r: (x_n, a_n, x_{n+1}) \in X \times A \times X \mapsto r(x_n,a_b, x_{n+1}) \in \mathbb{R}$$, 
is something that rewards us when the transition $$(x_n, a_n) \stackrel{\phi}{\mapsto} x_{n+1}$$ is executed. Lastly, $$\gamma$$ is a real number between 0 and 1, called the "discount rate".

"Solving" and MDP means finding a policy, $$\pi: X \to A$$ which maximizes

$$
    V[\pi](x_0) := \sum_{t \geq 0 } \gamma^t r_t
$$

where $$r_t$$ denotes the expected value of the reward given at time $$t$$.


### A superior definition
The traditional definition is needlessly restrictive, and is frequently violated in practice. In many cases the set of actions depends on the state. For example, consider an $$n$$-state system, where all the states are numbered $$0$$ through $$n$$, and the actions are to increase/decrease the state by one.  Then there are two possible actions on states $$1$$ through $$n-1$$, but only one possible action at the boundaries $$0$$ and $$n$$. Perhaps this is gnit-picky, but it's easy to fix.

Here's the fix. We assume the existence of an epimorphism $$\tau: \mathcal{A} \to X$$, and this map should be deterministic as well, however I conjecture that follows automatically from being epic. The action space for a given state $$x \in X$$ is given by the pre-image $$\tau^{-1}(x) \subset \mathcal{A}$$. The transition map is a stochastic morphism $$\phi:\mathcal{A} \to X$$. Thus, the kinematics of an MDP are given by the diagram

$$
    X \stackrel{\phi}{\leftarrow} \mathcal{A} \stackrel{\tau}{\twoheadrightarrow} X
$$

This picture is not quite complete.  It's not an MDP unless there is a reward function. However, I have another gnit-pick regarding the traditional definition of the reward function. Traditionally, the reward function is defined over the entirety of $$X \times A \times X$$. This is excessive.  The reward function need only be defined on transitions generated by $$\phi$$. A more precise definition is that the reward function is a stochastic relation $$r:\Gamma[\phi] \to \mathbb{R}$$ from the (stochastic) graph of $$\phi$$ to the reals.[^reals]

[^reals]: There is a caveat.  The reward function maps to the reals viewed as a measureable vector-space with orientation. This is because we take expected values of sums of rewards (thus we need vectoriness) and we maximize cumulative rewards (thus we need to know which way is heaven)

In summary, an MDP is given by a triple $$(\tau, \phi, r, \gamma)$$ where $$\tau$$ is deterministic-epic and the triple satisfies the diagram

![mdp]({{"assets/pomdp/mdp.svg" | absolute_url }}){:width="200em"}

### The category of $$MDPs$$
We can an MDP $$(\tau,\phi:\mathcal{A} \to X, r:\Gamma[\phi]\to\mathbb{R})$$ onto another MDP $$(\tau',\phi':\mathcal{A}' \to X', r':\Gamma[\phi'] \to \mathbb{R})$$ using a morphisms $$f_X:X \to X'$$, an affine orientation preserving transformation $$a:\mathbb{R} \to \mathbb{R}$$, and a morphism $$f: \mathcal{A} \to \mathcal{A}'$$ such that

$$\require{AMScd}
\begin{CD}
\mathcal{A} @>f>> \mathcal{A}'\\
@VV \tau V @VV \tau' V\\
X @>f_X>> X'
\end{CD}
$$,
$$\require{AMScd}
\begin{CD}
\mathcal{A} @>f>> \mathcal{A}'\\
@VV \phi V @VV \phi' V\\
X @>f_X>> X'
\end{CD}
$$,
$$\require{AMScd}
\begin{CD}
\Gamma[\phi] @> f_X \times f >> \Gamma[\phi']\\
@VV r V @VV r' V\\
\mathbb{R} @>a>> \mathbb{R}
\end{CD}
$$

In this sense, the triple $$(f,f_X, a)$$ is an arrow of $$(\tau,\phi,r,\gamma)$$ to $$(\tau',\phi',r', \gamma)$$.
This has the feel of a functor category, i.e. $$\mathrm{MDP} \approx \mathrm{SRel}^{J_{MDP}}$$
where $$J_{MDP}$$ is the commutative diagram of an MDP depicted in the last sub-section.[^caveat]

[^caveat]: I can't equate with $$\mathrm{SRel}^{J}$$ because our diagram has extra information in it (the diagram is more than a cartoon of a small category).  For example, the epicness of $$\tau$$ and the fact that reward function maps to $$\mathbb{R}$$ viewed as an oriented vector-space.

### Solutions to MDPs
The solution to an MDP is a policy, some way of choosing an action given the state. A policy, under this definition, is a section of $$\tau$$. i.e. a stochastic relation $$\pi:X \to \mathcal{A}$$ such that $$\tau \circ \pi = id_{\mathcal{A}}$$

Given a policy, we can form the composition $$\phi \circ \pi: X \to X$$. Thus a policy transforms an MDP into a markov process. A solution of an MDP is a policy that maximizes the value function

$$
    V^{\pi}(x_0) = \mathbb{E}( \sum_{t \geq 0} \gamma^{-t} r_t ) 
$$

Now some frantic hand-waving. I'm pretty sure the mapping which takes an MDP and gives you it's solution yields two functors. One which maps an MDP $$(\tau,\phi,r,\gamma)$$ to the optimal policy $$\pi^\ast$$, and another which maps to the markov process $$\phi \circ \pi^{\ast}$$.  I suspect, this is possible by viewing $$\mathbb{R}$$ as an totally ordered set, which induces a total ordering on the policies, and so we can take limits (in the categorical sense) and cobble together a functor. The solutions are not always unique :(. If we consider the subcategory of MDPs with unique solutions, or cleverly "quotient away" enough redundancies, I suspect this is possible.

## Partially observable markov decision processes
A partially observable Markov decision process (POMDP) is to an MDP as a hidden Markov model is to a Markov model. The traditional definition does little more than append a stochastic map $$y:X \to Y$$ of observations to the standard definition of an MDP. A little more care should be applied in my opinion though.  I think it's reasonable to assume that the set of actions one can take in a given state be observable (if you can't see them, they wouldn't be actionable).

As a result, we assume a (deterministic) epimorphism, $$\tau:\mathcal{A} \to Y$$. A pomdp consists of a tuple $$(\tau, \phi, r, \gamma, y)$$ where
 - $$\tau:\mathcal{A} \to Y$$ relates actions to observations
 - $$y:X \to Y$$ is the observation map
 - $$Y$$ denotes the observation space
 - $$X$$ denotes the state space
 - $$\phi: X \times_Y \mathcal{A} \to X$$ is the transition map
 - $$r: \Gamma[\phi] \to \mathbb{R}$$ is the reward function
 - $$\gamma \in (0,1)$$ is the discount factor.

The $$X \times_Y \mathcal{A}$$ is just the pull-back  of $$\tau$$ along $$y$$. As a set,  

$$
    X \times_Y \mathcal{A} \stackrel{\text{Set}}{=} \{ (x,a) \in X \times Y \times \mathcal{A} \mid y(x)=\tau(x) \}
$$
 
and is equipped with the two natural projections "$$(x,a) \mapsto x$$" and "$$(x,a) \mapsto a$$". All these maps allow us to diagram a generic POMDP as

![pomdp]({{"assets/pomdp/pomdp.svg" | absolute_url }}){:width="400em"}

### The category of POMDPs
Again, we can form a category of POMDPs by imagining the relevant commutative squares. A POMDP $$(y,\tau, \phi, r, \gamma)$$
where
 - $$y:X \to Y$$
 - $$\tau:\mathcal{A} \to Y$$
 - $$\phi: X \times_Y \mathcal{A} \to X$$
 - $$r:\Gamma(\phi) \to \mathbb{R}$$
 - $$\gamma \in (0,1)$$

can be mapped to another POMDP by maps
 - $$f:\mathcal{A} \to \mathcal{A}'$$
 - $$f_Y:Y \to Y'$$
 - $$f_X:X \to X'$$
 - $$a:\mathbb{R} \to \mathbb{R}'$$
 
which generates a new POMDP $$(\tau', y', \phi', r', \gamma)$$ as one which makes the
squares commute
 
$$\require{AMScd}
\begin{CD}
\mathcal{A} @>f>> \mathcal{A}'\\
@VV \tau V @VV \tau' V\\
Y @>f_Y>> Y'
\end{CD}
$$,
$$\require{AMScd}
\begin{CD}
X @>f_X>> X'\\
@VV y V @VV y' V\\
Y @>f_Y>> Y'
\end{CD}
$$,
$$\require{AMScd}
\begin{CD}
X \times_Y \mathcal{A} @>f_X \times f_Y \times f>> X' \times_{Y'} \mathcal{A}'\\
@VV \phi V @VV \phi' V\\
X @>f_X>> X'
\end{CD}
$$,
$$\require{AMScd}
\begin{CD}
\Gamma[\phi] @> f_X \times f >> \Gamma[\phi']\\
@VV r V @VV r' V\\
\mathbb{R} @>a>> \mathbb{R}
\end{CD}
$$
 
so again we may define the category as something like as functor category, $$\mathrm{POMDP} \approx \mathrm{SRel}^{J_{POMDP}}$$ where $$J_{POMDP}$$ is the diagram associated to POMDP's depicted earlier.

### (Not) Solving POMDPs
Just like the solution to an MDP is a policy that tells one what action to take, a solution to a POMDP is going to be a policy as well. What is a policy in this context? **Nobody knows!!!!** The answer to this question continues to be debated within the reinforcement learning community. Some believe a policy should be a section of $$\tau$$, i.e. a map from $$Y \to \mathcal{A}$$. Personally, that sounds ridiculous.  In the theory of control of LTI systems, you look at the history of observations to make an informed decision.  So some advocate for a map from histories of $$y$$'s to actions.  I have my own ideas, but they'll have to wait for another blog post.

## Concflusion
In this post basically nothing useful was accomplished. Have a nice day.

Full disclosure: This post is a primer for the next post, where actually useful work will be done. Solving POMDPs (and even defining the solution space) continues to perplex ppl, and this abstract nonsense could be helpful in clearing the crud and proposing an eleagant and "simple" solution.  There are standard techniques to solve MDPs.  If we can build a faithful functor $$F: \mathrm{POMDP} \to \mathrm{MDP}$$, we can solve POMDPs using the same techniques. This will be attempted in the next post.

<iframe src="https://giphy.com/embed/VypJYbpuh7ZtK" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/the-office-what-confused-VypJYbpuh7ZtK">via GIPHY</a></p>

[^lawvere]: Lawvere, "The Category of Probabilistic Mappings", 1962 [link](https://ncatlab.org/nlab/files/lawvereprobability1962.pdf)