#!/usr/bin/env python3.4

import pystache

template = open("govuk_template_mustache/views/layouts/govuk_template.html").read()

params = {
    "pageTitle": "Civil Service Survey",
    "assetPath": "govuk_template_mustache/assets/",
    "content": """
        <div id="wrapper">
        <main id="content">
       <p> This is the content :)</p>
       </main>
       </div>
    """,

    "headerClass": "with-proposition",
    "propositionHeader": """
<div class="header-proposition">
  <div class="content">
    <nav id="proposition-menu" role="navigation">
      <a href="/" id="proposition-name">Civil Service Survey</a>
      <span class="alpha-tag">Alpha</span>
      <a href="#proposition-links" class="js-header-toggle menu">Menu</a>
      <ul id="proposition-links">
        <li><a href="#">Login</a></li>
        <li><a href="#">About</a></li>
      </ul>
    </nav>
  </div>
</div>
""",

  "cookieMessage": """
  <p>GOV.UK uses cookies to make the site simpler. <a href="http://gov.uk/help/cookies">Find out more about cookies</a></p>
  """
}

html = pystache.render(template, params)
outfile = open("out.html", "w")
outfile.write(html)

