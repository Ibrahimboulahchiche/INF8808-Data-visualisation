'''
    This file contains the functions to call when
    a click is detected on the map, depending on the context
'''
import dash_html_components as html
import plotly.express as px


def no_clicks(style):
    '''
        Deals with the case where the map was not clicked

        Args:
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    return None, None, None, {'visibility': 'hidden'}


def map_base_clicked(title, mode, theme, style):
    '''
        Deals with the case where the map base is
        clicked (but not a marker)

        Args:
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    if style and style.get('visibility') == 'visible':
        return title, mode, theme, style
    else:
        return None, None, None, {'visibility': 'hidden'}


def map_marker_clicked(figure, curve, point, title, mode, theme, style): # noqa : E501 pylint: disable=unused-argument too-many-arguments line-too-long
    '''
        Deals with the case where a marker is clicked

        Args:
            figure: The current figure
            curve: The index of the curve containing the clicked marker
            point: The index of the clicked marker
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    data = figure['data'][curve]['customdata'][point]
    nom_projet = data[0]
    mode_implantation = data[1]
    objectif_thematique = data[2]
    
    colors = px.colors.qualitative.Plotly
    color = colors[(curve - 1) % len(colors)]
    
    title = html.Span(nom_projet, style={'color': color})
    mode = mode_implantation
    if objectif_thematique:
        print(objectif_thematique, flush=True)
        themes_list = objectif_thematique.split('\n')
        theme = html.Div([
            html.Span('Thématique :'),
            html.Ul([html.Li(t) for t in themes_list])
        ])
    else:
        theme = None
    style = {'visibility': 'visible', 'border': '1px solid black', 'padding': '10px'}
    
    return title, mode, theme, style
