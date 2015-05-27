import sys
if sys.version_info < (3,):
    range = xrange

"""
Mutates `properties` to apply fuzzy matches
"""
def apply_fuzzies(properties, short, prop, options):
    def iterate(property):
        for key in fuzzify(property):
            if not key in properties:
                properties[key] = properties[short]

    # Create them for the property
    # ("box-sizing" => "boxsizing", "boxsizi", "boxsi", "boxs", "box"...)
    iterate(prop.replace('-', ''))
    iterate(prop)

    # Also add aliases ("bgcolor" => "bgcolo", "bgcol", "bgco", "bgc" ...)
    # This kinda sucks, because aliases should have lowest priority.
    if options and "alias" in options:
        [iterate(alias) for alias in options["alias"]]

"""
Returns a generator with fuzzy matches for a given string.

>>> for s in fuzzify("border"):
>>>     print s
"b", "bo", "bor", "bord", "borde"
"""
def fuzzify(str):
    if str:
        for i in range(1, len(str)+1):
            yield str[0:i]
