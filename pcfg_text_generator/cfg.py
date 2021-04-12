from nltk import CFG

cfg_rules = CFG.fromstring(
  """
    S -> NP VP
    NP -> Det N
    PP -> P NP
    VP -> 'slept' | 'saw' NP | 'walked' PP
    Det -> 'the' | 'a'
    N -> 'man' | 'park' | 'dog'
    P -> 'in' | 'with'
""")