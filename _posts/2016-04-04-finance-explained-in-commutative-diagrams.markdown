---
author: hoj201
comments: true
date: 2016-04-04 00:19:00+00:00
layout: post
link: https://hoj201.wordpress.com/2016/04/03/finance-explained-in-commutative-diagrams/
slug: finance-explained-in-commutative-diagrams
title: Finance explained in commutative diagrams
wordpress_id: 924
tags: math economics
---

## Preface
This is actually a repost from my old blog [link](https://hoj201.wordpress.com/2016/04/03/finance-explained-in-commutative-diagrams/). I'm reposting it because I hope to write the sequel soon.

## Introduction
The intended audience for this post is people who want to see finance and diagram chasing in the same location (i.e. nobody?). [My last entry](https://hoj201.wordpress.com/2016/01/17/a-mathematical-model-of-stuff-i-read-in-the-new-jim-crow/) infused the hot topic of racial injustice in America with the excitement of a multiplication table. Well, I am back again, and determined to lose the rest of my readership.

![scrooge](https://hoj201.files.wordpress.com/2016/03/scrooge.jpg)

## The no-arbitrage principle in diagram form

The no-arbitrage principle is just what the name suggests.

> **The classical no-arbitrage principle:**
	There is no such thing as a profitable risk-free contract.


A contract is nothing but an agreement to exchange one commodity for another (e.g. "$3 for a pound of apples" or "wealth in exchange for your soul").
Given two commodities $$x$$ and $$y$$, we can represent a contract, $$a$$, as an arrow $$a:x \to y$$. In certain cases we can compose contracts. For example, the contract `$3 for a pound of apples` can be composed with the contract `wealth in exchange for your soul` to yield the contract `a bunch of apples in exchange for your soul`. Useful right! ... right? ... ( ... Shut up.)

![apple](https://hoj201.files.wordpress.com/2016/03/apple.png?w=300) "Snow White and the Seven Dwarfs" (1937)

More formally, given contracts $$a:x \to y$$ and $$b:y \to z$$, there is another contract $$c = b \circ a$$ which sends $$x \to z$$. When you sign a contract, you are traversing one of these arrows. When you issue a contract, you are going the opposite direction of the corresponding arrow. An arbitrage contract is basically a contract such as `$3 for $2`. Obviously, you would not want to sign this contract.  The person who issues you that contract is being a jerk.



Typically, the manifestation of an arbitrage contract is not so obvious.
For example, say $$ a$$ trades one orange for two apples and $$b$$ trades one apple for two kiwis. Then $$b \circ a$$ is a contract which trades one apple for four kiwis.
Additionally, let $$c$$ be a contract which trades one apple for three kiwis.
Then an arbitrage contract, $$d$$, of the form `4 kiwis for 3 kiwis` will make this diagram commute

![arbitrage](https://hoj201.files.wordpress.com/2016/03/arbitrage.png)

The no arbitrage principle assumes the market is so competitive that contracts like $$ d$$ are impossible, or that $$ d$$ can only trade `1 kiwi for 1 kiwi`, which would imply $$c = b \circ a$$. Another way to say this is:


>**The categorical no-arbitrage principle:**
The collection of all contracts forms a commutative diagram and the only contract from $$ x$$ to itself is a fair one.


Both these versions of the no-arbitrage principle are equivalent. However, they feel quite different. The categorical no-arbitrage principle might seem needlessly abstract. Does it make anything easier?


## An easy derivation of a future exchange rate


Consider this basic exercise:


>Q: The Fed has set the interest rate at $$ R_\$ $$.
The interest rate at the People's Bank of China is $$ R_\yen$$.
If the current exchange rate for US Dollars to Yuan is $$ q$$
then what do you expect the exchange rate to be next year?


Let us denote the exchange rate next year by $$ q_{\rm future}$$. An interest rate is nothing but a contract that exchanges present dollars for future dollars. Secondly, an exchange rate is nothing but a contract from dollars to yuan or vise-versa. This gives us the diagram:

![future](https://hoj201.files.wordpress.com/2016/03/future.png)
By the categorical no-arbitrage principle this diagram must commute. That is to say $$ q_{\rm future} (1+R_\$) = (1+R_{\yen}) q,$$ which implies $$ q_{\rm future} = q (1 + R_\yen)(1+R_\$)^{-1}.$$ Great scott!  We're done!

![back_to_the_future](https://hoj201.files.wordpress.com/2016/03/back_to_the_future.jpg) Back to the Future (1985)

Just to check our work, lets see what sort of derivation is written in a published and widely used mathematical finance text.


>Suppose $$ q_{future} > q \frac{1 + R_Y}{1+ R_\$}$$.
Then at time $$ t=0$$ borrow $$ q$$ (in USD); buy one RMB; enter into a short forward contract with forward price $$ q_{future}$$ with delivery date one year from now.
The resulting portfolio consists of RMB, a risk-free position, and a short forward contract with forward price $$ q_{future}$$...


Meh... never mind. This proof goes on like this for a full page! In summary, they derive $$ q_{\rm future}$$ using proof by contradiction. They assumes $$ q_{\rm future} > q (1 + R_Y)(1+ R_\$)$$ and find an arbitrage.  This contradict the classical no arbitrage principle, and thus $$ q_{\rm future} \le q (1 + R_Y)(1+ R_\$)^{-1}$$. Then they assume $$ q_{\rm future} < q \frac{1 + R_Y}{1+ R_\$}$$ and find another arbitrage contract. Personally, I think our new derivation is easier.

Admittedly, this criticism is more a matter of preference. People who are more comfortable with "real" things probably don't like the abstraction of these arrows and might consider our derivation more difficult. I really like this stuff, but claiming superiority would be hypocritical. Speaking of which...

## A fun example of hypocrisy
We have all heard some variant of *"China's devaluation of the Yuan makes it difficult for Americas producers to compete."* Why?

![pbc](https://hoj201.files.wordpress.com/2016/03/pbc.jpg)

There's a good chance you know why. Sorry if this seems patronizing. Just humor me. Lets draw the diagram of contracts. Lets say the price of an apple in china is $$p_\yen$$ in Yuan.
The exchange rate from US Dollars to RMB Yuans is $$q_{\rm money}$$. Implicitly, there exists a contract which exchanges a US apple for a Chinese apple. Let us say this exchange rate is $$ q_{\rm apple}$$.

![currency_manipulation](https://hoj201.files.wordpress.com/2016/03/currency_manipulation.png)
If this diagram commutes then $$q_{\rm apple} = p_\yen \circ q_{\rm money} \circ p_\$^{-1}$$. This means $$q_{\rm apple}$$ rises when $$q_{\rm money}$$ rises.
Which is to say that Chinese apples will be cheaper.

Can the US do anything in response. Ideally, without manipulating the value of the dollar, because that would be hypocritical. Well, we can re-arrange this commutative diagram by reversing a few of these arrows to get an equivalent diagram:
![apple_manipulation](https://hoj201.files.wordpress.com/2016/03/apple_manipulation.png)
The US can increase $$ q_{\rm apple}^{-1}$$ by placing a tariff. By the same argument, this will increase $$ q_{\rm money}^{-1}$$. Which means $$ q_{\rm money}$$ would decreases. This is exactly what China just did, but with currency instead of apples. Creating tariffs is just currency manipulation by another name.  One of the things I like about this diagram-chasing business is how well it illustrates such equivalences.


## Long = short


If the price of the stock today is $$ p$$, while the price tomorrow is $$ p_{\rm future}$$, and the interest rate of some risk-free asset (like a bond) is $$ r$$,
then in an arbitrage-free universe the following diagram should commute.

![middle](https://hoj201.files.wordpress.com/2016/03/middle.png)

However, when you know that the price of the stock rises faster that than the interest rate, the diagram will fail to commute and an arbitrage opportunity will arise. Remember that stupid contract that exchanges 4 kiwis for 3? The one that only a jerk would issue?  You can be that jerk!!!

![gordon_gekko](https://hoj201.files.wordpress.com/2016/03/gordon_gekko.jpeg) "Wall Street" (1987)

Taking advantage of these opportunities is what makes markets work, so don't feel too bad about this.  Anyway, this arbitrage opportunity yields the following commutative diagram where the arbitrage contract, $$a$$, is highlighted in red

![long](https://hoj201.files.wordpress.com/2016/03/long.png)

Basically $$a$$ trades future dollars for a smaller amount of future dollars. You want to issue $$a$$, you do not want to sign such a contract. Issuing $$a$$ is equivalent to going the opposite direction of $$a$$, i.e. $$a^{-1}$$. As this diagram commutes, we see that  $$a^{-1} = p_{\rm tommorrow}^{-1} \circ \text{wait} \circ p \circ (1+r)^{-1}$$. In words this means that we issue a bond (this is the $$(1+r)^{-1}$$ term)
then we buy the stock ($$p$$), then we wait, then we sell the stock ($$p_{\rm future}^{-1}$$). Congratulations, if you've done this you've basically issued $$ a$$ to some person (sorry person).

What about going short? All you do is swap the role of "$" and "Stock: to get this diagram
![short](https://hoj201.files.wordpress.com/2016/03/short.png)
Now you do the same thing as before. The only difference is that Stocks and bonds have the roles swapped. For example, the first step is borrowing a stock as opposed to borrowing cash. However, this shows that going short on a stock is conceptually identical to going long on the US Dollar.




## The end


To end, let's do a thought experiment.  We are basically viewing the space of transaction as an undirected graph.  Once an arbitrage is present, this becomes a directed graph.  In the world of directed graphs, there is the notion of a sink. What would this look like in the market? It would be an entity which you would trade for, but you would never trade back. A black hole in the space of investment products. An investment which everybody agrees would rise in price faster than competing investment products. Perhaps an evil sentient computer, at a hedge fund in New Jersey, that wanted to destroy mankind could try to make such an investment.  Anyway, that's the end.

![Ghost in the Shell.jpg](https://hoj201.files.wordpress.com/2016/03/ghost-in-the-shell.jpg) "Ghost in the Shell" (1995)




## Addendum:


One could say that "short" is dual to "long". But then I should probably explain what I mean by "dual". I had to cut that section.  In fact, a lot of things were cut.  There was just too much math. Here's a list of some things that were cut.




  * Portfolio theory results from applying the distribution functor to our discussion.


  * There is a functor which we could call `wait` which sends present commodities into the commodities of tomorrow. The adjoint of this functor yields the set of futures contracts.


  * I think the notion of "inherent value" can be viewed as both a limit / co-limit.


In the unlikely event that this post is a hit, I'd be happy to do a follow up, but I would need positive feedback to warrant it.
