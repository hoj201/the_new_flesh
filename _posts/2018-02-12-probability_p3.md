---
layout: post
title: Probabilistic notation is the worst (Part III)
subtitle: Now with machine learning
comments: true
tags: math
---
>“We were somewhere around Barstow, on the edge of the desert, when the drugs began to take hold.”
*― Hunter S. Thompson, Fear and Loathing in Las Vegas*

This post is the third in a three part series
 - [click here for part I]({{ site.baseurl }}{% post_url 2018-01-21-probability %})
 - [click here for part II]({{ site.baseurl }}{% post_url 2018-01-27-probability_p2 %})

In part II I discussed how probability theory deserves its own category, the same way that other sub fields of mathematics have their own category.  I showed how the standard definition does not transform properly under restriction, and prohibits the the formation of a category.  This motivated us to consider an alternative definition. However, I never illustrated the category which results. The present post accomplishes one thing: we will make a category for probability theory and tie it to the classical foundations.

![fear and loathing]({{"assets/probability_p3/getin_txt.jpg" | absolute_url }}){:width="400em"}

## The category of measurable spaces
A measurable space consists of a pair, $$(X,\Sigma)$$, where $$X$$ is a set and $$\Sigma \subset 2^X$$ is a $$\sigma$$-algebra.
We think of the elements of $$\Sigma$$ as events when we talk about probability.
Informally, a $$\sigma$$-algebra is just the algebraic entity which encodes the notion of a space of events.
For the formal definition see the wikipedia [link](https://en.wikipedia.org/wiki/Sigma-algebra).
Given two $$\sigma$$-algebras, $$(X,\Sigma_1)$$ and $$(Y,\Sigma_2)$$, we say that $$f:X \to Y$$ is measurable if $$f^{-1}(E) \in \Sigma_1$$ for every $$E \in \Sigma_2$$.
The collection of all measurable spaces forms a category where the arrows are given by measurable maps.


## The category of measure cones
A measure on a measurable space, $$(X,\Sigma)$$, is just a map $$\mu: \Sigma \to \mathbb{R}^+ \cup \{ \infty\}$$ such that
  - $$\mu(\emptyset) = 0$$
  - $$\mu \left( E_1 \uplus E_2 \right) = \mu(E_1) + \mu(E_2)$$

where $$\uplus$$ denotes disjoint union.
We denote the space of measures over a $$(X,\Sigma)$$ by $$\mathcal{M}(X,\Sigma)$$
and we will call such a space a measure-space.

Note that given two measures $$\mu_1,\mu_2 \in \mathcal{M}(X,\Sigma)$$ we can sum them to get a measure $$\mu_1 + \mu_2 \in \mathcal{M}(X,\Sigma)$$ so that $$\mathcal{M}(X,\Sigma)$$ forms a [convex cone](https://en.wikipedia.org/wiki/Convex_cone).

The assignment "$$(X,\Sigma) \mapsto \mathcal{M}(X,\Sigma)$$" is actually a functor, but to clarify that I need to describe the arrows.

## Arrows between measure cones
Not that for each event $$E \in \Sigma$$, we can describe a new $$\sigma$$-algebra $$(E, E \cap \Sigma)$$
where
$$E \cap \Sigma := \{ E \cap \bar{E} \mid \bar{E} \in \Sigma \}$$.
In fact this characterizes all the sub-algebras of $$\Sigma$$.
So we see each $$\sigma$$-algebra is equipped with a set of inclusion maps from it's sub-algebras.

The inclusion map $$\iota: E \cap \Sigma \hookrightarrow \Sigma$$ can be lifted to a map which embeds $$\mathcal{M}(E \cap \Sigma) \hookrightarrow \mathcal{M}(\Sigma)$$.
It's a measureable map after all.
A **posterior measure** is a map, $$m: \mathcal{M}(\Sigma_1) \to \mathcal{M}(\Sigma_2)$$ such that for any $$E \in \Sigma_1$$
there exists a unique map $$m_E : \mathcal{M}(E \cap \Sigma_1) \to \mathcal{M}(\Sigma_2)$$ which makes the diagram

![cd]({{"assets/probability_p3/presheaf.svg" | absolute_url }}){:width="300em"}

commute. *Sidetrack: Something here is eerily reminiscent of a pre-sheaf.*

The correspondence with the classical notion of a posterior measure might not be obvious.
In the case where $$X$$ is a manifold, a classical posterior measure, $$m(B \mid A)$$ where $$A \subset X$$ and $$B \in \Sigma_2$$
induces a map which sends a measure $$\mu_1 \in \mathcal{M}(X,\Sigma_1)$$ to a measures $$\mu_2 \in \mathcal{M}(Y,\Sigma_2)$$
by
$$\mu_2(B) :=  \int m(B \mid x) \mu_1(x) dx, \forall B \in \Sigma_2$$.
In the discrete case, the integral just becomes a sum.
This mapping satisfies the commutative diagram,
so we at least see the classical posteriors as special cases, and so have illustrated one direction of this equivalence.

The other direction can be demonstrated as well.
This mapping from $$\mathcal{M}(X,\Sigma_1)$$ to $$\mathcal{M}(Y,\Sigma_2)$$ completely characterizes the posterior $$\mu(B\mid A)$$.
This is most easily illustrated in the case where $$\Sigma_1$$ is finite.
Then you can take $$A$$ to be a singleton set, $$\{ x \}$$ for some $$x \in X$$, in which case $$\mu$$ is just a scalar which we'll call $$\mu_x \in \mathbb{R}^+$$.
The measure $$\iota_*(\mu)$$ has support on a single point, namely $$x$$, and the comutativity of the diagram implies that for any $$B \in \Sigma_2$$ that $$m[i_*\mu] (B) = \lambda_x(B) \mu_x$$ for some measure $$\lambda_x \in \mathcal{M}(\Sigma_2)$$.
However, all measures in $$\mathcal{M}(\Sigma_1)$$ are direct sums of measures of the form $$\iota_* \mu$$ where $$\iota$$ is the immersion of a singleton set.  Therefore, for a generic $$\mu \in \mathcal{M}(\Sigma_1)$$ we have
$$m[\mu](B) = \sum_{x \in X} \lambda_x(B)  \mu(x)$$.
The measure $$\lambda_x (B)$$ is just a manifestation of what is classically written as "$$\Pr(B \mid x \in X)$$".
In the case where $$\Sigma_1$$ is a continuous algebra, the summation just becomes integration.
For generic $$\sigma$$-algebras, I'm not sure how to write things, but in that scenario the top-down categorical definition of a posterior might serve us better anyway, by foregoing the need to write down an explicit expression.

Having defined posterior measures in this way, we see that the posterior measures are good candidates for the arrows of the category of measures. We need only define the composition operation.

## The composition
The composition operation is (perhaps unsurprisingly) the chain rule of measure theory.
Given posteriors $$m_1 :\mathcal{M}(X,\Sigma_1) \to \mathcal{M}(Y,\Sigma_2)$$,
and a posterior $$m_2:\mathcal{M}(Y,\Sigma_2) \to \mathcal{M}(Z,\Sigma_3)$$, we can compose
them to get the posterior $$m_3 = m_2 \circ m_1:\mathcal{M}(X,\Sigma_1) \to \mathcal{M}(Z,\Sigma_3)$$.
If we write this composition down using classical notation we find
$$m_3(C \mid A) =  \int_Y m_2(C \mid y) m_1(y \mid A) dy$$.

Having defined a collection of objects, the measure cones $$\mathcal{M}(\Sigma)$$, and arrows, represented by posteriors, we see that we have a category, which I'll dub $${\rm Meas}$$.

## Somebody has been here

![fear and loathing]({{"assets/probability_p3/creeping2.jpg" | absolute_url }}){:width="400em"}

  Definitely trodden territory.
  This notion of using posteriors as arrows is discussed at the [n-category cafe](https://golem.ph.utexas.edu/category/2007/02/category_theoretic_probability.html) and at the [n-lab](https://ncatlab.org/nlab/show/probability+theory) where they talk about a theory of ["Probabilistic Relations"](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.52.4840), by Prakash Panangaden.
  Apparently this line of thought goes back all the way to the early days of category theory, to an unpublished manuscript Lawvere wrote in the 1962 called "The category of probabilistic mappings".
  This manuscript was later elaborated on by M. Giry in ["a categorical approach to probability theory"](https://www.chrisstucchio.com/blog_media/2016/probability_the_monad/categorical_probability_giry.pdf) where the functor $$(X,\Sigma) \mapsto \mathcal{M}(X,\Sigma)$$ serves as the key ingredient to Monad.
  He then forms the Kleisli category of this monad, which apparently provides some insight into Chapman-Kolmogorov relations. This paper by Giry looks like a lot of fun, but to be honest, as a hobbyist mathematician with a fairly intense (less mathy) day job, I probably wont find the time to give Giry's work the attention it deserves any time soon.

## Our first functor
We are ready for our first functor, which sends the category of $$\sigma$$-algebras to $${\rm Meas}$$.
This is the functor given by "$$\Pi$$" in Giry's paper.
For each $$(X,\Sigma)$$ there is a measure cone $$\mathcal{M}(X,\Sigma)$$,
and for each measureable map $$f:X \to Y$$ there is a posterior measure $$m_f:\mathcal{M}(X,\Sigma) \to \mathcal{M}(Y,\Sigma)$$ given by $$m_f(\mu)(B) = \mu(f^{-1}(B))$$, basically sending a measure to its push-forward.
Note, this functor does not give all posteriors.
The only posteriors of this form have very Dirac-delta feel to them.

## From measures to probabilities
Getting from measures to probabilities is fairly trivial now.
We just apply the ray functor (see [part I]({{ site.baseurl }}{% post_url 2018-01-21-probability %}) of the series).
We've already established that $$\mathcal{M}(X,\Sigma_1)$$ is a cone.
Therefore, the notion of a ray is sensible, and we can send each non-zero measure $$\mu \in \mathcal{M}(X,\Sigma_1)$$ to a ray $$R[\mu] \in \mathcal{P}(X,\Sigma_1)$$ where $$\mathcal{P}(X,\Sigma)$$ denotes the ray-space of $$\mathcal{M}(X,\Sigma)$$.
These rays are (very modest generalization of) probability densities on $$(X,\Sigma_1)$$.
This was the content of the last few posts.

I'd like to promote the assignment of "$$\mu \mapsto R[\mu]$$"" to a functor. To do so, I must figure out how $$R$$ should handle the arrows in the category of measure cones, the posterior measures.
The set of posterior measures between $$\mathcal{M}(X,\Sigma_1)$$ and $$\mathcal{M}(Y,\Sigma_2)$$ is itself a convex cone.
So again, the notion of a ray is well defined there.
The ray of a posterior measure is just what it sounds like, and applying $$R$$ to the posterior measures in this way gives us a functor to a new category, which we will call $${\rm Prob}$$.

## The category of probability theory
In $${\rm Prob}$$, the objects are the spaces $$\mathcal{P}(X,\Sigma)$$ which consist of the ray space of $$\mathcal{M}(X,\Sigma)$$.  The rays themselves correspond with probability densities (see the first post).
The arrows correspond with our classical notion of posterior probabilities.
The composition operation corresponds with the the chain rule of probability theory.


## Relationship with the classical notions
Classically, when posteriors are introduced, they are only defined after a joint probability has been chosen, and then you will see a definition that looks like "$$\Pr(A \mid B) := \Pr(A,B) / \Pr(B)$$".
I'll try to relate what's written here, to this more classical derivation of a posterior probability.

Let $$(X,\Sigma_1)$$ and $$(Y,\Sigma_2)$$ be two measurable spaces.
There are two natural projections on $$\mathcal{M}(\Sigma_2 \times \Sigma_2)$$ to consider:
 - $$\pi_1 : \mathcal{M}(\Sigma_2 \times \Sigma_2) \to \mathcal{M}(\Sigma_1)$$
 - $$\pi_2 : \mathcal{M}(\Sigma_2 \times \Sigma_2) \to \mathcal{M}(\Sigma_2)$$

Given a posterior measure $$m : \mathcal{M}_1( \Sigma_1) \to \mathcal{M}(\Sigma_2)$$
there is a unique map $$s : \mathcal{M}_1( \Sigma_1) \to \mathcal{M}(\Sigma_1 \times \Sigma_2)$$
such that :
  - $$\pi_1 \circ s = 1$$
  - $$\pi_2 \circ s = m$$

This map relates a posterior measure to a joint measure, and manifests via the formula $$\mu(A,B) := \sigma( \mu_1)(A,B) = m(B|A) \mu_1(A)$$
This describes the classical relationship between a posterior density and joint.
Translating this over to probabilities is a trivial matter of taking the rays of the everything in sight.

The spirit in which a posterior is defined in this post is quite different.
Typically, one views posterior probabilities as derivations from a pre-chosen joint probability.
In contrast, in this category theoretic picture, the posteriors are entities which exist independently of choosing any joint probability.

#### Bayes' theorem?
Seems trivial.  We just note that we can swap the role of $$\Sigma_1$$ and $$\Sigma_2$$.

### Diffusion and Markov processes
A Markov process, in this context, is nothing but an arrow, $$\rho$$ from $$\mathcal{P}(X,\Sigma)$$ to itself.
A hidden markov model is nothing but a tuple $$(\rho, \gamma)$$, where $$\rho:\mathcal{P}(X,\Sigma) \to \mathcal{P}(X,\Sigma)$$ and $$\gamma : X \to Y$$, is a measuraeable map to a space of observables.
Diffusion results from the observation that $$\rho$$ is generically not invertible.
My guess is that ,$$\rho$$ is invertible if and only if
$$ \rho(\mu)(E) = \mu( \phi^{-1}(E))$$
for some measurable automorphism $$\phi:X \to X$$.

## Bayesian nets
With all these diagrams and arrows being drawn, it's tempting to wonder "What does this have to do with probabilistic graphical models and Bayesian networks". Perhaps there is a relation, but it might not resemble what you (or at least I) would have imagined.

The arrows of a Bayesian network are **not** posteriors.  The arrows of a Bayesian network represent the flow of information in a computation graph.
This is probably a good time to clear up another misconception.
Bayesian networks are **not** generalizations of computation graphs.
The reverse is true.
Bayesian networks are **special cases** of computation graphs.
They correspond to the scenario where all the nodes are probability distributions.

What category theory has to offer to the world of computation graphs is the notion of composition. Given two computation graphs with a single source node and a single target node, we can compose them to get another computation graph with a single source node and a single target node.
The composition corresponds with the composition operation in $${\rm Meas}$$.
After all, these are computation graphs for posterior probabilities.

More generally, we can consider graphs with multiple source nodes, and multiple target nodes, and there is a notion of higher order composition from higher-order category theory which applies in this scenario.

But now I've gone so far beyond things I'm qualified to talk about, that I can't even ...

>The possibility of physical and mental collapse is now very real. No sympathy for the Devil, keep that in mind. Buy the ticket, take the ride.”
― Hunter S. Thompson, Fear and Loathing in Las Vegas

![televandalist]({{"assets/probability_p3/televandalist.gif" | absolute_url }}){:width="400em"}

[gif created by televandalist](http://televandalist.com/)
