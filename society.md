---
layout: page
permalink: /society/
title: Society
---
{% for post in site.tags.society %}
 <li><span>{{ post.date | date_to_string }}</span> &nbsp; <a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}
