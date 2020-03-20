---
title: Solve POMDPs by converting them to MDPs
tags: math
---
In the [previous post]({{ site.baseurl}}{% post_url 2020-02-12-algebra-of-POMDPs %}) we used the category of stochastic relations to categorify the family of Markov decision processes (MDPs) and partially observable Markov decision processes (POMDPs) as functor categories.  That post is a pre-requesite for understanding this post.

Admittedly, all this abstraction is a different way to rediscover a known algorithm for solving POMDPs [described here](https://pomdp.org/tutorial/pomdp-solving.html)

## TL;DR
There is a faithful functor $$F: \mathrm{POMDP} \to \mathrm{MDP}$$. Solving the MDPs yields a policy for the POMDPs which maximizes the expected cumulative reward. The caveat is that the MDPs are over continous state spaces.


## Previously on "the new flesh"
We were briefly introducted to the category of stochastic relations, $$\mathrm{SRel}$$. This is a category where the objects are measureable spaces, and the morphisms are transition kernels / conditional probabilities.  That is to say, a morphism from $$\phi:X \to Y$$ is a map $$\phi: \Sigma(X) \to \Pr(Y)$$ which takes measureable sets of $$X$$ and spits our probability distributions.  Typical notation for $$\phi(E)(y)$$ would be $$\phi(y \mid E)$$ read "$$\phi$$ of $$y$$ given $$E$$). Composition in this category is given heuristically by

$$
	(\phi_1 \circ \phi_2)(z \mid x) = \int \phi_2(z \mid y ) \phi_1(y \mid z) dy.
$$

 We then found that Markov processes are given by a functor category $$\mathrm{MM} := \mathrm{SRel}^{\circlearrowleft}$$.  More generally, the same could be said for hidden Markov models (HMMs) , Markov decision processes (MDPs), and partially observable Markov decision processes (POMDPs). They are all (at least similar to) functor categories of the form $$\mathrm{SRel}^J$$ where the diagram $$J$$ takes the form
 


It's a short post and [you should read it before reading this one]({{ site.baseurl}}{% post_url 2020-02-12-algebra-of-POMDPs %}).

## Taking the "Hidden" out of Hidden Markov Models
Before diving into POMDPs, lets study their uncontrolled cousin, Hidden Markov Models. In this section we will construct a faithful functor $$F_{-H}:\mathrm{HMM} \to \mathrm{MM}$$ which sends a Hidden Markov model over a state space $$X$$ into a Markov model over a (continuous) state space $$\tilde{X}$$.  Faithfulness has the tangible consequence that the insights on the Markov model provide insights into the corresponding hidden Markov model.

### A fundamental example
Let's consider a simple HMM where the state space is $$X = \{0,1\}$$ and the observation, $$y:\{0,1\} \to \{0,1\}$$, is a random variable that tells you the correct state with probability $$p > 0.5$$, i.e. $$\Pr(y=x \mid x) = p$$. We can represent priors over $$X$$ as 2-vectors, $$(u, 1-u)$$ for $$u \in [0,1]$$, and the transition kernel $$\phi$$ as a $$2 \times 2$$ Markov matrix.

  Given a sequence of observations can you can not infer the hidden sequence states exactly.  However, you can make a probabilistic inference.  Without any knowledge or measurement, at $$t=0$$, your prior over $$X$$ ought to maximize entropy, thus we assume a uniform prior, $$\rho_0^- = (0.5, 0.5)$$. After your first measurement, $$\hat{y}_0 = 0$$ you might update this to $$\rho_0 = (p, 1-p)$$. Then the transition kernel can be applied to this prior to get $$\rho_1^- = \phi \cdot \rho_0 = (\rho_1^-[0], \rho_1^-[1])$$.  After your next measurement $$\hat{y}_1 = 1$$, you can again do a Bayesian update to get 

$$
 \rho_1 = \frac{1}{Z_1} (1-p \rho_1^-(0), p \rho_1^-[1])
$$

where $$Z_1$$ is a normalization constant. We then update again to get $$\rho_2^- = \phi \cdot \rho_1$$ and do a measurement and a Bayesian update to get $$\rho_2 $$.  Iterate this process over and over. The process that produces the sequence $$\rho_0, \rho_1, \dots, \rho_n, \dots$$ is Markovian because only the previous $$\rho$$ is used in the computation of the next one, and it's a stochastic process because the next $$\rho$$ is determined completly by the stochastic measurement $$y$$.  In otherwords we've represented the evolution of our Hidden Markov model on $$X = \{0,1\}$$ as a (unhidden) Markov model over the continous space of probability distributions $$\Pr(X)$$, which is isomorphic to the unit-interval $$[0,1]$$. We'll describe this transition more formally in what follows.

### Bayesian updates
Consider a hidden markov model $$(\phi, y) \in \mathrm{HMM}$$ where the transition kernel is $$\phi:X \to X$$ and the observation kernel $$y:X \to Y$$. We can construct the measureable set

$$
    \tilde{X} := \{ (\rho^+, \hat{y}) \in \Pr(X) \times Y \mid y[\rho^+] = \delta_{\hat{y}} \}
$$

which will serve as the state space for $$F(\phi,y)$$.[^statespace]

[^statespace]: I've not been able to determine the universal property that defines this space.  It has something to do with the graph of the map $$\sigma \circ \Pr(y) : \Pr(X) \to Y$$ given by sampling from the distribution $$y[\rho_x]$$.  I think it's the unique space such $$\pi_1:(\rho,\hat{y}) \in \tilde{X} \to \rho$$ is mono and $$\pi_2: (\rho,\hat{y}) \tilde{X} \to \hat{y} \in Y$$ is epic. But I'm really not too sure.

The process of doing a Bayesian update with respect to $$y$$ of a prior $$\rho \in \Pr(X)$$ yields a map $$\tilde{y}: \Pr(X) \to \tilde{X}$$.  Recall that a Bayesian update first means drawing a sample $$\hat{y} \sim y[\rho]$$.  Then updating the prior means computing the posterior

$$
    \rho^+(x) := \frac{1}{Z(\hat{y})} \Pr( y = \hat{y} \mid x) \rho(x)
$$

where $$Z(\hat{y}) = \int \Pr(y = \hat{y} \mid x) \rho(x) dx$$. Lets denote the map that does this Bayesian update by

$$
    \tilde{y} : \rho \in \Pr(X) \mapsto (\rho^+, \hat{y}) \in \tilde{X}.
$$

### Transition kernels
The (stochastic) transition kernel $$\phi:X \to X$$ can be lifted by the Giry monad to a (deterministic) transition kernel $$\Pr(\phi): \Pr(X) \to \Pr(X)$$. Explicitly

$$
    \Pr(\phi)[\rho](x^+) =  \int \phi(x^+ \mid x) \rho(x) dx \in \Pr(X)
$$
  
  For each $$\rho \in \Pr(X)$$. Additionally, we have the monomorphism

$$
    \tilde{i}: (\rho^+, \hat{y}) \in \tilde{X} \mapsto \rho^+ \in \Pr(X)
$$

which embeds $$\tilde{X}$$ into $$\Pr(X)$$.

### Our markov model
Using these maps, we can construct the markov model $$\tilde{\phi} := \tilde{y} \circ \phi \circ \tilde{i}: \tilde{X} \to \tilde{X}$$, which corresponds to the following sequence

 1. Take the $$\rho$$ part of the current state $$(\rho, \hat{y}) \in \tilde{X}$$.
 2. Evolve the distribution forward in time to get a new distribrution $$\Pr(\phi)[\rho]$$.
 3. Take an observation (i.e. sample $$\hat{y}^+ \sim y[\Pr(\phi)[\rho]]$$) and do a Bayesian update to get the posterior distribution $$\rho^+$$.
 4. We are now in a new state $$(\rho^+, \hat{y}^+) \in \tilde{X}$$.  Rinse and repeat.

This defines the object map of the functor $$F_{-H}$$. i.e. 

$$
	F: (\phi, y) \in \mathrm{HMM}(X,Y) \mapsto \tilde{\phi} \in \mathrm{MM}(\tilde{X})
$$

### Is this useful?
God damn you NSF-funded-sharks!!! Fine, incidentally, it might be, so I'll throw you this bloody bone.

  Let's say $$\tilde{\rho}$$ is a steady state distribution of the Markov transition kernel, $$\tilde{\phi}$$. In fact, let's assume the steady state distribution is unique.  Then we also know the steady-state behavior of the original hidden Markov model.

Explicitly, $$\tilde{\rho}$$ is a distribution over $$\tilde{X}$$.  Therefore the steady state behavior of the original hidden markov model is that the observation $$\hat{y}$$ is taken by drawing a sample $$(\hat{y}, \rho) \sim \tilde{\rho}$$.  The steady state behavior of the state is generally not observed, but instead the steady-state behavior of the beliefs of the current states is observed, and corresponds to $$\rho \in \Pr(X)$$.

### Are you sure?  It looks useless?
Admittedly, $$F_{-H}$$ is not a panacea. The resulting Markov model is over a **continuous state space**. If the original hidden Markov model has $$N$$ states, then the corresponding Markov model is over an $$N-1$$ simplex.  

A similar trade-off occurs when vieweing a non-linear stochastic differential equation on $$\mathbb{R}^n$$ as a deterministic linear ODE over $$L^1( \mathbb{R}^n)$$ by considering the Fokker-Planck equation. You could argue that this transition is useless and buys us nothing because it is "merely a change in perspective".  However, you would lose that argument. Such a sentiment is short-sighted and not supported by evidence. It's undeniable that the Fokker-Planck equation was useful in the study of SDEs. Mathematicians would have been impotent without the Fokker-Planck equation and the field of SDEs would have died on the operating table momentarily after birth. Our toolkit for linear operators is miles ahead of our toolkit for stochastic/nonlinear things, and it's been this way forever. Similarly, our toolkit for Markov processes is miles ahead of toolkit for hidden Markov models.

### A concrete insite
If $$F$$ were leveraged in an engineering application, it would probably be used in some numerical method. In that case, some sort of analytic assumption would need to be adopted or derived so that approximations of $$\tilde{\phi}$$ would be valid. For example, viewing $$\tilde{\phi}$$ as a linear operator on the space of measures, we could assume (or prove in special cases) that the specta of $$\tilde{\phi}$$ consists of $$H^k$$ subspaces. This would allow us to spectrally approximate $$\tilde{\phi}$$ as a $$n \times n$$ matrix, and we'd achieve a $$\mathcal{O}(t \cdot n^{-k})$$-ish error bound in time $$t$$. In fact, [the last thing I did before leaving the academy](https://arxiv.org/abs/1412.8369) was a building a spectral scheme like this, so this application is nearly a freebie in my mind.

### blah blah blah... useless
Allow me to direct you to somewhere more worthy of your time. [Click here](http://www.nickjr.com/paw-patrol/)

### Functorality
That link should distract the trolls for 30 minutes. We can get serious now.

So far we've only given the object map of $$F_{-H}$$. Let's consider an $$\mathrm{HMM}$$ morphism $$\alpha \in \mathrm{HMM}((\phi, y) ,\, (\phi', y'))$$ consists of two morphisms, $$\alpha_X:X \to X'$$ and $$\alpha_Y:Y \to Y'$$, where $$\alpha_X \circ \phi = \phi' \circ \alpha_X$$ and $$\alpha_Y \circ y = y' \circ \alpha_X$$. In otherwords, the following diagrams commute:

$$
\require{AMScd}
\begin{CD}
X @>\alpha_X >> X'\\
@VV \phi V @VV \phi V\\
X @> \alpha_X >> X'
\end{CD} \quad
\begin{CD}
X @>\alpha_X >> X'\\
@VV y V @VV y' V\\
Y @> \alpha_Y >> Y'
\end{CD}.
$$


 The morphism $$F(\alpha) \in \mathrm{MM}(\tilde{\phi}, \tilde{\phi}')$$, is really just a morphism $$\beta:\tilde{X} \to \tilde{X}'$$ such that $$\beta \circ \tilde{\phi} = \tilde{\phi}' \circ \beta$$. Recalling that $$\tilde{X} \subset \Pr(X) \times Y$$ it's pretty easy to guess that

$$
	F(\alpha) = \left. \left( \Pr(\alpha_X) \times \alpha_Y \right) \right|_{\tilde{X}}
$$

and if that's your guess, then good job, you've made the diagram

$$
\require{AMScd}
\begin{CD}
\tilde{X} @> F(\alpha) >> \tilde{X}'\\
@VV \phi V @VV \phi V\\
\tilde{X} @> F(\alpha) >> \tilde{X}'
\end{CD}
$$

commute!


## Taking the $$\mathrm{PO}$$ out of $$\mathrm{POMDP}$$
In this section we construct a faithful functor $$F_{-PO}:\mathrm{POMDP} \to \mathrm{MDP}$$. We bascially will use the same trick that we used to transform HMMs into MMs. If you understood the functor $$F_{-H}$$ then this section should be a cake-walk.

### The category of MDPs and POMDPs
Very quickly, an MDP consists of a space of states, $$X$$, an epimorphism $$\tau: \mathcal{A} \twoheadrightarrow X$$ which associates actions to each state[^trivial], a stochastic evolution map $$\phi: \mathcal{A} \to X$$, and finally a reward function $$r: \Gamma(\phi) \to \mathbb{R}$$, where $$\Gamma(\phi)$$ is the graph of $$\phi$$. Digramatically, an MDP looks like

![mdp]({{"assets/pomdp/mdp.svg" | absolute_url }}){:width="200em"}.

The collection of MDPs forms a category, $$\mathrm{MDP}$$ and an arrow $$\alpha:(\tau, \phi, r) \to (\tau', \phi', r')$$ consists of $$\mathrm{SRel}$$ morphisms

$$
	\alpha = \begin{Bmatrix}
		\alpha_{\mathcal{A}} : \mathcal{A} \to \mathcal{A}' \\
		\alpha_X : X \to X' \\
		\alpha_{\mathbb{R}}: \mathbb{R} \to \mathbb{R} 
	\end{Bmatrix}
$$

where $$\alpha_{\mathbb{R}}$$ is affine and orientation preserving (i.e. of the form $$ax+b$$ with $$a>0$$) and are such that 

$$
	\alpha_X \circ \tau = \tau' \circ \alpha_{\mathcal{A}} \\
	\alpha_X \circ \phi = \phi' \circ \alpha_X \\
	\alpha_{\mathbb{R}} \circ r = r' \circ \left.(\alpha_{\mathcal{A}} \times \alpha_X) \right|_{\Gamma(\phi)}
$$

[^trivial]: Typically in papers $$\mathcal{A} = X \times A$$ for some set $$A$$ and $$\tau$$ is just the projection onto $$X$$.

The goal is to find a policy $$\pi:X \hookrightarrow \mathcal{A}$$ (i.e. a section of $$\tau$$) which maximizes the cumulative reward

$$
	V^\pi = \sum_{n \geq 0} \mathbb{E}(r(\pi(x_n),x_{n+1}))
$$

where $$x_{n+1} \sim \phi(\cdot \mid x_n, a_n)$$. Adding another wrench, we typically do not know what $$r$$ and $$\phi$$ are, and so we must learn them via sampling.

Similarly a POMDP consists of a state space $$X$$, observation space $$Y$$, observable actions $$\mathcal{A}$$ and stochastic relations

$$
\tau: \mathcal{A} \twoheadrightarrow Y \\
y: X \to Y \\
\phi: X \times_Y \mathcal{A} \to X \\
r: \Gamma(\phi) \to X
$$

where $$X \times_Y \mathcal{A}$$ is the pull-back bundle of $$\tau$$ along $$y$$. Diagramatically, this means that a POMDP is a diagram of the form

![pomdp]({{"assets/pomdp/pomdp.svg" | absolute_url }}){:width="200em"}.

within $$\mathrm{SRel}$$.

Again, the goal is to find some way of choosing actions to maximize the cumulative reward without apriori knowing $$\phi$$ and $$r$$, however, we also do not observe the state. We only observe samples from $$r$$ and $$y$$ at each time-step.  Whatever answer we give it should be in the form of an $$\mathcal{A}$$ valued mapm, but it's not clear what the domain of the map should be.  Using the most recent sample from $$y$$ would be foolish, because you'd be discarding information from the history of observed $$y$$'s.[^markov]

[^markov]: You might wonder why the solution to an MDP only uses the most recently observed state (as opposed to the history).  The reason is the Markov property.  A previous $$x$$ contains less information regarding the future than the current $$x$$.  In contrast, in the POMDP case, the $$y$$'s do not satisfy a Markov property like this except in very special circumstances (e.g. like the fully observeable case).

### Setting the scene
Without throwing all the details at you just yet, we can prepare for what's coming.  $$F_{-PO}$$ is a functor whose object map looks like

$$
	F_{-PO}: \begin{Bmatrix} 
		\tau: \mathcal{A} \twoheadrightarrow Y \\
		y:X \to Y \\
		\phi: X \times_Y \mathcal{A} \to X \\
		r: \Gamma(\phi) \to X 
	\end{Bmatrix} \in \mathrm{POMDP}
	\mapsto
	\begin{Bmatrix} 
		\tilde{\tau}: \mathcal{A} \times_Y \tilde{X} \twoheadrightarrow \tilde{X} \\
		\tilde{\phi}: \mathcal{A} \times_Y \tilde{X} \to \tilde{X} \\
		\tilde{r}: \Gamma(\tilde{\phi}) \to \mathbb{R} 
	\end{Bmatrix} \in \mathrm{MDP}
$$

where

$$
	\tilde{X} = \{ (\hat{y},\rho) \in Y \times \Pr(X) \mid y[\rho] = \delta_{\hat{y}} \}
$$

The projection $$ (\hat{y}, \rho) \in \tilde{X} \mapsto \hat{y} \in Y$$ allows us to build the pull-back $$\mathcal{A} \times_Y \tilde{X}$$ which as a set looks like

$$
	\mathcal{A} \times_Y \tilde{X} = \{ (a, \hat{y}, \rho) \in \mathcal{A} \times \tilde{X} \mid \tau(a) = \hat{y} \}
$$

and is obviously a space over $$\tilde{X}$$ with epimorhpism $$\tilde{\tau}: (a, \hat{y}, \rho) \in \mathcal{A} \times_Y \tilde{X} \mapsto (\hat{y}, \rho) \in \tilde{X}$$.

So these are the spaces where all the actions take place. What's left is to describe the evolution kernel, $$\tilde{\phi}$$, and the stochastic reward, $$\tilde{r}$$.

### Leveraging our work on HMMs
Just as in the HMM case, we are in a situation where we intermittenly observe a measurement, and then need to update our priors. Through literally the same sequence of symbols, a Bayesian update is a morphism $$\tilde{y}: \Pr(X) \to \tilde{X}$$. Similarly, the transition kernel $$\phi: \mathcal{A} \times_Y X \to X$$ can be lifted to a (deterministic) kernel $$\Pr(\phi): \Pr(\mathcal{A} \times_Y X) \to \Pr(X)$$. We also have a natural embedding

$$
	i: (a,\hat{y},\rho) \in \mathcal{A} \times_Y \tilde{X} \mapsto \delta_a \otimes \rho \in \Pr( \mathcal{A} \times_Y X)
$$

So we can define the transition kernel

$$
	\tilde{\phi} := \tilde{y} \circ \Pr(\phi) \circ i : \mathcal{A} \times_Y \tilde{X} \to \tilde{X}
$$

Finally, the stochastic reward kernel $$\tilde{r}: \Gamma(\tilde{\phi}) \to \mathbb{R}$$, where $$r(a,\hat{y}, \rho)$$ is simply the process given by drawing from $$r(a,x,x^+)$$ after drawing $$x \sim \rho$$ and $$x^+ \sim \phi(a,x)$$.

### Functorality
It's just like for HMMs but with an extra map.  A morphism in POMDP, $$\alpha$$
consists of four maps

$$
	\alpha  = \begin{Bmatrix}
		\alpha_{\mathcal{A}} : \mathcal{A} \to \mathcal{A}' \\
		\alpha_X: X \to X' \\
		\alpha_Y: Y \to Y' \\
		\alpha_{\mathbb{R}} : \mathbb{R} \to \mathbb{R}
	\end{Bmatrix}
$$

such that yadda-yadda-yadda. The morphism $$F(\alpha)$$ then consists of

$$
	F(\alpha) = \begin{Bmatrix}
		(\alpha_Y \times \Pr(\alpha_X))|_{\tilde{X}}: \tilde{X} \to \tilde{X}' \\
		(\alpha_{\mathcal{A}} \times \alpha_Y \times \Pr(\alpha_X))|_{\mathcal{A} \times_Y \tilde{X}} : \mathcal{A} \times_Y \tilde{X} \to \mathcal{A}' \times_{Y'} \tilde{X}' \\
		\alpha_{\mathbb{R}} : \mathbb{R} \to \mathbb{R}
	\end{Bmatrix}
$$

** draw communcative squares**

### How is this useful?
Solving the MDPs given by the functor $$F_{-PO}$$ amounts to solving the corresponding POMDP. In particular, say

$$
	F_{-PO}: \begin{Bmatrix} 
		\tau: \mathcal{A} \twoheadrightarrow Y \\
		y:X \to Y \\
		\phi: X \times_Y \mathcal{A} \to X \\
		r: \Gamma(\phi) \to X 
	\end{Bmatrix} \in \mathrm{POMDP}
	\mapsto
	\begin{Bmatrix} 
		\tilde{\tau}: \mathcal{A} \times_Y \tilde{X} \twoheadrightarrow \tilde{X} \\
		\tilde{\phi}: \mathcal{A} \times_Y \tilde{X} \to \tilde{X} \\
		\tilde{r}: \Gamma(\tilde{\phi}) \to \mathbb{R} 
	\end{Bmatrix} \in \mathrm{MDP}.
$$

Then we can solve the MDP $$(\tilde{\tau}, \tilde{\phi}, \tilde{r})$$, which means obtaining a policy $$\tilde{\pi}: \tilde{X} \to \mathcal{A} \times_Y \tilde{X}$$, which maximizes the expected cumulative reward.  This policy is perfectly feasible to execute, as we observe a deterministic reading of $$\tilde{X}$$ after each observation, and the reading incorporates  


> Given a POMDP $$(\tau, y, \phi, r)$$ and a prior $$\rho_0 \in \Pr(X)$$ over the state space, solving $$F_{-PO}(\tau, y, \phi, r)$$ produces a policy that optimizes the expected cumulative reward of the original POMDP using only observable entities.

I'd argue that this is the Holy Grail.  Unfortunately, even if the POMDP is finite state, the MDPs that $$F_{-PO}$$ produces is infinite state.

![pomdp]({{"assets/pomdp/run_away.jpeg" | absolute_url }}){:width="300em"}.


### So it's useless?
It's true that we will not be able to solve a generic infinite state MDP. However, it's not like nothing has been gained.  In particular, if the original POMDP is finite state, then the corresponding MDP state-space takes place on an $$n$$-simplex in $$\mathbb{R}^{n}$$.  We can then apply function approximation techniques to get approximate solutions.  This is the idea behind [Least-squares policy iteration](https://www2.cs.duke.edu/research/AI/LSPI/jmlr03.pdf).[^LSPI]  Additionally, many deep reinforcement learning are designed on continuos state-spaces. For example, without reading the papers, you already know that [models that learn to play Mario and control robots are designed on continuous state spaces](https://arxiv.org/abs/1811.12560).

![mario]({{"assets/pomdp/mario.png" | absolute_url }}){:width="300em"}.

 The bottom line is that even though infinite-state MDPs are not solvable in the strict sense, they are practically solvable in many scenarios. Approximations of $$Q$$-learning over continuous spaces are executed every day. Literally driving cars in Silicon valley as you read this sentence. This is no longer pi-in-the-sky stuff.
 
## Conclusion
We've found a functor that maps a POMDP to an MDP, and solving the MDP effectively solves the POMDP as well. I doubt this solution has not already been discovered (perhaps minus the fancy math) because in the case where $$\mathcal{A} = A \times X$$ where $$A$$ and $$X$$ are finite sets, the resulting algorithm is not so hard to come up with. However, I've not been able to find a paper to cite, and many of the POMDP papers go down some pretty silly rabbit holes that make it impossible to get a solution as good as the one pointed to by $$F_{-PO}$$.

[^LSPI]: Lagoudakis, Parr, "Least-Squares Policy Iteration", Journal of Machine Learning Research 4 (2003) 1107-1149


