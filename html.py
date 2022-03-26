import re

web_document = """
<h1>Anonymous emailing</h1>
<p>
  Many web sites insist that you provide your email address
  before you can use their services, so that they can send you
  advertising. To avoid this you can use a temporary, anonymous
  email account when signing up! There are many providers of
  such accounts, each with their own email address formats,
  including:
</p>
<ul>
  <li>
    <a href="https://mailinator.com">Mailinator</a>
    whose email format lets you provide a false user name
    like <a href="mailto:xxx@mailinator.com">False Face</a>
  </li>
  <li>
    <a href="https://www.33mail.com/">33 Mail</a> which lets
    you create both the domain and user names, e.g.,
    <a href="mailto:aaa@bbb.33mail.com">The Phantom Blot</a>
  </li>
  <li>
    <a href="https://hide-your-email.com">Hide-Your-Email</a>
    which is exceptionally simple to use and allows you to
    create addresses like the following example:
    <a href="mailto:zzz@pidmail.com">The Shadow</a>
  </li>
</ul>  
<p>
  Acknowledgement: This information comes from
  <a href="https://au.pcmag.com/how-to/28205/">PC Magazine</a>.
  Call them at <a href="tel:+4755578">+47 555 78</a>
</p>
"""

print(re.findall('@.*">(.*)</a>', web_document))
