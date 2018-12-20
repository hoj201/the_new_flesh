---
layout: post
title: Probabilistic notation is the worst (and how to fix it)
comments: true
tags: math
---

![dice](http://learnersdictionary.com/media/ld/images/legacy_print_images/dice.gif)

## Prologue
This will be the first in a 3-part series where I grapple with the foundations of probability theory.
**Caution**: If you find commutative diagrams to be impenetrable, then you might not get much out of this series.

## The status quo
Does this sentence make sense?
> Given functions $$f:\mathbb{C} \to \mathbb{R}^3$$ and
$$g: \mathbb{C} \to \mathbb{R}$$, find the numbers such that $$g(f) > 0$$.

Rhetorical question.  It's nonsense.  What does $$g(f)$$ even mean!?
$$g$$ is a map which eats complex numbers, yet we are feeding it $$f$$.  WTF.

Now consider the following
> Given the probability space $$(\Omega, \mathcal{F}, \Pr)$$ and the random
variable $$X:\Omega \to \mathbb{R}$$, find the numbers such that $$\Pr(X) > 0$$.

Okay. So that sentence made sense, right?
The sentence is commanding that we find all
the numbers for which $$X$$ has a positive probability of hitting.

What is weird, to me at least, is that these two text boxes are virtually identical.
At least at the level of mathematical abstractions.
We've merely substituted $$f$$ with $$\Pr$$ and $$g$$ with $$X$$.
Moreover, the same issue arises.  $$\Pr$$ is a function of $$\mathcal{F}$$, so
how are we reading it a real valued map, $$X$$?

I think the reason we understand the second box, but not the first is because
the second box has contextual clues which hint at the intended meaning.
Probability theory relies heavily on contextual clues to compensate
for awful notation.

In terms of communications theory, the signal is highly redundant and therefore
robust to noise.
What sucks, is that all the noise is in the mathematical ink.  This is the
the opposite of where it should be.  If anything, the prose should be conveying
high level description, and the math should be the hyper-precise component which
fills in the details.

![keanu](http://cdn.empireonline.com/jpg/80/0/0/1000/563/0/north/0/0/0/0/0/t/films/1813/images/uprkH1mXqPZQXyl19VShgw9YMTf.jpg){:width="400em"}

**Devil's advocate**: *If we understand the second box, then what's the problem?
The point of words and notation is to convey syntax, by hook or crook.*

Well Keanu Reeves, you do have a point.  And I actually agree in principle.
However, all to often this sloppy notation actually catapults the syntax into a fog.
When I was first presented random-variables $$X,Y$$, and then asked to consider
the posterior distribution $$\Pr(X \mid Y)$$, This is roughly the conversation
I had with myself.

> Is this actually a distribution?  Over what space, is it $$X$$?
Yeah... $$X$$ makes sense.  But it has two arguments $$X$$ and $$Y$$.  Wait...
are $$X$$ and $$Y$$ arguments,  I thought they were random-variables.
Oh, I get it!  This is just short-hand notation for the probability distribution
over $$X$$, once we know what $$Y$$ is....  Wait??  So it is a distribution.
- me being confused (500 BC)

Bottom line, Keanu, I think you should stop advocating for Satan.

## The problem

The first issue is really about the nature of the expression "$$ \Pr( \cdot)$$".
Is it a function or not?  Your textbook will say that it is a function.
Unfortunately, it's the only "function" in the discipline of mathematics whose domain appears to change from one line of text to the next.  First it's $$ \Pr(A)$$, then $$ \Pr(X)$$ or worse $$ \Pr(x)$$ (which is a notational abuse of $$ \Pr(X=x)$$, which is incidentally pretty good notation for reasons which will be described).  Finally, you run into $$ \Pr(X,Y)$$?  A function has a single domain!  This function takes $$X$$'s, booleans like $$X = x$$, and then it takes in $$X$$ and $$Y$$ at the same time.

## Fixes

### Fix 1: Stop lying

Let's get one thing straight.  $$ \Pr$$ is a function.  I'm compelled to say this because the following sentiment is the current state of pedagogy:

>$$ \Pr$$ should really not be taken so seriously.  It really should be seen as casual short-hand for "probability of"
- Anonymous friend of mine who teaches statistics

This trick is pretty useful for getting through the textbook without pulling your hair out. Perhaps this is because this is how the textbook writer thinks of $$ \Pr$$.  Nonetheless, this approach only works because it provides comfort in a convenient lie.  If $$ (\Omega, \mathcal{F}, \Pr )$$ is a probability space, then $$ \Pr$$ is a function from the $$ \sigma$$-algebra, $$ \mathcal{F}$$, into the unit interval $$ [0,1]$$.  Stop lying.  Lying sucks.

### Fix 2: Stop sucking (start pushing)

If $$ (\Omega, \mathcal{F}, \Pr)$$ is a probability space, and $$ X:\Omega \to \mathbb{R}$$ is a random variable, then the expression $$ \Pr(X)$$ makes no sense (unless $$\mathcal{F}$$ is the Borel $$ \sigma$$-algebra on $$\mathbb{R}$$).  It's only upon looking at the examples that it becomes clear what is really meant is the push-forward. The map $$X$$ transforms the probability space $$ (\Omega, \mathcal{F}, \Pr)$$ into a new one, $$ ( X(\Omega), X( \mathcal{F}), X_* \Pr)$$. Here $$ X(\Omega) \subset \mathbb{R}$$ is just the image of $$X$$, $$  X( \mathcal{F}) := \{ X(A) \mid A \in \mathcal{F} \}$$, and $$ X_* \Pr$$ is the unique probability density function on $$ X(\mathcal{F})$$ defined by $$ X_*\Pr( X(B) ) = \Pr(B)$$.  We call $$ X_* \Pr$$ the push-forward of $$\Pr$$ by $$ X$$.  In measure theory, this notation is standard (see push-forward measure).  I don't see a compelling reason to for probability theory and statistics to resist it.

Just to be clear, $$ X_*\Pr$$ is a probability function on $$\mathbb{R}$$.  This means that $$X_*\Pr$$ takes measurable subsets of $$\mathbb{R}$$ and outputs real numbers between 0 and 1.

### Joint probabilities

In the case of two random variables on the same probability space,
$$X, Y : \Omega \to \mathbb{R}$$. The joint probability "$$\Pr(X,Y)$$"
is a push-forward as well.
Consider the random variable $$Z=X \times Y : \Omega \to \mathbb{R}^2$$.
Then the joint probability is $$Z_* \Pr$$.
No need to obfuscate when it's only a few extra pen-strokes.

## Fix 3: Say what you mean

Typically, this use of lower-case for a "realization" of a random variable is just a sloppy way to avoid dealing with the fact that $$ X$$ is a function from one space to another.  However, writing $$ \Pr(x)$$ makes no sense when you've not defined $$ x$$.  Calling it a "realization" does not define it.  All you get is an alias to an undefined symbol.  The correct expression is $$ \Pr(X^{-1}(x))$$ (recall, $$X$$, is a random variable, so it's pre-images are members of $$\mathcal{F}$$, which is the domain of $$ \Pr$$).  However, I can see a good defense for writing $$ \Pr(X = x)$$ instead of $$\Pr(X^{-1}(x))$$.  It's customary in the rest of mathematics to write "$$ f(x) = 0$$" as a short-hand for the set $$\{x \mid f(x)=0 \}$$.  The expression $$ \Pr( X=x)$$ is consistent with this standard.

Similarly, I think $$ \Pr(X > x)$$ is a pretty good replacement for the more verbose $$\Pr( X^{-1}( \{ x' \mid x' > x \} )$$.  Nonetheless, it's good to be aware you're making these abuses.
Such short-hands should be deliberate, not incidental or subconscious.
Math without precision is basically really bad poetry, (i.e. unstructured BS).

## Fix 4: The nuclear option

This last fix is probably a bad idea, but it's my favorite...  It's the best idea.
In fact I'm going to dedicate a section to it.

---

# The nuclear option

![strangelove](http://i.onionstatic.com/avclub/5865/19/16x9/960.jpg)
*"Dr Strangelove or: How I Learned to Stop Worrying and Love the Bomb" (1964)*

I think reconsidering the foundations is worthwhile.
Recall, a [probability space](https://en.wikipedia.org/wiki/Probability_space)
is a triple $$(\Omega, \mathcal{F}, \Pr)$$ where $$\Omega$$ is a set,
$$\mathcal{F} \subset 2^\Omega$$, is a [$$\sigma$$-algebra](https://en.wikipedia.org/wiki/Sigma-algebra)
and $$\Pr: \mathcal{F} \to [0,1]$$ is a probability measure.
Lastly, we should note that a measureable map $$X:\bar{\Omega} \to \Omega$$
is nothing but a $$\sigma$$-algebra morphism.

When I put my algebra hat on, the following perturbs me.
A measureable map, $$f:(\bar{\Omega},\mathcal{E}) \to (\Omega,\mathcal{F})$$,
ought to transform the probability space $$(\Omega, \mathcal{F}, \Pr)$$
into a probability space over the $$\sigma$$-algebra $$(\Omega, \mathcal{E})$$.
However, it is not generally the case that the natural candidate
$$f^{\ast}\Pr := \Pr \circ f$$, is a probability distribution.

For example, let $$A \in \mathcal{F}$$ (i.e. a measureable subset of $$\Omega$$),
then we can consider the map $$i_A: A \to \Omega$$, which then lifts to an obvious
$$\sigma$$-algebra morphism, embedding the $$\sigma$$-algebra $$(A, A \cap \mathcal{F})$$
into $$(\Omega,\mathcal{F})$$.
However, the function $$\Pr \circ i_A$$ is not a probability distribution on
$$\mathcal{F}$$ because $$(\Pr \circ i_A)(A) = \Pr(A) \neq 1$$  (at least not generally speaking).
It's too bad.  I really wanted the pull-back to be the posterior $$\Pr(B \mid A)$$.
(For those in the know, my gripe is that probability densities, defined in this way,
do not form a category.)

So what to do...  what to do...

Let's just redefine what a probability measure is, so that it automagically normalizes itself.
To begin, let's formalize this normalization business.

Given two measures, $$\mu_1, \mu_2$$ we will say they are probabilistically equivalent
if $$\mu_1 = \lambda \cdot \mu_2$$ for some scalar $$\lambda > 0$$.
In words, two measures are probabilistically equivalent if they are histograms of the same probability distribution.
Noting that a single probability distribution has an entire equivalence class of measures associated with it, we can turn this thinking on it's head[^1] and **define a probability distribution as an equivalence class**.

What exactly are these equivalent classes?
They are simply rays contained within the space of measures.
Recall, a ray of a vector-space (or a cone in this case) is just a semi-infinite line-segment
([wikipedia link](https://en.wikipedia.org/wiki/Line_(geometry)#Ray)).
There is a natural map from any vector-space to the space of rays through the origin
(for each non-zero vector, just take the ray through the origin which passes through it).
The reason this ray business is relevant is because of the way rays transform.
Transforming one ray into another has no effect on its "size", an notion which is not defined.
They are purely directional entities, and there is never a need to take a (possibly infinite)
norm for the sake of normalization.
So we arrive at the following re-definition of a probability measure.

> **Definition:** Let $$(\Omega, \mathcal{F})$$ be a $$\sigma$$-algebra.
A *neo-probability* is a ray within $$\mathcal{M}(\Omega, \mathcal{F})$$, the
space of measures.

Okay, I realize that definition might look weird ([unless you're into quantum stuff, maybe](https://en.wikipedia.org/wiki/Density_matrix)).


![bad idea](http://gph.to/2s9h34G){: .center-image}
{::comment}
![bomb](https://media.giphy.com/media/oe33xf3B50fsc/giphy.gif)
{:/comment}

First, just to check we aren't leaving our sanity behind,
I'll tie this new definition to the traditional definition.
Given a traditional probability
space $$(\Omega, \mathcal{F}, \Pr)$$ the corresponding ray is simply given by
$$\pi(\Pr)$$, where $$\pi : \mathcal{M}(\Omega) \backslash \{0\} \to {\rm Ray}(\mathcal{M}(\Omega ))$$
is the quotient map.
In other words, the rays we are concerned with are exactly the rays given by the traditional probability density, when viewed as elements of $$\mathcal{M}$$.

Now let's see how things behave under the embedding $$i_A$$.
Note that $$i_A$$ acts naturally on $$\mathcal{M}(\Omega)$$ by pull-back,
and we can naturally project this into a map on the space of rays, via the quotient
projection, $$\pi$$, ala the commutative diagram:

$$\require{AMScd}
\begin{CD}
  \mathcal{M}(\Omega) @>{i_A^{\ast}}>> \mathcal{M}(\Omega) \\
  @VV{\pi}V @VV{\pi}V \\
  {\rm Ray}(\mathcal{M}(\Omega)) @>{\pi_{\ast}(i_A^{\ast})}>> {\rm Ray}(\mathcal{M}(\Omega))
\end{CD}.
$$

In particular, given a probability, $$\Pr$$, over $$\Omega$$,
the ray in the bottom right corner of the diagram is that of the "posterior"
$$\Pr( \cdot \mid A)$$.
In other words, conditional probabilities arise naturally (via the restriction maps)
when we use this new definition!

### Similar findings
 - Marginals are push-forwards on cartesian products.
 - Intersection of measureable sets, "$$\cap$$", is a $$\sigma$$-algebra morphism.
 - Posteriors are arrows of a category and Baye's theorem is nearly a tautalogy (this is part 3).

okay, I can see your face.  I'll stop.  Hope you guys check out [part II]({{ site.baseurl }}{% post_url 2018-01-27-probability_p2 %}).

### Footnotes:
[^1]: In my opinion, this is actually putting our feet on the ground.  However, I understand that it might not feel natural if you've spent your life walking on your hands.
