'''
    Provides the template for the tooltips.
'''


def get_bubble_hover_template():
    '''
        Sets the template for the hover tooltips.
        
        Contains four labels, followed by their corresponding
        value and units where appropriate, separated by a
        colon : country, population, GDP and CO2 emissions.

        The labels' font is bold and the values are normal weight

        returns:
            The content of the tooltip
    '''
    return(
    '<span style="font-family:Roboto Slab"><b>Country :</b></span> '
    '<span style="font-family:Roboto">%{customdata[0]}</span><br>'
    '<span style="font-family:Roboto Slab"><b>Population :</b></span> '
    '<span style="font-family:Roboto">%{customdata[1]}</span><br>'
    '<span style="font-family:Roboto Slab"><b>GDP :</b></span> '
    '<span style="font-family:Roboto">%{x} $ (USD)</span><br>'
    '<span style="font-family:Roboto Slab"><b>CO2 emissions: </b></span> '
    '<span style="font-family:Roboto">%{y} metric tonnes</span>'
    '<extra></extra>')
    
