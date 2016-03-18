Title: Riding the pelican
Date: 2016-03-17
Category: misc
Tags: first, misc
Slug: first-article

Here it is: I have decided to switch my blog from Wordpress to Pelican. The question is why and actually, I don't know. I have read many posts introducing Pelican by the comparison dynamic/static blogs to explain why the latter were far superior to the former. I must say that I was not convinced by the answer. Indeed, they are faster to display... If you just want to display text. But add a twitter widget, a disqus widget, google analytics and so on, the performance starts to decrease. In addition, a dynamic blog can be edited from everywhere, as long as you have a web access; there is almost no effort required to configured it. In one or two clicks you can add the gizmo that you want to your blog.
In comparison with that, static blogs require a machine with the "compiling" environment and time to install and configure it. You can see that the advantages of static sites are not clear-cut.
Yet, I have made jump. Probably to say: yes, I can (and I suspect many coders start to write static blogs for the same reason): you belong to a small elite who is cultivating his own food.
But maybe, there is more than that. The main advantage of the method is the high level of flexibility: you can design your webpages almost as you want: you have plenty of plugins available and, if necessary, you can write your own ones. Thus, programmatically, you can define the components of your pages (text, pictures, latex, code, static Jupyter Notebooks,...) and design how they are interrelated. You do not depend anymore on the existing architecture of a CMS. But, you will say: we are static, so we lose all possibility to connect to a database and enrich our content with live feed. I am a big fan of Jupyter and I think that, in the future, users will be able to interact and calculate directly on the page. But it is not contradictory with the way taken by Pelican and others. Once again, what is static is the architecture of the page, but not what is inside: you can have widgets connected to databases or even computing kernels. This is how you have Disqus on static websites or Twitter feeds or the statistics from Google analytics.

And the last point that I like with static blogs: the source of the blog is available on [github](https://github.com/albanatita/albanatita.github.io), which means that I have no secret: you can see every details of my configuration, including both my tricks and my mistakes.
And this is something that is both frightening (no way to avoid criticism: this guy sucks at programming) and exciting (you learn by your mistakes).
So let's see how this blog will develop and if the future is as promising as expected.

As a last word, some links to the websites which helped most to install and configure [Pelican](http://blog.getpelican.com/) for this blog:
* [Drown in Genomics](http://a-slide.github.io/blog/github-pelican)
* [Futurile](http://futurile.net/resources/blogging/pelican.html)
* [Fedora Magazine](https://fedoramagazine.org/make-github-pages-blog-with-pelican/)
* [Osteel](http://blog.osteel.me/posts/2015/02/24/install-and-deploy-a-pelican-blog-using-fabric-part-1-local-environment.html)
