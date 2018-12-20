---
layout: post
title: Probabilistic notation is the worst (Part II)
comments: true
tags: math
---

![coin flip](https://media.giphy.com/media/5EQC8eAnEAAZG/giphy.gif){:width="300em"}


I ended an [earlier post]({{ site.baseurl }}{% post_url 2018-01-21-probability %})
 by suggesting a new definition of a probability
distribution.  I glossed over the bulk of the math in that post,
so I'll attempt to remedy that now.

> **Definition:** Let $$(\Omega, \mathcal{F})$$ be a $$\sigma$$-algebra.
A *neo-probability* is a ray within $$\mathcal{M}(\Omega, \mathcal{F})$$, the
space of measures.

##  Ray?
A *ray* is a semi-infinite line segment through the origin of a vector space.
The reason they are called "rays" is self-evident.

![a ray]({{"assets/prob_notation_is_worst_p2/ray.jpeg" | absolute_url }}){:width="400em"}

We can also think of rays in terms of symmetry by considering the group
of positive real-numbers with group product given by multiplication,
 $$(\mathbb{R}^+,\cdot)$$.
 For any real vector space $$V$$,
 we can define the group action of $$(\mathbb{R}^+,\dot)$$ on $$V$$
 by $$\rho(g) \cdot v = g \cdot v$$ where $$g \cdot v$$ is just the rescaling of
$$v \in V$$ by $$g \in \mathbb{R}^+$$.
 That this is a group action is basically a bullet-point within the definition
  of a vector-space.
  A ray is nothing but an element of the quotient space $$V^\circ / (\mathbb{R}^+, \cdot )$$
  where $$V^\circ := V \backslash \{ 0 \}$$.

In our case, the vector space under consideration is the space of measures, $$\mathcal{M}(\Omega)$$ over some $$\sigma$$-algebra, $$\Omega$$.
We'll denote the space of rays by $$\mathcal{R}(\Omega) := \mathcal{M}(\Omega) / \mathbb{R}^+$$
with the quotient projection $$\pi: \mathcal{M}(\Omega) \to \mathcal{R}(\Omega)$$.[^0]

## You lost me at quotient space
It probably seems needlessly abstract to define ray's as elements of a quotient
space, but let me bring it back home.
We were talking about probability a moment ago, and the notion of rescaling
comes up a lot there.
Recall, a probability is a measure of unit mass.
Given a finite measure, $$\mu$$ ,over some $$\sigma$$-algebra,
 $$(X, \Omega)$$, we can define a probability, $$\Pr(x) := \mu(x) / \mu(X)$$.
 Note that the measures contained in the ray
 $$\pi(\mu) := \{ g \cdot \mu \mid g \in \mathbb{R}^+\}$$ all map to the
 same probability distribution.
 In other-words the unit measures, $$\mathcal{M}_{1}(\Omega) := \{ \mu \in \mathcal{M}(\Omega) \mid \mu(X)=1\}$$, embed into the ray-space of measures, $$\mathcal{R}(\Omega) := \mathcal{M}(\Omega) / \mathbb{R}^+$$.
 This is how to correspond our new "ray-based" theory of probability with the classical "unit-measures based" theory of probability.
 However, this embedding is not surjective.
 It is only injective, which is to say that the "ray-based" theory is more general.

## Meh. So what?
You might have missed it, but there is a big restriction placed
on the sort of measures which can be normalized.  In particular, the measure must
be finite ($$\mu(X) < \infty$$).
There are many measures, such as the uniform measure on $$\mathbb{R}$$, which
[statisticians use it all the time](https://en.wikipedia.org/wiki/Prior_probability#Improper_priors), but are not finite.
For example, when we do least-squares linear regression, we are (implicitly) assuming
a uniform prior over the coefficients.
It's disturbing that these infinite measures are occasionally treated as if they
are probability distributions, yet are prohibited from the classical theory.
I think this means that we should have a more inclusive theory.[^1]
Using ray's instead of unit-mass measures serves as a solution because the ray of measure is well defined, even if the measure is not finite.

## Previous work
After a little digging, it seems that other people have thought along similar lines.
I noticed it pop in [this blog post](link) which cites, [this recent pre-print](https://arxiv.org/abs/1710.08933), which then cites both Renyi and
Kolmogorov...  (yeah, that Kolmogorov).
Sorry to name drop like that, but since this idea may seem a tad screwy I felt compelled to
note that other people besides me drawn to this line of thought.

![there are dozens of us](https://media.giphy.com/media/WzDBaDZIXFZ1C/giphy.gif)

I also asked a friend of mine for his thoughts, a professor of probability theory and statistics at Princeton, and he said that this redefinition did not feel so radical.
In fact, he felt it was implicitly adapted in certain scenarios (which we will get to in this post).

## Conditional probability using the classical definition

I mentioned this in my earlier post, but didn't really go through with the details.
Let $$(X,\Omega)$$ be a $$\sigma$$-algebra and $$A \in \Omega$$ be a measurable set.
then $$A \cap \Omega := \{ A \cap B \mid B \in \Omega \}$$ is a sub-$$\sigma$$-algebra of $$\Omega$$.

If restrict unit-mass measure, $$\Pr$$ (i.e. a classical probability distribution),
to the sigma algebra $$A \cap \Omega$$ the resulting restricted measure would **not** be unit mass
and therefore not a probability measure! You would need to normalize by $$\Pr(A)$$
it in order to obtain the conditional probability $$\Pr(B \mid A)$$.
Therefore,
**the classical definition of a probability distribution does not transform properly
under restrictions.**

## Transforming properly is important
An entity transforms properly if there is a set of morphisms which allow one
to form a [category](https://en.wikipedia.org/wiki/Category_(mathematics)).
Apparently, defining probability distributions as unit-mass measures prohibits us from forming a category if we wish to do things like restriction to a subset.  That's fuddup.

I know this might not mean much to many (most?) statisticians and probabilists. but virtually every other sub-discipline of mathematics studies an entity which is contained in a category.

![serial]({{"assets/prob_notation_is_worst_p2/super_serial.jpg" | absolute_url }}){:width="400em"}

I can't describe why this is important very quickly, and I will probably need
to do another post to do the point justice.
In the meantime, here are two lists.
First, a non-exhaustive list of major branches of mathematics where the central entity transforms properly:

 - Topology (topological spaces via continuous maps)
 - Differential Geometry (smooth manifolds via smooth maps)
 - Analysis (function spaces via continuous maps)
 - Logic and set theory (boolean algebras via maps between sets)
 - Algebraic geometry (varieties via regular maps)
 - Algebraic anything really (algebraic things via homomorphisms)
 - Group theory (groups via group homomorphisms)
 - Linear Algebra (vector spaces via linear maps)
 - Category theory (tags via natural transformations)
 - Measure theory (measure spaces via measurable maps)

Here is an exhaustive list of major mathematical sub-disciplines which lack a notion of "morphism":

- applied mathematics[^2]
- [my 3-year olds counting book](https://www.goodreads.com/book/show/17938496-my-bus)
- whatever this guy does[^crazy]
- Kabbalah
- probability theory (probability spaces)
- and of course, [time cube](http://timecube.2enp.com/)

Probability theory deserves a better home.

## Conditional probability with rays
As mentioned, measures spaces form a category.
Specifically, we can consider the category whose objects $$\sigma$$-algebras and whose morphisms are ... well, I'd like to save that for part III, but certainly measureable maps are among the morphisms.
The mapping $$\Omega \mapsto \mathcal{M}(\Omega)$$, which sends a $$\sigma$$-algebra
to the cone of measures over that algebra yields a natural transformation to a new category
where the objects are spaces of measures.
We can (quite literally) project that later category onto the relevant ray-space.
This is because the map $$\pi: \mathcal{M}(\Omega) \to \mathcal{R}(\Omega)$$ yields a [functor](https://en.wikipedia.org/wiki/Functor).

How is this related to conditional probability?
Well, we can restrict any measure, $$\mu \in \mathcal{M}(X)$$, to $$A \cap \Omega$$
by pull-back to get a measure $$i_A^* \mu \in \mathcal{M}(A)$$.
This is just fancy notation, $$i_A^* \mu( B \cap A) = \mu(B \cap A)$$ for
arbitrary $$B \in \Omega$$.
Additionally, we can project each of the measures $$\mu$$ and $$i_A^* \mu $$
To there respective ray spaces.  So now we can draw a commutative diagram (because $$\pi$$ yields a functor):

![Diagram]({{ "/assets/prob_notation_is_worst_p2/conditional.svg" | absolute_url }}){:width="200em"}

and, spoiler, *conditional probability will arise from the bottom arrow in the diagram.*
If $$\mu$$ is finite, we can identify the ray $$\pi(\mu)$$ with the (classical) probability measure "$$\Pr(B) := \mu(B) / \mu(X)$$" for each $$B \in \Omega$$.
Similarly, if $$\mu(A)$$ is finite, then the ray of $$i_A^* \mu$$ would be identified with
$$ \mu(B \cap A) / \mu(A)$$... That last expression is nothing but the conditional probability $$\Pr(B \mid A)$$... So that's telling.

However, this way thinking about Bayesianism is robust.
If $$\mu(X)$$ is not finite, the classical theory explodes while the ray-based theory is honey-badger.

![honey badger](http://i0.kym-cdn.com/entries/icons/facebook/000/005/637/Honey-Badger-Dont-Care.jpg){:width="300em"}

<!-- ## Random variables (push-forwards)
A real-valued random variable, $$Z$$ is nothing more than a sigma-algebra morphism from some sigma-algebra, $$(X,\Omega)$$ to the Borel sigma algebra on $$\mathbb{R}$$.
Thus, for any measure $$\mu$$ over $$(X,\Omega)$$ we can consider the push-forward
measure $$Z_*\mu$$ by making the diagram

![Diagram it]({{"/assets/prob_notation_is_worst_p2/pushforward.svg" | absolute_url }}){:width="200em"}

commute.
Thus $$Z_*$$ sends measures on $$X$$ to measures on $$\mathbb{R}$$.
We can project this mapping to ray space by making the diagram

![Diagram it]({{"/assets/prob_notation_is_worst_p2/pushforward2.svg" | absolute_url }}){:width="200em"}

commute.

 ## Independence
In the typical presentation of independence, you have two random variables, $$X$$ and $$Y$$, and you say they are independent if $$\Pr(X,Y) = \Pr(X) \Pr(Y)$$. (This is using that lousy probability theory notation that I hate)
To translate this notion to ray space we use the fact that measure theory plays nice with category theory, and project the results onto ray-space again.

Firstly, given two $$\sigma$$-algebras, $$\Omega_1$$ and $$\Omega_2$$,
the rank-one elements of $$\mathcal{M}(\Omega_1) \otimes \mathcal{M}(\Omega_2) \subset \mathcal{M}(\Omega_1 \times \Omega_2)$$ are the measures the form $$\mu(x,y) = \mu_1(x) \mu_2(y)$$.
In diagrams, they form the minimal set in the upper left corner which makes the diagram

![Diagram it]({{"/assets/prob_notation_is_worst_p2/rank_one.svg" | absolute_url }}){:width="300em"}

commute.
We can they say that $$X$$ and $$Y$$ are independent with respect to a ray, $$\rho \in \mathcal{R}(\Omega_1 \times \Omega_2)$$
if $$\rho = \pi(\mu)$$ for some rank-one $$\mu \in {\rm rank}_1[\mathcal{M}(\Omega_1 \times \Omega_2)]$$. I'm glossing over some pretty interesting details here, but this post is too long now so I'll just stop and hide some more things in footnotes[^independence]. -->

## Final thoughts
This has been a long post, just to derive the classical notion of conditional probability.
Bad news though. I don't think this is the best way to think about conditional probability.
Just like I want to do away with the classical definition of probability, I'd also like to do away with the
classical definition of conditional probability.
I don't want to think of it simply as a map from a sigma algebra to a probability measure.
Instead I'd like to think of conditional probabilities as arrows within a category.
But this post is too long, so I'll save that for part III.

![image]({{ "assets/prob_notation_is_worst_p2/end.jpg" | absolute_url }}){:width="400em"}

# Footnotes:
[^0]:Technically, the domain of $$\pi$$ is not all of $$\mathcal{M}(\Omega)$$ since there is no ray associated to the zero-measure.  Perhaps that's an indication we are on the right track (there is no probability distribution associated with the zero-measure).

[^1]: Admittedly, not all measures are reasonable.  For example, the measure $$e^{x^2} dx$$ over the reals serves as a crazy prior for determining the mean of Gaussian random variable, because it puts you in a situation where any finite number of samples gives you basically no knowledge [(see Craig Gidney's post)](http://algassert.com/post/1630). However, throwing out all improper priors because a subset of them are pernicious in a subset of situations strikes me as throwing the baby out with the bath-water. In that same post, the improper priors "$$dx$$" and "$$x^{-1}dx$$" are both used as examples of reasonable priors to use in this scenario.

[^2]: Applied mathematics gets a pass with respect to the "I transform properly" certification in my mind.  There is no central entity, and the field is defined by its borderline mathematical status.

[^crazy]: He looks like this ![image]({{ "assets/prob_notation_is_worst_p2/crazy_guy.png" | absolute_url }}){:width="400em"}.  [Here is a video you should not watch](https://youtu.be/svi6KmtPDQM).

[^independence]: illustrates another reason I hate the classical notation.  Apparently, if you clean up the notation (you don't really need rays, but just using measure theory notation suffices), you can find that $$X$$ is independent of $$Y$$ if the initial sigma algebra is projectable to a product of two sigma algebras and the probability distribution is a rank-one measure within the tensor product of measure spaces over those two sigma algebras.  I feel like I'm writing a paper at this point, so I really should cut myself short though.
