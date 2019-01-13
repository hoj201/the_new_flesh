---
title: Supervised machine learning for pure mathematicians
subtitle: Deep Learning for Mathematicians part I
layout: post
tags: math, philosophy
---

My own journey from academia to data-science was hard and annoying.
The hard part was becoming a decent coder. The annoying part
was the math. Not because the math was difficult, but because it was often written in such a boring way. I think the authors typically have practicality in mind, the math was merely a tool for them, and any abstraction needed immediate justification when used. That makes sense for the large readership of engineers and statisticians.
However, it left me unsatisfied, and I suspect I am not alone.
There is a small collection of people who actually enjoy abstraction for its
own sake. We might be afraid to admit it, because we were trained to hide predilections that risk our chances at grant money, but this doesn't change the truth of the matter. Now that I'm out of academia I feel safer admitting that I find abstraction fun, and an ends in and of itself. It is useful for the speed with which it allows one to transport logic from one domain into another. But it's also fun. My hope is that this series will make ML more fun for a neglected audience with similar feelings.

If you're a starving and idealistic mathematician, as I once was, and you are
coming to the depressing realization that the ivory tower is a shadow of its past self,
and now merely a zombie for promoting STEM initiatives and thus a puppet of private industry,
come with me and step down into our cave.

## Plato's cave
![plato]({{"assets/ml_p1/plato.jpg" | absolute_url }}){:width="300em"}

Plato's allegory of the cave is roughly summarized as follows: A bunch of people
are chained inside a cave and forced to watch shadow puppets dance on
the wall until they think the shadows are reality.
This happens to us every time we go to the movie theatre.
If the movie is any good, we forget that we are staring at a blank wall with
light projected on it.
Once we leave the theatre, it's not clear that we've really left **the** theatre.
Perhaps our perception of reality is but a shadow of truth.

The notion of a shadow is mathematically represented as a map projecting
the platonic forms into a space of observables.
If reality were a sequence of statistically independent events
then the model for such a reality could be easily mathematized.
Our senses could be represented by a collection of random variables
$$X_i: \Sigma \to \Sigma_i$$ for $$i=1,\dots,5$$.
All of data-science is concerned with studying
models based on finite collections of samples in this model of Plato's cave.
For example, what is the relationship (if any) between senses
$$X$$ and $$Y$$.

## Relations
A **relation** is merely a subset of a cartesian product,
$$R \subset X \times Y$$.
A function $$f:X \to Y$$ is represented as a relation by its graph,
$$\Gamma[f] := \{ (x,f(x)) \}_{x \in X}$$.

At a high level we have two categories here, and one is a strict subcategory.
The category $$\operatorname{Set}$$,
where the objects are sets and the arrows are maps,
and the category $$\operatorname{Rel} := \operatorname{Span}(\operatorname{Set})$$,
where the objects are sets and the arrows are relations.

Generally speaking, an arbitrary
relation is not the graph of a function... sad face emoji.
In **supervised machine learning**
we'd like to do something like constructing
a function from a relation... crying face emoji!!

## Stop crying!
So clearly the goal stated above is generically infeasible.
Fortunately, our real goal is not quite so dumb.
It's almost that dumb though.

