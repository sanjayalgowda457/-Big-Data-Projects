"""
    This function checks if the input 'silver' is None (indicating missing data) and returns 0 in such cases.
    If the input contains a value, it returns that value unchanged. The function ensures that the output
    is always an integer, thus making the dataset consistent for fields that expect numerical values.
"""
@outputSchema("silver:int")
def fill_missing(silver):
    if silver is None:
        return 0
    return silver
