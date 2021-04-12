from nltk import PCFG

pcfg_rules = PCFG.fromstring(
  """
    S -> NP VP [1.0]
    NP -> Det N [1.0]
    PP -> P NP [1.0]
    VP -> 'slept' [0.2] | 'saw' NP [0.4] | 'walked' PP [0.4]
    Det -> 'the' [0.5] | 'a' [0.5]
    N -> 'man' [0.2] | 'park' [0.4] | 'dog' [0.4]
    P -> 'in' [0.5] | 'with' [0.5]
""")