A labeled dataset consists of $$(x,y)$$ pairs, but it is **NOT**
merely a finite set of $$(x,y)$$ pairs. Elements can be listed more
than once, and so a labeled dataset is a finite [multiset](https://en.wikipedia.org/wiki/Multiset)
Multisets are a foundation for the field of probability.
Therefore, we should probably be doing something probabilistic.

**The goal of supervised machine learning is to construct a
probabilistic function (a posterior)
using a dataset sampled from a probabilistic relation
(a joint distribution)**.

I'll explain what these probabilistic functions and relations are next.

## The probabilistic category
Let's start by setting up some notation.  If $$\Sigma$$ is a $$\sigma$$-algebra,
we let $$\Pr(\Sigma)$$ denote the set of probability distributions over $$\Sigma$$.

We could define a probabilistic category
where the objects are probability distributions and the arrows
are conditional distributions. A conditional distribution is usually written with
two arguments like $$f(E_Y \mid E_X)$$, but it's only a probability distribution over
the first argument, $$E_Y$$. We can curry this function and viewed $$f$$,
as a map, $$f: \Sigma_X \to \Pr(\Sigma_Y)$$.
For a specific $$\rho_X \in \Pr(\Sigma_X)$$,
the conditional distribution, $$f$$, can be viewed as an arrow from
$$\rho_X \in \Pr(\Sigma_X)$$ to the distribution

$$
\begin{align}
  \rho_Y (E_y) := \int_{\Omega_X} f(E_y \mid x)\rho_X(x), \forall E_y \in \Sigma_Y
\end{align}
$$

and two posterior distributions, $$g(z \mid y), f(y \mid x)$$ can be
composed via the law of total probability

$$
\begin{align}
  (g \circ f)(z \mid x) := \int_{\Omega_Y} g(z \mid y) f(y\mid x) dy
\end{align}
$$

This defines the category, $$\operatorname{Prob}$$ where
 - the objects are probability distributions,
 - the arrows are conditional probability distributions,
 - and the composition is given by the law of total probability.

We will think of $$\operatorname{Prob}$$ as a probabilistic version of
$$\operatorname{Set}$$.[^prel]

[^prel]:The category $$\operatorname{Prob}$$ is related to the category of probabilistic relations. If your a fan of categorical approaches to mathematics, I recommend [this article](https://arxiv.org/abs/1205.1488). You might also enjoy my blog-series on the topic: [part I](https://www.thenewflesh.net/2018/01/21/probability.html), [part II](https://www.thenewflesh.net/2018/01/27/probability_p2.html), and [part III](https://www.thenewflesh.net/2018/02/12/probability_p3.html)

## Relations in the probabilistic category
There is a probabilistic analog to $$\operatorname{Rel}$$.
A stochastic relation from $$\rho_X \in \Pr(\Sigma_X)$$
to $$\rho_Y \in \Pr(\Sigma_Y)$$ is an element
$$\rho \in \Pr(\Sigma_X \otimes \Sigma_Y)$$
whose marginals are $$\rho_X$$ and $$\rho_Y$$ respectively.
We'll call this category $$\operatorname{ProbRel}$$.

Just as there is a functor which embeds $$\operatorname{Set}$$ into
$$\operatorname{Rel}$$, there is a functor, $$F$,
 which embeds $$\operatorname{Prob}$$ into $$\operatorname{ProbRel}$:

 - for an object $$\rho$$ in $$\operatorname{Prob}$$, $$F(\rho) := \rho$$.
 - for an arrow $$f: \rho_X \to \rho_Y$$ in $$\operatorname{Prob}$$, $$F(f)$$
 is the join distribution on $$\Sigma_X \otimes \Sigma_Y$$
 given by $$F(f)(E_x,E_y) = f(E_y \mid E_x) \rho_X(E_x)$$

Something to note: $$F$$ is invertible!

The goal of bayesian supervised machine is to associate a posterior
distribution to a labeled dataset, $$\mathcal{D} = \{ (x_i,y_i) \}_{i=1}^{N}$$,
sampled from an (unknown) joint distribution
$$\rho \in \Pr(\Sigma_X \otimes \Sigma_Y)$$.
In other words, given samples from a probabilistic relation, $$\rho$$, we'd like
to find a probabilistic function $$f$$ such that $$F[f] = \rho$$.
The upshot here is that $$F$$ is invertible.

<!--## Bayesian supervised machine learning
Just to re-iterate, we posit the existence of a probability distribution, $$\rho$$
over a $$sigma$$-algebra, $$\Sigma$$ and measureable maps $$X:\Sigma \to \Sigma_X$$
and $$Y: \Sigma \to \Sigma_Y$$. Our goal is to find
a conditional probability map $$f: \Pr(\Sigma_X) \to \Pr(\Sigma_Y)$$ such that the diagram

![cd]({{"assets/ml_p1/supervised_learning_cd.svg" | absolute_url }}){:width="300em"}

commutes.

Unfortunately, we typically do not know $$X, Y$$ or even the distribution $$\rho$$
over $$\Sigma$$.
Instead we have a finite dataset consisting of samples of $$X$$ and $$Y$$
with respect to some probability distribution.
Specifically, our dataset is

$$
\begin{align}
\mathcal{D} := \{(x(\omega_i),y(\omega_i)) \mid \omega_1,\dots, \omega_N \sim \rho \}
\end{align}
$$

with respect to some unknown probability distribution $$\rho$$ over
$$\Sigma$$.  Our hope is to find a posterior $$\tilde{f}$$, such that the diagram
"almost" commutes.  In this context, the posteriors from $$\Pr(\Sigma_X)$$
to $$\Pr(\Sigma_Y)$$ are called "classifiers" if $$Y$$ is a discrete random variable,
or "regressors" if $$Y$$ is continuous.-->

## The ideal solution
If we knew the probabilistic relation
$$\rho \in \Pr(\Sigma_X \otimes \Sigma_Y)$$
we could produce the desired posterior.
Let $$X: \Sigma_X \otimes \Sigma_Y \to \Sigma_X$$
and $$Y:\Sigma_X \otimes \Sigma_Y \to \Sigma_Y$$ denote the canonical projections
We would define $$f_{ideal}$$ to be the posterior
probability distribution

$$
\begin{align}
  f_{ideal}(E_Y \mid E_X) := \rho( X^{-1}(E_X) \cap Y^{-1}(E_Y)) / \rho( X^{-1}(E_X)).
\end{align}
$$
for events $$E_Y \in \Sigma_Y, E_X \in \Sigma_X$$.

However, since se do not know $$\rho$$, we can't compute $$f_{ideal}$$.
So much for idealism.

## Empiricism

![hume]({{"assets/ml_p1/hume.jpg" | absolute_url }}){:width="300em"}

We might not know $$\rho$$, but we do have a labeled dataset, $$\mathcal{D}$$ sampled
from $$\rho$$.  We should be able to approximate $$\rho$$ using the distribution
$$\rho_{\mathcal{D}} := N^{-1}\sum_{(x,y) \in \mathcal{D}} \delta_x \otimes \delta_y$$
where $$N = | \mathcal{D} |$$. In fact, for $$\sigma$$-algebras observed in
practice, we $$\rho_{\mathcal{D}} \to \rho$$ weakly as $$N \to \infty$$.

We could then do the same computation as before to get the posterior distribution

$$\begin{align}
  f_{\mathcal{D}} (E_x \mid E_y) = \frac{| \mathcal{D} \cap (E_x \times E_y) | }{ | \mathcal{D} \cap E_y \times X(\Omega)|}
\end{align}$$

In fact $$f_{\mathcal{D}} \to f_{ideal}$$ weakly as $$N \to \infty$$.
This is a very conservative data-driven approach which people like David Hume (pictured above)
may have advocated. His advice for anything not based upon direct observation was
to "commit it then to the flames: for it can contain nothing but sophistry and illusion."

So we're done right?

## Critique on Pure Reason
The empiricist approach *Kant* work.

![kant]({{"assets/ml_p1/kant.jpeg" | absolute_url }}){:width="300em"}

I'm so punny. Feel free to take a moment, and allow yourself to stop laughing.

The solution, $$f_{\mathcal{D}}$$ is (typically) a really bad solution.
Sure, it converges (sort of).
However, if $$| \Omega_X | \cdot |\Omega_Y|$$ is large convergence will be slow.
This is especially true if either $$X$$ or $$Y$$ are continuous random variables,
so that $$| \Omega_X | \cdot |\Omega_Y| = \infty$$.
For example, if $$X$$ is a real valued random variable, then
$$f_{\mathcal{D}}$$ is then ill-defined for any value of $$X$$ outside of dataset.
Such a failure will occur almost surely for any distribution of $$X$$'s with a support
with non-empty interior.
This phenomena is known as **overfit** and we'd say our solution has high **variance**
and the resulting errors are known as **generalization errors** because our
analysis failures to generalize to anything outside our dataset.

### The war on variance
To ensure that our classifier does not fail outside of $$\mathcal{D}$$ requires that we
adopt an assumption.
You need to take a risk in order to talk about data that has never been seen.

Typically one assumes the solution exists in some submanifold
$$M \subset \operatorname{Hom}(\rho_X,\rho_Y)$$ and then we choose
the "best" element of $$f_M \in M$$ as our solution.

### Best?
We define "best" using some cost function $$C:\operatorname{Hom}(\rho_X,\rho_Y) \times \Pr(\Sigma_X \otimes \Sigma_Y) \to \mathbb{R}$$ which satisfies

$$
  f_{ideal} = \arg \min_{f} C(f,\rho)
$$
and the continuity property
$$
  f_{ideal} = \lim_{|\mathcal{D}| \to \infty} \left(\arg \min_{f} C(f,\rho_{\mathcal{D}}) \right)
$$


For example, the negative log-liklihood function

$$\begin{align}
  C(f,\rho) := -\int_{\Omega} \rho(\omega) \log(f(X(\omega) \mid Y(\omega))) d\omega
\end{align}$$

would do nicely.  In this case

$$\begin{align}
  C(f,\rho_{\mathcal{D}}) := - \frac{1}{|\mathcal{D}|}\sum_{(x,y) \in \mathcal{D}} \log(f(x \mid y))
\end{align}$$

Then we can set
$$
  f_M = \arg \min_{f \in M} C(f,\rho_{\mathcal{D}})
$$

The cost function presented here, yields as estimate known as the maxiumum
likelihood estimate (MLE).

If $$f_{ideal} \in M$$ then $$f_M$$ will converge to $$f_{ideal}$$ as the
number of samples goes to infinity.
Unfortunately, it is unlikely that $$f_{ideal} \in M$$, so this convergence
is also unlikely.
This phenomena is known as **bias**.

There are more creative things one can do, like making $$M$$ really large and then
assuming a prior over $$M$$ to combat variance.
This is known as maximum aposterior estimation (MAP estimation)
but you will still suffer from bias.
The only way to ensure bias is a complete non issue is to set $$M = \operatorname{Hom}(\rho_X,\rho_Y)$$ and assume a uniform prior.  But then you
die from variance.
F\*\*\*, you just can't win!

## The bias variance tradeoff
Data-science is more of an art than a science.
The art is in choosing $$M$$ to be large enough that you don't get crushed by
bias, but small enough so that you don't get crushed by variance.

Fortunately these phenomena strike hard in different regimes.
For small datasets, non-convergence at infinity is a pipe-dream and bias is the least of your worries.  You should worry about
variance for small datasets.
Conversely, for large datasets you can reasonably expect to get close to the true value of the posterior, and worrying about bias starts to make sense.

I could tell you how to test for bias and variance, but that's out of the scope
of this blog-post.  Let's see an example

### Example:  A robot that denies people loans
A loan application consists of a variety of numbers
 - loan amount
 - credit score
 - historical default rate

We can represent an application as a single vector,
and view the process of recieving such applications as a vector valued
random variable, $$X$$.
As time progresses we will see some of these loans get paid back, or default.
Let $$Y$$ be the binary valued vector which is $$0$$ for default and $$1$$ otherwise.
Our goal is to find a posterior $$f: \Pr(\Sigma_{\mathbb{R}^n}) \to \Pr(\Sigma_2)$$
where $$\Sigma_{\mathbb{R}^n}$$ is just the Borel $$\sigma$$-algebra on $$\mathbb{R}^n$$
and $$\Sigma_2$$ is just the standard $$\sigma$$ algebra on $$2$$ objects.[^2]
Note that $$\Pr(\Sigma_2) \cong [0,1]$$ because any distribution on 2 objects is
represented by a biased coin (i.e. a Bournoulli distribution), and such coins are
parametrized by the probability that they turn up heads.

[^2]:I like this notation more than something like $$\Sigma_{\{0,1\}}$$. In any course on the foundations of math you would learn to define the natural numbers as a set. In particular $$0 := \emptyset$$, and then we define the successor operation $$n+1 := \{ \{n\}, \emptyset\}$$.  In particular, $$2 = \{ 1 , 0 \}$$.

Once we have a dataset $$\mathcal{D}$$, we can start to construct $$M$$.
First, consider the logistic function $$\operatorname{logit}(x) = \frac{\exp(x)}{1+\exp{x}}$$.
This function has the graph depicted below.

<p><a href="https://commons.wikimedia.org/wiki/File:Logistic-curve.svg#/media/File:Logistic-curve.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Logistic-curve.svg/1200px-Logistic-curve.svg.png" alt="Logistic-curve.svg"></a><br>By <a href="//commons.wikimedia.org/wiki/User:Qef" title="User:Qef">Qef</a> (<a href="//commons.wikimedia.org/wiki/User_talk:Qef" title="User talk:Qef">talk</a>) - Created from scratch with gnuplot, Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=4310325">Link</a></p>

The primary reason this is a useful function is because it maps $$\mathbb{R}$$ to
$$[0,1] \cong \Pr(\Sigma_2)$$. Now we just need a map from
$$\mathbb{R}^n$$ to $$\mathbb{R}$$ (because $$X$$ is $$\mathbb{R}^n$$ valued).
I'm tired, so we will just consider
linear mappings, or maybe affine mappings (linear + offset).
Therefore, let $$M$$ consist of posteriors of the form

$$
\begin{align}
    f_\beta(Y=1 \mid X=x) = \operatorname{logit}( \beta_1^T x + \beta_0 )
\end{align}
$$
for some $$\beta_1 \in \mathbb{R}^{n}$$ and $$\beta_0 \in \mathbb{R}$$.
This implies $$f_\beta(Y=0 \mid X=x) = 1 - f_\beta(Y=1 \mid X=x)$$ since $$Y$$
only takes the values $$0$$ and $$1$$.
We see that $$M$$ is parametrized by $$\beta = (\beta_0,\beta_1)$$ and so $$M \cong \mathbb{R}^{n+1}$$.

Given our dataset $$\mathcal{D}$$ we consider the (approximate) cross-entropy
$$
  C_N[\beta] = \sum_{k=0}^{1} \sum_{(x,y) \in \mathcal{D}} \delta(y,k) f_\beta(Y=k \mid X=x)
$$

And we solve for
$$
  \beta^{\ast} := \arg \max_\beta C_N[\beta]
$$
which is known as the Maximum likelihood estimate.

The function $$C_N$$ is convex, and so finding $$\beta^{\ast}$$ is not
a problem. This procedure is known as **logistic regression**

## What next?
It should be obvious that supervised learning is generically useful.  Via supervised learning our society could make robots for all sorts of things.
  - Robots for parsing legal documents
  - Robots for recommending products
  - Robots for identifying faces in photos
  - Robots to detect suspicious objects at the airport
  - Robots for hiring and firing people at a company
  - Robots for firing at people on the battle field
  - Robots for rendering legal verdicts such as the life sentences, or death sentences

... so that's cool.

## Footnotes
